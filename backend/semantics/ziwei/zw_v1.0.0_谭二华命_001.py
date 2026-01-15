"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699822
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
    semantic_id="zw_v1.0.0_谭二华命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 谭二华命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫府朝垣**：紫微、天府朝向官垣，主最高等尊贵。
  - **文曲武曲会合**：文曲与武曲同会于命局，主文武兼备。
  - **禄权加会**：禄星与权星同时加会命局，...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫府朝垣**：紫微、天府朝向官垣，主最高等尊贵。
  - **文曲武曲会合**：文曲与武曲同会于命局，主文武兼备。
  - **禄权加会**：禄星与权星同时加会命局，主财禄与权位。
  - **三台八座**：佐辅类吉星群拱照命局，主荣宠与根基稳固。
  - **廉贞处生合之为贵**：廉贞在适当生旺格局下转刑为贵。
  - **太岁返人乡**：太岁行至与命局相应的归位方位，象征自然收尾。
  - **阳男土五局**：谭二华命盘的五行局数，土五局主厚重极贵。

- **原文（source_text）**：  
  谭二华命。阳男土五局。此为紫府朝垣，文曲、武曲会合，禄权加会，三台八座，吉星俱拱昭宜为大贵之命。且廉贞守命垣，处生合之为贵，终身福厚，位登二品。后因太岁返人乡，故寿终。

- **规范化释义（primary_lang_explained）**：  
  谭二华命为阳男土五局，「紫府朝垣」配合文曲、武曲会合，禄星与权星同时加会，且得三台八座诸吉星拱照，是极高等级的「紫府文武禄权」组合，一生主大贵之命。廉贞守命垣而「处生合之为贵」，说明在适当的生年格局下，廉贞由刑杀之星转为贵气与节操，强化其清介而有权柄的形象。  
  原文言其「终身福厚，位登二品」，说明不仅仕途高显，且享有稳定福泽。末句「后因太岁返人乡，故寿终」，多被理解为行至适当太岁方位，寿元自然告成，是相对平顺、近乎「告老还乡」式的寿终，而非突发凶亡。

- **完整对等诠释（secondary_lang_full）**：  
  Tan Erhua’s chart is that of a Yang Earth native in the Fifth Configuration. Zi Wei and Tian Fu face the court while Wen Qu and Wu Qu combine; Lu and Quan join, and San Tai with Ba Zuo all shine upon the configuration. This "Zifu with literary‑martial and Lu‑Quan plus court stars" pattern is one of high rank and favour. Lian Zhen guards the Life but, "in its proper life‑giving setting," turns from pure punishment into nobility and integrity, reinforcing a profile of upright authority.  
  The text says he "enjoys rich blessings throughout life" and "attains second‑rank office," emphasising both status and sustained fortune. The phrase "when Tai Sui returns to his homeland, his life ends" suggests a natural closure when the Annual Tai Sui reaches a fitting sector, akin to retiring and returning home. Death here is portrayed not as catastrophe but as a timely completion of an illustrious career.

- **核心要点**：  
  1. 紫府朝垣配文武曲、禄权与三台八座，是权势与文武兼备的极贵格。  
  2. 廉贞守命垣且「处生合之为贵」，将刑杀能量转化为节操与威望。  
  3. 终身福厚位登二品，于太岁「返人乡」时自然寿终，整体路径平顺而圆满。"""
    normalized_text_zh: str = """"""
    subject: str = "谭二华命"
    factor_refs: list = ['pattern_zifu_chaoyuan', 'pattern_wenqu_wuqu_huihe', 'pattern_luquan_jiahui', 'star_santai_bazuo', 'star_lianzhen_chusheng', 'timing_taisui_fanrenxiang']
    
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
        book_id="ziwei",
        chapter="",
        l1_anchor="zw_v1.0.0_谭二华命_001_L1",
    )
    version: str = "1.0.0"
