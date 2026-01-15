"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.740023
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
    semantic_id="zw_v1.0.0_批女命_某星落陷不逢克战格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批女命某星落陷不逢克战格(SemanticEntry):
    """
    - 分字分词释义：

  - **命星落陷不逢克战**：命星落陷但不逢克战，凶中有转化之机。
  - **幽兰出谷**：落陷转吉的比喻，如幽兰出谷风送香来。
  - **金石之盟**：坚贞的婚姻誓约，...
    """
    
    original_text: str = """- 分字分词释义：

  - **命星落陷不逢克战**：命星落陷但不逢克战，凶中有转化之机。
  - **幽兰出谷**：落陷转吉的比喻，如幽兰出谷风送香来。
  - **金石之盟**：坚贞的婚姻誓约，良人有金石之盟同谐鹤发。
  - **助夫益子**：当助夫富厚、益子名香的女命功能。
  - **镜破仪分**：寿终的委婉表达，周流八卦镜破仪分。
  - **桂子天香**：子女出众，桂子有天香之秀当继书香。
  - **内助咸亨**：妇人贤惠、内助持家顺利。

- **原文（source_text）**：  
  某星虽落陷地，喜得不逢克战，此则为幽兰出谷，风送香来，当助夫富厚，益子名香。良人有金石之盟同谐鹤发，桂子有天香之秀当继书香。今限某星正旺，夫之地内助咸亨。助夫广增财上利，弄璋频应梦中诗。某岁乃驭杂之限，虽有喜而慎忧，不无得而有失，须防珠生蚌损，又恐燕语莺啼，宝髻懒梳愁折凤，菱花羞对怯飞鸾。且喜身有吉护，限虽恶何害。步入某限某星得合，十年平顺，荣夫增富贵，产子若人龙，瑞气盈门，蔼天香馥馥临。不惟门第鼎新，又教儿郎进业。此时果然积白堆黄，灾稀疾少。唯于某年虎逐羊头，某年过年羊跟猿尾，见此刑并漠漠羊肠。闺中无限伤心事，尽在停针不语时。耗于物，刑于丁，总作离愁之苦，羊肠苔径滑金莲缓步移。脱此星限行入某宫，福有万端，灾无半点，夫业兴子成名。悠悠五福廿年洋洋喜气蔼祯祥，不但助夫金玉广，喜看贵子出朝堂。某年徙然一吁，橦入某星有所不吉，花落自离枝，非干风雨催，幸不倒限，可以到某年而不可以出某年。周流八卦，镜破仪分。

- **规范化释义（primary_lang_explained）**：  
  此为批断「命星落陷而不逢克战」女命的标准套语。核心逻辑：虽然命星落陷，但不逢克战则如「幽兰出谷、风送香来」，仍可助夫富厚、益子名香。套语详论婚姻（金石之盟、鹤发偕老）、子女（桂子天香、书香传继）、限运吉凶（十年平顺、积白堆黄；刑并羊肠、闺中伤心），以及寿终应期（镜破仪分）。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the female fate pattern "Life Star in Detriment but No Clash". Core logic: though the Life star falls into detriment, without encountering clash it becomes "orchid emerging from valley, fragrance carried by wind"—still capable of enriching husband and benefiting children. The template details marriage (golden‑stone oath, growing old together), children (cassia offspring, scholarly legacy), period fortunes (ten years smooth, gold piling; clash periods, inner sorrow), and death timing (mirror broken, ceremony parted).

- **核心要点**：  
  1. 适用格局：命星落陷但不逢克战，凶中有转化之机。  
  2. 女命功能：助夫富厚、益子名香、内助咸亨。  
  3. 限运特征：有平顺期、有刑并期、有寿终应期。"""
    normalized_text_zh: str = """"""
    subject: str = "批女命·某星落陷不逢克战格"
    factor_refs: list = ['pattern_luoxian_bufeng_kezhan', 'symbol_youlan_chugu', 'symbol_jinshi_zhimeng', 'trait_zhufu_yizi', 'symbol_jingpo_yifen', 'source_ref', 'rel_vol7_16_001', 'pattern_luoxian_bufeng_kezhan', 'rel_vol7_16_002', 'symbol_youlan_chugu', 'rel_vol7_16_003', 'symbol_jinshi_zhimeng', 'rel_vol7_16_004', 'result_numing_gui', 'evi_vol7_16_001', 'rule_luoxian_youlan_zhufu', 'evi_vol7_16_002', 'symbol_jinshi_zhimeng', 'rule_jinshi_hefahuaxu', 'evi_vol7_16_003', 'symbol_jingpo_yifen', 'rule_jingpo_yifen_shoumian', 'concept_orchid_transformation', 'concept_golden_oath', 'concept_mirror_parting']
    
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
        l1_anchor="zw_v1.0.0_批女命_某星落陷不逢克战格_001_L1",
    )
    version: str = "1.0.0"
