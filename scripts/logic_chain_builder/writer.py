"""
LogicChainWriter - 输出逻辑链到YAML文件

将LogicChain写入data/logic_chains/目录。
"""

import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml

from scripts.logic_chain_builder.models import LogicChain, SourceMetadata
from scripts.logic_chain_builder.constants import OUTPUT_DIR
from scripts.logic_chain_builder.logging_config import get_logger


logger = get_logger(__name__)


class LogicChainWriter:
    """
    输出逻辑链到YAML文件
    
    将LogicChain写入data/logic_chains/{book_id}.yaml。
    
    Features:
    - 自动创建输出目录
    - 备份已存在的文件
    - 包含元数据（version, extracted_at, source_files）
    - 符合LogicChain schema (数据契约v1.1)
    """
    
    def __init__(self, output_dir: str = OUTPUT_DIR):
        """
        初始化写入器
        
        Args:
            output_dir: 输出目录路径
        """
        self.output_dir = Path(output_dir)
    
    def write(self, chain: LogicChain) -> Path:
        """
        写入YAML文件
        
        将LogicChain序列化为YAML格式并写入文件。
        如果文件已存在，会先进行备份。
        
        Args:
            chain: LogicChain实例
        
        Returns:
            写入的文件路径
            
        Requirements: 7.1, 7.2, 7.3, 7.4, 7.5
        """
        # 确保输出目录存在 (Requirement 7.4)
        self._ensure_directory()
        
        # 获取输出路径
        output_path = self._get_output_path(chain.book_id)
        
        # 备份已存在的文件 (Requirement 7.5)
        if output_path.exists():
            backup_path = self._backup(output_path)
            if backup_path:
                logger.info(f"Backed up existing file to {backup_path}")
        
        # 确保元数据完整 (Requirement 7.2)
        chain_data = self._prepare_chain_data(chain)
        
        # 写入YAML文件 (Requirement 7.1, 7.3)
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(
                chain_data,
                f,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,
                width=120
            )
        
        logger.info(f"Written logic chain to {output_path}")
        return output_path
    
    def _prepare_chain_data(self, chain: LogicChain) -> dict:
        """
        准备要写入的数据
        
        将LogicChain转换为字典格式，确保元数据完整。
        
        Args:
            chain: LogicChain实例
            
        Returns:
            准备好的字典数据
        """
        # 使用Pydantic的model_dump进行序列化
        data = chain.model_dump(mode='json')
        
        # 确保metadata包含必要字段 (Requirement 7.2)
        if 'metadata' not in data or data['metadata'] is None:
            data['metadata'] = {}
        
        metadata = data['metadata']
        
        # 确保version存在
        if 'version' not in metadata or not metadata['version']:
            metadata['version'] = chain.version or "1.0.0"
        
        # 确保extracted_at存在
        if 'extracted_at' not in metadata or not metadata['extracted_at']:
            metadata['extracted_at'] = datetime.now().isoformat()
        
        # 确保source_files存在
        if 'source_files' not in metadata or not metadata['source_files']:
            metadata['source_files'] = [
                f"data/schema_staging/snippets/{chain.book_id}_snippets.yaml",
                f"data/schema_staging/relations/{chain.book_id}_relations.yaml",
            ]
        
        return data
    
    def _ensure_directory(self) -> None:
        """
        确保输出目录存在
        
        如果目录不存在则创建。
        
        Requirement 7.4
        """
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def _backup(self, filepath: Path) -> Optional[Path]:
        """
        备份已存在的文件
        
        将文件重命名为 {filename}.{timestamp}.bak
        
        Args:
            filepath: 要备份的文件路径
        
        Returns:
            备份文件路径，如果原文件不存在则返回None
            
        Requirement 7.5
        """
        if not filepath.exists():
            return None
        
        # 生成备份文件名: {book_id}.{timestamp}.bak
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{filepath.stem}.{timestamp}.bak"
        backup_path = filepath.parent / backup_name
        
        # 复制文件（而非移动，以防写入失败时可恢复）
        shutil.copy2(filepath, backup_path)
        
        logger.debug(f"Created backup: {backup_path}")
        return backup_path
    
    def _get_output_path(self, book_id: str) -> Path:
        """
        获取输出文件路径
        
        Args:
            book_id: 书籍ID
            
        Returns:
            输出文件的完整路径
        """
        return self.output_dir / f"{book_id}.yaml"
