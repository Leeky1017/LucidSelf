"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.081215
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
    semantic_id="smth_v1.0.0_2_公吏兵卒商贾艺术与僧道_002",
    book_id="sanming",
    engine_id="bazi"
)
class 2公吏兵卒商贾艺术与僧道(SemanticEntry):
    """
    - 原文（source_text）：
  人有公吏、军戎、商贾、艺术，四者不同，各有所居。
  **公吏之命**：多带克刑，东西战斗，南北冲击。长生处破了，死绝处生起。五行错杂，象不纯一。倒食逢财，夹...
    """
    
    original_text: str = """- 原文（source_text）：
  人有公吏、军戎、商贾、艺术，四者不同，各有所居。
  **公吏之命**：多带克刑，东西战斗，南北冲击。长生处破了，死绝处生起。五行错杂，象不纯一。倒食逢财，夹贵逢破。财印相刑，引用无气。秀中带鬼，贵气损伤。干支重会，提纲悬针。此等之命，不离公门。
  **兵卒之命**：与吏大同。局中煞重而干支不等，象内贵轻而主本破伤。甲见卯支，丙临三丁之地；辛向亥地，壬家二癸之乡；乙丁逢蛇，戊土奔马。此乃悬针羊刃，更犯克破刑冲，又带福气，凶中有吉。悬针遇吉煞相扶，羊刃有贵神相助，由是从行伍而有权禄。
  **商贾之命**：日时并临子午，三元都值寅申。马前无辔，劫上逢财。或偏财身旺，复行财运；或六合会财，更坐马乡。壬人运南，丙人运北。经营买卖之人，贸迁有无之辈。甲乙居坎，犯壬癸未免萍梗他乡；元武遇亥，无戊己谅必龙断外土。
  **艺术之命**：又非商贾。命遇德秀，犯刑冲，小道可观。时逢学堂，见空亡，多能可鄙。乙庚化金于坎艮，丁壬化木于兑乾... 此乃秀而不秀，化而不成，格局破损，禄马不全。原夫秉赋聪明，多因生遇学堂；至于成就淡薄，乃是命无根本。
  **僧道之命**：五行在无气之乡，十干临死墓之地。年月尽逢孤寡，日时全见元辰。累犯空亡，重临华盖。妻子衰绝，身旺无依。火盛而身心禅定，水多而自在逍遥。

- 分字分词释义：
  - **公吏**：指古代衙门中的书吏、差役。特征是刑冲多、格局不清、财印相碍。
  - **兵卒**：军人。煞重身强，悬针羊刃。
  - **商贾**：商人。偏财旺，驿马动，身旺财乡。
  - **艺术**：技艺之人。德秀刑冲，学堂空亡，化气不成。
  - **僧道**：出家。死绝空亡，孤寡华盖，身旺无依。

- **规范化释义（primary_lang_explained）**：
  **公吏**：命局多刑冲克战，五行错杂不纯。倒食（偏印）逢财，夹贵被破，财印相刑。虽有秀气但带鬼（煞），贵气受损。多在公门役使。
  **兵卒**：煞重身强，悬针羊刃。虽有克破，但带福气（吉煞），凶中有吉。凭武勇在行伍中获权禄。
  **商贾**：日时子午寅申（冲动），马星奔腾。身旺偏财旺，或合财局。水火日主运行财地。漂泊他乡，贸易获利。
  **艺术**：命带德秀、学堂，聪明。但犯刑冲空亡，格局破损，化气不成。虽多能多艺，但成就淡薄，因命无根本（身弱或无财官）。
  **僧道**：五行死绝无气，满盘孤寡元辰空亡华盖。身旺而无财官倚托（无依）。火盛者身心禅定，水多者逍遥自在。

- 核心要点：
  - **职业分类**：根据格局清浊、神煞、五行气势定职业。
  - **清枯**：僧道艺术多清枯。
  - **浊杂**：公吏兵卒多浊杂。
  - **流动**：商贾多流动（驿马）。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_049]` `[trigger: 公吏之命]` `[factor_trigger: gongli_zhiming AND xingchong_cuoza]` `[role: 主干]` 公吏之命：多带克刑，东西战斗，南北冲击。长生处破了，死绝处生起。五行错杂，象不纯一。 → 《三命通会》卷十二#公吏兵卒商贾艺术与僧道
  - `[ns_smth_12_050]` `[trigger: 商贾之命]` `[factor_trigger: shanggu_zhiming AND piancai_shenwang]` `[role: 主干依赖]` 商贾之命：日时并临子午，三元都值寅申。马前无辔，劫上逢财。或偏财身旺，复行财运。 → 《三命通会》卷十二#公吏兵卒商贾艺术与僧道
  - `[ns_smth_12_051]` `[trigger: 艺术之命]` `[factor_trigger: yishu_zhiming AND dexiu_xingchong]` `[role: 条件分支]` 艺术之命：命遇德秀，犯刑冲，小道可观。时逢学堂，见空亡，多能可鄙。 → 《三命通会》卷十二#公吏兵卒商贾艺术与僧道
  - `[ns_smth_12_052]` `[trigger: 僧道之命]` `[factor_trigger: sengdao_zhiming AND kongwang_huagai]` `[role: 总结]` 僧道之命：五行在无气之乡，十干临死墓之地。年月尽逢孤寡，日时全见元辰。累犯空亡，重临华盖。妻子衰绝，身旺无依。 → 《三命通会》卷十二#公吏兵卒商贾艺术与僧道
  - `[ns_smth_12_caiyin]` `[trigger: 财印] [factor_trigger: caiyin]` `[role: 十神]` 财印者，财与印绶。 → `《三命通会·卷十二》#看命总论`
  - `[ns_smth_12_guanxing]` `[trigger: 官星] [factor_trigger: guanxing]` `[role: 十神]` 官星者，正官七杀。 → `《三命通会·卷十二》#看命总论`
  - `[ns_smth_12_qisha]` `[trigger: 七杀] [factor_trigger: qisha]` `[role: 十神]` 七杀者，偏官之称。 → `《三命通会·卷十二》#看命总论`
  - `[ns_smth_12_shangguan]` `[trigger: 伤官] [factor_trigger: shangguan]` `[role: 十神]` 伤官者，克官之神。 → `《三命通会·卷十二》#看命总论`
  - `[ns_smth_12_xiangzi]` `[trigger: 象子] [factor_trigger: xiangzi]` `[role: 命理]` 象子者，象之子。 → `《三命通会·卷十二》#看命总论`
  - `[ns_smth_12_yangren]` `[trigger: 羊刃] [factor_trigger: yangren]` `[role: 神煞]` 羊刃者，禄前一位。 → `《三命通会·卷十二》#看命总论`"""
    normalized_text_zh: str = """"""
    subject: str = "2 公吏兵卒商贾艺术与僧道"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_41', 'bazi_semantic', 'bazi_state_geju_2', 'bazi_semantic', 'bazi_state_geju_3', 'bazi_semantic', 'bazi_state_geju_4', 'bazi_semantic', 'bazi_state_geju_5', 'bazi_semantic', 'bazi_state_geju_6', 'bazi_semantic', 'source_ref', 'rel_smth_12_043', 'core_factor', 'rel_smth_12_044', 'cond_factor', 'rel_smth_12_045', 'risk_factor', 'evi_smth_12_043', 'core_factor', 'rule_name43', 'evi_smth_12_044', 'cond_factor', 'rule_name44', 'evi_smth_12_045', 'risk_factor', 'rule_name45', 'map_smth_12_029', 'map_smth_12_030']
    
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
        l1_anchor="smth_v1.0.0_2_公吏兵卒商贾艺术与僧道_002_L1",
    )
    version: str = "1.0.0"
