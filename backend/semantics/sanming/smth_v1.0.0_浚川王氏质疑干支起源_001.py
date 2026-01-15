"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227899
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
    semantic_id="smth_v1.0.0_浚川王氏质疑干支起源_001",
    book_id="sanming",
    engine_id="bazi"
)
class 浚川王氏质疑干支起源(SemanticEntry):
    """
    - **原文（source_text）**：
  浚川王氏曰：昔大挠作甲子，名数无有穷己，便于纪时，偶尔定之。若推考其源，必日月初转之日，而后为甲子可也。天之开尚未有地，安能有人？尚未有人，孰从而传以...
    """
    
    original_text: str = """- **原文（source_text）**：
  浚川王氏曰：昔大挠作甲子，名数无有穷己，便于纪时，偶尔定之。若推考其源，必日月初转之日，而后为甲子可也。天之开尚未有地，安能有人？尚未有人，孰从而传以记之？

- **分字分词释义**：
  - **浚川王氏**：王洙，字浚川，宋代学者。
  - **名数无有穷己**：名称数字没有穷尽。
  - **便于纪时**：便于记录时间。
  - **偶尔定之**：偶然确定的。
  - **日月初转**：日月初次运转。
  - **孰从而传**：谁来传播记录。

- **规范化释义（primary_lang_explained）**：
  浚川王洙说：过去大挠作甲子，名称数字没有穷尽，是为了便于纪时，偶然确定的。如果追究其根源，必须是日月初次运转那天，才能成为甲子。天刚开辟时还没有地，怎么能有人？既然还没有人，谁来传播记录这些呢？

- **完整对等诠释（secondary_lang_full）**：
  Wang Shi of Junchuan stated: When Da Nao created Jiazi in ancient times, the names and numbers were endless, convenient for recording time, and arbitrarily established. If we trace the source, it must be the day when sun and moon first rotated to be called Jiazi. When heaven opened, earth did not yet exist—how could there be humans? If there were no humans yet, who would transmit and record these matters?

- **核心要点**：
  - 王洙质疑甲子起源的神话传说
  - 认为甲子是便于纪时而偶然确定
  - 提出天开时无地无人，无法传记的逻辑问题
  - 对传统神话起源论提出理性质疑

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_145]` `[trigger: 王氏质疑干支起源]` `[factor_trigger: wang_junchuan AND rational_skepticism]` `[role: 主干]` 浚川王氏曰：昔大挠作甲子，名数无有穷己，便于纪时，偶尔定之。天之开尚未有地，安能有人？孰从而传以记之？ → 《三命通会》卷一#浚川王氏质疑干支起源

- **详细解说**：
  此条引用宋代学者王洙（字浚川）的理性质疑。王洙认为甲子并非神圣起源，而是古人为便于纪时而偶然确定的。他提出逻辑问题：如果真要追溯甲子起源，必须回到日月初转之时，但天开时尚无地，更无人，既然无人，谁来传播和记录甲子呢？这是对传统神话起源论的理性批判，体现宋代学者的实证精神。但作者并未完全认同这种怀疑论，后文将引用实践经验来反驳。

- **校勘与字词辨析（双语）**：
  - **中文**：王洙（996-1057），字浚川，北宋学者。"偶尔"此处指偶然、碰巧。"孰"，谁。
  - **English**: Wang Shu (996-1057 CE), courtesy name Junchuan, was a Northern Song scholar; "偶尔" here means "by chance" or "arbitrarily"; "孰" means "who.""""
    normalized_text_zh: str = """"""
    subject: str = "浚川王氏质疑干支起源"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_浚川王氏质疑干支起源_001_L1",
    )
    version: str = "1.0.0"
