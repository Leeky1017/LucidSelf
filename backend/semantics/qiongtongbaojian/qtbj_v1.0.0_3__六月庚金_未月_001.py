"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578328
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
    semantic_id="qtbj_v1.0.0_3__六月庚金_未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3六月庚金未月(SemanticEntry):
    """
    - **原文（source_text）**：
  六月庚金，三伏生寒，顽钝极矣，先用丁火，次取甲木。
  丁甲两透名显身荣，忌癸伤丁。有甲无丁、庸俗。有丁无甲、生员。丁甲全无，下贱之人。
  木虽有，...
    """
    
    original_text: str = """- **原文（source_text）**：
  六月庚金，三伏生寒，顽钝极矣，先用丁火，次取甲木。
  丁甲两透名显身荣，忌癸伤丁。有甲无丁、庸俗。有丁无甲、生员。丁甲全无，下贱之人。
  木虽有，丁不透，支又见水，执鞭之士。丁火无伤，贸易之流。
  支会土局，甲先丁后。甲透者，文章显达。丁透者，刀笔扬名。或柱多金，有二丁出制，异路功名。

- **分字分词释义**：
  - **六月**：未月 / 农历六月 / 土气旺
  - **三伏生寒**：三伏天金气进气 / 金渐旺 / 未月特点
  - **顽钝**：顽固愚钝 / 未炼之金 / 需火炼
  - **丁火**：阴火 / 正官 / 炼金用神
  - **甲木**：阳木 / 偏财 / 疏土引丁
  - **名显身荣**：名声显赫身世荣耀 / 吉象 / 功名
  - **癸伤丁**：癸水克丁火 / 伤官见官 / 凶象
  - **执鞭之士**：赶车的低贱人 / 下役 / 凶象
  - **土局**：辰戌丑未合土 / 土重 / 需甲疏
  - **刀笔**：文书职位 / 吏胥 / 功名类型

- **规范化释义（primary_lang_explained）**：
  六月（未月）的庚金，三伏生寒（金气进气），极其顽钝（土厚金顽），先用丁火（炼金），次取甲木（疏土/引丁）。
  丁火甲木两透，名声显赫身世荣耀，忌讳癸水伤丁。有甲木无丁火，庸俗。有丁火无甲木，生员。丁甲全无，下贱之人。
  木虽然有，丁火不透，地支又见水（湿木无焰），执鞭之士（赶车的/下役）。丁火无伤，贸易之流。
  地支会成土局（土重），甲木优先，丁火在后。甲木透出者，文章显达（疏土）。丁火透出者，刀笔扬名。如果柱中多金（身旺），有二个丁火出制，异路功名。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 6th Month (Goat Month): Three Fu Days generate Cold; extremely stubborn and dull. First use Ding, then Jia.
  If Ding and Jia are both revealed, name is prominent and self glorious; dread Gui hurting Ding. With Jia but no Ding, vulgar. With Ding but no Jia, a student. Without Ding/Jia, a lowly person.
  If Wood exists but Ding is not revealed, and branches see Water, one is a "Whip Holder" (servant). If Ding is unharmed, a trader.
  If branches meet Earth Frame, prioritize Jia, then Ding. If Jia reveals, essays are prominent. If Ding reveals, fame via pen/knife. If pillars have much Metal, and two Dings reveal to control, alternative fame.

- **核心要点**：
  - **首要用神**：丁火（炼金）、甲木（疏土）。未月土金气杂，金顽土厚。
  - **三伏生寒**：未月金进气，故称顽钝。
  - **忌水**：水湿木伤丁，格局低。

- **详细解说**：
  - 顽钝之金：三伏天金气进气，土厚金顽，非火不炼。
  - 甲木双用：疏土、引丁两大作用。
  - "刀笔扬名"：土局甲不透，丁透主文书吏职。"""
    normalized_text_zh: str = """"""
    subject: str = "3. 六月庚金（未月）"
    factor_refs: list = ['whip_holder', 'trade_merchant']
    
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
        l1_anchor="qtbj_v1.0.0_3__六月庚金_未月_001_L1",
    )
    version: str = "1.0.0"
