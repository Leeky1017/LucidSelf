"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101493
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
    semantic_id="smth_v1.0.0_天印贵_001",
    book_id="sanming",
    engine_id="bazi"
)
class 天印贵(SemanticEntry):
    """
    - **原文（source_text）**：
  有天印贵：甲子在寅中，乙逢亥亦同；丁酉戊申位，丙戌己羊宫；庚辛马蛇足，癸卯与壬龙。此号天印贵，荣达受皇封。

- **分字分词释义**：
  - **...
    """
    
    original_text: str = """- **原文（source_text）**：
  有天印贵：甲子在寅中，乙逢亥亦同；丁酉戊申位，丙戌己羊宫；庚辛马蛇足，癸卯与壬龙。此号天印贵，荣达受皇封。

- **分字分词释义**：
  - **天印贵**：以印绶之象为主的贵神，多主官印、资格与权柄。
  - **歌诀列位**：用甲子、乙亥、丁酉、戊申等干支组合标示不同日主所临天印之位。

- **规范化释义（primary_lang_explained）**：
  天印贵是一种偏向「印绶与官符」的贵格，强调正统资格、文凭证书与权柄授权。原文列出多种日主与支位的对应关系，合者多主荣达受封，有正式官职或权责在身。

- **完整对等诠释（secondary_lang_full）**：
  Heavenly-Seal Noble is based on the Seal imagery, symbolizing official credentials, qualifications, and institutional authorization. The mnemonic verse lists specific stem-branch combinations: Jia-Zi at Yin, Yi at Hai, etc. When the Seal is properly used (effective with Resource-God), it indicates "honor-reach and royal appointment" - formal official position.

  In modern terms, Tianyin maps to professional certifications, institutional recognition, and proper credentials. When it sits on Favorable-God position and combines with Tianyi Noble, it indicates smooth adaptation to formal career tracks requiring licenses (medicine, engineering, law).

  If Tianyin falls on Unfavorable-God position or gets clashed by sha-stars, the "qualification" aspect may manifest as bureaucratic complications and circuitous paths - not purely auspicious.

  Engineering note: Use tian_yin_flag for "credential acquisition propensity" rather than direct wealth/power prediction. Compare against actual certification data to calibrate weight.

- **核心要点**：
  - 与太极贵、天乙等不同，天印贵的重点在于「合法性与资格」，在系统建模中可与教育程度、职称、执照等现实变量做对照。
  - 实务判断时，应同时考察印绶在命局中的用忌关系以及是否受克冲，从而避免单凭口诀作过度乐观的解读。
 
- **详细解说**：
  1) 在命盘结构中识别日主、纳音与支位是否构成经典天印贵组合，并标注 `tian_yin_flag` 与其所在宫位、十神属性；
   2) 结合命局中本身的印绶星，区分「有印无贵」与「有贵无印」等情况，构建 `credential_potential_score`，用于刻画命主在资格、证书、牌照方面的获得倾向；
   3) 在现实数据层面，将天印相关特征与学历、职称、职业准入门槛（如医生、律师、注册工程师等）做对照校准其权重；
   4) 在解释输出时，将天印贵更多解读为「制度性认可与授权」的潜质，而不是简单许诺官职高位。

 - 反例与边界：
   - 不宜把天印贵直接等同于「必有官职」或「必在体制内」，现代社会中大量资格体现为行业证书、专业资质，而非传统官衔；
   - 若天印落在忌神之地或被重煞刑冲，其「资格」一面可能表现为手续繁琐、路径曲折，不能只按吉神论；
   - 工程上若将 `tian_yin_flag` 直接作为高收入或高权力的强预测因子，会放大偏见，应通过实际样本估计其真实贡献；
   - 反向误区是完全忽略天印结构，使模型难以解释「证书很多、路径合规」与「能力强但缺正式资质」这类现实差异。

 - 小例（示意）：
   - 某命局天印贵坐于用神之地，又与正印、天乙同见，现实中在需要严格执照的行业（如医疗、建筑）里取得完整资格并稳步晋升，系统可用「天印贵 + 印绶」结构解释其对制度轨道的适应度；
  - 另一命局虽有天印组合，却落在忌神宫位且被煞星冲破，现实表现为长期在非正式岗位或自由职业状态中徘徊，虽有能力却缺少硬证书支撑，系统则将天印视为「对资格有所追求但路径崎岖」的结构，而不简单许诺官职荣封。"""
    normalized_text_zh: str = """"""
    subject: str = "天印贵"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_55', 'bazi_semantic', 'bazi_state_factor_132', 'bazi_semantic', 'bazi_state_factor_133', 'bazi_semantic', 'bazi_relation_factor_59', 'bazi_semantic', 'bazi_condition_factor_38', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_天印贵_001_L1",
    )
    version: str = "1.0.0"
