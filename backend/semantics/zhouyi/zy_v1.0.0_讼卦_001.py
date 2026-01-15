"""
Auto-generated semantic module for zhouyi
Generated at: 2025-12-05T13:30:19.899743
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
    semantic_id="zy_v1.0.0_讼卦_001",
    book_id="zhouyi",
    engine_id="yijing"
)
class 讼卦(SemanticEntry):
    """
    - **原文（source_text）**：

  【卦辞】
  讼：有孚窒惕，中吉，终凶。利见大人，不利涉大川。

  【爻辞】
  初六，不永所事，小有言，终吉。
  九二，不克讼，归而逋，其邑人...
    """
    
    original_text: str = """- **原文（source_text）**：

  【卦辞】
  讼：有孚窒惕，中吉，终凶。利见大人，不利涉大川。

  【爻辞】
  初六，不永所事，小有言，终吉。
  九二，不克讼，归而逋，其邑人三百户，无眚。
  六三，食旧德，贞厉，终吉；或从王事，无成。
  九四，不克讼，复即命，渝，安贞吉。
  九五，讼，元吉。
  上九，或锡之鞶带，终朝三褫之。

  【彖传】
  《彖》曰：讼，上刚下险，险而健，讼。
  “讼，有孚窒惕，中吉”，刚来而得中也。
  “终凶”，讼不可成也。
  “利见大人”，尚中正也。
  “不利涉大川”，入于渊也。

  【象传】
  《象》曰：天与水违行，讼；君子以作事谋始。

- 分字分词释义：

  - 讼：卦名，有争讼、争辩之意，象征意见相左、利益相冲之时的对立与诉讼。
  - 有孚：内有诚信与真实，根据充分。
  - 窒惕：窒，阻塞；惕，警惕。指在争讼中有所阻塞而生警惕之心。
  - 中吉：居中守正而得吉。
  - 终凶：若讼久而不止，终必致凶。
  - 大人：德行高、居中正之人，可为裁决者。
  - 不利涉大川：不利于涉险而行，比喻不宜在争讼状态下冒进大事。
  - 不永所事：不长期坚持正在进行的争讼之事，宜适时止损。
  - 小有言：有小的非议、言语争执。
  - 归而逋：返回而逃避，离开争端中心。
  - 无眚：无灾祸、无罪咎。
  - 食旧德：享受先人的德泽，依靠既有的功业与信誉。
  - 贞厉：守正而有危险，需谨慎。
  - 复即命，渝：回到原来的命分与位置，改变想法、调整态度。
  - 安贞吉：安于守正则吉。
  - 鞶带：大带，象征高位官服与荣宠。
  - 终朝三褫之：一朝之内多次被剥夺，象征荣宠不稳、得失无常。
  - 天与水违行：天向上行，水向下流，比喻上下乖离、动向不一。
  - 作事谋始：做事之初便加以谋划，以防将来争讼。

- **规范化释义（primary_lang_explained）**：

  讼卦描述的是人与人之间发生争论、争讼的局面：内有险阻（坎在下），外为刚健（乾在上），上下违行，容易形成对立。卦辞“有孚窒惕，中吉，终凶”指出：在争讼之初，如果一方内有诚信、在阻塞中仍能保持警惕，并居中守正，则尚可得吉；但若争讼拖延不止、执意要分高下，最终必致凶祸。“利见大人”说明遇到争端时宜求助于德行与立场中正的大人裁决，而非自行纠缠；“不利涉大川”则提醒在争讼阶段不宜推进重大冒险之举。

  六爻刻画了争讼过程中的不同态度与结局：初六“ 不永所事，小有言，终吉”，强调争讼不宜长久，坚持不放反致祸；能及早止讼，即便有一些口舌之事，终能吉利。九二“不克讼，归而逋，其邑人三百户，无眚”，说明当己方条件不足、难以取胜时，退让与离开反而能保全自身与百姓，无灾无咎。六三“食旧德，贞厉，终吉；或从王事，无成”提示依赖旧有功业可以暂保吉利，但若在王事中争功，往往难有成就。九四“不克讼，复即命，渝，安贞吉”，说明争讼不利时，回归本位、改变执念，安于守正，反能获得安吉。九五“讼，元吉”是指身处中正之位、以公道之心裁决争讼，可以大吉，但前提是“中正而无私”。上九“或锡之鞶带，终朝三褫之”，以得失无常的官带象征因讼获利者难以长久：即便一时获赐高位，也会在短时间内多次被剥夺。

  彖传指出“讼，上刚下险，险而健，讼”，揭示了讼卦结构：下坎为险，上乾为刚，内心充满险阻，外在又刚强好胜，自然容易引发诉讼。象传以“天与水违行，讼；君子以作事谋始”进一步强调：讼之本在于“上下违行”“方向不一”，君子欲免于讼，关键在于“作事谋始”——在事情一开始就谋定方向、厘清权责，从源头上预防争端。


