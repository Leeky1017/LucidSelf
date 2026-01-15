"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264341
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
    semantic_id="smth_v1.0.0_太岁的定义与君臣结构_001",
    book_id="sanming",
    engine_id="bazi"
)
class 太岁的定义与君臣结构(SemanticEntry):
    """
    - **原文（source_text）**：  
  论太岁夫太岁者，乃一岁之主宰，诸神之领袖。其说有二：如四柱中生年，曰当生太岁；如逐年轮转，曰游行太岁。当生太岁，乃终身之主，其理已论于前。其逐年太...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论太岁夫太岁者，乃一岁之主宰，诸神之领袖。其说有二：如四柱中生年，曰当生太岁；如逐年轮转，曰游行太岁。当生太岁，乃终身之主，其理已论于前。其逐年太岁游行十二宫，定一年之祸福，为四时之吉凶。经云：太岁乃众煞之主，人命未必为凶。如逢战斗之乡，必主刑于本命。盖太岁如君也，大运如臣也。如君臣和悦，其年则吉；若值刑战，其年则凶。经又云：岁伤日干，有祸必轻；日犯岁君，灾殃必重。此又分言岁君伤日者，如庚年克甲日，为偏官，譬君治臣，父治子，虽有灾晦，不为大害。何则？上治其下顺也，其情尚未尽绝。日犯岁君，如甲日克戊年，为偏财，譬臣弑其君，子弑其父，深为不利。

- **规范化释义（primary_lang_explained）**：  
  本段先定义太岁：一为命局中的“当生太岁”（生年干支），为终身之主；二为逐年轮转的“游行太岁”，在十二宫中决定一年之祸福和四时吉凶。太岁是“众煞之主”，却不必然为凶，只有落在“战斗之乡”、与命局发生刑战时，才主刑克本命。作者以“太岁如君，大运如臣”作比：君臣和悦则该年吉，君臣相战则该年凶。进一步区分“岁伤日干”与“日犯岁君”：前者如庚年克甲日，为偏官，譬如君治臣、父治子，虽有灾晦，多属上治下顺，情分尚未断绝，故祸轻；后者如甲日克戊年，为偏财，譬如臣弑君、子弑父，是下凌上逆，凶象远重于前者。

- **完整对等诠释（secondary_lang_full）**：  
  This paragraph defines Tai Sui in two senses: as the natal year pillar, called the "birth Tai Sui," which acts as a life‑long sovereign, and as the annually rotating Tai Sui that moves through the twelve palaces, determining the fortunes and misfortunes of each year. Tai Sui is described as "lord of all baleful stars" but is not inherently evil; only when it resides in a "battlefield" position and engages in harsh clashes with the chart does it inflict severe damage. The metaphor "Tai Sui is like the ruler, major luck like the ministers" captures the relationship between annual and decade cycles: when ruler and ministers are in harmony, the year tends to be auspicious; when they are at war, the year turns dangerous. The text further distinguishes two situations: when the year stem attacks the Day Stem ("the year harms the day"), as in Geng year controlling Jia day, this is likened to a ruler disciplining a minister or a father correcting a son—there may be trouble and gloom, but the underlying relationship remains, so disaster is relatively light. When the Day Stem attacks the year stem ("the day offends the year lord"), as in Jia day controlling Wu year, this resembles a minister murdering his ruler or a son killing his father, a grave reversal of hierarchy; such configurations are considered especially inauspicious.

- **核心要点**：
  - 太岁分为“当生太岁”（生年）与“游行太岁”（逐年轮转），前者主终身，后者主一岁祸福。
  - 太岁如君、大运如臣，君臣和悦则吉，刑战则凶。
  - “岁伤日干”与“日犯岁君”吉凶轻重不同，后者为格局中更严重的逆叛之象。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_089]` `[trigger: 太岁为主宰]` `[factor_trigger: taisui_wei_zhuzai AND zhushen_lingxiu]` `[role: 主干]` 太岁者，乃一岁之主宰，诸神之领袖。 → 《三命通会》卷十#太岁的定义与君臣结构
  - `[ns_smth_10_090]` `[trigger: 太岁如君]` `[factor_trigger: taisui_rujun AND dayun_ruchen]` `[role: 主干依赖]` 太岁如君也，大运如臣也。如君臣和悦，其年则吉。 → 《三命通会》卷十#太岁的定义与君臣结构
  - `[ns_smth_10_091]` `[trigger: 岁伤日干]` `[factor_trigger: suishang_rigan AND huo_bi_qing]` `[role: 条件分支]` 岁伤日干，有祸必轻；日犯岁君，灾殃必重。 → 《三命通会》卷十#太岁的定义与君臣结构
  - `[ns_smth_10_092]` `[trigger: 太岁当头立]` `[factor_trigger: taisui_dangtou_li AND zhushen_bugan_dang]` `[role: 总结]` 太岁当头立，诸神不敢当。 → 《三命通会》卷十#太岁的定义与君臣结构

- **详细解说**：  
  这一段在工程上提供了年运与大运权重的结构比喻：太岁作为“年中天子”，给每一年盖章；大运作为“辅弼三元之臣”，决定十年基调。若只看大运而忽略太岁，就难以解释同一大运中不同年份的巨大差异。通过“岁伤日干/日犯岁君”的区分，还可以在同样的克合结构中区分“上治下”和“下逆上”两类情境：前者多表现为环境、制度对个人的压力；后者更可能表现为个人主动挑战权威或结构，因而引来更重的惩罚。

- **校勘与字词辨析（双语）**：
  - **中文**：“战斗之乡”可理解为干支刑冲并见、煞气聚集之宫位，传统多以刑冲破害重叠处为候。
  - **English**: The metaphors of ruler and minister, father and son underscore a Confucian moral hierarchy built into the astrological language; this is not incidental rhetoric but part of how severity is graded."""
    normalized_text_zh: str = """"""
    subject: str = "太岁的定义与君臣结构"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_太岁的定义与君臣结构_001_L1",
    )
    version: str = "1.0.0"
