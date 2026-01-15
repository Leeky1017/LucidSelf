"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101573
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
    semantic_id="smth_v1.0.0_十恶大败本义与用法边界_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十恶大败本义与用法边界(SemanticEntry):
    """
    - **原文（source_text）**：
  论十恶大败。十恶者，譬律法中人，犯十恶重罪，在所不赦；大败者，譬兵法中与敌交战，大败无一生还，喻极凶也。六甲旬中十个日值禄而空亡，如甲辰、乙巳，甲以寅...
    """
    
    original_text: str = """- **原文（source_text）**：
  论十恶大败。十恶者，譬律法中人，犯十恶重罪，在所不赦；大败者，譬兵法中与敌交战，大败无一生还，喻极凶也。六甲旬中十个日值禄而空亡，如甲辰、乙巳，甲以寅为禄，乙以卯为禄，甲辰旬以寅卯为空亡；壬申者，壬以亥为禄，甲子旬以亥为空亡，余如丙申、丁亥、庚辰、戊戌、癸亥、辛巳、乙丑等日皆仿此。命中犯者，当以日上见之为是，其余不论。况犯者未必皆凶，若内有吉神相扶、贵气相辅，当为吉论。《元白经》曰：「十恶都来十个辰，逐年有煞用区分。」如庚戌年见甲辰日，辛亥年见乙巳日，壬寅年见丙申日，癸巳年见丁亥日，甲辰年见戊戌日，乙未年见乙丑日，甲戌年见庚辰日，乙亥年见辛巳日，丙寅年见壬申日，丁巳年见癸亥日，盖以年支干冲日支干，无禄为忌，余悉无妨。

- **分字分词释义**：
  - **十恶、大败**：借律法重罪与战场全军覆没之喻，强调其在传统评断中的极端凶性。
  - **六甲旬中日值禄而空亡**：以「禄入空亡」为核心结构，说明十恶大败的取位方式。
  - **犯者未必皆凶**：原文明确提示，不可孤立以此断命，仍须看格局与吉神扶助。

- **规范化释义（primary_lang_explained）**：
  十恶大败常被后人简化为「逢之必凶」的标签，但原文实际强调了其使用边界：它以六甲旬中禄入空亡为基础，指出某些日子在禄位上见空，有如有位无禄、功不成名不就，因而称「大败」。然而作者反复说明：命中犯十恶，必须以日柱为准，且要结合局中吉神与贵气来判断，不能简单按日子判人生死贵贱。若内有吉神相扶，仍可视作磨练与波折，而不必视为绝对恶兆。

- **次语种完整诠释（secondary_lang_full）**：
  The Ten Evils Great Defeat refers to ten specific days in the six Jia periods where the Lu (Salary/Position) star falls into Void (Kong Wang). It metaphorically implies a state of "position without salary" or "effort without reward," akin to committing a heavy crime or suffering a total defeat in battle. However, the text emphasizes that its severity depends on the overall chart structure and supporting deities. If auspicious stars are present, it may only signify challenges or instability rather than absolute misfortune, serving as a test of resilience.

- **核心要点**：
  - 核心结构为「日禄入空亡」
  - 象征资源与结果的不稳定性
  - 需结合吉神判断，不可一票否决

- **详细解说**：
  在实际应用与推演中，十恶大败主要作为「禄位失真」的提示。"""
    normalized_text_zh: str = """"""
    subject: str = "十恶大败本义与用法边界"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'shi_e_da_bai', 'bazi_semantic', 'lu_in_void', 'bazi_semantic', 'auspicious_deity_rescue', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_十恶大败本义与用法边界_001_L1",
    )
    version: str = "1.0.0"
