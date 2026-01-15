"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.596975
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
    semantic_id="qtbj_v1.0.0_2__正月戊土_寅月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2正月戊土寅月(SemanticEntry):
    """
    - **原文（source_text）**：
  或一派甲木，无丙者，常人。得一庚透方妙。或支成水局，甲又出干，又有庚透，富贵双全。
  或无庚金，又无比印，难作从杀，定主遭凶，不然，必为盗贼。若日下...
    """
    
    original_text: str = """- **原文（source_text）**：
  或一派甲木，无丙者，常人。得一庚透方妙。或支成水局，甲又出干，又有庚透，富贵双全。
  或无庚金，又无比印，难作从杀，定主遭凶，不然，必为盗贼。若日下坐午，不得善终。
  或一派乙木，为官杀会党，即有庚透，却难制乙，此人内奸外直，口是心非。加一甲在内，无庚，必懒惰自甘，好食无厌。或丙多甲多，宜以癸庚参用。

- **分字分词释义**：
  - **一派甲木**：满盘皆甲木 / 七杀成群 / 杀重
  - **无丙者常人**：没有丙火化杀 / 杀性不化 / 贫贱
  - **支成水局**：地支合成水局 / 财旺 / 生杀
  - **从杀难成**：难以形成从杀格局 / 戊土有根 / 不从
  - **官杀会党**：官杀混杂结党 / 乙木成群 / 势众
  - **内奸外直**：内心奸诈外表正直 / 乙庚合 / 口是心非
  - **好食无厌**：贪食不知满足 / 土木失衡 / 享乐
  - **不得善终**：不能善终 / 凶亡/刑伤 / 杀重攻身

- **规范化释义（primary_lang_explained）**：
  如果一派甲木（七杀），没有丙火（化杀），是常人。得到一个庚金透出（食神制杀）才妙。如果地支合成水局（财），甲木又出干（杀），又有庚金透出（制杀），富贵双全（配合得宜）。
  如果无庚金，又无比肩印绶（身弱杀重），很难作从杀格（因为戊土长生在寅，有根气），定主遭凶灾，否则必为盗贼。如果日支坐午火（阳刃），被水局冲或被杀攻，不得善终。
  如果一派乙木（官星），是官杀会党（官多变杀），即使有庚金透出，也难制住乙木（乙庚合，贪合忘克），这人内奸外直，口是心非。加上一个甲木在内，没有庚金，必定懒惰自甘，好吃无厌。如果丙多甲多，适宜用癸水庚金参考使用。

- **完整对等诠释（secondary_lang_full）**：
  If there is a mass of Jia Wood without Bing, one is ordinary. Obtaining one Geng revealed is wondrous. If branches form a Water Frame, Jia reveals, and Geng reveals, it is complete wealth and nobility.
  If there is no Geng, and no Parallel/Seal, it is hard to Follow Killing (as Wu has root in Yin); it implies disaster or being a thief. If sitting on Wu (Day Branch), one will not have a good end.
  If there is a mass of Yi Wood, it is "Officer/Killing Gathering Party". Even with Geng revealed, it is hard to control Yi (due to combination); this person is treacherous inside but straight outside, mouth affirming but heart denying. Adding Jia without Geng implies laziness and gluttony. If Bing and Jia are abundant, use Gui/Geng.

- **核心要点**：
  - **杀重**：甲多无丙，贫贱。
  - **救应**：喜庚（食神制杀）。
  - **从杀难成**：寅月戊土长生，身不弱，难从杀。强杀攻身，遭凶/盗贼。
  - **官杀混杂/会党**：乙多难制（乙庚合），心术不正。

- **详细解说**：
  - 寅月七杀当令，最怕杀重身轻。
  - 丙火（印）化杀是上策（生身）；庚金（食）制杀是中策（交战）。
  - 若无印无食，杀攻身，非死即盗。
  - 乙庚合在寅月，金绝木旺，庚金被绊，不能制木，故心性“内奸”。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_304]` `[trigger: 甲多无丙]` `[factor_trigger: month_yin AND tiangan_wu AND jia_multiple AND NOT tiangan_bing AND tiangan_geng AND jia_no_bing]` `[role: 条件分支]` 或一派甲木，无丙者，常人。得一庚透方妙。 → 《穷通宝鉴·三春戊土》#21.2
  - `[ns_qttbj_305]` `[trigger: 杀重无制]` `[factor_trigger: month_yin AND tiangan_wu AND jia_multiple AND NOT tiangan_geng AND NOT tiangan_bing AND killing_heavy_no_control]` `[role: 例外处理]` 无庚金又无比印，难作从杀，定主遭凶，不然，必为盗贼。 → 《穷通宝鉴·三春戊土》#21.2
  - `[ns_qttbj_306]` `[trigger: 官杀会党]` `[factor_trigger: month_yin AND tiangan_wu AND yi_multiple AND tiangan_geng AND yi_geng_combine AND treacherous_inside]` `[role: 例外处理]` 一派乙木为官杀会党，即有庚透，却难制乙，此人内奸外直，口是心非。 → 《穷通宝鉴·三春戊土》#21.2"""
    normalized_text_zh: str = """"""
    subject: str = "2. 正月戊土（寅月）"
    factor_refs: list = ['officer_killing_party', 'treacherous_inside', 'bad_end']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_2__正月戊土_寅月_001_L1",
    )
    version: str = "1.0.0"
