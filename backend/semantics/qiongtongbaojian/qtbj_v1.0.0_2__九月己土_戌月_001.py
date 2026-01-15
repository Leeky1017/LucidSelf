"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597126
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
    semantic_id="qtbj_v1.0.0_2__九月己土_戌月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2九月己土戌月(SemanticEntry):
    """
    - **原文（source_text）**：
  总之，三秋己土，先癸后丙，取辛辅癸。九月土盛，宜甲木疏之，余皆酌用。
  或支成火局，无水救，乃大奸大恶之徒。
  
  勾陈全备润下，劳碌奔波之客。...
    """
    
    original_text: str = """- **原文（source_text）**：
  总之，三秋己土，先癸后丙，取辛辅癸。九月土盛，宜甲木疏之，余皆酌用。
  或支成火局，无水救，乃大奸大恶之徒。
  
  勾陈全备润下，劳碌奔波之客。土凝水竭，离乡背井之流。
  勾陈得位会才官，无克无破必然端，甲子北方寅卯木，管教环拱戴金冠。戊己喜亥卯未为官，申子辰为才，忌刑克杀害。

- **分字分词释义**：
  - **土盛宜甲**：土旺盛宜用甲疏 / 戌月特点 / 用神
  - **大奸大恶**：极大奸诈恶毒 / 火局无水 / 凶象
  - **勾陈**：戊己土的别名 / 北斗星名 / 术语
  - **润下**：水润下流 / 水局 / 凶象
  - **劳碌奔波**：辛劳奔波 / 财多身弱 / 凶象
  - **土凝水竭**：土冻结水枯竭 / 冬土 / 凶象
  - **离乡背井**：离开故乡 / 无依 / 凶象
  - **戴金冠**：佩戴金冠 / 做官 / 吉象

- **规范化释义（primary_lang_explained）**：
  总之，三秋己土，先用癸水后用丙火，取辛金辅助癸水。九月（戌月）土盛（土当令），适宜用甲木疏通它，其余的根据情况斟酌使用。
  如果地支合成火局，没有水救应（润燥），是大奸大恶之徒（燥土脆金，无情）。
  
  （诗云）勾陈（戊己土）全备润下（水局），是劳碌奔波的客人（财多身弱）。土凝水竭（冻土无水？或土重克水？），是离乡背井之流。
  勾陈得位（得地）会合财官，无克无破必然端正，走甲子北方运或寅卯木运，管教（保证）环拱戴金冠（做官）。戊己土喜亥卯未为官（木局），申子辰为财（水局），忌讳刑克杀害。

- **完整对等诠释（secondary_lang_full）**：
  In summary, for Autumn Ji Earth, first Gui then Bing, take Xin to assist Gui. In the 9th Month (Dog), Earth is prosperous; use Jia to dredge.
  If branches form a Fire Frame without Water to save, one is a greatly treacherous and evil person.
  (Poem) If Gouchen (Earth) fully encounters Runxia (Water Frame), one is a toil-worn traveler. If Earth freezes and Water is exhausted, one leaves home.
  If Gouchen is positioned well and meets Wealth/Officer, without clash/break, one is upright. Luck in Jia-Zi North or Yin-Mao Wood ensures wearing a gold crown (official). Wu/Ji like Hai-Mao-Wei as Officer, Shen-Zi-Chen as Wealth; dread punishment/clash.

- **核心要点**：
  - **戌月专用**：土盛用甲。
  - **燥土之恶**：火局无水，大奸大恶。
  - **润下**：水多土流，劳碌。

- **详细解说**：
  - 戌月己土，如同辰月，土厚。
  - 区别在于戌月土燥，故除了疏土（甲），更需润土（癸）。
  - “大奸大恶”：燥土不生养，且火土势众，性格偏激无情。"""
    normalized_text_zh: str = """"""
    subject: str = "2. 九月己土（戌月）"
    factor_refs: list = ['gouchen', 'runxia', 'great_evil']
    
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
        l1_anchor="qtbj_v1.0.0_2__九月己土_戌月_001_L1",
    )
    version: str = "1.0.0"
