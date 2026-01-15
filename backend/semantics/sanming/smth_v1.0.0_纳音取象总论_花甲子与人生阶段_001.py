"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228119
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
    semantic_id="smth_v1.0.0_纳音取象总论_花甲子与人生阶段_001",
    book_id="sanming",
    engine_id="bazi"
)
class 纳音取象总论花甲子与人生阶段(SemanticEntry):
    """
    - **原文（source_text）**：
  论纳音取象：昔者黄帝将甲子分轻重而配成六十，号曰花甲子。其花字诚为奥妙，圣人借意而喻之，不可着意执泥。夫自子至亥，十二宫各有金木水火土之属，始起于子为...
    """
    
    original_text: str = """- **原文（source_text）**：
  论纳音取象：昔者黄帝将甲子分轻重而配成六十，号曰花甲子。其花字诚为奥妙，圣人借意而喻之，不可着意执泥。夫自子至亥，十二宫各有金木水火土之属，始起于子为一阳，终于亥为六阴。其五行所属，金木水火土，在天为五星，于地为五岳，于德为五常，于人为五脏，其于命也为五行。是故甲子之属乃应之于命，命则一世之事，故甲子纳音象，圣人喻之，亦如人一世之事也。

- **分字分词释义**：
  - **花甲子**：六十甲子，花指繁复变化。
  - **分轻重**：区分轻重不同。
  - **不可着意执泥**：不可死板执着。
  - **十二宫**：十二地支。
  - **一阳**：子为一阳初生。
  - **六阴**：亥为六阴终结。
  - **五星五岳五常五脏**：五行的不同对应。
  - **一世之事**：人一生的事。

- **规范化释义（primary_lang_explained）**：
  讨论纳音取象：从前黄帝将甲子区分轻重而配成六十组，称为花甲子。这个"花"字确实奥妙，圣人借此来比喻，不可死板执着。从子到亥，十二宫各有金木水火土的归属，开始于子为一阳初生，终结于亥为六阴完成。五行所属的金木水火土，在天是五大行星，在地是五岳名山，在德行是五常，在人体是五脏，在命理就是五行。所以甲子的归属对应到命理，命理就是人一生的事，所以甲子纳音的象征，圣人用来比喻，就像人一生的事情一样。

- **完整对等诠释（secondary_lang_full）**：
  Discussing Nayin symbolic imagery: In ancient times Yellow Emperor distinguished the Jiazi according to weight and paired them into sixty combinations, called Flower Jiazi. The character "flower" is truly wondrous—sages borrowed this meaning as metaphor, not to be rigidly clung to. From Zi to Hai, the Twelve Palaces each belong to Metal-Wood-Water-Fire-Earth, beginning at Zi as one yang emerging, ending at Hai as six yin complete. The Five Elements Metal-Wood-Water-Fire-Earth: in Heaven are Five Planets, on Earth are Five Sacred Mountains, in virtue are Five Constants, in humans are Five Viscera, in destiny are Five Elements. Therefore Jiazi's attributions correspond to destiny, and destiny is one lifetime's affairs. Thus the Sixty Jiazi Nayin imagery that sages use as metaphor represents a human lifetime's journey.

- **核心要点**：
  - 花甲子：六十甲子繁复变化
  - 十二宫配五行
  - 子为一阳始，亥为六阴终
  - 五行多重对应：五星五岳五常五脏
  - 纳音象征人的一生

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_174]` `[trigger: 纳音取象总论]` `[factor_trigger: flower_jiazi AND twelve_palaces AND five_elements_correspondences]` `[role: 主干]` 黄帝将甲子分轻重而配成六十，号曰花甲子。其五行所属，在天为五星，于地为五岳，于德为五常，于人为五脏，其于命也为五行。 → 《三命通会》卷一#纳音取象总论

- **详细解说**：
  此条是纳音取象理论的总纲。黄帝创造六十甲子，称"花甲子"，"花"字暗含繁复变化、绚烂多彩之意。十二地支（十二宫）各配五行，从子（一阳生）到亥（六阴完），形成完整循环。五行不是孤立的，有多重对应：天上对应五大行星（金木水火土星），地上对应五岳（东岳泰山属木，西岳华山属金等），道德对应五常（仁义礼智信），人体对应五脏（肝心脾肺肾）。在命理学中，六十甲子纳音就是用这套五行体系来象征人的一生：从胎孕（子丑）到成长（寅卯）到壮年（辰巳午未）到衰老（申酉戌亥），就像人生的完整历程。这是用宇宙规律来比拟人生的宏大框架。

- **校勘与字词辨析（双语）**：
  - **中文**："花甲子"又称"花甲"，因天干地支配合循环一周为六十，如花朵般繁复。"不可着意执泥"指不可拘泥于字面。"一阳"指冬至子月阳气初生，"六阴"指亥月阴气至盛。
  - **English**: "Flower Jiazi" also called "Flower Sixty," because Stems-Branches complete one cycle at sixty, intricate like flower petals. "Not rigidly cling" means not to be literal. "One yang" refers to yang qi emerging at winter solstice Zi month; "six yin" refers to yin qi at its peak in Hai month."""
    normalized_text_zh: str = """"""
    subject: str = "纳音取象总论：花甲子与人生阶段"
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
        l1_anchor="smth_v1.0.0_纳音取象总论_花甲子与人生阶段_001_L1",
    )
    version: str = "1.0.0"
