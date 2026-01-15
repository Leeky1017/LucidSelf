"""
时间线推演器

基于 temporal 因子和规则结果，推演未来时间线。

对照文档: docs/ls_roadmap_executable.md §四、Phase 2: 时间线建模

核心功能:
1. 提取 temporal 类因子（流年/大运/流月/过境等）
2. 按时间桶聚合规则结果
3. 生成 TimelineNode 序列
4. 识别关键分支点（BranchPoint）
"""

import logging
import uuid
from collections import defaultdict
from datetime import date
from typing import Any, Dict, List, Optional

from backend.core.contracts import FactorMatrix, RuntimeRuleResult
from backend.core.contracts.unified_dimensions import (
    AnalysisDimension,
    DimensionRegistry,
    LifeDomain,
)
from backend.core.contracts.unified_time import (
    BranchPoint,
    TimeBucket,
    TimeBucketGranularity,
    TimeHorizon,
    TimelineNode,
    TimelineProjection,
    TimeRegistry,
)

logger = logging.getLogger(__name__)


# =============================================================================
# 时间因子模式匹配
# =============================================================================

TEMPORAL_FACTOR_PATTERNS = [
    # 八字
    "liunian",    # 流年
    "dayun",      # 大运
    "liuyue",     # 流月
    "liuri",      # 流日
    # 紫微
    "daxian",     # 大限
    # 占星
    "transit",    # 行星过境
    "solar_return",  # 太阳回归
    "lunar_return",  # 月亮回归
    "progression",   # 推运
]


