"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619850
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
    semantic_id="qtbj_v1.0.0_7__三月甲木_辰月_总论_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 7三月甲木辰月总论(SemanticEntry):
    """
    - **原文（source_text）**：
  三月甲木，木气相竭。先取庚金，次用壬水。庚壬两透，一榜堪图。但要运用相生，风水阴德，方许富贵。
  或见一二庚金，独取壬水。壬透清秀之人，才学必富。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  三月甲木，木气相竭。先取庚金，次用壬水。庚壬两透，一榜堪图。但要运用相生，风水阴德，方许富贵。
  或见一二庚金，独取壬水。壬透清秀之人，才学必富。
  或天干透出二丙，庚藏支下，此钝斧无钢，富贵难求。若有壬癸破火，堪作秀才。

- **分字分词释义**：
  - **木气相竭**：木气逐渐衰竭 / 春末木老 / 辰月特征
  - **先取庚金**：首先取庚金为用 / 修剪成器 / 第一用神
  - **次用壬水**：其次用壬水 / 滋润化杀 / 第二用神
  - **一榜堪图**：可以图谋科甲一榜 / 举人或进士 / 功名可期
  - **运用相生**：大运配合相生 / 行运助格 / 运气配合
  - **风水阴德**：风水和祖上阴德 / 外在条件 / 辅助因素
  - **清秀之人**：清雅秀气的人 / 壬透之象 / 文人气质
  - **钝斧无钢**：斧头变钝没有钢刃 / 火多销金 / 金无力修木
  - **破火**：制服火气 / 水克火 / 救庚之法

- **规范化释义（primary_lang_explained）**：
  三月（辰月）的甲木，木气逐渐衰竭（春深木老）。首先取庚金（修剪），其次用壬水（滋润）。如果庚金和壬水都透出，可以图谋科甲一榜（举人/进士）。但需要大运配合相生，以及风水阴德的辅助，才许诺富贵。
  或者见到一两个庚金，单独取壬水为用。壬水透出，主其人清秀，有才学且必定富有。
  如果天干透出两个丙火，庚金藏在地支下，这叫“钝斧无钢”（火多销金），富贵很难求。如果有壬癸水破除火气，还堪作一个秀才。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 3rd Month (Dragon Month): Wood energy is exhausting. First take Geng Metal, then use Ren Water. If both Geng and Ren are revealed, one can aim for the Roll (official degree). However, it requires Luck Pillars to be generative, along with Feng Shui and Hidden Virtues, to promise wealth and nobility.
  If one or two Geng Metals are seen, take Ren Water exclusively. If Ren is revealed, the person is clear and elegant, possessing talent and certain wealth.
  If two Bing Fires are revealed in the Stems and Geng is hidden in the Branches, this is "Blunt Axe without Steel" (Fire melts Metal). Wealth and nobility are hard to seek. If Ren/Gui Water breaks the Fire, one can still be a Xiucai (licentiate).

- **核心要点**：
  - **首要用神**：庚金（劈甲/制劫）。
  - **次要用神**：壬水（润局/化杀）。
  - **格局**：杀印相生（Geng + Ren）。
  - **忌讳**：火多销金（钝斧无钢）。

- **详细解说**：
  辰月是春末，木气虽有余气但已退，阳气渐盛，土性当权。
  - 此时木老，需金修整。
  - 土燥水渴，需水滋润。
  - 庚壬并透，金生水，水养木，杀印相生，既修剪又滋润，故贵。
  - 若丙火太重，克制庚金，斧头变钝，无法修木，必须用水制火救金。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_103]` `[trigger: 辰月甲木]` `[factor_trigger: month_chen AND tiangan_jia AND tiangan_geng AND tiangan_ren]` `[role: 主干]` 三月甲木，木气相竭，先取庚金，次用壬水。 → 《穷通宝鉴·三春甲木》#3.7
  - `[ns_qttbj_104]` `[trigger: 辰月甲木]` `[factor_trigger: month_chen AND tiangan_jia AND geng_revealed AND ren_revealed]` `[role: 主干依赖]` 庚壬两透，一榜堪图。 → 《穷通宝鉴·三春甲木》#3.7
  - `[ns_qttbj_105]` `[trigger: 辰月甲木]` `[factor_trigger: month_chen AND tiangan_jia AND ren_revealed]` `[role: 条件分支]` 壬透清秀之人，才学必富。 → 《穷通宝鉴·三春甲木》#3.7
  - `[ns_qttbj_106]` `[trigger: 钝斧无钢]` `[factor_trigger: month_chen AND tiangan_jia AND bing_excessive AND geng_hidden]` `[role: 例外处理]` 天干透出二丙，庚藏支下，此钝斧无钢，富贵难求。 → 《穷通宝鉴·三春甲木》#3.7
  - `[ns_qttbj_107]` `[trigger: 钝斧无钢]` `[factor_trigger: month_chen AND tiangan_jia AND bing_excessive AND (tiangan_ren OR tiangan_gui)]` `[role: 总结]` 若有壬癸破火，堪作秀才。 → 《穷通宝鉴·三春甲木》#3.7"""
    normalized_text_zh: str = """"""
    subject: str = "7. 三月甲木（辰月）总论"
    factor_refs: list = ['wood_qi_exhausting', 'blunt_axe_without_steel', 'hidden_virtue']
    
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
        l1_anchor="qtbj_v1.0.0_7__三月甲木_辰月_总论_001_L1",
    )
    version: str = "1.0.0"
