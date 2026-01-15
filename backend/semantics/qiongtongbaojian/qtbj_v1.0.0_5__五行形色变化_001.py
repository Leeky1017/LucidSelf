"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619703
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
    semantic_id="qtbj_v1.0.0_5__五行形色变化_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 5五行形色变化(SemanticEntry):
    """
    - **原文（source_text）**：
  推其形色，则水黑、火赤、木青、土黄，此正色也。及其变易，则不然。常以生旺从正色，死绝从母色，成形冠带从妻色，病败从鬼色，旺墓从子色。

- **分字分...
    """
    
    original_text: str = """- **原文（source_text）**：
  推其形色，则水黑、火赤、木青、土黄，此正色也。及其变易，则不然。常以生旺从正色，死绝从母色，成形冠带从妻色，病败从鬼色，旺墓从子色。

- **分字分词释义**：
  - **形色**：形态与颜色 / 外在表现 / 望气识人之法
  - **正色**：本来的颜色 / 五行固有之色 / 水黑火赤木青土黄金白
  - **变易**：变化更易 / 状态改变 / 随旺衰而变
  - **生旺**：长生、帝旺等旺相之地 / 气机强盛 / 正色显现
  - **死绝**：死、绝等衰败之地 / 气机衰竭 / 母色显现（求生）
  - **母色**：印星（生我者）的颜色 / 水生木则木死显水黑 / 求生之象
  - **妻色**：财星（我克者）的颜色 / 木克土则木冠带显土黄 / 克制之象
  - **鬼色**：官杀（克我者）的颜色 / 金克木则木病显金白 / 受克之象
  - **子色**：食伤（我生者）的颜色 / 木生火则木墓显火赤 / 泄秀之象

- **规范化释义（primary_lang_explained）**：
  推究五行的颜色，水黑、火红、木青、土黄（金白略），这是正色。但当五行发生变化时就不是这样了。通常生旺时显现正色，死绝时显现母色（印），成形冠带时显现妻色（财），病败时显现鬼色（官杀），旺墓时显现子色（食伤）。

- **完整对等诠释（secondary_lang_full）**：
  Deducing their forms and colors: Water is black, Fire is red, Wood is green/blue, Earth is yellow (Metal is white); these are the standard colors. However, when they change, it is different. Usually, in the Birth and Prosperous stages, they follow the Standard Color; in Death and Extinction stages, they follow the Mother's Color; in Formation and Cap and Sash stages, they follow the Wife's Color; in Sickness and Defeat stages, they follow the Ghost's Color; in Prosperity and Grave stages, they follow the Child's Color.

- **核心要点**：
  - 五行正色：水黑火赤木青土黄（金白）。
  - 气色随旺衰十二宫变化：
    - 生旺：本色
    - 死绝：母色（求生）
    - 冠带：妻色（克制）
    - 病败：鬼色（受克）
    - 旺墓：子色（泄秀）

- **详细解说**：
  这是极高阶的望气之法。正色是基础，变色反映了状态。例如木在死绝（如秋天）时，显现母色（水黑）是因为需要水生；在病败时显现鬼色（金白）是因为受克。这里的“妻、鬼、子、母”分别对应“财、官杀、食伤、印”。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_022]` `[trigger: 五行正色]` `[factor_trigger: wuxing_five_colors]` `[role: 主干]` 水黑、火赤、木青、土黄、金白，此正色也。 → 《穷通宝鉴·五行总论》#1.5
  - `[ns_qttbj_023]` `[trigger: 生旺气色]` `[factor_trigger: shier_shengwang]` `[role: 条件分支]` 生旺从正色，气色鲜明。 → 《穷通宝鉴·五行总论》#1.5
  - `[ns_qttbj_024]` `[trigger: 死绝气色]` `[factor_trigger: shier_sijue]` `[role: 条件分支]` 死绝从母色，求生于印。 → 《穷通宝鉴·五行总论》#1.5
  - `[ns_qttbj_025]` `[trigger: 冠带气色]` `[factor_trigger: state_color_mutation AND shishen_wealth]` `[role: 条件分支]` 成形冠带从妻色，财星显现。 → 《穷通宝鉴·五行总论》#1.5
  - `[ns_qttbj_026]` `[trigger: 病败气色]` `[factor_trigger: state_color_mutation AND shishen_officer]` `[role: 条件分支]` 病败从鬼色，受克于官杀。 → 《穷通宝鉴·五行总论》#1.5
  - `[ns_qttbj_027]` `[trigger: 旺墓气色]` `[factor_trigger: state_color_mutation AND shishen_output]` `[role: 条件分支]` 旺墓从子色，泄秀于食伤。 → 《穷通宝鉴·五行总论》#1.5"""
    normalized_text_zh: str = """"""
    subject: str = "5. 五行形色变化"
    factor_refs: list = ['wuxing_standard_color', 'color_resource_star', 'color_wealth_star', 'color_officer_killing_star', 'color_output_star']
    
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
        book_id="qiongtongbaojian",
        chapter="",
        l1_anchor="qtbj_v1.0.0_5__五行形色变化_001_L1",
    )
    version: str = "1.0.0"
