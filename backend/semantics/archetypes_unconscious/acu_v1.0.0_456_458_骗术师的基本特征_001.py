"""
Auto-generated semantic module for archetypes_unconscious
Generated at: 2025-12-05T13:30:20.545020
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
    semantic_id="acu_v1.0.0_456_458_骗术师的基本特征_001",
    book_id="archetypes_unconscious",
    engine_id="psych"
)
class 456458骗术师的基本特征(SemanticEntry):
    """
    **原文** (§456-458, 行7124-7162):

> [456] It is no light task for me to write about the figure of the ...
    """
    
    original_text: str = """**原文** (§456-458, 行7124-7162):

> [456] It is no light task for me to write about the figure of the trickster in American Indian mythology within the confined space of a commentary... A curious combination of typical trickster motifs can be found in the alchemical figure of Mercurius; for instance, his fondness for sly jokes and malicious pranks, his powers as a shape-shifter, his dual nature, half animal, half divine, his exposure to all kinds of tortures, and—last but not least—his approximation to the figure of a saviour.
>
> [457] Since all mythical figures correspond to inner psychic experiences and originally sprang from them, it is not surprising to find certain phenomena in the field of parapsychology which remind us of the trickster. These are the phenomena connected with poltergeists...
>
> [458] These mythological features extend even to the highest regions of man's spiritual development. If we consider, for example, the daemonic features exhibited by Yahweh in the Old Testament, we shall find in them not a few reminders of the unpredictable behaviour of the trickster...

**关键术语分析**:

| 术语 | 字面意义 | 象征意义 | 语境用法 |
|------|---------|---------|---------|
| Trickster (骗术师) | 恶作剧者 | 原始阴影 | 北美神话 |
| Mercurius (墨丘利) | 炼金术水银 | 双重性 | 变形者 |
| Poltergeist (骚灵) | 捣蛋鬼 | 无意识表现 | 超心理现象 |
| Shape-shifter | 变形者 | 流动认同 | 原始特征 |

**英文释义（主语言）**:

**骗术师的欧洲类比**：
荣格首次接触Bandelier的《欢乐制造者》时，联想到中世纪教会**狂欢节**——等级秩序的颠倒，至今仍延续于学生社团的狂欢活动。

**墨丘利中的骗术师母题**：
炼金术的**墨丘利形象**中可发现典型骗术师母题的奇特组合：
- 喜欢狡猾的笑话和恶作剧
- **变形能力**
- **双重本性**——半动物、半神圣
- 遭受各种折磨
- **接近救世主形象**

**骚灵现象**：
所有神话形象都对应内在心理体验并源于其中。因此超心理学领域中某些现象让人想起骗术师——与**骚灵**相关的现象，发生于各时各地、围绕**青春期前儿童**。骚灵的恶作剧和其智力的低下、其"通信"的愚蠢都广为人知。

**旧约雅威的骗术师特征**：
骗术师的神话特征甚至延伸到人的精神发展的最高领域。考察旧约中**雅威表现的魔性特征**，会发现不少骗术师不可预测行为的痕迹——无意义的毁灭狂欢、自我强加的痛苦、逐渐发展为救世主及同时的人性化。

**完整中文诠释（次语言）**:

**骗术师的文化平行物**：
荣格首次接触Bandelier的《欢乐制造者》时，联想到中世纪教会狂欢节——等级秩序的颠倒。魔鬼被描述为"上帝的猿猴"(simia dei)，在民间传说中被刻画为被"愚弄"或"欺骗"的"傻瓜"，也有骗术师的矛盾性。

**墨丘利的骗术师特征**：
炼金术的墨丘利形象中可发现典型骗术师母题的奇特组合：喜欢狡猾的笑话和恶作剧、变形能力、双重本性（半动物、半神圣）、遭受各种折磨、接近救世主形象。这些特质使墨丘利看起来像从原始时代复活的魔性存在，比希腊赫尔墨斯更古老。

**骚灵与萨满**：
所有神话形象都对应内在心理体验。超心理学领域中与骚灵相关的现象让人想起骗术师。骗术师的特质也存在于萨满和巫医的性格中——他们经常对人玩恶作剧，却又反过来成为报复的受害者。

**核心要点**:
- 骗术师 = 欧洲狂欢节颠倒秩序的平行物
- 墨丘利 = 典型骗术师母题的组合
- 骗术师特征：恶作剧、变形、双重性、受折磨、近救世主
- 骚灵 = 超心理学中的骗术师平行物
- 萨满/巫医 = 骗术师特质的载体
- 旧约雅威 = 骗术师特征的高级表现

**叙事片段**:
- `[ns_cw9i_VII_456_001]` `[trigger: trickster_features]` `[factor_trigger: jung_trickster AND jung_mercurius]` `[role: 主干]` 骗术师特征：恶作剧、变形、双重性、受折磨、近救世主——墨丘利是典型组合。→ §456
- `[ns_cw9i_VII_457_001]` `[trigger: poltergeist]` `[factor_trigger: jung_trickster AND jung_parapsychology]` `[role: 主干依赖]` 骚灵=超心理学中的骗术师平行物——围绕青春期前儿童的恶作剧和低智力通信。→ §457
- `[ns_cw9i_VII_458_001]` `[trigger: yahweh_trickster]` `[factor_trigger: jung_trickster AND jung_yahweh]` `[role: 主干依赖]` 旧约雅威展现骗术师特征——不可预测、毁灭狂欢、自我强加痛苦、逐渐人性化。→ §458"""
    normalized_text_zh: str = """"""
    subject: str = "§456-458 骗术师的基本特征"
    factor_refs: list = ['engine_id', 'trickster', 'psych_semantic', 'malicious_pranks', 'psych_semantic', 'shape_shifting', 'psych_semantic', 'dual_nature', 'psych_semantic', 'mercurius', 'psych_semantic', 'poltergeist', 'psych_semantic']
    
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
        book_id="archetypes_unconscious",
        chapter="",
        l1_anchor="acu_v1.0.0_456_458_骗术师的基本特征_001_L1",
    )
    version: str = "1.0.0"
