"""
SchemaLoader - 加载schema_staging中的数据

从data/schema_staging/目录加载snippets和relations数据。
"""

from pathlib import Path
from typing import List, Optional

import yaml
from pydantic import ValidationError as PydanticValidationError

from scripts.logic_chain_builder.constants import SNIPPETS_DIR, RELATIONS_DIR
from scripts.logic_chain_builder.logging_config import get_logger

# 复用schema_extractor中的模型
from scripts.schema_extractor.models import NarrativeSnippet, ConfigRelation


logger = get_logger(__name__)


class SchemaLoadError(Exception):
    """Schema加载错误基类"""
    pass


class SchemaValidationError(SchemaLoadError):
    """Schema验证错误"""
    pass


class SchemaLoader:
    """
    加载schema_staging中的数据
    
    负责从YAML文件加载snippets和relations数据。
    """
    
    def __init__(
        self,
        snippets_dir: str = SNIPPETS_DIR,
        relations_dir: str = RELATIONS_DIR
    ):
        """
        初始化加载器
        
        Args:
            snippets_dir: snippets目录路径
            relations_dir: relations目录路径
        """
        self.snippets_dir = Path(snippets_dir)
        self.relations_dir = Path(relations_dir)
    
    def load_snippets(self, book_id: str) -> List[NarrativeSnippet]:
        """
        加载指定书籍的叙事素材
        
        Args:
            book_id: 书籍ID
        
        Returns:
            NarrativeSnippet列表
        
        Raises:
            FileNotFoundError: 当文件不存在时
            SchemaValidationError: 当YAML结构不符合预期时
        """
        path = self._get_snippets_path(book_id)
        
        if not path.exists():
            logger.warning(f"Snippets file not found: {path}")
            raise FileNotFoundError(f"Snippets file not found: {path}")
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logger.error(f"Failed to parse YAML file {path}: {e}")
            raise SchemaValidationError(f"Invalid YAML syntax in {path}: {e}")
        
        # 验证基本结构
        if not isinstance(data, dict):
            raise SchemaValidationError(f"Expected dict at root level in {path}")
        
        if 'snippets' not in data:
            raise SchemaValidationError(f"Missing 'snippets' key in {path}")
        
        snippets_data = data.get('snippets', [])
        if not isinstance(snippets_data, list):
            raise SchemaValidationError(f"'snippets' must be a list in {path}")
        
        # 转换为NarrativeSnippet对象
        snippets: List[NarrativeSnippet] = []
        for i, item in enumerate(snippets_data):
            try:
                snippet = NarrativeSnippet(**item)
                snippets.append(snippet)
            except PydanticValidationError as e:
                logger.warning(f"Skipping invalid snippet at index {i} in {path}: {e}")
                continue
            except TypeError as e:
                logger.warning(f"Skipping malformed snippet at index {i} in {path}: {e}")
                continue
        
        logger.info(f"Loaded {len(snippets)} snippets from {path}")
        return snippets
    
    def load_relations(self, book_id: str) -> List[ConfigRelation]:
        """
        加载指定书籍的关系
        
        Args:
            book_id: 书籍ID
        
        Returns:
            ConfigRelation列表
        
        Raises:
            FileNotFoundError: 当文件不存在时
            SchemaValidationError: 当YAML结构不符合预期时
        """
        path = self._get_relations_path(book_id)
        
        if not path.exists():
            logger.warning(f"Relations file not found: {path}")
            raise FileNotFoundError(f"Relations file not found: {path}")
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logger.error(f"Failed to parse YAML file {path}: {e}")
            raise SchemaValidationError(f"Invalid YAML syntax in {path}: {e}")
        
        # 验证基本结构
        if not isinstance(data, dict):
            raise SchemaValidationError(f"Expected dict at root level in {path}")
        
        if 'relations' not in data:
            raise SchemaValidationError(f"Missing 'relations' key in {path}")
        
        relations_data = data.get('relations', [])
        if not isinstance(relations_data, list):
            raise SchemaValidationError(f"'relations' must be a list in {path}")
        
        # 转换为ConfigRelation对象
        relations: List[ConfigRelation] = []
        for i, item in enumerate(relations_data):
            try:
                relation = ConfigRelation(**item)
                relations.append(relation)
            except PydanticValidationError as e:
                logger.warning(f"Skipping invalid relation at index {i} in {path}: {e}")
                continue
            except TypeError as e:
                logger.warning(f"Skipping malformed relation at index {i} in {path}: {e}")
                continue
        
        logger.info(f"Loaded {len(relations)} relations from {path}")
        return relations
    
    def list_available_books(self) -> List[str]:
        """
        列出所有可处理的书籍
        
        扫描schema_staging目录，返回同时拥有snippets和relations文件的book_id列表。
        
        Returns:
            book_id列表
        """
        # 获取所有snippets文件的book_ids
        snippet_book_ids = set()
        if self.snippets_dir.exists():
            for path in self.snippets_dir.glob("*_snippets.yaml"):
                # 提取book_id: 移除 "_snippets.yaml" 后缀
                book_id = path.stem.replace("_snippets", "")
                snippet_book_ids.add(book_id)
        
        # 获取所有relations文件的book_ids
        relation_book_ids = set()
        if self.relations_dir.exists():
            for path in self.relations_dir.glob("*_relations.yaml"):
                # 提取book_id: 移除 "_relations.yaml" 后缀
                book_id = path.stem.replace("_relations", "")
                relation_book_ids.add(book_id)
        
        # 返回同时拥有snippets和relations的book_ids
        available_books = sorted(snippet_book_ids & relation_book_ids)
        
        logger.info(f"Found {len(available_books)} available books with both snippets and relations")
        return available_books
    
    def _get_snippets_path(self, book_id: str) -> Path:
        """获取snippets文件路径"""
        return self.snippets_dir / f"{book_id}_snippets.yaml"
    
    def _get_relations_path(self, book_id: str) -> Path:
        """获取relations文件路径"""
        return self.relations_dir / f"{book_id}_relations.yaml"
