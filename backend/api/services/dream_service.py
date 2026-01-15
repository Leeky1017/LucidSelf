"""
Dream Service

梦境记录业务逻辑。
"""

import logging
import uuid
from datetime import datetime
from typing import List, Optional, Tuple

from sqlalchemy import delete, func, or_, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models.dream import DreamRecord

logger = logging.getLogger(__name__)


class DreamService:
    """梦境服务"""
    
    def __init__(self, db: AsyncSession):
        self.db = db
    
    async def create_dream(
        self,
        user_id: str,
        org_id: str,
        raw_input: str,
        final_content: str,
        generated_content: Optional[str] = None,
        title: Optional[str] = None,
        mood: Optional[str] = None,
        tags: Optional[List[str]] = None,
        clarity: Optional[int] = None,
        status: str = "draft",
        mode: str = "quick",
    ) -> DreamRecord:
        """创建梦境记录"""
        dream = DreamRecord(
            id=uuid.uuid4(),
            user_id=user_id,
            org_id=org_id,
            status=status,
            mode=mode,
            raw_input=raw_input,
            generated_content=generated_content,
            final_content=final_content,
            title=title,
            mood=mood,
            clarity=clarity,
            tags=tags or [],
            generate_count=0,
        )
        
        self.db.add(dream)
        await self.db.flush()
        await self.db.refresh(dream)
        
        logger.info("Created dream %s for user_id=%s org_id=%s", dream.id, user_id, org_id)
        return dream
    
    async def get_dream(self, dream_id: str, user_id: str, org_id: str) -> Optional[DreamRecord]:
        """获取单个梦境"""
        try:
            dream_uuid = uuid.UUID(dream_id.replace("dream_", ""))
        except ValueError:
            return None
        
        result = await self.db.execute(
            select(DreamRecord).where(
                DreamRecord.id == dream_uuid,
            )
        )
        dream = result.scalar_one_or_none()
        if not dream:
            return None

        # 访问控制：不泄露存在性（返回 None），但记录越权尝试
        if dream.user_id != user_id:
            logger.warning(
                "Dream access denied: dream_id=%s requester_user_id=%s requester_org_id=%s",
                dream_id,
                user_id,
                org_id,
            )
            return None
        if dream.org_id is not None and dream.org_id != org_id:
            logger.warning(
                "Dream cross-tenant access blocked: dream_id=%s user_id=%s attempted_org_id=%s actual_org_id=%s",
                dream_id,
                user_id,
                org_id,
                dream.org_id,
            )
            return None

        return dream
    
    async def list_dreams(
        self,
        user_id: str,
        org_id: str,
        limit: int = 20,
        offset: int = 0,
    ) -> Tuple[List[DreamRecord], int]:
        """获取梦境列表"""
        # 查询总数
        count_result = await self.db.execute(
            select(func.count()).select_from(DreamRecord).where(
                DreamRecord.user_id == user_id,
                or_(DreamRecord.org_id == org_id, DreamRecord.org_id.is_(None)),
            )
        )
        total = count_result.scalar() or 0
        
        # 查询列表
        result = await self.db.execute(
            select(DreamRecord)
            .where(
                DreamRecord.user_id == user_id,
                or_(DreamRecord.org_id == org_id, DreamRecord.org_id.is_(None)),
            )
            .order_by(DreamRecord.created_at.desc())
            .offset(offset)
            .limit(limit)
        )
        dreams = list(result.scalars().all())
        
        return dreams, total
    
    async def update_dream(
        self,
        dream_id: str,
        user_id: str,
        org_id: str,
        **updates,
    ) -> Optional[DreamRecord]:
        """更新梦境"""
        dream = await self.get_dream(dream_id, user_id, org_id)
        if not dream:
            return None
        
        for key, value in updates.items():
            if hasattr(dream, key) and value is not None:
                setattr(dream, key, value)
        
        dream.updated_at = datetime.utcnow()
        await self.db.flush()
        await self.db.refresh(dream)
        
        return dream
    
    async def delete_dream(self, dream_id: str, user_id: str, org_id: str) -> bool:
        """删除梦境"""
        dream = await self.get_dream(dream_id, user_id, org_id)
        if not dream:
            return False

        result = await self.db.execute(delete(DreamRecord).where(DreamRecord.id == dream.id))
        return result.rowcount > 0
    
    async def increment_generate_count(self, dream_id: str, user_id: str, org_id: str) -> Optional[int]:
        """增加生成计数"""
        dream = await self.get_dream(dream_id, user_id, org_id)
        if not dream:
            return None
        
        dream.generate_count += 1
        await self.db.flush()
        
        return dream.generate_count
