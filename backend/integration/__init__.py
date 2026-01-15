"""
LucidSelf Integration Module - Layer 4 Fusion

多体系融合层，负责：
- FusionEngine: 多引擎结果融合
- WeightManager: 权重管理
- CrossValidator: 交叉验证
- ThemeMapper: 主题映射
- EvidenceChainBuilder: 证据链构建

对照文档:
- docs/ls_engine_architecture_v3.md §Layer 4
- .kiro/specs/layer4-fusion/

复用组件:
- ConflictResolver from backend.rules.conflict
- DimensionMapper from backend.rules.dimension
- FusionResult, ConflictWarning from backend.core.contracts
"""

from backend.integration.models import WeightedResult
from backend.integration.weight_manager import WeightManager
from backend.integration.cross_validator import CrossValidator
from backend.integration.theme_mapper import ThemeMapper
from backend.integration.evidence_chain import EvidenceChainBuilder
from backend.integration.fusion_engine import FusionEngine

__all__ = [
    "WeightedResult",
    "WeightManager",
    "CrossValidator",
    "ThemeMapper",
    "EvidenceChainBuilder",
    "FusionEngine",
]
