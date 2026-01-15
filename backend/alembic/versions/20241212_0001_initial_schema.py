"""Initial schema

Revision ID: 0001
Revises: 
Create Date: 2024-12-12

R-09/WP-08: 初始迁移 - Memory 表结构
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '0001'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # MemoryEventDB 表
    op.create_table(
        'memoryeventdb',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('user_id', sa.String(64), nullable=False, index=True),
        sa.Column('event_type', sa.String(32), nullable=False),
        sa.Column('data', sa.JSON, nullable=True),
        sa.Column('privacy_level', sa.String(16), nullable=False, server_default='normal'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    op.create_index('ix_memoryeventdb_user_type', 'memoryeventdb', ['user_id', 'event_type'])
    
    # MemoryInsightDB 表
    op.create_table(
        'memoryinsightdb',
        sa.Column('id', sa.String(36), primary_key=True),
        sa.Column('user_id', sa.String(64), nullable=False, index=True),
        sa.Column('summary', sa.Text, nullable=False),
        sa.Column('source_events', sa.JSON, nullable=True),
        sa.Column('confidence', sa.Float, nullable=False, server_default='0.5'),
        sa.Column('dimension', sa.String(32), nullable=True, index=True),
        sa.Column('source_engine', sa.String(32), nullable=True),
        sa.Column('privacy_level', sa.String(16), nullable=False, server_default='normal'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False),
    )
    op.create_index('ix_memoryinsightdb_user_dimension', 'memoryinsightdb', ['user_id', 'dimension'])


def downgrade() -> None:
    op.drop_table('memoryinsightdb')
    op.drop_table('memoryeventdb')
