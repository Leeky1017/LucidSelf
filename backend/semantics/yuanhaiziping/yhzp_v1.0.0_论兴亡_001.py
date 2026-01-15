"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559344
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
    semantic_id="yhzp_v1.0.0_论兴亡_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 论兴亡(SemanticEntry):
    """
    - **原文（source_text）**：
  夫人生柱中有纯杀为用也，杀神无制，则为白屋穷途之人、或一豪门营干之士；故要逢制杀运，假杀而起，进用朝廷，操权威福，功不可量。制伏运一入财乡，则能党杀，...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫人生柱中有纯杀为用也，杀神无制，则为白屋穷途之人、或一豪门营干之士；故要逢制杀运，假杀而起，进用朝廷，操权威福，功不可量。制伏运一入财乡，则能党杀，便兴祸患，如此官旺杀旺，运元恐失计。所以命党杀运，倘来生凶，偶然遇流年财杀少旺，杀神相党，并合兴殃；身主孤寒克害，轻则倾家徒配，重则刑弃其身，故其杀神并合，凶亡之可畏也。
  又有柱中月令，正气官星，为一生贵气，惟逢印运则利，盖官星喜逢财旺以生之，印旺以护之；故令其人能行仁布德、纬国经邦、权重爵高，所以贵也。后遇杀神旺乡，杀神禄位，岁杀并临，官化为鬼，丧身必矣。不行杀运、或逢伤官运，又无印绶制之，伤官得地，禄遭伤损，丧妻克子，剥职生灾，立可见矣。
  又有四柱中所专用神，无官杀气，惟偏财正财当旺而已；财神当道，隐隐兴隆，积财聚宝，但少贵矣！欲知且看行运如何？若财逢官禄旺之乡，又成富贵之局。设有不幸，财神脱局，阳刃相逢，财倾福败，多患其凶；及流年冲合阳刃，财神尽伤，元命衰绝，阳刃生凶，败亡极矣！

- **分字分词释义**：
  - **纯杀为用**：七杀纯正无杂，以杀为用神。
  - **杀神无制**：七杀无食神制伏，主贫贱或被人役使。
  - **假杀而起**：借七杀之力化凶为权，功名显达。
  - **财乡党杀**：财星生助七杀，杀势太旺反生祸患。
  - **正气官星**：月令透出纯正官星，主一生贵气。
  - **官喜财印**：官星喜财星来生、印绶来护。
  - **官化为鬼**：官杀混杂或行杀运，官星变为鬼杀，主凶。
  - **伤官得地**：伤官临旺地无印制，主剥职丧妻克子。
  - **财神当道**：财星旺于月令，主富而不贵。
  - **阳刃相逢**：遇阳刃劫财运，财神受伤，主破财败亡。

- **规范化释义（primary_lang_explained）**：
  本篇论述三种主要格局的兴衰成败：
  1. **纯杀格**：七杀无制主贫贱或为人作嫁；行制杀运（食神）则化权显贵。但若入财运党杀，财生杀旺，反生祸患，轻则倾家，重则刑伤。
  2. **正官格**：官星喜财生印护，主贵气显达。若行七杀运，官杀混杂变为鬼，主丧身；行伤官运无印制，主剥职丧妻克子。
  3. **纯财格**：无官杀，专取财星，主富而不贵。若行官禄运，财生官可成富贵；若遇阳刃劫财运，财神受伤，主破财败亡。

- **完整对等诠释（secondary_lang_full）**：
  **On Rise and Fall**:
  1. **Pure Killing Pattern**: Killing without control implies poverty or servitude. Meeting Control Luck (Eating God) brings authority and immense merit. However, entering Wealth Luck supports the Killing, causing disaster; Wealth generating abundant Killing leads to ruin, punishment, or death.
  2. **Correct Officer Pattern**: Officer Star represents nobility, favoring Seal Luck for protection and Wealth for generation. This brings benevolence, statecraft, and high rank. Meeting Killing Luck transforms Officer into Ghost, endangering life. Meeting Injuring Officer Luck without Seal control causes loss of position, wife, and children.
  3. **Pure Wealth Pattern**: Using only Wealth without Officer/Killing implies riches but little nobility. Entering Officer/Salary Luck creates a noble structure. Meeting Yang Blade (Rob Wealth) Luck strips Wealth, causing bankruptcy and ruin.

- **核心要点**：
  - **杀格喜忌**：喜制伏（食伤），忌财党杀
  - **官格喜忌**：喜财印，忌杀混、伤官
  - **财格喜忌**：喜官乡（富贵双全），忌比劫阳刃（破财）

- **详细解说**：  《论兴亡》专论三种主要格局的成败兴衰，是子平法格局成败理论的重要篇章。**纯杀格**——七杀无制主贫贱或为人作嫁，"白屋穷途之人"；行制杀运（食神）则"假杀而起"化凶为权，"进用朝廷，操权威福"。但若入财运"党杀"，财生杀旺，反生祸患，"轻则倾家徒配，重则刑弃其身"。**正官格**——正气官星"为一生贵气"，喜财生印护，"行仁布德，纬国经邦"；若行杀运"官化为鬼"主丧身，行伤官运无印制则"剥职生灾，丧妻克子"。**纯财格**——财神当道主富不贵，"隐隐兴隆，积财聚宝"；若行官禄运"财生官"可成富贵，若遇阳刃劫财运则"财倾福败，败亡极矣"。三种格局各有兴亡之机，核心在于大运配合原局的吉凶转换。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_638]` `[trigger: 杀神无制贫]` `[factor_trigger: qisha_wuzhi AND pinjian]` `[role: 条件分支]` 杀神无制，则为白屋穷途之人；七杀无制主贫贱。 → 《渊海子平·论兴亡》
  - `[ns_yhzp_639]` `[trigger: 假杀化权]` `[factor_trigger: zhisha_yun AND jiasha_huaquan AND gui AND anchong_qugui AND angui]` `[role: 条件分支]` 逢制杀运，假杀而起，进用朝廷，操权威福；制杀化权主贵。 → 《渊海子平·论兴亡》
  - `[ns_yhzp_640]` `[trigger: 财党杀凶]` `[factor_trigger: caiyun AND cai_dangsha AND huohuan]` `[role: 例外处理]` 制伏运一入财乡，则能党杀，便兴祸患；财生杀旺反为祸。 → 《渊海子平·论兴亡》
  - `[ns_yhzp_641]` `[trigger: 正官喜财印]` `[factor_trigger: zhengguan_ge AND xi_caisheng_yinhu AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 正气官星为一生贵气，官星喜逢财旺以生之印旺以护之。 → 《渊海子平·论兴亡》
  - `[ns_yhzp_642]` `[trigger: 官化为鬼]` `[factor_trigger: shayun_wangxiang AND guan_huawei_gui AND xiong AND anchong_qugui AND angui AND killing_pattern]` `[role: 例外处理]` 遇杀神旺乡，官化为鬼，丧身必矣；官杀混杂主凶。 → 《渊海子平·论兴亡》
  - `[ns_yhzp_643]` `[trigger: 财格阳刃败]` `[factor_trigger: caige AND yangren AND yangren_jiecai AND caiqing_fubai]` `[role: 例外处理]` 财神脱局阳刃相逢，财倾福败，败亡极矣；劫财破财主凶。 → 《渊海子平·论兴亡》
  - `[ns_yhzp_644]` `[trigger: 论兴亡纲领]` `[factor_trigger: lun_xingwang AND shage_guange_caige AND yuncheng_peihe]` `[role: 总结]` 论兴亡以杀格官格财格三种格局阐述兴衰成败之机，核心在于运程配合。 → 《渊海子平·论兴亡》"""
    normalized_text_zh: str = """"""
    subject: str = "论兴亡"
    factor_refs: list = ['pure_killing_usage', 'wealth_supports_killing', 'officer_transforms_ghost', 'wealth_escaping_pattern']
    
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
        book_id="yuanhaiziping",
        chapter="",
        l1_anchor="yhzp_v1.0.0_论兴亡_001_L1",
    )
    version: str = "1.0.0"
