"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997234
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
    semantic_id="dts_v1.0.0_地全三物_不可使天道莫之覆_001",
    book_id="dts",
    engine_id="bazi"
)
class 地全三物不可使天道莫之覆(SemanticEntry):
    """
    - **原文（source_text）**：
  地全三物，不可使天道莫之覆。

- 原注（原文注解）：
  　　寅卯辰，而遇甲乙庚辛相冲，为天莫覆。

- 分字分词释义：
  - 地全三物：地支成“...
    """
    
    original_text: str = """- **原文（source_text）**：
  地全三物，不可使天道莫之覆。

- 原注（原文注解）：
  　　寅卯辰，而遇甲乙庚辛相冲，为天莫覆。

- 分字分词释义：
  - 地全三物：地支成“方局三物”纯全之势（如寅卯辰）。
  - 天道：天干层面之覆载与统摄。
  - 莫之覆：上层（天干）无法覆护、难以相应。

- **规范化释义（primary_lang_explained）**：
  地支若成寅卯辰之类“三物纯全”，固然根基厚实，却仍需天干在上覆护相应；若天干缺位、偏离或被冲破，则成“地强天弱”，下有其局而上无其主，终难长久。

- **次语种完整诠释（secondary_lang_full）**:  
  When the earth branches form a pure three-branch assembly such as Yin–Mao–Chen, the chart holds a solid base of localised qi. Yet this foundation cannot stand alone: it requires corresponding heavenly stems above to cover, guide and answer it. If those stems are missing, scattered, or directly clashed by other stems, "heaven cannot cover earth"; the situation becomes one of strong structure below but weak response above. In practice this appears as good local conditions, resources or networks that never receive matching platforms, authority or recognition. The remedy is to secure either true counterparts on the stems or indirect supporters such as Resources and Wealth that bridge between heaven and earth, so that a complete earth pattern does not remain an empty shell but can be carried, protected and made genuinely useful.

- **核心要点**：
  - 地全三物只是“下局纯全”，仍需上有天道覆护方成大局。
  - 天干若缺位或被冲破，则易成“下实上虚”，力有余而位不足。
  - 补救在于寻求天干对位或间接补覆，使三物之力有处着落。

- **详细解说**：
  此条从“地强天弱”的角度谈天地配合：寅卯辰一类方局三物，代表某一类气在地支层面已成结构性优势，但若天干无相应、甚至被冲破，则好局只停留在“地方势力”“基层资源”层面，而难以上达为制度、平台与长期护持。实务判断时，一方面要看地支是否真成三物纯全，另一方面更要查天干是否有本气透出、用神在上呼应，抑或被其他干强行冲裂。若见“地全三物而天莫覆”，则应着力于引通上层资源：或透印透财以桥接，或借运岁之干暂代覆护，使下局之力不致空转.

- **narrative_snippets（叙事片段）**：
  - `[ns_dts_079]` `[trigger: 地支形成寅卯辰等三物纯全]` `[factor_trigger: dizhi_three_materials_purity_level==纯全 AND tiangan_cover_response==支持覆护 AND cover_integrity_flag==off]` `[role: 主干]` 地全三物而天干相应覆护，多主根基厚实且上有平台承接。 → 《滴天髓·天地承载》#地全三物
  - `[ns_dts_080]` `[trigger: 地全三物而天干缺位或被冲]` `[factor_trigger: dizhi_three_materials_purity_level==纯全 AND (tiangan_cover_response IN {对立, 缺位} OR cover_conflict_state==有) AND cover_integrity_flag==on]` `[role: 条件分支]` 地局虽成而天道莫覆，常见基础好却难登高位、成果难以兑现。 → 《滴天髓·天地承载》#地全三物
  - `[ns_dts_081]` `[trigger: 评估三物格局吉凶]` `[factor_trigger: dizhi_three_materials_purity_level!=未形成 AND (tiangan_cover_response==支持覆护 OR cover_compensation_type!=无)]` `[role: 主干依赖]` 断三物格局先看地之纯，再看天之覆护，有覆则成局，无覆则求补救之道。 → 《滴天髓·天地承载》#地全三物
  - `[ns_dts_149]` `[trigger: 天干被冲无覆]` `[factor_trigger: dizhi_three_materials_purity_level==纯全 AND cover_conflict_state==有 AND tiangan_cover_response IN {对立, 缺位} AND cover_integrity_flag==on]` `[role: 例外处理]` 天干被冲破而地局无覆护，纵有三物亦成空架。 → 《滴天髓·天地承载》#地全三物
  - `[ns_dts_150]` `[trigger: 地强天弱总则]` `[factor_trigger: dizhi_three_materials_purity_level IN {纯全, 偏} AND (tiangan_cover_response==支持覆护 OR cover_compensation_type!=无)]` `[role: 总结]` 地强须天覆，下局能否成就，关键看上层是否相应。 → 《滴天髓·天地承载》#地全三物

**校勘与字词辨析（textual_criticism）**：
  - 中文：无版本差异 / N/A  
  - English: No known textual variants / N/A"""
    normalized_text_zh: str = """"""
    subject: str = "地全三物，不可使天道莫之覆。"
    factor_refs: list = ['diquan_sanwu', 'tiandao', 'mozhifu', 'fuhu', 'fangju', 'shangxia_pipei']
    
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
        book_id="dts",
        chapter="",
        l1_anchor="dts_v1.0.0_地全三物_不可使天道莫之覆_001_L1",
    )
    version: str = "1.0.0"
