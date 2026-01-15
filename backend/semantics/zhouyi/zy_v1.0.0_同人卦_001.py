"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899811
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
    semantic_id="zy_v1.0.0_同人卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 同人卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  同人于野，亨，利涉大川，利君子贞。

  【彖传】
  《彖》曰：同人，柔得位得中而应乎乾，曰同人。
  同人曰：“同人于野，亨，利涉...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  同人于野，亨，利涉大川，利君子贞。

  【彖传】
  《彖》曰：同人，柔得位得中而应乎乾，曰同人。
  同人曰：“同人于野，亨，利涉大川”，乾行也。
  文明以健，中正而应，君子正也。
  唯君子为能通天下之志。

  【象传】
  《象》曰：天与火，同人；君子以类族辨物。

  【爻辞】
  初九，同人于门，无咎。
  六二，同人于宗，吝。
  九三，伏戎于莽，升其高陵，三岁不兴。
  九四，乘其墉，弗克攻，吉。
  九五，同人，先号啕，而后笑，大师克相遇。
  上九，同人于郊，无悔。

- 分字分词释义：

  - 同人：与人同心、同道，非仅外在结伴，而是志向相同。
  - 于野：在郊野之地，与城邑、宗族相对，象征超越宗族门第、在更开阔的场域结交。
  - 利涉大川：有利于跨越重大险阻，如渡大河，象征可承担大风险、大事业。
  - 利君子贞：有利于君子坚守正道，在同人的过程中不失其贞。
  - 文明以健：内有文明之文、外具刚健之行，是同人卦之德性结构。
  - 类族辨物：按类区分、按族辨别，不是无原则的“同所有人”。
  - 同人于门：在门户之处即能与人同，象征开放而不闭塞。
  - 同人于宗：只与本宗、本派之人同，道路狭窄，故吝。
  - 伏戎于莽：在草莽中埋伏军队，比喻同人中暗藏冲突与武备。
  - 大师克相遇：大军克敌而同盟相会，象征经过冲突后达成更广泛的同人。

- **规范化释义（primary_lang_explained）**：

  同人卦讲“如何在差异中求同”。卦辞说“同人于野，亨，利涉大川，利君子贞”：在开阔处与人和同，不局限于宗族与门户，这样的同人之道可以通达，足以承受跨越大险之事；前提是君子要守贞，不为同人而失节。

  彖传强调：柔爻得中而应乎乾，内文明、外刚健，中正相应，所以只有君子能“通天下之志”，真正把不同群体的志向贯通起来。象传以“天与火，同人”说明：同人不是无差别混同，而是像天与火那样各得其位，又彼此相照。

- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Tong Ren, "Fellowship with People", is about finding genuine common ground amid difference. The Judgment says, "Fellowship with people in the open country: success. It is favorable to cross the great river. It is favorable for the noble person to be steadfast." True fellowship does not confine itself to one’s own clan or gate but takes place "in the open country", beyond narrow boundaries. Such fellowship can carry one safely across great dangers—symbolized by crossing a great river—provided the noble person holds to correctness and does not betray his integrity for the sake of fitting in.

  The Tuan explains that a gentle Yin line occupies the central place and responds to Qian: inwardly we have clarity and culture (Li), outwardly we have strength and initiative (Qian). This structure, "civilized within and strong without", allows the noble person to make the aspirations of the whole world communicate and converge. The Image, "Heaven with Fire: Fellowship with People", shows fire shining upward under heaven: each thing keeps its own place and nature, yet all are illuminated by a common light. Fellowship here is not a featureless blending with everyone, but a principled joining with those of like mind across wider fields.

- 核心要点：

  - 同人卦的核心，不是“无条件结盟”，而是以君子之贞为前提，在更大的场域中与志同者相聚。
  - 卦辞与爻辞都强调“超越宗族／门内、警惕宗派”的维度：同人于野吉，同人于宗吝。
  - 同人过程中必然伴随防御与冲突（伏戎于莽、大师相遇），关键是能否在冲突后回到公正之道。

-  详细解说：

  卦象上乾下离：火在天上，光明向上而不独照一处，象征“文明以健”。下卦离为火，有明；上卦乾为天，有健，同人之道便是“以明相照、以健相行”。

  初九“同人于门，无咎”，处卦之始，强调的是一种开放姿态：在门户之处便愿意与人相会，不先设门户之见。六二“同人于宗，吝”则是全卦的警语：若只与本宗同志，同温层之内互相取暖，最终反成局限之源。

  九三、九四落在中上之位，转向冲突与节制：九三伏兵于莽，因敌刚而“三岁不兴”，其贵在知止、安行；九四“乘其墉，弗克攻，吉”，登城而不攻，是在冲突边缘选择收手。九五“同人，先号啕，而后笑，大师克相遇”则展示同人之道的高潮：经历痛哭与战争之后，才迎来真正的会合与欢笑。上九“同人于郊，无悔”，回到野外之象，说明同人之道最终仍要回到开阔空间，而非局限权力中心。

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization."""
    normalized_text_zh: str = """"""
    subject: str = "同人卦（䷌）"
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
        l1_anchor="zy_v1.0.0_同人卦_001_L1",
    )
    version: str = "1.0.0"