class TimelineProjector:
    """
    时间线推演器
    
    职责:
    - 提取 temporal 类因子
    - 按时间桶聚合规则结果
    - 生成 TimelineNode 序列
    - 识别关键分支点
    
    使用方式:
        projector = TimelineProjector()
        projection = projector.project(
            factor_matrix=matrix,
            rule_results=results,
            years=3,
        )
    """
    
    # 默认置信度（MVP阶段固定值，后续接入更精确模型）
    DEFAULT_CONFIDENCE = 0.6
    
    # 分支点阈值：风险因子数 >= 此值则标记为分支点
    BRANCH_POINT_THRESHOLD = 2
    
    # 最大分支点数量
    MAX_BRANCH_POINTS = 5
    
    def __init__(self):
        """初始化推演器"""
        pass
    
    def project(
        self,
        factor_matrix: FactorMatrix,
        rule_results: List[RuntimeRuleResult],
        scenario_id: Optional[str] = None,
        user_id: Optional[str] = None,
        horizon: TimeHorizon = TimeHorizon.LONG_TERM,
        years: int = 3,
        start_date: Optional[date] = None,
    ) -> TimelineProjection:
        """
        基于因子和规则结果，推演未来时间线
        
        Args:
            factor_matrix: 因子矩阵
            rule_results: 规则匹配结果
            scenario_id: 场景 ID
            user_id: 用户 ID
            horizon: 时间视野
            years: 预测年数
            start_date: 起始日期（默认今天）
            
        Returns:
            TimelineProjection 完整时间线预测
        """
        start = start_date or date.today()
        end = date(start.year + years, start.month, min(start.day, 28))
        
        # 1. 提取 temporal 类因子
        temporal_factors = self._extract_temporal_factors(factor_matrix)
        logger.debug(f"Extracted {len(temporal_factors)} temporal factors")
        
        # 2. 确定时间桶粒度
        granularity = TimeRegistry.get_granularity_for_horizon(horizon)
        
        # 3. 生成时间桶序列
        buckets = TimeRegistry.generate_buckets(start, end, granularity)
        logger.debug(f"Generated {len(buckets)} time buckets with {granularity.value} granularity")
        
        # 4. 预处理规则结果：按维度分组
        rules_by_dimension = self._group_rules_by_dimension(rule_results)
        
        # 5. 为每个时间桶生成节点
        nodes = []
        for bucket in buckets:
            node = self._project_bucket(
                bucket=bucket,
                temporal_factors=temporal_factors,
                rules_by_dimension=rules_by_dimension,
                all_rules=rule_results,
            )
            nodes.append(node)
        
        # 6. 识别分支点
        branch_points = self._identify_branch_points(nodes, rule_results)
        
        # 7. 计算整体置信度
        avg_confidence = (
            sum(n.confidence for n in nodes) / len(nodes)
            if nodes else self.DEFAULT_CONFIDENCE
        )
        
        projection = TimelineProjection(
            projection_id=self._gen_id("proj"),
            user_id=user_id or "",
            scenario_id=scenario_id or "",
            horizon=horizon,
            granularity=granularity,
            start_date=start,
            end_date=end,
            nodes=nodes,
            branch_points=branch_points,
            confidence=avg_confidence,
        )
        
        logger.info(
            f"Generated timeline projection: {len(nodes)} nodes, "
            f"{len(branch_points)} branch points, confidence={avg_confidence:.2f}"
        )
        
        return projection
    
    def _extract_temporal_factors(
        self, 
        matrix: FactorMatrix,
    ) -> Dict[str, Any]:
        """
        提取时间类因子
        
        通过模式匹配识别与时间相关的因子。
        
        Returns:
            factor_id → FactorValue 的映射
        """
        result = {}
        
        for factor_id, factor_value in matrix.factors.items():
            factor_lower = factor_id.lower()
            
            # 检查是否匹配任何 temporal 模式
            for pattern in TEMPORAL_FACTOR_PATTERNS:
                if pattern in factor_lower:
                    result[factor_id] = factor_value
                    break
        
        return result
    
    def _group_rules_by_dimension(
        self,
        rules: List[RuntimeRuleResult],
    ) -> Dict[str, List[RuntimeRuleResult]]:
        """按维度分组规则结果"""
        grouped = defaultdict(list)
        
        for rule in rules:
            if rule.matched and rule.dimension:
                grouped[rule.dimension].append(rule)
        
        return grouped
    
    def _project_bucket(
        self, 
        bucket: TimeBucket,
        temporal_factors: Dict[str, Any],
        rules_by_dimension: Dict[str, List[RuntimeRuleResult]],
        all_rules: List[RuntimeRuleResult],
    ) -> TimelineNode:
        """
        推演单个时间桶
        
        计算该时间段内各生活领域的预期得分。
        """
        # 计算各领域得分
        domain_scores = self._calculate_domain_scores(rules_by_dimension)
        
        # 提取有利因子（吉利规则）
        favorable = self._extract_favorable_factors(all_rules)
        
        # 提取风险因子（凶险规则）
        risks = self._extract_risk_factors(all_rules)
        
        # 提取关键事件提示
        key_events = self._extract_key_events(all_rules, bucket)
        
        # 提取建议行动
        suggested_actions = self._extract_suggested_actions(all_rules)
        
        # 识别贡献体系
        contributing_systems = self._identify_contributing_systems(all_rules)
        
        # 计算置信度（基于 temporal 因子数量和规则匹配数）
        confidence = self._calculate_node_confidence(
            temporal_factors, 
            all_rules,
        )
        
        return TimelineNode(
            node_id=self._gen_node_id(bucket),
            bucket=bucket,
            domain_scores=domain_scores,
            favorable_factors=favorable[:5],
            risk_factors=risks[:5],
            key_events=key_events[:3],
            suggested_actions=suggested_actions[:3],
            confidence=confidence,
            source_factors=list(temporal_factors.keys())[:10],
            source_rules=[r.rule_id for r in all_rules if r.matched][:10],
            contributing_systems=contributing_systems,
        )
    
    def _calculate_domain_scores(
        self,
        rules_by_dimension: Dict[str, List[RuntimeRuleResult]],
    ) -> Dict[str, float]:
        """
        计算各生活领域得分
        
        通过分析维度映射到生活领域，计算加权平均分。
        """
        # 分析维度 → 生活领域的映射
        domain_scores: Dict[str, List[float]] = defaultdict(list)
        
        for dim_str, rules in rules_by_dimension.items():
            # 标准化维度
            try:
                dim = DimensionRegistry.normalize_dimension(dim_str)
                domains = DimensionRegistry.get_domains_for_dimension(dim)
                
                # 计算该维度的平均分（使用 weight 作为得分基础）
                if rules:
                    # 归一化：weight范围 0-10 转换为 0-1
                    avg_score = sum(min(r.weight / 10.0, 1.0) for r in rules) / len(rules)
                    
                    # 分配到相关领域
                    for domain in domains:
                        domain_scores[domain.value].append(avg_score)
            except Exception:
                # 未知维度，归入 general
                if rules:
                    avg_score = sum(min(r.weight / 10.0, 1.0) for r in rules) / len(rules)
                    domain_scores["general"].append(avg_score)
        
        # 聚合为最终得分
        result = {}
        for domain_str, scores in domain_scores.items():
            if scores:
                result[domain_str] = sum(scores) / len(scores)
        
        # 确保核心领域有值
        for domain in [LifeDomain.CAREER, LifeDomain.WEALTH, 
                       LifeDomain.RELATIONSHIP, LifeDomain.HEALTH]:
            if domain.value not in result:
                result[domain.value] = 0.5  # 默认中等
        
        return result
    
    def _extract_favorable_factors(
        self,
        rules: List[RuntimeRuleResult],
    ) -> List[str]:
        """提取有利因子（吉利规则的描述）"""
        favorable = []
        for rule in rules:
            if rule.matched and rule.level in ["吉", "大吉", "有利", "吉利"]:
                if rule.description:
                    favorable.append(rule.description[:50])
                else:
                    favorable.append(rule.rule_id)
        return favorable
    
    def _extract_risk_factors(
        self,
        rules: List[RuntimeRuleResult],
    ) -> List[str]:
        """提取风险因子（凶险规则的描述）"""
        risks = []
        for rule in rules:
            if rule.matched and rule.level in ["凶", "大凶", "注意", "警告", "不利"]:
                if rule.description:
                    risks.append(rule.description[:50])
                else:
                    risks.append(rule.rule_id)
        return risks
    
    def _extract_key_events(
        self,
        rules: List[RuntimeRuleResult],
        bucket: TimeBucket,
    ) -> List[str]:
        """提取关键事件提示"""
        events = []
        for rule in rules:
            if rule.matched and rule.tags:
                # 查找带有事件标签的规则
                for tag in rule.tags:
                    if any(k in tag.lower() for k in ["事件", "event", "节点", "关键"]):
                        events.append(f"{bucket.label_zh}: {rule.description or rule.rule_id}")
                        break
        return events
    
    def _extract_suggested_actions(
        self,
        rules: List[RuntimeRuleResult],
    ) -> List[str]:
        """提取建议行动"""
        actions = []
        for rule in rules:
            if rule.matched and rule.cross_domain_axes:
                # 从跨域轴提取建议类型
                if rule.cross_domain_axes.advice_type:
                    for advice in rule.cross_domain_axes.advice_type:
                        if advice == "action" and rule.description:
                            actions.append(rule.description[:50])
        return actions
    
    def _identify_contributing_systems(
        self,
        rules: List[RuntimeRuleResult],
    ) -> List[str]:
        """识别贡献的分析体系"""
        systems = set()
        for rule in rules:
            if rule.matched and rule.rule_id:
                # 从 rule_id 前缀提取体系名称（如 bazi, astro, ziwei）
                # 规则用 bazi_xxx, astro_xxx 的命名约定
                parts = rule.rule_id.split("_")
                if len(parts) >= 2:
                    system = parts[0].lower()
                    if system in ["bazi", "astro", "ziwei", "tarot", "dream", "yijing"]:
                        systems.add(system)
        return list(systems)[:5]
    
    def _calculate_node_confidence(
        self,
        temporal_factors: Dict[str, Any],
        rules: List[RuntimeRuleResult],
    ) -> float:
        """
        计算节点置信度
        
        基于:
        - temporal 因子数量
        - 匹配规则数量
        - 规则本身的置信度
        """
        # 基础置信度
        base = 0.4
        
        # temporal 因子加成（有则加，最多 +0.2）
        temporal_bonus = min(0.2, len(temporal_factors) * 0.05)
        
        # 匹配规则加成（最多 +0.3）
        matched_rules = [r for r in rules if r.matched]
        rule_bonus = min(0.3, len(matched_rules) * 0.03)
        
        # 规则平均置信度加成
        if matched_rules:
            avg_rule_confidence = (
                sum(r.confidence for r in matched_rules if r.confidence) 
                / len(matched_rules)
            )
            confidence_bonus = avg_rule_confidence * 0.1
        else:
            confidence_bonus = 0
        
        total = base + temporal_bonus + rule_bonus + confidence_bonus
        return min(1.0, max(0.1, total))
    
    def _identify_branch_points(
        self,
        nodes: List[TimelineNode],
        rules: List[RuntimeRuleResult],
    ) -> List[BranchPoint]:
        """
        识别分支点
        
        分支点是需要用户做出决策的关键时刻。
        识别标准:
        1. 风险因子数 >= 阈值
        2. 存在冲突的建议
        """
        branch_points = []
        
        for node in nodes:
            # 条件1: 风险因子数足够
            if len(node.risk_factors) >= self.BRANCH_POINT_THRESHOLD:
                question = self._generate_decision_question(node)
                options = self._generate_options(node)
                
                branch_points.append(BranchPoint(
                    point_id=self._gen_id("bp"),
                    bucket=node.bucket,
                    decision_question=question,
                    options=options,
                    recommendation=options[0] if options else None,
                    source_rules=node.source_rules[:5],
                ))
        
        # 限制数量
        return branch_points[:self.MAX_BRANCH_POINTS]
    
    def _generate_decision_question(self, node: TimelineNode) -> str:
        """生成决策问题"""
        bucket_label = node.bucket.label_zh
        risks_count = len(node.risk_factors)
        
        if risks_count >= 3:
            return f"{bucket_label}期间存在多个风险因素，需要谨慎决策"
        elif risks_count >= 2:
            return f"{bucket_label}期间有挑战，需要考虑应对策略"
        else:
            return f"{bucket_label}期间可能需要做出选择"
    
    def _generate_options(self, node: TimelineNode) -> List[str]:
        """生成决策选项"""
        # 基础选项
        options = ["保守策略：稳健行事，规避风险"]
        
        # 根据领域得分添加选项
        high_scores = [d for d, s in node.domain_scores.items() if s > 0.6]
        if high_scores:
            options.append("积极策略：把握机遇，主动出击")
        
        # 平衡选项
        options.append("平衡策略：稳中求进，灵活应变")
        
        return options[:3]
    
    def _gen_id(self, prefix: str) -> str:
        """生成唯一 ID"""
        return f"{prefix}_{uuid.uuid4().hex[:12]}"
    
    def _gen_node_id(self, bucket: TimeBucket) -> str:
        """生成节点 ID"""
        # 使用时间桶 ID 创建稳定的节点 ID
        safe_id = bucket.bucket_id.replace("-", "_").replace("W", "w")
        return f"n_{safe_id}"


# =============================================================================
# 便捷函数
# =============================================================================

_projector: Optional[TimelineProjector] = None


def get_projector() -> TimelineProjector:
    """获取 TimelineProjector 单例"""
    global _projector
    if _projector is None:
        _projector = TimelineProjector()
    return _projector
