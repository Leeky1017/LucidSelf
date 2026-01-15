"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620035
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
    semantic_id="qtbj_v1.0.0_3__二月乙木_卯月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 3二月乙木卯月(SemanticEntry):
    """
    - **原文（source_text）**：
  二月乙木，阳气渐升，木不寒矣，以丙为君，癸为臣，丙癸两透，不透庚金，大富大贵。
  或天干透庚，支下无辰，不能化金，得癸透养木亦为贵，若见水库，则为假...
    """
    
    original_text: str = """- **原文（source_text）**：
  二月乙木，阳气渐升，木不寒矣，以丙为君，癸为臣，丙癸两透，不透庚金，大富大贵。
  或天干透庚，支下无辰，不能化金，得癸透养木亦为贵，若见水库，则为假化，平常人也。
  二月乙木，耑用丙癸，或支成木局，有癸透乃作贵命，更得丙泄木气，上上之命，但须透癸。或水多困丙，多戊化癸，皆下格。
  用丙者，木妻、火子。用癸者，金妻、水子。
  亥卯未逢于甲乙，富贵无疑。木全寅卯辰方，功名有准。活木忌埋根之铁，支下有庚辛，戕贼其根，木则朽矣。

- **分字分词释义**：
  - **阳气渐升**：阳气逐渐上升 / 卯月特征 / 木不寒
  - **以丙为君**：以丙火为主 / 首选用神 / 君臣之道
  - **癸为臣**：癸水为辅 / 次要用神 / 辅佐
  - **假化**：假的化气格 / 合而不化 / 平常
  - **曲直**：曲直仁寿格 / 木局 / 身旺
  - **埋根之铁**：埋在根部的铁器 / 地支金 / 大忌
  - **戕贼其根**：残害其根基 / 申酉克寅卯 / 凶象

- **规范化释义（primary_lang_explained）**：
  二月（卯月）的乙木，阳气逐渐上升，木不再寒冷了。以丙火为君（主要），癸水为臣（辅助）。如果丙火和癸水都透出，且不透出庚金（伤官见官/克木），是大富大贵的命。
  如果天干透出庚金，地支没有辰土（乙庚合金需辰戌丑未月），不能化气为金，此时若得到癸水透出滋养木（并化泄庚金），也算是贵命。如果地支见辰（水库），则可能是假化格，平常人。
  二月乙木，专用丙火和癸水。如果地支合成木局（曲直格或身旺），有癸水透出才算贵命（润局），若更得到丙火泄木气（木火通明），是上上之命，但必须透出癸水（防木枯）。如果水多困住丙火，或土多克制癸水，都是下等格局。
  亥卯未（木局）在甲乙日遇到，富贵无疑。木全寅卯辰东方一气，功名有准。活木（春木）忌讳“埋根之铁”，如果地支下有庚辛金（如申酉），残害木的根基，木就朽烂了。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 2nd Month (Rabbit Month): Yang Qi rises gradually, and Wood is no longer cold. Take Bing as the Sovereign (Ruler) and Gui as the Subject (Minister). If both Bing and Gui are revealed and Geng Metal is not, it is a life of great wealth and nobility.
  If Geng is revealed on the stems but there is no Chen in the branches, it cannot transform into Metal. If Gui is revealed to nourish the Wood (and leak Geng), it is also noble. If a Water treasury (Chen) is seen, it might be a fake transformation, leading to an ordinary life.
  For Yi Wood in the 2nd Month, exclusively use Bing and Gui. If branches form a Wood frame, having Gui revealed makes a noble life; obtaining Bing to leak the Wood Qi makes it a supreme life, but Gui must be revealed. If abundant Water traps Bing, or abundant Wu Earth neutralizes Gui, they are lower patterns.
  If Hai-Mao-Wei (Wood Frame) meets Jia/Yi, wealth and nobility are undoubted. If Wood completes the Eastern direction (Yin-Mao-Chen), fame is assured. Live Wood dreads "Iron Buried at the Root"; if branches contain Geng/Xin Metal damaging the root, the Wood becomes rotten.

- **核心要点**：
  - **君臣之道**：丙君癸臣。卯月阳气升，重在发荣（丙），辅以滋润（癸）。
  - **忌金**：春乙为活木，忌庚辛金克根（埋根之铁）。
  - **曲直/方局**：亥卯未或寅卯辰，喜丙癸配合（木火通明且有润）。

- **详细解说**：
  - 卯月乙木建禄，身旺。
  - “不透庚金”：乙木柔弱，最怕金克，且庚金合乙，羁绊用神。
  - “埋根之铁”：这是针对活木的著名论断。活木（尤其春木）地支忌见申酉金冲克寅卯根，根损则死。
  - 假化：乙庚合，生于卯月木旺，无法化金，若见辰（湿土生金）则似化非化，为假化。
- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_177]` `[trigger: 卯月乙木]` `[factor_trigger: month_mao AND tiangan_yi AND bing_revealed AND gui_revealed AND NOT tiangan_geng]` `[role: 主干]` 二月乙木，阳气渐升，木不寒矣，以丙为君，癸为臣，丙癸两透，不透庚金，大富大贵。 → 《穷通宝鉴·三春乙木》#7.3
  - `[ns_qttbj_178]` `[trigger: 埋根之铁]` `[factor_trigger: tiangan_yi AND season_spring AND (dizhi_shen OR dizhi_you) AND iron_buried_at_root]` `[role: 例外处理]` 活木忌埋根之铁，支下有庚辛，戕贼其根，木则朽矣。 → 《穷通宝鉴·三春乙木》#7.3
  - `[ns_qttbj_179]` `[trigger: 曲直格]` `[factor_trigger: (tiangan_jia OR tiangan_yi) AND (dizhi_wood_frame OR dizhi_east_direction)]` `[role: 条件分支]` 亥卯未逢于甲乙，富贵无疑。木全寅卯辰方，功名有准。 → 《穷通宝鉴·三春乙木》#7.3"""
    normalized_text_zh: str = """"""
    subject: str = "3. 二月乙木（卯月）"
    factor_refs: list = ['sovereign_subject', 'iron_buried_at_root', 'pattern_fake_transformation']
    
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
        l1_anchor="qtbj_v1.0.0_3__二月乙木_卯月_001_L1",
    )
    version: str = "1.0.0"
