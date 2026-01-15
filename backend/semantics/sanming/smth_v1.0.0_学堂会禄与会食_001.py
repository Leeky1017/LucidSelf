"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101508
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
    semantic_id="smth_v1.0.0_学堂会禄与会食_001",
    book_id="sanming",
    engine_id="bazi"
)
class 学堂会禄与会食(SemanticEntry):
    """
    - **原文（source_text）**：
  诸家说有学堂会禄：如金长生巳、临官申，甲乙人得之；水土长生申、临官亥，丙丁壬癸人得之；木长生亥、临官寅，戊己人得之；火长生寅、临官巳，庚辛人得之。又名...
    """
    
    original_text: str = """- **原文（source_text）**：
  诸家说有学堂会禄：如金长生巳、临官申，甲乙人得之；水土长生申、临官亥，丙丁壬癸人得之；木长生亥、临官寅，戊己人得之；火长生寅、临官巳，庚辛人得之。又名官贵学堂，以官贵长生之位为学堂，官贵临官之位为词馆也。有学堂会食，如甲食丙得丙寅，乙食丁得丁巳，丙食戊得戊申之类。兼官印、驿马，其福厚；遇禄、贵、奇、德，其气清；值刑克冲破，其气浊。清则科名巍峨，厚则官尊荣显，浊则福禄微薄，官职卑贱。

- **分字分词释义**：
  - **学堂会禄 / 官贵学堂**：学堂与禄位、官贵之位相会，加强读书入仕与职位晋升的关联。
  - **学堂会食**：学堂与食神相会，主才学与实际输出能力兼备。
  - **气清 / 气厚 / 气浊**：以同见之神煞与用神关系判断格局之清浊与厚薄。

- **规范化释义（primary_lang_explained）**：
  原文通过「学堂会禄」「学堂会食」等组合，说明学堂词馆格的强弱不只在有无学堂词馆本身，还要看是否与禄位、官贵、食神等相会。若学堂与禄、贵、奇、德等同见且不受刑冲破坏，则格局清而厚，多主科名显达、官尊荣显；若常被刑冲、空亡所破，则虽有学堂之名而福薄官卑。

- **完整对等诠释（secondary_lang_full）**：
  When the Study Hall meets Lu, official stars or noble positions, the bridge from education to resources and office is strengthened, and when it meets the Eating God it highlights the ability to turn learning into concrete output.
  The surrounding stars determine whether this pattern is clear and refined, thick and practical, or turbid and frustrated.
  Accordingly it should be used to grade the efficiency with which education converts into career opportunities and material support, rather than as a simple yes or no label.
- **核心要点**：
  - 学堂会禄、会食是评估学业与职位转化效率的重要结构，在系统建模中可标记为「教育→资源→职位」链条的强化节点。
  - 对于现实数据，可将高学历且职业匹配良好的样本，与学堂会禄/会食结构对照，以检验经典结构与现代社会的相关性。
 
- **详细解说**：
  1) 在命局特征中标记「学堂会禄」「学堂会官」「学堂会食」等组合，形成 `xuetang_meets_lu`、`xuetang_meets_guan`、`xuetang_meets_shi` 等二值或多值特征；
   2) 根据同见的禄星、官星、食神是否为用神，以及是否受冲破，计算教育资源、职位晋升与实际输出能力三方面的强化程度；
   3) 在现实样本中，将这些结构与「高学历但职业不匹配」「学历一般但职位上升快」等类型对比，用以验证和调整各组合的正负向作用；
   4) 在解释层，将学堂会禄/会食视为「教育成果被现实结构接住的机会点」，而不是简单的「科名必显」标签。

 - 反例与边界：
   - 不宜只凭学堂会禄、会食就断定命主必然「官尊荣显」，还需看整体格局与时代、行业环境；
   - 若同见结构多为忌神或被凶煞重重夹击，学堂会禄的正向作用会大打折扣，甚至可能表现为「高投入低回报」；
   - 工程上若将所有组合一股脑视为正向特征，会掩盖「学历与职位脱节」等现实模式，应允许其在负向维度上发挥作用；
   - 反向误区是完全不考虑这些精细组合，只用粗糙的学历或收入标签，使系统难以解释复杂的教育—职业轨迹。

 - 小例（示意）：
   - 某命局学堂会禄、会官且不受冲破，现实中虽出身普通但通过教育获得关键职位晋升机会，系统可用「教育→资源→职位链路强化」解释其跃迁路径；
  - 另一命局学堂会食但不会禄，现实表现为专业技能和输出能力很强，却长期处于自由职业或非正式岗位，系统则在解释中强调「实务能力强于头衔」，并建议选择更看重作品与成果的职业场域。"""
    normalized_text_zh: str = """"""
    subject: str = "学堂会禄与会食"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_4', 'bazi_semantic', 'bazi_structure_marker_5', 'bazi_semantic', 'bazi_state_geju_7', 'bazi_semantic', 'bazi_function_factor_9', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_学堂会禄与会食_001_L1",
    )
    version: str = "1.0.0"
