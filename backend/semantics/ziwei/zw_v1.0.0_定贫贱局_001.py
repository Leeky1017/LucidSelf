"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778612
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
    semantic_id="zw_v1.0.0_定贫贱局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 定贫贱局(SemanticEntry):
    """
    - 分字分词释义：

  - **定贫贱局**：判断贫贱格局的标准与方法。
  - **生不逢时**：出生时机不佳，命坐空亡位。
  - **命坐空亡**：命宫落在空亡位置。
  - **禄逢两杀**...
    """
    
    original_text: str = """- 分字分词释义：

  - **定贫贱局**：判断贫贱格局的标准与方法。
  - **生不逢时**：出生时机不佳，命坐空亡位。
  - **命坐空亡**：命宫落在空亡位置。
  - **禄逢两杀**：禄存同时遭遇两颗凶杀星。
  - **禄坐空亡**：禄存落入空亡位置，禄气虚耗。
  - **空劫杀星**：地劫天空与凶杀星同宫。
  - **马落空亡**：天马落入空亡位置，行动落空。
  - **禄冲会无用**：有禄来冲会也无法发挥作用。
  - **主奔波**：主一生奔波劳碌，无所成就。
  - **梁马飘荡**：天梁天马同宫主漂泊流浪。
  - **贪狼陷地**：贪狼落入陷弱之地。
  - **日月反背**：太阳太阴各在不利位置，背向而行。

#### 13.1 生不逢时

- 原文（断句）：生不逢时，命坐空亡，逢廉贞是也。

- 规范化释义（primary_lang_explained）：

  生不逢时命坐空亡逢廉贞是也。

- 核心要点：命空亡逢廉贞

#### 13.2 禄逢两杀

- 原文（断句）：禄逢两杀，禄坐空亡，又逢空劫杀星是也。

- 规范化释义（primary_lang_explained）：

  禄逢两杀禄坐空亡又逢空劫杀星是也。

- 核心要点：禄存空亡加空劫

#### 13.3 马落空亡

- 原文（断句）：马落空亡，马既落亡，虽禄冲会，无用；主奔波。

- 规范化释义（primary_lang_explained）：

  马落空亡马既落亡虽禄冲会无用主奔波。

- 核心要点：天马空亡，奔波无功

#### 13.4 日月藏辉

- 原文（断句）：日月藏辉，日月反背，又逢巨暗是也。

- 规范化释义（primary_lang_explained）：

  日月藏辉日月反背又逢巨暗是也。

- 核心要点：日月反背加巨门暗曜

#### 13.5 财与囚仇

- 原文（断句）：财与囚仇，武贞同守身命是也。

- 规范化释义（primary_lang_explained）：

  财与囚仇武贞同守身命是也。

- 核心要点：武曲廉贞同守身命

#### 13.6 一生孤贫

- 原文（断句）：一生孤贫，谓破守命，居陷地是也。

- 规范化释义（primary_lang_explained）：

  一生孤贫谓破守命居陷地是也。

- 核心要点：破军守命陷地

- 完整对等诠释（secondary_lang_full）：

  The poverty‑and‑baseness configuration standards, by contrast, gather eight patterns in which voids, malefics and debilitation combine to undermine salary, resources and social standing. They explain why some lives remain lonely and impoverished in spite of occasional minor blessings, and why certain mixtures of stars are considered fundamentally hard to redeem.
  Birth‑Untimely refers to charts where the Life palace falls into void and at the same time meets harsh stars such as Lianzhen, so that effort seldom matches timing. Salary‑Encountering‑Dual‑Malefics appears when Lucun or other salary stars sit in void and are then hit again by calamity stars such as Tianko and Dijie, damaging both income and stability. Horse‑Falling‑Void describes Tianma in void or trapped, so that movement and striving never settle into lasting gain. Sun‑Moon Concealing‑Radiance shows the luminaries turned away or darkened, often with Jumen, hiding their light and depriving the native of recognition. Wealth‑Prison‑Feud arises when Wuqu and Lianzhen co‑guard Life or Body, tying money matters to restraint, confinement or constant conflict. Lifetime‑Solitary‑Poverty is illustrated by Pojun guarding Life in a fallen position, making it difficult to build or keep stable resources. Gentleman‑In‑Wilderness depicts charts where benefic stars are forced into fallen places while malefics surround the Life and Body palaces, leaving the person with talent but no platform. Dual‑Canopy refers to dual‑salary patterns that are immediately undercut by void and calamity stars, turning what could have been high honor into isolation or wasted potential.
  Together these eight patterns emphasize that extreme poverty and lowliness rarely come from a single factor. They require the stacking of voids, debilitation and heavy malefics especially on the Life, Body, wealth and movement houses. When such triple afflictions are present and not relieved by strong benefics, the chart tends toward a life marked by hard labor, meagre returns, broken support networks and a sense of being cut off from mainstream society.

- 叙事素材（narrative_snippets）：

  - **生不逢时**：命坐空亡又逢廉贞，往往努力与时机总是错身而过，事倍功半。
  - **禄逢两杀**：禄存空亡再遇空劫、杀曜，像薪水打到账上又马上被扣走，难以积累。
  - **马落空亡**：天马落空，跑得越多越累，回头发现“山河走遍，囊中依旧空空”。
  - **日月藏辉**：日月反背加巨门暗曜，才华与良心都被压在阴影里，难得舞台。
  - **财与囚仇**：武曲廉贞同守身命，钱途总伴随限制、官非或心累，容易“有钱难安”。
  - **一生孤贫/君子在野/两重华盖**：或终身孤贫，或有才无位、长年在野，或双禄遇空劫，高位难登反成高处不胜寒。"""
    normalized_text_zh: str = """"""
    subject: str = "定贫贱局"
    factor_refs: list = ['combo_shengbufengshi', 'combo_lufengliangsha', 'combo_maluokongwang', 'combo_riyuecanghui', 'combo_caiyuqiuchou', 'combo_liangchonghuagai', 'source_ref', 'rel_pinju_001', 'kongwang_pohao', 'rel_pinju_002', 'xiongxing_juji', 'rel_pinju_003', 'xiandi_shihui', 'evi_pinju_001', 'combo_shengbufengshi', 'rule_shengbufengshi', 'evi_pinju_002', 'combo_maluokongwang', 'rule_maluokongwang', 'concept_poverty_structure', 'concept_void_damage', 'concept_malefic_cluster']
    
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
        l1_anchor="zw_v1.0.0_定贫贱局_001_L1",
    )
    version: str = "1.0.0"
