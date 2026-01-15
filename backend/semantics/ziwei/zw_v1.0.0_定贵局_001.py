"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.778602
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
    semantic_id="zw_v1.0.0_定贵局_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 定贵局(SemanticEntry):
    """
    - 分字分词释义：

  - **定贵局**：判断官贵格局的标准与方法。
  - **日月夹命**：太阳太阴从两侧夹持命宫。
  - **日出扶桑**：太阳在卯宫（东方）守命，日出东升之象。
  - ...
    """
    
    original_text: str = """- 分字分词释义：

  - **定贵局**：判断官贵格局的标准与方法。
  - **日月夹命**：太阳太阴从两侧夹持命宫。
  - **日出扶桑**：太阳在卯宫（东方）守命，日出东升之象。
  - **月朗天门**：太阴在亥宫守命，月明天门之象。
  - **月生沧海**：太阴在子宫守田宅，月照大海之象。
  - **辅弼拱主**：左辅右弼拱照紫微帝座。
  - **君臣庆会**：紫微与辅弼魁钺等臣星相会。
  - **财印夹禄**：财星印星从两侧夹持禄存。
  - **禄马佩印**：禄存天马与印星同宫或拱照。
  - **坐贵向贵**：命坐贵人星，对宫亦有贵人。
  - **七杀朝斗**：七杀在寅申子午向北斗朝拜。
  - **明珠出海**：太阴在亥子丑宫守命，月出海面。
  - **科权禄拱**：化科化权化禄三化星拱照命宫。
  - **贪火相逢**：贪狼与火星同宫，主暴发。
  - **府相朝垣**：天府天相从三方朝照命宫。

主要格局包括：
1. 日月夹命
2. 日出扶桑（日卯守命）
3. 月落亥宫（月朗天门）
4. 月生沧海（月子守田宅）
5. 辅弼拱主
6. 君臣庆会
7. 财印夹禄
8. 禄马佩印
9. 坐贵向贵（魁钺）
10. 马头带剑
11. 七杀朝斗
12. 日月并明
13. 明珠出海
14. 日月同临
15. 刑囚夹印（武勇）
16. 科权禄拱
17. 贪火相逢
18. 武曲守垣（卯宫）
19. 府相朝垣
20. 紫府朝垣
21. 文星暗拱
22. 权禄生逢
23. 擎羊入庙
24. 巨机居卯
25. 明禄暗禄
26. 科明禄暗
27. 金舆扶驾

- 完整对等诠释（secondary_lang_full）：

  The nobility configuration standards collect twenty‑seven classic patterns that specifically promise official rank, honors and recognized status. Rather than speaking vaguely of wealth and good fortune, this section asks whether the chart contains structures strong enough to support a sustained career in office or positions of visible authority.
  The first group centers on the luminaries and imperial stars. Patterns such as Sun‑Moon flanking the Life palace, Sun rising from Fusang with the Sun in Mao, the Moon clarifying the Heavenly Gate in Hai, or Ziwei and Tianfu facing the court from three directions all indicate that the native stands in a bright, publicly recognized position. When these are joined by assistants and nobles such as Zuofu, Youbi, Tiankui and Tianyue, or by the transformations of Examination, Authority and Salary arching toward Life, they describe people who both hold rank and actually exercise power.
  A second group focuses on martial and mixed civil‑military configurations. Qisha facing the Dipper, the Horse‑Head Carrying‑Sword pattern where Qingyang rides with Tianma, or Wuqu guarding the territory in key palaces all support command in military, police or other force‑bearing roles. When literary stars such as Wenchang and Wenqu secretly arch toward the Life palace at the same time, the result can be officials who are both competent administrators and capable strategists.
  A third group describes more specialized paths into nobility: dual‑salary patterns where Lucun and the star receiving Transformation‑Salary stand together, Manifest‑Hidden Dual‑Salary where manifest and hidden wealth both support the chart, Authority‑and‑Salary meeting in timely cycles, or the Gold‑Carriage Supporting‑Driver pattern where auspicious carriages and escorts symbolically surround the native. By listing these twenty‑seven patterns, the text provides a checklist for assessing how solidly a chart is rooted in noble structures: the more such configurations appear in clean, dignified form, the more likely the person is to enjoy a steady, upward‑moving career within official or elite circles.

- 叙事素材（narrative_snippets）：

  - **日月夹命：自带聚光灯**：日月夹命或同临明亮之地，一生多站在台前，适合公职、领袖或公众人物路线。
  - **君臣庆会：上下齐心**：紫微会辅弼、魁钺等贵星，如帝王与股肱同堂，多见真有权责而非空名的官职。
  - **马头带剑：披甲上阵**：擎羊天马同宫，常主军警、执法、安保等“带刀”的武职生涯，以行动与胆识立身。
  - **明禄暗禄：内外皆有靠山**：显禄、暗禄并存时，台面有职位与俸禄，台下还有人情与财力撑腰，属于“里外皆贵”的格局。
  - **金舆扶驾：坐车不走路**：各类车舆、扶驾象征环绕命宫，命主往往不必事事奔走，而是坐在体系与资源搭建好的“车上”前行。

- 核心要点：
  - 以紫微、天府、日月等官贵星曜为主轴，辅以辅弼、魁钺等吉曜的拱照。
  - 重视官贵星曜的强势、吉曜的加持以及宫位的重要性。
  - 贵格的形成需要官贵星曜的强势、吉曜的加持以及宫位的重要性。

- 详细解说：
  | 君臣庆会 | Monarch-Ministers Celebration | 紫微与辅弼魁钺会合 | Ziwei encountering Assistants and Nobles |
  | 马头带剑 | Horse-Head Carrying-Sword | 擎羊天马同宫的武贵格 | Martial nobility with Qingyang-Tianma co-presence |
  | 明禄暗禄 | Manifest-Hidden Dual-Salary | 禄存化禄同守的双禄格 | Dual-salary pattern with Lucun-transformation-Salary |

---"""
    normalized_text_zh: str = """"""
    subject: str = "定贵局"
    factor_refs: list = ['combo_junchengqinghui', 'combo_matoudaijian', 'combo_mingluanlu', 'combo_riyuejiaming', 'combo_kequanlugong', 'source_ref', 'rel_guiju_001', 'guige_xingyao', 'rel_guiju_002', 'huayao_jiachi', 'rel_guiju_003', 'kuiyue_guixing', 'evi_guiju_001', 'combo_junchengqinghui', 'rule_junchengqinghui', 'evi_guiju_002', 'combo_matoudaijian', 'rule_matoudaijian', 'concept_nobility_structure', 'concept_transformation', 'concept_noble_stars']
    
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
        l1_anchor="zw_v1.0.0_定贵局_001_L1",
    )
    version: str = "1.0.0"
