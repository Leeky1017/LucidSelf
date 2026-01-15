"""
数据库初始化脚本

功能：
1. 创建 PostgreSQL 表
2. 创建 MongoDB 集合
3. 加载示例数据
"""

import json
import os
from pathlib import Path
from datetime import datetime

# PostgreSQL
try:
    import psycopg2
    from psycopg2.extras import Json
    PSYCOPG2_AVAILABLE = True
except ImportError:
    PSYCOPG2_AVAILABLE = False
    print("Warning: psycopg2 not installed. PostgreSQL initialization will be skipped.")

# MongoDB
try:
    from pymongo import MongoClient
    PYMONGO_AVAILABLE = True
except ImportError:
    PYMONGO_AVAILABLE = False
    print("Warning: pymongo not installed. MongoDB initialization will be skipped.")


class DatabaseInitializer:
    """数据库初始化器"""
    
    def __init__(self, pg_conn_string: str = None, mongo_uri: str = None):
        self.pg_conn_string = pg_conn_string or os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:password@localhost:5432/lucidself"
        )
        self.mongo_uri = mongo_uri or os.getenv(
            "MONGODB_URI",
            "mongodb://localhost:27017"
        )
        self.data_dir = Path(__file__).parent.parent / "data"
    
    def init_postgresql(self):
        """初始化 PostgreSQL"""
        if not PSYCOPG2_AVAILABLE:
            print("Skipping PostgreSQL initialization (psycopg2 not available)")
            return
        
        try:
            conn = psycopg2.connect(self.pg_conn_string)
            cursor = conn.cursor()
            
            print("Creating PostgreSQL tables...")
            
            # 用户表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(255) UNIQUE NOT NULL,
                    password_hash VARCHAR(255) NOT NULL,
                    full_name VARCHAR(100),
                    gender VARCHAR(20),
                    timezone VARCHAR(50) DEFAULT 'UTC',
                    language VARCHAR(10) DEFAULT 'zh-CN',
                    subscription_tier VARCHAR(20) DEFAULT 'free',
                    subscription_start_date TIMESTAMP,
                    subscription_end_date TIMESTAMP,
                    is_active BOOLEAN DEFAULT true,
                    is_verified BOOLEAN DEFAULT false,
                    last_login TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # 八字状态表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_bazi_states (
                    state_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
                    birth_datetime TIMESTAMP NOT NULL,
                    birth_timezone VARCHAR(50) NOT NULL,
                    birth_location JSONB,
                    is_solar_calendar BOOLEAN DEFAULT true,
                    year_pillar JSONB NOT NULL,
                    month_pillar JSONB NOT NULL,
                    day_pillar JSONB NOT NULL,
                    hour_pillar JSONB NOT NULL,
                    day_master VARCHAR(10) NOT NULL,
                    birth_season VARCHAR(20),
                    shi_shen JSONB,
                    pattern VARCHAR(50),
                    pattern_strength DECIMAL(3,2),
                    yong_shen VARCHAR(50),
                    xi_shen VARCHAR(50),
                    ji_shen VARCHAR(50),
                    dayun_start_age INTEGER,
                    dayun_pillars JSONB,
                    version VARCHAR(20) DEFAULT '1.0.0',
                    calculation_method VARCHAR(50) DEFAULT 'standard',
                    notes TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # 推理历史表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS inference_history (
                    inference_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
                    request_type VARCHAR(50) NOT NULL,
                    request_params JSONB,
                    result_ref UUID NOT NULL,
                    rules_matched INTEGER,
                    execution_time_ms INTEGER,
                    confidence_avg DECIMAL(3,2),
                    rule_version VARCHAR(20),
                    engine_version VARCHAR(20),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # 反馈表
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_feedback (
                    feedback_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
                    user_id UUID NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
                    target_type VARCHAR(50) NOT NULL,
                    target_id UUID NOT NULL,
                    feedback_type VARCHAR(50) NOT NULL,
                    accuracy_score DECIMAL(3,2),
                    user_comment TEXT,
                    specific_issues JSONB,
                    action_executed BOOLEAN,
                    action_result TEXT,
                    feedback_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
            cursor.close()
            conn.close()
            
            print("✓ PostgreSQL tables created successfully")
        
        except Exception as e:
            print(f"✗ PostgreSQL initialization failed: {e}")
    
    def init_mongodb(self):
        """初始化 MongoDB"""
        if not PYMONGO_AVAILABLE:
            print("Skipping MongoDB initialization (pymongo not available)")
            return
        
        try:
            client = MongoClient(self.mongo_uri)
            db = client["lucidself"]
            
            print("Creating MongoDB collections...")
            
            # 创建集合
            collections = ["source_texts", "semantic_cores", "rules", "inference_results", "snapshots"]
            for collection_name in collections:
                if collection_name not in db.list_collection_names():
                    db.create_collection(collection_name)
                    print(f"  ✓ Created collection: {collection_name}")
            
            # 创建索引
            db["source_texts"].create_index("source_id", unique=True)
            db["semantic_cores"].create_index("semantic_id", unique=True)
            db["semantic_cores"].create_index("source_ref")
            db["rules"].create_index("rule_id", unique=True)
            db["rules"].create_index("base_semantic")
            db["inference_results"].create_index([("user_id", 1), ("created_at", -1)])
            
            print("✓ MongoDB collections and indexes created successfully")
            
            client.close()
        
        except Exception as e:
            print(f"✗ MongoDB initialization failed: {e}")
    
    def load_sample_data(self):
        """加载示例数据"""
        if not PYMONGO_AVAILABLE:
            print("Skipping sample data loading (pymongo not available)")
            return
        
        try:
            client = MongoClient(self.mongo_uri)
            db = client["lucidself"]
            
            print("Loading sample data...")
            
            # 加载原文
            sources_dir = self.data_dir / "sources"
            if sources_dir.exists():
                for source_file in sources_dir.glob("*.json"):
                    with open(source_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        db["source_texts"].update_one(
                            {"source_id": data["source_id"]},
                            {"$set": data},
                            upsert=True
                        )
                        print(f"  ✓ Loaded source: {data['source_id']}")
            
            # 加载语义
            semantics_dir = self.data_dir / "semantics"
            if semantics_dir.exists():
                for semantic_file in semantics_dir.glob("*.json"):
                    with open(semantic_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        db["semantic_cores"].update_one(
                            {"semantic_id": data["semantic_id"]},
                            {"$set": data},
                            upsert=True
                        )
                        print(f"  ✓ Loaded semantic: {data['semantic_id']}")
            
            # 加载规则
            rules_dir = self.data_dir / "rules"
            if rules_dir.exists():
                for rule_file in rules_dir.glob("*.json"):
                    with open(rule_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, list):
                            for item in data:
                                db["rules"].update_one(
                                    {"rule_id": item["rule_id"]},
                                    {"$set": item},
                                    upsert=True
                                )
                        else:
                            db["rules"].update_one(
                                {"rule_id": data["rule_id"]},
                                {"$set": data},
                                upsert=True
                            )
                        print(f"  ✓ Loaded rule: {data.get('rule_id', 'unknown')}")
            
            print("✓ Sample data loaded successfully")
            
            client.close()
        
        except Exception as e:
            print(f"✗ Sample data loading failed: {e}")
    
    def run(self):
        """运行所有初始化"""
        print("=" * 60)
        print("LucidSelf Database Initialization")
        print("=" * 60)
        
        self.init_postgresql()
        self.init_mongodb()
        self.load_sample_data()
        
        print("=" * 60)
        print("Initialization complete!")
        print("=" * 60)


if __name__ == "__main__":
    initializer = DatabaseInitializer()
    initializer.run()
