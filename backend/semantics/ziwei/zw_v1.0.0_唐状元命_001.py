"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699857
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
    semantic_id="zw_v1.0.0_唐状元命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 唐状元命(SemanticEntry):
    """
    - 分字分词释义：

  - **紫微守命**：紫微帝星坐守命宫，主最高层尊贵。
  - **龙池凤阁**：象征文学、科第与宫廷礼乐的吉星组合。
  - **左辅右彼**：拱卫命宫或君星的两颗辅彼星，...
    """
    
    original_text: str = """- 分字分词释义：

  - **紫微守命**：紫微帝星坐守命宫，主最高层尊贵。
  - **龙池凤阁**：象征文学、科第与宫廷礼乐的吉星组合。
  - **左辅右彼**：拱卫命宫或君星的两颗辅彼星，主贵人与辅佐。
  - **天相朝垣得紫微**：天相朝拱官垣并得紫微照拂，主臣位尊崇。
  - **君臣庆会**：君星与臣星同会且辅彼聚拱，主居权力中枢。
  - **富贵必矣**：富贵确定无疑的命局断语。
  - **阴男火六局**：唐状元命盘的五行局数，火六局主明亮状元。

- **原文（source_text）**：  
  唐状元命。阴男火六局。紫微守命，龙池凤阁，左辅右弼，朝垣天相得紫微，是为君臣庆会，其富贵必矣。

- **规范化释义（primary_lang_explained）**：  
  唐状元命为阴男火六局，「紫微守命」表最高主星坐命；「龙池凤阁」「左辅右弼」皆为文采与近侍之吉星，再加天相朝垣并得紫微，是经典「君臣庆会」格局——主君星与臣星同会，辅弼齐聚，一般解释为上承天恩、下得群臣扶持。  
  在科举语境中，「状元」指最高科名，配合龙池凤阁与左辅右弼，多主文章冠绝一时，入朝为高阶重臣。原文直接断言「其富贵必矣」，说明此格不仅仅是清高名望，更有实在权位与俸禄，属典型的帝国核心文官命局。

- **完整对等诠释（secondary_lang_full）**：  
  This "Tang Zhuangyuan" chart belongs to a Yin Fire native in the Sixth Configuration. Zi Wei sits in the Life palace; Long Chi and Feng Ge, the Dragon‑Pool and Phoenix‑Pavilion stars, attend; Zuo Fu and You Bi flank; and Tian Xiang faces the court together with Zi Wei. This array crystallises the "ruler‑minister celebration" pattern, where sovereign and ministerial stars converge, supported by literary and attendant stars.  
  In the examination context, "Zhuangyuan" marks the very top graduate. Combined with Dragon‑Phoenix imagery and Left‑Right Assistants, it signals outstanding literary talent that earns a place among the empire’s highest officials. The text simply states that "his wealth and rank are certain," framing this as a civil‑service destiny seated near the centre of power rather than at its periphery.

- **核心要点**：  
  1. 紫微守命配龙池凤阁与左右辅弼，是极强的君臣庆会格。  
  2. 以状元之名凸显其在科第与文章上的拔尖地位。  
  3. 命例体现「深植帝国中枢的高阶文官」路径，富贵稳固。"""
    normalized_text_zh: str = """"""
    subject: str = "唐状元命"
    factor_refs: list = ['star_ziwei_shouming', 'star_longchi_fengge', 'star_zuofu_youbi', 'pattern_tianxiang_ziwei', 'pattern_junchen_qinghui', 'result_fugui_biyi']
    
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
        l1_anchor="zw_v1.0.0_唐状元命_001_L1",
    )
    version: str = "1.0.0"
