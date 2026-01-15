"""
IntelligentSummaryGenerator - 智能摘要生成

基于领域关键词生成语义完整的摘要，确保节点摘要在50字符限制内保留核心含义。

**Validates: Requirements 15.1, 15.2, 15.3, 15.4, 15.5**
"""

import re
from typing import Dict, List, Optional, Set, Tuple

from scripts.logic_chain_builder.models import LogicNode, SnippetRole
from scripts.logic_chain_builder.book_type_adapter import BookType, BookTypeAdapter
from scripts.logic_chain_builder.constants import MAX_SUMMARY_LENGTH
from scripts.logic_chain_builder.logging_config import get_logger
from scripts.schema_extractor.models import NarrativeSnippet


logger = get_logger(__name__)


# Domain keywords for each book type
# These keywords help preserve semantic meaning when generating summaries
DOMAIN_KEYWORDS: Dict[str, List[str]] = {
    "命理": [
        "格局", "用神", "喜忌", "吉凶", "日主", "月令", "财官", "印绶",
        "食伤", "比劫", "七杀", "正官", "偏财", "正财", "偏印", "正印",
        "身强", "身弱", "从格", "化格", "调候", "通关", "制化", "合化",
    ],
    "占卜": [
        "卦象", "爻辞", "意象", "符号", "诠释", "吉凶", "变卦", "动爻",
        "大阿卡纳", "小阿卡纳", "权杖", "圣杯", "宝剑", "钱币",
        "正位", "逆位", "牌阵", "塔罗", "hexagram", "trigram",
    ],
    "梦学": [
        "象征", "潜意识", "心理", "解析", "意义", "预兆", "梦境",
        "原型", "集体无意识", "阴影", "阿尼玛", "阿尼姆斯",
        "symbol", "archetype", "unconscious", "interpretation",
    ],
    "西方占星": [
        "行星", "宫位", "相位", "星座", "能量", "过境", "本命",
        "太阳", "月亮", "水星", "金星", "火星", "木星", "土星",
        "天王星", "海王星", "冥王星", "上升", "中天", "下降", "天底",
        "合相", "对分", "三分", "四分", "六分",
        "planet", "house", "aspect", "sign", "transit",
    ],
}

# Role prefixes for summary generation
ROLE_PREFIXES: Dict[SnippetRole, str] = {
    SnippetRole.MAIN: "【核心】",
    SnippetRole.MAIN_DEPENDENCY: "【依赖】",
    SnippetRole.CONDITION_BRANCH: "【条件】",
    SnippetRole.EXCEPTION: "【例外】",
    SnippetRole.SUMMARY: "【结论】",
}


