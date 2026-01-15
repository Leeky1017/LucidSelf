"""
Migration 001: Create world_cities table

Creates the world_cities table for storing GeoNames cities500 data.
This table serves as the primary offline database for geocoding resolution.

Schema:
- city_id: Primary key (e.g., 'gn-2038060')
- country_code: ISO 3166-1 alpha-2 country code
- admin1_code: First-level administrative division code
- admin1_name: First-level administrative division name
- city_name: Canonical city name
- alt_names: JSON array of alternate names
- lat: Latitude
- lng: Longitude
- timezone: IANA timezone identifier
- population: Population count
- source: Data source (default 'geonames')

Indices:
- idx_world_cities_country_city: (country_code, city_name)
- idx_world_cities_country_admin1_city: (country_code, admin1_code, city_name)

Requirements: 3.1, 3.2
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
CREATE TABLE IF NOT EXISTS world_cities (
    city_id TEXT PRIMARY KEY,
    country_code TEXT NOT NULL,
    admin1_code TEXT,
    admin1_name TEXT,
    city_name TEXT NOT NULL,
    alt_names TEXT,
    lat REAL NOT NULL,
    lng REAL NOT NULL,
    timezone TEXT NOT NULL,
    population INTEGER,
    source TEXT NOT NULL DEFAULT 'geonames'
);
"""

CREATE_INDEX_COUNTRY_CITY_SQL = """
CREATE INDEX IF NOT EXISTS idx_world_cities_country_city 
ON world_cities (country_code, city_name);
"""

CREATE_INDEX_COUNTRY_ADMIN1_CITY_SQL = """
CREATE INDEX IF NOT EXISTS idx_world_cities_country_admin1_city 
ON world_cities (country_code, admin1_code, city_name);
"""

DROP_TABLE_SQL = """
DROP TABLE IF EXISTS world_cities CASCADE;
"""


def upgrade(conn_string: Optional[str] = None) -> bool:
    """
    Apply migration: create world_cities table and indices.
    
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
        
        print("Creating world_cities table...")
        cursor.execute(CREATE_TABLE_SQL)
        
        print("Creating index idx_world_cities_country_city...")
        cursor.execute(CREATE_INDEX_COUNTRY_CITY_SQL)
        
        print("Creating index idx_world_cities_country_admin1_city...")
        cursor.execute(CREATE_INDEX_COUNTRY_ADMIN1_CITY_SQL)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ Migration 001_create_world_cities completed successfully")
        return True
    
    except Exception as e:
        print(f"✗ Migration failed: {e}")
        return False


def downgrade(conn_string: Optional[str] = None) -> bool:
    """
    Rollback migration: drop world_cities table.
    
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
        
        print("Dropping world_cities table...")
        cursor.execute(DROP_TABLE_SQL)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ Rollback 001_create_world_cities completed successfully")
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
