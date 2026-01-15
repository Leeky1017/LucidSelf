"""
场景路由器

将用户问题/意图路由到具体场景，并生成 ScenarioContext 供后续 Pipeline 使用。

三层分类策略：
1. 关键词匹配 (<1ms) - 快速路径
2. 语义匹配 (<10ms) - 备选路径 (TODO: 需要 embedding 模型)
3. LLM fallback (<500ms) - 最终兜底 (TODO: 需要 LLM 集成)

对照文档: docs/ls_roadmap_executable.md §四、场景系统设计
"""

import logging
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from backend.core.contracts.unified_dimensions import (
    DecisionAxis,
    DOMAIN_TO_DECISION_AXES,
    LifeDomain,
    LIFE_DOMAIN_LABELS,
)
from backend.services.scenario.models import (
    ScenarioContext,
    ScenarioKeywords,
    ScenarioRoutingResult,
    ScenarioTemplate,
)

logger = logging.getLogger(__name__)


# 默认场景关键词配置
DEFAULT_SCENARIO_KEYWORDS: Dict[LifeDomain, ScenarioKeywords] = {
    LifeDomain.CAREER: ScenarioKeywords(
        primary=["事业", "工作", "职业", "career", "job", "work"],
        synonyms=["职场", "升职", "跳槽", "转行", "创业", "加薪", "晋升", "老板", "同事", "行业", "岗位"],
        negative=["退休", "辞职后"],
        weight=1.0,
    ),
    LifeDomain.WEALTH: ScenarioKeywords(
        primary=["财富", "财运", "钱", "wealth", "money", "finance"],
        synonyms=["投资", "理财", "收入", "赚钱", "存款", "房子", "股票", "基金", "债务", "贷款"],
        negative=["捐款"],
        weight=1.0,
    ),
    LifeDomain.RELATIONSHIP: ScenarioKeywords(
        primary=["感情", "恋爱", "婚姻", "relationship", "love", "marriage"],
        synonyms=["对象", "相亲", "分手", "复合", "结婚", "离婚", "暗恋", "表白", "约会", "伴侣"],
        negative=[],
        weight=1.0,
    ),
    LifeDomain.HEALTH: ScenarioKeywords(
        primary=["健康", "身体", "疾病", "health", "body", "illness"],
        synonyms=["生病", "医院", "手术", "体检", "养生", "锻炼", "睡眠", "饮食", "压力", "疲劳"],
        negative=[],
        weight=1.0,
    ),
    LifeDomain.FAMILY: ScenarioKeywords(
        primary=["家庭", "家人", "亲属", "family", "relatives"],
        synonyms=["父母", "孩子", "子女", "兄弟", "姐妹", "婆媳", "公婆", "育儿", "养老", "家族"],
        negative=[],
        weight=0.9,
    ),
    LifeDomain.CREATIVITY: ScenarioKeywords(
        primary=["学习", "创造", "考试", "study", "creativity", "exam"],
        synonyms=["读书", "考研", "留学", "技能", "培训", "艺术", "创作", "设计", "写作", "灵感"],
        negative=[],
        weight=0.8,
    ),
    LifeDomain.SPIRITUAL: ScenarioKeywords(
        primary=["精神", "内心", "修行", "spiritual", "mental", "meditation"],
        synonyms=["冥想", "信仰", "宗教", "佛", "道", "心理", "焦虑", "抑郁", "情绪", "自我"],
        negative=[],
        weight=0.8,
    ),
}


