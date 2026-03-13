#!/usr/bin/env python
"""
Thorough cleanup of all indexes on account_service table.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from django.db import connection

def list_and_drop_indexes():
    """List all indexes on account_service and drop the problematic ones."""
    
    with connection.cursor() as cursor:
        # List all indexes
        cursor.execute("""
            SELECT indexname, indexdef FROM pg_indexes 
            WHERE tablename = 'account_service'
            ORDER BY indexname;
        """)
        
        print("Current indexes on account_service:")
        indexes = cursor.fetchall()
        for name, definition in indexes:
            print(f"  - {name}")
            print(f"    {definition}\n")
        
        # Drop any slug-related indexes (except the primary key)
        drop_candidates = [
            'account_service_slug_9ac1401c_like',
            'account_service_slug_key',
            'account_service_slug_idx',
        ]
        
        print("\nDropping slug-related indexes...")
        for index_name in drop_candidates:
            try:
                cursor.execute(f"DROP INDEX IF EXISTS {index_name} CASCADE;")
                print(f"  ✓ Dropped '{index_name}'")
            except Exception as e:
                print(f"  ⚠ Could not drop '{index_name}': {e}")
        
        # Also try to drop any constraints on the slug column
        print("\nDropping slug-related constraints...")
        try:
            cursor.execute(f"ALTER TABLE account_service DROP CONSTRAINT IF EXISTS account_service_slug_key CASCADE;")
            print(f"  ✓ Dropped constraint 'account_service_slug_key'")
        except Exception as e:
            print(f"  ⚠ Could not drop constraint: {e}")
        
        # Verify what's left
        cursor.execute("""
            SELECT indexname FROM pg_indexes 
            WHERE tablename = 'account_service'
            ORDER BY indexname;
        """)
        
        print("\nRemaining indexes after cleanup:")
        remaining = cursor.fetchall()
        for idx in remaining:
            print(f"  - {idx[0]}")
        
        # Also check for constraints
        cursor.execute("""
            SELECT constraint_name, constraint_type
            FROM information_schema.table_constraints 
            WHERE table_name = 'account_service'
            ORDER BY constraint_name;
        """)
        
        print("\nConstraints on account_service:")
        constraints = cursor.fetchall()
        for name, ctype in constraints:
            print(f"  - {name} ({ctype})")

if __name__ == '__main__':
    try:
        list_and_drop_indexes()
        print("\n✓ Cleanup complete.")
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
