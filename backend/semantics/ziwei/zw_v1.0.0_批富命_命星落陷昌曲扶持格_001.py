"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.739988
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
    semantic_id="zw_v1.0.0_批富命_命星落陷昌曲扶持格_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 批富命命星落陷昌曲扶持格(SemanticEntry):
    """
    - 分字分词释义：

  - **命星落陷**：命宫主星落陷（弱地无光），按理难成格局。
  - **昌曲扶持**：文昌文曲在三合扶持命宫，化弱为秀。
  - **衰中带旺**：衰弱中带有旺势，浊处又...
    """
    
    original_text: str = """- 分字分词释义：

  - **命星落陷**：命宫主星落陷（弱地无光），按理难成格局。
  - **昌曲扶持**：文昌文曲在三合扶持命宫，化弱为秀。
  - **衰中带旺**：衰弱中带有旺势，浊处又还清。
  - **金谷**：石崇金谷园，巨富典故，积玉堆金石崇金谷。
  - **萧曹**：萧何曹参由椽吏做到丞相，喻落陷得扶亦成大器。
  - **为人秀气丰姿**：落陷得昌曲扶持之人外表秀气、清雅心灵。
  - **富比春申**：功名不显但巨富，如战国春申君。

- **原文（source_text）**：  
  又命星直为落陷，论来弱地无光。于中三合昌曲，左右扶持的当。正是衰中欣带旺，浊处又还清。乃主为人秀气丰姿，清雅心灵，肯收意马读遗经。端然成大用，可以播芳名。日月虽然返背，权禄才福荣华，不然肯事小材成。萧曹由椽吏，做到汉皇丞。纵把功名敝踪，也应积玉堆金石，崇金谷富春申。五行皆具备，财福自然兴。命主某星某宿，主星明白清新。只坐某星在身宫，安身傍贵不为宁。据理六亲冰炭，衡阳鴈阵成群。佳人鸡警近贤能，四宫其星守，三四好麒麟。假如限行某星，劫空忌耗之乡，正如月色带浮云。有妨人玩赏，不见广寒明。

- **规范化释义（primary_lang_explained）**：  
  此为批断「命星落陷、得昌曲左右扶持」富命的标准套语。核心逻辑：命星虽落陷（弱地无光），但三合有文昌文曲、左右辅弼扶持的当，则「衰中欣带旺、浊处又还清」。此格主为人秀气丰姿、清雅心灵、肯读书收心，虽功名不显但「积玉堆金石、崇金谷富春申」（巨富）。套语以萧何曹参由椽吏做到丞相为喻，说明落陷得扶亦可成大器。

- **完整对等诠释（secondary_lang_full）**：  
  This template interprets the "Life Star in Detriment with Chang Qu Support" wealth pattern. Core logic: though Life star falls into detriment (weak position without brilliance), with Wen Chang, Wen Qu, Zuo Fu and You Bi in supportive configuration, it becomes "joy emerging from decline, clarity from murky". This pattern indicates elegant appearance, refined spirit, willing to study and cultivate. Though official fame may not manifest, one achieves "piling jade and gold, rivaling Jin Gu and Chun Shen" (immense wealth). The template uses Xiao He and Cao Can rising from clerks to prime ministers as analogy.

- **核心要点**：  
  1. 格局特点：命星落陷，得昌曲左右扶持。  
  2. 转化逻辑：衰中带旺、浊处还清。  
  3. 富命特征：功名不显但积玉堆金、富比金谷春申。"""
    normalized_text_zh: str = """"""
    subject: str = "批富命·命星落陷昌曲扶持格"
    factor_refs: list = ['star_mingxing_luoxian', 'pattern_changqu_fuchi', 'mech_shuaizhong_daiwang', 'allusion_jingu', 'allusion_xiaocao', 'source_ref', 'rel_vol7_14_001', 'star_mingxing_luoxian', 'rel_vol7_14_002', 'mech_shuaizhong_daiwang', 'rel_vol7_14_003', 'result_luoxian_fuming', 'evi_vol7_14_001', 'rule_luoxian_changqu_zhuanji', 'evi_vol7_14_002', 'allusion_jingu', 'rule_jingu_chunshen_jufu', 'evi_vol7_14_003', 'allusion_xiaocao', 'rule_xiaocao_chenggong', 'concept_decline_to_prosperity', 'concept_elegant_spirit', 'concept_jingu_wealth']
    
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
        l1_anchor="zw_v1.0.0_批富命_命星落陷昌曲扶持格_001_L1",
    )
    version: str = "1.0.0"
