"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523827
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
    semantic_id="zpzq_v1.0.0_今人不知命理_见夏水冬火便为之弱_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 今人不知命理见夏水冬火便为之弱(SemanticEntry):
    """
    - **原文（source_text）**：
  今人不知命理，见夏水冬火，不问有无通根，便为之弱。更有阳干逢库，如壬逢辰、丙坐戌之类，不以为水火通根身库，甚至求刑冲开之。此种谬论，必宜一切扫除也。
...
    """
    
    original_text: str = """- **原文（source_text）**：
  今人不知命理，见夏水冬火，不问有无通根，便为之弱。更有阳干逢库，如壬逢辰、丙坐戌之类，不以为水火通根身库，甚至求刑冲开之。此种谬论，必宜一切扫除也。

- 原注（原文注解）：
  　　此段批判坊间两大谬论：一是"见夏水冬火就断弱"（不看通根），二是"逢库必冲"（不知库即是根），强调必须依据"四柱有根"原则活看旺衰，扫除机械论命的陋习。

- 分字分词释义：
  - 今人不知命理：现在很多人不懂命理的真正道理。
  - 见夏水冬火，不问有无通根，便为之弱：一看到夏天的水、冬天的火，不管有没有通根，就断定为弱。
  - 更有阳干逢库：更有一种情况，阳干遇到墓库。
  - 如壬逢辰、丙坐戌之类：例如壬水遇到辰土（水之墓库）、丙火坐在戌土（火之墓库）。
  - 不以为水火通根身库：不把这种情况看作是水火通根于身库。
  - 甚至求刑冲开之：甚至还要去找刑冲来"开库"。
  - 此种谬论，必宜一切扫除也：这种错误的理论，必须全部扫除。

- 核心要点：
  - **批判机械论旺衰**：不可见夏水冬火就断弱，需看通根与否。
  - **库即是根**：阳干逢库应视为通根身库，而非必须刑冲开库。
  - **扫除谬论**：坊间"逢库必冲"之说必须扫除。

- **规范化释义（primary_lang_explained）**：
 - 现在很多人不懂命理的真正道理，一看到夏天的水、冬天的火，不管有没有通根，就断定为弱。这是典型的机械论命，只看月令不看通根。更有一种情况，阳干遇到墓库，例如壬水遇到辰土（水之墓库）、丙火坐在戌土（火之墓库），很多人不把这种情况看作是水火通根于身库，甚至还要去找刑冲来"开库"，认为不开库就用不上。这种错误的理论，必须全部扫除。

- **完整对等诠释（secondary_lang_full）**：  
  This short paragraph applies the "four pillars have roots" principle to two widespread errors. First, many readers see Water in a summer chart or Fire in a winter chart and immediately label it weak, without asking whether it is rooted elsewhere; this is season‑only thinking. Second, when a yang stem sits in its own tomb—for example Ren Water with Chen, or Bing Fire on Xu—they fail to recognise this as the Day Master being rooted in a storehouse, and even go looking for clashes and punishments to "open the tomb". Both habits, the author insists, must be swept away. Summer Water and winter Fire are only genuinely weak when they both lose the Season and also have no supporting roots in any branch. Likewise, a yang Day Master that sits in its own store is not something that always needs to be broken open; more often it is the very place where its life‑force is conserved.

- 详细解说：
  - 本段是对前两节理论的实战应用，直接批判当时（以及现在）最常见的两种机械论命错误。
  - "夏水冬火便为弱"是月令决定论的典型表现，忽视了四柱通根的根本作用。
  - "逢库必冲"是对墓库理论的严重误解，不知库本身就是根，盲目追求刑冲开库反而破坏格局。

- 核心要点：
  - 判断旺衰必须综合月令与通根，不能只看月令。
  - 库是根的一种，阳干逢库为通根身库，无需刑冲开之。
  - 刑冲开库只在特定情况下（如要取库中财官）才需要，不能一概而论。

- 应用推演：
  1) 见夏水冬火，先不要急于断弱，检查四柱地支有无通根。
  2) 若有亥子、申子辰等水根，或寅午戌、巳午等火根，则不弱。
  3) 若日主坐库（如壬辰日、丙戌日），视为通根身库，身不弱。
  4) 只有在月令失时且四柱无根的情况下，才能断为真弱。
  5) 刑冲开库不是必需，除非要取库中财官，否则不宜刑冲。

- 反例与边界：
  - 机械论"夏水必弱、冬火必弱"，是最普遍的错误，本段明确批判。
  - 盲目追求"逢库必冲"，不知库本身就是根，反而破坏格局。
  - 把"刑冲开库"当作万能法则，不分具体情况，导致误判。

- 小例（示意）：
  - 壬水生夏月（失令），但日坐辰库（通根身库）、年支亥水（长生），则壬水不弱，无需刑冲开库。
  - 丙火生冬月（失令），但日坐戌库（通根身库）、时支午火（羊刃），则丙火不弱，强求丑冲或辰冲反破格。

- 校勘与字词辨析：
  - "今人不知命理"：作者对当时命理界机械论命的批判，至今仍有现实意义。
  - "通根身库"：强调库是日主的根气所在，而非需要打开的"宝库"。
  - "此种谬论，必宜一切扫除也"：语气坚决，表明作者对机械论命的强烈反对。


- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_256]` `[trigger: 命理要义]` `[factor_trigger: benjie_hexin_mingli AND lunshu_yaodian]` `[role: 主干]` 本节核心命理论述。 → 《子平真诠》#第49节
  - `[ns_zpzy_257]` `[trigger: 实践要领]` `[factor_trigger: duanming_shijian AND yaoling_zonghe]` `[role: 主干]` 断命实践要领。 → 《子平真诠》#上卷
  - `[ns_zpzy_258]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_259]` `[trigger: 格成格破]` `[factor_trigger: (gecheng=true AND result=ji) OR (gepo=true AND result=xiong)]` `[role: 主干]` 格成则吉，格破则凶。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "今人不知命理，见夏水冬火便为之弱"
    factor_refs: list = ['xiashui_donghuo', 'yanggan_fengku', 'xingchong_kaiku', 'jixie_lunming', 'tonggen_shenku']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_今人不知命理_见夏水冬火便为之弱_001_L1",
    )
    version: str = "1.0.0"
