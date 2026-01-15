"""
Auto-generated semantic module for dts
Generated at: 2025-12-05T13:30:18.997588
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
    semantic_id="dts_v1.0.0_吉神太露_起争夺之风_凶物深藏_成养虎之患_001",
    book_id="dts",
    engine_id="bazi"
)
class 吉神太露起争夺之风凶物深藏成养虎之患(SemanticEntry):
    """
    - **原文（source_text）**：
  吉神太露，起争夺之风。凶物深藏，成养虎之患。

- 原注（原文注解）：
  　　局中所喜之神，透于天干，岁运伤之；局中所忌之神，伏于地支，岁运扶之，皆...
    """
    
    original_text: str = """- **原文（source_text）**：
  吉神太露，起争夺之风。凶物深藏，成养虎之患。

- 原注（原文注解）：
  　　局中所喜之神，透于天干，岁运伤之；局中所忌之神，伏于地支，岁运扶之，皆为祸患。故暗用吉神则吉，如明露忌神，制化得所者亦吉。

- **规范化释义（primary_lang_explained）**：
  喜神宜藏而用，忌神宜制而不露。露喜遭攻、藏忌遇扶，皆生患。

- 分字分词释义：
  - 太露：过度外显、易受攻伐。
  - 深藏：伏而不显、但遇扶即起。
  - 争夺之风：争竞之象由此而生。
  - 养虎之患：隐伏凶物遇助而成大害。


- **L2-术语对齐（Term Glossary）**:

| 中文术语 | 英文术语 | 中文定义 | 英文定义 | factor_id | status |
|---------|---------|---------|---------|-----------|--------|
| 隐显 | Hidden-Visible (Yin-Xian) | 藏与露 | Concealment and exposure | yinxian | existing |
| 吉神太露 | Auspicious God Too Exposed | 喜用外露 | Good God exposed | jishen_tailu | new_candidate |
| 凶物深藏 | Malicious Thing Deep Hidden | 忌神深伏 | Bad Thing hidden deep | xiongwu_shencang | new_candidate |
| 争夺之风 | Wind of Competition | 争夺劫掠 | Competition and robbery | zhengduo_zhifeng | new_candidate |
| 养虎之患 | Trouble of Rearing Tiger | 隐患无穷 | Hidden danger grows | yanghu_zhihuan | new_candidate |
| 暗用 | Use Secretly (An-Yong) | 暗中取用 | Use discreetly | anyong | new_candidate |


- **次语种完整诠释（secondary_lang_full）**:  
  Yin-Xian (Hidden-Visible) theory: Auspicious Gods (Ji-Shen) exposed too much (Tai-Lu) invite competition (Zheng-Duo). Malicious things (Xiong-Wu) hidden deep (Shen-Cang) become "Rearing a Tiger" (Yang-Hu). Best to use Auspicious Gods secretly (An-Yong) or control exposed Malicious Gods immediately."""
    normalized_text_zh: str = """"""
    subject: str = "吉神太露，起争夺之风，凶物深藏，成养虎之患。"
    factor_refs: list = []
    
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
        l1_anchor="dts_v1.0.0_吉神太露_起争夺之风_凶物深藏_成养虎之患_001_L1",
    )
    version: str = "1.0.0"
