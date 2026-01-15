"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228870
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
    semantic_id="smth_v1.0.0_城头土_天京玉垒与木山水格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 城头土天京玉垒与木山水格(SemanticEntry):
    """
    - **原文（source_text）**：
  戊寅己卯城头土城头土者，天京玉垒，帝里金城，龙盘千里之形，虎踞四维之势。此土有成有未成，作两般论。凡遇见路傍为已成之土，不必月火；若无路傍为未成之土，...
    """
    
    original_text: str = """- **原文（source_text）**：
  戊寅己卯城头土城头土者，天京玉垒，帝里金城，龙盘千里之形，虎踞四维之势。此土有成有未成，作两般论。凡遇见路傍为已成之土，不必月火；若无路傍为未成之土，必须用火。大都城土皆须资木。杨柳癸未最隹，壬午则忌。桑柘，癸丑为上，壬子次之，庚寅、辛卯，就位相克，则城崩不宁，何以安人也耶？如见木无夹辅，只以贵人禄马论之，见水有山为显贵。甲申、丁丑俱吉，天河滋助亦吉，惟忌霹雳、大海，壬戍不忌合化，俱以吉推。土爱路傍，防见诸火，大驿逄山，须作贵观。若独见无根本，贫夭孤寒。五行见金，只有白镴、怕巽，二者相妨，余金无用，亦须以贵人禄马看之。

- **规范化释义（primary_lang_explained）**：
  戊寅、己卯为城头土。城头土如天京玉垒、帝里金城，具龙盘千里之形、虎踞四维之势，是城墙顶部与城堞之土，象征防御体系与权力中枢。此土有"已成"与"未成"两种：遇路旁土则为已成之城，不必再借火助；若无路旁土为基，则为未成之土，须用火锻烧方能成城。一般城土都须资木支撑：杨柳木癸未为上选，壬午则为忌；桑柘木以癸丑为山最佳，壬子次之。庚寅、辛卯若就位相克，则有"木冲城墙"之象，易致城崩不宁，难以安民。若见木而无其他辅佐，只能就贵人、禄马而论其吉凶。水若配有山，则主显贵：甲申、丁丑皆吉，天河水滋润亦吉；惟忌霹雳火与大海水，壬戌之水若能合化则不忌，仍以吉推。土自身仍爱路旁土为基，遇大驿土而兼有山时须作贵格看待；若城头土独立无根，则多主贫夭孤寒。金方面唯白镴金与怕巽（指某类清金）两者相互牵制有用，余金多无助力，仍须结合贵人、禄马而观之。

- **完整对等诠释（secondary_lang_full）**：
  Wuyin and Jimao belong to City-Top Earth. City-Top Earth is like heavenly capitals and jade ramparts, imperial golden cities, with the form of dragons coiling across a thousand miles and tigers crouching at the four quarters—symbolizing fortifications and centers of authority. This Earth exists in two states: completed and incomplete. When it meets Roadside Earth, it becomes completed city soil and no longer needs additional Fire; without Roadside Earth, it is still unformed and must rely on Fire to bake it into solid walls. In general, all city Earths require Wood support: Willow Wood at Guiwei is best, Renwu is disliked; for Mulberry Wood, Guichou as mountain is superior, Renzi second. When Gengyin or Xinmao Woods appear in position and clash with the city, it signifies Wood attacking walls—the city collapses and cannot provide safety. If Wood appears without other assisting factors, the chart must instead be judged by nobleman and stipend stars. When Water is seen together with mountains, high rank is indicated: Jiashen and Dingchou are both auspicious; Heavenly-River moisture is likewise good. Thunder-Bolt Fire and Ocean Water are to be feared; Renxu Water, when entering harmonious transformation, is not feared and can be treated as fortunate. Among Earths, City-Top still prefers Roadside Earth as base; when Grand-Post Earth comes together with mountains, the configuration should often be read as noble. If City-Top Earth stands alone with no roots, poverty, short life, and loneliness are likely. Regarding Metal, only White-Tin Metal and a specific Xun-associated Metal are relevant—they mutually constrain each other; other Metals are largely useless and must still be judged through the lens of nobleman and stipend.

- **核心要点**：
  - 城头土象征城堞城垣与权力中心，有"已成"与"未成"两态
  - 需路傍土为基，未成之土必须用火烧炼方成城
  - 喜适度之木、水与山，共同构成"城有基、有梁、有护河"之格局
  - 忌霹雳火、大海水以及庚寅辛卯等木来相克，易致城崩人与不安

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_115]` `[trigger: 城头土]` `[factor_trigger: wuyin_jimao AND chengtou_tu]` `[role: 主干]` 城头土者，天京玉垒，帝里金城，龙盘千里之形，虎踞四维之势。此土有成有未成，作两般论。凡遇见路傍为已成之土，不必月火；若无路傍为未成之土，必须用火。 → 《三命通会》卷一#城头土

- **详细解说**：
  城头土强调"结构完备度"与"城防系统"：有路傍土作基时，城墙已成，只需维护；无路傍土时，仍属土堆草创阶段，必须用火烧炼（象征制度、工程与时间）才成真城。木象代表城上的建筑与守卫：杨柳柔木可作城边垂柳与护堤，桑柘则为城市衣冠礼制之根基；若庚寅辛卯等刚木直接冲城，则有内外冲突之象。水象则通过"有山之水"（如甲申、丁丑配山）体现护城河与水利；天河为雨露润城，霹雳、大海则象征暴雷与洪涛，足以毁城。金几乎不直接构成城之根基，仅有白镴等清金可作城饰与器物，多需以禄贵星衡量是否能化为"帝里金城"，抑或仅是空城一座。

- **校勘与字词辨析（双语）**：
  - **中文**："天京玉垒"、"帝里金城"为典型形容京城城垣之辞；"龙盘虎踞"本为地势形容，这里专指城防之雄伟。
  - **English**: "Heavenly capital and jade ramparts" and "imperial golden city" are stock phrases for mighty city walls; "dragon coiling and tiger crouching" metaphors describe strategic, imposing fortifications."""
    normalized_text_zh: str = """"""
    subject: str = "城头土：天京玉垒与木山水格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_城头土_天京玉垒与木山水格_001_L1",
    )
    version: str = "1.0.0"
