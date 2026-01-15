"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899831
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
    semantic_id="zy_v1.0.0_谦卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 谦卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  谦，亨，君子有终。

  【彖传】
  《彖》曰：谦，亨。
  天道下济而光明，地道卑而上行。
  天道亏盈而益谦，地道变盈而流谦，鬼...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  谦，亨，君子有终。

  【彖传】
  《彖》曰：谦，亨。
  天道下济而光明，地道卑而上行。
  天道亏盈而益谦，地道变盈而流谦，鬼神害盈而福谦，人道恶盈而好谦。
  谦尊而光，卑而不可逾，君子之终也。

  【象传】
  《象》曰：地中有山，谦；君子以裒多益寡，称物平施。

  【爻辞】
  初六，谦谦君子，用涉大川，吉。
  六二，鸣谦，贞吉。
  九三，劳谦，君子有终，吉。
  六四，无不利，㧑谦。
  六五，厥孚交如，威如，吉。
  上六，冥豫，成，有渝，无咎。

- 分字分词释义：

  - 谦：谦虚、退让、能下。卦名指以谦德行事之道。
  - 君子有终：君子能以谦德自始至终，不中途败德。
  - 天道下济而光明：天空在上却向下济泽万物，使光明遍及。
  - 地道卑而上行：大地居下却不断向上生发万物。
  - 亏盈益谦：削减盈满，以益于不满之处。
  - 害盈福谦：鬼神为盈满之人带来损害，为谦下之人带来福泽。
  - 裒多益寡：收敛多者、增益少者。
  - 称物平施：权衡事物，使施予均平。
  - 鸣谦：谦德已闻于外，名声远播。
  - 劳谦：勤劳而不矜，劳而能谦。
  - 㧑谦：推举谦德，使谦德之人得用。

- **规范化释义（primary_lang_explained）**：

  谦卦集中谈“在有的状态下仍然谦下”。卦辞“谦，亨，君子有终”点出：谦德本身即可通达，关键在于君子能否终身保持不改。彖传从天道、地道、鬼神、人道四个层面说明“道、神、人无不恶盈而好谦”，谦卦由此成为全书中极受推重的一卦。

  象传“地中有山”之象，形容高者能藏于下，不露锋芒；君子观此，以“裒多益寡，称物平施”，即在资源与权力分配上主动向弱方倾斜，让整体趋于平衡。六爻则展示谦德在不同位置上的具体表现：初六“谦谦君子，用涉大川，吉”，说明谦德可用来承担大险；六二“鸣谦，贞吉”则是内心中正而名声自然远播；九三“劳谦，君子有终，吉”强调在辛劳与成就之后仍能保持谦卑，才是真正“有终”。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Qian, "Modesty" or "Humility", is about remaining lowly and yielding even while one already "has"—position, achievement, or resources. The Judgment, "Modesty: success; the noble person has an end", states that modesty in itself is a way to success; the crucial question is whether the noble person can maintain this virtue to the very end, without losing it halfway. The Tuan explains from four levels—Heaven, Earth, spirits, and human beings—that all abhor fullness and favor modesty: Heaven reduces what is overfull and adds to what is modest; Earth shifts away from fullness and causes modesty to flow; spirits harm the proud and bless the humble; people dislike the arrogant and love the modest. For this reason Qian is one of the most highly valued hexagrams in the whole book.

  The Image, "a mountain within the earth", shows height hidden below: what is high is concealed in what is low and does not flaunt itself. The noble person, seeing this, "gathers from the abundant and adds to the lacking, weighing things and giving in a balanced way"—that is, he actively tilts resources and power toward those who have less so that the whole can move toward balance. The six lines display how modesty operates in different positions: the first line, "a modest, modest noble person; using this to ford the great river; good fortune", shows that modesty is not weakness or mere retreat but a heart of self-restraint that can bear great dangers. The second line, "proclaimed modesty; steadfast and auspicious", portrays inner correctness that naturally becomes widely known, not modesty put on as an act. The third line, "labored modesty; the noble person has an end; good fortune", stresses that only those who remain humble after toil and accomplishment truly "have an end".

  The fourth line, "in nothing unfavorable; he promotes modesty", speaks of one who does not keep merit for himself but elevates people of modest virtue. The fifth line, "not enriching himself, but his neighbors; it is favorable to use punitive expeditions; in nothing unfavorable", turns toward governance: rather than glorying in his own wealth, the ruler shares with neighbors and uses force only as a rightful correction, aligned with modest virtue. The top line, "deeply obscure in joy; it is accomplished; there is change; no blame", warns that even when modesty is widely recognized, one can still fall into a kind of dark complacency; only by changing and not relying on force or fame as the final support can one remain without blame.

- 核心要点：

  - 谦卦不是贫弱之卦，而是“在有中守下”的卦：有位、有功而仍能下人。
  - 天地鬼神人道一致偏向“减盈、益谦”，谦卦因此被视为一种与大势相符的长期策略。
  - 六五、上六的“利用侵伐”“利用行师”，提示谦德并不排斥必要的征伐与行动，但前提是立场公正、出于整齐是非，而非逞强。

- 详细解说：

  卦象上坤下艮：山在地中，既有高度，又肯埋藏，是谦德的形象。与大有相邻：大有谈丰盛，谦谈在丰盛之后“如何自处”。若大有而不谦，则盈；顺而不戒，则冥豫。

  初六处下卦之始，“谦谦君子，用涉大川，吉”指出谦德不是软弱退避，而是以自守之心涉险。六二“鸣谦，贞吉”偏重内中之正：并非为了美名而谦，而是因为心中有中正之德，自然发为声誉。九三“劳谦，君子有终，吉”处阳位，说明在负重劳作、建功立业之后仍能谦下，才是真正不败之道。

  六四“无不利，㧑谦”则从“推贤”的角度谈谦：自己不居其功，而推举谦德之人；六五“不富，以其邻，利用侵伐，无不利”转向具体政务——不以自富为荣，而借助亲邻之助整饬不服之处；上六“冥豫成，有渝，无咎”则是谦德名满天下之时仍需谨慎：虽可用兵，却不宜以武力为终极依靠。"""
    normalized_text_zh: str = """"""
    subject: str = "谦卦（䷎）"
    factor_refs: list = []
    
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
        book_id="zhouyi",
        chapter="",
        l1_anchor="zy_v1.0.0_谦卦_001_L1",
    )
    version: str = "1.0.0"
