"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492363
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
    semantic_id="zpzq_v1.0.0_七煞格的行运侧重点_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 七煞格的行运侧重点(SemanticEntry):
    """
    - **原文（source_text）**：
  四十、论偏官取运.
  偏官取运，即以偏官所成之局分而配之。煞用食制，煞重食轻则助食，煞轻食重则助煞，煞食均而日主根轻则助身。忌正官之混杂，畏印绶之夺...
    """
    
    original_text: str = """- **原文（source_text）**：
  四十、论偏官取运.
  偏官取运，即以偏官所成之局分而配之。煞用食制，煞重食轻则助食，煞轻食重则助煞，煞食均而日主根轻则助身。忌正官之混杂，畏印绶之夺食.

  煞用印绶，不利财乡，伤官为美，印绶身旺，俱为福地.

  七煞用财，其以财而去印存食者，不利劫财，伤食皆吉，喜财怕印，透煞亦顺.

  其以财而助煞不及者，财已足，则喜食印与帮身；财未足，则喜财旺而露煞.

  煞带正官，不论去官留煞，去煞留官，身轻则喜助身，食轻则喜助食。莫去取清之物，无伤制煞之神.

  煞无食制而用刃当煞，煞轻刃重则喜助煞，刃轻煞重，则宜制伏，无食可夺，印运何伤？七煞既纯，杂官不利.

- 原注（原文注解）：
  　本章承接三十九章，从“动态行运”的角度说明：不同类型的偏官（七煞）格，在行运中应如何配合食、印、财、比、官等力量。重点不在于“见煞即凶”，而在于 **让煞在时间轴上被正确调度**。

  1) **煞用食制之取运**：
  - “煞用食制，煞重食轻则助食，煞轻食重则助煞，煞食均而日主根轻则助身”：
    - 若煞重食轻 → 行运宜“助食”，增强制煞之力；
    - 若煞轻食重 → 行运宜“助煞”，以免食太多而失去制煞对象、反成耗身；
    - 若煞与食均衡而日主根轻 → 行运宜“助身”，使身能承受煞与食两股力量；
    - 总体须“忌正官之混杂，畏印绶之夺食” → 官混则格不清，印过则夺食.

  2) **煞用印绶之取运**：
  - “煞用印绶，不利财乡，伤官为美，印绶身旺，俱为福地”：
    - 以印承煞时，财来多成“破印党煞”，故忌重财之运；
    - 伤官运反而可美：
      - 伤官泄身成秀，又不直接破印；
    - 印绶与日主在行运中得旺，多为福地.

  3) **七煞用财之取运**：
  - “七煞用财，其以财而去印存食者，不利劫财，伤食皆吉，喜财怕印，透煞亦顺”：
    - 若命局以财去印存食，使“食制煞”得以显现：
      - 比劫（劫财）运不利 → 比劫争财，破坏财去印之用；
      - 伤官、食神之运反为吉 → 可加强制煞之力；
      - 喜财运、不喜印运 → 财强化、印削弱，有利于保持“财去印存食”的结构；
      - 煞透于干，行运顺势而行，亦可顺用.

  4) **以财助煞不足之取运**：
  - “其以财而助煞不及者，财已足，则喜食印与帮身；财未足，则喜财旺而露煞”：
    - 若原局财已足够 → 行运应偏向食、印与比劫，以帮身、调和；
    - 若原局财尚不足 → 行运可再行财运，使煞“露而有根”，形成“财生煞”的清格；
    - 这里强调的是“够与不够”，而非一味多财为好.

  5) **煞带正官之取运**：
  - “煞带正官，不论去官留煞，去煞留官，身轻则喜助身，食轻则喜助食。莫去取清之物，无伤制煞之神”：
    - 官煞并存时，最终要“取清”，或官或煞为主；
    - 行运侧重点在于：
      - 身轻 → 先助身，以免官煞双方都克身；
      - 食轻 → 助食，以保留制煞之神；
    - 特别提醒：
      - 不可在行运中把“唯一清晰的制煞之神”去掉，否则难以驾驭煞力.

  6) **煞无食制而用刃当煞之取运**：
  - “煞无食制而用刃当煞，煞轻刃重则喜助煞，刃轻煞重，则宜制伏，无食可夺，印运何伤？七煞既纯，杂官不利”：
    - 当命局以阳刃（比劫之极）当煞而无食制时：
      - 若煞轻刃重 → 行运宜助煞，使刃与煞势均力敌；
      - 若刃轻煞重 → 行运宜制伏（印、食、财等），以免煞压刃；
      - 因局中本无食神可夺印，故印运反不为害；
      - 七煞既纯、杂官反不利 → 强调行运中仍要避免官煞混杂，保持结构单纯.

- 分字分词释义：
  - 偏官取运：以七煞为主格时，选择行运配合的原则；
  - 煞用食制：以食神制煞，使煞为我用；
  - 煞用印绶：以印承煞、化煞护身；
  - 七煞用财：以财生煞或借财清印、存食的结构；
  - 帮身：比肩、劫财之运，增强日主根气；
  - 刃当煞：以阳刃之力抗衡七煞，形成“刃煞对峙”的局面.

- **规范化释义（primary_lang_explained）**：
  若把三十九章看作“七煞静态格局说明书”，本章就是“七煞行运调度手册”：
- **完整对等诠释（secondary_lang_full）**：  
  Luck that touches Seven Killing is judged by how it interacts with the mechanism that already manages Killing in the natal chart. In some patterns, Food is the main tool: strengthening Food years allows sharp pressure to be digested and turned into achievement. In others, Printing must take the lead, bearing and civilising Killing so that risk becomes responsibility. In yet others, Wealth is used to clarify the structure—removing excess Ink or杂煞, preserving the one line of Killing that is actually needed—or even Yang Blade is called in to stand opposite Killing and hold the line.

  The same "Killing year" can therefore rescue or ruin, depending on whether it reinforces the existing chain of control or breaks it. When luck strengthens the right环节 in the system—Food, Printing, Wealth, body or Officer—it helps Seven Killing play its role as a focused, disciplined force. When it amplifies the wrong piece or cuts off the controls, the pattern tips over into uncontrolled danger. Reading Seven Killing luck is thus not about simply liking or fearing Killing, but about seeing which module should be boosted at a given stage so that the whole structure remains stable rather than pushed past its critical point.

  - 同样是偏官格：
    - 有的依靠食神制煞；
    - 有的依靠印绶承煞；
    - 有的依靠财星清印存食；
    - 有的则以阳刃当煞.
  - 行运选择的关键，不在于简单“喜煞”或“忌煞”，而在于：
    - 当前阶段应强化哪一环：食、印、财、身、官？
    - 强化之后，系统是否更稳，还是更接近临界点.

- 详细解说：
  - 偏官取运体现了一种“动态平衡”的思维：
    - 煞不可无，也不可失控；
    - 制煞、护煞、助煞、帮身，四者之间必须随时调整；
  - 对现代工程/决策而言：
    - 七煞类似“高风险配置”：在某些阶段需要加码，在某些阶段必须降杠杆；
    - 本章给出的是一种“根据当前配置决定加减项”的方法，而非一套固定配方.

- **核心要点**：
  - 煞格取运，以煞格所成之局分而配之
  - 煞用食制，运喜身旺，食伤之地
  - 煞用印化，运喜印绶，身旺之方
  - 煞用财滋，运喜财地，身旺印绶

- **叙事素材（narrative_snippets）**：
  - `[ns_zpzy_557]` `[trigger: 七煞格的行运侧重点]` `[role: 主干]` `[factor_trigger: sha_ge_quyun AND yi_shage_suocheng_zhiju_fen_er_pei]` 煞格取运，以煞格所成之局分而配之 → 《子平真诠》#下卷
  - `[ns_zpzy_558]` `[trigger: 七煞格的行运侧重点]` `[role: 条件分支]` `[factor_trigger: sha_yong_shi_zhi AND yunxi_shenwang AND shishang_zhidi]` 煞用食制，运喜身旺，食伤之地 → 《子平真诠》#下卷
  - `[ns_zpzy_559]` `[trigger: 七煞格的行运侧重点]` `[role: 条件分支]` `[factor_trigger: sha_yong_yin_hua AND yunxi_yinshou AND shenwang_zhifang]` 煞用印化，运喜印绶，身旺之方 → 《子平真诠》#下卷
  - `[ns_zpzy_560]` `[trigger: 七煞格的行运侧重点]` `[role: 条件分支]` `[factor_trigger: sha_yong_cai_zi AND yunxi_caidi AND shenwang_yinshou]` 煞用财滋，运喜财地，身旺印绶 → 《子平真诠》#下卷"""
    normalized_text_zh: str = """"""
    subject: str = "七煞格的行运侧重点"
    factor_refs: list = ['pianguan_quyun', 'shayong_shizhi', 'shayong_yinshou', 'rendang_sha', 'engine_id', 'pianguan_quyun_leixing', 'bazi_rule_engine', 'shashi_qiangruo', 'bazi_rule_engine', 'yun_zhisha', 'bazi_rule_engine', 'shage_fengxian', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_146', 'shashi_qiangruo', 'rel_zpzq_147', 'yun_zhisha', 'evi_zpzq_131', 'shashi_qiangruo', 'rule_shashi_yunxiang', 'concept_dynamic']
    
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
        l1_anchor="zpzq_v1.0.0_七煞格的行运侧重点_001_L1",
    )
    version: str = "1.0.0"
