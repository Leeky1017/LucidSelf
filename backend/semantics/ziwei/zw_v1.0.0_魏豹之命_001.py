"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699355
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
    semantic_id="zw_v1.0.0_魏豹之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 魏豹之命(SemanticEntry):
    """
    - 分字分词释义：

  - **科禄相逢**：化科化禄与禄存会合，主最高强。
  - **太阳天梁同位**：太阳天梁同宫，主权威显赫。
  - **运限顺行**：限运顺行皆吉，一路顺遂。
  - *...
    """
    
    original_text: str = """- 分字分词释义：

  - **科禄相逢**：化科化禄与禄存会合，主最高强。
  - **太阳天梁同位**：太阳天梁同宫，主权威显赫。
  - **运限顺行**：限运顺行皆吉，一路顺遂。
  - **大限遇陀星**：大限行至逢陀罗，主凶险。
  - **廉贞化忌**：丙年廉贞星化忌，主权力危机。
  - **申人忌铃星**：申年生人逢铃星主凶。
  - **阳男土五局**：魏豹命盘的五行局数，土五局主厚重权谋。

- **原文（source_text）**：  
  魏豹之命。阳男土局五科。禄相逢，遇太阳天梁同位，最高强，运限顺行俱为吉。后因大限遇陀星，小限地网丙年廉贞化忌凶，又兼申人忌铃星，故主难过。却此岁。

- **规范化释义（primary_lang_explained）**：  
  魏豹命属阳男土五局，科禄相逢、太阳天梁同位，最高强，运限顺行为吉。然大限遇陀星，小限地网丙年廉贞化忌，申人忌铃星，故难过此岁而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Wei Bao's Yang male Earth Fifth chart has Academic‑Salary meeting, Sun‑Tianliang same position—most powerful, periods smooth all auspicious. But major meets Tuo; minor at Earth Net in bing year, Lian Zhen transforms taboo; Shen natives taboo Bell. Cannot pass that year.

- **核心要点**：  
  1. 科禄相逢、太阳天梁同位，最高强。  
  2. 大限遇陀星，小限地网廉贞化忌。  
  3. 申人忌铃星，为难过之岁。

- **叙事素材（narrative_snippets）**：
  - **最高强格**："禄相逢，遇太阳天梁同位，最高强，运限顺行俱为吉"，魏豹命主早年凭科禄与太阳天梁之力，高位高权、一路顺行。
  - **化忌凶年**："后因大限遇陀星，小限地网丙年廉贞化忌凶"，大限遇陀、小限地网又逢廉贞化忌，为原局难以承受的重压之年。
  - **申人忌铃**："又兼申人忌铃星，故主难过却此岁"，点明申年生人逢铃星凶年，象征突发风波与官非。
  - **现代应用**：格局再强的领导者，在化忌加陀星、铃星等组合年份，也需主动做"减法"——降低扩张、慎防财务与权力危机，而非盲目凭惯性冲刺。"""
    normalized_text_zh: str = """"""
    subject: str = "魏豹之命"
    factor_refs: list = ['trans_lianzhenhuaji', 'taboo_shenrenlingxing', 'pattern_taiyangtianliangwei', 'source_ref', 'rel_weibao_001', 'pattern_kelutianyangtianliang', 'rel_weibao_002', 'trans_lianzhenhuaji', 'rel_weibao_003', 'taboo_shenrenlingxing', 'evi_weibao_001', 'trans_lianzhenhuaji', 'rule_lianzhen_huaji', 'concept_sun_tianliang', 'concept_lianzhen_taboo']
    
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
        l1_anchor="zw_v1.0.0_魏豹之命_001_L1",
    )
    version: str = "1.0.0"
