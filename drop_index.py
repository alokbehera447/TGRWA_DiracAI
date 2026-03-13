#!/usr/bin/env python
"""
Drop the conflicting index that's blocking the migration.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from django.db import connection

def drop_index():
    """Drop the conflicting index."""
    index_name = 'account_service_slug_9ac1401c_like'
    
    with connection.cursor() as cursor:
        try:
            # Drop the index
            cursor.execute(f"DROP INDEX IF EXISTS {index_name};")
            print(f"✓ Successfully dropped index '{index_name}'")
            
            # List all indexes on account_service to verify
            cursor.execute("""
                SELECT indexname FROM pg_indexes 
                WHERE tablename = 'account_service'
                ORDER BY indexname;
            """)
            indexes = cursor.fetchall()
            print("\nRemaining indexes on account_service:")
            for idx in indexes:
                print(f"  - {idx[0]}")
                
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    return True

if __name__ == '__main__':
    try:
        if drop_index():
            print("\n✓ Index cleanup complete. Ready to run migration.")
            sys.exit(0)
        else:
            sys.exit(1)
    except Exception as e:
        print(f"✗ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
