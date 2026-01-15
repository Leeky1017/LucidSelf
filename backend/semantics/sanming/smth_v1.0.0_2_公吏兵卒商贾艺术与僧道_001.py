"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.081084
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
    semantic_id="smth_v1.0.0_2_公吏兵卒商贾艺术与僧道_001",
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

- 规范化释义（primary_lang_explained）：  
  本段从“人有公吏、军戎、商贾、艺术，四者不同，各有所居”起笔，将命局中的清浊结构、神煞组合与现实职业一一对应。所谓公吏之命，多见刑冲克战、五行错杂不纯：倒食（偏印）逢财，夹贵逢破，财印相刑，说明虽有文才与贵气，却被杂气消耗，只能在衙门、公门中奔走，承担书吏、差役、文案之类的事务性工作。兵卒之命与公吏大体相似，只是煞重身强，带悬针、羊刃之象：格局中虽多克破，却又有福星、贵煞扶持，因此往往以武职出头，在军旅行伍之中，以勇敢与冲突换取权禄与军功。  
  商贾之命，则以偏财旺、驿马多动为核心特征：日时并临子午、寅申，三元值马，象征不停奔波；或构成六合会财，再行财运之地，终身营于买卖、贸易、迁徙之间。“马前无辔”“龙断外土”一类句子，既形容其冒险与机变，也暗示一旦判断失误，极易人财两空。艺术之命，一方面有德秀、学堂加持，秉赋聪明多才；另一方面却犯刑冲空亡、化气不成，禄马不全，所以多在技艺、艺术、小道上见长，而难以获得与才华相称的社会地位。僧道之命则是五行落在死绝无气之乡，十干临墓绝，孤寡、元辰、华盖重重，妻子衰绝、身旺无依——象征与世俗关系渐渐稀薄，却在火盛时走向禅定清明，在水多时趋于云水逍遥，终以出世之路安顿自身。  

- 完整对等诠释（secondary_lang_full）：  
  This passage delineates five broad vocational paths—clerks in public office, soldiers, merchants, artisans, and monks or Taoist priests—by matching each with a characteristic mixture of structure and spirits in the chart. The "official clerk" type is marked by heavy clashes and punishments and by a confused mixture of Five Elements: partial Seals colliding with Wealth, noble stars squeezed or broken, and Wealth and Seals attacking one another. Such a person may possess talent and a touch of noble气, but their abilities are continually drained by conflicting currents, so they tend to serve within government yamen or bureaucratic systems, handling paperwork and errands rather than holding real power. The "soldier" type shares this turbulent quality yet differs in that Killing stars are strong and the Day Master is equally robust, with indicators such as Suspended Needle and Blade. Though danger and injury are present, auspicious stars often lend support, allowing the person to win rank and reward through military courage and life on campaign.  
  The "merchant" pattern centres on vigorous partial Wealth and active travelling stars: Day and Hour in Zi–Wu or Yin–Shen, Horses constantly in motion, or combinations that gather Wealth, especially when the运 cycles repeatedly pass through Wealth territories. Such charts describe lives spent on trade, brokerage and the constant movement between places; there is genuine opportunity for profit, but also the risk implied by "horses without reins" and "dragons cut off from their own soil"—ventures that can just as easily collapse. The "artisan" or "artist" type enjoys the blessing of academic and elegant stars, indicating intelligence and skill, yet these are entangled with clashes, voids and incomplete transformations. The person is gifted but their configurations are broken; achievement tends to concentrate in specialised crafts or arts, with limited worldly recognition. Finally, the "monk/Taoist" type appears when the Five Elements lie in places of death and exhaustion, the stems sit in tomb or extinction, and the chart is saturated with solitude, calamity and Huagai, while the Day Master itself remains strong but unsupported by Wealth, Officer or Seals. Such a life tends to loosen its ties with conventional family and career, moving instead toward monastic discipline or wandering spiritual practice—fiery charts toward intense meditative focus, watery charts toward free‑flowing, cloud‑and‑water detachment.  

- 核心要点：
  - **职业分类**：根据格局清浊、神煞、五行气势定职业。
  - **清枯**：僧道艺术多清枯。
  - **浊杂**：公吏兵卒多浊杂。
  - **流动**：商贾多流动（驿马）。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_021]` `[trigger: 公吏之命]` `[factor_trigger: gongli_zhiming AND xingchong_cuoza]` `[role: 主干]` 公吏之命：多带克刑，东西战斗，南北冲击。长生处破了，死绝处生起。五行错杂，象不纯一。 → 《三命通会》卷十二#公吏兵卒商贾艺术与僧道
  - `[ns_smth_12_022]` `[trigger: 商贾之命]` `[factor_trigger: shanggu_zhiming AND piancai_shenwang]` `[role: 主干依赖]` 商贾之命：日时并临子午，三元都值寅申。马前无辔，劫上逢财。或偏财身旺，复行财运。 → 《三命通会》卷十二#公吏兵卒商贾艺术与僧道
  - `[ns_smth_12_023]` `[trigger: 艺术之命]` `[factor_trigger: yishu_zhiming AND dexiu_xingchong]` `[role: 条件分支]` 艺术之命：命遇德秀，犯刑冲，小道可观。时逢学堂，见空亡，多能可鄙。 → 《三命通会》卷十二#公吏兵卒商贾艺术与僧道
  - `[ns_smth_12_024]` `[trigger: 僧道之命]` `[factor_trigger: sengdao_zhiming AND kongwang_huagai]` `[role: 总结]` 僧道之命：五行在无气之乡，十干临死墓之地。年月尽逢孤寡，日时全见元辰。累犯空亡，重临华盖。妻子衰绝，身旺无依。 → 《三命通会》卷十二#公吏兵卒商贾艺术与僧道"""
    normalized_text_zh: str = """"""
    subject: str = "2 公吏兵卒商贾艺术与僧道"
    factor_refs: list = ['engine_id', 'bazi_structure_factor_36', 'bazi_semantic', 'bazi_relation_geju_wuxing', 'public_clerk', 'bazi_relation_geju_yangren', 'soldier', 'bazi_relation_geju_piancai_yima', 'merchant', 'bazi_relation_geju_1', 'artisan_artist', 'bazi_relation_geju_2', 'monk_taoist', 'source_ref', 'rel_smth_12_022', 'core_factor', 'rel_smth_12_023', 'cond_factor', 'rel_smth_12_024', 'risk_factor', 'evi_smth_12_022', 'core_factor', 'rule_name22', 'evi_smth_12_023', 'cond_factor', 'rule_name23', 'evi_smth_12_024', 'risk_factor', 'rule_name24', 'map_smth_12_015', 'map_smth_12_016']
    
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
        l1_anchor="smth_v1.0.0_2_公吏兵卒商贾艺术与僧道_001_L1",
    )
    version: str = "1.0.0"
