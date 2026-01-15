"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699628
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
    semantic_id="zw_v1.0.0_白起之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 白起之命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫破未官为上格**：紫微与破军在未宫成官格，主权势与功名。
  - **左右扶持福不轻**：左辅右彼扶持，福力不轻。
  - **文武双全富贵命**：兼具谋略与武功，...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫破未官为上格**：紫微与破军在未宫成官格，主权势与功名。
  - **左右扶持福不轻**：左辅右彼扶持，福力不轻。
  - **文武双全富贵命**：兼具谋略与武功，富贵荣显。
  - **权禄加会乃为荣**：权星与禄星加会，更增权势荣耀。
  - **羊陀失并命垣**：羊刃与陀罗同并于命宫，主血光与武劫。
  - **太岁白虎三方命合**：太岁带白虎与命宫成三方合局，主血光与动荡集中。
  - **阴男土五局**：白起命盘的五行局数，土五局主厚重大将。

- **原文（source_text）**：  
  白起之命。阴男土五局。紫破未官为上格，左右扶持福不轻，文武双全富贵命，权禄加会乃为荣。七十五岁，羊陀失并命垣太岁、白虎三方命合，是为凶也，故死。

- **规范化释义（primary_lang_explained）**：  
  白起命为阴男土五局，「紫破未官为上格」指紫微与破军在未宫成官格，再得左右扶持，福力不轻，是文武双全、富贵荣显的结构；权星与禄星加会，更增权势荣耀。  
  七十五岁时，羊刃与陀罗失并于命垣，太岁又带白虎与命宫成三方合局，是「羊陀同并 + 太岁白虎三方命合」的极重凶象。此时既象征军事与权力结构中的凶险爆发，也代表血光与动荡集中于命主自身，最终在此年死亡。命例以白起为名，呈现「权禄极盛、文武双全而终结于羊陀白虎重凶」的迟暮轨迹。

- **完整对等诠释（secondary_lang_full）**：  
  Bai Qi’s chart is that of a Yin Earth native in the Fifth Configuration. The phrase "Zi‑Po at Wei in the officer pattern" indicates Zi Wei and Po Jun forming a high‑grade official structure in Wei, with Zuo and You providing support. This yields a chart that is "complete in both civil and martial talents," enriched further when Power and Lu converge. Such a pattern befits a distinguished general‑official whose glory is widely recognised.  
  At seventy‑five, however, Yang Blade and Tuo Luo join at the Life sector, while the Annual Tai Sui carrying Bai Hu forms a triplicity with the Life palace—"Yang and Tuo combining, Tai Sui and White Tiger forming three‑fold contact." This configuration concentrates martial danger, bloodshed and upheaval directly on the native. The case, referencing the famous general Bai Qi, portrays a life of extreme honour and power brought to an end by a convergence of cutting and predatory influences in old age.

- **核心要点**：  
  1. 紫破未官格配左右扶持与权禄加会，是文武双全、权禄极盛的上等格局。  
  2. 七十五岁羊陀失并命垣，太岁白虎三方命合，是血光与权势风暴集中之岁。  
  3. 命例呈现「权禄极盛而终结于羊陀白虎重凶」的高危晚年轨迹。

- **叙事素材（narrative_snippets）**：
  - **紫破未官**："紫破未官为上格，左右扶持福不轻，文武双全富贵命"，白起命主以紫破官格配左右，兼具谋略与武功。
  - **权禄加会**："权禄加会乃为荣"，权星禄星再度加会，使其一生权禄集于一身，战功赫赫。
  - **羊陀白虎**："七十五岁，羊陀失并命垣太岁、白虎三方命合，是为凶也，故死"，羊刃与陀罗同并命垣，太岁白虎三方合命，是高龄仍有血光与刑戮风险的年份。
  - **现代应用**：对现实中仍在一线掌兵权、掌安保或掌强势资源的高龄人物而言，当命盘出现「羊陀 + 白虎」强合命宫之年，应及早规划退居与权力交接，避免在生命后段仍被卷入高危对抗。"""
    normalized_text_zh: str = """"""
    subject: str = "白起之命"
    factor_refs: list = ['pattern_zipo_weiguan', 'pattern_zuoyou_fuchi', 'quality_wenwu_shuangquan', 'pattern_quanlu_jiahui', 'malefic_yangtuo_shibing', 'malefic_baihu_sanfang']
    
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
        l1_anchor="zw_v1.0.0_白起之命_001_L1",
    )
    version: str = "1.0.0"
