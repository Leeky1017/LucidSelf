"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699909
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
    semantic_id="zw_v1.0.0_进士之命_阴男金四局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 进士之命阴男金四局(SemanticEntry):
    """
    - 分字分词释义：

  - **科权守照**：科星与权星同守命宫或身宫，主科名与权位。
  - **昌曲暗拱**：文昌文曲虽不显著同宫，却在三方四正暗拱命宫。
  - **天魁坐命**：天魁星坐守命...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权守照**：科星与权星同守命宫或身宫，主科名与权位。
  - **昌曲暗拱**：文昌文曲虽不显著同宫，却在三方四正暗拱命宫。
  - **天魁坐命**：天魁星坐守命宫，主贵人相助。
  - **当为科甲之士**：命局主当成为科甲之士。
  - **限行绝地**：大限行至绝地或不利宫位，行动空间受限。
  - **五十四后方利达**：五十四岁后运势转佳，事业方渐利达。
  - **阴男金四局**：进士命盘的五行局数，金四局主刚断科第。

- **原文（source_text）**：  
  进士之命。阴男金四局。科权守照，昌曲暗拱天魁坐命，当为科甲之士，但中年以上，限行绝地，未得遂志，至五十四后方利达。

- **规范化释义（primary_lang_explained）**：  
  此条进士命为阴男金四局，「科权守照」主科星、权星同拱命宫，「昌曲暗拱天魁坐命」则是文昌、文曲暗中拱照，配合天魁坐命，构成「科权 + 文星 + 贵人」的科甲格局，故曰「当为科甲之士」。  
  然而原文指出「但中年以上，限行绝地，未得遂志」，说明命主在中年以前虽有才名，却因大运行至不利之地（绝地），难以施展抱负；直到五十四岁之后，运势转佳，方能「利达」，即仕途与事业才真正打开。这是典型的「后发型进士」命局：早有才名而晚得其用。

- **完整对等诠释（secondary_lang_full）**：  
  This "Jinshi" chart for a Yin Metal native in the Fourth Configuration features Ke and Quan guarding the Life palace, while Wen Chang and Wen Qu "secretly" flank and Tian Kui sits on Life. The combination of exam, authority, literary talent and noble patron clearly points to someone who attains the degree of Presented Scholar.  
  Yet the text notes that in mid‑life "the periods travel through a wasteland" and his ambitions are not fulfilled. Only after fifty‑four do conditions improve and his career finally gains real traction. This is a pattern of delayed realisation: ability and credentials appear early, but circumstances and timing postpone actual influence and success until later years.

- **核心要点**：  
  1. 科权守照配昌曲暗拱与天魁坐命，是标准进士格局。  
  2. 中年前限行绝地，才名难以转化为实在权位与成就。  
  3. 五十四岁后运势转佳，呈现「后发而终达」的进士命路径。"""
    normalized_text_zh: str = """"""
    subject: str = "进士之命（阴男金四局）"
    factor_refs: list = ['pattern_kequan_shouzhao', 'pattern_changqu_angong', 'star_tiankui_zuoming', 'quality_kejia_zhishi', 'timing_xian_juedi', 'timing_wushisi_lida']
    
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
        l1_anchor="zw_v1.0.0_进士之命_阴男金四局_001_L1",
    )
    version: str = "1.0.0"
