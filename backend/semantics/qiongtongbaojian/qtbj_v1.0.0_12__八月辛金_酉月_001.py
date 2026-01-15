"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578513
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
    semantic_id="qtbj_v1.0.0_12__八月辛金_酉月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 12八月辛金酉月(SemanticEntry):
    """
    - **原文（source_text）**：
  八月辛金，当权得令，旺之极矣，专用壬水淘洗，故云：金见水以流通。如见戊己，则生扶太过，故以土为病，见甲制土、方妙。无戊、不宜用甲。
  或四柱一点壬水...
    """
    
    original_text: str = """- **原文（source_text）**：
  八月辛金，当权得令，旺之极矣，专用壬水淘洗，故云：金见水以流通。如见戊己，则生扶太过，故以土为病，见甲制土、方妙。无戊、不宜用甲。
  或四柱一点壬水，甲多泄水，此为用神无力，奸诈之徒。得庚制者，反主仁义。或三点辛金，一重壬水，多见甲木，有庚透者，主大富贵。不见丁为美，若见一丁，此人风雅清高，衣食饶裕而已。
  或一二比肩，壬甲皆一，无庚出干，亦有恩荣。若二三比肩，一点壬水，戊土多见，此为土厚埋金，此人愚懦，见一甲出，必为创立之人。
  或一派辛金，一位壬水，无庚杂乱，又主富中取贵。或一派壬水泄金，无戊出制，为沙水同流，主奔波劳苦。若得支见一戊止流，其人颇有才略，艺术过人。
  或支成金局，干见比肩，无壬淘洗，此宜用丁，无丁必主凶顽无赖。若得一壬高透，以泄群金，又名一清到底，定有治国之材。
  或支成金局，戊己透干，壬透无火，名曰虎格，运行西北，富贵大显，子息艰难。或透丙火，虽有壬出，亦属平庸。
  或一二辛金，一派己土，定为僧道。或干透己土，支见庚甲，一生安闲。或一派乙木，不见庚干，为才多身弱，一见庚制，富贵可期。
  金生秋月土重，贫无寸铁。六辛日逢戊子时，运喜西方，阴若朝阳，切忌丙丁离位。庚辛局全巳酉丑，位高权重。

- **分字分词释义**：
  - **当权得令**：掌权得时令 / 酉月辛金 / 身极旺
  - **金见水以流通**：金遇水而流通 / 壬水泄金 / 口诀
  - **土为病**：土是病因 / 戊己太多 / 忌象
  - **用神无力**：用神力量不足 / 甲多泄壬 / 凶象
  - **奸诈之徒**：奸诈狡猾之人 / 用神无力 / 凶象
  - **土厚埋金**：土多埋没金 / 戊土太多 / 凶象
  - **沙水同流**：沙石随水流去 / 壬多无戊 / 凶象
  - **一清到底**：一片清澈到底 / 一壬泄群金 / 格局名
  - **虎格**：虎形格局 / 金局戊己壬透 / 格局名
  - **治国之材**：治理国家的人才 / 一清到底 / 大贵

- **规范化释义（primary_lang_explained）**：（内容较长保持原文对照释义格式）

- **完整对等诠释（secondary_lang_full）**：（英文完整对应）

- **核心要点**：
  - **首要用神**：壬水专用淘洗
  - **忌神**：戊己生扶太过
  - **配合**：甲木制土庚金发源

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_421]` `[trigger: 辛生酉月]` `[factor_trigger: month_you AND tiangan_xin AND tiangan_ren]` `[role: 主干]` 八月辛金，当权得令，旺之极矣，专用壬水淘洗，故云：金见水以流通。 → 《穷通宝鉴·三秋辛金》#34.12
  - `[ns_qttbj_422]` `[trigger: 一清到底]` `[factor_trigger: month_you AND tiangan_xin AND ren_single AND xin_multiple AND one_clear_to_bottom]` `[role: 条件分支]` 若得一壬高透，以泄群金，又名一清到底，定有治国之材。 → 《穷通宝鉴·三秋辛金》#34.12
  - `[ns_qttbj_423]` `[trigger: 虎格]` `[factor_trigger: month_you AND tiangan_xin AND dizhi_metal_frame AND (tiangan_wu OR tiangan_ji) AND tiangan_ren AND NOT element_fire AND tiger_pattern]` `[role: 条件分支]` 或支成金局，戊己透干，壬透无火，名曰虎格，运行西北，富贵大显。 → 《穷通宝鉴·三秋辛金》#34.12
  - `[ns_qttbj_424]` `[trigger: 沙水同流]` `[factor_trigger: month_you AND tiangan_xin AND ren_multiple AND NOT tiangan_wu AND sand_water_flow]` `[role: 例外处理]` 或一派壬水泄金，无戊出制，为沙水同流，主奔波劳苦。 → 《穷通宝鉴·三秋辛金》#34.12"""
    normalized_text_zh: str = """"""
    subject: str = "12. 八月辛金（酉月）"
    factor_refs: list = ['one_clear_to_bottom', 'tiger_pattern', 'sand_water_flow']
    
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
        l1_anchor="qtbj_v1.0.0_12__八月辛金_酉月_001_L1",
    )
    version: str = "1.0.0"
