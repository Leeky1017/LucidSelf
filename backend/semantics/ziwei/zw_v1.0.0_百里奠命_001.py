"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.699273
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
    semantic_id="zw_v1.0.0_百里奠命_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 百里奠命(SemanticEntry):
    """
    - 分字分词释义：

  - **巨日同宫**：巨门太阳同在一宫，主晚成。
  - **禄合守照**：禄存与化禄拱守命宫，主财禄。
  - **左右昌曲加会**：左辅右彼文昌文曲同会，主晚年得志。
 ...
    """
    
    original_text: str = """- 分字分词释义：

  - **巨日同宫**：巨门太阳同在一宫，主晚成。
  - **禄合守照**：禄存与化禄拱守命宫，主财禄。
  - **左右昌曲加会**：左辅右彼文昌文曲同会，主晚年得志。
  - **少年不顺**：早年限行羊铃地劫虚绝之地，多有奔波挫折。
  - **擎羊败地**：擎羊在十二长生败地，主凶险。
  - **禄马倒行**：禄存天马不利逾行，主不吉。
  - **阳男土五局**：百里奠命盘的五行局数，土五局主厚重稳健。

- **原文（source_text）**：  
  百里奠命。阳男土五属。巨日同宫，禄合守照，左右昌曲加会，少年不顺，因限步行羊、铃、地劫、虚绝之地，卅五后方得遂志。大限入酉，擎羊败地，小限在命垣，与太岁相冲，禄马倒不吉。

- **规范化释义（primary_lang_explained）**：  
  百里奚命属阳男土五局，巨日同宫、禄合守照、左右昌曲加会，少年不顺因限行羊铃地劫虚绝之地，三十五后方遂志。大限入酉擎羊败地，小限在命垣与太岁相冲，禄马倒不吉而亡。

- **完整对等诠释（secondary_lang_full）**：  
  Lin Xiangru's Yang male Earth Fifth chart has Jumen‑Sun same palace, Salary combination guarding, Left‑Right Chang‑Qu converge. Youth not smooth due to periods in Blade‑Bell‑Robbery‑Extinction. Success after 35. Major at You with Blade in Defeat; minor at Life clashes Tai Sui. Salary‑Horse unfavourable. Death.
  Baili Xi's Yang male Earth Fifth chart has Jumen‑Sun same palace, Salary combination guarding, Left‑Right Chang‑Qu converge. Youth not smooth due to periods in Blade‑Bell‑Robbery‑Extinction. Success after 35. Major at You with Blade in Defeat; minor at Life clashes Tai Sui. Salary‑Horse unfavourable. Death.

- **核心要点**：  
  1. 巨日同宫、禄合左右昌曲，三十五后遂志。  
  2. 少年不顺因限行凶地。  
  3. 大限擎羊败地、小限冲太岁，为寿终应期。

- **叙事素材（narrative_snippets）**：
  - **晚成之命**："巨日同宫，禄合守照，左右昌曲加会，少年不顺，卅五后方得遂志"，百里奚命主前困后达、典型晚成格局。
  - **少年多厄**："因限步行羊、铃、地劫、虚绝之地"，少年多行羊铃地劫虚绝等凶地，易有奔波挫折与环境桎梏。
  - **禄马倒不吉**："大限入酉，擎羊败地，小限在命垣，与太岁相冲，禄马倒不吉"，禄马倒行配擎羊败地，为寿终关口。
  - **现代应用**：晚成命局可鼓励三十五岁前以学习积累为主；当大限行至擎羊败地又逢禄马倒行之年，应谨慎变动与投资，以免功成之时反生大挫。"""
    normalized_text_zh: str = """"""
    subject: str = "百里奠命"
    factor_refs: list = ['pattern_juritonggong', 'pattern_qingyangbaidi', 'pattern_lumadaoxing', 'source_ref', 'rel_bailixi_001', 'pattern_juritonggong', 'rel_bailixi_002', 'pattern_qingyangbaidi', 'rel_bailixi_003', 'pattern_lumadaoxing', 'evi_bailixi_001', 'pattern_lumadaoxing', 'rule_qingyang_baidi', 'concept_late_bloomer', 'concept_blade_defeat']
    
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
        l1_anchor="zw_v1.0.0_百里奠命_001_L1",
    )
    version: str = "1.0.0"
