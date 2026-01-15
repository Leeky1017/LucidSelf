"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699364
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
    semantic_id="zw_v1.0.0_刘都衙命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 刘都衙命(SemanticEntry):
    """
    - 分字分词释义：

  - **贞破卯酉**：廉贞破军在卯酉宫，主公门之命。
  - **生逢落子陷地**：生时逢落陷之地，不能发达。
  - **公门中轩昂**：在官署中略有威风，但难飞黄腾达。
...
    """
    
    original_text: str = """- 分字分词释义：

  - **贞破卯酉**：廉贞破军在卯酉宫，主公门之命。
  - **生逢落子陷地**：生时逢落陷之地，不能发达。
  - **公门中轩昂**：在官署中略有威风，但难飞黄腾达。
  - **二限到夹地**：大小限皆到夹地，主凶祸。
  - **文昌见贪破**：文昌遇贪狼破军，主公门是非。
  - **羊铃同见**：擎羊铃星同见，主凶亡。
  - **阳男火六局**：刘都衙命盘的五行局数，火六局主热情执行。

- **原文（source_text）**：  
  刘都衙命。阳男火六局。贞破卯酉，作公人权禄，虽生逢落子陷地，不能发达，不过公门中轩昂而已。二限到夹地，不免凶祸，且文昌不宜见贪破，又见羊铃，故主凶亡。

- **规范化释义（primary_lang_explained）**：  
  刘都衙命属阳男火六局，廉贞破军在卯酉，为公门之命，生逢落子陷地不能发达，公门中轩昂而已。二限到夹地，文昌见贪破又见羊铃，故凶亡。

- **完整对等诠释（secondary_lang_full）**：  
  Liu Duya's Yang male Fire Sixth chart has Lian Zhen‑Po Jun at Mao‑You—official gate destiny. Born at fallen position cannot flourish, just prominent in office. Both periods flanked; Wenchang sees Tan‑Po with Blade‑Bell. Violent death.

- **核心要点**：  
  1. 廉贞破军卯酉，公门之命。  
  2. 生逢陷地，不能发达。  
  3. 二限夹地、文昌见贪破羊铃，为凶亡应期。

- **叙事素材（narrative_snippets）**：
  - **公门之命**："贞破卯酉，作公人权禄"，刘都衙命主一生多在官署衙门中求存，权禄系于公门。
  - **陷地难发**："虽生逢落子陷地，不能发达，不过公门中轩昂而已"，落陷之地使其难以真正飞黄腾达，只能在体制内略有威风。
  - **夹地羊铃**："二限到夹地，不免凶祸，且文昌不宜见贪破，又见羊铃，故主凶亡"，夹地配贪破羊铃，为公门是非、刑戮之象。
  - **现代应用**：体制内打工者，若命局多陷地又逢羊铃重叠之年，宜减少卷入权力斗争与灰色地带，避免因制度之网而自伤前途乃至性命。"""
    normalized_text_zh: str = """"""
    subject: str = "刘都衙命"
    factor_refs: list = ['pattern_lianpomaoyu', 'state_shengfengxiandi', 'pattern_wenchangtanpo', 'source_ref', 'rel_liuduya_001', 'pattern_lianpomaoyu', 'rel_liuduya_002', 'state_shengfengxiandi', 'rel_liuduya_003', 'pattern_yanglingtongjian', 'evi_liuduya_001', 'pattern_yanglingtongjian', 'rule_jiadi_yangling', 'concept_lian_po', 'concept_fallen_born']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_刘都衙命_001_L1",
    )
    version: str = "1.0.0"
