"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.413002
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
    semantic_id="smth_v1.0.0_白虎持势与金气用事_001",
    book_id="sanming",
    engine_id="bazi"
)
class 白虎持势与金气用事(SemanticEntry):
    """
    - **原文（source_text）**：

  庚辛金属西方，谓之白虎持势者，得其势也。如庚午、庚寅、庚戌、辛巳、辛卯、辛未，此六日生，坐下财官印贵，要日主有托受生气，或官旺得时有助，不见财官，用...
    """
    
    original_text: str = """- **原文（source_text）**：

  庚辛金属西方，谓之白虎持势者，得其势也。如庚午、庚寅、庚戌、辛巳、辛卯、辛未，此六日生，坐下财官印贵，要日主有托受生气，或官旺得时有助，不见财官，用官必贵，用财必富，岁运同。有以辛卯日时犯白虎，不利勇猛战斗，令人多有眼目之疾，重犯尤忌之。诗曰：白虎持世寅卯强，如临巳午未戌乡，四野遇之多富贵，必向皇都作栋梁。

- 分字分词释义：

  - **庚辛金属西方，谓之白虎**：以庚辛金喻西方白虎之气，主刚烈、决断与肃杀之权。
  - **持势者，得其势也**：强调“得势”而非仅有形，意指金气得令、有根，有足以担当财官之权势。
  - **庚午、庚寅、庚戌、辛巳、辛卯、辛未六日**：列举白虎持势之典型日柱，日支多为火木土等财官印之地。
  - **坐下财官印贵**：日支所居之地中同时含有财星、官星或印绶，使日主一坐之下，即有财官印三者环绕。
  - **不见财官，用官必贵，用财必富**：此处“见”作“另行透出、散乱之见”，若不再多见杂乱之财官，而能专用一端，则易成贵富之象。
  - **辛卯日时犯白虎，多眼目之疾**：特别指出辛卯日时之“犯白虎”，象征刚猛之气直冲头目，易引发眼目相关疾患。

- **规范化释义（primary_lang_explained）**：

  白虎持势格，是以庚辛金日坐财官印之地、而金气得势为核心的一类格局。庚辛金本身就象征刚烈、决断、持权之性，当其日支又居于午、寅、戌、巳、卯、未等财官印旺盛之处时，便好比白虎既得其位，又得其势——既有权力之象，又有资源与支持。

  原文指出，此类日柱若日主有托、得生气，或官星得时、有助力，再不见纷乱杂透之财官，则“用官必贵，用财必富”：一则可以专用官星为权柄，二则可以专用财星为富源。反之，若以辛卯日时犯白虎，或类似结构使刚猛之气直冲头面，则容易在勇猛、争斗之际招致眼目之疾，重犯者尤应戒惧。

- 核心要点：

  - 以**庚辛金日坐财官印旺地**为基础，金气得势，为“持势”之根本。
  - 日支财官印齐备，且日主有托、有生气，方能成“贵富兼备”的白虎持势格。
  - 不宜财官杂乱、气势分散；专用一端（官或财）更易成就。
  - 忌犯白虎过甚，尤其辛卯等格局，需防头面眼目之疾与因勇猛冲动而起的祸端。

- 详细解说：

  若从结构上看，白虎持势格可分三层来理解：

  1. **金得其位**：庚辛日生于适当的月令或局中有金根，使自身不致空乏；
  2. **金得其势**：日支坐下财官印旺地，形成“权势、资源、名声”三者集中于日主脚下之象；
  3. **势有所用**：或以官为用，主权位显达；或以财为用，主富厚，非常怕的是“有势无用”或“用神混杂”。

  在实际判断中，除了观察六个典型日柱本身外，还要结合：

  - 月令是否帮扶金气或财官气；
  - 四柱有无伤官过重以破官，或比劫过多以争财；
  - 行运是否延续“金得其势”的状态，抑或转入制约金气的运程。原文以眼目之疾为例，实则提醒此格之人若过度倚仗刚猛之气、不善收敛，易在头面、名誉与身家安危上付出代价。

- **校勘与字词辨析（双语）**：

  - 原文“白虎持势者，得其势也”一句，本稿在释义与白话中明确为“金气得位兼得时”的综合象意。
  - 对“用官必贵，用财必富”之语，本稿理解为“专用官/专用财”的两种不同取法，而非同时兼用，以免与“财官混杂”之忌矛盾。
  - 关于“辛卯日时犯白虎”以及“眼目之疾”的说法，本稿在白话中仅作体征性举例，不将其机械化为必然定论。
  - **English**：
    - Not mechanically treated as inevitable conclusion.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_245]` `[trigger: 白虎持势]` `[factor_trigger: baihu_chishi AND gengxin_xifang]` `[role: 主干]` 庚辛金属西方，谓之白虎持势者，得其势也。 → 《三命通会》卷六#白虎持势
  - `[ns_smth_06_246]` `[trigger: 坐下财官印贵]` `[factor_trigger: zuoxia_caiguanyin AND riyou_tuo]` `[role: 主干依赖]` 坐下财官印贵，要日主有托受生气。 → 《三命通会》卷六#白虎持势
  - `[ns_smth_06_247]` `[trigger: 用官必贵]` `[factor_trigger: yongguan_bigui AND yongcai_bifu]` `[role: 条件分支]` 不见财官，用官必贵，用财必富。 → 《三命通会》卷六#白虎持势
  - `[ns_smth_06_248]` `[trigger: 栋梁之材]` `[factor_trigger: siyu_guida AND dongliang_zhi_cai]` `[role: 总结]` 四野遇之多富贵，必向皇都作栋梁。 → 《三命通会》卷六#白虎持势"""
    normalized_text_zh: str = """"""
    subject: str = "白虎持势与金气用事"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_86', 'bazi_semantic', 'bazi_condition_metal_deling', 'bazi_semantic', 'bazi_state_metal_water_3', 'bazi_semantic', 'source_ref', 'rel_smth_06_211', 'baihuchishi_presence', 'rel_smth_06_212', 'chishi_youli', 'rel_smth_06_213', 'jinhan_shuileng', 'evi_smth_06_211', 'baihuchishi_presence', 'rule_baihu', 'evi_smth_06_212', 'jinqi_deling', 'rule_qiuling', 'evi_smth_06_213', 'jinhan_shuileng', 'rule_jinhan', 'map_smth_06_141', 'map_smth_06_142']
    
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
        l1_anchor="smth_v1.0.0_白虎持势与金气用事_001_L1",
    )
    version: str = "1.0.0"
