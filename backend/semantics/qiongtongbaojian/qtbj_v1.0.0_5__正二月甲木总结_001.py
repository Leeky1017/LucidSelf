"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619829
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
    semantic_id="qtbj_v1.0.0_5__正二月甲木总结_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 5正二月甲木总结(SemanticEntry):
    """
    - **原文（source_text）**：
  凡三春甲木，用庚者，土为妻，金为子。用丁者，木为妻，火为子。
  总之正二月甲木，有庚戊者上命。如有丁透，大富大贵之命也。

- **分字分词释义**...
    """
    
    original_text: str = """- **原文（source_text）**：
  凡三春甲木，用庚者，土为妻，金为子。用丁者，木为妻，火为子。
  总之正二月甲木，有庚戊者上命。如有丁透，大富大贵之命也。

- **分字分词释义**：
  - **用庚者**：以庚金为用神 / 杀制刃 / 主武职或异途
  - **土为妻金为子**：财为妻、官杀为子 / 用神为子的六亲取法 / 财滋杀
  - **用丁者**：以丁火为用神 / 食伤泄秀 / 主文贵
  - **木为妻火为子**：比劫为妻、食伤为子 / 另一种六亲取法 / 木火通明
  - **庚戊者**：有庚金和戊土 / 杀与财齐备 / 财滋弱杀配置
  - **上命**：上等命格 / 富贵可期 / 较高格局
  - **丁透**：丁火透出天干 / 泄秀或驾杀 / 木火通明之象

- **规范化释义（primary_lang_explained）**：
  凡是春天的甲木，如果用神是庚金（杀），那么以土（财）为妻，金（杀）为子（财生官杀）。如果用神是丁火（伤），那么以木（比劫）为妻，火（伤）为子（木生火）。
  总之，正月二月的甲木，八字里有庚金和戊土的是上等命（财滋弱杀）。如果更有丁火透出（木火通明或配合制杀），那是大富大贵的命。

- **完整对等诠释（secondary_lang_full）**：
  Generally for Jia Wood in Spring: If Geng Metal is the Useful God, then Earth is the Wife and Metal is the Child. If Ding Fire is the Useful God, then Wood is the Wife and Fire is the Child.
  In summary, for Jia Wood in the 1st and 2nd Months, having Geng and Wu makes for a superior life. If Ding is also revealed, it is a life of great wealth and nobility.

- **核心要点**：
  - **六亲取法**：以用神为子，生用神者为妻。
    - 用庚（官杀）：土妻金子。
    - 用丁（食伤）：木妻火子。
  - **正二月总决**：
    - 庚戊齐备：上命（财滋弱杀）。
    - 丁透：配合得宜（木火通明或伤官驾杀），大富贵。

- **详细解说**：
  这里提出了子平命理中"用神为子"的六亲理论，而非通用的"财为妻官杀为子"。
  - 正二月木旺，首选庚金（斫轮），配戊土（财）生杀，为贵。
  - 若无庚，用丁（泄秀），为富/文贵。
  - 庚戊丁三者配合（如庚丁甲戊），往往能成大器（劈甲引丁，火炼真金）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_095]` `[trigger: 春甲六亲]` `[factor_trigger: season_spring AND tiangan_jia AND (tiangan_geng OR tiangan_ding)]` `[role: 主干]` 用庚者，土为妻，金为子；用丁者，木为妻，火为子。 → 《穷通宝鉴·三春甲木》#3.5
  - `[ns_qttbj_096]` `[trigger: 春甲上命]` `[factor_trigger: (month_yin OR month_mao) AND tiangan_jia AND tiangan_geng AND tiangan_wu]` `[role: 主干依赖]` 正二月甲木，有庚戊者上命。 → 《穷通宝鉴·三春甲木》#3.5
  - `[ns_qttbj_097]` `[trigger: 春甲大贵]` `[factor_trigger: (month_yin OR month_mao) AND tiangan_jia AND tiangan_geng AND tiangan_wu AND tiangan_ding]` `[role: 总结]` 如有丁透，大富大贵之命也。 → 《穷通宝鉴·三春甲木》#3.5"""
    normalized_text_zh: str = """"""
    subject: str = "5. 正二月甲木总结"
    factor_refs: list = ['useful_god_as_child', 'wealth_nourishing_weak_killing']
    
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
        l1_anchor="qtbj_v1.0.0_5__正二月甲木总结_001_L1",
    )
    version: str = "1.0.0"
