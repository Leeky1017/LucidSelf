"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.458376
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
    semantic_id="smth_v1.0.0_弃命从煞格的条件与风险_001",
    book_id="sanming",
    engine_id="bazi"
)
class 弃命从煞格的条件与风险(SemanticEntry):
    """
    - **原文（source_text）**：
  《独步》云：弃命从煞，须要会煞从财，忌煞从煞。盖言从煞格，以煞神太重，身无所归，不得已从之；要行煞旺及财乡，四柱无一点比肩、印绶方论。如遇运扶身旺，与...
    """
    
    original_text: str = """- **原文（source_text）**：
  《独步》云：弃命从煞，须要会煞从财，忌煞从煞。盖言从煞格，以煞神太重，身无所归，不得已从之；要行煞旺及财乡，四柱无一点比肩、印绶方论。如遇运扶身旺，与煞为敌，从煞不专，故为祸患。经云：弃命从煞，论刚柔：言弃天干从地支，随五行性情。阴干从地支，煞纯者多贵，以阴柔能从物也；阳干从地支，煞纯者亦贵，但次于阴，以阳不受制也。水、火、金、土皆从，惟阳木不能从，死木受斧斤，反遭其伤故也。《元理赋》云：平生为富且贵，皆因煞重身柔。鬼多无鬼，反不为凶。古歌曰：五阳坐日全逢煞，弃命相从寿不坚；如是五阴逢此地，身衰煞旺吉堪言。

- **完整对等诠释（secondary_lang_full）**：
  The classic Du Bu says of the 'abandoning life to follow Killing' pattern that it must 'meet Killing and follow wealth, and must not be Killing merely following more Killing'. This describes a chart where Killing is overwhelmingly strong and the day-master has nowhere to stand—no peers or Seals to rely on—so it has no choice but to go along with the Killing qi. For such a true follow-Killing structure, the chart must travel through fortunes where Killing and wealth are both prosperous, and the four pillars must be free from any trace of parallel or Seal; otherwise the day-master and Killing become enemies and the following is no longer pure, turning the configuration into a source of disaster.
  Another passage, 'Abandoning life to follow Killing discusses hardness and softness', explains that this means abandoning the standpoint of the day stem and following the nature of the branches and their five-element qi instead. Yin stems, being softer, more easily follow the branch and, when the Killing is pure, often become noble through following. Yang stems can also follow but usually with slightly less ease, since yang nature does not submit readily, and yang wood in particular is said not to be suited for this pattern: like a great tree that cannot bend, it is more likely to be cut down by the axe than to follow the force that fells it.


- 分字分词释义：
  - **弃命从煞**：指日主极衰、七煞极旺，日主之"命"无所依归，只能随煞之气而行的格局。
  - **会煞从财，忌煞从煞**：从煞格以煞配财为佳，财可引煞生用；若只是煞多再会煞（煞从煞），则煞气过重，多为横祸。
  - **身无所归，不得已从之**：日主根气全失，无比劫印绶可依，只能顺从强势之煞，这是一种"被迫从煞"。
  - **弃天干从地支**：舍弃日干本身的生克立场，而随地支五行之性情与所从之煞。
  - **阴干从地支，煞纯者多贵**：阴日干柔顺易从，煞星纯粹时较易成贵；阳干虽亦可从，但不及阴干之易从物。
  - **阳木不能从**：阳木比喻大木，性不易屈折，从煞则如死木受斧斤，多遭其伤，不宜强论弃命从煞。
  - **鬼多无鬼**："鬼"即七煞，煞多而能从，反不以鬼论凶，乃以权论。

- **规范化释义（primary_lang_explained）**：
  弃命从煞，是一种日主极弱而七煞极强的从格。所谓"弃命"，是指日主本身几乎没有根气，无比肩、印绶可依，若以"扶身"为思路反而会被煞击破；此时若煞旺又得财星配合，反宜顺其煞势，任其为用，即所谓"从煞"。但从煞有严苛条件：四柱忌见比肩、印绶来争气，也忌再见杂煞破局；运势则宜行煞旺与财旺之乡，若行运反而扶身、与煞对抗，则"从煞不专"，容易招致祸患。
  
  文中强调刚柔之分：阴干柔顺，若地支煞纯，又无比印牵扯，较易成从煞之贵；阳干性刚，不易从物，即便煞纯亦贵而略逊阴干，尤其阳木难以从煞。故古歌云：五阳日坐七煞全逢，多主弃命从煞者寿不坚；五阴日若身衰煞旺，则从煞反多吉应，可为富贵之命。

- 核心要点：
  - 弃命从煞格必须**身极弱、煞极旺、无比印**，且多配财星，引煞为用。
  - 此格忌行"扶身"之运，一旦身旺与煞对抗，反破从局，多主祸患。
  - 阴干较易从煞而贵，阳干次之，阳木尤忌强论从煞。

- 详细解说：
  在普通七煞格中，论法是"身强可任煞，身弱要制煞"；而在弃命从煞中，局面已经超出"制煞"的范围：日主根气几乎全失，若再图以印比相扶，只会使身与煞对敌，反而激化冲突。此时真正的逻辑是"舍身从煞"——承认自己在局中并非主导，而是顺着煞与财的流向发展。
  
  "会煞从财"四字极为关键：财可以牵引煞气，使煞不直接攻身，而是转化为实际事务与权力结构中的压力、任务和职责；若只有煞而无财，则煞多成灾。又由于此格以"从"为贵，故四柱不可再见比肩、印绶来争夺日元之气；一旦有比印，便不再是纯从之局，反而成"身弱煞强"的大凶格。
  
  阴干从煞较阳干更易成格，是因为阴干本性柔顺，能随大势而转；阳干则多有不屈之性，不易全然放弃自我定位，故即便表面条件类似，实际应象有别。阳木更因其象为大木，既难受制又难屈从，强论从煞反而多伤。

- 校勘与字词辨析：
  - "鬼多无鬼"一句，古人以"鬼"指七煞，意在说明煞多而能从者，反不以凶鬼视之，而当作权星。
  - "弃天干从地支"是从格论中的常见说法，强调的是气势之所归，而非字面上真的不要日干。
  - **English**：
    - Refers to where nobility belongs; not literally discarding day stem.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_05_072]` `[trigger: 弃命从煞]` `[factor_trigger: qiming_congsha_presence]` `[role: 主干]` 弃命从煞，须要会煞从财，忌煞从煞。 → 《三命通会》卷五#弃命从煞
  - `[ns_smth_05_073]` `[trigger: 身无所归]` `[factor_trigger: shen_wu_suo_gui AND bu_de_yi_cong]` `[role: 主干依赖]` 煞神太重，身无所归，不得已从之。 → 《三命通会》卷五#弃命从煞
  - `[ns_smth_05_074]` `[trigger: 阴干易从]` `[factor_trigger: yinyang_gangrou_diff AND sha_chun_duo_gui]` `[role: 条件分支]` 阴干从地支，煞纯者多贵，以阴柔能从物也。 → 《三命通会》卷五#弃命从煞
  - `[ns_smth_05_075]` `[trigger: 鬼多无鬼]` `[factor_trigger: gui_duo_wu_gui]` `[role: 总结]` 鬼多无鬼，反不为凶。 → 《三命通会》卷五#弃命从煞"""
    normalized_text_zh: str = """"""
    subject: str = "弃命从煞格的条件与风险"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'qiming_congsha_presence', 'bazi_semantic', 'congshi_config', 'bazi_semantic', 'sheshen_congshi_score', 'bazi_semantic', 'yinyang_gangrou_diff', 'bazi_semantic', 'chuncong_condition', 'bazi_semantic', 'fushen_poju_risk', 'bazi_semantic', 'source_ref', 'rel_smth_05_055', 'qiming_congsha_presence', 'rel_smth_05_056', 'yinyang_gangrou_diff', 'rel_smth_05_057', 'fushen_poju_risk', 'evi_smth_05_055', 'congshi_config', 'rule_congcai', 'evi_smth_05_056', 'yinyang_gangrou_diff', 'rule_yinyi', 'evi_smth_05_057', 'fushen_poju_risk', 'rule_fushen', 'map_smth_05_037', 'map_smth_05_038']
    
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
        l1_anchor="smth_v1.0.0_弃命从煞格的条件与风险_001_L1",
    )
    version: str = "1.0.0"
