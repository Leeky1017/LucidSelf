"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597135
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
    semantic_id="qtbj_v1.0.0_1__三冬己土总论与十月_亥月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1三冬己土总论与十月亥月(SemanticEntry):
    """
    - **原文（source_text）**：
  总之，三冬己土，湿泥寒冻，非丙暖不生，取丙为尊，甲木参酌。戊土癸水不用。
  惟初冬壬旺，取戊制之。余皆用丙丁，但丁不能解冻除寒，不能大济。
  或干...
    """
    
    original_text: str = """- **原文（source_text）**：
  总之，三冬己土，湿泥寒冻，非丙暖不生，取丙为尊，甲木参酌。戊土癸水不用。
  惟初冬壬旺，取戊制之。余皆用丙丁，但丁不能解冻除寒，不能大济。
  或干透一丙，支藏一丙，加以甲透，科甲有准。即藏丙无制，亦主衣蠴。
  或多壬水，得戊透制之，此命安然，富中取贵。不见戊土，富屋贫人。
  凡三冬己土，见壬水出干，为水浸湖田，此人孤苦。若见火不孤，见土不贫。

- **分字分词释义**：
  - **湿泥寒冻**：湿润泥土寒冷冻结 / 冬己土性 / 需暖
  - **丙为尊**：丙火最为尊贵 / 调候 / 用神
  - **解冻除寒**：融化冰冻除去寒气 / 丙火作用 / 用神
  - **富屋贫人**：住富屋的穷人 / 财多身弱 / 凶象
  - **水浸湖田**：水浸没湖边田地 / 壬透 / 凶象
  - **见火不孤**：见火就不孤独 / 印护 / 救应
  - **见土不贫**：见土就不贫穷 / 比劫帮身 / 救应

- **规范化释义（primary_lang_explained）**：
  冬天的己土，是湿泥寒冻的土，没有丙火照暖就不能生发，取丙火为尊，甲木参酌使用（生火/疏土）。戊土癸水通常不用（除非特殊情况）。
  只有初冬（亥月）壬水旺盛，取戊土制约壬水。其余时间都用丙丁火，但是丁火（灯烛）不能解冻除寒，不能大济事（不如太阳丙火）。
  如果天干透出一个丙火，地支藏一个丙火，加上甲木透出（官印相生），科甲有准。即使丙火藏支且无水克制，也主秀才。
  如果多壬水，得到戊土透出制约，这命安然，富中取贵。不见戊土，是富屋贫人（财多身弱）。
  凡是三冬的己土，见到壬水出干，叫“水浸湖田”，这人孤苦。如果见到火（印）就不孤，见到土（比劫）就不贫。

- **完整对等诠释（secondary_lang_full）**：
  Ji Earth in the Three Winter Months: Wet mud, cold and frozen. Without Bing to warm, it does not generate. Exclusively take Bing; consult Jia. Do not use Wu/Gui generally.
  Only in early Winter (Pig Month) when Ren is prosperous, use Wu to control it. Otherwise use Bing/Ding. But Ding cannot unfreeze or remove cold; it cannot help much.
  If one Bing reveals and one hides, plus Jia reveals, Civil Service is assured. Even if Bing is hidden and uncontrolled, it implies a degree.
  If Ren is abundant, obtaining Wu to control it makes a peaceful life, obtaining nobility amidst wealth. Without Wu, "Rich House Poor Man".
  Generally for Winter Ji Earth, seeing Ren reveal is "Water Soaking the Lake Field"; this person is lonely/bitter. Seeing Fire prevents loneliness; seeing Earth prevents poverty.

- **核心要点**：
  - **首要用神**：丙火（解冻）。湿泥非火不干，非暖不生。
  - **忌讳**：壬水（水浸湖田）。
  - **救应**：戊土（制水）、丙火（暖土）。

- **详细解说**：
  - 亥月己土绝地，水旺土荡。
  - “水浸湖田”：形象比喻，冬水旺则田园被淹，且寒冻无用。
  - 丙火是唯一的生机。甲木在冬月作用主要是生火（湿木不生火，需有火引），或者作为官星配合印星。"""
    normalized_text_zh: str = """"""
    subject: str = "1. 三冬己土总论与十月（亥月）"
    factor_refs: list = ['water_soaking', 'wet_mud_frozen', 'rich_house_poor']
    
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
        l1_anchor="qtbj_v1.0.0_1__三冬己土总论与十月_亥月_001_L1",
    )
    version: str = "1.0.0"
