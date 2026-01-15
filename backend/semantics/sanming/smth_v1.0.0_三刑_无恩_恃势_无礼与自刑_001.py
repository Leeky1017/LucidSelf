"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.264475
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
    semantic_id="smth_v1.0.0_三刑_无恩_恃势_无礼与自刑_001",
    book_id="sanming",
    engine_id="bazi"
)
class 三刑无恩恃势无礼与自刑(SemanticEntry):
    """
    - **原文（source_text）**：  
  论三刑阴符经曰：恩生于害，害生于恩。三刑生于三合，亦如六害生于六合之义。如申子辰三合，加寅卯辰三位，则申刑寅，子刑卯，辰见辰自刑。寅午戌加巳午未，...
    """
    
    original_text: str = """- **原文（source_text）**：  
  论三刑阴符经曰：恩生于害，害生于恩。三刑生于三合，亦如六害生于六合之义。如申子辰三合，加寅卯辰三位，则申刑寅，子刑卯，辰见辰自刑。寅午戌加巳午未，则寅刑巳，午见午，自刑，戌刑未；巳酉丑加申酉戌，则巳刑申，酉见酉自刑，丑刑戌。亥卯未加亥子丑，则亥见亥自刑，卯刑子，未刑丑，合中生刑，犹人夫妇相合而反致刑伤，造化人事，其理一而已矣。经云：金刚火强，自刑其方。木落归本，水流趋东……子、卯一刑也；寅、巳、申二刑也；丑、未戌三刑也。或曰：三刑之法，以数起之……寅、巳、申何以谓之无恩？……又云：丑、戌、未何以谓之恃势？……子卯何以谓之无礼？……辰午、酉、亥何以谓之自刑？……凡命有官星、印绶者，须用官印来刑则吉，若官印被命刑则凶。

- **规范化释义（primary_lang_explained）**：  
  三刑被视为三合局的“内部崩裂形态”，与六害一样，源于原本应当和协的结构。作者先从组合上说明：在申子辰等三合局上叠加寅卯辰等支，便出现申刑寅、子刑卯、辰自刑等局面；其他火局、金局、木局亦然。接着以方位与性质划分金刚火强、木落归本、水流趋东等象，进而在义理上区分“无恩之刑”（寅巳申）、“恃势之刑”（丑戌未）、“无礼之刑”（子卯）与“自刑”（辰午酉亥）四类：无恩之刑重在“忘本克生”、不顾恩德；恃势之刑重在仗持自身旺势压制他人；无礼之刑重在上下失序、子母相刑；自刑则是自身结构过强或失衡，转化为对自己的反噬。文本一再提醒：刑不必然为凶，关键在于“刑上刑下”与“谁来刑谁”，以及是否有官星、印绶等吉神参与，用“以煞止煞”的方式，将刑转化为约束与精炼力量；反之，若官印被命局之刑所伤，则为大凶。

- **完整对等诠释（secondary_lang_full）**：  
  Here, the treatise deepens its exploration of conflict patterns by treating sanctions (xing) as arising precisely where there is greatest potential intimacy and cooperation. Just as the Six Harms emerge from the Six Harmonies, the Three Punishments are said to "grow out of the triads": once additional branches enter a三合局, internal tensions can turn the system against itself. The classification into "no‑gratitude" (wu en), "relying on power" (shi shi), "no‑propriety" (wu li) and "self‑punishment" offers a moralized vocabulary for different ways relationships or personalities can go wrong—forgetting benefactors, abusing strength, violating hierarchy or turning destructive impulses inward. In contemporary structural terms, these correspond to patterns where support structures become sources of pressure, where safety mechanisms over‑tighten, or where self‑discipline collapses into self‑attack. The text also outlines conditions under which punishment can be harnessed productively: when the punishing force is identified with rightful authority (Officer) or protective structure (Seal), and when it checks excess rather than destroying what is vital. This gives a nuanced view: xing is neither purely evil nor purely good, but a high‑tension configuration whose outcome depends on what it falls upon and how it is integrated.

- **核心要点**：
  - 三刑同样“生于三合”，是局内高能量转为内部冲突的表现。
  - 四类刑各有侧重：无恩（忘本克生）、恃势（仗势凌人）、无礼（上下失序）、自刑（自我反噬）。
  - 刑若落在该被约束的过旺之处，且由官印主导，则可成为“制度化的约束力”；反之则成破坏力。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_10_153]` `[trigger: 恩生于害]` `[factor_trigger: ensheng_yuhai AND haisheng_yuen]` `[role: 主干]` 阴符经曰：恩生于害，害生于恩。三刑生于三合，亦如六害生于六合之义。 → 《三命通会》卷十#三刑
  - `[ns_smth_10_154]` `[trigger: 无恩之刑]` `[factor_trigger: wuen_zhixing AND yinsishen_xing]` `[role: 主干依赖]` 寅巳申何以谓之无恩？以寅中有甲木生丙火，丙火生戊土，戊即申位长生，申恩生于寅也。 → 《三命通会》卷十#三刑
  - `[ns_smth_10_155]` `[trigger: 恃势之刑]` `[factor_trigger: shishi_zhixing AND chouxuwei_xing]` `[role: 条件分支]` 丑戌未何以谓之恃势？以丑中有旺水，水墓在辰，辰即戌位……皆恃势以临之。 → 《三命通会》卷十#三刑
  - `[ns_smth_10_156]` `[trigger: 官印刑吉]` `[factor_trigger: guanyin_xingji AND beiminxing_xiong]` `[role: 总结]` 凡命有官星、印绶者，须用官印来刑则吉，若官印被命刑则凶。 → 《三命通会》卷十#三刑

- **详细解说**：  
  工程化时，可为三刑建立一个“目标—载体”模型：谁是施加刑的源头（targetor），谁是被刑的载体（target），再看此二者在命局中各自代表的角色（如官星、印绶、财星、日主等）。当官印之气适度刑制过旺的比劫或食伤时，可以视为“结构优化”；若反之，是日主刑官、财星刑印，则多为“结构破坏”。此外，可将无恩、恃势、无礼、自刑四类，作为心理与关系层面的风险标签：前二者偏向对外攻击与冷酷，后两者偏向关系礼法与自我关系的扭曲。在实际解读中，建议将“三刑”放入“冲—合—害—刑”的整体网络中统一评估，而不是孤立地视为绝对凶兆。

- **校勘与字词辨析（双语）**：
  - **中文**：“恩生于害，害生于恩”一句指出：很多严厉约束最初源于保护与善意，本精校在释义中将其视作“支持结构的阴影面”。
  - **English**: The traditional moral labels (no gratitude, no propriety) are retained, but the analysis recasts them as descriptions of systemic dysfunctions rather than personal condemnation."""
    normalized_text_zh: str = """"""
    subject: str = "三刑：无恩、恃势、无礼与自刑"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_三刑_无恩_恃势_无礼与自刑_001_L1",
    )
    version: str = "1.0.0"
