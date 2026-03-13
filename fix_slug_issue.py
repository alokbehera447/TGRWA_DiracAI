#!/usr/bin/env python
"""
Helper script to fix duplicate empty slugs and drop the conflicting index.
Run this from the Django project root with the virtual environment activated:
    python fix_slug_issue.py
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from django.db import connection
from django.utils.text import slugify
from account.models import Service


def fix_empty_slugs():
    """Find and fix services with empty or null slugs."""
    print("\n=== Fixing Empty Slugs ===")
    
    qs = Service.objects.filter(slug='') | Service.objects.filter(slug__isnull=True)
    count = qs.count()
    
    if count == 0:
        print("✓ No empty or null slugs found.")
        return True
    
    print(f"Found {count} service(s) with empty/null slug")
    
    for s in qs:
        # Generate slug from title
        base = slugify(getattr(s, 'title', '') or 'service')[:240]
        if not base:
            base = 'service'
        
        candidate = base
        counter = 1
        
        # Ensure uniqueness
        while Service.objects.filter(slug=candidate).exclude(pk=s.pk).exists():
            candidate = f"{base[:235]}-{counter}"
            counter += 1
        
        s.slug = candidate
        s.save(update_fields=['slug'])
        print(f"  ✓ Service {s.id} ('{s.title}') → slug='{s.slug}'")
    
    print(f"✓ Fixed {count} service(s)")
    return True


def drop_conflicting_index():
    """Drop the index left behind by the failed migration."""
    print("\n=== Dropping Conflicting Index ===")
    
    index_name = 'account_service_slug_9ac1401c_like'
    
    with connection.cursor() as cursor:
        try:
            cursor.execute(f"DROP INDEX IF EXISTS {index_name};")
            print(f"✓ Dropped index '{index_name}'")
        except Exception as e:
            print(f"⚠ Error dropping index: {e}")
            return False
    
    return True


def verify_no_duplicates():
    """Verify no empty slugs remain."""
    print("\n=== Verification ===")
    
    empty_count = Service.objects.filter(slug='').count()
    print(f"Empty slugs remaining: {empty_count}")
    
    if empty_count > 0:
        print("✗ Still have empty slugs!")
        return False
    
    print("✓ No empty slugs")
    return True


if __name__ == '__main__':
    try:
        if not fix_empty_slugs():
            sys.exit(1)
        
        if not drop_conflicting_index():
            print("⚠ Failed to drop index, but continuing...")
        
        if not verify_no_duplicates():
            sys.exit(1)
        
        print("\n" + "="*50)
        print("✓ Ready to re-run migration!")
        print("   Run: python manage.py migrate account")
        print("="*50 + "\n")
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
