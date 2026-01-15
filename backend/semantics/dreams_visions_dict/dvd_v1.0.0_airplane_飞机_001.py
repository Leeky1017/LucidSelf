"""
Auto-generated semantic module for dreams_visions_dict
Generated at: 2025-12-05T13:30:20.439591
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
    semantic_id="dvd_v1.0.0_airplane_飞机_001",
    book_id="dreams_visions_dict",
    engine_id="dream"
)
class Airplane飞机(SemanticEntry):
    """
    ### Source Text

> **General Meaning**: The vehicle for your ministry. It will be fast, effective an...
    """
    
    original_text: str = """### Source Text

> **General Meaning**: The vehicle for your ministry. It will be fast, effective and will reach new heights.

**Dreams - Positive**: Dreaming of a large jumbo jet could speak of a public ministry or expansion into something more public. If you are dreaming of flying the plane, this could speak of a promotion.

**Dreams - Negative**: If you have a fear of flying, then dreaming of being in a plane could represent having to face your fears. If you dream that you are flying this plane but that you are not meant to, that someone else should be flying it, this could indicate that you are taking charge of things that are not yours to take charge of.

**Visions - Positive**: I have come to see airplanes as a representation of ministry. The larger the plane, the larger the ministry. A fighter plane speaks of a ministry of intercession and warfare—surveying the land on behalf of the Body of Christ and overcoming the enemy.

**Scripture**: Jeremiah 49:22 - "Behold, he shall come up and fly as the eagle, and spread his wings over Bozrah."

**See also**: Car, Vehicles

### Key Terms

| Term | Definition | Significance |
|------|------------|--------------|
| Airplane | Ministry vehicle | Fast, effective, reaching heights |
| Jumbo jet | Large public ministry | Expansion, many helpers needed |
| Fighter plane | Warfare/intercession ministry | Aggressive, overcoming enemy |

### English Paraphrase

Airplanes in dreams represent your ministry vehicle—fast, effective, reaching new heights. The size indicates ministry scope: jumbo jet = large public ministry requiring many helpers; fighter plane = warfare/intercession ministry, aggressive and enemy-defeating. Flying the plane yourself suggests promotion or leadership. But if you're flying when someone else should be, you're taking control of things not yours—putting yourself in God's place. Fear of flying in dreams may indicate facing fears in real life.

### Chinese Interpretation（完整对等诠释）

梦中的飞机代表你的事工载具——快速、有效、达到新高度。大小指示事工范围：大型客机=需要许多帮手的大型公开事工；战斗机=争战/代祷事工，具攻击性且能胜过仇敌。自己驾驶飞机暗示晋升或领导。但如果你在驾驶而应该是别人驾驶，表示你在掌控不属于你的事——把自己放在神的位置。梦中怕飞可能表示现实生活中需要面对恐惧。

### Core Points

- 飞机 = 事工载具（vs Car = 个人呼召）
- 飞机大小 = 事工规模
- 大型客机 = 公开事工、需要团队
- 战斗机 = 争战代祷事工
- 驾驶 = 领导/掌控
- 不该驾驶却驾驶 = 越权/抢夺神的位置

### Narrative Snippets

- `[ns_dav_a004]` `[trigger: 梦飞机]` `[factor_trigger: dream_symbol_airplane]` `[role: 主干]` Airplane = ministry vehicle—fast, effective, reaching new heights. Size indicates ministry scope. → Dreams Dictionary #Airplane
- `[ns_dav_a005]` `[trigger: 飞机类型]` `[factor_trigger: dream_symbol_airplane AND airplane_size]` `[role: 主干依赖]` Jumbo jet = large public ministry; Fighter plane = warfare/intercession ministry. → Dreams Dictionary #Airplane
- `[ns_dav_a006]` `[trigger: 驾驶飞机]` `[factor_trigger: dream_symbol_airplane AND dream_driving AND pilot_role]` `[role: 条件分支]` Flying plane yourself = promotion. Flying when shouldn't = taking control not yours. → Dreams Dictionary #Airplane"""
    normalized_text_zh: str = """"""
    subject: str = "Airplane 飞机"
    factor_refs: list = ['dream_symbol_airplane', 'dream_symbol_fighter_plane', 'action_flying']
    
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
        book_id="dreams_visions_dict",
        chapter="",
        l1_anchor="dvd_v1.0.0_airplane_飞机_001_L1",
    )
    version: str = "1.0.0"
