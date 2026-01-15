"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559184
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
    semantic_id="yhzp_v1.0.0_论妇人总诀_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论妇人总诀(SemanticEntry):
    """
    - **原文（source_text）**：推妇人之命，与男命大不同。取官为夫，为福星；财旺生官，则夫纳福。印绶食神为名贵，有称呼。生气印绶，难为子息。印绶财官，必生于富贵之家，才貌贤淑。伤官见官，克...
    """
    
    original_text: str = """- **原文（source_text）**：推妇人之命，与男命大不同。取官为夫，为福星；财旺生官，则夫纳福。印绶食神为名贵，有称呼。生气印绶，难为子息。印绶财官，必生于富贵之家，才貌贤淑。伤官见官，克夫再嫁、身心劳役。财多而淫；故女人要财薄，旺夫益子。七杀正官，只要一位者良；杀多则夫多。官杀被合，乃婢妾姊妹争权。女命只要身弱，主性纯粹而温柔、能奉公姑、助益夫主；身强欺夫，不孝公姑、是非生事、性多急躁。

- **分字分词释义**：
  - **推妇人之命**：专门推断女性命局，与男命判断体系有根本区别。
  - **取官为夫**：女命以正官星代表丈夫，官星即夫星。
  - **财旺生官**：财星旺盛并生扶官星，象征妻子旺夫、丈夫得福。
  - **印绶食神为名贵**：印绶主学识名望，食神主才艺秀气，二者皆主女命有身份地位。
  - **生气印绶，难为子息**：印绶过旺克制食伤（子星），故难有子息。
  - **伤官见官**：伤官克制官星（夫星），女命遇之主克夫。
  - **克夫再嫁**：克制丈夫导致丧偶或离异，需再嫁他人。
  - **财多而淫**：财星过多，女命好物质享乐，易生淫乱之心。
  - **财薄旺夫益子**：财星适度不过旺，方能旺夫且有利子息。
  - **官杀只要一位**：官星或七杀以单一纯正为佳，多则主多夫。
  - **官杀被合**：官星或七杀被他干合去，象征夫被他人争夺。
  - **婢妾姊妹争权**：妾室、姊妹或同辈女性与自己争夺丈夫或家庭地位。
  - **身弱主温柔**：日主偏弱，性情柔顺，能服从丈夫与公婆。
  - **身强欺夫**：日主过强，性情刚硬，凌驾于丈夫之上。
  - **奉公姑**：侍奉公公婆婆，尽儿媳之孝道。
  - **是非生事**：好争好斗，引发家庭矛盾与口舌纷争。

- **规范化释义（primary_lang_explained）**：女命与男命大不同。取官为夫星福星，财生官旺夫；印绶食神主名贵有称呼。伤官见官克夫再嫁身心劳役；财多主淫乱，女人宜财薄旺夫益子；官杀多主多夫；官杀被合主姊妹争权。女命宜身弱性温柔孝顺助夫；身强则欺夫不孝急躁。

- **完整对等诠释（secondary_lang_full）**：Women's fate greatly differs from men's. Takes Officer as husband-star/fortune-star—Wealth generating Officer prospers husband; Seal/Eating God brings nobility and honor. Injuring Officer meeting Officer harms husband causing remarriage and life toil; abundant Wealth brings promiscuity—women should have modest Wealth to prosper husband and children; multiple Officer/Killing brings multiple husbands; Officer/Killing being combined indicates sisters/concubines competing. Women's fate favors weak Self—brings pure gentle nature serving in-laws assisting husband; strong Self brings domineering husband-bullying, unfilial急躁temperament.

- **核心要点**：女命取官为夫财生官旺夫；伤官见官克夫；财多主淫；官杀多主多夫；女命宜身弱温柔孝顺；身强则欺夫不孝

- **详细解说**：  本条是《渊海子平》女命判断的总纲，开宗明义指出"推妇人之命，与男命大不同"——女命的核心逻辑以"夫"与"子"为两大主轴，而非男命的"财"与"官"。在十神映射上：正官为夫星，食神伤官为子星，财星为妾身与物欲，印绶为名望与庇护。吉配方面：官星纯正得位、财星适度生官、印绶食神并见，则"夫荣子贵、才貌贤淑、出身富贵"。凶配方面：伤官见官克制夫星，主"克夫再嫁、身心劳役"；财星过多，主淫乱不贞；官杀多位，主多夫或夫被争夺；印绶太旺克食伤，主难有子息。在身旺身弱的判断上，女命与男命恰好相反：身弱为吉，主"性纯粹而温柔、能奉公姑、助益夫主"；身强为凶，主"欺夫、不孝公姑、是非生事、性多急躁"。这一条可以概括为女命判断的"三看法则"：一看夫星（官杀）得位与否，二看子星（食伤）生旺与否，三看身强身弱的调节作用。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_217]` `[trigger: 女命总则]` `[factor_trigger: nvming AND shishen_guanxing AND fuxing]` `[role: 主干]` 推妇人之命，与男命大不同。取官为夫，为福星；财旺生官，则夫纳福。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_218]` `[trigger: 印绶食神名贵]` `[factor_trigger: nvming AND shishen_yinshou AND shishen_shishen AND minggui AND anchong_qugui AND angui AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 印绶食神为名贵，有称呼；印绶财官，必生于富贵之家，才貌贤淑。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_219]` `[trigger: 印绶难子]` `[factor_trigger: nvming AND shishen_yinshou AND ke_zixing AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 生气印绶，难为子息；印绶过旺则克制食伤子星。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_220]` `[trigger: 伤官见官克夫]` `[factor_trigger: nvming AND shangguan_jianguan AND ke_fu]` `[role: 条件分支]` 伤官见官，克夫再嫁、身心劳役；伤官克制官星（夫星）为女命大忌。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_221]` `[trigger: 财多主淫]` `[factor_trigger: nvming AND caixing_duo AND yin AND abundant_wealth_promiscuity AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 财多而淫；故女人要财薄，旺夫益子。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_222]` `[trigger: 官杀一位]` `[factor_trigger: nvming AND guansha_yiwei AND jixiang]` `[role: 条件分支]` 七杀正官，只要一位者良；杀多则夫多。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_223]` `[trigger: 官杀被合争权]` `[factor_trigger: nvming AND guansha_beihe AND zhengfu]` `[role: 条件分支]` 官杀被合，乃婢妾姊妹争权；夫星被合去则有争夫之象。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_224]` `[trigger: 身弱温柔]` `[factor_trigger: nvming AND shenruo AND wenrou]` `[role: 主干依赖]` 女命只要身弱，主性纯粹而温柔、能奉公姑、助益夫主。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_225]` `[trigger: 身强欺夫]` `[factor_trigger: nvming AND shenqiang AND qifu]` `[role: 例外处理]` 身强欺夫，不孝公姑、是非生事、性多急躁。 → 《渊海子平·论妇人总诀》
  - `[ns_yhzp_226]` `[trigger: 女命三看法则]` `[factor_trigger: nvming AND sankan_faze]` `[role: 总结]` 女命判断三看：一看夫星得位，二看子星生旺，三看身强身弱调节。 → 《渊海子平·论妇人总诀》

- **L2-术语对齐（Term Glossary）**：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|----------|-----------|--------|
| 官星为夫 | Officer as Husband | 女命以正官为夫星 | Women's fate takes Officer as husband-star | officer_husband | existing |
| 财旺生官旺夫 | Wealth Generating Officer Prospers Husband | 财生官主夫贵显 | Wealth generating Officer brings husband's nobility | wealth_officer_prospers_husband | existing |
| 伤官见官克夫 | Injuring Officer Meets Officer Harms Husband | 伤官见官主克夫再嫁 | Injuring Officer meeting Officer harms husband causing remarriage | injuring_officer_harms_husband | existing |
| 财多主淫 | Abundant Wealth Brings Promiscuity | 财星过多主淫乱 | Excessive Wealth brings promiscuous behavior | abundant_wealth_promiscuity | existing |
| 女命身弱为吉 | Women Favor Weak Self | 女命以身弱为佳主温柔 | Women's fate favors weak Self bringing gentle nature | self | existing |"""
    normalized_text_zh: str = """"""
    subject: str = "论妇人总诀"
    factor_refs: list = []
    
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
        l1_anchor="yhzp_v1.0.0_论妇人总诀_001_L1",
    )
    version: str = "1.0.0"
