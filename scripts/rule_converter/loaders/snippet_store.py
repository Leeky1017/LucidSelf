"""
Snippet Store

解析精校文档中的叙事素材（Snippet）。

Feature: rule-converter
Requirement Refs: Req 2.1-2.10
"""

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


@dataclass
class Snippet:
    """
    叙事素材
    
    格式: [snippet_id] [trigger: xxx] [factor_trigger: xxx] [role: xxx] content → source_ref
    """
    snippet_id: str
    trigger: str
    factor_trigger: str
    role: str
    content: str
    source_ref: str
    
    # 来源信息
    book_id: Optional[str] = None
    file_path: Optional[str] = None


class SnippetStore:
    """
    叙事素材存储
    
    从精校文档中解析叙事素材，提供 O(1) 查询接口。
    
    Requirement Refs: Req 2.1-2.10
    """
    
    DEFAULT_DIRS = [Path("典籍/中文典籍"), Path("典籍/texts")]
    
    # 解析正则表达式 - 格式1: 每个字段单独反引号，有 source_ref
    # - `[ns_xxx]` `[trigger: xxx]` `[factor_trigger: xxx]` `[role: xxx]` content → source_ref
    SNIPPET_PATTERN_SEPARATE = re.compile(
        r'-\s*`\[([^\]]+)\]`\s*'  # snippet_id: [ns_xxx]
        r'`\[trigger:\s*([^\]]+)\]`\s*'  # trigger
        r'`\[factor_trigger:\s*([^\]]+)\]`\s*'  # factor_trigger
        r'`\[role:\s*([^\]]+)\]`\s*'  # role
        r'(.+?)\s*→\s*'  # content
        r'(.+?)$',  # source_ref
        re.MULTILINE
    )
    
    # 解析正则表达式 - 格式1b: 每个字段单独反引号，无 source_ref
    # - `[ns_xxx]` `[trigger: xxx]` `[factor_trigger: xxx]` `[role: xxx]` content
    SNIPPET_PATTERN_SEPARATE_NO_REF = re.compile(
        r'-\s*`\[([^\]]+)\]`\s*'  # snippet_id: [ns_xxx]
        r'`\[trigger:\s*([^\]]+)\]`\s*'  # trigger
        r'`\[factor_trigger:\s*([^\]]+)\]`\s*'  # factor_trigger
        r'`\[role:\s*([^\]]+)\]`\s*'  # role
        r'([^→\n]+?)$',  # content (无 →)
        re.MULTILINE
    )
    
    # 解析正则表达式 - 格式2: 多字段合并在一个反引号内
    # - `[ns_xxx]` `[trigger: xxx] [factor_trigger: xxx]` `[role: xxx]` content → source_ref
    SNIPPET_PATTERN_MERGED = re.compile(
        r'-\s*`\[([^\]]+)\]`\s*'  # snippet_id
        r'`\[trigger:\s*([^\]]+)\]\s*\[factor_trigger:\s*([^\]]+)\]`\s*'  # trigger + factor_trigger 合并
        r'`\[role:\s*([^\]]+)\]`\s*'  # role
        r'(.+?)\s*→\s*'  # content
        r'(.+?)$',  # source_ref
        re.MULTILINE
    )
    
    # 备用正则（没有 factor_trigger 的旧格式）
    SNIPPET_PATTERN_LEGACY = re.compile(
        r'-\s*`\[([^\]]+)\]`\s*'  # snippet_id
        r'`\[trigger:\s*([^\]]+)\]`\s*'  # trigger
        r'`\[role:\s*([^\]]+)\]`\s*'  # role
        r'(.+?)\s*→\s*'  # content
        r'(.+?)$',  # source_ref
        re.MULTILINE
    )
    
    # L1 区域标记
    L1_BEGIN = "<!-- L1_BEGIN -->"
    L1_END = "<!-- L1_END -->"
    
    def __init__(self, base_dir: Optional[Path] = None, lazy_load: bool = True):
        # 支持单个目录或使用默认多目录
        if base_dir:
            self.base_dirs = [Path(base_dir)]
        else:
            self.base_dirs = self.DEFAULT_DIRS
        self.lazy_load = lazy_load
        
        self._snippets: Dict[str, Snippet] = {}
        self._by_book: Dict[str, List[str]] = {}
        self._loaded = False
        self._stats: Dict[str, int] = {
            "total_files": 0,
            "parsed_files": 0,
            "failed_files": 0,
            "total_snippets": 0,
            "snippets_with_factor_trigger": 0,
        }
    
    def load_from_dir(self, directory: Optional[Path] = None) -> None:
        """
        从目录加载所有叙事素材
        
        Args:
            directory: 目录路径，默认使用 base_dirs
        """
        self._snippets.clear()
        self._by_book.clear()
        self._reset_stats()
        
        # 确定要扫描的目录
        if directory:
            dirs_to_scan = [Path(directory)]
        else:
            dirs_to_scan = self.base_dirs
        
        for dir_path in dirs_to_scan:
            if not dir_path.exists():
                logger.warning(f"Directory not found: {dir_path}")
                continue
            
            # 查找所有精校文档（支持 */编辑/*.md 和 */编辑/*.md）
            md_files = list(dir_path.glob("*/编辑/*.md")) + list(dir_path.glob("*/*/编辑/*.md"))
            self._stats["total_files"] += len(md_files)
            
            for md_file in md_files:
                try:
                    self._parse_file(md_file)
                    self._stats["parsed_files"] += 1
                except Exception as e:
                    self._stats["failed_files"] += 1
                    logger.warning(f"Failed to parse {md_file}: {e}")
        
        self._loaded = True
        logger.info(
            f"Loaded {self._stats['total_snippets']} snippets from "
            f"{self._stats['parsed_files']} files"
        )
    
    def _parse_file(self, path: Path) -> None:
        """解析单个精校文档"""
        content = path.read_text(encoding="utf-8")
        
        # 提取书籍ID（从路径推断）
        # 典籍/中文典籍/{book_name}/编辑/{file}.md
        # 或 {base_dir}/{book_name}/编辑/{file}.md
        parts = path.parts
        book_id = None
        
        # 查找 "编辑" 目录的上一级作为 book_id
        for i, part in enumerate(parts):
            if part == "编辑" and i > 0:
                book_id = parts[i - 1]
                break
        
        # fallback: 使用文件名
        if not book_id:
            book_id = path.stem
        
        # 提取 L1 区域内容
        l1_sections = self._extract_l1_sections(content)
        
        for section in l1_sections:
            self._parse_section(section, book_id, str(path))
    
    def _extract_l1_sections(self, content: str) -> List[str]:
        """
        提取需要解析的文档区域
        
        策略：直接解析整个文件，因为很多 snippet 在 L1 区域外
        """
        # 直接返回整个文件内容，让正则匹配所有 snippet
        return [content]
    
    def _parse_section(self, section: str, book_id: str, file_path: str) -> None:
        """解析单个 L1 区域"""
        # 格式1: 每个字段单独反引号
        for match in self.SNIPPET_PATTERN_SEPARATE.finditer(section):
            snippet_id, trigger, factor_trigger, role, content, source_ref = match.groups()
            
            snippet = Snippet(
                snippet_id=snippet_id.strip(),
                trigger=trigger.strip(),
                factor_trigger=factor_trigger.strip(),
                role=role.strip(),
                content=content.strip(),
                source_ref=source_ref.strip(),
                book_id=book_id,
                file_path=file_path,
            )
            
            self._add_snippet(snippet)
            self._stats["snippets_with_factor_trigger"] += 1
        
        # 格式2: trigger 和 factor_trigger 合并在一个反引号内
        for match in self.SNIPPET_PATTERN_MERGED.finditer(section):
            snippet_id, trigger, factor_trigger, role, content, source_ref = match.groups()
            
            # 跳过已解析的
            if snippet_id.strip() in self._snippets:
                continue
            
            snippet = Snippet(
                snippet_id=snippet_id.strip(),
                trigger=trigger.strip(),
                factor_trigger=factor_trigger.strip(),
                role=role.strip(),
                content=content.strip(),
                source_ref=source_ref.strip(),
                book_id=book_id,
                file_path=file_path,
            )
            
            self._add_snippet(snippet)
            self._stats["snippets_with_factor_trigger"] += 1
        
        # 格式3: 旧格式（没有 factor_trigger）
        for match in self.SNIPPET_PATTERN_LEGACY.finditer(section):
            snippet_id, trigger, role, content, source_ref = match.groups()
            
            # 跳过已解析的
            if snippet_id.strip() in self._snippets:
                continue
            
            snippet = Snippet(
                snippet_id=snippet_id.strip(),
                trigger=trigger.strip(),
                factor_trigger="",  # 旧格式没有
                role=role.strip(),
                content=content.strip(),
                source_ref=source_ref.strip(),
                book_id=book_id,
                file_path=file_path,
            )
            
            self._add_snippet(snippet)
    
    def _add_snippet(self, snippet: Snippet) -> None:
        """添加叙事素材"""
        self._snippets[snippet.snippet_id] = snippet
        self._stats["total_snippets"] += 1
        
        # 按书籍索引
        if snippet.book_id:
            if snippet.book_id not in self._by_book:
                self._by_book[snippet.book_id] = []
            self._by_book[snippet.book_id].append(snippet.snippet_id)
    
    def _reset_stats(self) -> None:
        """重置统计"""
        for key in self._stats:
            self._stats[key] = 0
    
    def _ensure_loaded(self) -> None:
        """确保数据已加载"""
        if not self._loaded and self.lazy_load:
            self.load_from_dir()
    
    def get(self, snippet_id: str) -> Optional[Snippet]:
        """
        获取单个叙事素材
        
        Args:
            snippet_id: 叙事素材ID
            
        Returns:
            Snippet 或 None
        """
        self._ensure_loaded()
        return self._snippets.get(snippet_id)
    
    def get_batch(self, snippet_ids: List[str]) -> List[Snippet]:
        """
        批量获取叙事素材
        
        Args:
            snippet_ids: 叙事素材ID列表
            
        Returns:
            成功获取的 Snippet 列表（保持顺序，跳过不存在的）
        """
        self._ensure_loaded()
        result = []
        for sid in snippet_ids:
            snippet = self._snippets.get(sid)
            if snippet:
                result.append(snippet)
        return result
    
    def has(self, snippet_id: str) -> bool:
        """检查叙事素材是否存在"""
        self._ensure_loaded()
        return snippet_id in self._snippets
    
    def get_by_book(self, book_id: str) -> List[Snippet]:
        """获取指定书籍的所有叙事素材"""
        self._ensure_loaded()
        snippet_ids = self._by_book.get(book_id, [])
        return [self._snippets[sid] for sid in snippet_ids]
    
    @property
    def stats(self) -> Dict[str, int]:
        """获取统计信息"""
        self._ensure_loaded()
        return self._stats.copy()
    
    @property
    def snippets_by_book(self) -> Dict[str, int]:
        """获取每本书的叙事素材数量"""
        self._ensure_loaded()
        return {book: len(ids) for book, ids in self._by_book.items()}
    
    def __len__(self) -> int:
        self._ensure_loaded()
        return len(self._snippets)
    
    def __contains__(self, snippet_id: str) -> bool:
        return self.has(snippet_id)
