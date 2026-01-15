"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559135
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
    semantic_id="yhzp_v1.0.0_论母_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论母(SemanticEntry):
    """
    - **原文（source_text）**：  
  正印者，乃生我之身也。如甲日以癸为母，遇己丑未主克母；见多，主母嫁二夫。一戊失地、或被克，主母伤前夫。戊字受生、或印临桃花沐浴，母有外情。如印长生...
    """
    
    original_text: str = """- **原文（source_text）**：  
  正印者，乃生我之身也。如甲日以癸为母，遇己丑未主克母；见多，主母嫁二夫。一戊失地、或被克，主母伤前夫。戊字受生、或印临桃花沐浴，母有外情。如印长生，主母慈淑寿长、益和子母。如临阳刃杀地、或值绝墓孤寡，主母不贤或有残疾不睦。须以理推，无不验矣！

- **分字分词释义**：
  - **正印**：生我且阴阳相异者，代表母亲。
  - **生我之身**：正印生日主，故为母亲。
  - **甲日以癸为母**：甲木日主以癸水（阴水）为正印母星。
  - **遇己丑未**：己土克癸水，丑未为土旺之地，主克母。
  - **见多主母嫁二夫**：正官（母之夫星）多见，主母再嫁。
  - **戊失地或被克**：戊为偏财父星，受损主母伤前夫。
  - **桃花沐浴**：印星临桃花沐浴，主母有外情。
  - **印长生**：印星临长生之地，主母慈淑寿长。
  - **阳刃杀地**：印星临凶神之地，主母不贤。
  - **绝墓孤寡**：印星临凶地，主母有残疾不睦。

- **规范化释义（primary_lang_explained）**：  
  正印者乃生我之身。如甲日以癸为母，遇己丑未主克母；见多主母嫁二夫。一戊失地或被克主母伤前夫。戊字受生或印临桃花沐浴母有外情。如印长生主母慈淑寿长益和子母。如临阳刃杀地或值绝墓孤寡，主母不贤或有残疾不睦。须以理推无不验。

- **完整对等诠释（secondary_lang_full）**：  
  Proper Seal is that which gives birth to my body. For instance, if Jia Day uses Gui as mother, encountering Ji, Chou, or Wei indicates harming the mother; if these are numerous, it indicates the mother marrying two husbands. If one Wu loses its position or is controlled, it indicates the mother harming her former husband. If the Wu character receives generation, or the Seal occupies Peach Flower or Bathing positions, the mother has extramarital affairs. If the Seal is in Long Life phase, it indicates the mother is compassionate, virtuous, and long-lived, with harmony between mother and child. If occupying Yang Blade or Killing positions, or encountering Extinction, Tomb, Solitude, or Widowhood phases, it indicates the mother is not virtuous, or has disabilities, or is discordant. One must deduce based on these principles, and it will invariably be accurate!

- **核心要点**：
  - 正印者乃生我之身，代表母亲
  - 印星受克（遇财星）主克母
  - 官星多见，主母嫁二夫
  - 父星受损，主母伤前夫
  - 印临桃花沐浴，主母有外情
  - 印临长生，主母慈淑寿长
  - 印临凶神凶地，主母不贤或有残疾

- **详细解说**：  
  本条专论母亲的判断方法。"正印者，乃生我之身也"——正印生日主，故代表母亲。以甲日为例："甲日以癸为母"——甲木日主以癸水（阴水生阳木）为正印母星。克母的情况是"遇己丑未主克母"——己土克癸水，丑未为土旺之地，财克印主克母。"见多，主母嫁二夫"——官星（母之夫星）多见主母再嫁。"一戊失地、或被克，主母伤前夫"——戊为偏财父星，受损主母伤前夫。母亲品行的判断："印临桃花沐浴，母有外情"——印星临桃花主母有外遇。"印长生，主母慈淑寿长"——印星临长生主母贤良长寿。"临阳刃杀地、或值绝墓孤寡，主母不贤或有残疾不睦"——印星临凶神凶地主母不贤或有残疾。
 
- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_168]` `[trigger: 正印为母]` `[factor_trigger: proper_seal_mother AND mother_relationship]` `[role: 主干]` 正印者，乃生我之身也。 → 《渊海子平·论母》
  - `[ns_yhzp_169]` `[trigger: 克母之象]` `[factor_trigger: proper_seal_mother AND pattern_harm_mother_proposal]` `[role: 条件分支]` 如甲日以癸为母，遇己丑未主克母。 → 《渊海子平·论母》
  - `[ns_yhzp_170]` `[trigger: 母嫁二夫]` `[factor_trigger: proper_seal_mother AND direct_officer AND mu_jia_erfu]` `[role: 条件分支]` 见多，主母嫁二夫。 → 《渊海子平·论母》
  - `[ns_yhzp_171]` `[trigger: 母伤前夫]` `[factor_trigger: proper_seal_mother AND direct_wealth]` `[role: 条件分支]` 一戊失地、或被克，主母伤前夫。 → 《渊海子平·论母》
  - `[ns_yhzp_172]` `[trigger: 母有外情]` `[factor_trigger: proper_seal_mother AND wealth_peach_blossom AND taohua_muyu]` `[role: 例外处理]` 戊字受生、或印临桃花沐浴，母有外情。 → 《渊海子平·论母》
  - `[ns_yhzp_173]` `[trigger: 母慈淑寿长]` `[factor_trigger: proper_seal_mother AND seal_generating_self AND changsheng]` `[role: 条件分支]` 如印长生，主母慈淑寿长、益和子母。 → 《渊海子平·论母》
  - `[ns_yhzp_174]` `[trigger: 母不贤]` `[factor_trigger: proper_seal_mother AND yang_blade AND juemu_guagua]` `[role: 总结]` 如临阳刃杀地、或值绝墓孤寡，主母不贤或有残疾不睦。 → 《渊海子平·论母》"""
    normalized_text_zh: str = """"""
    subject: str = "论母"
    factor_refs: list = ['proper_seal_mother', 'pattern_harm_mother_proposal']
    
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
        l1_anchor="yhzp_v1.0.0_论母_001_L1",
    )
    version: str = "1.0.0"
