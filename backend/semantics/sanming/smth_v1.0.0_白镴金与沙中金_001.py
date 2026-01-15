"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228143
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
    semantic_id="smth_v1.0.0_白镴金与沙中金_001",
    book_id="sanming",
    engine_id="bazi"
)
class 白镴金与沙中金(SemanticEntry):
    """
    - **原文（source_text）**：
  庚辰辛巳，以金居火土之地，气己发生，金尚在矿，寄形生养之乡，受西方之正色，乃曰白镴金。甲午乙未，则气已成物，质自坚实，混于沙而别于沙，居于火而炼于火，...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚辰辛巳，以金居火土之地，气己发生，金尚在矿，寄形生养之乡，受西方之正色，乃曰白镴金。甲午乙未，则气已成物，质自坚实，混于沙而别于沙，居于火而炼于火，乃曰沙中金也。

- **分字分词释义**：
  - **白镴金**：白色的镴金（锡铅合金）。
  - **火土之地**：火土旺的地方。
  - **气己发生**：气已经开始发生。
  - **金尚在矿**：金还在矿石中。
  - **寄形生养之乡**：寄托形体在生养的地方。
  - **西方之正色**：西方金的正统颜色（白色）。
  - **气已成物**：气已经成为物质。
  - **混于沙而别于沙**：混在沙中但又区别于沙。
  - **居于火而炼于火**：处在火中并被火锻炼。

- **规范化释义（primary_lang_explained）**：
  庚辰辛巳，金处在火土旺的地方，气已经开始发生，金还在矿石中，寄托形体在生养的地方，接受西方金的正统颜色，就叫白镴金。甲午乙未，气已经成为物质，质地自然坚实，混在沙中但又区别于沙，处在火中并被火锻炼，就叫沙中金。

- **完整对等诠释（secondary_lang_full）**：
  Gengchen-Xinsi: Metal residing in Fire-Earth ground, qi already generating, Metal still in ore, lodging form in nurturing locale, receiving Western direction's proper color (white), thus called White-Wax Metal. Jiawu-Yiwei: qi already formed into substance, quality naturally firm and solid, mixed in sand yet distinct from sand, dwelling in fire yet tempered by fire, thus called Sand-Center Metal.

- **核心要点**：
  - 庚辰辛巳：白镴金（金在矿中，气已发生）
  - 甲午乙未：沙中金（质地坚实，火中锻炼）
  - 白镴金如矿中之金，初具形体
  - 沙中金如沙里淘金，经火锻炼

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_177]` `[trigger: 白镴金与沙中金]` `[factor_trigger: white_wax_metal AND sand_center_metal AND nayin_metal_formation]` `[role: 主干]` 庚辰辛巳，以金居火土之地，气己发生，金尚在矿，乃曰白镴金。甲午乙未，则气已成物，质自坚实，混于沙而别于沙，居于火而炼于火，乃曰沙中金也。 → 《三命通会》卷一#白镴金与沙中金

- **详细解说**：
  此条续解金纳音。庚辰辛巳为"白镴金"：辰为土库，巳为火旺，金在火土之地开始发生（矿石中含金），虽在矿中但"寄形生养"，接受西方金的白色，如同矿石中的白色金属（锡铅合金）。甲午乙未为"沙中金"：午为火旺，未为土旺，金气已成实物，质地坚实，混在沙土中但可以分辨（如沙金），在火中被锻炼提纯。从海中金（隐藏）→金泊金（极弱）→白镴金（在矿）→沙中金（成物），体现了金从孕育到成形的完整过程。命理上，沙中金比前三种更有力量，因为已经成物且经过火炼。

- **校勘与字词辨析（双语）**：
  - **中文**："白镴金"，镴音腊，指锡铅合金。"寄形生养之乡"指金在辰巳得到生养。"西方之正色"，西方属金，金色为白。"混于沙而别于沙"指沙金虽在沙中但质地不同。
  - **English**: "White-Wax Metal," "la" (wax) refers to tin-lead alloy. "Lodging form in nurturing locale" means Metal nurtured at Chen-Si. "Western direction's proper color"—West belongs to Metal, Metal color is white. "Mixed in sand yet distinct" refers to placer gold different in quality from sand."""
    normalized_text_zh: str = """"""
    subject: str = "白镴金与沙中金"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_白镴金与沙中金_001_L1",
    )
    version: str = "1.0.0"
