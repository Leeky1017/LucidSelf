"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.101550
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
    semantic_id="smth_v1.0.0_羊刃本义与极盛之吉凶_001",
    book_id="sanming",
    engine_id="bazi"
)
class 羊刃本义与极盛之吉凶(SemanticEntry):
    """
    - **原文（source_text）**：
  论羊刃。《三车》云：「羊言刚也，刃者取宰割之义。」禄过则刃生，功成当退不退则过，越其分如羊之在刃，言有伤也。故羊刃常居禄前一辰。希尹曰：「阴阳万物之理...
    """
    
    original_text: str = """- **原文（source_text）**：
  论羊刃。《三车》云：「羊言刚也，刃者取宰割之义。」禄过则刃生，功成当退不退则过，越其分如羊之在刃，言有伤也。故羊刃常居禄前一辰。希尹曰：「阴阳万物之理，皆恶权盛。」当其极，处火则焦，灭水则涌，竭金则折，缺土则崩，裂木则摧折，故既成而未极，则为福，已极则将反而为凶。极盛之地，十干中正处是也：卯者，甲之正位，为阳木之极；辰者，乙之正位，为阴木之极；午者，丙之正位，为阳火之极；未者，丁之正位，为阴火之极；酉者，庚之正位，为阳金之极；戌者，辛之正位，为阴金之极；子者，壬之正位，为阳水之极；丑者，癸之正位，为阴水之极。午马在申，庚禄在申，乙巳贵在申，庚羊刃在酉，却乙巳贵人取甲申为驿马而前视羊刃，故曰揽辔澄清。此格多为清严之官，若更有吉类，多为酷吏，能制奸宄。子平以甲丙戊庚壬五阳干有刃，乙丁己辛癸五阴干无刃，惟见伤官，与羊刃同祸，是指阴阳之阳，非牛羊之羊，其义见后论阳刃格中。

- **分字分词释义**：
  - **羊言刚也，刃者宰割之义**：羊刃象征过刚、过盛之力，如刀锋在前，稍有不慎即伤人伤己。
  - **禄过则刃生**：从「禄」发展而来，当福禄与权势过度集中时，就转化为羊刃之险。
  - **极盛之地**：八个「正位」分别对应十干之极盛处，是羊刃之根本所在。
  - **揽辔澄清格**：驿马前临羊刃而得贵人相扶，多主刚正严厉之官，能清乱世，但亦带肃杀之气。
  - **命前三辰 / 命后三辰**：依阴阳与性别取前后三辰各为勾或绞，类似亡劫的对向结构。
  - **爪牙煞、金神白虎并**：提示与刑戮、兵权、猛暴之神同见时，凶性倍增。

- **规范化释义（primary_lang_explained）**：
  羊刃的核心在于「极盛即危」：它并非单纯的凶星，而是力量推到极限后那一道刀锋。禄过则刃生，意味着原本有利的福禄与权势在累积到应退不退时，就会转化为可能伤己伤人的锋刃之气。得位而有官印贵人节制时，羊刃可以表现为极强的行动力、执行力与破局能力，如「揽辔澄清格」那样在乱世中整饬纲纪；失位或煞多无制时，则容易演变为冲动、刚愎、自负甚至暴烈，既损身也损名。

- **完整对等诠释（secondary_lang_full）**：
  Yang Ren, the Goat Blade, is the label for a stem standing at its point of absolute strength where Lu has tipped over into cutting edge.
  It can grant tremendous drive, courage and capacity to break through resistance when guided by sound structures such as officials and seals, but becomes dangerous when mixed with many uncontrolled Sha or when the person lacks inner regulation.
  Modern reading should therefore distinguish between disciplined high energy configurations and genuinely volatile ones, treating Yang Ren as a double edged indicator of extreme activation.
- **核心要点**：
  - 羊刃是「极盛阳刚动能」的标签：既可能成就冲破阻碍的大将之材，也可能带来自损与横祸。
  - 工程化分析时，应将羊刃与官星、印绶、食伤、七煞等结构一并考量，区分「有制之刚」与「失控之刚」，而非简单视为吉或凶。

- **详细解说**：
  1) 在十干与十二支映射中，为每一命局标注 `yang_ren_flag`，记录羊刃是否出现及其所在宫位、与日主的距离与强弱；
  2) 结合官星、印绶与煞星，计算 `yang_ren_control_score`：官印有力、格局清纯者视为「有制」，煞多而官印不及者视为「失控」，居中者标为「部分节制」；
  3) 在风险模型中，将高羊刃强度且失控的结构用于提高意外伤害、冲突升级、激进决策失误等事件的权重；在职业与角色标签中，则在「高压、高风险、高执行力」岗位上提高适配度，但附带更高能耗与风险提示；
  4) 在解释层，用「高能、高压、需节制」的现代语言来描述羊刃，而非简单贴上「凶星」或「英雄」的标签。

 - 反例与边界：
  - 不宜见羊刃便断必有横祸或暴力倾向，很多命盘只是「做事风格偏刚」而已，需结合环境与修为；
  - 若命主所处行业本身风险极低、规则严密（如基础研究、后台技术岗位），羊刃的外显形式多为加班硬扛、意志力强，而非频繁事故；
  - 工程上若将 `yang_ren_flag` 直接视为强负面特征，会低估在高压环境中表现出色的人群，应允许其在不同任务上呈现正负双向作用；
  - 反向误区是浪漫化羊刃，将一切冲动与极端行为美化为「有血性」，模型在解释时应明确区分有节制的担当与失控的冒险。

- 小例（示意）：
  - 某命局日主坐羊刃而又得官印同宫，现实中在高压行业中担任危机处理或一线决策岗位，关键时刻敢于拍板、执行力极强，却也长期处于高负荷状态，系统可用「有制之羊刃」解释其强执行力与高压轨迹，并提示注意身心健康与团队支持；
  - 另一命局羊刃重而无官印制化，又逢七煞、劫煞混杂，现实表现为多次因冲动投资或情绪失控引发事故与人际决裂，系统则将其视为「失控之羊刃」，在建议中强调建立风险规程与情绪管理机制，避免把一时冲动当作勇气。"""
    normalized_text_zh: str = """"""
    subject: str = "羊刃本义与极盛之吉凶"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_yangren', 'bazi_semantic', 'bazi_state_yangren_strength', 'bazi_semantic', 'bazi_state_yangren', 'bazi_semantic', 'bazi_function_factor_14', 'bazi_semantic']
    
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
        l1_anchor="smth_v1.0.0_羊刃本义与极盛之吉凶_001_L1",
    )
    version: str = "1.0.0"
