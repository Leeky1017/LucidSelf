"""
Auto-generated semantic module for ziwei
Generated at: 2025-12-05T13:30:19.755711
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
    semantic_id="zw_v1.0.0_论人生时安命吉凶_001",
    book_id="ziwei",
    engine_id="ziwei"
)
class 论人生时安命吉凶(SemanticEntry):
    """
    - 分字分词释义：

  - **生时安命吉凶**：以出生时辰的阴阳属性与命宫落点的阴阳属性是否匹配，来判断人生基础顺逆。
  - **六阳时**：寅、午、戌与申、子、辰六个时辰，气机偏阳、外向，与阳...
    """
    
    original_text: str = """- 分字分词释义：

  - **生时安命吉凶**：以出生时辰的阴阳属性与命宫落点的阴阳属性是否匹配，来判断人生基础顺逆。
  - **六阳时**：寅、午、戌与申、子、辰六个时辰，气机偏阳、外向，与阳宫相应则顺。
  - **六阴时**：巳、酉、丑与亥、卯、未六个时辰，气机偏阴、收敛，与阴宫相应则顺。
  - **安命在此六宫者吉**：命宫落在与生时同组（阳配阳、阴配阴）的宫位，象征天时与根基和谐，人生较为顺遂。
  - **阴阳相应**：生时与命宫极性一致，气机和顺，多主根基稳当、行事有据。
  - **阴阳反背**：生时与命宫极性相反（阳时阴宫或阴时阳宫），气机不顺，多主奔波流动。
  - **少逐**：反背者一生"少有定处可逐"，频繁迁徙、职业多变或身份认同不稳。
  - **时辰配命**：将十二时辰分为阴阳两组，与命宫所属的阴阳宫位进行匹配验证。

- 原文（断句）：

  凡男女生在寅午戍、申子辰六阳时，安命在此六宫者吉；生在已酉丑、亥卯未六阴时，安命在此六阴宫者吉。反此则少逐。

- 规范化释义（primary_lang_explained）：

  本条以「生时阴阳」与「安命宫位」的对应为主轴，提出一条极为简要的吉凶规则：若人生于寅、午、戍与申、子、辰这六个偏阳的时辰，而又将命安在同一组阳宫中，则为相应相生，多主根基稳当、行事顺遂；若出生在已、酉、丑与亥、卯、未这六个偏阴的时辰，而命宫也落在六阴宫之内，同样被视为气机相应，较易得天时地利、人事配合。

  反之，若阳时之生而命安阴宫，或阴时之生而命安阳宫，则为阴阳反背，不顺其类。原文以「少逐」简略点出此类命局多主奔波劳碌、难以久安于一处，或是在身份、地域、职业上反复迁徙，少有长久安定。这里的「吉凶」并非简单的好坏二分，而是强调：出生时的阴阳气机，若与命宫落点和谐相应，则一生基础较稳、顺水行舟；若长年逆着这股大势行走，则多见折腾频仍、成事不易。

- 完整对等诠释（secondary_lang_full）：

  This brief rule pairs the yin–yang quality of the birth hour with the house
  where the Life palace is placed. People born in the six yang hours
  (corresponding to Yin, Wu, Xu and Shen, Zi, Chen) are said to fare best when
  their Life palace also falls in this yang group of houses; those born in the
  six yin hours (Yi, You, Chou and Hai, Mao, Wei) are most at ease when their
  Life palace lies within the yin group. In both cases, heaven's timing and the
  chart's anchor point echo one another, giving a sense of moving with the
  current rather than against it.

  When the polarities are crossed—yang hours with a yin Life palace or yin
  hours with a yang Life palace—the text describes life as more "driven about",
  implying frequent moves, restless careers or a general lack of long-term
  settlement. This does not automatically mean disaster, but it marks a
  structure that tends to seek change rather than stay put. The rule therefore
  acts as a background gauge of stability: charts with matching polarities and
  strong structures can rest easier, while mismatched ones call for more effort
  and flexibility to find a harmonious path.

- 核心要点：

  1. 生时被分为六阳时（寅午戍、申子辰）与六阴时（已酉丑、亥卯未）两组。
  2. 阳时生而安命于阳宫，阴时生而安命于阴宫，皆属阴阳相应，多主路向顺势。
  3. 阴阳反背（阳时安命阴宫、阴时安命阳宫）则多主奔波劳碌、难以久安，象征气机不顺。
  4. 此条着重「基础格局」的顺逆，与具体星曜吉凶配合使用，不可孤立一条定人生高下。
  5. 实务中宜先看阴阳相应与否，再结合前文八座与入格等规则综合判断命局稳固程度。

- 叙事素材（narrative_snippets）：

  - **六阳六阴**："寅午戌申子辰为六阳时，巳酉丑亥卯未为六阴时"，生时分阴阳两组。
  - **阴阳相应**："阳时安命阳宫，阴时安命阴宫，皆属阴阳相应"，气机顺势。
  - **阴阳反背**："阳时安命阴宫、阴时安命阳宫，多主奔波劳碌"，气机不顺。
  - **现代应用**：本条可作为评估"命局稳定性"的基础指标，阴阳相应者较易安定。"""
    normalized_text_zh: str = """"""
    subject: str = "论人生时安命吉凶"
    factor_refs: list = ['group_liuyang', 'group_liuyin', 'action_anming', 'state_yinyangxiangying', 'state_yinyangfanbei', 'source_ref', 'rel_anming_001', 'group_liuyang', 'rel_anming_002', 'group_liuyin', 'rel_anming_003', 'state_yinyangfanbei', 'evi_anming_001', 'state_yinyangxiangying', 'rule_anming_xiangying', 'evi_anming_002', 'state_yinyangfanbei', 'rule_anming_fanbei', 'concept_yinyang_match', 'concept_stability']
    
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
        l1_anchor="zw_v1.0.0_论人生时安命吉凶_001_L1",
    )
    version: str = "1.0.0"
