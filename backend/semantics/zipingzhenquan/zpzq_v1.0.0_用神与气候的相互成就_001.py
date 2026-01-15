"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.524025
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
    semantic_id="zpzq_v1.0.0_用神与气候的相互成就_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 用神与气候的相互成就(SemanticEntry):
    """
    - **原文（source_text）**：
  论命惟以月令用神为主，然亦须配气候而互参之。譬如英雄豪杰，生得其时，自然事半功倍；遭时不顺，虽有奇才，成功不易。

  是以印绶遇官，此谓官印双全，无...
    """
    
    original_text: str = """- **原文（source_text）**：
  论命惟以月令用神为主，然亦须配气候而互参之。譬如英雄豪杰，生得其时，自然事半功倍；遭时不顺，虽有奇才，成功不易。

  是以印绶遇官，此谓官印双全，无人不贵。而冬木逢水，虽透官星，亦难必贵，盖金寒而水益冻，冻水不能生木，其理然也。身印两旺，透食则贵，凡印格皆然。而用之冬木，尤为秀气，以冬木逢火，不惟可以泄身，而即可以调候也。

  伤官见官，为祸百端，而金水见之，反为秀气。非官之不畏夫伤，而调候为急，权而用之也。伤官带煞，随时可用，而用之冬金，其秀百倍。

  伤官佩印，随时可用，而用之夏木，其秀百倍，火济水，水济火也。

  伤官用财，本为贵格，而用之冬水，即使小富，亦多不贵，冻水不能生木也。

  伤官用财，即为秀气，而用之夏木，贵而不甚秀，燥土不甚灵秀也。

  春木逢火，则为木火通明，而夏木不作此论；秋金遇水，则为金水相涵，而冬金不作此论。气有衰旺，取用不同也。春木逢火，木火通明，不利见官；而秋金遇水，金水相涵，见官无碍。假如庚生申月，而支中或子或辰，会成水局，天干透丁，以为官星，只要壬癸不透露干头，便为贵格，与食神伤官喜见官之说同论，亦调候之道也。

  食神虽逢正印，亦谓夺食，而夏木火盛，轻用之亦秀而贵，与木火伤官喜见水同论，亦调候之谓也。

  此类甚多，不能悉述，在学者引伸触类，神而明之而已。

- 原注（原文注解）：
  　　本段在“用神变化”与“格局高低”之后，专门强调一条往往被忽略的原则：**用神必须与气候（时令寒暖燥湿）相配合**，否则再好的格局，也可能因为调候失当而大打折扣。
  - 开篇以“英雄豪杰”比喻：生逢其时，则事半功倍；遭时不顺，则成就不易。
  - 正格与气候的数个对比：
    - 印绶遇官为“官印双全”之贵格，但若“冬木逢水”，则金寒水冻，水不能生木，即使官星透出，也难言显贵；
    - 身印两旺透食，本是印格之贵，而用之冬木，更显秀气——冬木逢火，一则泄身，二则调候，故更佳；
    - 伤官见官平素为大忌，而在金水局中，反而成为“秀气”——并非官不畏伤，而是寒凉太重，以调候为急，权而用之；
    - 伤官带煞、伤官佩印等格，随时可用，但若用在冬金、夏木等特定气候，则其秀气倍增或减损。
  - 结尾指出：
    - 春木逢火成“木火通明”，夏木不必强求同论；
    - 秋金遇水成“金水相涵”，冬金不必强求同论；
    - 一切取用要看“气有衰旺”，不可千篇一律。

- 分字分词释义：
  - 配气候：在判断用神与格局时，把季节寒暖燥湿的实际状态纳入考量。
  - 事半功倍：得时得势，付出较少而收获较大。
  - 冬木逢水：冬季木气已衰，再逢寒水，更难得生。
  - 金寒而水益冻：金气太寒，水被冻住，失去流动与生木之能。
  - 冻水不能生木：水虽为木之源，但在过寒之境中，无法发挥生机。
  - 调候：调整寒热燥湿，使气候适中，五行协调。
  - 火济水，水济火：火与水彼此调剂，使不过热、不过寒。
  - 木火通明：木得火照，既有生机又有光明，象征明达之气。
  - 金水相涵：金遇水而有润泽之象，刚柔相济。
  - 夺食：正印克制食神，使其不能发挥泄秀之用。
  - 引伸触类，神而明之：由少数例子类推到更多情形，凭理性推演，又在反复体悟中加深理解。

- **规范化释义（primary_lang_explained）**：
  这一章强调：用神与格局虽然是以月令为主来确定的，但**不能脱离季节气候来使用**。若只看格局美不美，而不看寒暖燥湿，往往会造成严重偏差。

  首先，作者用“英雄豪杰”的比喻说明：一个人纵然有非凡才能，如果生逢其时，时势相助，就能事半功倍；反之，纵有奇材，在不合时宜的环境中，成功也会非常艰难。命局中的用神与气候关系，正与此类似。

  接着举了几组对比：
  - **印绶遇官、冬木逢水**：
    - 一般来说，印绶格若遇官星，是“官印双全”的高贵格局；
    - 但若日主为木，生于严冬，又再逢水，虽有官星透出，金寒水冻，水已难以生木，此时再谈“官印双全”，便不如先考虑如何调候。
  - **身印两旺透食、冬木逢火**：
    - 身印两旺而透出食神，本为印格中的佳局；
    - 若此局用在冬木，尤为秀气，因为冬木最需要火来暖身、调候：火一方面泄身，另一方面改善寒冷环境，使印格得势而不偏。
  - **伤官见官、金水为秀**：
    - 按一般理论，“伤官见官，为祸百端”；
    - 然而在金水局中，金寒水冷，以调候为急，适度的官伤互动，反能化寒凉为秀气。
  - **伤官带煞、伤官佩印、伤官用财**：
    - 这些结构在不同气候下有不同表现：
      - 用于冬金，伤官带煞能扭转过寒之气，其秀百倍；
      - 用于夏木，伤官佩印能使火济水、水济火，格局尤为清秀；
      - 伤官用财本为贵格，但若用在冬水，水已冻结，即使有财，也难以生木；
      - 同为伤官用财，用在夏木虽仍可贵，但土燥不灵，秀气不及适候之局。

  最后，作者用“春木逢火、秋金遇水”的对比总结：
  - 春木逢火，木火通明，是极佳的调候与成格；
  - 秋金遇水，金水相涵，也是刚柔相济之象；
  - 然而夏木、冬金却不能简单套用同样公式，必须按气有衰旺、时有寒热来区别取用。
  并具体举出庚生申月、支成水局、干透丁为官、只要壬癸不透干头便为贵格的例子，说明“食神伤官喜见官”在调候法下与本章完全相通。

- **完整对等诠释（secondary_lang_full）**：  
  In practical fate reading we certainly begin from the Month branch and its Useful God, but we must always measure that choice against the seasonal climate. Heroes and capable people who are ‘born at the right time’ find that effort goes twice as far for the same result; those whose talents run against the season struggle no matter how gifted they are. Officer joined with Resource is a fine pattern, yet for winter Wood more Water, even in the form of Officer, only deepens the cold Metal–Water combination so that the roots of Wood freeze and cannot grow. In such charts the true medicine is Fire: it vents the strong body, warms the environment and allows the promised pattern to show itself.

  By the same token, a configuration that theory treats as dangerous—such as Hurting Officer meeting Officer—may become acceptable or even elegant when it plays the role of climate adjustment. In some Metal–Water charts, Hurting Officer or Food appearing together with Officer provides movement and warmth where the structure would otherwise be too cold and stagnant, so the mind and talent shine instead of merely attacking rank. The original author notes that there are many cases of this kind and cannot list them all. Students are asked instead to extend from a few clear examples, always asking: given this particular season, which element is genuinely acting as medicine, and which is simply adding to an excess? Only by cross‑referencing the Useful God with climate can we judge whether the pattern’s promised nobility will actually be realised.

- 详细解说：
  - 这一章把“用神”提升到“时空—气候”维度来考察：
    - 同一格局，在不同气候、节令下，其吉凶程度可能截然不同；
    - 调候本身就是一种“更高层次的用神”，决定了局中五行是否真正适用。
  - 许多被写成“死格”的公式（如伤官见官、印绶遇官等），在调候问题上往往需要重新理解：
    - 有些格局在寒凉中需要“违常用法”来救寒；
    - 有些格局在燥热中需要“逆向取用”来润燥。
  - “引伸触类，神而明之”其实是在要求命理学习者：
    - 不仅要记住例句，更要理解例句背后“气候—用神—格局”三者之间的关系；
    - 由少数范例推知更多可能，在实务中灵活运用，而非机械搬用。

- 核心要点：
  - 用神判断必须同时回答三件事：
    1) 用什么？（用神本身）
    2) 怎么用？（生克制化的结构）
    3) 在什么气候下用？（时令寒暖、湿燥如何？）
  - 调候不当，再好的格局也会失色；调候得宜，很多看似危险的配置反而可以化为秀气。
  - 春木宜火、秋金宜水，冬木宜火、夏木宜水等，都是“用神配气候”的典型经验公式，但任何公式都必须回到具体命局中检验。

- 应用推演：
  1) 先以月令确定用神与格局大纲；
  2) 再检查节令与气候：是寒、是热、是燥、是湿？
  3) 判断当前用神是否顺应气候，或为调候提供帮助；
  4) 对于伤官见官、印绶遇官、伤官用财等典型格局，重新按“调候优先”的思路评估其吉凶；
  5) 在岁运推断中，特别关注能否补足或破坏原局调候的运：
     - 寒局行火、燥局行水，多半有助于成格；
     - 火局再行火、水局再行水，则需谨慎观察是否过犹不及。

- 反例与边界：
  - 只按格名断凶吉，不看季节与气候，导致“冬木逢水仍硬说贵格”等误判；
  - 把调候当作万能理由，无论何局都以“气候”之名强行翻盘，使命理失去可验证性；
  - 忽略“轻重”的问题：即使在合适气候下，五行有无根、有无量，仍需一并考察。

- 小例（示意）：
  - 一命印格，用神在印，身印两旺透食，行运再见微火，冬木得暖，终身多以学问立身，为“用神与气候同心”的例子；
  - 另一命伤官用财，本为贵格，却生于严冬，水寒木冻，又行水运，虽有财星，终多劳而寡功，是“格好而调候不佳”的写照。

- 校勘与字词辨析：
  - 原文“变幼无穷”等处部分本作“变化无穷”“变幻无穷”，本章仍从底本行文，仅在此统一说明调候思想与全书其他章节之呼应；
  - “火济水，水济火”“木火通明”“金水相涵”等语，与《滴天髓》《三命通会》中多处用法互见，可互相参看以加深理解.

---

## 十五．论相神紧要




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_303]` `[trigger: 配气候]` `[factor_trigger: tiaohou_weiji AND hannuan_zaoshi_dangxian_lun]` `[role: 主干]` 调候为急，寒暖燥湿当先论。 → 《子平真诠》#上卷
  - `[ns_zpzy_304]` `[trigger: 偏枯之格]` `[factor_trigger: pianku_zhige AND xu_xingyun_bu_zhi]` `[role: 主干]` 偏枯之格，须行运补之。 → 《子平真诠》#上卷
  - `[ns_zpzy_305]` `[trigger: 喜神来助]` `[factor_trigger: xishen_laizhu=true AND result=shishi_shunsui]` `[role: 条件分支]` 喜神来助，事事顺遂。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "用神与气候的相互成就"
    factor_refs: list = ['xiangshen', 'yongshen', 'heshang_cunguan', 'hesha_cuncai', 'xiangshen_shanghai', 'engine_id', 'xiangshen_juese', 'bazi_rule_engine', 'xiangshen_wanhao', 'bazi_rule_engine', 'yongxiang_zhenyingdu', 'bazi_rule_engine', 'xiangshen_mingan', 'bazi_rule_engine', 'shangxiang_yandu', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_124', 'xiangshen_juese', 'rel_zpzq_125', 'xiangshen_wanhao', 'rel_zpzq_126', 'xiangshen_mingan', 'evi_zpzq_113', 'xiangshen_juese', 'rule_xiangshen_shibie', 'evi_zpzq_114', 'shangxiang_yandu', 'rule_shangxiang_cengji', 'concept_auxiliary', 'concept_pivot', 'concept_vulnerability']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_用神与气候的相互成就_001_L1",
    )
    version: str = "1.0.0"
