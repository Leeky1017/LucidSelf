"""
HierarchicalClusterer - L2 三级聚类器

实现三级聚类策略:
- L1: source_ref (章节级)
- L2: trigger (主题级)
- L3: factor_signature (因子组合级)
"""

import re
from collections import defaultdict
from typing import Dict, List, Optional

from scripts.logic_chain_builder.models import LogicNode, SnippetRole
from scripts.logic_chain_builder.constants import ROLE_PRIORITY, MAX_SUMMARY_LENGTH
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.logic_chain_builder.v2.factor_mapper import FactorMapper
from scripts.schema_extractor.models import NarrativeSnippet

logger = get_logger(__name__)


class HierarchicalClusterer:
    """
    三级聚类器 (L2)
    
    实现三级聚类策略，解决waite全书仅2节点的问题。
    """
    
    MAX_SNIPPETS_PER_NODE = 5
    MIN_SNIPPETS_PER_NODE = 1
    MAX_NODE_TEXT_LENGTH = 500
    MIN_UNIQUE_SOURCE_REFS = 3
    
    def __init__(self, factor_mapper: FactorMapper = None):
        """
        初始化聚类器
        
        Args:
            factor_mapper: FactorMapper实例
        """
        self.factor_mapper = factor_mapper or FactorMapper()
        self._node_counter = 0
    
    def cluster(
        self,
        snippets: List[NarrativeSnippet],
        book_id: str
    ) -> List[LogicNode]:
        """
        三级聚类策略
        
        Level 1: source_ref (章节级)
        Level 2: trigger (主题级)
        Level 3: factor_signature (因子组合级)
        
        Args:
            snippets: NarrativeSnippet列表
            book_id: 书籍ID
            
        Returns:
            LogicNode列表
        """
        if not snippets:
            return []
        
        self._node_counter = 0
        
        # 检查是否需要跳过L1
        unique_source_refs = len(set(
            s.source_ref for s in snippets if s.source_ref
        ))
        
        if unique_source_refs < self.MIN_UNIQUE_SOURCE_REFS:
            logger.info(
                f"Book {book_id} has only {unique_source_refs} unique source_refs, "
                "using trigger-based clustering as primary"
            )
            return self._cluster_by_trigger_primary(snippets, book_id)
        
        # Level 1: Group by source_ref
        l1_groups = self._cluster_by_source_ref(snippets)
        
        nodes = []
        for source_ref, group in l1_groups.items():
            if len(group) <= self.MAX_SNIPPETS_PER_NODE:
                nodes.extend(self._create_nodes(
                    group, book_id, source_ref, cluster_level="L1"
                ))
            else:
                # Level 2: Split by trigger
                l2_groups = self._cluster_by_trigger(group)
                for trigger, subgroup in l2_groups.items():
                    if len(subgroup) <= self.MAX_SNIPPETS_PER_NODE:
                        nodes.extend(self._create_nodes(
                            subgroup, book_id, source_ref, cluster_level="L2"
                        ))
                    else:
                        # Level 3: Split by factor_signature
                        l3_groups = self._cluster_by_factor_signature(subgroup)
                        for sig, subsubgroup in l3_groups.items():
                            nodes.extend(self._create_nodes(
                                subsubgroup, book_id, source_ref, cluster_level="L3"
                            ))
        
        logger.info(
            f"Clustered {len(snippets)} snippets into {len(nodes)} nodes for {book_id}"
        )
        
        return nodes
    
    def _cluster_by_trigger_primary(
        self,
        snippets: List[NarrativeSnippet],
        book_id: str
    ) -> List[LogicNode]:
        """
        当source_ref太少时，使用trigger作为主聚类策略
        
        Args:
            snippets: snippet列表
            book_id: 书籍ID
            
        Returns:
            LogicNode列表
        """
        # L1: Group by trigger
        trigger_groups = self._cluster_by_trigger(snippets)
        
        nodes = []
        for trigger, group in trigger_groups.items():
            if len(group) <= self.MAX_SNIPPETS_PER_NODE:
                nodes.extend(self._create_nodes(
                    group, book_id, trigger, cluster_level="L1"
                ))
            else:
                # L2: Split by factor_signature
                factor_groups = self._cluster_by_factor_signature(group)
                for sig, subgroup in factor_groups.items():
                    nodes.extend(self._create_nodes(
                        subgroup, book_id, trigger, cluster_level="L2"
                    ))
        
        return nodes
    
    def _cluster_by_source_ref(
        self,
        snippets: List[NarrativeSnippet]
    ) -> Dict[str, List[NarrativeSnippet]]:
        """Level 1: 按source_ref分组"""
        groups: Dict[str, List[NarrativeSnippet]] = defaultdict(list)
        for snippet in snippets:
            key = snippet.source_ref or "__NO_SOURCE_REF__"
            groups[key].append(snippet)
        return dict(groups)
    
    def _cluster_by_trigger(
        self,
        snippets: List[NarrativeSnippet]
    ) -> Dict[str, List[NarrativeSnippet]]:
        """Level 2: 按trigger分组"""
        groups: Dict[str, List[NarrativeSnippet]] = defaultdict(list)
        for snippet in snippets:
            key = snippet.trigger or "__NO_TRIGGER__"
            groups[key].append(snippet)
        return dict(groups)
    
    def _cluster_by_factor_signature(
        self,
        snippets: List[NarrativeSnippet]
    ) -> Dict[str, List[NarrativeSnippet]]:
        """Level 3: 按factor_signature分组"""
        groups: Dict[str, List[NarrativeSnippet]] = defaultdict(list)
        for snippet in snippets:
            factors = self.factor_mapper.extract_factors(
                snippet.factor_trigger or ""
            )
            # 创建签名
            signature = "|".join(sorted(factors)) if factors else "__NO_FACTORS__"
            groups[signature].append(snippet)
        return dict(groups)
    
    def _create_nodes(
        self,
        snippets: List[NarrativeSnippet],
        book_id: str,
        group_key: str,
        cluster_level: str
    ) -> List[LogicNode]:
        """
        创建节点，确保大小约束
        
        当snippets超过MAX_SNIPPETS_PER_NODE时自动分割
        
        Args:
            snippets: snippet列表
            book_id: 书籍ID
            group_key: 分组键
            cluster_level: 聚类层级 (L1, L2, L3)
            
        Returns:
            LogicNode列表
        """
        if not snippets:
            return []
        
        # 如果仍然太大，分割成块
        if len(snippets) > self.MAX_SNIPPETS_PER_NODE:
            chunks = [
                snippets[i:i + self.MAX_SNIPPETS_PER_NODE]
                for i in range(0, len(snippets), self.MAX_SNIPPETS_PER_NODE)
            ]
            return [
                self._create_single_node(
                    chunk, book_id, group_key, cluster_level, chunk_index=i
                )
                for i, chunk in enumerate(chunks)
            ]
        
        return [self._create_single_node(
            snippets, book_id, group_key, cluster_level
        )]
    
    def _create_single_node(
        self,
        snippets: List[NarrativeSnippet],
        book_id: str,
        group_key: str,
        cluster_level: str,
        chunk_index: int = None
    ) -> LogicNode:
        """创建单个节点"""
        self._node_counter += 1
        
        # 规范化book_id和group_key用于node_id
        book_abbr = self._normalize_for_id(book_id)
        group_abbr = self._normalize_for_id(group_key)[:20]
        
        # 生成node_id
        if chunk_index is not None:
            node_id = f"n_{book_abbr}_{group_abbr}_{self._node_counter}_{chunk_index}"
        else:
            node_id = f"n_{book_abbr}_{group_abbr}_{self._node_counter}"
        
        # 确定角色
        role = self._determine_role(snippets)
        
        # 生成摘要
        summary = self._generate_summary(snippets)
        
        # 构建metadata
        metadata = {
            "cluster_level": cluster_level,
            "source_ref": snippets[0].source_ref if snippets else None,
            "snippet_count": len(snippets),
        }
        if chunk_index is not None:
            metadata["chunk_index"] = chunk_index
        
        return LogicNode(
            node_id=node_id,
            snippet_ids=[s.snippet_id for s in snippets],
            role=role,
            condition=None,
            summary=summary,
            metadata=metadata,
        )
    
    def _normalize_for_id(self, text: str) -> str:
        """规范化文本用于node_id"""
        if not text:
            return "unknown"
        
        # 移除特殊字符
        normalized = re.sub(r'[^a-zA-Z0-9_\u4e00-\u9fff]', '_', text)
        
        # 转小写（ASCII部分）
        normalized = ''.join(
            c.lower() if c.isascii() else c
            for c in normalized
        )
        
        # 压缩连续下划线
        normalized = re.sub(r'_+', '_', normalized)
        normalized = normalized.strip('_')
        
        return normalized[:30] if normalized else "unknown"
    
    def _determine_role(self, snippets: List[NarrativeSnippet]) -> SnippetRole:
        """根据snippet roles确定节点角色"""
        if not snippets:
            return SnippetRole.SUMMARY
        
        # 收集所有角色
        roles_found = []
        for snippet in snippets:
            role_value = snippet.role.value if hasattr(snippet.role, 'value') else str(snippet.role)
            roles_found.append(role_value)
        
        # 找最高优先级
        best_role = None
        best_priority = float('inf')
        
        for role_str in roles_found:
            priority = ROLE_PRIORITY.get(role_str, 999)
            if priority < best_priority:
                best_priority = priority
                best_role = role_str
        
        if best_role:
            try:
                return SnippetRole(best_role)
            except ValueError:
                return SnippetRole.SUMMARY
        
        return SnippetRole.SUMMARY
    
    def _generate_summary(
        self,
        snippets: List[NarrativeSnippet],
        max_length: int = MAX_SUMMARY_LENGTH
    ) -> str:
        """生成节点摘要"""
        if not snippets:
            return "空节点"
        
        # 优先使用trigger
        triggers = [s.trigger for s in snippets if s.trigger and s.trigger.strip()]
        if triggers:
            summary = triggers[0].strip()
            if len(summary) <= max_length:
                return summary
            return summary[:max_length - 3] + "..."
        
        # 回退到snippet_text
        texts = [s.snippet_text for s in snippets if s.snippet_text and s.snippet_text.strip()]
        if texts:
            summary = texts[0].strip()
            if len(summary) <= max_length:
                return summary
            return summary[:max_length - 3] + "..."
        
        return "无内容"


# 导出
__all__ = ["HierarchicalClusterer"]
