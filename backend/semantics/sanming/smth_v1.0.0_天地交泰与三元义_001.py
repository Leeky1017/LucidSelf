"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228071
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
    semantic_id="smth_v1.0.0_天地交泰与三元义_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天地交泰与三元义(SemanticEntry):
    """
    - **原文（source_text）**：
  自午至于亥为阴，故林钟至于应钟，皆上生。夫上下生者，正谓天气下降，地气上升。易曰天地交泰，义见于此。然所生止三者，亦三元之义。故经曰：三而成天，三而成...
    """
    
    original_text: str = """- **原文（source_text）**：
  自午至于亥为阴，故林钟至于应钟，皆上生。夫上下生者，正谓天气下降，地气上升。易曰天地交泰，义见于此。然所生止三者，亦三元之义。故经曰：三而成天，三而成地，三而成人。易爻之象取三。老子曰：一生二，二生三，三生万物。盖有始有中，有终毕矣。

- **分字分词释义**：
  - **林钟**：律名，六月之律。
  - **应钟**：律名，十月之律。
  - **上生**：音律向上生。
  - **天气下降地气上升**：天地交感。
  - **天地交泰**：天地交合为泰卦。
  - **所生止三**：生成只到三。
  - **三元**：三个元素或阶段。
  - **三而成**：以三来成就。
  - **易爻之象取三**：易卦爻象取三爻。
  - **有始有中有终**：有开始有中间有结束。

- **规范化释义（primary_lang_explained）**：
  从午到亥是阴的范围，所以林钟律到应钟律，都是向上生。所谓上生下生，正是指天气下降地气上升。《易经》说天地交合为泰卦，这个道理在此体现。然而所生只到三，这也是三元的意义。所以经书说：三而成天，三而成地，三而成人。易卦爻象取三爻。老子说：一生二，二生三，三生万物。有开始有中间有结束就完整了。

- **完整对等诠释（secondary_lang_full）**：
  From Wu to Hai is the yin range, thus from Linzhong pitch to Yingzhong pitch, all generate upward. What is called upward-downward generation truly means Heaven's qi descending and Earth's qi ascending. The Yi states "Heaven-Earth Interact as Tai"—the principle is manifest here. Yet generation stops at three, this is also the meaning of Three Origins. Thus the classics state: Three completes Heaven, three completes Earth, three completes Humanity. Yi hexagram lines take three. Laozi said: One generates two, two generates three, three generates myriad things. Having beginning, middle, and end, all is complete.

- **核心要点**：
  - 午至亥为阴，上生为主
  - 上下生体现天地交泰
  - 所生止三：三元之义
  - 三而成天地人
  - 易爻取三，一二三生万物
  - 有始中终即完整

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_168]` `[trigger: 天地交泰与三元]` `[factor_trigger: heaven_earth_tai AND three_origins AND shengzhongzhong]` `[role: 主干]` 上下生者，正谓天气下降，地气上升。易曰天地交泰，义见于此。然所生止三者，亦三元之义。故经曰：三而成天，三而成地，三而成人。 → 《三命通会》卷一#天地交泰与三元义

- **详细解说**：
  此条论纳音上下生的天地交泰原理和三元哲学。子至巳为阳（下生为主），午至亥为阴（上生为主），体现天气下降（阳）地气上升（阴）的交感，正是《易经》泰卦的"天地交泰"之象。纳音生成每次只生三个（孟仲季），体现"三元"哲学：天地人三才、易卦三爻、老子"一生二二生三三生万物"。三代表完整性：有始（孟）、有中（仲）、有终（季）。这将纳音音律理论提升到易理哲学高度，揭示天地人三才合一、生生不息的宇宙观。

- **校勘与字词辨析（双语）**：
  - **中文**：林钟为六月律，应钟为十月律。泰卦上坤下乾，象征天地交合。三元指天元地元人元。
  - **English**: Linzhong is the sixth lunar month pitch, Yingzhong the tenth; Tai hexagram with Kun above Qian below symbolizes Heaven-Earth interaction; Three Origins refer to Heaven, Earth, Human origins."""
    normalized_text_zh: str = """"""
    subject: str = "天地交泰与三元义"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_天地交泰与三元义_001_L1",
    )
    version: str = "1.0.0"
