"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.597107
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
    semantic_id="qtbj_v1.0.0_2__四五六月己土_午未月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2四五六月己土午未月(SemanticEntry):
    """
    - **原文（source_text）**：
  四月己土，丙火建禄，田园焦坼，专取癸水，无癸用壬。有水无金，水无源头，富贵不久。
  五月己土，火势更炎，得癸透辛生，富贵双全。
  六月己土，燥气未...
    """
    
    original_text: str = """- **原文（source_text）**：
  四月己土，丙火建禄，田园焦坼，专取癸水，无癸用壬。有水无金，水无源头，富贵不久。
  五月己土，火势更炎，得癸透辛生，富贵双全。
  六月己土，燥气未除，先用癸水，次用丙火。

  （接原文后续段落）
  时日月年
  戊己己己
  辰巳巳巳
  
  时日月年
  辛己辛乙
  未巳巳巳

  时日月年
  庚己辛乙
  午巳巳丑

  时日月年
  乙己癸丙
  亥亥巳申

- **分字分词释义**：
  - **田园焦坼**：田园干裂焦枯 / 巳月火旺 / 需水
  - **专取癸水**：专门取用癸水 / 调候 / 用神
  - **水无源头**：水没有源头 / 无金生 / 次凶
  - **富贵不久**：富贵不能持久 / 水无根 / 凶象
  - **火势更炎**：火势更加炎热 / 午月特点 / 需水
  - **富贵双全**：富贵皆有 / 癸辛配合 / 吉象
  - **燥气未除**：干燥之气未消 / 未月特点 / 需润

- **规范化释义（primary_lang_explained）**：
  （补述：四月巳月，火旺土燥，癸水为尊，辛金佐之。五月午月，建禄，更加燥热，非大量水不能救。六月未月，土当令，依然燥。）
  示例命造：
  1. 戊辰、己巳、己巳、己巳：土火太重，无水（除辰中一点），恐为稼穑格或火炎土燥。
  2. 乙巳、辛巳、己巳、辛未：食神制杀，火旺。
  3. 乙丑、辛巳、己巳、庚午：伤官配印？
  4. 丙申、癸巳、己亥、乙亥：丙癸透，支见申亥水木，水火既济，贵格。

- **完整对等诠释（secondary_lang_full）**：
  (Note: Original text treats Summer Ji Earth collectively.)
  4th Month (Snake): Bing at Jianlu; fields scorched. Exclusively take Gui; without Gui use Ren. Water without Metal lacks source; wealth not lasting.
  5th Month (Horse): Fire even more intense. With Gui revealed and Xin generating, wealth and nobility are complete.
  6th Month (Goat): Dry Qi remains. First Gui, then Bing.

- **核心要点**：
  - **通用法则**：三夏己土皆喜癸水。
  - **源头**：喜金生水，源远流长。

- **详细解说**：
  - 夏月己土与戊土类似，都怕火炎土燥。
  - 但己土为阴土，更需滋润，否则成“瓦砾”或“灰尘”。
  - 示例命造4（丙申/癸巳/己亥/乙亥）完美符合“丙癸两透，水火既济”，且地支有根，故贵。"""
    normalized_text_zh: str = """"""
    subject: str = "2. 四五六月己土（午未月）"
    factor_refs: list = ['fields_scorched', 'fire_intense']
    
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
        l1_anchor="qtbj_v1.0.0_2__四五六月己土_午未月_001_L1",
    )
    version: str = "1.0.0"
