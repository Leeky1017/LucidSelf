"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559401
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
    semantic_id="yhzp_v1.0.0_妖祥赋_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 妖祥赋(SemanticEntry):
    """
    - **原文（source_text）**：
  命理深微，子平可推；先要取其日干，次则详其月令。年时共表其吉凶，《妖祥》不忒于岁月，通参于成败，祸福无遗。或有不见之形，须当审究；更有分抽之绪，后学难...
    """
    
    original_text: str = """- **原文（source_text）**：
  命理深微，子平可推；先要取其日干，次则详其月令。年时共表其吉凶，《妖祥》不忒于岁月，通参于成败，祸福无遗。或有不见之形，须当审究；更有分抽之绪，后学难知。
  天清地浊，自然禀一气之生。
  五行正贵，忌刑冲克破之乡。
  四柱支干，喜三合六合之地。
  寅申巳亥，乃财官印绶长生。
  辰戌丑未，系禄马印星奇库。
  日贵时贵，大忌刑冲克破。
  拱禄拱贵，最怕填实刑冲。
  观无合有合，逢凶不凶。
  伤官之于年，运到官乡不喜。
  阳刃冲合岁君，运临而祸至。
  辰戌魁罡，忌官星怕逢七杀。
  金神日刃，喜七杀而忌刑冲。
  时上偏官要制伏，弱身强官。
  专杀莫逢鬼旺，亦要制伏为强；但看本有本无，遇而不遇，要禀中和。
  辛亥多逢丑地，怕填实，不喜官星。（飞天禄马格）
  甲子日再逢子时，嫌丑午，亦畏庚辛壬癸亥子。（子遥巳格）
  禄马飞天，离巽（巳）丙丁聚巳午。
  倒冲天禄，壬骑龙背，辰多冲戌官星。
  乙用丙子，聚贵声名。（乙巳鼠贵格）
  嗟夫！财命有气，背禄而不贫；绝财命衰，纵建禄而不富。
  癸到艮（寅）山，怕庚辛忌逢戊土。（刑合格）
  壬逢丑地，忌戊己怕见庚金。
  庚遇申子辰，乃井栏叉，又谓之入局，忌丙丁，愁巳午。（井栏叉格）
  戊见申时，怕甲丙亦忌寅卯。（合禄格）
  辛金己土若遇，谓之‘从格’，名为‘秀气’；四柱火伤又无救，是灾迍邅。
  辛日戊子时，忌子多怕日相冲。（六阴朝阳格）
  阳水逢辰见戊己，灾临难避。
  甲见己时，偏财运喜财乡。
  丁日辛年号岁财，运逢戊贵。
  乙逢申位，忌见刑冲。
  日时归禄，官逢有祸。（归禄格）
  另有天冲地击、阴错阳差、贪合忘官、劫先财后，名难成贵。
  贪合忘杀，身旺时福，福禄增加。
  官藏杀见，有制伏亦自辉煌。
  官见杀藏，身弱后终见波渣。
  身弱喜逢旺运。身强最爱杀乡。
  将来者进，功成者退，富贵喜重犯者奇；宜通变而推，决无差误矣！

- **分字分词释义**：
  - **命理深微子平可推**：命理深奥微妙，子平法可以推算。
  - **先要取其日干次则详其月令**：首看日干，次看月令。
  - **五行正贵忌刑冲克破**：五行纯正主贵，忌刑冲克破。
  - **寅申巳亥乃财官印绶长生**：四长生之地，财官印绶得生旺。
  - **辰戌丑未系禄马印星奇库**：四墓库之地，禄马印星入库。
  - **拱禄拱贵最怕填实刑冲**：拱格忌填实或刑冲。
  - **辰戌魁罡忌官星怕逢七杀**：魁罡格忌官杀。
  - **金神日刃喜七杀而忌刑冲**：金神格喜杀制，忌刑冲。
  - **财命有气背禄而不贫**：财旺命强，虽无禄亦不贫。
  - **贪合忘杀身旺时福**：合神化解七杀，身旺则福禄增加。

- **规范化释义（primary_lang_explained）**：
  本篇《妖祥赋》论述命理吉凶的诸多法则，涵盖正格与外格：
  1. **总论**：日干为主，月令为重，年时参断吉凶。
  2. **五行喜忌**：五行正贵忌刑冲克破；喜三合六合之地。
  3. **长生墓库**：寅申巳亥为长生，辰戌丑未为墓库，各有妙用。
  4. **特殊格局**：
     - **拱格**（拱禄拱贵）：忌填实刑冲。
     - **魁罡格**：忌官星七杀。
     - **金神格**：喜七杀制，忌刑冲。
     - **飞天禄马**（辛亥丑地）：忌填实官星。
     - **子遥巳格**（甲子日子时）：忌丑午庚辛。
  5. **身强身弱**：身弱喜旺运，身强爱杀乡。贪合忘杀可化凶为吉。

- **完整对等诠释（secondary_lang_full）**：
  **Auspicious & Inauspicious Treatise (Yao Xiang Fu)**:
  - **Core Principles**: Day Stem is master; Month Command is priority. Examine Year and Hour together for fortune assessment.
  - **Five Elements**: Pure Five Elements indicate nobility; dread Penalty/Clash/Control/Destruction.
  - **Long Life & Tombs**: Yin/Shen/Si/Hai are Long Life positions; Chen/Xu/Chou/Wei are Tomb positions.
  - **Special Patterns**:
    - **Embracing Salary/Nobility**: Fears filling in or clashing.
    - **Kui Gang**: Fears Officer and Seven Killings.
    - **Golden Spirit**: Favors Killing control, dreads Penalty/Clash.
    - **Flying Sky Salary Horse**: Fears filling in and Officers.
  - **Body Strength**: Weak Self favors strengthening luck; Strong Self loves Killing luck. "Greedy Combination Forgetting Killing" transforms danger into blessing.

- **核心要点**：
  - **日主月令**：日干为主，月令为重
  - **格局喜忌**：拱格忌填实，魁罡忌官杀，金神喜杀
  - **身强身弱**：弱喜旺运，强爱杀乡
  - **贪合忘杀**：合化七杀，转凶为吉

- **详细解说**：  《妖祥赋》是子平法论述吉凶格局的重要篇章，开篇即定调"命理深微，子平可推"，强调日干月令的核心地位。**五行法则**——"五行正贵，忌刑冲克破之乡"，纯正无破主贵；"喜三合六合之地"，合局增益格局。**长生墓库**——"寅申巳亥，乃财官印绶长生"主生旺得力；"辰戌丑未，系禄马印星奇库"主入库收藏。**特殊格局**——"拱禄拱贵，最怕填实刑冲"；"辰戌魁罡，忌官星怕逢七杀"；"金神日刃，喜七杀而忌刑冲"等各格喜忌。**身强身弱**——"身弱喜逢旺运，身强最爱杀乡"，揭示运程配合的原理。**贪合忘杀**——"贪合忘杀，身旺时福，福禄增加"，合神化解七杀可转凶为吉。末句"宜通变而推，决无差误"点明论命需灵活变通。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_696]` `[trigger: 日干月令为主]` `[factor_trigger: rigan_weizhu AND yueling_xiang AND lunming_hexin]` `[role: 主干]` 先要取其日干，次则详其月令；日干月令为论命核心。 → 《渊海子平·妖祥赋》
  - `[ns_yhzp_697]` `[trigger: 五行正贵忌破]` `[factor_trigger: wuxing_zhenggui AND ji_xingchong_kepo AND xi_sanhe_liuhe AND anchong_qugui AND angui]` `[role: 条件分支]` 五行正贵，忌刑冲克破之乡；四柱支干喜三合六合之地。 → 《渊海子平·妖祥赋》
  - `[ns_yhzp_698]` `[trigger: 拱格忌填实]` `[factor_trigger: gonglu_gonggui AND zuipa_tianshi_xingchong AND anchong_qugui AND angui]` `[role: 条件分支]` 拱禄拱贵，最怕填实刑冲；拱格特殊喜忌。 → 《渊海子平·妖祥赋》
  - `[ns_yhzp_699]` `[trigger: 魁罡忌官杀]` `[factor_trigger: chenxu_kuigang AND ji_guanxing_qisha AND ji_guansha AND kui_gang_pattern]` `[role: 条件分支]` 辰戌魁罡，忌官星怕逢七杀；魁罡格喜忌。 → 《渊海子平·妖祥赋》
  - `[ns_yhzp_700]` `[trigger: 金神喜杀]` `[factor_trigger: jinshen_riren AND xi_qisha AND ji_xingchong AND golden_spirit_pattern]` `[role: 条件分支]` 金神日刃，喜七杀而忌刑冲；金神格需杀制。 → 《渊海子平·妖祥赋》
  - `[ns_yhzp_701]` `[trigger: 身弱身强运程]` `[factor_trigger: shenruo_xi_wangyun AND shenqiang_ai_shaxiang]` `[role: 条件分支]` 身弱喜逢旺运，身强最爱杀乡；运程配合法则。 → 《渊海子平·妖祥赋》
  - `[ns_yhzp_702]` `[trigger: 贪合忘杀]` `[factor_trigger: tanhe_wangsha AND shenwang AND fulu_zengjia]` `[role: 条件分支]` 贪合忘杀，身旺时福，福禄增加；合化七杀转吉。 → 《渊海子平·妖祥赋》
  - `[ns_yhzp_703]` `[trigger: 妖祥赋纲领]` `[factor_trigger: yaoxiang_fu AND teshu_geju AND tongbian_tuiduan]` `[role: 总结]` 妖祥赋以日干月令为主，论拱格魁罡金神等特殊格局喜忌，强调通变推断。 → 《渊海子平·妖祥赋》"""
    normalized_text_zh: str = """"""
    subject: str = "妖祥赋"
    factor_refs: list = ['auspicious_inauspicious', 'embracing_pattern', 'kui_gang_pattern', 'greedy_combination']
    
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
        l1_anchor="yhzp_v1.0.0_妖祥赋_001_L1",
    )
    version: str = "1.0.0"
