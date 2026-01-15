"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739952
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
    semantic_id="zw_v1.0.0_批富命_巨门辰戌化忌得扶格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批富命巨门辰戌化忌得扶格(SemanticEntry):
    """
    - 分字分词释义：

  - **巨门辰戌陷**：巨门在辰戌宫为陷地，主是非口舌。
  - **化忌峙嵬**：辛年生人巨门化忌更显峙嵬凶象。
  - **左右扶持**：左辅右彼扶持命宫，化凶为吉。
 ...
    """
    
    original_text: str = """- 分字分词释义：

  - **巨门辰戌陷**：巨门在辰戌宫为陷地，主是非口舌。
  - **化忌峙嵬**：辛年生人巨门化忌更显峙嵬凶象。
  - **左右扶持**：左辅右彼扶持命宫，化凶为吉。
  - **紫微镇财**：紫微星镇守财宫，财源稳固。
  - **有制有化**：凶星得制得化则转吉，化忌转吉的核心逻辑。
  - **黄梁梦**：人生如梦典故，寿终仙逝的隐喻。
  - **威风凛然志昂昂**：凶星得化后之人性情威严、志向高远。

- **原文（source_text）**：  
  辰戌坐陷巨门，辛人化忌峥嵘，据理未能成格局，扶身左右相帮官禄。紫帝镇守财宫，一宿财藏，深喜太阳午方照申子申，的当吉凶前后循序，得垣少陷辉光。火星虽晤水星，克既济之功，理讲乃为是非之曜，有制有化，中央威风凛然志昂昂，扩充先人闻望。命主某宫某宿，主星值在财乡，财星贴主，喜生方皓月空宵夜朗。堂上椿萱俱庆，庭前棠棣联芳。红楼早配效鸾凰，子息麒麟天降。早岁童庒之内，寒暑不测灾殃。七年九祀在关乡，尤当调持珍重。某限十年上美，郁含脱翠松篁，太岁冲提尚徜徉，晚景安然福享。七十二三归去，觉来梦叶黄梁。

- **规范化释义（primary_lang_explained）**：  
  此为批断「巨门辰戌陷地化忌、得左右扶持」富命的标准套语。核心逻辑：巨门在辰戌为陷地，辛年生人化忌更显峥嵘（凶象），按理难成格局；然而得左右辅弼扶持、紫微镇守财宫、太阳午方照会，则凶星得化、化忌转吉。套语论述性情（威风凛然）、六亲（椿萱俱庆、棠棣联芳）、早年童庚灾厄，以及七十寿终「觉来梦叶黄梁」。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the "Ju Men in Chen/Xu Detriment with Hua Ji, Supported and Transformed" wealth pattern. Core logic: Ju Men in Chen or Xu is in detriment, for Xin year birth transforming to Ji makes it more formidable; logically difficult to form good configuration. However, with Zuo Fu and You Bi support, Zi Wei guarding Wealth Palace, and Tai Yang shining from Wu position, the malefic becomes transformed. The template discusses temperament, Six Relations, early tribulations, and death at seventy "awakening from Yellow Millet dream".

- **核心要点**：  
  1. 格局特点：巨门辰戌陷化忌，得左右扶持、紫微镇财。  
  2. 转化逻辑：凶星有制有化，化忌转吉。  
  3. 人生周期：早年灾厄→限运起伏→七十寿终。"""
    normalized_text_zh: str = """"""
    subject: str = "批富命·巨门辰戌化忌得扶格"
    factor_refs: list = ['star_jumen_chenxu_xian', 'sihua_huaji_zhengrong', 'pattern_zuoyou_fuchi', 'pattern_ziwei_zhencai', 'mech_youzhiyouhua', 'symbol_huangliangmeng', 'source_ref', 'rel_vol7_12_001', 'star_jumen_chenxu_xian', 'rel_vol7_12_002', 'pattern_zuoyou_fuchi', 'rel_vol7_12_003', 'pattern_ziwei_zhencai', 'rel_vol7_12_004', 'result_jumen_fuming', 'evi_vol7_12_001', 'rule_jumen_huaji_defuzhuan', 'evi_vol7_12_002', 'rule_ziwei_zhencai_fuming', 'evi_vol7_12_003', 'symbol_huangliangmeng', 'rule_huangliang_shoumian', 'concept_malefic_transformation', 'concept_early_hardship', 'concept_yellow_millet']
    
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
        l1_anchor="zw_v1.0.0_批富命_巨门辰戌化忌得扶格_001_L1",
    )
    version: str = "1.0.0"
