#!/usr/bin/env python3
"""
直接在数据库中创建用户（绕过限流）
"""
import asyncio
import bcrypt
import secrets
import sys
from datetime import datetime
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

async def create_user(email: str, password: str, name: str):
    from backend.db import async_session_maker
    from backend.models.auth import User, AuthCredential, AuthProvider
    from sqlalchemy import select
    
    # 生成ID
    user_id = f'user_{secrets.token_hex(6)}'
    auth_id = f'auth_{secrets.token_hex(6)}'
    
    # 哈希密码
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode(), salt).decode()
    
    async with async_session_maker() as db:
        # 检查是否已存在
        stmt = select(User).where(User.email == email.lower())
        result = await db.execute(stmt)
        existing = result.scalar_one_or_none()
        
        if existing:
            print(f'用户已存在: {existing.user_id} ({existing.email})')
            return
        
        # 创建User
        user = User(
            user_id=user_id,
            email=email.lower(),
            name=name,
            provider=AuthProvider.EMAIL,
            tier='free',
        )
        db.add(user)
        
        # 创建AuthCredential
        credential = AuthCredential(
            auth_id=auth_id,
            user_id=user_id,
            provider=AuthProvider.EMAIL,
            email=email.lower(),
            email_verified=True,
            password_hash=password_hash,
            last_login_at=datetime.utcnow(),
        )
        db.add(credential)
        
        await db.commit()
        print(f'用户创建成功!')
        print(f'  user_id: {user_id}')
        print(f'  email: {email}')
        print(f'  name: {name}')

if __name__ == "__main__":
    # 你的账户信息
    EMAIL = "3118895255@qq.com"
    PASSWORD = "@aloneever"
    NAME = "李晴吾"
    
    asyncio.run(create_user(EMAIL, PASSWORD, NAME))
