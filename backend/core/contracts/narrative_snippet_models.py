"""
Narrative Snippet Models for LucidSelf Contracts

叙事素材 Schema 定义，包括叙事片段、逻辑链和组装协议。
对照文档: docs/数据契约_Schema定义规范_v1.md §3.4-3.6

v1.1 新增内容：
- NarrativeSnippet: 叙事素材（§3.4）
- LogicChain: 逻辑链（§3.5）
- AssemblyProtocol: 组装协议（§3.6）
"""

from enum import Enum
from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

from backend.core.contracts.base import (
    VERSION_PATTERN,
    SourceMetadata,
)


# =============================================================================
# 叙事素材正则模式
# =============================================================================

SNIPPET_ID_PATTERN = r"^[a-z][a-z0-9_]*_\d{3}$"
"""叙事素材ID正则: 书籍简称_主题_序号，如 dts_jia_spring_001"""

CHAIN_ID_PATTERN = r"^chain_[a-z0-9_]+$"
"""逻辑链ID正则: chain_书籍简称，如 chain_ditianshui"""

PROTOCOL_ID_PATTERN = r"^asm_[a-z0-9_]+$"
"""组装协议ID正则: asm_协议名，如 asm_career_standard"""


# =============================================================================
# 叙事素材枚举定义 (§3.4, §3.6)
# =============================================================================


class SnippetRole(str, Enum):
    """
    叙事素材逻辑角色枚举
    
    对照文档 §3.4 SnippetRole
    仅允许五个枚举值
    """
    MAIN = "主干"              # 核心论述
    MAIN_DEPENDENCY = "主干依赖"  # 主干成立的前提
    CONDITIONAL = "条件分支"     # 特定条件下的变体
    EXCEPTION = "例外处理"       # 异常情况
    SUMMARY = "总结"            # 归纳性陈述


class ConflictResolutionStrategy(str, Enum):
    """
    冲突解决策略枚举
    
    对照文档 §3.6 ConflictResolutionStrategy
    """
    PRIORITY_BASED = "priority_based"      # 按优先级选择
    WEIGHT_BASED = "weight_based"          # 按权重选择
    CONFIDENCE_BASED = "confidence_based"  # 按置信度选择
    SOURCE_BASED = "source_based"          # 按典籍权威性选择
    MERGE = "merge"                        # 合并展示（标注分歧）


class NarrativeOrderStrategy(str, Enum):
    """
    叙事顺序策略枚举
    
    对照文档 §3.6 NarrativeOrderStrategy
    """
    LOGIC_CHAIN = "logic_chain"            # 按逻辑链顺序
    CONFIDENCE_DESC = "confidence_desc"    # 按置信度降序
    DIMENSION_GROUP = "dimension_group"    # 按维度分组
    CHRONOLOGICAL = "chronological"        # 按时间顺序（流年类）


# =============================================================================
# NarrativeSnippet (§3.4)
# =============================================================================


