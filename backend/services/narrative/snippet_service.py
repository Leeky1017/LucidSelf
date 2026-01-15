"""
Narrative Snippet Service

叙事素材检索服务，从精校典籍中加载并按条件匹配叙事素材。

对照文档: docs/数据契约_Schema定义规范_v1.md §3.4-3.6
"""

import logging
import os
from pathlib import Path
from typing import Dict, List, Optional, Set

import yaml

logger = logging.getLogger(__name__)


# 数据目录
SNIPPETS_DIR = Path(__file__).parent.parent.parent.parent / "data" / "schema_staging" / "snippets"


# =============================================================================
# 因子别名映射 (Phase 5 Task 5.1)
# =============================================================================

FACTOR_ALIAS_MAP: Dict[str, List[str]] = {
    # 日主因子 → 通用触发词
    "day_master_jia": ["day_master", "甲"],
    "day_master_yi": ["day_master", "乙"],
    "day_master_bing": ["day_master", "丙"],
    "day_master_ding": ["day_master", "丁"],
    "day_master_wu": ["day_master", "戊"],
    "day_master_ji": ["day_master", "己"],
    "day_master_geng": ["day_master", "庚"],
    "day_master_xin": ["day_master", "辛"],
    "day_master_ren": ["day_master", "壬"],
    "day_master_gui": ["day_master", "癸"],
    
    # 季节因子
    "season_spring": ["season", "春"],
    "season_summer": ["season", "夏"],
    "season_autumn": ["season", "秋"],
    "season_winter": ["season", "冬"],
    
    # 十神因子
    "ten_god_zhengguan": ["ten_god", "正官"],
    "ten_god_qisha": ["ten_god", "七杀"],
    "ten_god_zhengcai": ["ten_god", "正财"],
    "ten_god_piancai": ["ten_god", "偏财"],
    "ten_god_zhengyin": ["ten_god", "正印"],
    "ten_god_pianyin": ["ten_god", "偏印"],
    "ten_god_shangguan": ["ten_god", "伤官"],
    "ten_god_shishen": ["ten_god", "食神"],
    "ten_god_bijian": ["ten_god", "比肩"],
    "ten_god_jiecai": ["ten_god", "劫财"],
    
    # 身强弱因子
    "strength_strong": ["strength", "身强"],
    "strength_weak": ["strength", "身弱"],
    "strength_neutral": ["strength", "中和"],
}

# 体系到典籍类别的映射 (Phase 5 Task 5.3)
ENGINE_TO_CORPUS: Dict[str, List[str]] = {
    "bazi-calculator": ["滴天髓", "子平真诠", "穷通宝鉴", "三命通会"],
    "astro-calculator": ["占星术的历史", "现代占星指南"],
    "ziwei-calculator": ["紫微斗数全书", "紫微斗数精成"],
    "tarot-interpreter": ["塔罗智慧"],
    "dream-extractor": ["周公解梦", "梦的解析"],
    "yijing-calculator": ["周易", "易传"],
    "psych-analyzer": ["心理学与生活", "性格分析"],  # R-03: 补齐 psych
}

# Fallback 触发词 (Phase 5 Task 5.4)
ENGINE_FALLBACK_TRIGGERS: Dict[str, List[str]] = {
    "bazi-calculator": ["通用", "八字", "命理"],
    "astro-calculator": ["通用", "星盘", "占星"],
    "ziwei-calculator": ["通用", "紫微", "命理"],
    "tarot-interpreter": ["通用", "塔罗"],
    "dream-extractor": ["通用", "解梦", "梦境"],
    "yijing-calculator": ["通用", "易经", "周易"],
    "psych-analyzer": ["通用", "心理", "性格", "情绪"],  # R-03: 补齐 psych
}


def expand_factors_with_aliases(factors: List[str]) -> Set[str]:
    """将因子列表扩展为包含别名的集合"""
    expanded = set(factors)
    for factor in factors:
        factor_lower = factor.lower()
        if factor_lower in FACTOR_ALIAS_MAP:
            expanded.update(FACTOR_ALIAS_MAP[factor_lower])
        # 也检查原始大小写
        if factor in FACTOR_ALIAS_MAP:
            expanded.update(FACTOR_ALIAS_MAP[factor])
    return expanded


