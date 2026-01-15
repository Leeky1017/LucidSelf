"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654035
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
    semantic_id="zw_v1.0.0_起五寅例_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 起五寅例(SemanticEntry):
    """
    **主题**：根据生年天干确定正月的天干起点。

#### 原文（断句）：

甲己之岁起丙寅，乙庚之岁起戊寅，丙辛之岁起庚寅，丁壬之岁起壬寅，戊癸之岁起甲寅。

#### 分字分词释义：

- **甲...
    """
    
    original_text: str = """**主题**：根据生年天干确定正月的天干起点。

#### 原文（断句）：

甲己之岁起丙寅，乙庚之岁起戊寅，丙辛之岁起庚寅，丁壬之岁起壬寅，戊癸之岁起甲寅。

#### 分字分词释义：

- **甲己之岁**：生年天干为甲或己的年份。
- **起丙寅**：以丙寅为正月的天干地支起点。
- **五寅**：五组年干对应的五个不同的寅月起点（丙寅、戊寅、庚寅、壬寅、甲寅）。
- **天干五合**：甲己合化土、乙庚合化金、丙辛合化水、丁壬合化木、戊癸合化火。
- **月柱**：用天干地支表示的月份信息，与年柱、日柱、时柱构成四柱。

#### 规范化释义（primary_lang_explained）：

甲己之岁起丙寅乙庚之岁起戊寅丙辛之岁起庚寅丁壬之岁起壬寅戊癸之岁起甲寅。

#### 核心要点：

- 甲己年：正月起丙寅
- 乙庚年：正月起戊寅
- 丙辛年：正月起庚寅
- 丁壬年：正月起壬寅
- 戊癸年：正月起甲寅

#### 应用：用于推算各月天干地支。

#### 完整对等诠释（secondary_lang_full·3起五寅例）：

Five-Yin Starting Formula explains how to derive the stem of the first lunar month from the birth-year stem. The ten heavenly stems are paired into five combined groups—Jia with Ji, Yi with Geng, Bing with Xin, Ding with Ren, and Wu with Gui—and each pair is linked to a specific starting stem–branch at Yin. Jia–Ji years begin at Bing-Yin, Yi–Geng years at Wu-Yin, Bing–Xin years at Geng-Yin, Ding–Ren years at Ren-Yin, and Wu–Gui years at Jia-Yin. Once the starting pair at Yin is fixed, the remaining months follow in order as the stems and branches cycle forward.

In practice this rule builds a conversion bridge from year stem to month stem, allowing the astrologer to compute the month pillar used in many later techniques. It also encodes the doctrine of the five stem combinations: each paired group shares a common energetic root and therefore launches its year from the same flavour at Yin. Getting the Five-Yin starting point correct keeps seasonal timing, later transformations and certain chart structures consistent with the native’s birth year.

#### L2-术语对齐（Term Glossary·六列）：

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 起五寅 | Five-Yin Starting | 根据年干确定正月干支起点 | First-month stem from year-stem | algo_qiwuyin | new_candidate |
| 天干五合 | Heavenly-Stem Five-Combo | 甲己乙庚丙辛丁壬戊癸五组配对 | Five pairings Jia-Ji etc | principle_tianganwuhe | existing |
| 月柱 | Month Pillar | 月份的天干地支组合 | Stem-branch monthly timing | structure_yuezhu | existing |
| 寅月 | Yin Month | 地支寅对应正月 | Yin branch first lunar month | position_yinyue | existing |

#### 详细解说：

起五寅例是紫微斗数与八字命理共用的基础算法，用于根据生年天干推算正月的月干。这一规则体现了天干五合的原理。

**算法原理**：
天干五合是指甲与己、乙与庚、丙与辛、丁与壬、戊与癸两两配对，形成五组合化关系。同一组内的年干，其正月天干起点相同：
- 甲己年→丙寅月起
- 乙庚年→戊寅月起
- 丙辛年→庚寅月起
- 丁壬年→壬寅月起
- 戊癸年→甲寅月起

**记忆口诀**：
"甲己丙作首，乙庚戊为头，丙辛庚上起，丁壬壬位求，戊癸甲寅始，月干不须愁。"

**应用场景**：
1. 推算命盘中各月的天干地支
2. 验证排盘软件的计算结果
3. 理解四化飞星与月干的关系

#### 校勘与字词辨析（bilingual）：

- **"甲己之岁"**：甲年或己年。英文："Jia or Ji year"。
- **"起"**：起始、开始计算。英文："start from" 或 "begin counting at"。
- **"寅"**：正月对应的地支，固定不变。英文："Yin branch, fixed for the first lunar month"。

#### 叙事素材（narrative_snippets）：

- **传统叙事**："甲己丙寅首，乙庚戊位头，丙辛庚上起，丁壬壬位求，戊癸甲寅始。"此为传统记忆口诀，帮助学习者快速掌握五寅规则。
- **五合原理**：五寅规则源于天干五合的化气理论，体现了阴阳五行相合相化的哲学思想。
- **现代应用**：现代排盘软件自动计算月干，但理解五寅规则对于验证计算结果、深入理解干支体系仍有价值。

**L2 叙事素材层（规范格式）**：

- `[ns_zwds_j3_028]` `[trigger: 起五寅算法]` `[factor_trigger: algo_qiwuyin]` `[role: 主干]` 起五寅算法为根据年干确定正月天干起点的算法。 → 《起五寅例》
- `[ns_zwds_j3_029]` `[trigger: 天干五合]` `[factor_trigger: principle_tianganwuhe]` `[role: 主干]` 天干五合为甲己乙庚丙辛丁壬戊癸五组配对原理。 → 《起五寅例》
- `[ns_zwds_j3_030]` `[trigger: 甲己合化]` `[factor_trigger: combo_jiaji]` `[role: 条件分支]` 甲己合化土，甲己年正月起丙寅。 → 《起五寅例》"甲己丙寅首"
- `[ns_zwds_j3_031]` `[trigger: 乙庚合化]` `[factor_trigger: combo_yigeng]` `[role: 条件分支]` 乙庚合化金，乙庚年正月起戊寅。 → 《起五寅例》"乙庚戊位头"
- `[ns_zwds_j3_032]` `[trigger: 丙辛合化]` `[factor_trigger: combo_bingxin]` `[role: 条件分支]` 丙辛合化水，丙辛年正月起庚寅。 → 《起五寅例》"丙辛庚上起"
- `[ns_zwds_j3_033]` `[trigger: 丁壬合化]` `[factor_trigger: combo_dingren]` `[role: 条件分支]` 丁壬合化木，丁壬年正月起壬寅。 → 《起五寅例》"丁壬壬位求"
- `[ns_zwds_j3_034]` `[trigger: 戊癸合化]` `[factor_trigger: combo_wugui]` `[role: 条件分支]` 戊癸合化火，戊癸年正月起甲寅。 → 《起五寅例》"戊癸甲寅始"
- `[ns_zwds_j3_035]` `[trigger: 纳音五行]` `[factor_trigger: system_nayin]` `[role: 主干]` 纳音五行为六十甲子的五行归属体系。 → 《起五寅例》
- `[ns_zwds_j3_036]` `[trigger: 月干推算]` `[factor_trigger: algo_yuegantuisuan]` `[role: 主干]` 月干推算为根据年干和月份推算月干的算法。 → 《起五寅例》"""
    normalized_text_zh: str = """"""
    subject: str = "起五寅例"
    factor_refs: list = ['source_ref', 'rel_wuyin_001', 'algo_qiwuyin', 'rel_wuyin_002', 'principle_tianganwuhe', 'evi_wuyin_001', 'algo_qiwuyin', 'rule_jiaji_bingyin', 'evi_wuyin_002', 'algo_qiwuyin', 'rule_wugui_jiayin', 'concept_stem_combo', 'concept_month_pillar']
    
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
        l1_anchor="zw_v1.0.0_起五寅例_001_L1",
    )
    version: str = "1.0.0"