class ScenarioRouter:
    """
    场景路由器
    
    职责：
    - 将用户问题/意图路由到具体场景
    - 生成 ScenarioContext 供后续 Pipeline 使用
    - 支持多场景混合识别
    """
    
    # 最低匹配阈值
    MIN_CONFIDENCE = 0.3
    # 混合场景阈值（次场景得分超过此比例视为混合）
    MIXED_THRESHOLD = 0.6
    
    def __init__(
        self,
        templates_dir: Optional[Path] = None,
        custom_keywords: Optional[Dict[LifeDomain, ScenarioKeywords]] = None,
    ):
        """
        初始化路由器
        
        Args:
            templates_dir: 场景模板配置目录
            custom_keywords: 自定义关键词配置
        """
        self._templates_dir = templates_dir or Path("data/scenario_templates")
        self._keywords = custom_keywords or DEFAULT_SCENARIO_KEYWORDS
        self._templates: Dict[LifeDomain, ScenarioTemplate] = {}
        self._load_templates()
    
    def _load_templates(self) -> None:
        """加载场景模板配置"""
        if not self._templates_dir.exists():
            logger.debug(f"Templates directory not found: {self._templates_dir}, using defaults")
            return
        
        for yaml_file in self._templates_dir.glob("*.yaml"):
            try:
                with open(yaml_file, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                if data:
                    template = ScenarioTemplate(**data)
                    self._templates[template.domain] = template
            except Exception as e:
                logger.warning(f"Failed to load template {yaml_file}: {e}")
    
    def route(
        self,
        query: str,
        context: Optional[Dict] = None,
    ) -> ScenarioRoutingResult:
        """
        路由用户问题到场景
        
        三层分类策略：
        1. 关键词匹配 (<1ms) - 快速路径
        2. 语义匹配 (<10ms) - 备选路径
        3. LLM fallback (<500ms) - 最终兜底
        
        Args:
            query: 用户问题/意图文本
            context: 额外上下文信息
            
        Returns:
            ScenarioRoutingResult 包含主场景和备选场景
        """
        start_time = time.time()
        
        # Layer 1: 关键词匹配
        scores = self._keyword_match(query)
        
        if scores and max(scores.values()) >= self.MIN_CONFIDENCE:
            # 关键词匹配成功
            return self._build_result_from_scores(scores, query, start_time, "keyword")
        
        # Layer 2: 语义匹配
        semantic_result = self._semantic_match(query)
        if semantic_result:
            return self._build_result_from_scores(
                semantic_result, query, start_time, "semantic"
            )
        
        # Layer 3: LLM fallback（目前使用简化逻辑）
        llm_result = self._llm_fallback(query)
        if llm_result:
            return self._build_result_from_scores(
                llm_result, query, start_time, "llm"
            )
        
        # 最终兜底：返回默认场景
        primary = self._build_context(
            LifeDomain.CAREER,
            confidence=0.3,
            matched_keywords=[],
            method="default",
        )
        return ScenarioRoutingResult(
            primary=primary,
            routing_time_ms=(time.time() - start_time) * 1000,
        )
    
    def _semantic_match(self, query: str) -> Optional[Dict[LifeDomain, float]]:
        """
        Layer 2: 语义匹配
        
        使用 embedding 向量计算语义相似度。
        """
        try:
            from backend.services.scenario.semantic_matcher import get_semantic_matcher
            
            matcher = get_semantic_matcher()
            if not matcher.is_available():
                logger.debug("Semantic matcher not available, skipping")
                return None
            
            results = matcher.match_with_threshold(query, threshold=0.4)
            
            if results:
                logger.debug(f"Semantic match found: {results}")
                return {domain: score for domain, score in results}
            
            return None
        
        except Exception as e:
            logger.debug(f"Semantic matching failed: {e}")
            return None
    
    def _llm_fallback(self, query: str) -> Optional[Dict[LifeDomain, float]]:
        """
        Layer 3: LLM fallback
        
        使用 LLM 进行复杂问题的场景分类。
        优先使用 LLM，失败时降级到模式匹配。
        """
        # 首先尝试 LLM 调用
        llm_result = self._call_llm_for_classification(query)
        if llm_result:
            return llm_result
        
        # LLM 不可用时降级到模式匹配
        return self._pattern_based_fallback(query)
    
    def _call_llm_for_classification(
        self, 
        query: str,
    ) -> Optional[Dict[LifeDomain, float]]:
        """
        调用 LLM 进行场景分类
        
        使用简短 prompt 让 LLM 返回最相关的领域。
        """
        try:
            from backend.core.llm.client import LLMClient
            from backend.core.llm.cost_monitor import CostMonitor
            
            client = LLMClient()
            if not client.is_available():
                return None
            
            # 构建分类 prompt
            domain_list = ", ".join([d.value for d in LifeDomain])
            prompt = f"""请分析以下用户问题最相关的生活领域。
可选领域: {domain_list}

用户问题: {query}

请仅返回 JSON 格式，例如: {{"career": 0.8, "wealth": 0.3}}
只返回相关度 > 0.3 的领域，分数范围 0-1。"""
            
            # 使用低成本模型
            import asyncio
            try:
                loop = asyncio.get_event_loop()
            except RuntimeError:
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            # 同步调用
            response = loop.run_until_complete(
                client.complete(
                    prompt=prompt,
                    model="gpt-4o-mini",  # 使用低成本模型
                    max_tokens=100,
                    temperature=0.3,
                )
            )
            
            if not response or not response.content:
                return None
            
            # 解析 JSON 响应
            import json
            import re
            
            # 提取 JSON 部分
            content = response.content.strip()
            json_match = re.search(r'\{[^}]+\}', content)
            if not json_match:
                return None
            
            scores_raw = json.loads(json_match.group())
            
            # 转换为 LifeDomain
            scores: Dict[LifeDomain, float] = {}
            for domain_str, score in scores_raw.items():
                try:
                    domain = LifeDomain(domain_str)
                    if score > 0.3:
                        scores[domain] = min(1.0, float(score))
                except ValueError:
                    continue
            
            if scores:
                logger.debug(f"LLM classification: {scores}")
                return scores
            
            return None
            
        except Exception as e:
            logger.debug(f"LLM classification failed: {e}")
            return None
    
    def _pattern_based_fallback(
        self,
        query: str,
    ) -> Optional[Dict[LifeDomain, float]]:
        """基于模式的备用分类"""
        try:
            # 问题类型关键词
            question_patterns = {
                LifeDomain.CAREER: ["什么时候", "适合", "发展", "前景", "机会", "工作"],
                LifeDomain.RELATIONSHIP: ["什么时候", "遇到", "缘分", "适合", "感情"],
                LifeDomain.HEALTH: ["注意", "小心", "怎么办", "状态", "身体"],
                LifeDomain.WEALTH: ["有没有", "机会", "运气", "收益", "投资"],
                LifeDomain.FAMILY: ["孩子", "父母", "家庭", "家人"],
                LifeDomain.CREATIVITY: ["学习", "考试", "创意", "灵感"],
                LifeDomain.SPIRITUAL: ["内心", "迷茫", "意义", "方向"],
            }
            
            scores: Dict[LifeDomain, float] = {}
            query_lower = query.lower()
            
            for domain, patterns in question_patterns.items():
                hit_count = sum(1 for p in patterns if p in query_lower)
                if hit_count > 0:
                    scores[domain] = min(0.45, 0.2 + hit_count * 0.1)
            
            return scores if scores else None
        
        except Exception as e:
            logger.debug(f"Pattern fallback failed: {e}")
            return None
    
    def _build_result_from_scores(
        self,
        scores: Dict[LifeDomain, float],
        query: str,
        start_time: float,
        method: str,
    ) -> ScenarioRoutingResult:
        """从分数构建路由结果"""
        
        # 排序取最高分
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        best_domain, best_score = sorted_scores[0]
        
        # 提取匹配的关键词（仅关键词匹配时有效）
        matched = self._get_matched_keywords(query, best_domain) if method == "keyword" else []
        
        primary = self._build_context(
            best_domain,
            confidence=best_score,
            matched_keywords=matched,
            method=method,
        )
        
        # 检查是否混合场景
        secondary = None
        alternatives = []
        
        if len(sorted_scores) > 1:
            second_domain, second_score = sorted_scores[1]
            if second_score >= best_score * self.MIXED_THRESHOLD:
                # 混合场景
                primary.is_mixed = True
                primary.secondary_domains = [second_domain]
                
                second_matched = self._get_matched_keywords(query, second_domain) if method == "keyword" else []
                secondary = self._build_context(
                    second_domain,
                    confidence=second_score,
                    matched_keywords=second_matched,
                    method=method,
                )
            
            # 备选场景（取前3个非主要的）
            for domain, score in sorted_scores[1:4]:
                if score >= self.MIN_CONFIDENCE:
                    alt_matched = self._get_matched_keywords(query, domain) if method == "keyword" else []
                    alt_ctx = self._build_context(
                        domain,
                        confidence=score,
                        matched_keywords=alt_matched,
                        method=method,
                    )
                    alternatives.append(alt_ctx)
        
        return ScenarioRoutingResult(
            primary=primary,
            secondary=secondary,
            alternatives=alternatives,
            routing_time_ms=(time.time() - start_time) * 1000,
        )
    
    def _keyword_match(self, query: str) -> Dict[LifeDomain, float]:
        """
        关键词匹配
        
        Returns:
            各场景的匹配得分 (0-1)
        """
        scores: Dict[LifeDomain, float] = {}
        query_lower = query.lower()
        
        for domain, keywords in self._keywords.items():
            score = 0.0
            hit_count = 0
            
            # 主关键词（高权重）
            for kw in keywords.primary:
                if kw in query or kw in query_lower:
                    score += 0.4 * keywords.weight
                    hit_count += 1
            
            # 同义词（中权重）
            for kw in keywords.synonyms:
                if kw in query or kw in query_lower:
                    score += 0.2 * keywords.weight
                    hit_count += 1
            
            # 否定词（扣分）
            for kw in keywords.negative:
                if kw in query or kw in query_lower:
                    score -= 0.3
            
            # 命中多个关键词加成
            if hit_count > 1:
                score *= 1 + (hit_count - 1) * 0.1
            
            # 归一化到 0-1
            score = min(1.0, max(0.0, score))
            
            if score > 0:
                scores[domain] = score
        
        return scores
    
    def _get_matched_keywords(self, query: str, domain: LifeDomain) -> List[str]:
        """获取匹配的关键词列表"""
        matched = []
        keywords = self._keywords.get(domain)
        if not keywords:
            return matched
        
        query_lower = query.lower()
        for kw in keywords.primary + keywords.synonyms:
            if kw in query or kw in query_lower:
                matched.append(kw)
        
        return matched
    
    def _build_context(
        self,
        domain: LifeDomain,
        confidence: float,
        matched_keywords: List[str],
        method: str,
    ) -> ScenarioContext:
        """构建场景上下文"""
        # 获取决策维度
        decision_axes = DOMAIN_TO_DECISION_AXES.get(domain, [])
        
        # 如果有模板，使用模板的完整配置
        template = self._templates.get(domain)
        factor_filter = {}
        rule_categories = []
        
        if template:
            decision_axes = template.decision_axes or decision_axes
            factor_filter = {
                "include": template.factor_include_patterns,
                "exclude": template.factor_exclude_patterns,
                "always": template.factor_always_include,
            }
            rule_categories = template.rule_categories
        
        return ScenarioContext(
            scenario_id=f"scn_{domain.value}",
            domain=domain,
            decision_axes=decision_axes,
            confidence=confidence,
            matched_keywords=matched_keywords,
            router_method=method,
            factor_filter=factor_filter,
            rule_categories=rule_categories,
        )
    
    def get_all_domains(self) -> List[LifeDomain]:
        """获取所有支持的场景领域"""
        return list(LifeDomain)
    
    def get_domain_label(self, domain: LifeDomain, lang: str = "zh") -> str:
        """获取场景领域标签"""
        return LIFE_DOMAIN_LABELS.get(domain, {}).get(lang, domain.value)