class SnippetEntry:
    """轻量级叙事素材条目"""
    
    __slots__ = (
        "snippet_id", "trigger", "factor_trigger", "role", 
        "snippet_text", "source_ref", "source_book"
    )
    
    def __init__(
        self,
        snippet_id: str,
        trigger: str,
        factor_trigger: str,
        role: str,
        snippet_text: str,
        source_ref: str,
        source_book: str,
    ):
        self.snippet_id = snippet_id
        self.trigger = trigger
        self.factor_trigger = factor_trigger
        self.role = role
        self.snippet_text = snippet_text
        self.source_ref = source_ref
        self.source_book = source_book


class NarrativeSnippetService:
    """
    叙事素材检索服务
    
    功能:
    - 从 YAML 文件加载叙事素材
    - 按 factor_trigger 匹配素材
    - 按 rule_id 关联素材
    - 按角色 (role) 优先级排序
    
    使用方式:
        service = NarrativeSnippetService.get_instance()
        snippets = service.find_by_factors(["day_master_jia", "season_spring"])
    """
    
    # 单例
    _instance: Optional["NarrativeSnippetService"] = None
    
    # 角色优先级
    ROLE_PRIORITY = {
        "主干": 0,
        "主干依赖": 1,
        "条件分支": 2,
        "例外处理": 3,
        "总结": 4,
    }
    
    def __init__(self, snippets_dir: Optional[Path] = None):
        """初始化服务"""
        self._snippets_dir = snippets_dir or SNIPPETS_DIR
        self._snippets: List[SnippetEntry] = []
        self._by_factor: Dict[str, List[SnippetEntry]] = {}
        self._by_book: Dict[str, List[SnippetEntry]] = {}
        self._loaded = False
    
    @classmethod
    def get_instance(cls) -> "NarrativeSnippetService":
        """获取单例"""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    @classmethod
    def reset_instance(cls) -> None:
        """重置单例 (用于测试)"""
        cls._instance = None
    
    def ensure_loaded(self) -> None:
        """确保数据已加载"""
        if not self._loaded:
            self.load_all()
    
    def load_all(self) -> int:
        """
        加载所有 snippet YAML 文件
        
        Returns:
            加载的素材总数
        """
        if not self._snippets_dir.exists():
            logger.warning(f"Snippets directory not found: {self._snippets_dir}")
            return 0
        
        total = 0
        for yaml_file in self._snippets_dir.glob("*.yaml"):
            count = self._load_file(yaml_file)
            total += count
        
        self._loaded = True
        logger.info(f"Loaded {total} narrative snippets from {len(list(self._snippets_dir.glob('*.yaml')))} files")
        return total
    
    def _load_file(self, path: Path) -> int:
        """加载单个 YAML 文件"""
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            
            if not data or "snippets" not in data:
                return 0
            
            book_id = data.get("book_id", path.stem)
            count = 0
            
            for item in data["snippets"]:
                entry = SnippetEntry(
                    snippet_id=item.get("snippet_id", ""),
                    trigger=item.get("trigger", ""),
                    factor_trigger=item.get("factor_trigger", ""),
                    role=item.get("role", "主干"),
                    snippet_text=item.get("snippet_text", ""),
                    source_ref=item.get("source_ref", ""),
                    source_book=item.get("source_book", book_id),
                )
                
                self._snippets.append(entry)
                
                # 按 factor_trigger 索引
                for factor in self._extract_factors(entry.factor_trigger):
                    if factor not in self._by_factor:
                        self._by_factor[factor] = []
                    self._by_factor[factor].append(entry)
                
                # 按书籍索引
                if book_id not in self._by_book:
                    self._by_book[book_id] = []
                self._by_book[book_id].append(entry)
                
                count += 1
            
            return count
        
        except Exception as e:
            logger.error(f"Failed to load snippets from {path}: {e}")
            return 0
    
    def _extract_factors(self, factor_trigger: str) -> Set[str]:
        """从 factor_trigger 表达式中提取因子名"""
        if not factor_trigger:
            return set()
        
        # 简单解析: 提取所有看起来像因子名的部分
        # 例如: "day_master=甲 AND month∈[寅,卯]" -> {"day_master", "month"}
        # 例如: "dizhi_shengong" -> {"dizhi_shengong"}
        factors = set()
        
        # 替换操作符和分隔符为空格
        cleaned = factor_trigger
        for sep in ["==", "!=", ">=", "<=", ">", "<", "∈", "AND", "OR", "NOT", "IN", "[", "]", "(", ")", "{", "}", ",", "="]:
            cleaned = cleaned.replace(sep, " ")
        
        # 提取单词
        for word in cleaned.split():
            # 只保留看起来像因子名的部分 (小写带下划线)
            if word and (word[0].islower() or word.startswith("day_") or "_" in word):
                # 去除值部分
                if word not in ("on", "off", "高", "中", "低", "有", "无"):
                    factors.add(word)
        
        return factors
    
    def find_by_factors(
        self,
        factors: List[str],
        max_results: int = 10,
        roles: Optional[List[str]] = None,
        engine_id: Optional[str] = None,
    ) -> List[SnippetEntry]:
        """
        按因子查找匹配的叙事素材
        
        Args:
            factors: 因子名列表
            max_results: 最大返回数量
            roles: 限制的角色列表
            engine_id: 引擎 ID，用于优先返回对应体系的典籍
            
        Returns:
            匹配的素材列表，按角色优先级排序
        """
        self.ensure_loaded()
        
        if not factors:
            return []
        
        # Task 5.1: 扩展因子别名
        expanded_factors = expand_factors_with_aliases(factors)
        factors_lower = {f.lower() for f in expanded_factors}
        
        # 收集匹配的素材，带分数
        matched_with_score: List[tuple[SnippetEntry, float]] = []
        matched_ids: Set[str] = set()
        
        for entry in self._snippets:
            if entry.snippet_id in matched_ids:
                continue
            
            # 角色过滤
            if roles and entry.role not in roles:
                continue
            
            # 提取素材的因子触发词
            snippet_factors = self._extract_factors(entry.factor_trigger)
            snippet_factors_lower = {f.lower() for f in snippet_factors}
            
            # 精确匹配
            exact_match = len(factors_lower.intersection(snippet_factors_lower))
            
            # Task 5.2: 前缀匹配
            prefix_match = 0
            for factor in factors_lower:
                for trigger in snippet_factors_lower:
                    if trigger.startswith(factor) or factor.startswith(trigger):
                        if factor != trigger:  # 避免重复计算精确匹配
                            prefix_match += 1
            
            total_score = exact_match + prefix_match * 0.5
            
            if total_score > 0:
                # Task 5.3: 体系优先级
                if engine_id and engine_id in ENGINE_TO_CORPUS:
                    preferred_sources = ENGINE_TO_CORPUS[engine_id]
                    if entry.source_book in preferred_sources:
                        total_score *= 1.5
                
                matched_ids.add(entry.snippet_id)
                matched_with_score.append((entry, total_score))
        
        # 按分数排序，同分按角色优先级
        matched_with_score.sort(
            key=lambda x: (-x[1], self.ROLE_PRIORITY.get(x[0].role, 99))
        )
        
        return [entry for entry, _ in matched_with_score[:max_results]]
    
    def get_fallback_snippets(
        self,
        engine_id: str,
        max_results: int = 3,
    ) -> List[SnippetEntry]:
        """
        获取体系通用 fallback 素材 (Task 5.4)
        
        Args:
            engine_id: 引擎 ID
            max_results: 最大返回数量
            
        Returns:
            通用素材列表
        """
        triggers = ENGINE_FALLBACK_TRIGGERS.get(engine_id, ["通用"])
        return self.find_by_factors(triggers, max_results=max_results, engine_id=engine_id)
    
    def find_by_book(
        self,
        book_id: str,
        max_results: int = 20,
    ) -> List[SnippetEntry]:
        """按书籍查找素材"""
        self.ensure_loaded()
        return self._by_book.get(book_id, [])[:max_results]
    
    def format_for_prompt(
        self,
        snippets: List[SnippetEntry],
        include_source: bool = True,
        max_chars: int = 1500,
    ) -> str:
        """
        将素材格式化为 Prompt 注入格式
        
        Args:
            snippets: 素材列表
            include_source: 是否包含来源引用
            max_chars: 最大字符数
            
        Returns:
            格式化后的字符串
        """
        if not snippets:
            return ""
        
        lines = []
        total_chars = 0
        
        for entry in snippets:
            if include_source:
                line = f"- {entry.snippet_text} → {entry.source_ref}"
            else:
                line = f"- {entry.snippet_text}"
            
            if total_chars + len(line) > max_chars:
                break
            
            lines.append(line)
            total_chars += len(line) + 1  # +1 for newline
        
        return "\n".join(lines)
    
    def get_stats(self) -> Dict[str, int]:
        """获取统计信息"""
        self.ensure_loaded()
        return {
            "total_snippets": len(self._snippets),
            "total_books": len(self._by_book),
            "total_factors": len(self._by_factor),
        }


# 便捷函数
def get_snippet_service() -> NarrativeSnippetService:
    """获取叙事素材服务单例"""
    return NarrativeSnippetService.get_instance()
