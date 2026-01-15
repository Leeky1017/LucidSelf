"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699686
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
    semantic_id="zw_v1.0.0_项济川命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 项济川命(SemanticEntry):
    """
    - 分字分词释义：

  - **科权禄会合**：科星、权星与禄星同宫或互会，主功名权禄齐至。
  - **昌曲巳酉**：文昌文曲分布于巳酉二宫，主文才得位且稳固。
  - **巨机居卯**：巨门与天...
    """
    
    original_text: str = """- 分字分词释义：

  - **科权禄会合**：科星、权星与禄星同宫或互会，主功名权禄齐至。
  - **昌曲巳酉**：文昌文曲分布于巳酉二宫，主文才得位且稳固。
  - **巨机居卯**：巨门与天机同居卯位，主智谋与口才俱佳。
  - **火忌不辱**：即便逢火忌也不致辱没，反而富贵称羡。
  - **大限天伤**：大限行至天伤之位，主身体与事业遭受打击。
  - **小限败地**：小限落于失势破落之地，主事败与能量流失。
  - **天哭杀临**：太岁逢天哭与杀星同临，主哀伤、丧事与精神打击。
  - **阴男火六局**：项济川命盘的五行局数，火六局主热情多才。

- **原文（source_text）**：  
  项济川命。阴男火六局。科权禄会合，昌曲居于巳酉，且巨机居卯，虽逢火忌，亦不为辱，富贵全羡。大限天伤，小限败地，太岁天哭杀临，主六十一岁而亡。

- **规范化释义（primary_lang_explained）**：  
  项济川命为阴男火六局，科星、权星与禄星会合，文昌、文曲分布于巳酉，再有巨门与天机居卯，为「科权禄会合 + 昌曲得位 + 巨机居卯」的复合文武格。即便命局中有火忌存在，仍不致辱没，反而富贵备受称羡。  
  然而大限行至天伤，小限落于败地，太岁又见天哭杀临，是「天伤 + 败地 + 天哭杀」叠加之运。此组合一方面象征事业基础与身体承受反复打击，另一方面指向悲伤事件或舆论风波，对命主精神与肉体造成沉重压迫，最终在六十一岁死亡。

- **完整对等诠释（secondary_lang_full）**：  
  Xiang Jichuan’s chart is that of a Yin Fire native in the Sixth Configuration. Ke, Quan and Lu meet, Wen Chang and Wen Qu occupy auspicious positions in Si and You, and Ju Men with Tian Ji reside in Mao. This "Ke‑Quan‑Lu with well‑placed Chang‑Qu and Ju‑Ji" pattern blends literary, strategic and administrative talents; even with fire‑type malefics present, the text notes that he "is not disgraced" and that his prosperity is widely envied.  
  Yet the major period eventually reaches Tian Shang, the minor period falls into a "defeated ground," and the Annual Tai Sui brings Tian Ku and killing influences. This triad—Tian Shang, defeat ground, Tian Ku Sha—suggests repeated blows to both career base and physical health, framed by sorrowful or scandal‑coloured events. Under such pressure the native dies around sixty‑one. The case shows a broadly successful chart whose later life is ultimately shortened by cumulative wounding and grief‑laden transits.

- **核心要点**：  
  1. 科权禄会合、昌曲得位、巨机居卯，为文武兼具、令人称羡的富贵格。  
  2. 大限天伤、小限败地、太岁天哭杀临，是事业与身体被反复打击并夹杂悲伤色彩的运势。  
  3. 六十一岁在多重打击下身亡，呈现「富贵而后期被天伤与哀杀拖垮」的轨迹。"""
    normalized_text_zh: str = """"""
    subject: str = "项济川命"
    factor_refs: list = ['pattern_kequanlu_huihe', 'pattern_changqu_siyou', 'pattern_juji_jumao', 'timing_daxian_tianshang', 'timing_xiaoxian_baidi', 'malefic_tianku_shalin']
    
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
        l1_anchor="zw_v1.0.0_项济川命_001_L1",
    )
    version: str = "1.0.0"
