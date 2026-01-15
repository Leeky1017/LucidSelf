"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558759
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
    semantic_id="yhzp_v1.0.0_论疾病_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论疾病(SemanticEntry):
    """
    - **原文（source_text）**：夫疾病者，乃精神气血之所主，各有感伤；内曰'脏腑'，外曰'肢体'。八字干支，五行生克之义，取伤重者而断之；五行干支太旺、不及俱病。且如生命，天干内府所属，诗...
    """
    
    original_text: str = """- **原文（source_text）**：夫疾病者，乃精神气血之所主，各有感伤；内曰'脏腑'，外曰'肢体'。八字干支，五行生克之义，取伤重者而断之；五行干支太旺、不及俱病。且如生命，天干内府所属，诗曰：'甲肝，乙胆，丙小肠，丁心，戊胃，己脾乡，庚是大肠，辛属肺，壬是膀胱，癸肾脏。'天干外支所属：'甲头，乙项，丙肩求，丁心，戊胁，己属腹，庚系人脐，辛为股，壬胫，癸足自来求。'

- **分字分词释义**：
  - **疾病**：身体的不适与病症，由五行失衡所致。
  - **精神气血**：人体生命活动的基本物质与能量，精神为意识活动，气血为生理基础。
  - **脏腑**：五脏六腑，内部器官，各有对应天干。
  - **肢体**：四肢躯干，外部身体部位，各有对应天干。
  - **太旺**：五行过于强盛，物极必反而致病。
  - **不及**：五行过于衰弱，功能不足而致病。
  - **甲肝乙胆**：甲木对应肝脏，乙木对应胆囊，以此类推。
  - **甲头乙项**：甲木对应头部，乙木对应颈项，以此类推。

- **规范化释义（primary_lang_explained）**：疾病由精神气血失调所致，内为脏腑，外为肢体。八字中五行过旺或不及皆主病。天干对应内脏：甲肝乙胆丙小肠丁心戊胃己脾庚大肠辛肺壬膀胱癸肾。天干对应外体：甲头乙项丙肩丁心戊胁己腹庚脐辛股壬胫癸足。根据五行受克情况判断疾病部位。

- **完整对等诠释（secondary_lang_full）**：Illnesses stem from imbalanced vital essence, spirit, qi, and blood—internally affecting organs, externally affecting limbs. In Eight Characters, Five Elements excessively prosperous or deficient both bring disease. Heavenly Stems correspond to internal organs: Jia-liver, Yi-gallbladder, Bing-small intestine, Ding-heart, Wu-stomach, Ji-spleen, Geng-large intestine, Xin-lungs, Ren-bladder, Gui-kidneys. Stems also correspond to external body parts: Jia-head, Yi-neck, Bing-shoulders, Ding-heart, Wu-ribs, Ji-abdomen, Geng-navel, Xin-thighs, Ren-shins, Gui-feet. Judge disease location based on which element receives control/injury.

- **核心要点**：
  - 疾病由精神气血失调所致
  - 五行过旺或不及皆主病
  - 天干对应内脏：甲肝乙胆丙小肠丁心戊胃己脾庚大肠辛肺壬膀胱癸肾
  - 天干对应外体：甲头乙项丙肩丁心戊胁己腹庚脐辛股壬胫癸足
  - 根据五行受克情况判断疾病部位

- **详细解说**：  
  本条论述命理与疾病的关系，是"命医同源"理论的具体体现。疾病的根源在于"精神气血"的失调，外在表现为脏腑和肢体的病变。子平法判断疾病的核心原则是"五行干支太旺、不及俱病"——任何五行过于强盛（太旺）或过于衰弱（不及）都会导致对应部位的疾病。本条给出了两套天干对应系统：一是内脏系统（甲肝乙胆等），一是外体系统（甲头乙项等）。判断时，需找出命局中受克最重或失衡最严重的五行，其对应的脏腑或肢体即为易患病部位。例如命中木被金克伤严重，则易患肝胆之疾或头颈之疾。此理论与中医"五行配五脏"高度吻合，体现了命理与医理的相通。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_690]` `[trigger: 疾病根源]` `[factor_trigger: day_master_strength]` `[role: 主干]` 疾病者，乃精神气血之所主，各有感伤。 → 《渊海子平·论疾病》
  - `[ns_yhzp_691]` `[trigger: 五行致病]` `[factor_trigger: five_element_generation AND five_element_imbalance]` `[role: 主干依赖]` 五行干支太旺、不及俱病。 → 《渊海子平·论疾病》
  - `[ns_yhzp_692]` `[trigger: 天干配脏腑]` `[factor_trigger: stem_organ_mapping]` `[role: 条件分支]` 甲肝，乙胆，丙小肠，丁心，戊胃，己脾，庚大肠，辛肺，壬膀胱，癸肾。 → 《渊海子平·论疾病》
  - `[ns_yhzp_693]` `[trigger: 天干配肢体]` `[factor_trigger: stem_body_mapping AND body_vigorous_no_reliance AND body_vigorous_weak_adjustment]` `[role: 条件分支]` 甲头，乙项，丙肩，丁心，戊胁，己腹，庚脐，辛股，壬胫，癸足。 → 《渊海子平·论疾病》
  - `[ns_yhzp_033]` `[trigger: 判断病位]` `[factor_trigger: five_element_control]` `[role: 总结]` 取伤重者而断之，五行受克即为易病部位。 → 《渊海子平·论疾病》"""
    normalized_text_zh: str = """"""
    subject: str = "论疾病"
    factor_refs: list = ['stem_organ_mapping', 'stem_body_mapping', 'five_element_imbalance']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论疾病_001_L1",
    )
    version: str = "1.0.0"
