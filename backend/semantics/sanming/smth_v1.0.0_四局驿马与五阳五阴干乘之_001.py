"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101353
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
    semantic_id="smth_v1.0.0_四局驿马与五阳五阴干乘之_001",
    book_id="sanming",
    engine_id="bazi"
)
class 四局驿马与五阳五阴干乘之(SemanticEntry):
    """
    - **原文（source_text）**：
  寅午戌生人，马在申，而五阳干乘之：见甲申，截路空亡马；丙申，大败马；戊申，福星伏马；庚申，逢天关马；壬申，大败马。以上巳酉丑申年月日时发应。申子辰人，...
    """
    
    original_text: str = """- **原文（source_text）**：
  寅午戌生人，马在申，而五阳干乘之：见甲申，截路空亡马；丙申，大败马；戊申，福星伏马；庚申，逢天关马；壬申，大败马。以上巳酉丑申年月日时发应。申子辰人，马在寅，而五阳干乘之：见甲寅，正禄文星马；丙寅，福星马；戊寅，伏马；庚寅，破禄马；壬寅，截路马。以上亥卯未寅年月日时发应。巳酉丑人，马在亥，而五阴干乘之：见乙亥，天德马，以马中支生干，汨没无成，徒自聪明；丁亥，天乙马；己亥，旺禄马；辛亥，正禄马；癸亥，大败马。以上申子辰亥年月日时发应。亥卯未人，马在巳，而五阴干乘之：见乙巳，正禄马；丁巳，旺气马；己巳，九天禄库马；辛巳，截路马；癸巳，天乙伏马。以上寅午戌巳年月日时发应。

- **分字分词释义**：
  - **五阳干 / 五阴干**：甲丙戊庚壬为阳干，乙丁己辛癸为阴干，分别乘驿马位置。
  - **截路马 / 大败马 / 福星马 / 正禄马等**：对不同干乘于驿马位置形成之吉凶性质的分类名目。

- **规范化释义（primary_lang_explained）**：
  这一段将前文的数理分布落实到具体命局：寅午戌为火局，马在申，由五阳干乘之，各有「截路」「大败」「福星」「天关」等不同象；申子辰为水局，马在寅，同样由五阳干乘之，分别构成正禄文星马、福星马、伏马、破禄马、截路马。巳酉丑金局马在亥，由五阴干乘之，形成天德马、天乙马、旺禄马、正禄马、大败马等；亥卯未木局马在巳，同样由五阴干乘之，形成正禄马、旺气马、九天禄库马、截路马、天乙伏马。各局所「发应」的年月日时也在原文中点明。

- **核心要点**：
  - 四局驿马的吉凶取决于「哪一个天干搭在马位上」，而非单看有无驿马支。
  - 对系统来说，可以将驿马位看作一个槽位，再按所乘干的性质打上对应标签（福星、大败、截路等），用于迁移、升迁等预测场景。
 
- **详细解说**：
  1) 在识别出本局驿马支后，读取其上所乘天干，判断属于哪一类名目（福星马、截路马、大败马、旺禄马、正禄马等）；
  2) 将「马位 + 所乘天干」编码为组合特征，例如 `horse_type=FUXING`, `horse_type=DABAI`，并额外派生「吉/中/凶」「稳/波动」「资源/负担」等维度；
  3) 对不同局（火局、水局、金局、木局）的驿马，分别统计其与实际迁移、升职、职业转向的共现频率，用于校正古籍名目的现代含义；
  4) 在预测层面，将吉性马位用于提高「良性变动」的概率，将截路、大败类马位用于提高「变动中伴随损耗或折返」的风险权重。

- 反例与边界：
  - 不宜见「截路马」「大败马」便简单认定一切迁移皆凶，系统应结合命局中财官印食以及现实背景判断具体风险等级；
  - 同一命局中若存在多重马位与多种名目，不可强行用单一象来概括所有变动，应分阶段、分领域拆开分析；
  - 工程化时，若只保留「命中有无马位」而丢弃马位上天干信息，则会损失大量关于变动质量的区分度；
  - 反向误区是只关心「马」的吉凶，而忽略命局中是否真的存在适合变动的资源与条件，使解释流于玄虚。

- 小例（示意）：
  - 某寅午戌局命，马在申，日干为戊而命中见戊申福星伏马，系统可解释为「在变动中易得贵人和资源协助」，适合在岗位轮换或地区调动中争取更高责任；
  - 另一申子辰局命，马在寅却落壬寅截路马且行运反复触及，系统则提示「多有调整但方向感容易丢失」，建议现实中避免频繁无计划跳槽，以阶段性项目方式消化动象。"""
    normalized_text_zh: str = """"""
    subject: str = "四局驿马与五阳五阴干乘之"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_yima_1', 'bazi_semantic', 'bazi_state_factor_105', 'bazi_semantic', 'bazi_state_factor_106', 'bazi_semantic', 'bazi_state_factor_107', 'bazi_semantic', 'bazi_relation_combo', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_四局驿马与五阳五阴干乘之_001_L1",
    )
    version: str = "1.0.0"
