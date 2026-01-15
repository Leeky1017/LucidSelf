"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559355
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
    semantic_id="yhzp_v1.0.0_1__宝法第一_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 1宝法第一(SemanticEntry):
    """
    - **原文（source_text）**：
  夫，禀阴阳而生天地间，故造化之赋于人也，禀造化而生；物亦如之，莫不由阴阳变化。是故，推人吉凶休咎，斯理昭著；然术家之法固多，究征索子平之外未有矣！
 ...
    """
    
    original_text: str = """- **原文（source_text）**：
  夫，禀阴阳而生天地间，故造化之赋于人也，禀造化而生；物亦如之，莫不由阴阳变化。是故，推人吉凶休咎，斯理昭著；然术家之法固多，究征索子平之外未有矣！
  子平一法，专以日干为主，而取提纲所藏之物为令；次及年月时支以表其端。
  凡格用月令提纲，勿于傍求年日时为格；今人多不知其法，于此百法百失。
  譬如月令，以金木水火土为要，但有一事而定言之，若于傍求，则有失误；取其月令实事，则以遍求轻重浅深格局破冲可也。
  西山易鉴先生得其变通，将干格分为六格为重：'曰官、曰印、曰财、曰杀、曰食神、曰伤官'，而消息之，无不验矣！其法曰：'逢官看财，逢杀看印，逢印看官'，斯有奥妙不传之法。取四者不偏不倚、生克制化，而遇破体囚为下运；有生有去为福，有助有剥为祸。

- **分字分词释义**：
  - **专以日干为主**：论命以日干为核心，称"日主"或"日元"。
  - **提纲所藏之物为令**：月令所藏天干为定格用神之本。
  - **勿于傍求年日时为格**：不可在年日时支乱取格局，必以月令为准。
  - **月令以金木水火土为要**：月令本气决定格局五行属性。
  - **六格为重**：官、印、财、杀、食神、伤官为六大正格。
  - **逢官看财**：见官星需查财星是否相生。
  - **逢杀看印**：见七杀需查印绶是否化解。
  - **逢印看官**：见印绶需查官星是否相生。
  - **不偏不倚生克制化**：取用须中和平衡，生克制化有情。

- **规范化释义（primary_lang_explained）**：
  本篇强调子平法的正统性与核心法则：
  1. **日主与提纲**：专以日干为主，取月令提纲所藏之物为用神，不可在年日时支乱取格局。
  2. **六格法**：引西山易鉴先生法，定正官、正印、财、七杀、食神、伤官为六大正格。
  3. **相生法则**：逢官看财（财生官），逢杀看印（印化杀），逢印看官（官生印）。强调生克制化的中和平衡。

- **完整对等诠释（secondary_lang_full）**：
  **Precious Method I**:
  - **Ziping Fundamentals**: Focus exclusively on Day Stem as master and Month Command's hidden elements as the order. Do not seek patterns in Year/Day/Hour branches randomly.
  - **Six Patterns**: Citing Master Xishan Yijian, divide patterns into six priorities: Officer, Seal, Wealth, Killing, Eating God, Injuring Officer.
  - **Usage Rules**: "Meeting Officer, look for Wealth; meeting Killing, look for Seal; meeting Seal, look for Officer." This highlights the cycle of generation and protection needed for auspicious patterns.

- **核心要点**：
  - **提纲为重**：格局必取月令
  - **六格正统**：官印财杀食伤六格
  - **相生互护**：官赖财生，杀赖印化

- **详细解说**：  《宝法第一》是子平法定格取用的核心理论篇章，开篇即确立"专以日干为主，而取提纲所藏之物为令"的根本原则。"勿于傍求年日时为格"警告学者不可被年日时支的五行迷惑而误取格局，"今人多不知其法，于此百法百失"。本篇引用西山易鉴先生的"六格法"——官、印、财、杀、食神、伤官为六大正格，并提出核心口诀："逢官看财，逢杀看印，逢印看官"。此法揭示了格局成立的条件：官格需财星相生，杀格需印绶化解，印格需官星护身。"有生有去为福，有助有剥为祸"则概括了吉凶判断的基本原则：有相生有去处为福，有相助有克剥则为祸。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_645]` `[trigger: 日干为主提纲为令]` `[factor_trigger: rigan_weizhu AND tigang_weiling]` `[role: 主干]` 子平一法，专以日干为主，而取提纲所藏之物为令。 → 《渊海子平·宝法第一》
  - `[ns_yhzp_646]` `[trigger: 勿傍求取格]` `[factor_trigger: yueling_tigang_quege AND wu_pangqiu_nianrishi]` `[role: 主干依赖]` 凡格用月令提纲，勿于傍求年日时为格；今人多不知其法于此百法百失。 → 《渊海子平·宝法第一》
  - `[ns_yhzp_647]` `[trigger: 六格为重]` `[factor_trigger: liuge AND guan_yin_cai_sha_shishen_shangguan AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 西山易鉴先生将干格分为六格为重：曰官曰印曰财曰杀曰食神曰伤官。 → 《渊海子平·宝法第一》
  - `[ns_yhzp_648]` `[trigger: 逢官看财]` `[factor_trigger: fengguan_kancai AND fengsha_kanyin AND fengyin_kanguan AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 逢官看财，逢杀看印，逢印看官；斯有奥妙不传之法。 → 《渊海子平·宝法第一》
  - `[ns_yhzp_649]` `[trigger: 有生有去]` `[factor_trigger: yousheng_youqu AND fu AND youbo AND huo]` `[role: 条件分支]` 有生有去为福，有助有剥为祸；生克制化不偏不倚。 → 《渊海子平·宝法第一》
  - `[ns_yhzp_650]` `[trigger: 宝法一纲领]` `[factor_trigger: baofa_diyi AND rigan_yueling_liuge]` `[role: 总结]` 宝法第一以日干为主月令为格六格为重，逢官看财逢杀看印为核心法则。 → 《渊海子平·宝法第一》"""
    normalized_text_zh: str = """"""
    subject: str = "1. 宝法第一"
    factor_refs: list = ['officer_wealth_generation', 'killing_seal_transformation', 'pattern']
    
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
        l1_anchor="yhzp_v1.0.0_1__宝法第一_001_L1",
    )
    version: str = "1.0.0"