class NarrativeSnippet(BaseModel):
    """
    配置态叙事素材
    
    承载从典籍精校与L2语义提取得到的原子化叙事片段。
    对照文档 §3.4 NarrativeSnippet
    
    约束：
    - snippet_text 长度 5-200 字符
    - role 仅允许五个枚举值
    """
    # 标识
    snippet_id: str = Field(
        ...,
        pattern=SNIPPET_ID_PATTERN,
        description="叙事素材ID，格式：书籍简称_主题_序号"
    )
    
    # 触发条件
    trigger_condition: str = Field(
        ...,
        description="触发条件，与因子/规则系统共享命名空间，如：day_master=甲 AND month∈[寅,卯]"
    )
    
    # 逻辑角色
    role: SnippetRole = Field(..., description="在推理链中的逻辑位置")
    
    # 语言与内容
    primary_lang: Literal["zh-CN", "en-US"] = Field(
        ...,
        description="主语种，中文典籍为zh-CN，英文典籍为en-US"
    )
    snippet_text: str = Field(
        ...,
        min_length=5,
        max_length=200,
        description="精校后的主语种短句，建议10-40字/词，满足原子化原则"
    )
    
    # 溯源
    source_ref: str = Field(
        ...,
        description="来源引用，格式：《书名》#章节#行号"
    )
    metadata: SourceMetadata = Field(..., description="溯源元数据")
    
    # 关联
    related_factors: List[str] = Field(
        default_factory=list,
        description="关联的factor_id列表"
    )
    related_rules: List[str] = Field(
        default_factory=list,
        description="关联的rule_id列表"
    )
    
    # 版本
    version: str = Field(
        ...,
        pattern=VERSION_PATTERN,
        description="版本号 x.y.z"
    )
    engine_id: str = Field(..., description="所属引擎ID")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "snippet_id": "dts_jia_spring_001",
                "trigger_condition": "day_master=甲 AND month∈[寅,卯]",
                "role": "主干",
                "primary_lang": "zh-CN",
                "snippet_text": "甲木生于春，得时得令，如参天大树。",
                "source_ref": "《滴天髓》#通神论#L23",
                "metadata": {
                    "book_id": "ditianshui",
                    "chapter": "通神论",
                    "l1_anchor": "DTS_L1_023"
                },
                "related_factors": ["day_master_jia", "season_spring"],
                "related_rules": ["rule_jia_spring_strong"],
                "version": "1.0.0",
                "engine_id": "bazi_semantic"
            }
        }
    )


# =============================================================================
# LogicChain Components (§3.5)
# =============================================================================


class LogicNode(BaseModel):
    """
    逻辑链节点
    
    对照文档 §3.5 LogicNode
    """
    node_id: str = Field(..., description="节点ID")
    snippet_ids: List[str] = Field(
        ...,
        description="关联的NarrativeSnippet ID列表"
    )
    role: SnippetRole = Field(..., description="节点在推理链中的角色")
    condition: Optional[str] = Field(None, description="节点激活条件")
    summary: str = Field(..., description="节点语义摘要")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "node_id": "n1",
                "snippet_ids": ["dts_jia_001", "dts_jia_002"],
                "role": "主干",
                "condition": None,
                "summary": "甲木基本特性"
            }
        }
    )


class LogicEdge(BaseModel):
    """
    逻辑链边
    
    对照文档 §3.5 LogicEdge
    """
    from_node: str = Field(..., description="起始节点ID")
    to_node: str = Field(..., description="目标节点ID")
    relation: Literal["depends_on", "leads_to", "conflicts_with", "supports"] = Field(
        ...,
        description="边的关系类型"
    )
    condition: Optional[str] = Field(None, description="边的激活条件")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "from_node": "n1",
                "to_node": "n2",
                "relation": "leads_to",
                "condition": None
            }
        }
    )


