"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725605
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
    semantic_id="zw_v1.0.0_10_巨门星_002",
    book_id="ziwei",
    engine_id="ziwei"
)
class 10巨门星(SemanticEntry):
    """
    #### 8.10 天相星

- 原文（source_text）：

  问：天相星所主若何？
  
  答曰：天相属水，南斗第五星也。为司爵之宿，为福善，化气曰印，是为官禄文星，佐帝之位。若人命逢之...
    """
    
    original_text: str = """#### 8.10 天相星

- 原文（source_text）：

  问：天相星所主若何？
  
  答曰：天相属水，南斗第五星也。为司爵之宿，为福善，化气曰印，是为官禄文星，佐帝之位。若人命逢之，言语诚实，事不虚为，见人难有恻忆之心，见人恶抱不平之气。官禄得之则显荣，帝座合之则五权，虽佐日月之光，兼化廉贞之恶。身命得之而荣耀，子息得之而嗣续昌，十二宫中皆为祥福，不随恶而变志，不因杀而改移，限步逢之，富不可量。
  
  希夷先生曰：天相，南斗司爵之星，化气为印，主人衣食丰足，昌曲左右加会，位至公卿。陷地贪廉、武破，羊陀杀凑，巧艺安身，火铃冲破残疾。女人主聪明端庄，志过丈夫。三方吉拱封赠论。若昌曲冲破，侍妾，在僧道主清高。
  
  歌曰：天相原属水，化印主官禄。身命两官逢，定主多财福。形体又肥满，语言不轻渎。出仕主飞腾，居家主财谷。二限若逢之，有事皆充足。

- 分字分词释义：

  - **天相**：南斗第五星，五行属水，化气为印，主官禄文星。
  - **司爵之宿**：掌管爵位、官阶、品秩与授职的星曜。
  - **化气曰印**：星曜之气转化为印绶象征，主文书、资格与合法性。
  - **官禄文星**：主管官职禄位与文职仕途的星曜。
  - **佐帝之位**：作为紫微帝星的辅佐，地位尊崇。
  - **言语诚实，事不虚为**：天相入命者说话真实、做事诚信不虚伪。
  - **恻忆之心**：同情怜悯之心，见人受难会产生同情。
  - **不平之气**：见到不公不义之事会抱打不平。
  - **不随恶而变志**：在凶星或不利环境中仍保持原则。
  - **不因杀而改移**：不因杀星冲击而改变立场。
  - **昌曲左右加会**：文昌、文曲、左辅、右弼同宫或夹拱。
  - **位至公卿**：官至公卿高位，仕途显达。
  - **巧艺安身**：陷地遇凶时，以手艺技能谋生。
  - **志过丈夫**：女命志向超过丈夫，有主见有能力。
  - **封赠论**：可获朝廷封赠荣誉。

- 核心要点：

  1. **天相化印**：司爵之宿化气为印，主官禄文星。
  2. **佐帝之位**：佐帝之位，不随恶而变志，不因杀而改移。
  3. **衣食丰足**：主人衣食丰足，昌曲左右加会，位至公卿。
  4. **女命聪明**：女人主聪明端庄，志过丈夫，三方吉拱封赠论。
  5. **十二宫祥**：十二宫中皆为祥福，限步逢之富不可量。

- 叙事素材（narrative_snippets）：

  - **化气为印**："天相化气为印，主官禄文星"，天相为印绶官禄之星。
  - **佐帝不变**："佐帝之位，不随恶而变志，不因杀而改移"，天相性情稳定坚定。
  - **昌曲公卿**："昌曲左右加会，位至公卿"，天相配合吉星可至高位。
  - **十二宫祥**："十二宫中皆为祥福，限步逢之富不可量"，天相为吉祥之星。
  - **现代应用**：天相可作为评估"职业稳定性与资质"的核心指标——印绶主凭据与官方认可。

- 完整对等诠释（secondary_lang_full）：

  Tianxiang, the fifth star of the Southern Dipper, embodies the Ministerial Seal—its qi transforms into the emblem of credentials, documents, and official appointment. As a "Star of Titles and Rank," it governs career advancement, honors, and material security. In disposition, Tianxiang is steadfast: it does not bend under evil influence nor shift its principles when confronted by killing stars. Those with Tianxiang prominent enjoy abundant clothing and food; when Wenchang, Wenqu, Zuofu, and Youbi join through aspect or conjunction, the native may rise to ministerial rank. For women, Tianxiang indicates intelligence, dignity, and ambitions that may exceed those of their husbands, with benefic aspects pointing toward imperial honors. Across all twelve palaces, Tianxiang brings auspicious fortune; when encountered during favorable limit periods, wealth becomes immeasurable. The caution is to avoid fallen placements with Tanlang, Lianzhen, Wuqu, Pojun, and the harsh stars converging—such configurations reduce the native to artisanal survival rather than official glory."""
    normalized_text_zh: str = """"""
    subject: str = "10 巨门星"
    factor_refs: list = ['star_tianxiang', 'concept_huaqi_yin', 'concept_sijue', 'trait_busui_ebian', 'combo_changqu_jiahui']
    
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
        l1_anchor="zw_v1.0.0_10_巨门星_002_L1",
    )
    version: str = "1.0.0"
