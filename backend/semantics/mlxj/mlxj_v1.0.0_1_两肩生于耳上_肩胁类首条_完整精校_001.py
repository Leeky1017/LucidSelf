"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.836862
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
    semantic_id="mlxj_v1.0.0_1_两肩生于耳上_肩胁类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1两肩生于耳上肩胁类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

两肩生于耳上，似无项，大吉。体壮身强，爵高禄重。杜畿梦衣锦坐危车游黄河，左沙坡，悬镜自照。两肩高耸，颏连胸乳，似虎无项。次日，魏参军拉饮帐中，畿语曰：夜梦无...
    """
    
    original_text: str = """#### 原文（source_text）

两肩生于耳上，似无项，大吉。体壮身强，爵高禄重。杜畿梦衣锦坐危车游黄河，左沙坡，悬镜自照。两肩高耸，颏连胸乳，似虎无项。次日，魏参军拉饮帐中，畿语曰：夜梦无项恐不祥。参军曰：此乃威振边疆之象。果为河东太守。是时，天下郡县皆残破，河东最先，畿为守，郡民安物阜，名振三国。

#### 规范化释义（primary_lang_explained）

梦见两肩生于耳上，好像没有脖子，大吉。主体壮身强，爵高禄重。

杜畿曾梦见身穿锦衣坐危车游黄河，在沙坡悬镜自照，两肩高耸，下颏连着胸乳，像老虎一样没有脖子。第二天，魏参军请他饮酒，杜畿说：「昨夜梦见无项，恐不祥。」参军说：「这是威振边疆之象。」后来果然做了河东太守。当时天下郡县皆残破，河东最先安定，杜畿为守，郡民安乐物产丰富，名振三国。

#### 完整对等诠释（secondary_lang_full）

Dreaming of shoulders rising to ear level, appearing neckless, is greatly auspicious. It signifies a strong body, high rank, and generous salary.

Du Ji once dreamed of wearing brocade, sitting in a precarious carriage touring the Yellow River. On a sandy slope, he held up a mirror to look at himself—his shoulders rose high, chin connected to chest, like a tiger without a neck. The next day, General Wei invited him to drink. Du Ji said: "Last night I dreamed of having no neck—I fear it's inauspicious." The General replied: "This is a sign of commanding authority at the frontier." Indeed, he later became Governor of Hedong. At that time, all counties were in ruins, but Hedong was the first to be pacified. Under Du Ji's governance, the people prospered, and his fame spread across the Three Kingdoms.

#### 核心要点

- 两肩高耸似无项=虎形=威振之象
- 体壮身强=健康
- 爵高禄重=官位荣显
- 杜畿典故：梦应为河东太守，名振三国

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v9_001]` `[trigger: 形貌梦象]` `[factor_trigger: lishi_zhengxuan AND dream_liangjianshengyuersh AND dream_daokaixing AND dream_jianxiefubei]` `[role: 形貌类]` 郑玄典故、两肩生月日升、刀开星、肩胁腹背等形貌梦象。 → 《梦林玄解·卷九》#形貌"""
    normalized_text_zh: str = """"""
    subject: str = "1 两肩生于耳上（肩胁类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_两肩生于耳上_肩胁类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
