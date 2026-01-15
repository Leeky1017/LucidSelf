"""
Migration 003: Create user_places table

Creates the user_places table for user-level place bindings.
This table stores semantic bindings between users and places (e.g., birth_place, current_city).

Schema:
- id: Primary key (UUID)
- user_id: User identifier
- place_id: Reference to place
- place_json: Serialized Place object
- label: Semantic label (e.g., 'birth_place', 'current_city')
- district_name_raw: Raw district name for display
- created_at: Creation timestamp

Indices:
- idx_user_places_user_label: UNIQUE (user_id, label)

Requirements: 4.1
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
CREATE TABLE IF NOT EXISTS user_places (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    place_id TEXT NOT NULL,
    place_json TEXT NOT NULL,
    label TEXT NOT NULL,
    district_name_raw TEXT,
    created_at TIMESTAMP NOT NULL
);
"""

CREATE_INDEX_USER_LABEL_SQL = """
CREATE UNIQUE INDEX IF NOT EXISTS idx_user_places_user_label 
ON user_places (user_id, label);
"""

DROP_TABLE_SQL = """
DROP TABLE IF EXISTS user_places CASCADE;
"""


def upgrade(conn_string: Optional[str] = None) -> bool:
    """
    Apply migration: create user_places table and indices.
    
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
        
        print("Creating user_places table...")
        cursor.execute(CREATE_TABLE_SQL)
        
        print("Creating index idx_user_places_user_label...")
        cursor.execute(CREATE_INDEX_USER_LABEL_SQL)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ Migration 003_create_user_places completed successfully")
        return True
    
    except Exception as e:
        print(f"✗ Migration failed: {e}")
        return False


def downgrade(conn_string: Optional[str] = None) -> bool:
    """
    Rollback migration: drop user_places table.
    
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
        
        print("Dropping user_places table...")
        cursor.execute(DROP_TABLE_SQL)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ Rollback 003_create_user_places completed successfully")
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
