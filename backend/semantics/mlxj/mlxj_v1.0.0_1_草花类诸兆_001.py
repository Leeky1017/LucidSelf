"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.802944
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
    semantic_id="mlxj_v1.0.0_1_草花类诸兆_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1草花类诸兆(SemanticEntry):
    """
    #### 分类汇总

**大吉类**：
- 琼花大吉：位冠群寮，官居一品
- 萱花吉：忘忧宜男

**吉类**：
- 玫瑰吉：子姓兴隆
- 夜合吉：阳刚中正
- 樱桃吉：少年荣华
- 接花吉：移花接木...
    """
    
    original_text: str = """#### 分类汇总

**大吉类**：
- 琼花大吉：位冠群寮，官居一品
- 萱花吉：忘忧宜男

**吉类**：
- 玫瑰吉：子姓兴隆
- 夜合吉：阳刚中正
- 樱桃吉：少年荣华
- 接花吉：移花接木，有收成

**贞吉否凶类**：
- 槿：防微杜渐
- 绣毬：子息望空
- 凌霄花：气宇昂昂，但须附乔松

**凶类**：
- 花草凋枯凶：色衰气败
- 花飞花谢花残枯：散乱漂泊
- 十姊妹凶：群阴之象

#### 花色象征

| 花色 | 主应 |
|------|------|
| 红 | 少年寿不长 |
| 白 | 清高 |
| 紫 | 贵显 |
| 黄 | 富贵 |

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v18_001]` `[trigger: 草花象征]` `[factor_trigger: dream_caohua AND dream_zhuying AND huase]` `[role: 象征体系]` 花色主应：红少年寿不长，白清高，紫贵显，黄富贵。 → 《梦林玄解·卷十八》#草花类
- `[ns_mlxj_v18_002]` `[trigger: 树木梦象]` `[factor_trigger: shumu_zhuangtai AND dream_songchufufu AND dream_shumumaosheng]` `[role: 树木类]` 树木状态、松出夫妇、树木茂盛等梦象。 → 《梦林玄解·卷十八》#树木"""
    normalized_text_zh: str = """"""
    subject: str = "1 草花类诸兆"
    factor_refs: list = ['source_ref']
    
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
        book_id="mlxj",
        chapter="",
        l1_anchor="mlxj_v1.0.0_1_草花类诸兆_001_L1",
    )
    version: str = "1.0.0"