class IntelligentSummaryGenerator:
    """
    智能摘要生成 - 基于领域关键词生成语义完整的摘要
    
    Generates semantically complete summaries for LogicNodes by:
    1. Analyzing all snippets to extract core meaning
    2. Using domain-specific keywords based on book type
    3. Reflecting node role in the summary
    4. Ensuring summaries are <= 50 characters
    
    **Validates: Requirements 15.1, 15.2, 15.3, 15.4, 15.5**
    """
    
    def __init__(self, max_length: int = MAX_SUMMARY_LENGTH):
        """
        Initialize the summary generator.
        
        Args:
            max_length: Maximum summary length (default: 50)
        """
        self.max_length = max_length
        self.book_type_adapter = BookTypeAdapter()
    
    def get_domain_keywords(self, book_type: str) -> List[str]:
        """
        Get domain keywords for a book type.
        
        Args:
            book_type: Book type string (命理, 占卜, 梦学, 西方占星)
            
        Returns:
            List of domain keywords
        """
        return DOMAIN_KEYWORDS.get(book_type, [])
    
    def extract_triggers(
        self, 
        snippets: List[NarrativeSnippet]
    ) -> List[str]:
        """
        Extract unique, non-empty triggers from snippets.
        
        Args:
            snippets: List of snippets
            
        Returns:
            List of unique trigger strings (preserving order)
        """
        seen: Set[str] = set()
        triggers: List[str] = []
        
        for snippet in snippets:
            if snippet.trigger and snippet.trigger.strip():
                trigger = snippet.trigger.strip()
                if trigger not in seen:
                    seen.add(trigger)
                    triggers.append(trigger)
        
        return triggers
    
    def find_domain_keywords_in_text(
        self,
        text: str,
        book_type: str
    ) -> List[str]:
        """
        Find domain keywords present in the given text.
        
        Args:
            text: Text to search
            book_type: Book type for keyword selection
            
        Returns:
            List of found keywords (in order of appearance)
        """
        keywords = self.get_domain_keywords(book_type)
        found: List[str] = []
        text_lower = text.lower()
        
        for keyword in keywords:
            # Check both original and lowercase for matching
            if keyword in text or keyword.lower() in text_lower:
                if keyword not in found:
                    found.append(keyword)
        
        return found
    
    def extract_core_meaning(
        self,
        snippets: List[NarrativeSnippet],
        book_type: str
    ) -> Tuple[str, List[str]]:
        """
        Extract core meaning from snippets.
        
        Analyzes all snippets to find:
        1. Primary trigger (most representative)
        2. Domain keywords present in snippet texts
        
        Args:
            snippets: List of snippets to analyze
            book_type: Book type for domain keyword selection
            
        Returns:
            Tuple of (core_text, found_keywords)
            
        **Validates: Requirements 15.1**
        """
        if not snippets:
            return ("空节点", [])
        
        # Extract triggers
        triggers = self.extract_triggers(snippets)
        
        # Combine all snippet texts for keyword analysis
        combined_text = " ".join(
            s.snippet_text for s in snippets 
            if s.snippet_text and s.snippet_text.strip()
        )
        
        # Find domain keywords in combined text
        found_keywords = self.find_domain_keywords_in_text(combined_text, book_type)
        
        # Determine core text
        if triggers:
            # Use first trigger as core
            core_text = triggers[0]
        elif combined_text.strip():
            # Use first snippet text
            core_text = snippets[0].snippet_text.strip()
        else:
            core_text = "无内容"
        
        return (core_text, found_keywords)
    
    def get_role_prefix(
        self,
        role: SnippetRole,
        include_prefix: bool = True
    ) -> str:
        """
        Get role prefix for summary.
        
        Args:
            role: Node role
            include_prefix: Whether to include the prefix
            
        Returns:
            Role prefix string or empty string
            
        **Validates: Requirements 15.3**
        """
        if not include_prefix:
            return ""
        return ROLE_PREFIXES.get(role, "")
    
    def compose_summary(
        self,
        core_text: str,
        role: SnippetRole,
        found_keywords: List[str],
        include_role_prefix: bool = True
    ) -> str:
        """
        Compose a summary from components.
        
        Strategy:
        1. Start with role prefix (if enabled)
        2. Add core text
        3. Add domain keywords if space permits
        4. Truncate to max_length
        
        Args:
            core_text: Core meaning text
            role: Node role
            found_keywords: Domain keywords found in snippets
            include_role_prefix: Whether to include role prefix
            
        Returns:
            Composed summary (<= max_length chars)
            
        **Validates: Requirements 15.2, 15.3, 15.4**
        """
        # Get role prefix
        prefix = self.get_role_prefix(role, include_role_prefix)
        
        # Start building summary
        summary = prefix + core_text
        
        # If already at or over limit, truncate
        if len(summary) >= self.max_length:
            return self._truncate(summary)
        
        # Try to add domain keywords
        for keyword in found_keywords:
            # Skip if keyword is already in summary
            if keyword in summary or keyword.lower() in summary.lower():
                continue
            
            # Check if we can add this keyword
            addition = f"·{keyword}"
            if len(summary) + len(addition) <= self.max_length:
                summary += addition
                break  # Only add one keyword to keep it concise
        
        return self._truncate(summary)
    
    def _truncate(self, text: str) -> str:
        """
        Truncate text to max_length with ellipsis if needed.
        
        Args:
            text: Text to truncate
            
        Returns:
            Truncated text (<= max_length chars)
        """
        if len(text) <= self.max_length:
            return text
        
        # Truncate with ellipsis
        return text[:self.max_length - 3] + "..."
    
    def generate_summary(
        self,
        node: LogicNode,
        snippets: List[NarrativeSnippet],
        book_type: str,
        include_role_prefix: bool = True
    ) -> str:
        """
        Generate a semantically complete summary for a node.
        
        Main entry point for summary generation. Analyzes snippets,
        extracts core meaning, and composes a summary that:
        - Is <= 50 characters
        - Reflects the node's role
        - Contains domain-relevant keywords when possible
        
        Args:
            node: The LogicNode to generate summary for
            snippets: All snippets (will filter to node's snippet_ids)
            book_type: Book type string for domain keyword selection
            include_role_prefix: Whether to include role prefix
            
        Returns:
            Generated summary string (<= max_length chars)
            
        **Validates: Requirements 15.1, 15.2, 15.3, 15.4, 15.5**
        """
        # Build snippet lookup
        snippet_map = {s.snippet_id: s for s in snippets}
        
        # Get snippets belonging to this node
        node_snippets = [
            snippet_map[sid]
            for sid in node.snippet_ids
            if sid in snippet_map
        ]
        
        if not node_snippets:
            logger.warning(f"Node {node.node_id} has no valid snippets")
            return "空节点"
        
        # Extract core meaning
        core_text, found_keywords = self.extract_core_meaning(
            node_snippets, book_type
        )
        
        # Compose summary
        summary = self.compose_summary(
            core_text=core_text,
            role=node.role,
            found_keywords=found_keywords,
            include_role_prefix=include_role_prefix
        )
        
        logger.debug(
            f"Generated summary for {node.node_id}: '{summary}' "
            f"(keywords: {found_keywords})"
        )
        
        return summary
    
    def generate_summary_for_book(
        self,
        node: LogicNode,
        snippets: List[NarrativeSnippet],
        book_id: str,
        include_role_prefix: bool = True
    ) -> str:
        """
        Generate summary using book_id to determine book type.
        
        Convenience method that looks up book type from book_id.
        
        Args:
            node: The LogicNode to generate summary for
            snippets: All snippets
            book_id: Book identifier
            include_role_prefix: Whether to include role prefix
            
        Returns:
            Generated summary string
        """
        book_type = self.book_type_adapter.get_book_type_str(book_id)
        return self.generate_summary(
            node=node,
            snippets=snippets,
            book_type=book_type,
            include_role_prefix=include_role_prefix
        )
    
    def improve_existing_summary(
        self,
        node: LogicNode,
        snippets: List[NarrativeSnippet],
        book_type: str
    ) -> Tuple[str, bool]:
        """
        Attempt to improve an existing node summary.
        
        Compares the current summary with a newly generated one and
        returns the better option based on:
        - Presence of domain keywords
        - Role reflection
        - Semantic completeness
        
        Args:
            node: Node with existing summary
            snippets: All snippets
            book_type: Book type string
            
        Returns:
            Tuple of (improved_summary, was_changed)
        """
        current_summary = node.summary
        new_summary = self.generate_summary(
            node=node,
            snippets=snippets,
            book_type=book_type,
            include_role_prefix=True
        )
        
        # Score both summaries
        current_score = self._score_summary(current_summary, book_type, node.role)
        new_score = self._score_summary(new_summary, book_type, node.role)
        
        if new_score > current_score:
            return (new_summary, True)
        return (current_summary, False)
    
    def _score_summary(
        self,
        summary: str,
        book_type: str,
        role: SnippetRole
    ) -> float:
        """
        Score a summary for quality.
        
        Scoring criteria:
        - Contains domain keyword: +1.0
        - Contains role prefix: +0.5
        - Not truncated (no ...): +0.3
        - Reasonable length (10-40 chars): +0.2
        
        Args:
            summary: Summary to score
            book_type: Book type for keyword matching
            role: Expected node role
            
        Returns:
            Quality score (higher is better)
        """
        score = 0.0
        
        # Check for domain keywords
        keywords = self.get_domain_keywords(book_type)
        for keyword in keywords:
            if keyword in summary or keyword.lower() in summary.lower():
                score += 1.0
                break
        
        # Check for role prefix
        expected_prefix = ROLE_PREFIXES.get(role, "")
        if expected_prefix and expected_prefix in summary:
            score += 0.5
        
        # Check for truncation
        if not summary.endswith("..."):
            score += 0.3
        
        # Check length
        if 10 <= len(summary) <= 40:
            score += 0.2
        
        return score
    
    def has_domain_keyword(self, summary: str, book_type: str) -> bool:
        """
        Check if summary contains at least one domain keyword.
        
        Args:
            summary: Summary to check
            book_type: Book type for keyword selection
            
        Returns:
            True if summary contains a domain keyword
            
        **Validates: Requirements 15.5**
        """
        keywords = self.get_domain_keywords(book_type)
        summary_lower = summary.lower()
        
        for keyword in keywords:
            if keyword in summary or keyword.lower() in summary_lower:
                return True
        
        return False


def get_summary_generator(max_length: int = MAX_SUMMARY_LENGTH) -> IntelligentSummaryGenerator:
    """
    Get an IntelligentSummaryGenerator instance.
    
    Args:
        max_length: Maximum summary length
        
    Returns:
        IntelligentSummaryGenerator instance
    """
    return IntelligentSummaryGenerator(max_length=max_length)
