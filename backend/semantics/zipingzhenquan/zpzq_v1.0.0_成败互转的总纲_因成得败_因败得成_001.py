"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.524013
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
    semantic_id="zpzq_v1.0.0_成败互转的总纲_因成得败_因败得成_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 成败互转的总纲因成得败因败得成(SemanticEntry):
    """
    - **原文（source_text）**：
  八字之中，变化不一，遂分成败；而成败之中，又变化不测，遂有因成得败，因败得成之奇。

  是故化伤为财，格之成也，然辛生亥月，透丁为用，卯未会财，乃以...
    """
    
    original_text: str = """- **原文（source_text）**：
  八字之中，变化不一，遂分成败；而成败之中，又变化不测，遂有因成得败，因败得成之奇。

  是故化伤为财，格之成也，然辛生亥月，透丁为用，卯未会财，乃以党煞，因成得败矣。印用七煞，格之成也，然癸生申月，秋金重重，略带财以损太过，逢煞，则煞印忌财，因成得败也。如此之类，不可胜数，皆因成得败之例也。

  官印逢伤，格之败也，然辛生戊戌月，年丙时壬，壬不能越戊克丙，而反能泄身为秀，是因败得成矣。煞刃逢食，格之败也，然庚生酉月，年丙月丁，时上逢壬，则食神合官留煞，而官煞不杂，煞刃局清，是因败得成矣。如此之类，亦不可胜数，皆因败得成之例也。

  其间奇奇怪怪，变幼无穷，惟以理权衡之，随在观理，因时运化，由他奇奇怪怪，自有一种至当不易之论。观命者，毋眩而无主，执而不化也。

- 原注（原文注解）：
  　　本段在“用神变化、纯杂、格局高低”的基础上，再进一步说明成败之间并非一条直线，而是可以互相转化：
  - 其一，**因成得败**：原本成格之处，若用之过度或配置失衡，反而从成中引出败象；
  - 其二，**因败得成**：原本为败格或破格之处，若恰逢生克得宜或岁运相扶，反能从败中转出成局。
  作者以四个例子说明：
  - 化伤为财本为成格，辛亥透丁、卯未会财，却偏党煞，以致从成而败；
  - 印用七煞本为成格，癸申秋金重重，又带财以损印，煞印俱忌财，亦从成而败；
  - 官印逢伤本属败象，但辛戊戌年丙时壬，壬不越戊克丙，反泄身成秀，从败而成；
  - 煞刃逢食本为败局，庚酉年丙月丁时逢壬，食神合官而留煞，使煞刃局清，也是从败而成。
  最后以“奇奇怪怪，变幼无穷”作结，提醒学者：
  - 成败互转之机，变幻不穷，不能拘泥格名；
  - 惟有随时以“理”权衡，并结合时运变化，方能在诸多奇变中守住一个“至当不易”的判断标准。

- 分字分词释义：
  - 因成得败：由成格条件本身引出后续败象，所谓“好事用过头”。
  - 因败得成：由败格条件中另生转机，反而成其贵用。
  - 化伤为财：伤官本为泄秀、克官，化财则转为生财之用。
  - 党煞：与七煞同党、同气，而非用于制煞或通关，反倾向于助煞为虐。
  - 印用七煞：以煞生印之格，本可成贵，但须配合身印强弱与财星多少。
  - 略带财以损太过：财轻而来克印或扶煞，反使印格失平衡。
  - 官印逢伤：正官与印被伤官所克，本属破格之象。
  - 煞刃逢食：七煞、阳刃再见食神，本属纷乱。但庚日生酉月，年丙月丁，时上又逢壬水时，壬水食神与官星相合，以合官之方式留煞，使官煞分途、煞刃局反而清纯，这样便从败局中翻转成可用之贵格。

  这些例子说明：
  - 格局不是一成不变的标签，而是一套“在变化中看整体”的系统；
  - 很多看似成格的地方，如果搭配不当，可能潜藏“因成得败”的隐患；
  - 很多看似败格的地方，只要再加一笔制化，便可能出现“因败得成”的奇妙转机。

  末段“奇奇怪怪，变幼无穷”提醒我们：
  - 成败之间的微妙变化，不可能全部列举，只能靠“以理权衡”，随时在具体命局与具体时运中观察；
- **规范化释义（primary_lang_explained）**：
  八字之中变化多端，因此有成格与败格之分；而在成败之间，又有更微妙的变化，于是出现"因成得败、因败得成"的奇妙情形。所谓"因成得败"：化伤为财本是成格，但辛日生亥月透丁为用，卯未会财却偏偏助煞，于是从成而败；印用七煞本是成格，但癸日生申月秋金重重，稍带财星以损太过之印，逢煞时煞印皆忌财，也是从成而败。这类例子不胜枚举。所谓"因败得成"：官印逢伤本是败象，但辛日生戊戌月、年丙时壬，壬水不能越戊克丙，反而泄身为秀，从败而成；煞刃逢食本是败局，但庚日生酉月、年丙月丁、时上逢壬，食神合官而留煞，使煞刃局清，也是从败而成。这类例子同样不胜枚举。其间奇奇怪怪、变化无穷，唯有以"理"来权衡，随时观察道理、因时因运而化。不论多么奇怪的变化，终有一个"至当不易"的标准。观命者切勿被表象迷惑而无主见，也不可执着一端而不知变通。

- **完整对等诠释（secondary_lang_full）**：  
  Building on the earlier discussion of change, this passage shows how apparent success can contain the seeds of later failure, and how apparent failure can sometimes be turned to advantage. “Success breeding failure” refers to patterns that are theoretically well‑founded but are later pushed beyond their proper limits. A chart that turns Hurting Officer into Wealth, or that uses Seven Killings through Resource, may start as a fine structure; yet if subsequent stems and branches pile on extra Wealth in support of Killing, or introduce more Metal into an already heavy Killing–Resource combination, the very factors that once brought distinction now become the instruments of harm. What began as a noble pattern is slowly bent out of shape.

  “Failure breeding success” describes the opposite movement. Some charts that would ordinarily be dismissed—Officer and Resource apparently ruined by Hurting Officer, or a harsh Killing‑Blade configuration—can be rescued when a new star redirects the flow. Hurting Officer may shift from attacking Officer to simply leaking excess qi and turning into refined talent, or Food God may combine with Officer so that Killing is contained in the background and the structure becomes clear. In such cases a would‑be failure is transformed into something workable, even distinguished.
  Between these extremes lie countless curious and subtle variations. The author therefore recommends a single standard: always weigh things by principle and by timing. We must look for the hidden lines of defeat within successful patterns and the hidden lines of use within flawed ones, and then ask how time and luck will activate one or the other. Static labels of “good pattern” or “bad pattern” are never enough; the real art lies in seeing how success and failure can turn into one another under changing conditions.

  - 成格不必自满，败格不必绝望；关键在于能否抓住合适的通关与制化点；
  - 观命者若仅凭几条格名就下结论，容易“眩而无主”；若又死守一格、不肯因时因运而变，则是“执而不化”。真正的“至当不易之论”，恰恰是在万变之中守住一个不偏不倚的理。

- 详细解说：
  - “因成得败、因败得成”不是玄虚，而是提醒我们：
    - 成格必有其限度：一旦过度或搭配失衡，就会走向反面；
    - 败格亦有其可用之处：若能以适当生克通关，则可化败为成。
  - 命局之贵与否，不能只看静态格名，而要看：
    - 成中有没有败的隐线；
    - 败中有没有成的活路；
    - 岁运来时，是触发隐线，还是开启活路。
  - “以理权衡、因时运化”是本段的关键词：一切成败判断皆当依理、依时，不可凭好恶与成见。

- 核心要点：
  - 三重审视：
    1) 先看静态格局之成败；
    2) 再看成中之败、败中之成；
    3) 最后看岁运何时触发哪一条线。
  - 对“成格”的局，要预判其可能“因成得败”的节点（如财过度扶煞、伤过度泄身等）。
  - 对“败格”的局，要寻找潜在“因败得成”的着力点（如合去一字、通关一气、调候一行等）。
  - 不可把例子当作死法套用，而应回到具体命局、具体时运上，用“成败互转”的思路来检验。

- 应用推演：
  1) 以前文方法先定格局与用神，并判断初步成败；
  2) 检视局中有无“化伤为财而党煞”“印用七煞而忌财”等结构，标记为“因成得败风险点”；
  3) 检视局中有无“官印逢伤而伤转为泄秀”“煞刃逢食而食合官留煞”等结构，标记为“因败得成机会点”；
  4) 将岁运纳入：观察岁运是加强风险点，还是强化机会点；
  5) 在实际断命与用命（择业、行事、择日）时，帮助当事人避开“因成得败”的极端用法，尽量走向“因败得成”的化解路径。

- 反例与边界：
  - 见“化伤为财”便认定一生富贵，不看是否党煞或财印失衡；
  - 见“官印逢伤”“煞刃逢食”便一概断为大凶，不看是否有机会转为泄秀或局清；
  - 把成败互转理解为“凡事皆可圆说”，以之掩盖推理不足，而非基于具体生克结构；
  - 反向误区是，为了追求“奇奇怪怪之妙”，反而抛弃基本用神与格局法则，导致断命缺乏可验证的依据。

- 小例（示意）：
  - 一命原为伤官生财格，岁运再见财煞同来，若不警惕“因成得败”，则易因过度逐利而惹祸；若能适度收敛、以印护身，反可保持原有成格之美；
  - 另一命本属煞刃逢食之局，青少年运多挫折，但中年行印运，恰能化食为泄秀、以印护煞，从“败格”中走出较高的成就路径，正是“因败得成”的写照。

- 校勘与字词辨析：
  - 原文“变幼无穷”，多种刻本作“变化无穷”或“变幻无穷”，今仍从此本，理解为“变化无穷”，在此提示异文；
  - “自有一种至当不易不论”，今据语意当作“自有一种至当不易之论”，意指在诸多变化中，终有一条合乎道理而不易动摇的判断标准。

---

## 十四．论用神配气候得失




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_300]` `[trigger: 因成得败]` `[factor_trigger: (yincheng_debai OR yinbai_decheng) AND yunlu_fenqi]` `[role: 主干]` 因成得败因败得成，运路分歧。 → 《子平真诠》#上卷
  - `[ns_zpzy_301]` `[trigger: 中和为贵]` `[factor_trigger: zhonghe_zhi_ming AND fushou_shuangquan]` `[role: 主干]` 中和之命，福寿双全。 → 《子平真诠》#上卷
  - `[ns_zpzy_302]` `[trigger: 相神得用]` `[factor_trigger: xiangshen_deyong=true AND fuge_yougong]` `[role: 条件分支]` 相神得用，辅格有功。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "成败互转的总纲：因成得败，因败得成"
    factor_refs: list = ['pei_qihou', 'tiaohou', 'muhuotongming', 'jinshuixianghan', 'qi_shuaiwang', 'engine_id', 'qihou_pipei', 'bazi_rule_engine', 'tiaohou_youxianji', 'bazi_rule_engine', 'qihou_zuoyong', 'bazi_rule_engine', 'qihou_mingan', 'bazi_rule_engine', 'tiaohou_bianjie', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_121', 'qihou_pipei', 'rel_zpzq_122', 'tiaohou_youxianji', 'rel_zpzq_123', 'qihou_mingan', 'evi_zpzq_111', 'qihou_pipei', 'rule_dongmu_fengsui', 'evi_zpzq_112', 'tiaohou_youxianji', 'rule_jinshui_shangguan', 'concept_timing', 'concept_adjustment', 'concept_seasonal']
    
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
        l1_anchor="zpzq_v1.0.0_成败互转的总纲_因成得败_因败得成_001_L1",
    )
    version: str = "1.0.0"
