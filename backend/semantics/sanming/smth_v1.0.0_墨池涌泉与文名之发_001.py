"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412550
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
    semantic_id="smth_v1.0.0_墨池涌泉与文名之发_001",
    book_id="sanming",
    engine_id="bazi"
)
class 墨池涌泉与文名之发(SemanticEntry):
    """
    - **原文（source_text）**：

  墨池涌泉：谓辛巳得癸巳、癸亥。如陈朝议：辛巳、壬辰、癸巳、癸亥是也。推此类，丙寅爱戊寅，戊申爱庚申，己巳爱辛亥，庚午爱壬申，甲戌爱丙寅，壬辰爱甲申，...
    """
    
    original_text: str = """- **原文（source_text）**：

  墨池涌泉：谓辛巳得癸巳、癸亥。如陈朝议：辛巳、壬辰、癸巳、癸亥是也。推此类，丙寅爱戊寅，戊申爱庚申，己巳爱辛亥，庚午爱壬申，甲戌爱丙寅，壬辰爱甲申，皆同此格，主文贵。

- 分字分词释义：

  - **墨池涌泉**：以“墨池”比喻文章学问之源，以“涌泉”比喻才思泉涌，主文章科名之贵。
  - **辛巳得癸巳、癸亥等例**：指特定日柱与时柱或他支成组，既见食神、印绶，又见长生、禄位等相扶之象。
  - **主文贵**：多主以文章、学问、策论取贵，而非纯以武职或财利取胜。

- **规范化释义（primary_lang_explained）**：

  墨池涌泉格，专指一类“才学与气势相互激发”的结构。以辛巳日为例，若再得癸巳、癸亥等时支或配合，则水火相济、金水相生，如同砚池中墨汁因水而涌，写作之笔因气而行。类似的组合尚有丙寅配戊寅、戊申配庚申、己巳配辛亥、庚午配壬申、甲戌配丙寅、壬辰配甲申等，皆偏向“文名之贵”。

- 核心要点：

  - 墨池涌泉以**文采与气势相乘**为主轴，多见食神、印绶、长生、禄位等吉神相配。
  - 多主以文章、辞令、学识、策划等方式获得名望与地位。
  - 忌煞气过重或财星过盛，以致才华沦为奔波谋利或口舌是非。

- 详细解说：

  可以把墨池涌泉看作“高风险高杠杆”的能量点：

  - 对性格：多主刚烈、不服输、行动决断，但也容易偏激、急躁；
  - 对命运：在竞争环境中，墨池涌泉之人往往更敢争、更敢抢，既可能一举成功，也可能因过度冒险而铩羽而归；
  - 对关系：墨池涌泉与财、官纠缠不清时，易在婚姻、合作、上下级关系中产生强烈冲突。

  判断墨池涌泉时，需要兼看：

  1. **力量层面**：墨池涌泉表示日主在文字、策论、学术、司法、策划等领域，容易表现为“文笔有力、条理清楚、情理交融”。若再行运得印、食之助，则科名与职业声望常有佳绩；若行煞、财太过之运，则才华易被卷入纷争、权力斗争或纯粹赚钱事务中，文名反成次要。

  2. **结构层面**：看这股力量是用来生财、任官，还是用在内耗（比劫争财、伤官克官）上。

  3. **时序层面**：看原局是否先具财官之根，再在行运中开花结果。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_125]` `[trigger: 墨池涌泉]` `[factor_trigger: mochi_yongquan AND wencai_zhiyuan]` `[role: 主干]` 墨池涌泉者，辛巳得癸巳、癸亥，以墨池比喻文章学问之源，主文贵。 → 《三命通会》卷六#墨池涌泉与文名之发
  - `[ns_smth_06_126]` `[trigger: 文采气势]` `[factor_trigger: wencai_qishi AND xiangcheng]` `[role: 主干依赖]` 墨池涌泉以文采与气势相乘为主轴，食神印绶长生禄位等吉神相配。 → 《三命通会》卷六#墨池涌泉与文名之发
  - `[ns_smth_06_127]` `[trigger: 煞财过盛]` `[factor_trigger: shaqi_guozhong OR caixing_guosheng]` `[role: 条件分支]` 忌煞气过重或财星过盛，以致才华沦为奔波谋利或口舌是非。 → 《三命通会》卷六#墨池涌泉与文名之发
  - `[ns_smth_06_128]` `[trigger: 墨池结论]` `[factor_trigger: mochi_yongquan AND xingyin_shizhu]` `[role: 总结]` 得墨池涌泉者，多主以文章、辞令、学识、策划等方式获得名望与地位。 → 《三命通会》卷六#墨池涌泉与文名之发

- **校勘与字词辨析（双语）**：

  - "墨池涌泉"一名，本稿直接沿用，不另作拆解，只在释义中以“文章与才思之源”解释。
  - 命例中所列多为历史人物或据传命局，本稿不作史实考据，仅视作结构范本。
  - “主文贵”一语，在现代语境下扩展为“以知识与表达能力取胜”的各种职业形态。
  - **English**：
    - Various career forms where "winning through technical ability" applies are noted."""
    normalized_text_zh: str = """"""
    subject: str = "墨池涌泉与文名之发"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_27', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_degree_12', 'bazi_semantic', 'bazi_state_factor_16', 'bazi_semantic', 'bazi_condition_factor_170', 'bazi_semantic', 'bazi_condition_factor_171', 'bazi_semantic', 'source_ref', 'rel_smth_06_088', 'mochi_yongquan_presence', 'rel_smth_06_089', 'shiyin_jiaohui', 'rel_smth_06_090', 'shacai_guowang_risk', 'evi_smth_06_088', 'mochi_yongquan_presence', 'rule_mochi', 'evi_smth_06_089', 'wenming_fangxiang', 'rule_wengui', 'evi_smth_06_090', 'shacai_guowang_risk', 'rule_shacai', 'map_smth_06_059', 'map_smth_06_060']
    
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
        l1_anchor="smth_v1.0.0_墨池涌泉与文名之发_001_L1",
    )
    version: str = "1.0.0"
