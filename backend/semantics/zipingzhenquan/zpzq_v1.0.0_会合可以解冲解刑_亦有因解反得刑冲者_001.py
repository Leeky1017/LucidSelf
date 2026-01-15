"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.523853
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
    semantic_id="zpzq_v1.0.0_会合可以解冲解刑_亦有因解反得刑冲者_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 会合可以解冲解刑亦有因解反得刑冲者(SemanticEntry):
    """
    - **原文（source_text）**：
  八字支中，刑冲俱非美事，而三会六合，可以解之.假如甲生酉月，逢卯则冲，而或支中有戌，则卯与戌合而不冲；有辰，则酉与辰合而不冲；有亥与未，则卯与亥未会而...
    """
    
    original_text: str = """- **原文（source_text）**：
  八字支中，刑冲俱非美事，而三会六合，可以解之.假如甲生酉月，逢卯则冲，而或支中有戌，则卯与戌合而不冲；有辰，则酉与辰合而不冲；有亥与未，则卯与亥未会而不冲；有巳与丑，则酉与巳丑会而不冲.是会合可以解冲也.又如丙生子月，逢卯则刑，而或支中有戌，则与戌合而不刑；有丑，则子与丑合而不刑；有亥与未，则卯与亥未会而不刑；有申与辰，则子与申辰会而不刑.是会合可以解刑也.又有因解而反得刑冲者，何也？假如甲生子月，支逢二卯相并，二卯不刑一子，而支又逢戌，戌与卯合，本为解刑，而合去其一，则一合而一刑，是因解而反得刑冲也.

- 原注（原文注解）：
  　　本段阐明两层意思：
  - 三会、六合在很多情况下确实可以“解冲、解刑”；
  - 但也有“因解反成”的特殊格局：原欲解刑冲，反因合去一支，使剩余一支独自形成更强的刑冲.

- 分字分词释义：
  - 解冲：通过会合，使原本的六冲关系失去直接对冲的对象.
  - 解刑：通过会合，使原本的三刑关系不再成立.
  - 二卯相并：命局支中有两个卯支并列.
  - 一合而一刑：合走其中一支，剩下的一支反而形成新的刑冲.

- **规范化释义（primary_lang_explained）**：
  地支中的刑冲通常都不是好事，但三会、六合往往可以缓和甚至解除这些紧张关系.比如甲日生于酉月，卯酉相冲；如果命局中再见戌支，则卯与戌合局，使卯不再单独冲酉；或若有辰支，则酉与辰合局，使酉不再被卯直冲；若有亥、未等支，卯与亥未会局；有巳、丑则酉与巳丑会局，这些都属于“会合可以解冲”.同理，丙生子月，卯刑子；若支中有戌、丑、亥未、申辰等，会合形成局，就可以使原本的刑不再成立，这就是“会合解刑”.

  但作者提醒我们，还有一种"因解而反得刑冲"的情况：比如甲生子月，支中有两个卯，两个卯一起看时，二卯反而不去刑一个子（力量分散）；但若支中再出现戌支，戌与其中一个卯相合，本是想"解刑"，结果把一个卯合走，剩下的另一个卯与子重新形成独立的刑冲，于是就变成"一合而一刑".这种格局便是"欲解反成"的典型例子.

- **完整对等诠释（secondary_lang_full）**：  
  Here the text explains how meetings and combinations can relax tension between branches, and also how attempts to resolve a clash can sometimes accidentally create a new one. In the first group of examples, a direct clash or punishment between two branches is neutralised because one of them is drawn into a three‑branch meeting or into a separate combination. Once, for instance, Mao has combined with Xu or entered a meeting with Hai and Wei, it no longer stands alone opposite You, so the original Mao–You clash can no longer act in full. The same logic applies to the example of Bing born in Zi month: if either Zi or Mao is pulled into a combination or meeting with other branches, the punitive relationship between them is weakened or dissolved.

  In the second example, the chart contains two Maos against one Zi. When both Maos are free, the pressure on Zi is dispersed and the punishment does not fully bite. If, however, one Mao is taken away into a combination with Xu in order to "solve" the problem, the remaining Mao now confronts Zi by itself and the punishment becomes sharply focused. What was intended as a remedy then turns into the very cause of harm. This is a warning that we must look at the entire network of branches before concluding that a given meeting or combination has safely cancelled a clash or punishment.

- 详细解说：
  - 会合解冲解刑的原则是“让冲刑双方不再直接对立”，但一旦改变了支数与支位，可能产生新的冲刑结构.
  - 多支同类参与时（如二卯），合走其一可能让剩余一支变得更加突出，反而加强原本欲解之象.
  - 命局的动态性体现在此：一处调整，可能解除一个紧张点，却在另一处形成新的紧张点.

- 核心要点：
  - 会合能解冲刑，但要防“合伴被拉走”导致旧冲复现；
  - 多支同类参与的刑冲局，要防“合去其一，剩一反烈”的情况；
  - 分析时需整体观照，不可只看某一支的会合就断“刑冲全解”.

- 应用推演：
  1) 先标出所有冲刑结构（如子午、卯酉、子卯等）；
  2) 再查有无三会或六合参与，与这些支形成会合关系；
  3) 对多支同类者，特别注意“合走其一后余支的状态”；
  4) 综合判断：到底是“真正解冲解刑”，还是“解一处而成另一处冲刑”.

- 反例与边界：
  - 见会合就简单断“冲刑皆解”，不看支数与分布，容易漏掉“因解反成”的情况；
  - 把任何“合”都视为吉，不考虑它可能带来新的冲刑焦点.

- 小例（示意）：
  - 命局有子、卯、卯三支，初看二卯不刑一子；若再遇戌，会合一卯，剩余子卯反成独立刑局，此时要提高对有关六亲的注意.

- 校勘与字词辨析：
  - “二卯不刑一子，而支又逢戌”句，本精校版依照原意解释为“多卯时初不刑子，后因戌合而留一卯成刑”，以免误解.

---




- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_264]` `[trigger: 命理要义]` `[factor_trigger: benjie_hexin_mingli AND lunshu_yaodian]` `[role: 主干]` 本节核心命理论述。 → 《子平真诠》#第55节
  - `[ns_zpzy_265]` `[trigger: 实践要领]` `[factor_trigger: duanming_shijian AND yaoling_zonghe]` `[role: 主干]` 断命实践要领。 → 《子平真诠》#上卷
  - `[ns_zpzy_266]` `[trigger: 边界条件]` `[factor_trigger: shiyong_tiaojian AND bianjie_xianzhi]` `[role: 条件分支]` 适用条件与边界。 → 《子平真诠》#上卷
  - `[ns_zpzy_267]` `[trigger: 用神无力]` `[factor_trigger: yongshen_wuli=true AND result=pinjian_nanmian]` `[role: 主干]` 用神无力，贫贱难免。 → 《子平真诠》#上卷"""
    normalized_text_zh: str = """"""
    subject: str = "会合可以解冲解刑，亦有因解反得刑冲者"
    factor_refs: list = ['jiechong', 'jiexing', 'duozhi_tonglei', 'yihe_yixing', 'engine_id', 'yuanshi_xingchong', 'bazi_rule_engine', 'huihe_zhishu', 'bazi_rule_engine', 'huihe_wendingdu', 'bazi_rule_engine', 'jiechong_jiexing_net', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_072', 'jiechong', 'rel_zpzq_073', 'yihe_yixing', 'evi_zpzq_072', 'jiechong', 'rule_huihe_jiechong', 'evi_zpzq_073', 'yihe_yixing', 'rule_yinjie_fancheng', 'concept_resolution', 'concept_backfire']
    
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
        book_id="zipingzhenquan",
        chapter="",
        l1_anchor="zpzq_v1.0.0_会合可以解冲解刑_亦有因解反得刑冲者_001_L1",
    )
    version: str = "1.0.0"
