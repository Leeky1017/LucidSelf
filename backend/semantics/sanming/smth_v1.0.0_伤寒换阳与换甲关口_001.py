"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264300
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
    semantic_id="smth_v1.0.0_伤寒换阳与换甲关口_001",
    book_id="sanming",
    engine_id="bazi"
)
class 伤寒换阳与换甲关口(SemanticEntry):
    """
    - **原文（source_text）**：  
  古语云：伤寒换阳，行运换甲。换过是人，换不过是鬼。假如甲戌接癸亥，是火土接水，丑交寅，辰交巳，未交申，戍交亥，东西南北，四方转角，谓栘根接木。更遇...
    """
    
    original_text: str = """- **原文（source_text）**：  
  古语云：伤寒换阳，行运换甲。换过是人，换不过是鬼。假如甲戌接癸亥，是火土接水，丑交寅，辰交巳，未交申，戍交亥，东西南北，四方转角，谓栘根接木。更遇换甲格，凶者多死，善者亦灾，老人大忌，后生差慢。

- **分字分词释义**：
  - **伤寒换阳**：医家以重病“换阳”为极险之关，喻运程中的生死转折点。
  - **行运换甲**：行到某步大运，日主所依之干气根本更换，好比根气被替换。
  - **换过是人，换不过是鬼**：顺利度过此关则得生机，过不去则有重祸甚至夭亡之象。
  - **栘根接木**：树根横移再接新木，比喻运方突变、根基移动后再行接运。
  - **老人大忌，后生差慢**：年老体弱者最忌骤变大运，后生元气尚足，虽有损亦较缓和。

- **规范化释义（primary_lang_explained）**：  
  作者以“伤寒换阳”的重病关口比喻行运中的“换甲”：有些大运交界不只是十神喜忌的小幅变化，而是运程主气与根气的整体更换。所谓“换过是人，换不过是鬼”，就是在强调这一换甲之处往往关乎生死祸福。文中举“甲戌接癸亥”为例，说明从火土方的大运忽然转入北方水运，东西南北、四方转角，如同树根横向延展，再去接另一株树，这就是“栘根接木”之象。若命局根基深厚、调候得宜，则虽有剧变仍可逢凶化吉；若原局气弱又再逢此等换甲格，则凶者多死，善者亦灾，尤以年老体弱者为最忌，而后生因元气尚存，虽有损伤，尚可缓行承受。

- **完整对等诠释（secondary_lang_full）**：  
  The text uses a medical image to illustrate a critical turning point in fate: just as a patient suffering from severe cold-induced illness may undergo a highly risky "yang change" in order to survive, so too a person's major luck can reach a phase where the very root qi represented by the stem is replaced. This is called "changing Jia" in luck. The saying "if the change succeeds, one remains human; if it fails, one becomes a ghost" underlines that such transitions may correspond to life‑or‑death crises. The example of Jia‑Xu luck followed by Gui‑Hai indicates a sharp shift from a Fire‑Earth sector to a Water sector, described as roots stretching to another corner of the field and grafting anew—"shifting roots to graft wood." If the natal chart has solid roots and proper adjustment of qi, even such a drastic change can lead to renewed growth; but if the chart is weak and poorly balanced, a change‑Jia configuration can easily bring serious illness, calamity, or even death. Elderly natives are said to be particularly vulnerable, whereas younger people, having more vital qi, can endure the shock somewhat better, though not without trial.

- **核心要点**：
  - “换甲”象征大运主气与根气的根本转换，而非一般小变。
  - 换甲之关如同重病“换阳”，成败关乎祸福，轻则大病大灾，重则夭亡。
  - 火土方与水方等运方剧烈互换时，对身弱老年命局尤为不利。

- **详细解说**：  
  在实际推运中，所谓“换甲格”多出现在大运交界，并且伴随用神方位的突变：例如命局以火土为用，前一阶段大运又在火土旺地，忽然交入水方，若命局缺乏足够木火调候，这一步水运既冲击原有格局，又难在新的结构中找到承接点，就会表现为事业格局剧烈转向、家庭结构大变，甚至身体遭遇重病或大手术。判断此类关口时，一方面要看换运前后的五行方位跨度有多大，属于“轻转弯”还是“急拐弯”；另一方面要结合命局本身根气深浅、救应多少，以及年龄与身体状况，分清“险而可渡”与“险而难渡”的不同层级。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_069]` `[trigger: 伤寒换阳]` `[factor_trigger: shanghan_huanyang AND xingyun_huanjia]` `[role: 主干]` 古语云：伤寒换阳，行运换甲。换过是人，换不过是鬼。 → 《三命通会》卷十#伤寒换阳与换甲关口
  - `[ns_smth_10_070]` `[trigger: 剁根接木]` `[factor_trigger: yigen_jiemu AND sifang_zhuanjiao]` `[role: 主干依赖]` 东西南北，四方转角，谓剁根接木。 → 《三命通会》卷十#伤寒换阳与换甲关口
  - `[ns_smth_10_071]` `[trigger: 凶者多死]` `[factor_trigger: xiongzhe_duosi AND shanzhe_yizai]` `[role: 条件分支]` 更遇换甲格，凶者多死，善者亦灾。 → 《三命通会》卷十#伤寒换阳与换甲关口
  - `[ns_smth_10_072]` `[trigger: 老人大忌]` `[factor_trigger: laoren_daji AND housheng_chaman]` `[role: 总结]` 老人大忌，后生差慢。 → 《三命通会》卷十#伤寒换阳与换甲关口"""
    normalized_text_zh: str = """"""
    subject: str = "伤寒换阳与换甲关口"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        book_id="sanming",
        chapter="",
        l1_anchor="smth_v1.0.0_伤寒换阳与换甲关口_001_L1",
    )
    version: str = "1.0.0"
