"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699427
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
    semantic_id="zw_v1.0.0_郭恪之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 郭恪之命(SemanticEntry):
    """
    - 分字分词释义：

  - **廉贞七杀午申宫**：廉贞与七杀同在午宫或申宫，主流荡天涯。
  - **左右昌曲**：左辅右彼与文昌文曲同见，主文才与交际手腕兼具。
  - **贪狼化忌守命**：贪...
    """
    
    original_text: str = """- 分字分词释义：

  - **廉贞七杀午申宫**：廉贞与七杀同在午宫或申宫，主流荡天涯。
  - **左右昌曲**：左辅右彼与文昌文曲同见，主文才与交际手腕兼具。
  - **贪狼化忌守命**：贪狼星化忌坐守命宫，令求财与欲望转为不安与失衡。
  - **太岁沉马**：太岁与驿马星形成沉滞格局，主远行受阻或旅途生变。
  - **丧门白虎合命**：丧门与白虎两丧吊凶星同会命宫，主血光、意外伤灾。
  - **小限冲命**：小限所在宫位与命宫形成对冲，激活凶象。
  - **阴男水二局**：郭恪命盘的五行局数，水二局主智慧流动。

- **原文（source_text）**：  
  郭恪之命。阴男水二局。廉贞七杀午申宫，主人流荡天涯，左右昌曲，虽无加会拱照，只嫌命垣贪狼化忌，因为商贾在外，太岁沉马，五十四岁，小限在子冲之，丧门、白虎合命，故凶。

- **规范化释义（primary_lang_explained）**：  
  郭恪为阴男水二局，命局以廉贞、七杀在午申宫为核心，带有强烈的流动性与风险色彩，原文直言「主人流荡天涯」，多主在外奔波、远离乡土。左右、昌曲同见，说明命主并非粗鄙之才，而是具备一定文才与交际手腕，适合在商旅往来之中经营人脉与利益。但命垣贪狼化忌，贪狼本主欲望与求财，化忌之后，贪欲易偏向投机与不安分，使「商贾在外」这一选择同时蕴含巨大的风险。  
  寿命应期上，原文点出「太岁沉马」与五十四岁小限在子冲命，又见丧门、白虎合命，形成「流动中遇凶关」的组合：奔忙于四方之时，遇到太岁、马星、丧门、白虎等多重凶象叠加，往往应于旅途之灾或远方横祸，最终使命主折于五十四岁左右，成为「游历多、商贾身，却难以终寿」的命例。

- **完整对等诠释（secondary_lang_full）**：  
  Guo Ke’s chart belongs to a Yin Water native whose core pattern is formed by Lian Zhen and Qi Sha in the Wu‑Shen sector. This combination imparts restlessness, risk and a tendency to roam, summed up by the phrase "wandering to the ends of the earth." The presence of assistants and literary stars suggests that he is not a rough drifter but a capable, articulate figure who can trade, negotiate and weave networks on the road. The problem lies in Tan Lang in the Life palace transforming to Ji: the star of desire and acquisition, when turned taboo, pushes the native toward more speculative and unstable ventures, especially in commerce abroad.  
  In terms of lifespan, the text highlights a cluster of malefic timings: the Annual Tai Sui aligns with the Galloping Horse, and around the age of fifty‑four the minor period in the Zi branch clashes with the Life palace while Mourning Gate and White Tiger converge. This describes a man whose life is spent travelling and trading, but whose end is likely to come through misfortune on the road or far from home, when mobile circumstances and heavy malefics coincide. The case stands as a warning that a chart designed for movement and commerce must still respect the hard limits set by dangerous years.

- **核心要点**：  
  1. 廉贞七杀在午申宫，配合水二局，主一生多在外奔波、流荡天涯。  
  2. 左右、昌曲同见，使命主具备文才与人脉经营能力，适合行商与外务。  
  3. 贪狼化忌守命，使求财心态偏向贪急与冒险，易在商旅中累积结构性风险。  
  4. 五十四岁前后太岁沉马、小限冲命并会丧门、白虎，构成远行途中致命凶关。

- **叙事素材（narrative_snippets）**：
  - **流荡天涯**："廉贞七杀午申宫，主人流荡天涯"，郭恪命主一生奔波在外，多为商旅与外务奔走。
  - **商贾在外**："因为商贾在外"，说明其求财路径多在远行经商、人情往来之中。
  - **远行凶年**："太岁沉马，五十四岁，小限在子冲之，丧门、白虎合命，故凶"，沉马加丧白冲命，典型远方横祸之年。
  - **现代应用**：长期出差或驻外的从业者，在马星、丧门、白虎等多重凶星组合的年份，应降低旅次与高风险路线，增加保险与安全预案。"""
    normalized_text_zh: str = """"""
    subject: str = "郭恪之命"
    factor_refs: list = ['pattern_lianzhen_qisha', 'malefic_tanlang_huaji', 'pattern_zuoyou_changqu', 'timing_taisui_chenma', 'malefic_sangmen_baihu', 'timing_xiaoxian_chongming']
    
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
        l1_anchor="zw_v1.0.0_郭恪之命_001_L1",
    )
    version: str = "1.0.0"
