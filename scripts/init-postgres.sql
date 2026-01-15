-- LucidSelf PostgreSQL 初始化脚本
-- 创建扩展和基础表

-- 启用UUID扩展
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 创建dream_records表
CREATE TABLE IF NOT EXISTS dream_records (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id VARCHAR(64) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'draft',
    mode VARCHAR(20) NOT NULL DEFAULT 'quick',
    raw_input TEXT NOT NULL,
    generated_content TEXT,
    final_content TEXT NOT NULL,
    title VARCHAR(200),
    mood VARCHAR(50),
    clarity INTEGER CHECK (clarity >= 1 AND clarity <= 5),
    tags TEXT[] DEFAULT '{}',
    analysis JSONB,
    generate_count INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    published_at TIMESTAMP WITH TIME ZONE
);

-- 创建user_profiles表
CREATE TABLE IF NOT EXISTS user_profiles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id VARCHAR(64) NOT NULL UNIQUE,
    birth_data JSONB,
    preferences JSONB NOT NULL DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW()
);

-- 创建user_limits表
CREATE TABLE IF NOT EXISTS user_limits (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id VARCHAR(64) NOT NULL,
    limit_date DATE NOT NULL,
    daily_dreams INTEGER NOT NULL DEFAULT 5,
    daily_readings INTEGER NOT NULL DEFAULT 10,
    dreams_used INTEGER NOT NULL DEFAULT 0,
    readings_used INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW(),
    UNIQUE (user_id, limit_date)
);

-- 创建索引
CREATE INDEX IF NOT EXISTS ix_dream_records_user_id ON dream_records(user_id);
CREATE INDEX IF NOT EXISTS ix_dream_records_user_created ON dream_records(user_id, created_at DESC);
CREATE INDEX IF NOT EXISTS ix_dream_records_status ON dream_records(status);
CREATE INDEX IF NOT EXISTS ix_user_profiles_user_id ON user_profiles(user_id);
CREATE INDEX IF NOT EXISTS ix_user_limits_user_id ON user_limits(user_id);
CREATE INDEX IF NOT EXISTS ix_user_limits_date ON user_limits(limit_date);

-- 创建更新时间触发器函数
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- 为每个表添加更新时间触发器
DROP TRIGGER IF EXISTS update_dream_records_updated_at ON dream_records;
CREATE TRIGGER update_dream_records_updated_at
    BEFORE UPDATE ON dream_records
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_user_profiles_updated_at ON user_profiles;
CREATE TRIGGER update_user_profiles_updated_at
    BEFORE UPDATE ON user_profiles
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

DROP TRIGGER IF EXISTS update_user_limits_updated_at ON user_limits;
CREATE TRIGGER update_user_limits_updated_at
    BEFORE UPDATE ON user_limits
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- 输出初始化完成信息
DO $$
BEGIN
    RAISE NOTICE 'LucidSelf database initialized successfully';
END $$;
