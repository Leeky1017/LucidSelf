"""
Auto-generated semantic module for mlxj
Generated at: 2025-12-05T13:30:19.823532
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
    semantic_id="mlxj_v1.0.0_1_万羊大吉_六畜类首条_完整精校_001",
    book_id="mlxj",
    engine_id="dream"
)
class 1万羊大吉六畜类首条完整精校(SemanticEntry):
    """
    #### 原文（source_text）

万羊大吉，牧羊山野，赵民比王侯之富；牧羊坻上，苏卿佐帝相之忠。羊为畜类之属，于卦为兑，于辰为未。凡梦之为生男，为生贵女，为牧民之象。人君梦万羊，必得贤佐；士...
    """
    
    original_text: str = """#### 原文（source_text）

万羊大吉，牧羊山野，赵民比王侯之富；牧羊坻上，苏卿佐帝相之忠。羊为畜类之属，于卦为兑，于辰为未。凡梦之为生男，为生贵女，为牧民之象。人君梦万羊，必得贤佐；士庶梦万羊者，大贵。黄帝梦人执千钧之弩，驱羊万群。曰：千钧之弩，力也。驱羊万群，能牧民为善者也。得力牧。唐李德裕尝梦行晋山，有牧羊者数十辈迎拜，曰：此君所食万羊。后果为相。

#### 规范化释义（primary_lang_explained）

梦万羊，大吉。

历史典故：
- 牧羊山野：赵民比王侯之富
- 牧羊坻上：苏武佐帝相之忠

羊的象征：
- 于卦属兑
- 于辰属未
- 梦之为生男、生贵女、牧民之象

按身份分化：
- 人君梦万羊：必得贤佐
- 士庶梦万羊：大贵

典故：
- 黄帝梦执千钧弩驱羊万群：得力牧
- 李德裕梦牧羊者迎拜"此君所食万羊"：后果为相

#### 完整对等诠释（secondary_lang_full）

Dreaming of ten thousand sheep is greatly auspicious.

Historical allusions:
- Herding sheep in mountains: Wealth rivaling lords
- Herding sheep on hillocks: Su Wu's loyalty to the emperor

Symbolism of sheep:
- In trigrams: Dui (Lake)
- In earthly branches: Wei (Sheep)
- Signifies: bearing sons, noble daughters, shepherding the people

By status:
- Rulers dreaming of ten thousand sheep: Will obtain worthy ministers
- Commoners dreaming of ten thousand sheep: Great nobility

Allusions:
- Yellow Emperor dreamed of driving ten thousand sheep: Obtained Li Mu (Force Shepherd)
- Li Deyu dreamed shepherds bowed saying "This lord's ten thousand sheep": Later became prime minister

#### 核心要点

- 万羊=大贵=牧民之象
- 卦属兑，辰属未
- 人君→得贤佐，士庶→大贵
- 黄帝得力牧，李德裕为相

#### 叙事素材（narrative_snippets）

- `[ns_mlxj_v19_001]` `[trigger: 飞走梦象]` `[factor_trigger: dream_zhuquan AND lishi_huangdi AND dream_wanyang]` `[role: 飞走类]` 猪犬、黄帝典故、万羊等飞走梦象。 → 《梦林玄解·卷十九》#飞走"""
    normalized_text_zh: str = """"""
    subject: str = "1 万羊大吉（六畜类首条·完整精校）"
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
        l1_anchor="mlxj_v1.0.0_1_万羊大吉_六畜类首条_完整精校_001_L1",
    )
    version: str = "1.0.0"
