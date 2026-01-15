"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699548
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
    semantic_id="zw_v1.0.0_王圭之命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 王圭之命(SemanticEntry):
    """
    - 分字分词释义：

  - **鲒居午位**：禄星居于午宫，官资得位，仕途清显。
  - **天梁文曲位至台纲**：天梁对照、文曲夹命，主清议公正之高位。
  - **丧门吊客**：与丧事、悲哀、损...
    """
    
    original_text: str = """- 分字分词释义：

  - **鲒居午位**：禄星居于午宫，官资得位，仕途清显。
  - **天梁文曲位至台纲**：天梁对照、文曲夹命，主清议公正之高位。
  - **丧门吊客**：与丧事、悲哀、损耗相关的丧曜组合。
  - **太岁冲凶**：太岁与命或限形成冲照并引发凶星。
  - **三杀照命**：多颗杀星同度照临命宫，主急剧风险与打击。
  - **四十四岁损寿**：中年前后遭遇重创而折寿。
  - **阴男水二局**：王圭命盘的五行局数，水二局主智慧清正。

- **原文（source_text）**：  
  王圭之命。阴男水二局。鿄居午位，官资清题朝堂，天梁文曲，位至台纲。四十四岁，丧门吊客，太岁冲凶，三杀又照，故损寿。凡天梁对照，文曲夹命者，合此格。

- **规范化释义（primary_lang_explained）**：  
  王圭命为阴男水二局，原文言「鿄居午位」，配合「官资清题朝堂」可理解为禄与官星得位，仕途清显。再加天梁、文曲同会，位至台纲，是以清议、公正著称的台谏或监察高官命格。「凡天梁对照，文曲夹命者，合此格」一句，则将此类「天梁 + 文曲夹命」结构概括为一型清贵官格。  
  然而其寿元在四十四岁附近受损：行至此年，命逢丧门、吊客等丧曜，太岁又冲凶，三杀并照，形成「丧门吊客 + 太岁冲凶 + 三杀照命」的多重压力结构。一方面象征环境中横生丧煞、官非与诛责，另一方面也标志着身体与气数在中年前后遭受重创，故以「损寿」而非终寿结束。此命例体现了「清贵台纲而寿不及高龄」的命局特征。

- **完整对等诠释（secondary_lang_full）**：  
  Wang Gui’s chart is that of a Yin Water native in the Second Configuration. With a key star—implicitly associated with stipends—"residing in Wu," and the phrase "his official rank bears clean inscriptions in the court," the pattern points to a refined, upright career. The presence of Tian Liang and Wen Qu further elevates the chart, supporting elevation "to the rank of the Censorate," where integrity and moral judgment are paramount. The text generalises that whenever Tian Liang stands in opposition and Wen Qu flanks the Life palace, the same dignified pattern is formed.  
  Yet his lifespan is curtailed around forty‑four. In that year the chart encounters Sang Men and Diao Ke, funeral stars indicating mourning and loss; the Annual Tai Sui clashes with malefics and "three Sha" shine upon the configuration. This combination—funeral indicators, aggressive yearly冲 and triple Sha—describes intense external pressure and internal depletion, leading to shortened life rather than a full span. The example illustrates a censorial, morally upright official who achieves high status but does not live into old age.

- **核心要点**：  
  1. 阴男水二局中，天梁对照、文曲夹命，官资清题，构成清贵台纲命格。  
  2. 此类命主以清议、公正与监察之责著称，却常处于高压政治环境。  
  3. 四十四岁丧门吊客、太岁冲凶、三杀并照，形成损寿而非终寿的高危组合。

- **叙事素材（narrative_snippets）**：
  - **台纲清贵**："鿄居午位，官资清题朝堂，天梁文曲，位至台纲"，王圭命主以天梁、文曲成清贵监察之职，位阶显赫。
  - **台谏格局**："凡天梁对照，文曲夹命者，合此格"，点出凡天梁对照、文曲夹命皆可成类似台纲清议格局。
  - **四十四岁损寿**："四十四岁，丧门吊客，太岁冲凶，三杀又照，故损寿"，丧门吊客加三杀照命，为中年前后折寿的具体应期。
  - **现代应用**：在现代从事纪检、监察、审计或舆论监督者，如命局带天梁、文曲台纲格，在中年前后遇到丧曜与三杀重叠的年份，应减少正面硬刚与过度操劳，用制度化、团队化方式承担压力，以免个人先被系统耗损。"""
    normalized_text_zh: str = """"""
    subject: str = "王圭之命"
    factor_refs: list = ['pattern_lu_wuwei', 'pattern_tianliang_wenqu_taigang', 'role_taigang', 'malefic_sangmen_diaoke', 'timing_taisui_chongxiong', 'malefic_sansha_zhaoming']
    
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
        l1_anchor="zw_v1.0.0_王圭之命_001_L1",
    )
    version: str = "1.0.0"
