"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699732
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
    semantic_id="zw_v1.0.0_车明贫命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 车明贫命(SemanticEntry):
    """
    - 分字分词释义：

  - **劫空临财福之乡**：地劫天空等虚空星临于财帛福德宫，主资源被抽空。
  - **戊生人逢巨门**：戊年生人巨门守命于子宫，主一生苦困口舌。
  - **子宫守命垣**...
    """
    
    original_text: str = """- 分字分词释义：

  - **劫空临财福之乡**：地劫天空等虚空星临于财帛福德宫，主资源被抽空。
  - **戊生人逢巨门**：戊年生人巨门守命于子宫，主一生苦困口舌。
  - **子宫守命垣**：命宫在子位，为特定星曜的关键位置。
  - **午限沉马之乡**：禄马落空或被冲之宫位，主福禄支撑崩塾。
  - **身命恶杀交并**：多重凶星同时作用于身命关键宫位。
  - **命难逃**：凶象重叠无解，命数难逃。
  - **阳男金四局**：车明贫命盘的五行局数，金四局主刚断贫困。

- **原文（source_text）**：  
  车明贫命。阳男金四局。生来贫贱，劫空临财福之乡。戊生人逢巨门，在子宫，守命垣，多主苦困。五十四入于午限沉马之乡，小限又到午宫，身命恶杀交并，故命难逃。

- **规范化释义（primary_lang_explained）**：  
  车明贫命为阳男金四局，「生来贫贱，劫空临财福之乡」，说明命主自出生便带有贫困结构，地劫、天空等虚空之星临于财帛、福德等关键宫位，先天资源匮乏。更关键的是「戊生人逢巨门，在子宫，守命垣，多主苦困」，戊年出生的人若巨门守命于子宫，往往一生劳碌、口舌是非多，苦困难以翻身。原文点明应期：「五十四入于午限沉马之乡，小限又到午宫，身命恶杀交并」，五十四岁时大限行至午宫，午为子的对冲位，形成「沉马」之象（禄马落空或被冲），小限也到午宫，身宫与命宫同时遭遇恶杀交并，最终「命难逃」。

- **完整对等诠释（secondary_lang_full）**：  
  This "Che Ming the Impoverished" chart for a Yang Metal native features inherent poverty: Kong and Jie occupy the Wealth and Blessings palaces, draining resources from the start. For someone born in Wu year, Ju Men guarding Life in Zi often brings lifelong hardship and disputes. At fifty‑four, the major period enters Wu—the opposing position to Zi, creating "sinking horse" imagery where fortune and support collapse. The minor period also reaches Wu, and malefics converge on both Body and Life palaces. Under this pile‑up, the native "cannot escape fate."

- **核心要点**：  
  1. 劫空临财福之乡，先天资源匮乏，贫困结构自出生即定。  
  2. 戊生人巨门守命于子，一生多苦困与口舌是非。  
  3. 五十四岁大小限同入午宫，沉马与恶杀交并，构成致命年份。"""
    normalized_text_zh: str = """"""
    subject: str = "车明贫命"
    factor_refs: list = ['malefic_jiekong_caifu', 'pattern_wusheng_jumen_zi', 'malefic_chenma_zhixiang', 'timing_wuxian', 'malefic_esha_jiaobing', 'result_ming_nantao']
    
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
        l1_anchor="zw_v1.0.0_车明贫命_001_L1",
    )
    version: str = "1.0.0"
