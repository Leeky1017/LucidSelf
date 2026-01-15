"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.785787
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
    semantic_id="mlxj_v1.0.0_1_金光灿烂_金类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1金光灿烂金类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

金光灿烂，大吉。金曰从革，五行之一，地四生金，天九成之。其色有高下，紫赤为贵，黄者次之，青者又次之。其光焰焕发，射人夺目。梦此者，文士姓名显扬，武人爵位高迁...
    """
    
    original_text: str = """#### 原文（source_text）

金光灿烂，大吉。金曰从革，五行之一，地四生金，天九成之。其色有高下，紫赤为贵，黄者次之，青者又次之。其光焰焕发，射人夺目。梦此者，文士姓名显扬，武人爵位高迁，功名赫奕，威光烂爉之兆也。但疾病反复，狱讼刑伤。此外，有志必成，无往不利。

#### 规范化释义（primary_lang_explained）

梦金光灿烂，大吉。金属从革，为五行之一，地四生金，天九成之。

金色等级：
- 紫赤为贵
- 黄者次之
- 青者又次之

光焰焕发，射人夺目。梦此者：
- 文士：姓名显扬
- 武人：爵位高迁
- 功名赫奕，威光烂爉

例外：疾病反复、狱讼刑伤。

#### 完整对等诠释（secondary_lang_full）

Dreaming of brilliant golden light is greatly auspicious. Gold transforms from metal, one of the Five Elements—earth four generates gold, heaven nine completes it.

Color grades:
- Purple-red is most precious
- Yellow ranks second
- Blue-green ranks third

Radiant brilliance dazzles the eyes. Dreamers:
- Scholars: Names become renowned
- Warriors: Ranks elevated
- Fame illustrious, prestige resplendent

Exceptions: Illness fluctuates, lawsuits cause harm.

#### 核心要点

- 金光灿烂=大吉
- 金色等级：紫赤>黄>青
- 文士→显扬，武人→高迁
- 例外：疾病狱讼不宜

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v21_001]` `[trigger: 珍玩梦象]` `[factor_trigger: dream_qiantie AND jibingsongyu AND dream_jinguangcanlan]` `[role: 珍玩类]` 钱铁、疾病讼狱、金光灿烂等珍玩梦象。 → 《梦林玄解·卷二十一》#珍玩"""
    normalized_text_zh: str = """"""
    subject: str = "1 金光灿烂（金类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_金光灿烂_金类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
