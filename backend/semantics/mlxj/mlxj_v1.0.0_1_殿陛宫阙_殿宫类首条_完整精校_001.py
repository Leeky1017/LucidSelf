"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.814314
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
    semantic_id="mlxj_v1.0.0_1_殿陛宫阙_殿宫类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1殿陛宫阙殿宫类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

殿陛宫阙大吉。凡此兆主恩荣之事，惟帝王之梦，殿陛当以他物论，何也？身居九重，非臣民比也。若夫后妃王子，宫人内相，则又以梦中所见者推之矣。卿相官吏，梦之主钦命...
    """
    
    original_text: str = """#### 原文（source_text）

殿陛宫阙大吉。凡此兆主恩荣之事，惟帝王之梦，殿陛当以他物论，何也？身居九重，非臣民比也。若夫后妃王子，宫人内相，则又以梦中所见者推之矣。卿相官吏，梦之主钦命召赐升加；文人武士，梦之主显爵厚禄进取；平民老幼梦之，主将来荣华富贵。妇人女子梦之，主丈夫子婿高明，亲族孙支茂盛，疾病患难梦之主祸去福临寿永。僧道尼姑梦之，主天神佛力扶持。

#### 规范化释义（primary_lang_explained）

梦见殿陛宫阙，大吉。此兆主恩荣之事。

按身份分化：
- **帝王**：殿陛当以他物论（身居九重，非臣民比）
- **后妃王子宫人内相**：以梦中所见推之
- **卿相官吏**：主钦命召赐升加
- **文人武士**：主显爵厚禄进取
- **平民老幼**：主将来荣华富贵
- **妇人女子**：主丈夫子婿高明，亲族孙支茂盛
- **疾病患难者**：主祸去福临寿永
- **僧道尼姑**：主天神佛力扶持

#### 完整对等诠释（secondary_lang_full）

Dreaming of palace halls and imperial gates is greatly auspicious. This omen signifies grace and glory.

Interpreted by status:
- **Emperors**: Palace dreams interpreted differently (residing in the ninth tier, unlike subjects)
- **Empresses, princes, palace attendants**: Interpret by what appears in the dream
- **Ministers and officials**: Imperial summons, bestowals, promotions
- **Scholars and warriors**: Noble ranks, generous salaries, advancement
- **Commoners young and old**: Future glory and wealth
- **Women**: Husband and sons-in-law distinguished, relatives flourishing
- **Those ill or in difficulty**: Misfortune departs, blessings arrive, longevity
- **Buddhist and Taoist clergy**: Divine and Buddha's support

#### 核心要点

- 殿陛宫阙=恩荣之事=最高吉兆
- 身份分化占断法
- 帝王例外：身居九重非臣民比
- 普遍吉兆：祸去福临

#### 典故

- 待制王素梦玉京黄阙：碧虚白玉京，飞入黄金城
- 蔡茂梦坐大殿极上三穗禾：中穗=中台之位，后为司徒

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v15_001]` `[trigger: 栋宇梦象]` `[factor_trigger: dream_dizhai AND dream_dianbigongque]` `[role: 栋宇类]` 第宅、殿壁宫阙等栋宇梦象。 → 《梦林玄解·卷十五》#栋宇"""
    normalized_text_zh: str = """"""
    subject: str = "1 殿陛宫阙（殿宫类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_殿陛宫阙_殿宫类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
