"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.654399
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
    semantic_id="zw_v1.0.0_庙旺利益平和落陷表_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 庙旺利益平和落陷表(SemanticEntry):
    """
    - 分字分词释义：

  - **庙旺**：星曜在该宫位力量最强。
  - **得地**：星曜在该宫位力量次强。
  - **平和**：星曜在该宫位力量一般。
  - **落陷**：星曜在该宫位力量最...
    """
    
    original_text: str = """- 分字分词释义：

  - **庙旺**：星曜在该宫位力量最强。
  - **得地**：星曜在该宫位力量次强。
  - **平和**：星曜在该宫位力量一般。
  - **落陷**：星曜在该宫位力量最弱。
  - **利益**：星曜在该宫位主吉利。
  - **十二宫星曜**：各宫位适合的星曜配置。

#### 十二宫星曜庙旺表（简表）：

| 宫位 | 庙旺星 | 得地星 | 平和星 | 落陷星 |
|------|--------|--------|--------|--------|
| 子 | 破曲梁存阴相府 | 机同武巨贪羊昌 | 紫贞日 | 火铃 |
| 丑 | 紫相杀昌府月曲武羊 | 梁破火 | 贞贪同日巨 | 机 |
| 寅 | 紫相巨府梁杀禄马日 | 机武破存同曲 | 贪贞陀昌 | 月 |
| ... | ... | ... | ... | ... |

（详细表格见原文）

#### 完整对等诠释（secondary_lang_full·44庙旺落陷表）：

  The Dignity Table (Miao Wang Li Yi Ping He Luo Xian Biao) grades each star's strength according to the palace it occupies. Temple (Miao) and Prosperous (Wang) placements indicate maximum power; Favorable (Li) and Beneficial (Yi) indicate strong support; Balanced (Ping) and Harmonious (He) indicate neutral ground; Fallen (Luo) and Trapped (Xian) indicate weakness and difficulty. For instance, in Zi palace, Pojun, Wuqu, Tianliang, Lucun, Taiyin, Tianxiang, and Tianfu all enjoy temple dignity, while Huoxing and Lingxing are fallen. Each of the twelve palaces has its own roster. Consulting this table before interpretation ensures the astrologer correctly weighs how much a given star can deliver on its promises—or how much its deficits will drag on the native's potential."""
    normalized_text_zh: str = """"""
    subject: str = "庙旺利益平和落陷表"
    factor_refs: list = ['state_miaowang', 'state_dedi', 'state_pinghe', 'state_luoxian']
    
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
        l1_anchor="zw_v1.0.0_庙旺利益平和落陷表_001_L1",
    )
    version: str = "1.0.0"
