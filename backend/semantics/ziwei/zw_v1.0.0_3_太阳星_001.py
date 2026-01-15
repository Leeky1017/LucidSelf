"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.725527
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
    semantic_id="zw_v1.0.0_3_太阳星_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 3太阳星(SemanticEntry):
    """
    - 原文（source_text）：

  问：太阳所主若何？

  答曰：太阳星属火，日之精也，乃造化之表仪。在数，主人有贵气，能为文为武。诸吉集则降祯祥，处黑星则劳心费力。若随身命之中，居于庙乐之...
    """
    
    original_text: str = """- 原文（source_text）：

  问：太阳所主若何？

  答曰：太阳星属火，日之精也，乃造化之表仪。在数，主人有贵气，能为文为武。诸吉集则降祯祥，处黑星则劳心费力。若随身命之中，居于庙乐之地，为数中之至曜，乃官禄之枢机，后化贵化禄，最宜在官禄宫，男作父星，女为夫主。命逢诸吉守照，更得太阴同照，富贵全美。若身居之，逢吉聚，则可在贵人门下客，否则公卿走卒。

- 原注（原文注解，可无则省略小节）：

  希夷先生曰：太阳星周天历度，轮转无穷，喜辅弼而佐君，象以禄存而助福。所忌者巨暗遭逢，所乐者太阴相旺，诸宫会吉则吉，黑道遇之则劳。守人身命，主人忠鲠，不较是非。若居庙旺，化禄化权，允为贵论。

  歌曰：太阳原属火，正主官禄星。若居身命位，禀性最聪明。慈爱量宽大，福寿享遐龄。若与太阴会，骤发贵无伦。有辉照身命，平步入金门。巨门不相犯，升殿承君恩。偏垣逢暗度，贫贱不可言。男人必克父，女命夫不全。火铃逢苦定，羊陀眼目昏，二限若值此，必定卖田园。

  玉蟾先生曰：太阳司权贵为文，遇天刑为武。在寅卯为初升，在辰巳为升殿，在午为日丽中天，主大富贵，在未申为偏垣，作事先勤后惰，在酉为西没，贵而不显，秀而不实；在戌亥子为失辉，更逢巨暗破军，一生劳碌贫忙，更主眼目有伤，与人寡合招非。女命逢之，夫星不美，遇耗则非礼成婚。

- 分字分词释义：

  - **造化之表仪**：日之精华外显，为天地运行与人间秩序的可见象征，主显贵与权柄。
  - **庙乐之地**：太阳落在得地、庙旺之宫（如寅卯辰巳午等），光辉充足，力量端正。
  - **日丽中天**：太阳在午宫，如日当空，主权力与名望达到顶点。
  - **失辉**：太阳在戌亥子酉等地失去光辉，象征权位不稳、体力与眼目受损。
  - **男作父星，女为夫主**：在古法中，太阳同时象征男命的父亲与女命的丈夫，反映其对权威男性角色的投射。

- 规范化释义（primary_lang_explained）：

  本条将太阳描写为“造化之表仪”，亦即一切权力、荣誉与外在光辉的象征。太阳居于庙旺之地、特别是官禄宫时，往往意味着命主有机会进入权力结构的中枢，担任决策角色；若再得太阴同照、辅弼禄存相助，则既有贵气又不乏实际资源，富贵较为完整。相反，若太阳处在黑道、失辉之地，又逢巨门暗曜、破军等凶星冲破，则多见劳心劳力而难以得到相称的回报，甚至因权责失衡而招致非议与损伤。

  在性格层面，得地之太阳多主光明磊落、忠鲠不阿，行事有担当，重视名誉与责任；失辉而又受杀冲时，则可能表现为强撑的自尊与易受伤的自我形象，一方面渴望被承认，一方面又常感吃力不讨好。古法以太阳为“男父女夫”：在男命中，太阳体现父亲的形象与父系权威；在女命中，则多象征伴侣与婚姻中的男性角色，因此太阳得失辉，常直接映照出父女关系或婚姻质量。总体而言，本条提醒命师：判断太阳，不仅要看其是否“亮”，更要看它照在何处、与哪些星曜同度，以及在一生运程中何时被放大或削弱。

- 完整对等诠释（secondary_lang_full）：

  This passage presents the Sun as the visible emblem of creation—an indicator of status, authority and public presence. When the Sun stands in dignified signs and especially when it rules or occupies the Career palace, it often marks a life that is drawn into the centre of organisational or political structures. With strong support from assistants such as benefic stars, fortune indicators and a well‑placed Moon, the native can combine personal brilliance with real backing, resulting in positions of trust, honours and material security. By contrast, when the Sun falls into places where its light is weakened and is further entangled with dark stars like Jumen or Pojun, the text describes people who work hard, carry responsibility and yet struggle to receive proportionate recognition or reward.

  On the character level, a well‑placed Sun corresponds to openness, generosity, loyalty and a natural sense of duty. The person tends to be warm‑hearted, willing to take the lead and to stand up for what they believe is right. A weakened or heavily afflicted Sun, however, can show up as fragile pride and a constant tension between the wish to be seen and the fear of failure or humiliation; such individuals may oscillate between bursts of confidence and long stretches of self‑doubt. Traditional Ziwei Doushu also reads the Sun as the "father star" in male charts and the "husband star" in female charts, so its condition speaks directly to one’s experience of paternal authority and intimate partnership. Overall, the teaching is that the Sun does not simply promise rank or misfortune; it describes how far one’s inner radiance can translate into stable roles in the outer world, and what kinds of relational and bodily costs may accompany that journey, especially when the Sun loses its light or is struck by harsh companions.

- 核心要点：

  1. **太阳化贵**：造化之表仪，化贵化禄，主官禄权贵。
  2. **日月配合**：喜太阴同照，富贵全美；忌巨暗遭逢。
  3. **旺地为要**：寅卯初升、辰巳升殿、午为日丽中天，大富贵；酉戌亥失辉则贫贱。
  4. **男父女夫**：男作父星，女为夫主，失辉则克父克夫。
  5. **眼目之疾**：失辉遇凶，主眼目有伤。

- 叙事素材（narrative_snippets）：

  - **造化表仪**："太阳星，日之精也，乃造化之表仪"，太阳为权贵化禄之星。
  - **日月同照**："喜太阴同照，富贵全美"，日月配合为上等富贵组合。
  - **得辉失辉**："寅卯辰巳午为得辉，大富贵；酉戌亥为失辉，贫贱"，太阳的旺衰机制。
  - **父夫之星**："男作父星，女为夫主"，太阳对男女命的六亲意义不同。
  - **现代应用**：太阳可作为评估"官禄权贵"的关键指标，需关注其在命盘中的得辉与配合状态。"""
    normalized_text_zh: str = """"""
    subject: str = "3 太阳星"
    factor_refs: list = ['star_taiyang', 'state_dehui_shihui', 'combo_riyue_tongzhao', 'palace_guanlu', 'role_nanfu_nvfu']
    
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
        l1_anchor="zw_v1.0.0_3_太阳星_001_L1",
    )
    version: str = "1.0.0"
