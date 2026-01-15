"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412309
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
    semantic_id="smth_v1.0.0_辛癸未日合亥冲巳之官格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 辛癸未日合亥冲巳之官格(SemanticEntry):
    """
    - **原文（source_text）**：

  此格乃辛未、癸未二日，以二三未字合起亥字，冲出巳中丙戊为辛癸之官，柱有酉丑一字合住贵气为妙，怕填实冲刑。如甲戌、辛未、癸未、癸丑，庚申、癸未、辛未、...
    """
    
    original_text: str = """- **原文（source_text）**：

  此格乃辛未、癸未二日，以二三未字合起亥字，冲出巳中丙戊为辛癸之官，柱有酉丑一字合住贵气为妙，怕填实冲刑。如甲戌、辛未、癸未、癸丑，庚申、癸未、辛未、乙未，二命合格，俱贵。诗曰：羊击猪蛇格最强，日逢辛癸未相当，柱中再逢酉申字，合禄无伤入庙堂。以上诸格，须柱中无财官方用，有则不取。

- 分字分词释义：

  - **辛未、癸未二日**：仅限辛日、癸日且日支为未（土），构成本格的日主条件。
  - **二三未字合起亥字**：命局中有两三个未土，相互引动，与亥水发生合拱关系，形成“羊（未）击猪（亥）”之象。
  - **冲出巳中丙戊为辛癸之官**：亥与巳相冲，巳中丙火、戊土为辛、癸之官星，被冲动而外显。
  - **柱有酉丑一字合住贵气**：酉、丑可与巳成巳酉丑合局，或与未、亥构成交互制约，使被冲出的官禄不致散失。
  - **怕填实冲刑**：若巳、亥、未等位被填实、刑冲过重，则官禄之气混杂或受伤，格局难成。
  - **以上诸格，须柱中无财官方用，有则不取**：指本节及前一节虎午奔巳等“特殊官禄格”，皆以命局无明财官为前提，若原局已有明财官，则不再另以此格论。

- **规范化释义（primary_lang_explained）**：

  羊击猪蛇格，是辛未日、癸未日的一种“合起亥、冲出巳官”的官禄格。“羊”指未，“猪”指亥，“蛇”指巳。命局中若有两三个未土，相互引动并合起亥水，则亥与巳相冲，巳中所藏丙火、戊土随之被冲出：对辛日来说丙火为官，对癸日来说戊土为官，因此形成辛癸二日的官格。
  
  若柱中再见酉或丑一支，与巳成合局，或与未、亥形成相生相制的结构，则被冲出的官禄之气不致散失，反而更显清贵。古人以“羊击猪蛇格最强，日逢辛癸未相当，柱中再逢酉申字，合禄无伤入庙堂”来赞其贵重，但即便如此，仍需以“柱中无明财官”作为前提——若原局已有财官可用，则不再额外以羊击猪蛇论格，以免格局混乱。

- 核心要点：

  - 仅限辛未、癸未二日，属特定日主专用格。
  - 结构核心是“多未合亥，亥冲巳出丙戊为官”，再辅以酉、丑等支摄官护禄。
  - 命局须无明财官，且日主身旺，方能承载冲出之官禄。
  - 填实、重刑、杂合等情况会削弱乃至破坏此格，只能降格或另以常规官煞格论。

- 详细解说：

  与虎午奔巳格一样，羊击猪蛇也是围绕巳中丙戊而做文章。不同之处在于：虎午奔巳依赖“寅刑丑、丑合巳”的刑合结构，而羊击猪蛇则依赖“多未合亥、亥冲巳”的冲合结构。未为“羊”、亥为“猪”、巳为“蛇”，多未合亥，使亥中水气与未土相联；再由亥冲巳，将巳中官禄之气击出。
  
  在实践中，需要特别留意以下几点：
  1. 未字的数量：一两个未不足以形成明显结构，二三未则格局鲜明，但过多则易成土重埋金、水弱火绝；
  2. 官星的清纯：巳中丙戊被冲出之后，若同时再见庚辛金、丙丁火等过多，则易使官煞交杂、火金相战；
  3. 合局护禄：酉、丑等支若能与巳构成合局，有助于稳定官禄之气，避免“羊击”过度而致禄不存；
  4. 原局明财官：若八字本来财官清正，则不宜再强扯入羊击猪蛇之格，以免喧宾夺主。

- **校勘与字词辨析（双语）**：

  - 原文“以二三未字合起亥字，冲出巳中丙戊为辛癸之官”一句，为本格结构总纲，本稿据底本保留，仅以现代标点分句，并在释义中拆解其逻辑。
  - “羊击猪蛇格最强，日逢辛癸未相当，柱中再逢酉申字，合禄无伤入庙堂”一句，将“羊、猪、蛇”的生肖象与未、亥、巳三支相配，本稿仅在释义中点明，不改用字。
  - “以上诸格，须柱中无财官方用，有则不取”一句，按上下文理解为兼指虎午奔巳与羊击猪蛇等特殊官格，本稿在白话部分作了合并说明。
  - **English**：
    - The sentence "using two or three Wei to combine Hai, clashing out Bing-Wu in Si as official for Xin-Gui" is the structural principle; this edition preserves it with modern punctuation.
    - The verse "Sheep Strikes Pig-Snake pattern is strongest, day meeting Xin-Gui with Wei is fitting, if the chart also has You-Shen, combined salary unharmed enters the temple" links zodiac imagery to the three branches; this edition explains the imagery source.
    - The sentence "above patterns require no wealth-official in chart; if present, do not use" applies to both Tiger-Horse and Sheep-Strikes patterns; this edition provides a consolidated explanation.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_033]` `[trigger: 羊击猪蛇定义]` `[factor_trigger: yangji_zhushe_presence]` `[role: 主干]` 辛未、癸未二日，以二三未字合起亥字，冲出巳中丙戊为辛癸之官。 → 《三命通会》卷六#羊击猪蛇
  - `[ns_smth_06_034]` `[trigger: 酉丑合贵]` `[factor_trigger: you_chou_he_gui AND pa_tianshi]` `[role: 主干依赖]` 柱有酉丑一字合住贵气为妙，怕填实冲刑。 → 《三命通会》卷六#羊击猪蛇
  - `[ns_smth_06_035]` `[trigger: 无财官方用]` `[factor_trigger: wu_cai_guan_fang_yong]` `[role: 条件分支]` 以上诸格，须柱中无财官方用，有则不取。 → 《三命通会》卷六#羊击猪蛇
  - `[ns_smth_06_036]` `[trigger: 入庙堂]` `[factor_trigger: he_lu_wu_shang]` `[role: 总结]` 羊击猪蛇格最强，日逢辛癸未相当，柱中再逢酉申字，合禄无伤入庙堂。 → 《三命通会》卷六#羊击猪蛇

- **完整对等诠释（secondary_lang_full）**：
  The "Sheep Strikes Pig-and-Snake" pattern is a clash-and-combination configuration exclusive to Xin-Wei and Gui-Wei days. In this structure "Sheep" refers to Wei (the Goat branch), "Pig" refers to Hai, and "Snake" refers to Si. When the chart contains two or three Wei branches, their collective earth energy can draw Hai water into a combining relationship; Hai then clashes Si on the opposite side of the zodiac, and the officials stored inside Si—Bing fire for Xin and Wu earth for Gui—are knocked out and made available for use.
  
  The mechanism differs from "Tiger-Horse Rushing to Si", which relies on Yin punishing Chou and Chou combining with Si. Here the driving force is the mass of Wei branches that first ropes in Hai and then lets Hai do the clashing. To stabilise the released qi, the chart ideally includes a You or Chou branch that forms a metal trine with Si and prevents the official power from scattering after the clash. The chart must lack obvious wealth and officials on the stems; when all conditions align and the day-master is strong, this pattern points to noble rank."""
    normalized_text_zh: str = """"""
    subject: str = "辛癸未日合亥冲巳之官格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_12', 'bazi_semantic', 'bazi_structure_wei_hai_si_config', 'bazi_semantic', 'bazi_state_strength_3', 'bazi_semantic', 'bazi_state_you_chou_degree', 'bazi_semantic', 'bazi_condition_factor_140', 'bazi_semantic', 'bazi_condition_day_master_condition_1', 'bazi_semantic', 'source_ref', 'rel_smth_06_025', 'yangji_zhushe_presence', 'rel_smth_06_026', 'chonghe_qiguan_score', 'rel_smth_06_027', 'mingcaiguan_ganrao_risk', 'evi_smth_06_025', 'duowei_hehai_config', 'rule_yangji', 'evi_smth_06_026', 'youchou_heju_hulu', 'rule_youchou', 'evi_smth_06_027', 'mingcaiguan_ganrao_risk', 'rule_wuming', 'map_smth_06_017', 'map_smth_06_018']
    
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
        l1_anchor="smth_v1.0.0_辛癸未日合亥冲巳之官格_001_L1",
    )
    version: str = "1.0.0"
