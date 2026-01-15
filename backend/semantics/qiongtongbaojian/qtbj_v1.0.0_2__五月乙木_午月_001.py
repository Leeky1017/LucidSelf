"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620066
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
    semantic_id="qtbj_v1.0.0_2__五月乙木_午月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2五月乙木午月(SemanticEntry):
    """
    - **原文（source_text）**：
  五月乙木，丁火司权，禾稼俱旱。上半月属阳，仍用癸水。下半月属阴，三伏生寒，丙癸齐用。
  柱多金水，丙火为先，余皆用癸水为先。
  乙木重逢火位，名为...
    """
    
    original_text: str = """- **原文（source_text）**：
  五月乙木，丁火司权，禾稼俱旱。上半月属阳，仍用癸水。下半月属阴，三伏生寒，丙癸齐用。
  柱多金水，丙火为先，余皆用癸水为先。
  乙木重逢火位，名为气散之文，支成火局，泄乙精神，须用癸滋。癸透有根，富贵双全。
  或庚辛年上，癸透时干，定许科甲，无癸者常人。
  若见丙透，支成火局，阳焦木性，此人残疾，无癸必夭，见壬可解。或火土太多，其人愚贱，或为僧道门下闲人。

- **分字分词释义**：
  - **丁火司权**：丁火当权主事 / 午月特征 / 火旺
  - **禾稼俱旱**：庄稼都干旱 / 需水 / 调候急
  - **三伏生寒**：三伏天生出寒气 / 夏至后 / 一阴生
  - **气散之文**：气息散尽的文章 / 火泄木 / 华而不实
  - **泄乙精神**：泄掉乙木精神 / 火局 / 虚脱
  - **阳焦木性**：阳火焦灼木性 / 火局丙透 / 残疾
  - **愚贱**：愚蠢下贱 / 火土多 / 极凶

- **规范化释义（primary_lang_explained）**：
  五月（午月）的乙木，丁火掌权，庄稼都干旱。上半月阳气盛，仍然用癸水（润）。下半月阴气生（夏至后一阴生），三伏生寒，丙火和癸水一齐使用（丙防寒，癸润燥）。
  如果柱中金水多（金水寒），以丙火为先。其余情况（火土燥），都以癸水为先。
  乙木重重遇到火位（午月火旺），这叫“气散之文”（文章华而不实），地支合成火局，泄尽乙木精神，必须用癸水滋润。癸水透出且有根，富贵双全。
  如果庚辛金在年上，癸水透出在时干（化杀生身），定许科甲功名，没有癸水就是常人。
  如果见到丙火透出，地支合成火局，阳火焦灼木性，此人残疾，没有癸水必定夭折，见到壬水可以解救。如果火土太多，这人愚蠢下贱，或者是僧道门下的闲人。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 5th Month (Horse Month): Ding Fire holds authority; crops are suffering from drought. In the first half (Yang), use Gui Water. In the second half (Yin), Three Fu Days generate cold; use both Bing and Gui.
  If pillars have much Metal/Water, prioritize Bing. Otherwise, prioritize Gui.
  Yi Wood repeatedly meeting Fire positions is called "Essays of Dispersed Qi" (flashy but empty). If branches form a Fire frame, leaking Yi's spirit, Gui must be used to nourish. If Gui is revealed and rooted, wealth and nobility are complete.
  If Geng/Xin is on the Year, and Gui is revealed on the Hour (Transforming Killing), Civil Service is promised; without Gui, ordinary.
  If Bing is revealed and branches form a Fire frame, Yang scorches the Wood nature; this person is disabled. Without Gui, they will surely die prematurely; Ren can resolve this. If Fire/Earth are excessive, the person is stupid and lowly, or an idler under monks/Taoists.

- **核心要点**：
  - **气散之文**：火太旺泄气过甚，华而不实。
  - **调候**：癸水绝对优先。无水则残疾/夭折/愚贱。
  - **夏至后**：一阴生，稍可用丙（若金水多）。
  午月乙木长生，但那是“火长生”，实则木死。
  - 所谓“乙木重逢火位”，即午月又见丙丁或火局，木气泄尽。
  - 必须有癸水（印）来生身制火。
  - "愚贱"：火土燥烈，木无生机，神智不清（木主智/肝/条达）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_188]` `[trigger: 午月乙木]` `[factor_trigger: month_wu AND tiangan_yi AND tiangan_gui]` `[role: 主干]` 五月乙木，丁火司权，禾稼俱旱，上半月属阳，仍用癸水。 → 《穷通宝鉴·三夏乙木》#8.2
  - `[ns_qttbj_189]` `[trigger: 气散之文]` `[factor_trigger: month_wu AND tiangan_yi AND dizhi_fire_frame AND dispersed_qi_essay]` `[role: 主干依赖]` 乙木重逢火位，名为气散之文，支成火局，泄乙精神，须用癸滋。 → 《穷通宝鉴·三夏乙木》#8.2
  - `[ns_qttbj_190]` `[trigger: 午月残疾]` `[factor_trigger: month_wu AND tiangan_yi AND bing_revealed AND dizhi_fire_frame AND NOT tiangan_gui]` `[role: 例外处理]` 丙透，支成火局，阳焦木性，此人残疾，无癸必夭，见壬可解。 → 《穷通宝鉴·三夏乙木》#8.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 五月乙木（午月）"
    factor_refs: list = ['dispersed_qi_essay', 'yang_scorches_wood']
    
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
        l1_anchor="qtbj_v1.0.0_2__五月乙木_午月_001_L1",
    )
    version: str = "1.0.0"
