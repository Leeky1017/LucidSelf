"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523745
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
    semantic_id="zpzq_v1.0.0_又如甲逢庚为煞_与乙作合_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 又如甲逢庚为煞与乙作合(SemanticEntry):
    """
    - **原文（source_text）**：
  又如甲逢庚为煞，与乙作合，而煞不攻身；甲逢乙为劫财，甲逢丁为伤，与壬作合，而丁不为伤官；甲逢壬为枭，与丁作合，而壬不夺食。此四忌神因合化吉者也。

-...
    """
    
    original_text: str = """- **原文（source_text）**：
  又如甲逢庚为煞，与乙作合，而煞不攻身；甲逢乙为劫财，甲逢丁为伤，与壬作合，而丁不为伤官；甲逢壬为枭，与丁作合，而壬不夺食。此四忌神因合化吉者也。

- 原注（原文注解）：
  　　本段举例说明“忌神因合而转吉”的几种典型情况：
  - 庚为甲之煞，与乙合，则煞力偏向乙，不直接攻身；
  - 乙为甲之劫财，丁为伤官，与壬合，则伤不伤官、枭不夺食；
  - 四类本为忌神，因合化而减弱甚至转化其凶性。

- 分字分词释义：
  - 甲逢庚为煞：甲木遇庚金，为七煞。
  - 与乙作合：庚与乙合金，庚之力量部分转向乙木。
  - 煞不攻身：七煞之力不直接冲击日主甲身。
  - 甲逢乙为劫财：乙木为甲之劫财，同类争财。
  - 甲逢丁为伤：丁火为甲之伤官。
  - 与壬作合，而丁不为伤官：丁壬合木，丁之力量转化为木气，不再单纯作为伤官克官。
  - 甲逢壬为枭：壬水为甲之偏印（枭神）。
  - 与丁作合，而壬不夺食：壬丁合木，枭神不再夺食神之气。

- **规范化释义（primary_lang_explained）**：
  这一段专讲“忌神被合化之后，变得没有那么凶，甚至有转吉的空间”。例如：甲木遇庚金，本来庚是七煞，主刚烈之克；但如果庚又去和乙木相合，形成乙庚合金，那么庚的力量被牵引到“为乙办事”上，反而不再全力攻甲，七煞之害因而大减。再如：乙木对甲是劫财，丁火对甲是伤官，壬水对甲是偏印（枭），这些本都是常见的忌神；但当丁去与壬合化成木时，丁火不再只充当“克官之伤官”，壬水也不再只是“夺食之枭神”，而是共同参与一条新的生化线（化木生火等），原来的凶性大幅缓和。

- **完整对等诠释（secondary_lang_full）**：  
  This paragraph looks at the opposite side of the story: harmful stars that become far less dangerous once their power is redirected by combination. For a Jia Wood Day Master, Geng Metal is Seven Killings and normally represents a harsh, attacking force. If Geng now combines with Yi Wood to form a Metal configuration centred on Yi, a large share of Geng's energy is drawn off to "work for" Yi instead of striking directly at Jia, so the Killing no longer attacks the body. Likewise, Yi is Rob Wealth to Jia, Ding is Hurting Officer, and Ren is the so‑called Owl (a sharp form of Resource that can damage Food God); all three are usually counted among the more difficult stars. When Ding Fire and Ren Water combine to produce a stream of Wood qi, however, Ding is no longer acting primarily as a Hurting Officer against Jia's Officer star, and Ren is no longer seizing the nourishment of Food God. Both have been reassigned into a new generative line.

  In all four examples, stars that would ordinarily be treated as serious afflictions are partly neutralised, or even turned toward constructive use, because their strength is bound into other tasks. This is an important mechanism behind the saying that "meeting what is ominous does not always bring misfortune": a Killing, Hurting Officer or Owl that has truly been drawn off by combination cannot be judged in the same way as one that strikes the Day Master head‑on.

- 详细解说：
  - 忌神并非一出现就必然带来坏结果，还要看它是否被合住、合化，以及合向何方。
  - “煞不攻身、伤不为伤、枭不夺食”这三种情形，都是看合化是否把凶性导向别处，或让其参与新的生化结构。
  - 与前一小节“喜神被合而无用”互成对照：一边是喜神被合走、一边是忌神被合去，这两者在实务判断中的影响截然不同。

- 核心要点：
  - 看忌神时，不只看“有无”，更要看“是否合向他处”。
  - 被合去的忌神，其凶性多有折扣，甚至转为整体结构中的一部分力量。
  - 官煞、伤官、枭印等凶神，只要适当地被合化、制衡，往往能成为格局的重要配角，而非单纯祸端。

- 应用推演：
  1) 标出命局中所有忌神（煞、伤、枭等）。
  2) 检查这些忌神是否参与某种合化（如庚与乙合金、丁与壬合木等）。
  3) 判断合化是否让忌神“转向”，不再直冲日主或关键用神。
  4) 在格局分析中，区别“直击型忌神”和“被合化的忌神”，分别定其轻重。

- 反例与边界：
  - 只因见庚煞，就武断判为“七煞攻身”，不看庚是否与乙、辛等发生合化，易误断凶险程度。
  - 认为“合化必吉”，不分喜忌，也不分合向何处，同样是偏差。

- 小例（示意）：
  - 甲日生酉月，庚辛并透，本为煞重之局；若支中有乙卯与庚合，而辛又受制，则“煞不专攻身”，格局可向清化。

- 校勘与字词辨析：
  - “此四忌神因合化吉者也”：四者分别指煞、劫、伤、枭。本句强调的是“因合而转吉（或减凶）”，并非说一旦合化就完全没有凶性。"""
    normalized_text_zh: str = """"""
    subject: str = "又如甲逢庚为煞，与乙作合"
    factor_refs: list = ['sha_bugongshen', 'jiecai_beihe', 'shangguan_hehua', 'xiao_buduoshi', 'sijishen_hehuaji']
    
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
        l1_anchor="zpzq_v1.0.0_又如甲逢庚为煞_与乙作合_001_L1",
    )
    version: str = "1.0.0"