- **完整对等诠释（secondary_lang_full）**：

  The Hexagram Song, "Conflict" or "Litigation", addresses how to avoid, handle, and resolve disputes in the midst of disagreement. The Judgment "Song: having sincerity yet being constrained; being vigilant brings centrality and good fortune, but ending brings misfortune; it is favorable to see the great person, not favorable to cross the great water" establishes the basic principle for handling conflict: even if one's position is correct, litigation cannot be prolonged; one should seek resolution through a just and impartial great person rather than pursue victory at all costs. The Image "heaven and water move in contrary directions, Song; the noble person thereby plans the beginning when undertaking affairs" points to the root of litigation: upper and lower moving in opposite directions, directions not unified; if the noble person wishes to avoid litigation, the key is to "plan the beginning when undertaking affairs"—clarify direction and define responsibilities from the very start, preventing disputes at the source.

  - **English**: Based on Wang Bi commentary edition. Punctuation modernized for readability while preserving original characters. Classical terminology maintained without arbitrary modernization.
#### 核心要点：

  - 讼卦的核心是“争讼不可久”：初能中吉，久则终凶。
  - 面对争端，应优先寻求中正的大人裁决，而非一味争胜；在不利之势下，适时退让可保全自身与众人。
  - 六爻展示从“及早止讼”“退让保全”“凭旧德维持”“认命而变”“公正裁判”“一时荣宠难久”的多种形态，提示在争讼中不同角色的得失。
  - 预防胜于补救：君子以“作事谋始”来避免将来走到讼卦局面。

#### 详细解说：

  在卦序中，讼继需而来：需卦讲“在险之前的等待与蓄势”，讼卦则讲“在利益与立场冲突时的对峙与裁决”。乾上坎下的结构，与需卦同样是“外刚内险”，但需偏重“未入险而自守”，讼则强调“已成对立而求决”。这表明在等待期若谋划不当，便易发展为讼。

  卦辞“有孚窒惕，中吉，终凶”中，“有孚”是争讼得以站得住脚的前提：若没有真实的证据与诚信，仅凭情绪之争，根本谈不上“中吉”；“窒惕”意味着在受到阻滞与压力时，能保持警惕与自省，从而不至于越界。然争讼一旦超出必要的范围、持续过久，就会侵蚀双方、损伤群体，因此“终凶”。

  爻辞中多次出现“不克讼”：九二“不克讼，归而逋，其邑人三百户，无眚”，九四“不克讼，复即命，渝，安贞吉”。这两爻分别代表两个层面的退让策略：前者是“以撤离争端中心、保全自己与百姓”为要，后者是“在自知理亏或势弱时，回归原位、改变态度，以守正自安”。这都体现出易传对于“知止”的高度重视。六三“食旧德”则提醒：依赖过往功业可以支撑一时的地位，但在新局势中若不能再次展现德行与能力，最终难有实绩。

  九五“讼，元吉”是讼卦中的关键：只有当身处裁决位置的人真正“刚健中正”，才能使讼事得到大吉的结果。若九五偏私，则整个讼局将流入“终凶”的方向。因此在实际应用中，当卦象指向讼时，往往意味着需要寻找值得信赖的“九五角色”——无论是制度、裁判者还是内心的公正原则，而不仅仅是寻找强者庇护。

  上九“或锡之鞶带，终朝三褫之”以反复授予又剥夺的官带，象征通过争讼得来的荣利难以稳固：依靠诉讼和争夺获得的位置，本身即缺乏稳固的德行基础，因而易得易失。这对于现代情境中依赖“维权/诉讼/争功”来获取利益的行为，也有相当的警示意义。"""
    normalized_text_zh: str = """"""
    subject: str = "讼卦（䷅）"
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
        l1_anchor="zy_v1.0.0_讼卦_001_L1",
    )
    version: str = "1.0.0"
