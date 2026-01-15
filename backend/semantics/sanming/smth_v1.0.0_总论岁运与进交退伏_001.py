"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264366
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
    semantic_id="smth_v1.0.0_总论岁运与进交退伏_001",
    book_id="sanming",
    engine_id="bazi"
)
class 总论岁运与进交退伏(SemanticEntry):
    """
    - **原文（source_text）**：  
  总论岁运。夫太岁者，年中天子，一岁诸神煞之尊，统正方位，回送六气，迁运四时，以成岁功，至尊无上。若人遇克冲、压伏，皆为不祥之兆。运者，恊和二十四气...
    """
    
    original_text: str = """- **原文（source_text）**：  
  总论岁运。夫太岁者，年中天子，一岁诸神煞之尊，统正方位，回送六气，迁运四时，以成岁功，至尊无上。若人遇克冲、压伏，皆为不祥之兆。运者，恊和二十四气，般运一生休咎，扶持四柱，辅弼三元。运与流年二者相为表里，乃人命祸褔死生所系。岁用天元，运用地支，凡行好运而日干伤流年天元，为祸轻；若行不好运，及脱财官运，而日干伤岁干，为祸重。若是己发之命，祸患立至。凡行不好运，未可便言衰绝，大要知己发未发，其气数已过未过言之。行运以生月为运元，最怕行运与太岁冲克，若岁运冲月，必祸。若岁运与日相对，谓之返吟；岁运压日，谓之伏吟，二者不利六亲，非横破财，不为吉兆。凡岁运吉凶，当生天元，或支中原无官星，天元有正官，或原有偏官，制伏太过。运遇天元官星，亦可发福。运支无财而运干是财，亦可发财；运支无煞而运干是煞，亦足为祸。经云：岁冲克运者吉，运冲克岁者凶。格局不吉者死，岁运相生者吉，禄马贵人相合交互者亦吉。详审细推，无有不验。论进交退伏阎东叟云：以十干为四候，十五日为一候，十二日为进神候，外三日为交退伏神候。故甲子为第一进神，则丙子、丁丑、戊寅为交退伏神；己卯为第二进神，则辛卯、壬辰、癸巳为交退伏神；甲午为第三进神，则丙午、丁未、戊申为交退伏神；己酉为第四进神，则辛酉、壬戌、癸亥为交退伏神。值进神则发迹亨快；值交神则庶事不谐；值退神则官资降黜；值伏神则所作留滞。经云：进神四座兼奇特，贵煞相扶为福力。是也。

- **规范化释义（primary_lang_explained）**：  
  这一段是对前文岁运论的总结。太岁被称为“年中天子”，统摄一岁诸神煞与方位气机；大运则“辅弼三元”，协调二十四节气，贯穿一生休咎。岁与运相为表里，一为天、一为地，共同决定人生命运的时间坐标。技术上，岁用天元（年干），运用地支（运支），再叠加运干。行好运时，日干克流年天元，其祸尚轻；行坏运或脱财官运时，日干克岁干，则祸重，若命局已先发贵，更易出现“祸患立至”的急转。判断“不好运”时，不宜一见凶象便言衰绝，还要看命主是否已经发过、气数是否已过。行运以生月为运元，最怕岁运冲克月令（冲运元），以及岁运与日柱构成返吟伏吟，这些结构多不利六亲，往往表现为破财、丧事或家庭变故。后文再强调：岁冲克运者反吉，运冲克岁者真凶；岁运相生、禄马贵人相合交互者皆为吉象。最后引用阎东叟之说，将流年按“进神、交神、退神、伏神”细分：值进神则发迹亨快，交神多不谐，退神主降黜，伏神主停滞不前。

- **完整对等诠释（secondary_lang_full）**：  
  This comprehensive passage summarizes the interplay between annual Tai Sui and major luck. Tai Sui is portrayed as the "yearly emperor," overseeing all baleful and auspicious stars, governing directions and circulating the six qi to complete the work of the year. Major luck functions as the ministerial apparatus that harmonizes the twenty‑four solar terms and carries a person's fortunes and misfortunes throughout life. Together, year and luck form the framework upon which life and death, fortune and calamity depend. Technically, the year uses the heavenly stem (tian yuan) while luck uses the earthly branch (di zhi), with the luck stem adding another layer. When a person is in a favorable decade, if the Day Stem harms the Annual Stem, the resulting misfortune tends to be lighter; when in a bad decade or after wealth and office have already peaked, the same configuration becomes much more serious. One must therefore always ask whether a chart has already "expended" its peak blessings. Luck is taken from the birth month as its origin (yun yuan), and clashes between year and luck against the Month Branch, or configurations of "return echo" and "submerged echo" between year/luck and day pillar, are particularly problematic, often manifesting as losses among relatives or sudden financial and familial troubles. Conversely, when year and luck mutually generate, or when benefic stars such as Salary Horse and Nobleman combine across these layers, the result is strongly auspicious. The theory of "advancing, intersecting, retreating, and hidden" qi further refines annual timing: advancing spirits favor rapid success, intersecting spirits bring friction, retreating spirits indicate demotion or decline, and hidden spirits signify delays and stagnation.

- **核心要点**：
  - 太岁与大运一为“年中天子”、一为“辅弼三元”，共同构成人生命运的时间坐标。
  - 岁用天元、运用地支，日干与岁运的冲合方向与所处运势好坏，会极大改变凶吉程度。
  - 岁运冲月令、返吟伏吟、多主六亲不利与破财丧事；岁冲克运反吉，运冲克岁则真凶。
  - 进神/交神/退神/伏神提供对同一年内部运势细节的进一步划分。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_101]` `[trigger: 年中天子]` `[factor_trigger: nianzhong_tianzi AND yisui_zhushensha]` `[role: 主干]` 夫太岁者，年中天子，一岁诸神煞之尊。 → 《三命通会》卷十#总论岁运与进交退伏
  - `[ns_smth_10_102]` `[trigger: 运与流年]` `[factor_trigger: yun_yu_liunian AND biaoli_xiwei]` `[role: 主干依赖]` 运与流年二者相为表里，乃人命祸福死生所系。 → 《三命通会》卷十#总论岁运与进交退伏
  - `[ns_smth_10_103]` `[trigger: 返吟伏吟]` `[factor_trigger: fanyin_fuyin AND liuqin_buji]` `[role: 条件分支]` 若岁运与日相对，谓之返吟；岁运压日，谓之伏吟，二者不利六亲。 → 《三命通会》卷十#总论岁运与进交退伏
  - `[ns_smth_10_104]` `[trigger: 进神发迹]` `[factor_trigger: jinshen_faji AND tuishen_jiangchu]` `[role: 总结]` 值进神则发迹亨快；值交神则庶事不谐；值退神则官资降黜；值伏神则所作留滞。 → 《三命通会》卷十#总论岁运与进交退伏

- **详细解说**：  
  工程化上，可以将“年—运—日”视为三层时间轴：年为外层节拍，运为中层阶段，日柱为个体核心。文中提供了若干可以直接转化为因子的判读规则：例如“岁冲克运者吉、运冲克岁者凶”可以建模为一个方向性布尔因子，放到 L3 规则中；“岁运冲月”“返吟”“伏吟”则是对运元（月令）和日柱的高危标记。“是否已发过”“气数已过未过”则提示我们在系统里为命主引入“已实现潜能/未实现潜能”的状态维度，不再把命局视为静态。阎东叟的进交退伏法则，则可选作更细粒度的年内时序标签，用于解释为何同一年中上半年与下半年表现迥异。

- **校勘与字词辨析（双语）**：
  - **中文**：“返吟”“伏吟”在古书中多指干支伏吟反吟，现代常简化为“岁运与日柱同柱或相对”之象，此处仍据原文用语，在解释中给出现代化转译。
  - **English**: Terms like "advancing spirit" and "retreating spirit" are metaphorical devices to describe phases of momentum within a year; they are not literal spirits but functional labels for timing."""
    normalized_text_zh: str = """"""
    subject: str = "总论岁运与进交退伏"
    factor_refs: list = ['source_ref']
    
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
        l1_anchor="smth_v1.0.0_总论岁运与进交退伏_001_L1",
    )
    version: str = "1.0.0"
