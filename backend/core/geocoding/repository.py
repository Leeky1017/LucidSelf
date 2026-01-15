"""
Geocoding Repositories

地理编码服务的数据访问层。
"""

import json
import os
from datetime import datetime, timezone
from typing import Optional, Protocol, Any
from backend.core.geocoding.models import Place


class DatabaseConnection(Protocol):
    """Protocol for database connection abstraction."""
    
    def execute(self, query: str, params: tuple = ()) -> Any:
        """Execute a query and return cursor."""
        ...
    
    def fetchone(self) -> Optional[tuple]:
        """Fetch one row from cursor."""
        ...
    
    def fetchall(self) -> list[tuple]:
        """Fetch all rows from cursor."""
        ...
    
    def commit(self) -> None:
        """Commit transaction."""
        ...


class WorldCitiesRepository:
    """
    Repository for world_cities table.
    
    世界城市数据库访问层。
    
    Requirements: 3.3, 3.4
    """
    
    def __init__(self, connection: Optional[Any] = None):
        """
        Initialize repository with database connection.
        
        Args:
            connection: Database connection object. If None, uses in-memory storage.
        """
        self._conn = connection
        # In-memory storage for testing when no DB connection
        self._memory_store: dict[str, Place] = {}
    
    def find_by_country_city(
        self,
        country_code: str,
        city_name: str,
        admin1_code: Optional[str] = None
    ) -> Optional[Place]:
        """
        Find place by country code and city name.
        
        根据国家代码和城市名查找地点。
        
        Args:
            country_code: ISO 3166-1 alpha-2 country code
            city_name: City name to search for
            admin1_code: Optional first-level admin code for refinement
            
        Returns:
            Place object if found, None otherwise
            
        Requirements: 3.3
        """
        if self._conn is None:
            return self._find_in_memory(country_code, city_name, admin1_code)
        
        return self._find_in_db(country_code, city_name, admin1_code)
    
    def _find_in_memory(
        self,
        country_code: str,
        city_name: str,
        admin1_code: Optional[str] = None
    ) -> Optional[Place]:
        """Find place in in-memory storage."""
        country_upper = country_code.upper()
        city_lower = city_name.lower()
        
        for place in self._memory_store.values():
            if place.country_code.upper() != country_upper:
                continue
            if place.city_name.lower() != city_lower:
                continue
            if admin1_code is not None and place.admin1_code != admin1_code:
                continue
            # Return with source='local_db' per Requirement 3.4
            return Place(
                place_id=place.place_id,
                country_code=place.country_code,
                city_name=place.city_name,
                lat=place.lat,
                lng=place.lng,
                timezone=place.timezone,
                source='local_db',  # Always local_db for world_cities hits
                accuracy='city',
                admin1_code=place.admin1_code,
                admin1_name=place.admin1_name,
                district_name_raw=place.district_name_raw,
            )
        
        return None
    
    def _find_in_db(
        self,
        country_code: str,
        city_name: str,
        admin1_code: Optional[str] = None
    ) -> Optional[Place]:
        """Find place in database."""
        cursor = self._conn.cursor()
        
        if admin1_code is not None:
            query = """
                SELECT city_id, country_code, admin1_code, admin1_name, 
                       city_name, lat, lng, timezone, source
                FROM world_cities
                WHERE UPPER(country_code) = UPPER(%s) 
                  AND LOWER(city_name) = LOWER(%s)
                  AND admin1_code = %s
                LIMIT 1
            """
            cursor.execute(query, (country_code, city_name, admin1_code))
        else:
            query = """
                SELECT city_id, country_code, admin1_code, admin1_name, 
                       city_name, lat, lng, timezone, source
                FROM world_cities
                WHERE UPPER(country_code) = UPPER(%s) 
                  AND LOWER(city_name) = LOWER(%s)
                ORDER BY population DESC NULLS LAST
                LIMIT 1
            """
            cursor.execute(query, (country_code, city_name))
        
        row = cursor.fetchone()
        cursor.close()
        
        if row is None:
            return None
        
        return Place(
            place_id=row[0],
            country_code=row[1],
            admin1_code=row[2],
            admin1_name=row[3],
            city_name=row[4],
            lat=row[5],
            lng=row[6],
            timezone=row[7],
            source='local_db',  # Always local_db for world_cities hits (Req 3.4)
            accuracy='city'
        )
    
    def insert(self, place: Place) -> None:
        """
        Insert a new place record.
        
        插入新的地点记录。
        
        Args:
            place: Place object to insert
            
        Requirements: 3.4
        """
        if self._conn is None:
            self._memory_store[place.place_id] = place
            return
        
        cursor = self._conn.cursor()
        query = """
            INSERT INTO world_cities 
                (city_id, country_code, admin1_code, admin1_name, 
                 city_name, lat, lng, timezone, source)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (city_id) DO UPDATE SET
                country_code = EXCLUDED.country_code,
                admin1_code = EXCLUDED.admin1_code,
                admin1_name = EXCLUDED.admin1_name,
                city_name = EXCLUDED.city_name,
                lat = EXCLUDED.lat,
                lng = EXCLUDED.lng,
                timezone = EXCLUDED.timezone,
                source = EXCLUDED.source
        """
        cursor.execute(query, (
            place.place_id,
            place.country_code,
            place.admin1_code,
            place.admin1_name,
            place.city_name,
            place.lat,
            place.lng,
            place.timezone,
            place.source
        ))
        self._conn.commit()
        cursor.close()
    
    def find_all(self) -> list[Place]:
        """
        Find all places in repository.
        
        获取所有地点记录（主要用于测试）。
        
        Returns:
            List of all Place objects
        """
        if self._conn is None:
            return list(self._memory_store.values())
        
        cursor = self._conn.cursor()
        query = """
            SELECT city_id, country_code, admin1_code, admin1_name, 
                   city_name, lat, lng, timezone, source
            FROM world_cities
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        
        return [
            Place(
                place_id=row[0],
                country_code=row[1],
                admin1_code=row[2],
                admin1_name=row[3],
                city_name=row[4],
                lat=row[5],
                lng=row[6],
                timezone=row[7],
                source='local_db',
                accuracy='city'
            )
            for row in rows
        ]
    
    def clear(self) -> None:
        """Clear all records (for testing)."""
        if self._conn is None:
            self._memory_store.clear()
        else:
            cursor = self._conn.cursor()
            cursor.execute("DELETE FROM world_cities")
            self._conn.commit()
            cursor.close()


class GeoCacheRepository:
    """
    Repository for geo_cache table.
    
    系统级地理缓存访问层。
    
    Requirements: 5.1, 5.2, 5.3
    """
    
    def __init__(self, connection: Optional[Any] = None):
        """
        Initialize repository with database connection.
        
        Args:
            connection: Database connection object. If None, uses in-memory storage.
        """
        self._conn = connection
        # In-memory storage: cache_key -> (place_json, created_at, last_used_at, hit_count)
        self._memory_store: dict[str, dict] = {}
    
    def get(self, cache_key: str) -> Optional[Place]:
        """
        Get cached place by cache key.
        
        根据缓存键获取缓存的地点。
        
        Note: This method does NOT update hit count. Call update_hit() separately
        after confirming the cache hit should be recorded.
        
        Args:
            cache_key: Cache key to look up
            
        Returns:
            Place object if found, None otherwise
            
        Requirements: 5.1
        """
        if self._conn is None:
            return self._get_from_memory(cache_key)
        
        return self._get_from_db(cache_key)
    
    def _get_from_memory(self, cache_key: str) -> Optional[Place]:
        """Get from in-memory storage."""
        entry = self._memory_store.get(cache_key)
        if entry is None:
            return None
        return Place.from_json(entry['place_json'])
    
    def _get_from_db(self, cache_key: str) -> Optional[Place]:
        """Get from database."""
        cursor = self._conn.cursor()
        query = """
            SELECT place_json FROM geo_cache WHERE cache_key = %s
        """
        cursor.execute(query, (cache_key,))
        row = cursor.fetchone()
        cursor.close()
        
        if row is None:
            return None
        
        return Place.from_json(row[0])
    
    def set(self, cache_key: str, place: Place) -> None:
        """
        Store place in cache.
        
        将地点存入缓存。
        
        Args:
            cache_key: Cache key for storage
            place: Place object to cache
            
        Requirements: 5.3
        """
        if self._conn is None:
            self._set_in_memory(cache_key, place)
            return
        
        self._set_in_db(cache_key, place)
    
    def _set_in_memory(self, cache_key: str, place: Place) -> None:
        """Store in in-memory storage."""
        now = datetime.now(timezone.utc).isoformat()
        self._memory_store[cache_key] = {
            'place_json': place.to_json(),
            'place_id': place.place_id,
            'created_at': now,
            'last_used_at': now,
            'hit_count': 1
        }
    
    def _set_in_db(self, cache_key: str, place: Place) -> None:
        """Store in database."""
        cursor = self._conn.cursor()
        now = datetime.now(timezone.utc)
        query = """
            INSERT INTO geo_cache (cache_key, place_id, place_json, created_at, last_used_at, hit_count)
            VALUES (%s, %s, %s, %s, %s, 1)
            ON CONFLICT (cache_key) DO UPDATE SET
                place_id = EXCLUDED.place_id,
                place_json = EXCLUDED.place_json,
                last_used_at = EXCLUDED.last_used_at
        """
        cursor.execute(query, (cache_key, place.place_id, place.to_json(), now, now))
        self._conn.commit()
        cursor.close()
    
    def update_hit(self, cache_key: str) -> None:
        """
        Update hit count and last_used_at.
        
        更新命中计数和最后使用时间。
        
        Args:
            cache_key: Cache key to update
            
        Requirements: 5.2
        """
        if self._conn is None:
            self._update_hit_in_memory(cache_key)
            return
        
        self._update_hit_in_db(cache_key)
    
    def _update_hit_in_memory(self, cache_key: str) -> None:
        """Update hit in in-memory storage."""
        entry = self._memory_store.get(cache_key)
        if entry is not None:
            entry['hit_count'] += 1
            entry['last_used_at'] = datetime.now(timezone.utc).isoformat()
    
    def _update_hit_in_db(self, cache_key: str) -> None:
        """Update hit in database."""
        cursor = self._conn.cursor()
        query = """
            UPDATE geo_cache 
            SET hit_count = hit_count + 1, last_used_at = %s
            WHERE cache_key = %s
        """
        cursor.execute(query, (datetime.now(timezone.utc), cache_key))
        self._conn.commit()
        cursor.close()
    
    def get_stats(self, cache_key: str) -> Optional[dict]:
        """
        Get cache entry statistics.
        
        获取缓存条目统计信息（用于测试）。
        
        Returns:
            Dict with hit_count and last_used_at, or None if not found
        """
        if self._conn is None:
            entry = self._memory_store.get(cache_key)
            if entry is None:
                return None
            return {
                'hit_count': entry['hit_count'],
                'last_used_at': entry['last_used_at'],
                'created_at': entry['created_at']
            }
        
        cursor = self._conn.cursor()
        query = """
            SELECT hit_count, last_used_at, created_at 
            FROM geo_cache WHERE cache_key = %s
        """
        cursor.execute(query, (cache_key,))
        row = cursor.fetchone()
        cursor.close()
        
        if row is None:
            return None
        
        return {
            'hit_count': row[0],
            'last_used_at': row[1].isoformat() if hasattr(row[1], 'isoformat') else row[1],
            'created_at': row[2].isoformat() if hasattr(row[2], 'isoformat') else row[2]
        }
    
    def clear(self) -> None:
        """Clear all cache entries (for testing)."""
        if self._conn is None:
            self._memory_store.clear()
        else:
            cursor = self._conn.cursor()
            cursor.execute("DELETE FROM geo_cache")
            self._conn.commit()
            cursor.close()


class UserPlacesRepository:
    """
    Repository for user_places table.
    
    用户级地点绑定访问层。
    
    Requirements: 4.1, 4.2, 4.3
    """
    
    def __init__(self, connection: Optional[Any] = None):
        """
        Initialize repository with database connection.
        
        Args:
            connection: Database connection object. If None, uses in-memory storage.
        """
        self._conn = connection
        # In-memory storage: (user_id, label) -> place_json
        self._memory_store: dict[tuple[str, str], dict] = {}
        self._id_counter = 0
    
    def get_by_label(self, user_id: str, label: str) -> Optional[Place]:
        """
        Get place by user ID and label.
        
        根据用户ID和标签获取地点。
        
        Args:
            user_id: User identifier
            label: Semantic label (e.g., 'birth_place', 'current_city')
            
        Returns:
            Place object if binding exists, None otherwise
            
        Requirements: 4.1, 4.2
        """
        if self._conn is None:
            return self._get_from_memory(user_id, label)
        
        return self._get_from_db(user_id, label)
    
    def _get_from_memory(self, user_id: str, label: str) -> Optional[Place]:
        """Get from in-memory storage."""
        entry = self._memory_store.get((user_id, label))
        if entry is None:
            return None
        return Place.from_json(entry['place_json'])
    
    def _get_from_db(self, user_id: str, label: str) -> Optional[Place]:
        """Get from database."""
        cursor = self._conn.cursor()
        query = """
            SELECT place_json FROM user_places 
            WHERE user_id = %s AND label = %s
        """
        cursor.execute(query, (user_id, label))
        row = cursor.fetchone()
        cursor.close()
        
        if row is None:
            return None
        
        return Place.from_json(row[0])
    
    def bind(self, user_id: str, label: str, place: Place, district_name_raw: Optional[str] = None) -> None:
        """
        Create user-place binding.
        
        创建用户-地点绑定。
        
        Args:
            user_id: User identifier
            label: Semantic label (e.g., 'birth_place', 'current_city')
            place: Place object to bind
            district_name_raw: Optional raw district name for display
            
        Requirements: 4.3
        """
        if self._conn is None:
            self._bind_in_memory(user_id, label, place, district_name_raw)
            return
        
        self._bind_in_db(user_id, label, place, district_name_raw)
    
    def _bind_in_memory(self, user_id: str, label: str, place: Place, district_name_raw: Optional[str]) -> None:
        """Bind in in-memory storage."""
        self._id_counter += 1
        now = datetime.now(timezone.utc).isoformat()
        self._memory_store[(user_id, label)] = {
            'id': f'up-{self._id_counter}',
            'user_id': user_id,
            'place_id': place.place_id,
            'place_json': place.to_json(),
            'label': label,
            'district_name_raw': district_name_raw,
            'created_at': now
        }
    
    def _bind_in_db(self, user_id: str, label: str, place: Place, district_name_raw: Optional[str]) -> None:
        """Bind in database."""
        import uuid
        cursor = self._conn.cursor()
        now = datetime.now(timezone.utc)
        binding_id = str(uuid.uuid4())
        
        # Use upsert to handle re-binding
        query = """
            INSERT INTO user_places (id, user_id, place_id, place_json, label, district_name_raw, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (user_id, label) DO UPDATE SET
                place_id = EXCLUDED.place_id,
                place_json = EXCLUDED.place_json,
                district_name_raw = EXCLUDED.district_name_raw,
                created_at = EXCLUDED.created_at
        """
        cursor.execute(query, (
            binding_id, user_id, place.place_id, place.to_json(), 
            label, district_name_raw, now
        ))
        self._conn.commit()
        cursor.close()
    
    def get_all_for_user(self, user_id: str) -> list[tuple[str, Place]]:
        """
        Get all place bindings for a user.
        
        获取用户的所有地点绑定（用于测试）。
        
        Returns:
            List of (label, Place) tuples
        """
        if self._conn is None:
            results = []
            for (uid, label), entry in self._memory_store.items():
                if uid == user_id:
                    results.append((label, Place.from_json(entry['place_json'])))
            return results
        
        cursor = self._conn.cursor()
        query = """
            SELECT label, place_json FROM user_places WHERE user_id = %s
        """
        cursor.execute(query, (user_id,))
        rows = cursor.fetchall()
        cursor.close()
        
        return [(row[0], Place.from_json(row[1])) for row in rows]
    
    def clear(self) -> None:
        """Clear all bindings (for testing)."""
        if self._conn is None:
            self._memory_store.clear()
        else:
            cursor = self._conn.cursor()
            cursor.execute("DELETE FROM user_places")
            self._conn.commit()
            cursor.close()
