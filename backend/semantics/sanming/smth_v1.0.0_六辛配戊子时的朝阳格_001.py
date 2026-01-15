"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412322
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
    semantic_id="smth_v1.0.0_六辛配戊子时的朝阳格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 六辛配戊子时的朝阳格(SemanticEntry):
    """
    - **原文（source_text）**：

  《喜忌篇》云：六辛日，时逢戊子，嫌午位，运喜西方。此格六辛日为主，辛以丙为官星，以癸为寿星，喜戊子时，以戊合癸，子乃辛之生地，戊禄在巳，戊来印辛，戊...
    """
    
    original_text: str = """- **原文（source_text）**：

  《喜忌篇》云：六辛日，时逢戊子，嫌午位，运喜西方。此格六辛日为主，辛以丙为官星，以癸为寿星，喜戊子时，以戊合癸，子乃辛之生地，戊禄在巳，戊来印辛，戊乃丙之子，丙见戊印辛，丙却生戊合辛，为贵，辛日得官星也。柱中只宜子字一位，多则不中，怕午冲丑绊，则阴不能朝阳，丙巳填实运行西方金旺之地故喜，东北财伤次之，南方死绝则忌。此格只宜生申辰亥卯未酉月，若生四季，以印绶论，丙午、丙寅、丙戌月以财官论，甲寅、乙卯月只以财论。月令为主，行运不拘南北，身旺为妙，若成此格，多名胜于财，为人高亢，伤妻害子，如犯上忌，贫薄。秘诀云：辛日子时，忌行火地，西北行来则吉，东南一去忧凶。古歌云：辛逢戊子号朝阳，运喜西方禄位昌，丑午丙丁无出现，腰金衣紫入朝堂。又：辛日生时逢戊子，戊来动丙作辛官，六阴金合朝阳格，富贵基是不难；子宫只宜得一位，若连丑位福还悭，丙丁巳午俱无迹，运向西方利不凡。又：朝阳行运喜西方，临到东方也吉昌，最怕北方多不吉，南离冲破主灾殃。

- 分字分词释义：

  - **六辛日**：指六个辛日（辛丑、辛卯、辛巳、辛未、辛酉、辛亥），皆可论入本格，以日干辛为主。
  - **时逢戊子**：时柱天干戊、地支子；戊为土，子为水，子为辛之长生之地。
  - **辛以丙为官星，以癸为寿星**：十干生克中，辛金以丙火为官，以癸水为印、寿星。
  - **戊合癸，子乃辛之生地**：戊土合癸水成印，子水为辛金的生地，共同生扶日主与官星。
  - **戊禄在巳，戊来印辛，丙见戊印辛**：戊之禄在巳宫，巳中丙火生戊、戊又生辛，形成“丙 → 戊 → 辛”的生扶链条。
  - **阴不能朝阳**：若午火、丑土等位冲绊过重，则阴金（辛）难以从子位“朝向”丙火之阳，失却朝阳之义。
  - **运喜西方金旺之地**：以西方申酉戌等金旺运为佳，其次东北财伤运，最忌南方火土死绝运。

- **规范化释义（primary_lang_explained）**：

  六阴朝阳格，是为六个辛日配戊子时的贵格。辛金本为阴金，以丙为官、以癸为印与寿星；时支子水是辛的长生之地，时干戊土又能合癸成印，戊之禄在巳宫，巳中丙火为辛之官。如此一来，形成“丙 → 戊 → 辛”的生扶链条：丙火生戊土，戊土印辛金，辛金得子水生扶，再以丙为官星，故名“六阴朝阳”：阴金得阳火之照临而成贵。
  
  格局要求：柱中只宜一个子字，多则不中；忌午火、丑土过多冲绊子位，使阴金难以“朝阳”；亦忌丙、巳等火位过于填实，使官星、印星之气过重而伤身。月令以申、辰、亥、卯、未、酉等金水或印星得地之月为佳；若生四季月，则多以印绶格论，不必强扯朝阳之名。成格之人，多名重于财，为人高亢，有伤妻害子、犯上忌之倾向，失衡则易贫薄。

- 核心要点：

  - 仅限六辛日配戊子时，为阴金得阳火之官、印同来的贵格。
  - 结构核心是“丙 → 戊 → 辛”生扶链，加上子水长生辛金、戊合癸为印。
  - 子位只宜一支，忌午、丑等过度冲绊；运喜西方金旺之地，忌南方火土死绝。
  - 成格者多重名节、轻财利，性情高傲，需防伤妻害子与犯上之祸。

- 详细解说：

  古书所谓“六阴朝阳”，关键在于“阴金得阳火而不被烧伤”，亦即官星（丙火）有印星（戊合癸）与长生（水局）相调和，使辛金既受其照临，又不致熔化。子水作为辛之生地，承接了从丙至戊、由戊至辛的生扶链条；若子位受午冲、丑绊，则这一链条被打断，阴金便难以真正“朝阳”。
  
  实务判断时，可按以下路径检查：
  1. 是否为辛日且时为戊子；
  2. 子位是否单纯而不被午、丑等重冲重绊；
  3. 是否存在巳中丙戊与戊合癸形成的官印生身结构；
  4. 大运是否多行西方金旺或北方水旺之地，而少走南方火土死绝运。
  
  若上述条件基本具足，则可按六阴朝阳格论贵；若仅有其名而缺其结构，或官印太重、身弱不堪，则宁可退回按印绶、财官等常规格局来判断，以免过度拔高。

- **校勘与字词辨析（双语）**：

  - 原文中“六辛日，时逢戊子，嫌午位，运喜西方”一句，为本格总纲，本稿在释义中拆解为“辛日 + 戊子时 + 忌午位 + 运喜西方”。
  - “辛以丙为官星，以癸为寿星”中“寿星”一词，本稿理解为“印绶兼主寿命、安稳之星”，并在白话中统一为“印星与寿星”。
  - 多首歌诀中关于“子宫只宜得一位”“丙丁巳午俱无迹”等语，本稿在白话与详细解说中转化为对子位纯粹、火土不过旺的结构要求。
  - **English**：
    - The sentence "Six Xin days, hour meets Wu-Zi, dislikes Wu position, fortune favors the West" is the guiding principle; this edition breaks it down as "Xin day + Wu-Zi hour + avoid Wu + Western fortune."
    - The term "longevity star" in "Xin uses Bing as official, Gui as longevity star" is interpreted as "Seal star also governing longevity and stability"; this edition unifies it as "Seal and longevity star."
    - Verses about "Zi palace should have only one" and "Bing-Ding-Si-Wu all absent" are transformed into structural requirements for Zi purity and fire-earth not being excessive.

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_037]` `[trigger: 六阴朝阳定义]` `[factor_trigger: liuyin_chaoyang_presence]` `[role: 主干]` 六辛日，时逢戊子，嫌午位，运喜西方。 → 《三命通会》卷六#六阴朝阳
  - `[ns_smth_06_038]` `[trigger: 戊合癸印]` `[factor_trigger: wu_he_gui AND zi_wei_changsheng]` `[role: 主干依赖]` 戊合癸，子乃辛之生地，戊禄在巳，戊来印辛。 → 《三命通会》卷六#六阴朝阳
  - `[ns_smth_06_039]` `[trigger: 子位单纯]` `[factor_trigger: zi_wei_danyi AND pa_wu_chong]` `[role: 条件分支]` 柱中只宜子字一位，多则不中，怕午冲丑绊。 → 《三命通会》卷六#六阴朝阳
  - `[ns_smth_06_040]` `[trigger: 腰金衣紫]` `[factor_trigger: yao_jin_yi_zi]` `[role: 总结]` 辛逢戊子号朝阳，运喜西方禄位昌，丑午丙丁无出现，腰金衣紫入朝堂。 → 《三命通会》卷六#六阴朝阳

- **完整对等诠释（secondary_lang_full）**：
  The "Six Yin Facing Yang" pattern is a noble configuration for all six Xin days when the hour pillar is Wu-Zi. Xin metal is Yin metal; it takes Bing fire as its Proper Official and Gui water as its Seal and longevity star. In the Wu-Zi hour, Zi water is the long-life position for Xin, while Wu earth on the stem can combine with Gui to form an additional Seal. Wu's own salary seat is in Si, and Si contains Bing fire. This creates a generative chain "Bing → Wu → Xin": Bing fire produces Wu earth, Wu earth seals Xin metal, and Xin metal is nourished by Zi water while receiving Bing as its official star. The name "Six Yin Facing Yang" captures the image of Yin metal being illuminated by Yang fire and thereby rising to nobility.
  
  The pattern requires exactly one Zi branch in the chart; more than one dilutes the structure. Wu fire and Chou earth clashing or tying Zi are especially feared, because they break the chain and prevent Yin metal from "facing Yang". Likewise, excessive Bing or Si filling the chart makes the official and Seal too heavy for the day-master to bear. The best months are those where metal or water is strong—Shen, Chen, Hai, Mao, Wei, You—so that the body can handle the official star. Those who successfully form this pattern tend to value reputation over wealth and display a proud, lofty temperament; they must guard against harming spouse and children or offending superiors."""
    normalized_text_zh: str = """"""
    subject: str = "六辛配戊子时的朝阳格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_13', 'bazi_semantic', 'bazi_structure_bing_wu_xin_config', 'bazi_semantic', 'bazi_state_zi', 'bazi_semantic', 'bazi_state_factor_8', 'bazi_semantic', 'bazi_condition_wu_chou', 'bazi_semantic', 'bazi_condition_factor_141', 'bazi_semantic', 'source_ref', 'rel_smth_06_028', 'liuyin_chaoyang_presence', 'rel_smth_06_029', 'ziwei_chuncu_score', 'rel_smth_06_030', 'yuncheng_fangxiang_jixiong', 'evi_smth_06_028', 'liuyin_chaoyang_presence', 'rule_chaoyang', 'evi_smth_06_029', 'ziwei_chuncu_score', 'rule_ziwei', 'evi_smth_06_030', 'wuchong_chouban_risk', 'rule_chongban', 'map_smth_06_019', 'map_smth_06_020']
    
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
        l1_anchor="smth_v1.0.0_六辛配戊子时的朝阳格_001_L1",
    )
    version: str = "1.0.0"
