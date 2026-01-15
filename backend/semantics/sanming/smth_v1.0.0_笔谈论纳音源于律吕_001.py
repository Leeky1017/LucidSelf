"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228045
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
    semantic_id="smth_v1.0.0_笔谈论纳音源于律吕_001",
    book_id="sanming",
    engine_id="bazi"
)
class 笔谈论纳音源于律吕(SemanticEntry):
    """
    - **原文（source_text）**：
  尝观笔谈论六十甲子纳音，本六十律旋相为宫法也。一律含五音，凡气始于东方而右行，音起于西方而左行，阴阳相错而生变化。所谓气始于东方者，四时始于木，右行传...
    """
    
    original_text: str = """- **原文（source_text）**：
  尝观笔谈论六十甲子纳音，本六十律旋相为宫法也。一律含五音，凡气始于东方而右行，音起于西方而左行，阴阳相错而生变化。所谓气始于东方者，四时始于木，右行传于火，火传于土，土传于金，金传于水。所谓始于西方者，五音始于金，左旋传于火，火传于木，木传于水，水传于土。

- **分字分词释义**：
  - **笔谈**：《梦溪笔谈》，沈括著。
  - **六十律**：六十个音律。
  - **旋相为宫**：旋转相生成为宫音。
  - **一律含五音**：一个律包含五个音。
  - **气始于东方而右行**：气从东方开始向右旋转。
  - **音起于西方而左行**：音从西方开始向左旋转。
  - **阴阳相错**：阴阳交错。
  - **四时始于木**：四季从春木开始。
  - **右行传**：向右传递。
  - **左旋传**：向左传递。

- **规范化释义（primary_lang_explained）**：
  曾观看《笔谈》论述六十甲子纳音，本于六十音律旋转相生成宫音的方法。一个律包含五个音，凡是气从东方开始向右旋转，音从西方开始向左旋转，阴阳交错而产生变化。所谓气从东方开始，是指四季从春木开始，向右传递到火，火传到土，土传到金，金传到水。所谓从西方开始，是指五音从金开始，向左传递到火，火传到木，木传到水，水传到土。

- **完整对等诠释（secondary_lang_full）**：
  I have examined the Bitan (Brush Talks) discussion of Sixty Jiazi Nayin—it is based on the method of sixty pitches rotating and mutually becoming palace tones. One pitch contains five tones; generally qi begins in the East moving rightward, sound arises in the West moving leftward, yin and yang interlace to generate transformations. What is called "qi beginning in the East" means the four seasons begin with Wood, moving right to transmit to Fire, Fire to Earth, Earth to Metal, Metal to Water. What is called "beginning in the West" means the five tones begin with Metal, rotating left to transmit to Fire, Fire to Wood, Wood to Water, Water to Earth.

- **核心要点**：
  - 纳音源于六十律旋相为宫
  - 一律含五音
  - 气始东方右行：木火土金水
  - 音起西方左行：金火木水土
  - 阴阳相错生变化

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_165]` `[trigger: 纳音源于音律]` `[factor_trigger: sixty_pitches AND rotating_palace AND qi_sound_movement]` `[role: 主干]` 纳音本于六十音律旋相为宫之法。气始于东方而右行，音起于西方而左行，阴阳相错而生变化。 → 《三命通会》卷一#《笔谈》论纳音源于音律

- **详细解说**：
  此条引北宋沈括《梦溪笔谈》论纳音的音律基础。纳音本于六十音律旋转相生成宫音的方法，一个律管包含宫商角徵羽五音。关键是气与音的对立运动：气（五行之气）从东方木开始向右（顺时针）运行（木→火→土→金→水，五行相生顺序）；音（五音）从西方金开始向左（逆时针）运行（金→火→木→水→土，不同于五行相生）。气与音一右一左，阴阳交错，产生六十甲子纳音的变化。这揭示了纳音理论的音律学基础，将天文历法、五行哲学与音律学深度融合。

- **校勘与字词辨析（双语）**：
  - **中文**：沈括《梦溪笔谈》为北宋笔记。"旋宫"是古代音乐术语。气的右行是五行相生顺序，音的左行则不同。
  - **English**: Shen Kuo's "Brush Talks" (Mengxi Bitan) was a Northern Song notebook; "rotating palace" is an ancient musical term; qi's rightward movement follows Five Elements generation order, while sound's leftward differs."""
    normalized_text_zh: str = """"""
    subject: str = "笔谈论纳音源于律吕"
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
        l1_anchor="smth_v1.0.0_笔谈论纳音源于律吕_001_L1",
    )
    version: str = "1.0.0"
