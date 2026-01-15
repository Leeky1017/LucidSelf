"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.829220
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
    semantic_id="mlxj_v1.0.0_1_冕旒_冠冕类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1冕旒冠冕类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

冕旒，大吉。冕旒之制古矣，始于黄帝，冠上有覆，前后有旒。夏禹致孝享，美乎黻冕。孔子论为邦服周之冕。乃至尊之元服。国家举盛典，行隆礼，则用此焉。梦之者，主有大...
    """
    
    original_text: str = """#### 原文（source_text）

冕旒，大吉。冕旒之制古矣，始于黄帝，冠上有覆，前后有旒。夏禹致孝享，美乎黻冕。孔子论为邦服周之冕。乃至尊之元服。国家举盛典，行隆礼，则用此焉。梦之者，主有大喜庆事。士人见冕旒，必受恩荣。女子见冕旒，必蒙钦选。官僚见冕旒，为左右辅弼；嫔妃见冕旒，得朝夕进御；庶民见冕旒，子孙入觐天颜。或自见神像以应梦焉。

#### 规范化释义（primary_lang_explained）

梦见冕旒，大吉。冕旒之制始于黄帝，冠上有覆，前后有旒。夏禹致孝享美于黻冕，孔子论为邦服周之冕。这是至尊的首服，国家举盛典行隆礼则用此。

按身份分化：
- **梦者**：主有大喜庆事
- **士人**：必受恩荣
- **女子**：必蒙钦选
- **官僚**：为左右辅弼
- **嫔妃**：得朝夕进御
- **庶民**：子孙入觐天颜

或自见神像以应梦。

#### 完整对等诠释（secondary_lang_full）

Dreaming of the imperial crown with pendants (mian liu) is greatly auspicious. This headgear system began with the Yellow Emperor—a crown with covering and pendants front and back. Yu the Great honored it in ancestral rites; Confucius praised the Zhou dynasty's crown. It is the supreme headgear, used in grand state ceremonies.

By status:
- **Dreamers**: Great celebration ahead
- **Scholars**: Certain to receive grace and glory
- **Women**: Certain to be imperially selected
- **Officials**: Becoming left-right advisors
- **Consorts**: Gaining daily audience with the emperor
- **Commoners**: Descendants will attend imperial court

Or one may see divine statues in response to the dream.

#### 核心要点

- 冕旒=至尊之元服=最高权力象征
- 始于黄帝，夏禹孔子皆重之
- 国家盛典隆礼之用
- 身份分化占断：各有对应主应
- 大喜庆事

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v16_001]` `[trigger: 服饰梦象]` `[factor_trigger: dream_mianliu AND yise]` `[role: 服饰类]` 冕旒、衣色等服饰梦象。 → 《梦林玄解·卷十六》#服饰"""
    normalized_text_zh: str = """"""
    subject: str = "1 冕旒（冠冕类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_冕旒_冠冕类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
