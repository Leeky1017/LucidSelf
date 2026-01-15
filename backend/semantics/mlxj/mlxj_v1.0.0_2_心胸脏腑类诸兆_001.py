"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.836945
Version: 1.0.0

对照 Requirements 6.4 - 带 @SemanticRegistry.register 装饰器的 Python 模块
"""

from backend.semantics.core.base import SemanticEntry, SemanticRegistry, NarrativeSnippetExtended
from backend.core.contracts import (
    SnippetRole,
    SourceMetadata,
    ConfigRelation,
    EvidenceChainEntry,
    RelationType,
    EffectDirection,
    ConfidenceLevel,
)


@SemanticRegistry.register(
    semantic_id="mlxj_v1.0.0_2_心胸脏腑类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 2心胸脏腑类诸兆(SemanticEntry):
    """
    #### 心胸类汇总

**大吉类**：
- 以刀开心大吉：心窍通，郑玄典故
- 取人心肝吉：大得民心（唐张俭典故）
- 胸前心坎大如斗大吉：心宽意乐
- 胸傍出火焰吉：赵方典故

**吉类**：
-...
    """
    
    original_text: str = """#### 心胸类汇总

**大吉类**：
- 以刀开心大吉：心窍通，郑玄典故
- 取人心肝吉：大得民心（唐张俭典故）
- 胸前心坎大如斗大吉：心宽意乐
- 胸傍出火焰吉：赵方典故

**吉类**：
- 胸中出锦绣纨绮吉：文章锦绣
- 胸前悬镜吉：大将登坛
- 胸光如水晶吉：胸中灵秀
- 胸挂虎形吉：君子成虎变
- 胸生逆鳞大吉：龙形，贵无上
- 胸藏笔吉：词章都丽

**凶类**：
- 胸露骨无肤凶：心膂暴露

#### 脏腑肠胃类汇总

**大吉类**：
- 盛脏满盆见五色大吉：文章华丽
- 洗涤肠胃吉：弃旧更新（王仁裕典故）
- 肺上生花吉：文思生花
- 掘地得自己肺腑大吉：贫得财，富增万金

**吉类**：
- 自灌水入脏吉：水为金子
- 胃脘开豁吉：时运通达
- 肺生两翼吉：金气有余
- 换易肺腑吉：改恶从善（冯俊典故）
- 肺肝如石吉：福至病痊
- 抽取人肠吉：得人之长

**凶类**：
- 肺肝被虎食凶：身陷虎口"""
    normalized_text_zh: str = """"""
    subject: str = "2 心胸脏腑类诸兆"
    factor_refs: list = []
    
    # 叙事素材（包含 trigger_human）
    narrative_snippets: list = [

    ]
    
    # L2.5 因子关系
    related_semantics: list = [

    ]
    
    # L2.5 证据链
    evidence_refs: list = [

    ]
    
    metadata: SourceMetadata = SourceMetadata(
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_2_心胸脏腑类诸兆_001_L1",
    )
    version: str = "1.0.0"
