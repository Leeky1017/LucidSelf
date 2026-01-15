"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619714
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
    semantic_id="qtbj_v1.0.0_6__五行数理_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 6五行数理(SemanticEntry):
    """
    - **原文（source_text）**：
  其数则水一、火二、木三、金四、土五。生旺加倍，死绝减半。

- **分字分词释义**：
  - **数**：数字、数目 / 河图生数 / 天地生成之序...
    """
    
    original_text: str = """- **原文（source_text）**：
  其数则水一、火二、木三、金四、土五。生旺加倍，死绝减半。

- **分字分词释义**：
  - **数**：数字、数目 / 河图生数 / 天地生成之序
  - **水一**：水的生数为一 / 天一生水 / 河图第一位
  - **火二**：火的生数为二 / 地二生火 / 河图第二位
  - **木三**：木的生数为三 / 天三生木 / 河图第三位
  - **金四**：金的生数为四 / 地四生金 / 河图第四位
  - **土五**：土的生数为五 / 天五生土 / 河图第五位
  - **生旺**：长生、帝旺等旺地 / 气机强盛 / 数量加倍
  - **加倍**：数量乘以二 / 旺则增益 / 断数之法
  - **死绝**：死、绝等衰地 / 气机衰竭 / 数量减半
  - **减半**：数量除以二 / 衰则折损 / 断数之法

- **规范化释义（primary_lang_explained）**：
  五行的生数是：水一、火二、木三、金四、土五。在生旺的状态下，数量加倍；在死绝的状态下，数量减半。

- **完整对等诠释（secondary_lang_full）**：
  Their numbers are: Water One, Fire Two, Wood Three, Metal Four, Earth Five. In the Birth and Prosperous stages, double the number; in the Death and Extinction stages, halve the number.

- **核心要点**：
  - 河图生数：水1，火2，木3，金4，土5。
  - 数量加减法则：旺加倍，衰减半。

- **详细解说**：
  这是基于《河图》的五行生成数（天一生水，地二生火...）。在实际命理应用中，常用此断子女数、兄弟数或事物数量，但必须结合旺衰进行倍增或折半的调整。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_028]` `[trigger: 五行数理]` `[factor_trigger: wuxing_hetu_numbers]` `[role: 主干]` 水一、火二、木三、金四、土五，此河图生数。 → 《穷通宝鉴·五行总论》#1.6
  - `[ns_qttbj_029]` `[trigger: 旺衰断数]` `[factor_trigger: shier_shengwang OR shier_sijue]` `[role: 条件分支]` 生旺加倍，死绝减半。 → 《穷通宝鉴·五行总论》#1.6
  - `[ns_qttbj_030]` `[trigger: 数理应用]` `[factor_trigger: wuxing_number AND shier_shengwang]` `[role: 总结]` 断子女数、兄弟数，须结合旺衰调整。 → 《穷通宝鉴·五行总论》#1.6"""
    normalized_text_zh: str = """"""
    subject: str = "6. 五行数理"
    factor_refs: list = ['shier_shengwang', 'shier_sijue', 'number_double', 'number_halve']
    
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
        l1_anchor="qtbj_v1.0.0_6__五行数理_001_L1",
    )
    version: str = "1.0.0"
