"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523788
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
    semantic_id="zpzq_v1.0.0_争合妒合与化气真伪_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 争合妒合与化气真伪(SemanticEntry):
    """
    - **原文（source_text）**：
  然又有争合妒合之说，何也？如两辛合丙，两丁合壬之类，一夫不娶二妻，一女不配二夫，所以有争合妒合之说。然到底终有合意，但情不专耳。若以两合一而隔位，则全...
    """
    
    original_text: str = """- **原文（source_text）**：
  然又有争合妒合之说，何也？如两辛合丙，两丁合壬之类，一夫不娶二妻，一女不配二夫，所以有争合妒合之说。然到底终有合意，但情不专耳。若以两合一而隔位，则全无争妒。如庚午、乙酉、甲子、乙亥，两乙合庚，甲日隔之，此高太尉命，仍作合煞留官，无减福也。化气有真有假。上两造为化气之真者，亦有化气有余，而日带根苗劫印者；有日主无根，而化神不足者；更有合化虽真，而闲神来伤化气者，皆为假化。

- 原注（原文注解）：
  　　本段一方面说明“争合妒合”的现象，一方面交代“化气真、化气假”的判断原则：
  - 两干争合同一干，如“两辛合丙”，比喻一夫难娶二妻、一女难配二夫；
  - 若隔位不在同一重心，则无争妒之实；
  - 合化虽符合字面条件，若日主无根、化神不足或被闲神所伤，皆为“假化”。

- 分字分词释义：
  - 争合妒合：多干争相与同一干合，形成“争夺合位”的状态。
  - 一夫不娶二妻，一女不配二夫：比喻合化关系应当专一，不宜过多争夺。
  - 两合一而隔位：两边都来合同一干，但位置不在同一重心上，争夺不成。
  - 化气有真有假：有的合化能真正在格局中发挥作用，有的只是形式上的合，并未真正改气。
  - 化气有余，而日带根苗劫印：合化之神虽真，却被日主的根气与劫印分夺。
  - 日主无根，而化神不足：日主自身无根，又想依靠化神，力量常常不够。
  - 闲神来伤化气：与格局核心无关的“闲杂之神”却来冲破合化，使化气之力无从发挥。

- **规范化释义（primary_lang_explained）**：
  有时候，会出现“争合妒合”的局面：比如两颗辛金同时来合一颗丙火，或两颗丁火同时来合一颗壬水，好比“一夫不娶二妻，一女不配二夫”，大家都想和同一对象结成合局，结果必然“有争有妒”。不过，即便如此，合意终究还是有，只是情不专、力不纯而已。若是“两合一而隔位”，比如庚午、乙酉、甲子、乙亥一局之中，两乙合庚，而甲日在中隔开，这时由于位置上并非都紧贴核心，反倒没有真正的争妒之实，仍可作“合煞留官”看，格局不减其福，这就是高太尉命的例子。

  紧接着，作者提出“化气有真有假”。上面两造（指前例）属于化气较真之例，但也有几种情况会使化气成为“假化”：
  - 一种是化气虽成，日主自己根气很重，还有劫印等帮身之神，导致合化之神“有余无用”；
  - 一种是日主无根，而化神本身力量不足，难以真正支撑格局；
  - 更有一些，是合化条件本来都具备，却被闲神刑冲、破害，让化气无法完成其功。凡此三类，都不宜勉强论作真化格。

- **完整对等诠释（secondary_lang_full）**：  
  Sometimes several stems compete to combine with the same partner, which the author calls "competing" or "jealous" combinations. Two Xin Metals both trying to combine with one Bing Fire, or two Ding Fires both trying to combine with one Ren Water, are likened to one husband who cannot properly marry two wives, or one wife who cannot properly marry two husbands. The desire to combine is there on all sides, but affection and strength are divided, so none of the bonds is fully exclusive. If, however, the contenders stand far apart in the four pillars and are not gathered around the same centre, there may be no real competition in practice. In the well‑known example of the "Grand Marshal Gao" chart, two Yi Woods might be seen as contenders to combine with Geng Metal, yet the positions are such that the combination can still be read as "Killing combined, Officer remaining" without loss of fortune.

  On this basis the text turns to the question of true and false transformation. A configuration may look like a perfect transformation on paper, yet still fail to establish a stable new pattern. Broadly speaking there are three problematic cases: (1) the transformation is strong in itself, but the Day Master has substantial roots and the help of Companions and Resources, so the transformed element is "more than enough" without actually becoming the true centre of the chart; (2) the Day Master has no roots and tries to rely entirely on the transformed element, but that element itself is too weak to carry the load; (3) all formal conditions for transformation are present, yet idle or unrelated stars clash, punish or otherwise damage the configuration so that its qi cannot do its work. In all of these, we should be cautious about declaring a genuine transformation pattern and treat it, at best, as partial or symbolic.

- 详细解说：
  - 合化不但要看“字是否合”，还要看“情是否专”“力是否足”“是否有外力相伤”。
  - 争合妒合的存在，提醒我们在实务中要警惕“过多的合向同一对象”，往往导致力量分散、情义不专。
  - 对化气格的判断尤其要谨慎：若不分真伪，一见合化形似，就论作化格，极易导致断命大偏。

- 核心要点：
  - 合化三问：
    1) 情是否专？（有无争合妒合）
    2) 力是否足？（日主与化神是否皆有根气支撑）
    3) 有无外伤？（闲神是否冲破化局）
  - 化气真，方可据为立格之本；化气假，仅可作参考，不足以独立成格。

- 应用推演：
  1) 看到合化结构时，先排查是否存在争合妒合，或多干争夺同一合位；
  2) 检视日主根气与化神根气，评估合化后新格局是否“有力”；
  3) 检查有无刑冲破害之神，对化局是否造成致命折损；
  4) 根据上述三步，决定此化局是“真化”“半化”还是“假化”，并据此调整断语份量。

- 反例与边界：
  - 见一合局就称“化气格”，不问情专与否、不问根气与否，是最常见误用。
  - 把争合妒合一律视为“大凶”，忽略其中仍存在可用之合意，亦失偏驳。

- 小例（示意）：
  - 命局中辛金两见，天干一丙在中，两辛争合丙，虽有化意，却终难纯粹；若一辛靠近日主、一辛远隔，则应分轻重而不能混为一谈。

- 校勘与字词辨析：
  - "化气有真有假"一句，本精校版将后文"化气有余而日带根苗劫印者""日主无根而化神不足者""闲神来伤化气者"三种情形整理为判断化气真伪的三大类，方便实务使用。

---

## 六．论十干得时不旺失时不弱




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_238]` `[trigger: 子平宗旨]` `[factor_trigger: ziping_zhi_fa AND rizhu_wei_zhu AND yueling_wei_gang]` `[role: 主干]` 子平之法，以日主为主，月令为纲。 → 《子平真诠·序》#宗旨
  - `[ns_zpzy_239]` `[trigger: 月令为纲]` `[factor_trigger: bazi_yongshen AND zhuanqiu_yueling]` `[role: 主干]` 八字用神，专求月令。 → 《子平真诠·序》#月令
  - `[ns_zpzy_240]` `[trigger: 格局为本]` `[factor_trigger: lunming_xian_li_geju AND zai_cha_yongshen_xiji]` `[role: 主干]` 论命先立格局，再察用神喜忌。 → 《子平真诠·序》#格局
  - `[ns_zpzy_241]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_242]` `[trigger: 神煞不论]` `[factor_trigger: shensha_xingchen AND bu_ru_zhenglun]` `[role: 主干]` 神煞星辰，不入正论。 → 《子平真诠》#上卷
  - `[ns_zpzy_243]` `[trigger: 有病无药]` `[factor_trigger: youbing=true AND wuyao=true AND result=zhongshen_buli]` `[role: 主干]` 有病无药，终身不利。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "争合妒合与化气真伪"
    factor_refs: list = ['zhenghe_duhe', 'huaqige', 'zhenhua', 'jiahua', 'xianshen', 'engine_id', 'zhenghe_duhe_flag', 'bazi_rule_engine', 'huashen_genqi', 'bazi_rule_engine', 'xianshen_chongpo', 'bazi_rule_engine', 'hehua_zhenwei', 'bazi_rule_engine', 'huaju_weight', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_058', 'zhenghe_duhe_flag', 'rel_zpzq_059', 'huashen_genqi', 'rel_zpzq_060', 'xianshen_chongpo', 'evi_zpzq_058', 'zhenghe_duhe', 'rule_zhenghe_duhe', 'evi_zpzq_059', 'hehua_zhenwei', 'rule_hehua_zhenwei', 'evi_zpzq_060', 'xianshen_chongpo', 'rule_xianshen_po', 'concept_competing', 'concept_true_false']
    
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
        l1_anchor="zpzq_v1.0.0_争合妒合与化气真伪_001_L1",
    )
    version: str = "1.0.0"
