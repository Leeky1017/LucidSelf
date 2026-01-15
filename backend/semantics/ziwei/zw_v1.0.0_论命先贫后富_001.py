"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755743
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
    semantic_id="zw_v1.0.0_论命先贫后富_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论命先贫后富(SemanticEntry):
    """
    - 分字分词释义：

  - **先贫后富**：早年出身微贱、生活艰辛，中晚年因行运得扶而发达致富的人生轨迹。
  - **先成后败**：早年生于富贵之家，中途因恶运而人离财散、家道中落的人生轨迹。
...
    """
    
    original_text: str = """- 分字分词释义：

  - **先贫后富**：早年出身微贱、生活艰辛，中晚年因行运得扶而发达致富的人生轨迹。
  - **先成后败**：早年生于富贵之家，中途因恶运而人离财散、家道中落的人生轨迹。
  - **限步逢凶**：大限、小限与太岁相冲照，又叠加凶杀守临，导致阶段性的重大破败。
  - **限步相扶**：大小限运行至吉曜庙旺之地，星辰配合良好，使原本中庸的格局得以翻身。
  - **中庸之局**：本命格局既非极贵亦非极贱，弹性较大，随行运起伏可上可下。
  - **不贫即损寿**：恶运下的典型后果，要么财富尽失，要么寿元折损，甚至两者兼有。
  - **平地升腾**：从低起点突然跃升，如草根逆袭、寒门发迹，常见于先贫后富的格局。
  - **本命与限运交互**：判断贫富起落时，必须同时考量原局结构与行运阶段的互动，而非只看一端。

- 原文（断句）：

  论命先贫后富：

  如人生于富贵之家，一生快乐享福，财官题达，妻荣子贵，奴仆成行，声名昭著。其间有半途遭伤，人离财散，官非火盗，身丧家亡。此等之命，非命也，却是限步逢凶，大小二限及太岁相冲照，又加凶杀守临，故此破败，不贫即损寿也，所谓先成后败，先大后小也。

  又有人命出身微贱，营活生理，百工巧艺，九流医术，又为农圃等辈，初历艰辛度日，却乃中末平地升腾发财，惊骇乡邦，因生在中庸之局，后因限步相扶，星辰逢吉曜庙旺，以此突然发达进禄，所谓先贫后富，先小后大是也。

- 规范化释义（primary_lang_explained）：

  本条以两种相反的人生轨迹，说明「原生环境」与「行运吉凶」之间的关系。第一段讲的是先富后贫：有人生在富贵之家，早年享尽财官恩宠、妻荣子贵、家丁成行，却在半途遭逢伤灾、官非、火盗、人员散离乃至家破身亡。原文明确指出，这种情形「非命也，却是限步逢凶」，即并非先天命局就是「必败格」，而是在大小二限与太岁相冲照，又叠加凶杀守临、恶运频仍的情形下，才出现「先成后败、先大后小」的破局格局，有时只是财富与地位消失，有时更牵连寿命折损。

  第二段讲的是先贫后富：有人原本出身微贱，靠百工巧艺、医术、农圃等辛苦营生，早年生活颇为艰辛，却在中晚年突然「平地升腾」，发财进禄、惊动乡里。其原因在于本命多属「中庸之局」——结构并不极差——而后天限步相扶、星辰逢吉曜庙旺，运程逐渐打开，于是形成「先贫后富、先小后大」的翻盘走势。换言之，本条要强调的并非简单的宿命对比，而是提醒占者：判断一生命运时，必须将原局结构与限运节奏合参，既不能因早年富贵而断一生无忧，也不能因早年困顿而否定中晚年翻身的可能。

- 完整对等诠释（secondary_lang_full）：

  This passage contrasts two opposite life paths to show how birth structure and
  timing interact. In the first, a person is born into wealth and privilege,
  enjoying status, spouse and children, servants and fame, yet in midlife meets
  severe blows—lawsuits, fire, theft, separation and even the collapse of home
  and body. The text insists that this is "not inherent in the fate itself" but
  arises when major and minor periods and the annual stem–branch repeatedly hit
  harsh places and gather malefic stars. The result is a pattern of "success
  then decline, greatness then smallness", sometimes limited to loss of wealth
  and office, sometimes extending to shortened lifespan.

  The second path begins in poverty. A person from a humble background relies on
  craft, medicine or farming and struggles through early life, only to rise
  sharply in middle or later years, gaining wealth and rank in ways that shock
  their community. Here the natal chart is described as a moderate base that is
  later lifted by supportive periods and dignified benefic stars, producing the
  "poverty then wealth, small then great" pattern. Together these stories
  caution readers not to judge an entire life by its opening scene. Both the
  starting structure and the sequence of periods must be weighed before calling
  a destiny fortunate or unfortunate.

- 核心要点：

  1. 「先成后败、先大后小」多由富贵格局在行运中频遇恶限、二限与太岁相冲照并叠加凶杀所致。
  2. 「先贫后富、先小后大」往往源于中庸命局在中晚年得到吉曜庙旺与行运扶助，逐步打开格局。
  3. 原文强调「非命也，却是限步逢凶/相扶」，即分清命局结构与运程阶段的不同责任。
  4. 断人贫富起落时，必须同时考量出身环境、本命结构与大小二限、太岁等时间因子。
  5. 实务上应避免以早年一段的状态，武断推论全生命走向，忽略中晚年的逆转与回落可能。"""
    normalized_text_zh: str = """"""
    subject: str = "论命先贫后富"
    factor_refs: list = ['pattern_xianchenghoubai', 'pattern_xianpinhoufu', 'state_xianbufengxiong', 'type_zhongyongzhiju', 'result_pobaisunshou', 'source_ref', 'rel_pinfu_001', 'type_zhongyongzhiju', 'rel_pinfu_002', 'state_xianbufengxiong', 'rel_pinfu_003', 'result_pobaisunshou', 'evi_pinfu_001', 'state_xianbufengxiong', 'rule_pinfu_xiancheng', 'evi_pinfu_002', 'pattern_xianpinhoufu', 'rule_pinfu_xianpin', 'concept_life_curve', 'concept_fortune_reversal']
    
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
        l1_anchor="zw_v1.0.0_论命先贫后富_001_L1",
    )
    version: str = "1.0.0"
