"""
SnippetClusterer - 将snippets聚类为逻辑节点

按source_ref分组snippets，创建LogicNode。
"""

import re
from collections import defaultdict
from typing import Dict, List, Optional

from scripts.logic_chain_builder.models import LogicNode, SnippetRole
from scripts.logic_chain_builder.constants import ROLE_PRIORITY, MAX_SUMMARY_LENGTH
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.schema_extractor.models import NarrativeSnippet


logger = get_logger(__name__)

# Placeholder for empty source_ref
EMPTY_SOURCE_REF_PLACEHOLDER = "__EMPTY_SOURCE_REF__"


class SnippetClusterer:
    """
    将snippets聚类为逻辑节点
    
    按source_ref分组snippets，为每组创建一个LogicNode。
    """
    
    def _normalize_source_ref(self, source_ref: Optional[str]) -> str:
        """
        Normalize source_ref for consistent grouping.
        
        Handles:
        - Empty/None source_ref -> placeholder
        - Whitespace trimming
        - Special character normalization
        
        Args:
            source_ref: The source reference string
            
        Returns:
            Normalized source_ref string
        """
        if source_ref is None or source_ref.strip() == "":
            return EMPTY_SOURCE_REF_PLACEHOLDER
        
        # Trim whitespace
        normalized = source_ref.strip()
        
        # Normalize multiple spaces to single space
        normalized = re.sub(r'\s+', ' ', normalized)
        
        return normalized
    
    def cluster_by_source_ref(
        self,
        snippets: List[NarrativeSnippet]
    ) -> Dict[str, List[NarrativeSnippet]]:
        """
        按source_ref分组snippets
        
        Groups snippets by their source_ref field. Snippets with the same
        source_ref (same chapter/section) are grouped together.
        
        Edge cases handled:
        - Empty/None source_ref: grouped under placeholder key
        - Special characters: preserved as-is after normalization
        - Whitespace: trimmed and normalized
        
        Args:
            snippets: NarrativeSnippet列表
        
        Returns:
            source_ref -> snippets列表的映射
        """
        groups: Dict[str, List[NarrativeSnippet]] = defaultdict(list)
        
        for snippet in snippets:
            normalized_ref = self._normalize_source_ref(snippet.source_ref)
            groups[normalized_ref].append(snippet)
        
        # Log grouping statistics
        logger.debug(
            f"Clustered {len(snippets)} snippets into {len(groups)} groups"
        )
        
        # Warn about empty source_ref snippets
        if EMPTY_SOURCE_REF_PLACEHOLDER in groups:
            count = len(groups[EMPTY_SOURCE_REF_PLACEHOLDER])
            logger.warning(
                f"Found {count} snippets with empty source_ref"
            )
        
        return dict(groups)
    
    def _normalize_chapter_id(self, chapter: str) -> str:
        """
        Normalize chapter string for use in node_id.
        
        Keeps alphanumeric characters (including Chinese) and underscores.
        
        Args:
            chapter: Chapter identifier string
            
        Returns:
            Normalized chapter string suitable for node_id
        """
        if not chapter:
            return "unknown"
        
        # Remove special characters, keep alphanumeric, Chinese chars, and underscores
        # \u4e00-\u9fff covers CJK Unified Ideographs
        normalized = re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fff]', '_', chapter)
        
        # Convert ASCII letters to lowercase (keep Chinese as-is)
        normalized = ''.join(
            c.lower() if c.isascii() else c 
            for c in normalized
        )
        
        # Replace multiple underscores with single
        normalized = re.sub(r'_+', '_', normalized)
        
        # Remove leading/trailing underscores
        normalized = normalized.strip('_')
        
        # Limit length to avoid overly long node_ids
        if len(normalized) > 30:
            normalized = normalized[:30]
        
        return normalized if normalized else "unknown"
    
    def _extract_chapter_from_source_ref(self, source_ref: str) -> str:
        """
        Extract chapter identifier from source_ref.
        
        Handles formats like:
        - 《书名》#章节
        - Book Name#Chapter
        
        Args:
            source_ref: Source reference string
            
        Returns:
            Extracted chapter identifier
        """
        if source_ref == EMPTY_SOURCE_REF_PLACEHOLDER:
            return "unknown"
        
        # Try to extract chapter after # symbol
        if '#' in source_ref:
            parts = source_ref.split('#', 1)
            if len(parts) > 1 and parts[1].strip():
                return parts[1].strip()
        
        # Fallback: use the whole source_ref
        return source_ref
    
    def create_node(
        self,
        book_abbr: str,
        chapter: str,
        seq: int,
        snippets: List[NarrativeSnippet]
    ) -> LogicNode:
        """
        创建逻辑节点
        
        Generates a LogicNode with:
        - Unique node_id following pattern n_{book_abbr}_{chapter}_{seq}
        - Aggregated snippet_ids from the group
        - Role determined by snippet roles
        - Summary generated from snippet texts (max 50 chars)
        
        Args:
            book_abbr: 书籍缩写 (lowercase alphanumeric)
            chapter: 章节标识
            seq: 序号 (0-indexed)
            snippets: 该节点包含的snippets
        
        Returns:
            LogicNode实例
        """
        # Normalize book_abbr - keep Chinese characters and alphanumeric
        book_abbr_normalized = re.sub(r'[^a-zA-Z0-9\u4e00-\u9fff]', '', book_abbr)
        # Convert ASCII to lowercase, keep Chinese as-is
        book_abbr_normalized = ''.join(
            c.lower() if c.isascii() else c 
            for c in book_abbr_normalized
        )
        if not book_abbr_normalized:
            book_abbr_normalized = "unknown"
        
        # Normalize chapter
        chapter_normalized = self._normalize_chapter_id(chapter)
        
        # Generate node_id: n_{book_abbr}_{chapter}_{seq}
        node_id = f"n_{book_abbr_normalized}_{chapter_normalized}_{seq}"
        
        # Aggregate snippet_ids
        snippet_ids = [s.snippet_id for s in snippets]
        
        # Determine role
        role = self.determine_node_role(snippets)
        
        # Generate summary
        summary = self.generate_summary(snippets)
        
        # Build metadata
        metadata = {
            "source_ref": snippets[0].source_ref if snippets else None,
            "snippet_count": len(snippets),
        }
        
        return LogicNode(
            node_id=node_id,
            snippet_ids=snippet_ids,
            role=role,
            condition=None,  # Will be set by EdgeInferrer if needed
            summary=summary,
            metadata=metadata,
        )
    
    def determine_node_role(
        self,
        snippets: List[NarrativeSnippet]
    ) -> SnippetRole:
        """
        根据snippet roles确定节点角色
        
        优先级: 主干 > 主干依赖 > 条件分支 > 例外处理 > 总结
        
        When a node contains snippets with mixed roles, the highest priority
        role is selected based on ROLE_PRIORITY mapping.
        
        Args:
            snippets: NarrativeSnippet列表
        
        Returns:
            节点角色 (SnippetRole enum)
        """
        if not snippets:
            # Default to SUMMARY for empty snippet list
            return SnippetRole.SUMMARY
        
        # Collect all roles from snippets
        roles_found: List[str] = []
        for snippet in snippets:
            # Handle both enum and string role values
            role_value = snippet.role.value if hasattr(snippet.role, 'value') else str(snippet.role)
            roles_found.append(role_value)
        
        # Find the highest priority role (lowest number in ROLE_PRIORITY)
        best_role = None
        best_priority = float('inf')
        
        for role_str in roles_found:
            priority = ROLE_PRIORITY.get(role_str, 999)
            if priority < best_priority:
                best_priority = priority
                best_role = role_str
        
        # Convert string back to SnippetRole enum
        if best_role:
            try:
                return SnippetRole(best_role)
            except ValueError:
                logger.warning(f"Unknown role '{best_role}', defaulting to SUMMARY")
                return SnippetRole.SUMMARY
        
        return SnippetRole.SUMMARY
    
    def generate_summary(
        self,
        snippets: List[NarrativeSnippet],
        max_length: int = MAX_SUMMARY_LENGTH
    ) -> str:
        """
        生成节点摘要
        
        Generates a summary by combining snippet texts, prioritizing:
        1. Trigger text (if available and meaningful)
        2. First snippet's text
        
        The summary is truncated to max_length (default 50 chars).
        
        Args:
            snippets: NarrativeSnippet列表
            max_length: 最大长度 (default: 50)
        
        Returns:
            摘要字符串 (max 50 chars)
        """
        if not snippets:
            return "空节点"
        
        # Try to use trigger as summary first (often more concise)
        triggers = [s.trigger for s in snippets if s.trigger and s.trigger.strip()]
        if triggers:
            # Use the first non-empty trigger
            summary = triggers[0].strip()
            if len(summary) <= max_length:
                return summary
            # Truncate with ellipsis
            return summary[:max_length - 3] + "..."
        
        # Fallback to snippet_text
        texts = [s.snippet_text for s in snippets if s.snippet_text and s.snippet_text.strip()]
        if texts:
            summary = texts[0].strip()
            if len(summary) <= max_length:
                return summary
            # Truncate with ellipsis
            return summary[:max_length - 3] + "..."
        
        return "无内容"
    
    def is_entry_node_candidate(self, node: LogicNode) -> bool:
        """
        Check if a node is a candidate entry node.
        
        Entry nodes are nodes with role=主干 (MAIN).
        
        Args:
            node: LogicNode to check
            
        Returns:
            True if node is an entry node candidate
        """
        return node.role == SnippetRole.MAIN
    
    def is_terminal_node_candidate(self, node: LogicNode) -> bool:
        """
        Check if a node is a candidate terminal node.
        
        Terminal nodes are nodes with role=总结 (SUMMARY).
        
        Args:
            node: LogicNode to check
            
        Returns:
            True if node is a terminal node candidate
        """
        return node.role == SnippetRole.SUMMARY
