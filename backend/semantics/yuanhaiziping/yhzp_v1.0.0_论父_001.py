"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559127
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
    semantic_id="yhzp_v1.0.0_论父_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论父(SemanticEntry):
    """
    - **原文（source_text）**：  
  偏财是父，乃印绶之官星也。如甲日以戊为父，再见甲寅字、或木局全、或临死绝冲刑之地，主克父也；不然，主离异不睦、或疾病残伤。若得庚字申字救，庶无大害...
    """
    
    original_text: str = """- **原文（source_text）**：  
  偏财是父，乃印绶之官星也。如甲日以戊为父，再见甲寅字、或木局全、或临死绝冲刑之地，主克父也；不然，主离异不睦、或疾病残伤。若得庚字申字救，庶无大害。如甲旺戊衰，亦主有疾少靠。如戊临生旺、贵人、天月德地，亦主有贵；更得丙丁生助，享父之福无穷。如临杀地，父死他乡。居衰败受制之处、墓绝之地，主父平常，不得父力也。

- **分字分词释义**：
  - **偏财是父**：偏财代表父亲（我克且阴阳相同者）。
  - **印绶之官星**：偏财克正印，正印为母，偏财为母之夫星，故为父。
  - **甲日以戊为父**：甲木日主以戊土（阳土）为偏财父星。
  - **木局全**：寅卯辰三合木局，木旺克土，主克父。
  - **死绝冲刑**：父星临死绝之地或受冲刑，主父不利。
  - **庚申字救**：庚金申金能克制甲木，救父星。
  - **甲旺戊衰**：日主强财弱，主父有疾少靠。
  - **生旺贵人天月德**：父星临吉神吉地，主父贵。
  - **丙丁生助**：火生土，助旺父星。
  - **临杀地**：父星临七杀之地，主父死他乡。
  - **墓绝之地**：父星临墓绝，主父平常无力。

- **规范化释义（primary_lang_explained）**：  
  偏财是父，乃印绶之官星。如甲日以戊为父，再见甲寅或木局全或临死绝冲刑之地，主克父；不然主离异不睦或疾病残伤。若得庚申字救庶无大害。如甲旺戊衰亦主有疾少靠。如戊临生旺贵人天月德地亦主有贵，更得丙丁生助享父之福无穷。如临杀地父死他乡。居衰败受制墓绝之地，主父平常不得父力。

- **完整对等诠释（secondary_lang_full）**：  
  Indirect Wealth represents the father, being the Officer Star of the Seal (Mother). For instance, if Jia Day uses Wu as father, and one sees Jia-Yin again, or the Wood bureau is complete, or the father star occupies positions of death, extinction, clash, or punishment, it indicates harming the father; otherwise, it signifies separation, discord, disease, or disability. If one obtains Geng or Shen characters for rescue, there will likely be no great harm. If Jia is vigorous and Wu is weak, it also indicates the father having illness or being of little reliance. If Wu occupies positions of Growth-Vigor, Noble Person, or Heaven-Moon Virtue, it indicates the father has nobility; if further obtaining Bing-Ding for generation and assistance, one enjoys endless fortune from the father. If occupying Killing positions, the father dies in a foreign land. If residing in declining, defeated, controlled places or tomb-extinction lands, it indicates an ordinary father from whom one gains no strength.

- **核心要点**：
  - 偏财是父，乃印绶之官星
  - 日主旺财星弱，或财临死绝冲刑，主克父
  - 有救神（克日主者）可减轻克父
  - 财临生旺、贵人、天月德，主父贵
  - 财得火生助，享父之福无穷
  - 财临杀地，主父死他乡
  - 财居墓绝，主父平常不得父力

- **详细解说**：  
  本条专论父亲的判断方法。"偏财是父，乃印绶之官星"——偏财代表父亲的理论依据是：偏财克正印，正印为母，偏财为母之夫星，故为父。以甲日为例："甲日以戊为父"——甲木克戊土，戊为偏财即父星。克父的情况是"再见甲寅字、或木局全、或临死绝冲刑之地"——日主过旺或父星受损则克父；"若得庚字申字救"——有克制日主的五行可救父星。父贵的情况是"戊临生旺、贵人、天月德地"——父星临吉神吉地主父贵；"更得丙丁生助，享父之福无穷"——火生土助旺父星。凶象是"如临杀地，父死他乡"——父星临七杀之地主父客死他乡；"居衰败受制之处、墓绝之地，主父平常，不得父力"——父星无力则父平庸无助。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_161]` `[trigger: 偏财是父]` `[factor_trigger: shishen_piancai AND liuqin_fu AND yinshou_guanxing AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 主干]` 偏财是父，乃印绶之官星也。 → 《渊海子平·论父》
  - `[ns_yhzp_162]` `[trigger: 克父之象]` `[factor_trigger: liuqin_fu AND ke_fu AND rizhu_wang]` `[role: 条件分支]` 如甲日以戊为父，再见甲寅字、或木局全、或临死绝冲刑之地，主克父也。 → 《渊海子平·论父》
  - `[ns_yhzp_163]` `[trigger: 救父之神]` `[factor_trigger: liuqin_fu AND jiu_shen AND ke_rizhu]` `[role: 例外处理]` 若得庚字申字救，庶无大害。 → 《渊海子平·论父》
  - `[ns_yhzp_164]` `[trigger: 日旺财衰]` `[factor_trigger: rizhu_wang AND caixing_shuai AND fu_youji]` `[role: 条件分支]` 如甲旺戊衰，亦主有疾少靠。 → 《渊海子平·论父》
  - `[ns_yhzp_165]` `[trigger: 父贵之象]` `[factor_trigger: liuqin_fu AND shengwang AND guiren AND fugui AND anchong_qugui AND angui AND fugui_pinhan]` `[role: 条件分支]` 如戊临生旺、贵人、天月德地，亦主有贵；更得丙丁生助，享父之福无穷。 → 《渊海子平·论父》
  - `[ns_yhzp_166]` `[trigger: 父死他乡]` `[factor_trigger: liuqin_fu AND sha_di AND fu_si_taxiang]` `[role: 例外处理]` 如临杀地，父死他乡。 → 《渊海子平·论父》
  - `[ns_yhzp_167]` `[trigger: 不得父力]` `[factor_trigger: liuqin_fu AND shuaibai AND bude_fuli]` `[role: 总结]` 居衰败受制之处、墓绝之地，主父平常，不得父力也。 → 《渊海子平·论父》"""
    normalized_text_zh: str = """"""
    subject: str = "论父"
    factor_refs: list = ['indirect_wealth_father', 'new_candidate']
    
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
        l1_anchor="yhzp_v1.0.0_论父_001_L1",
    )
    version: str = "1.0.0"
