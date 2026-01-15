"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725614
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
    semantic_id="zw_v1.0.0_11_天梁星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 11天梁星(SemanticEntry):
    """
    - 原文（source_text）：

  问：天梁星所主若何？
  
  答曰：天梁属土，南斗第二星也。司寿化气，为荫为福。寿乃父母之主，宰杀帝之权。于人命则性情磊落，于相貌则厚重温谦，循理无私，临...
    """
    
    original_text: str = """- 原文（source_text）：

  问：天梁星所主若何？
  
  答曰：天梁属土，南斗第二星也。司寿化气，为荫为福。寿乃父母之主，宰杀帝之权。于人命则性情磊落，于相貌则厚重温谦，循理无私，临事果决，荫于身命，福及子孙。遇昌曲于财官，逢太阳于福德，合乃为万全，声名题于王室，职位临于风宪。若逢耗曜，更逢天机及杀，宜僧道，亦受王朝制诰。逢贪狼同度，而乱礼乱家。太岁冲而为福，白虎临而无殃。
  
  希夷先生曰：天梁南斗，司寿之星，化气为荫为寿，佐上帝威权，为父母宫主，主人清秀温和，形神稳重，性情磊落，善识兵法。得昌曲左右加会，位至台省。在父母宫，则厚重威严，会太阳于福德，极品之贵。戊巳生人合局，若四杀冲破，则苗而不秀。逢天机耗曜，僧道清闲；如贪巨同度，则败伦乱俗。太岁冲而为福，白虎会而无灾。奏书动，则有意外之荣；青龙动，则有文书之喜。
  
  歌曰：天梁原属土，南斗最吉星。化荫名延寿，父母宫主星。田宅兄弟内，得之福自生。形神自持重，心性更和平。生来无灾患，文章有声名。六亲更和睦，仕宦居王庭。巨门若相会，劳碌历艰辛。若逢天机照，僧道享山林。

- 分字分词释义：

  - **天梁**：南斗第二星，五行属土，司寿化荫，为父母宫主。
  - **司寿化气**：掌管寿命之星，其气化为荫护与福寿。
  - **为荫为福**：象征庇护、福荫，能庇佑命主与子孙。
  - **父母之主**：天梁为父母宫主星，主父母之力与长辈庇护。
  - **性情磊落**：光明正大、坦荡无私的性格特质。
  - **厚重温谦**：外表稳重、性情温和谦逊。
  - **循理无私**：遵循道理、不存私心。
  - **临事果决**：面对事情时果断决策。
  - **位至台省**：官至中央机构高位（古指尚书省、中书省等）。
  - **极品之贵**：至高无上的贵显地位。
  - **苗而不秀**：有才华潜质但难以展现成就。
  - **僧道清闲**：适合出家修行或清闲离俗的生活。
  - **败伦乱俗**：违背伦理、败坏风俗。
  - **太岁冲而为福**：被太岁冲击反而激活庇护，凶险之年反成福年。
  - **白虎会而无灾**：遇白虎凶星也无灾祸，天梁能化解。

- 核心要点：

  1. **天梁化荫**：司寿之星化气为荫为寿，父母宫主。
  2. **性情磊落**：性情磊落，厚重温谦，临事果决。
  3. **荫福子孙**：荫于身命，福及子孙，太岁冲而为福。
  4. **天机同度**：逢天机耗曜僧道清闲，善识兵法。
  5. **女命旺夫**：女人吉星入庙旺夫益子，封赠论。

- 叙事素材（narrative_snippets）：

  - **荫寿父母**："司寿之星化气为荫为寿，父母宫主"，天梁主长辈庇护与长寿。
  - **性情磊落**："性情磊落，厚重温谦，临事果决"，体现刚正而不刻薄的品格结构。
  - **太岁冲福**："荫于身命，福及子孙，太岁冲而为福"，看似冲犯反成激活庇护之力。
  - **僧道清闲**："逢天机耗曜僧道清闲"，适合以修行、清闲离俗的路径承载其能量。
  - **女命旺夫**："女人吉星入庙旺夫益子，封赠论"，女命得天梁多主旺夫益子封赠。
  - **现代应用**：天梁可作为评估"家族庇护与道义骨架"的指标——看一生能否在风波中仍有长辈与制度护持。"""
    normalized_text_zh: str = """"""
    subject: str = "11 天梁星"
    factor_refs: list = ['star_tianliang', 'concept_huayin_yanshou', 'pattern_taisui_chongfu', 'pattern_sengdao_qingxian', 'combo_tanju_tongdu']
    
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
        l1_anchor="zw_v1.0.0_11_天梁星_001_L1",
    )
    version: str = "1.0.0"
