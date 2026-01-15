"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.066607
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
    semantic_id="smth_v1.0.0_1_气象规模与刚柔中和_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1气象规模与刚柔中和(SemanticEntry):
    """
    - 原文（source_text）：
  今夫立四柱而取五行，定一运而关十载。清浊纯驳，万有不齐；好恶是非，理难执一。故古之论命，研究精微，则由体而该用；今之论命，拘泥格局，遂执假而失真。
  是必先...
    """
    
    original_text: str = """- 原文（source_text）：
  今夫立四柱而取五行，定一运而关十载。清浊纯驳，万有不齐；好恶是非，理难执一。故古之论命，研究精微，则由体而该用；今之论命，拘泥格局，遂执假而失真。
  是必先观气象规模，乃富贵贫贱之纲领；次论用神出处，尽死生穷达之精微。不须八字繁华，只要五行和气。浪指三元六甲，谁知万绪千端。学者务要钩玄索隐，发表归根，向实寻虚，从无取有。虽曰命之理微，于此思过半矣。
  然大海从于勺水，少阴产于老阳。成乃败之机，变乃化之渐。此又所当深察。
  乃若一阳解冻，三伏生寒。阳刚不中，亢则害也；刚而能柔，吉之道也。柔弱偏枯，小人之象；刚健中正，君子之风。
  过于寒薄，和暖处终难奋发；过于燥烈，水激处反有凶灾。
  过于执实，事难显豁；过于清冷，思有凄凉。
  过于有情，志无远达；过于用力，成亦多难。
  过于贵人，逢灾自愈；过于恶煞，遇福难享。

- 分字分词释义：
  - **气象规模**：八字的整体格局气势，如雄伟、狭促、清纯、混杂等。
  - **用神出处**：用神是真神还是假神，有根还是无根。
  - **五行和气**：五行流通有情，不相战克。
  - **阳刚不中**：阳气过盛，无阴调和，为亢阳。
  - **柔弱偏枯**：阴气过盛，无阳生发，或五行偏缺。
  - **执实**：固执死板，不通变。
  - **有情**：合多，或贪合忘冲。

- **规范化释义（primary_lang_explained）**：
  论命首先要看八字的气象规模，这是判断富贵贫贱的总纲；其次才论用神的来源和有力与否，以推断生死的细节。不需要八字排得花哨，只要五行之气平和流通。不要被表面的神煞（三元六甲）迷惑，要探求深层的道理。
  如冬至一阳生，夏至一阴生，事物总在变化。阳刚若太过（不中和），就会有亢龙有悔的害处；刚强而能柔顺，才是吉道。柔弱且偏枯（如纯阴无阳），是小人之象；刚健且中正（如阳刚有制），是君子之风。
  命局过于寒薄（金水寒凝），即使行暖运也难奋发；过于燥烈（火炎土燥），行水运激火，反有凶灾。
  过于固执死板（用神死板），事业难显达；过于清冷（金寒水冷），思想多凄凉。
  合多过于有情，往往意志不坚，难成大器；用神太弱需强力扶持（过于用力），虽成也多磨难。
  贵人太多，逢灾虽能解，但依赖心重；恶煞太多，即使有福也难享受（带病延年或有财无寿）。

- 完整对等诠释（secondary_lang_full）：

  This section discusses "Qi-Image Scale and Rigid-Soft Centered Harmony" from the Qi-Xiang Chapter:

  - First observe Qi-Image Scale, this is the outline for wealth-nobility-poverty-baseness; next discuss Use God origin, to exhaustively determine life-death details.
  - Yang-Rigid not centered, excess then harms; rigid yet able soft, is auspicious way. Soft-weak partial-withered, petty person's image; rigid-healthy centered-upright, gentleman's manner.
  - Excessively cold-thin, warm-harmonious place hard to rise; excessively dry-fierce, Water-激 place反 has disaster.
  - Excessively affectionate (many combinations), ambition has no far reach; excessively forceful, achievement also many difficulties.
  - Key: Centered harmony as precious; avoid extremes of cold/hot/rigid/soft; the gentleman is one who knows balance.

- 核心要点：
  - **气象为纲**：先看格局大意，后看用神细节。
  - **中和为贵**：忌偏枯、亢烈、寒薄。
  - **过犹不及**：有情太过、贵人太过皆非美事。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_11_001]` `[trigger: 气象规模]` `[factor_trigger: qixiang_guimo AND fugui_pinjian]` `[role: 主干]` 是必先观气象规模，乃富贵贫贱之纲领；次论用神出处，尽死生穷达之精微。 → 《三命通会》卷十一#气象规模与刚柔中和
  - `[ns_smth_11_002]` `[trigger: 五行和气]` `[factor_trigger: wuxing_heqi AND buqiu_fanhua]` `[role: 主干依赖]` 不须八字繁华，只要五行和气。 → 《三命通会》卷十一#气象规模与刚柔中和
  - `[ns_smth_11_003]` `[trigger: 刚健中正]` `[factor_trigger: gangjian_zhongzheng AND junzi_zhifeng]` `[role: 条件分支]` 柔弱偏枯，小人之象；刚健中正，君子之风。 → 《三命通会》卷十一#气象规模与刚柔中和
  - `[ns_smth_11_004]` `[trigger: 过于有情]` `[factor_trigger: guoyu_youqing AND zhiwu_yuanda]` `[role: 总结]` 过于有情，志无远达；过于用力，成亦多难。 → 《三命通会》卷十一#气象规模与刚柔中和

- 详细解说：
  《气象篇》强调宏观视角。所谓“气象”，是八字整体给人的感觉，如“金白水清”、“木火通明”是清气象，“伤官见官”、“枭印夺食”是浊气象。赋文指出，过寒、过燥、过刚、过柔都是病。特别是“过于有情，志无远达”，指八字合多（如甲己合、乙庚合等），日主贪合忘志，或用神被合绊，导致命主优柔寡断，沉溺于私情或安逸，难有大作为。

- 校勘与字词辨析：
  - **“勺水”**：原文“大海从于勺水”，意指积少成多，源头重要。
  - **“执实”**：指用神单一且无变化，或命主性格固执。
  - **English**：
    - Combined pattern analysis terms clarified; multi-factor interactions explained with systematic logic."""
    normalized_text_zh: str = """"""
    subject: str = "1 气象规模与刚柔中和"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_6', 'bazi_semantic', 'bazi_state_factor_46', 'bazi_semantic', 'bazi_relation_factor_9', 'bazi_semantic', 'bazi_state_factor_47', 'bazi_semantic', 'bazi_condition_wuxing', 'bazi_semantic', 'bazi_factor_21', 'bazi_semantic', 'source_ref', 'rel_smth_11_001', 'qixiang_guimo', 'rel_smth_11_002', 'guoyu_youqing', 'rel_smth_11_003', 'pianku_hanbo', 'evi_smth_11_001', 'qixiang_guimo', 'rule_qixiang_guimo1', 'evi_smth_11_002', 'tanhe_wangzhi', 'rule_guoyu_youqing1', 'evi_smth_11_003', 'zhonghe_zhidao', 'rule_gangrou_zhonghe1', 'map_smth_11_001', 'map_smth_11_002']
    
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
        l1_anchor="smth_v1.0.0_1_气象规模与刚柔中和_001_L1",
    )
    version: str = "1.0.0"
