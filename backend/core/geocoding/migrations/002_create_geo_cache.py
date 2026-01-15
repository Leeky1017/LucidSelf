"""
Migration 002: Create geo_cache table

Creates the geo_cache table for system-level geocoding cache.
This table stores resolved Place objects keyed by normalized query + country hint.

Schema:
- cache_key: Primary key (normalized_query + '|' + hint_country)
- place_id: Reference to resolved place
- place_json: Serialized Place object
- created_at: Creation timestamp
- last_used_at: Last access timestamp
- hit_count: Access count

Indices:
- idx_geo_cache_place_id: (place_id)

Requirements: 5.1
"""

import os
from typing import Optional

try:
    import psycopg2
    PSYCOPG2_AVAILABLE = True
except ImportError:
    PSYCOPG2_AVAILABLE = False


# SQL statements for migration
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS geo_cache (
    cache_key TEXT PRIMARY KEY,
    place_id TEXT NOT NULL,
    place_json TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_used_at TIMESTAMP NOT NULL,
    hit_count INTEGER NOT NULL DEFAULT 1
);
"""

CREATE_INDEX_PLACE_ID_SQL = """
CREATE INDEX IF NOT EXISTS idx_geo_cache_place_id 
ON geo_cache (place_id);
"""

DROP_TABLE_SQL = """
DROP TABLE IF EXISTS geo_cache CASCADE;
"""


def upgrade(conn_string: Optional[str] = None) -> bool:
    """
    Apply migration: create geo_cache table and indices.
    
    Args:
        conn_string: PostgreSQL connection string. If None, uses DATABASE_URL env var.
    
    Returns:
        True if migration succeeded, False otherwise.
    """
    if not PSYCOPG2_AVAILABLE:
        print("Error: psycopg2 not installed. Cannot run migration.")
        return False
    
    conn_string = conn_string or os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/lucidself"
    )
    
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        
        print("Creating geo_cache table...")
        cursor.execute(CREATE_TABLE_SQL)
        
        print("Creating index idx_geo_cache_place_id...")
        cursor.execute(CREATE_INDEX_PLACE_ID_SQL)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ Migration 002_create_geo_cache completed successfully")
        return True
    
    except Exception as e:
        print(f"✗ Migration failed: {e}")
        return False


def downgrade(conn_string: Optional[str] = None) -> bool:
    """
    Rollback migration: drop geo_cache table.
    
    Args:
        conn_string: PostgreSQL connection string. If None, uses DATABASE_URL env var.
    
    Returns:
        True if rollback succeeded, False otherwise.
    """
    if not PSYCOPG2_AVAILABLE:
        print("Error: psycopg2 not installed. Cannot run migration.")
        return False
    
    conn_string = conn_string or os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:password@localhost:5432/lucidself"
    )
    
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        
        print("Dropping geo_cache table...")
        cursor.execute(DROP_TABLE_SQL)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ Rollback 002_create_geo_cache completed successfully")
        return True
    
    except Exception as e:
        print(f"✗ Rollback failed: {e}")
        return False


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "downgrade":
        downgrade()
    else:
        upgrade()