class LogicChain(BaseModel):
    """
    逻辑链 - 单书推理结构
    
    由Logic-Agent构建的推理结构，连接叙事素材形成完整的论证链。
    每本书产出一个逻辑链文件。
    对照文档 §3.5 LogicChain
    
    约束：edges 引用的节点必须存在于 nodes 中
    注意：LogicChain 没有 engine_id 字段（书籍级别结构）
    """
    # 标识
    chain_id: str = Field(
        ...,
        pattern=CHAIN_ID_PATTERN,
        description="逻辑链ID，格式：chain_书籍简称"
    )
    book_id: str = Field(..., description="来源书籍ID")
    
    # 结构
    nodes: List[LogicNode] = Field(..., description="逻辑节点列表")
    edges: List[LogicEdge] = Field(..., description="逻辑边列表")
    
    # 叙事顺序
    narrative_order: List[str] = Field(
        ...,
        description="推荐的叙事输出顺序（节点ID列表）"
    )
    
    # 入口与出口
    entry_nodes: List[str] = Field(
        ...,
        description="入口节点ID列表（无前置依赖）"
    )
    terminal_nodes: List[str] = Field(
        ...,
        description="终端节点ID列表（总结性节点）"
    )
    
    # 元数据
    metadata: SourceMetadata = Field(..., description="溯源元数据")
    version: str = Field(
        ...,
        pattern=VERSION_PATTERN,
        description="版本号 x.y.z"
    )

    @model_validator(mode='after')
    def validate_edge_references(self) -> 'LogicChain':
        """确保所有边引用的节点都存在"""
        node_ids = {n.node_id for n in self.nodes}
        for edge in self.edges:
            if edge.from_node not in node_ids:
                raise ValueError(f"Edge references non-existent node: {edge.from_node}")
            if edge.to_node not in node_ids:
                raise ValueError(f"Edge references non-existent node: {edge.to_node}")
        return self

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "chain_id": "chain_ditianshui",
                "book_id": "ditianshui",
                "nodes": [
                    {"node_id": "n1", "snippet_ids": ["dts_jia_001"], "role": "主干", "summary": "甲木基本特性"},
                    {"node_id": "n2", "snippet_ids": ["dts_jia_002"], "role": "条件分支", "summary": "春季特殊表现"}
                ],
                "edges": [
                    {"from_node": "n1", "to_node": "n2", "relation": "leads_to"}
                ],
                "narrative_order": ["n1", "n2"],
                "entry_nodes": ["n1"],
                "terminal_nodes": ["n2"],
                "metadata": {
                    "book_id": "ditianshui",
                    "chapter": "全书",
                    "l1_anchor": "DTS_CHAIN"
                },
                "version": "1.0.0"
            }
        }
    )


# =============================================================================
# AssemblyProtocol (§3.6)
# =============================================================================


class AssemblyProtocol(BaseModel):
    """
    组装协议
    
    定义规则命中后如何组装叙事素材，包括冲突解决、叙事顺序和风格控制。
    对照文档 §3.6 AssemblyProtocol
    
    注意：AssemblyProtocol 没有 engine_id 字段（跨引擎协议）
    """
    # 标识
    protocol_id: str = Field(
        ...,
        pattern=PROTOCOL_ID_PATTERN,
        description="协议ID，格式：asm_协议名"
    )
    
    # 适用范围
    target_dimensions: List[str] = Field(
        ...,
        description="适用的维度列表，如：['事业', '财富']"
    )
    target_engines: List[str] = Field(
        default_factory=list,
        description="适用的引擎ID列表，空表示全部"
    )
    
    # 冲突解决
    conflict_resolution: ConflictResolutionStrategy = Field(
        default=ConflictResolutionStrategy.PRIORITY_BASED,
        description="冲突解决策略"
    )
    
    # 叙事顺序
    narrative_order: NarrativeOrderStrategy = Field(
        default=NarrativeOrderStrategy.LOGIC_CHAIN,
        description="叙事顺序策略"
    )
    
    # 素材选择
    max_snippets_per_dimension: int = Field(
        default=5,
        ge=1,
        le=20,
        description="每个维度最多选择的素材数量"
    )
    role_priority: List[SnippetRole] = Field(
        default_factory=lambda: [
            SnippetRole.MAIN,
            SnippetRole.MAIN_DEPENDENCY,
            SnippetRole.CONDITIONAL,
            SnippetRole.EXCEPTION,
            SnippetRole.SUMMARY,
        ],
        description="角色优先级顺序"
    )
    
    # 输出控制
    include_source_citation: bool = Field(
        default=True,
        description="是否包含典籍引用"
    )
    include_confidence_indicator: bool = Field(
        default=False,
        description="是否显示置信度指示"
    )
    
    # 版本
    version: str = Field(
        ...,
        pattern=VERSION_PATTERN,
        description="版本号 x.y.z"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "protocol_id": "asm_career_standard",
                "target_dimensions": ["事业", "财富"],
                "target_engines": [],
                "conflict_resolution": "priority_based",
                "narrative_order": "logic_chain",
                "max_snippets_per_dimension": 5,
                "role_priority": ["主干", "主干依赖", "条件分支", "例外处理", "总结"],
                "include_source_citation": True,
                "include_confidence_indicator": False,
                "version": "1.0.0"
            }
        }
    )
