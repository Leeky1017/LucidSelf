"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264349
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
    semantic_id="smth_v1.0.0_太岁克战与五行救应_001",
    book_id="sanming",
    engine_id="bazi"
)
class 太岁克战与五行救应(SemanticEntry):
    """
    - **原文（source_text）**：  
  何则？下凌其上逆也，其凶决不能免。若五行有救，四柱有情，如甲日克戊年，四柱元有庚申金，或大运中亦有将甲木制伏纯粹，不能克戊土，为有救。经云：戊巳愁...
    """
    
    original_text: str = """- **原文（source_text）**：  
  何则？下凌其上逆也，其凶决不能免。若五行有救，四柱有情，如甲日克戊年，四柱元有庚申金，或大运中亦有将甲木制伏纯粹，不能克戊土，为有救。经云：戊巳愁逢甲乙，干头须要庚辛是也。如大运并四柱中有一癸字，与戊相合，为有情，经云：壬以癸妹配戊，凶为吉兆是也。若二字俱全，其年凶反为吉；有一字者凶半，二字俱无，凶莫能解。经云：五行有救，其年反必为财。四柱无情，故论名为克岁是也。

- **规范化释义（primary_lang_explained）**：  
  承上文“日犯岁君”之凶，作者解释其所以然：因为“下凌其上逆”，故“其凶决不能免”。但若五行有救、四柱有情，则可转危为安。以甲日克戊年为例，若命局或大运中有庚申金，能够制伏甲木，使其不能实质克戊土，则构成救应；古语“戊巳愁逢甲乙，干头须要庚辛”即指此意。又如大运或四柱中有癸水与戊土相合，形成“壬以癸妹配戊”的有情结构，则原本的凶象可部分或全部化解：二者俱全则凶反成吉，仅有其一则凶减半，两者皆无则“凶莫能解”。因此，经曰“五行有救，其年反必为财”，若四柱无情，则只能论为真克岁。

- **完整对等诠释（secondary_lang_full）**：  
  Continuing from the notion that "the day offends the year lord" is inherently severe because it represents inferiors rebelling against superiors, the author explains that such configurations are not absolutely fatal: they may be mitigated when the Five Elements supply rescue and when the natal chart shows harmonious relationships. In the case of Jia day attacking Wu year, if the chart or major luck contains Geng‑Shen Metal that strongly controls Jia Wood, the Day Stem loses the power to injure Wu Earth, and the situation is "rescued." The line "Wu‑Si fears encountering Jia or Yi; the stem must have Geng or Xin" summarizes this requirement. Similarly, if Gui Water appears to combine with Wu Earth—"Ren marries off his Gui sister to Wu"—the hostile relationship is softened into an affectionate bond, turning danger into opportunity: with both Metal control and Water combination present, a potentially disastrous year may become auspicious; with only one of them, the misfortune is halved; with neither, disaster is hard to avert. Thus the saying "when the Five Elements provide rescue, that year actually turns into wealth" contrasts sharply with the unmitigated case called "truly attacking the year."

- **核心要点**：
  - 日犯岁君本属严重逆叛，但可由五行救应与“有情”结构部分或完全化解。
  - 庚辛金制甲、癸水合戊，皆为典型救应方式。
  - 无制无合、四柱无情时，才是真正“克岁”，凶象难解。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_093]` `[trigger: 下凌其上]` `[factor_trigger: xia_ling_qi_shang AND xiong_buneng_mian]` `[role: 主干]` 何则？下凌其上逆也，其凶决不能免。 → 《三命通会》卷十#太岁克战与五行救应
  - `[ns_smth_10_094]` `[trigger: 五行有救]` `[factor_trigger: wuxing_youjiu AND sizhu_youqing]` `[role: 主干依赖]` 若五行有救，四柱有情，如甲日克戊年，四柱元有庚申金，为有救。 → 《三命通会》卷十#太岁克战与五行救应
  - `[ns_smth_10_095]` `[trigger: 凶反为吉]` `[factor_trigger: xiong_fanwei_ji AND erzi_juquan]` `[role: 条件分支]` 若二字俱全，其年凶反为吉；有一字者凶半，二字俱无，凶莫能解。 → 《三命通会》卷十#太岁克战与五行救应
  - `[ns_smth_10_096]` `[trigger: 反必为财]` `[factor_trigger: fanbi_weicai AND sizhu_wuqing_kesui]` `[role: 总结]` 经云：五行有救，其年反必为财。四柱无情，故论名为克岁是也。 → 《三命通会》卷十#太岁克战与五行救应

- **详细解说**：  
  这一段为“太岁克战”引入了“救应评分”的思路：同样是日犯岁君，若命局中已有强力制约日干之神，或运岁提供合化桥梁，其实际凶度就会被打折扣。工程上可以把“制伏日干的五行”和“与岁干成合的五行”分别建模为两个救应因子，并允许它们叠加：二者同时存在时，可将原本的负面权重显著降低甚至翻转为正向机会；仅有其一时，则按“凶半”处理；二者皆无时，则完整保留“克岁”带来的高危权重。

- **校勘与字词辨析（双语）**：
  - **中文**：“壬以癸妹配戊”一语，以人伦譬合，是说壬水把癸水之“妹”嫁给戊土，形成有情之合，非指真实人物关系。
  - **English**: The expressions of "fear" and "marriage" in the aphorisms are metaphors for elemental control and combination rather than literal emotions or family ties."""
    normalized_text_zh: str = """"""
    subject: str = "太岁克战与五行救应"
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
        l1_anchor="smth_v1.0.0_太岁克战与五行救应_001_L1",
    )
    version: str = "1.0.0"
