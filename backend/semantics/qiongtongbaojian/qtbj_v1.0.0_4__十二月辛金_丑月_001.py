"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578432
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
    semantic_id="qtbj_v1.0.0_4__十二月辛金_丑月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 4十二月辛金丑月(SemanticEntry):
    """
    - **原文（source_text）**：
  十二月辛金，寒冻之极，先丙后壬，无丙不能解冻，无壬不能洗淘。丙壬两透，金马玉堂之客。壬丙俱藏，游庠食饩之人。有丙无壬富真贵假。有壬乏丙，贱而且贫。或丙...
    """
    
    original_text: str = """- **原文（source_text）**：
  十二月辛金，寒冻之极，先丙后壬，无丙不能解冻，无壬不能洗淘。丙壬两透，金马玉堂之客。壬丙俱藏，游庠食饩之人。有丙无壬富真贵假。有壬乏丙，贱而且贫。或丙多、无壬、有癸，市中贸易之流。
  或水多、有戊己出干，又有丙丁，必主衣食充盈，一生安乐。
  十二月辛金，丙先壬后，戊己次之。

- **分字分词释义**：
  - **寒冻之极**：极度寒冷冰冻 / 丑月特点 / 需丙解
  - **解冻**：融化冰冻 / 丙火作用 / 调候
  - **洗淘**：冲洗淘涤 / 壬水作用 / 清金
  - **金马玉堂**：翰林院 / 丙壬两透 / 大贵
  - **游庠食饩**：在学校读书吃俸禄 / 秀才 / 次吉
  - **富真贵假**：真富假贵 / 有丙无壬 / 次吉
  - **贱而且贫**：卑贱且贫穷 / 有壬乏丙 / 凶象
  - **市中贸易**：市场商贩 / 丙多无壬有癸 / 次吉
  - **衣食充盈**：衣食丰足 / 戊己丙丁配合 / 吉象

- **规范化释义（primary_lang_explained）**：
  十二月（丑月）辛金寒冻之极先丙后壬无丙不能解冻无壬不能洗淘。丙壬两透金马玉堂之客。壬丙俱藏游庠食饩之人。有丙无壬富真贵假。有壬乏丙贱而且贫。或丙多无壬有癸市中贸易之流。
  或水多有戊己出干又有丙丁必主衣食充盈一生安乐。
  十二月辛金丙先壬后戊己次之。

- **完整对等诠释（secondary_lang_full）**：
  Xin Metal in 12th Month (Ox Month): extreme cold-frozen. First Bing then Ren. Without Bing cannot unfreeze without Ren cannot wash. Bing/Ren revealing Golden Horse Jade Hall guest. Ren/Bing both hidden academy student with stipend. Having Bing without Ren wealthy-true noble-false. Having Ren lacking Bing lowly且poor. If Bing many no Ren having Gui market trader.
  If Water many Wu/Ji revealing also Bing/Ding surely food-clothing abundant life peaceful.
  12th month Xin Metal: Bing first Ren second Wu/Ji next.

- **核心要点**：
  - **配合**：戊己（止水护金）
  - **丑月特点**：寒湿冻土非丙不暖非壬不清

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_399]` `[trigger: 辛生丑月]` `[factor_trigger: month_chou AND tiangan_xin AND tiangan_bing AND tiangan_ren]` `[role: 主干]` 十二月辛金，寒冻之极，先丙后壬，无丙不能解冻，无壬不能洗淘。 → 《穷通宝鉴·三冬辛金》#34.4
  - `[ns_qttbj_400]` `[trigger: 丙壬两透]` `[factor_trigger: month_chou AND tiangan_xin AND bing_revealed AND ren_revealed]` `[role: 条件分支]` 丙壬两透，金马玉堂之客。壬丙俱藏，游庞食饿之人。 → 《穷通宝鉴·三冬辛金》#34.4
  - `[ns_qttbj_401]` `[trigger: 有壬乏丙]` `[factor_trigger: month_chou AND tiangan_xin AND tiangan_ren AND NOT tiangan_bing]` `[role: 例外处理]` 有壬乏丙，贱而且贫。 → 《穷通宝鉴·三冬辛金》#34.4
  - `[ns_qttbj_402]` `[trigger: 丑月总结]` `[factor_trigger: month_chou AND tiangan_xin AND priority_bing_ren]` `[role: 总结]` 十二月辛金，丙先壬后，戊己次之。 → 《穷通宝鉴·三冬辛金》#34.4"""
    normalized_text_zh: str = """"""
    subject: str = "4. 十二月辛金（丑月）"
    factor_refs: list = ['golden_horse_jade_hall', 'academy_student_stipend', 'bing_unfreeze']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_4__十二月辛金_丑月_001_L1",
    )
    version: str = "1.0.0"
