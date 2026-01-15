"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228684
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
    semantic_id="smth_v1.0.0_丙辰丁巳沙中土_自库自绝之土正印建福_001",
    book_id="sanming",
    engine_id="bazi"
)
class 丙辰丁巳沙中土自库自绝之土正印建福(SemanticEntry):
    """
    - **原文（source_text）**：
  丙辰自库之土，厚且壮，喜甲辰火，恶戊辰木，此土凡木不能伤。盖丙火也。辰为火偏库，土已成器，惟嫌戊戌、己亥、辛卯、戊辰之木。五行要论云：丙辰土为正印，建...
    """
    
    original_text: str = """- **原文（source_text）**：
  丙辰自库之土，厚且壮，喜甲辰火，恶戊辰木，此土凡木不能伤。盖丙火也。辰为火偏库，土已成器，惟嫌戊戌、己亥、辛卯、戊辰之木。五行要论云：丙辰土为正印，建五福吉会之德，禀之者，类皆亨大有为，不贵即富，惟犯冲者，多为僧道。丁巳自绝之土，又不为绝。盖一土居二火之下，在父母之乡，乘天属之恩，故不为绝。木不能克，火，多益佳。玉霄宝鉴云：丁巳含东南火德旺数，得之者，含容福寿。

- **分字分词释义**：
  - **自库之土**：入库的土。
  - **厚且壮**：深厚而强壮。
  - **火偏库**：火的偏库。
  - **土已成器**：土已经成器。
  - **正印**：十神之正印。
  - **建五福吉会**：建立五福吉祥聚会。
  - **亨大有为**：亨通大有作为。
  - **犯冲**：冲犯。
  - **自绝之土**：自己绝灭的土。
  - **父母之乡**：父母的位置。
  - **天属之恩**：天然隶属的恩德。
  - **东南火德旺数**：东南方火德旺盛的数理。
  - **含容福寿**：包容福气寿命。

- **规范化释义（primary_lang_explained）**：
  丙辰是入库的土，深厚而强壮，喜欢甲辰火，讨厌戊辰木，这种土一般木不能伤害。因为有丙火。辰为火的偏库，土已经成器，只忌讳戊戌、己亥、辛卯、戊辰的木。五行要论说：丙辰土为正印，建立五福吉祥聚会的德性，禀受它的人，大多亨通大有作为，不是贵就是富，只有犯冲的人，多成为僧道。丁巳是自绝的土，又不算绝。因为一个土居于两个火之下，在父母的位置，承受天然隶属的恩德，所以不算绝。木不能克制，火越多越好。玉霄宝鉴说：丁巳包含东南方火德旺盛的数理，得到它的人，包容福气寿命。

- **完整对等诠释（secondary_lang_full）**：
  Bingchen is self-storage earth, thick and robust, favors Jiachen Fire, dislikes Wuchen Wood. This earth ordinary wood cannot harm, since has Bing Fire. Chen is fire's partial-repository, earth already formed-vessel, only fears Wuxu, Jihai, Xinmao, Wuchen Wood. Five Elements Essential Discourse says: Bingchen Earth as proper-seal, establishes five-blessings auspicious-gathering virtue. Those receiving it, mostly prosperous greatly-accomplished, not noble then wealthy. Only those violating-clash, many become monks-priests. Dingsi is self-extinct earth, yet not extinct, since one earth resides beneath two fires, at parents' location, receiving natural-affiliation grace, thus not extinct. Wood cannot overcome, Fire abundant increasingly-excellent. Jade-Sky Treasure-Mirror says: Dingsi contains southeast fire-virtue prosperous-number. Those obtaining it, embrace blessings-longevity.

- **核心要点**：
  - 丙辰为沙中土，自库之土
  - 厚且壮、喜甲辰火、恶戊辰木
  - 辰为火偏库土已成器
  - 丙辰为正印、建五福吉会
  - 亨大有为不贵即富、犯冲为僧道
  - 丁巳自绝之土又不为绝
  - 一土二火在父母乡、木不克火多益佳
  - 含东南火德旺数、含容福寿

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_243]` `[trigger: 丙辰丁巳土性质]` `[factor_trigger: bingchen_self_storage_earth AND proper_seal AND five_blessings_auspicious_greatly_accomplished]` `[role: 主干]` 丙辰自库之土，厚且壮，喜甲辰火，恶戊辰木，此土凡木不能伤。盖丙火也。辰为火偏库，土已成器，惟嫌戊戌、己亥、辛卯、戊辰之木。五行要论云：丙辰土为正印，建五福吉会之德，禀之者，类皆亨大有为，不贵即富，惟犯冲者，多为僧道。丁巳自绝之土，又不为绝。盖一土居二火之下，在父母之乡，乘天属之恩，故不为绝。木不能克，火，多益佳。玉霄宝鉴云：丁巳含东南火德旺数，得之者，含容福寿。 → 《三命通会》卷一#丙辰丁巳土性质

- **详细解说**：
  此条详论丙辰、丁巳（沙中土）的性质与格局。丙辰自库土厚且壮，喜甲辰火（覆灯火）、恶戊辰木（大林木），因有丙火护持凡木不伤，辰为火偏库土已成器。五行要论强调丙辰为正印（十神），建五福吉会，亨大有为不贵即富，犯冲为僧道。丁巳自绝土又不为绝（一土二火在父母乡），木不克火多益佳，含东南火德旺数、含容福寿。这是论述库土绝土的成器与福德特质。

- **校勘与字词辨析（双语）**：
  - **中文**："自库"指辰为土库。"偏库"指辰为火偏库非正库。"正印"为十神，主智慧文化。"五福"指长寿、富贵、康宁、好德、善终。"父母之乡"指火生土，巳中丙火、丁火都是土的父母。
  - **English**: "Self-storage" means Chen is earth's repository. "Partial-repository" means Chen is fire's non-primary repository. "Proper-seal" is one of Ten Gods, governing wisdom and culture. "Five-blessings" means longevity, wealth-nobility, health-peace, virtue-love, good-ending. "Parents' location" means fire generates earth, Bing and Ding fires in Si are earth's parents."""
    normalized_text_zh: str = """"""
    subject: str = "丙辰丁巳沙中土：自库自绝之土正印建福"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_丙辰丁巳沙中土_自库自绝之土正印建福_001_L1",
    )
    version: str = "1.0.0"
