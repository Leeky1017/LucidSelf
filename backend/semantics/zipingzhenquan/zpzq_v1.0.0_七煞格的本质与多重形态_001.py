"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492350
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
    semantic_id="zpzq_v1.0.0_七煞格的本质与多重形态_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 七煞格的本质与多重形态(SemanticEntry):
    """
    - **原文（source_text）**：
  三十九、论偏官。
  煞以攻身，似非美物，百大贵之格，多存七煞。盖控制得宜，煞为我用，如大英雄大豪杰，似难驾驭，而处之有方，则惊天动地之功，忽焉而就。...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十九、论偏官。
  煞以攻身，似非美物，百大贵之格，多存七煞。盖控制得宜，煞为我用，如大英雄大豪杰，似难驾驭，而处之有方，则惊天动地之功，忽焉而就。此王侯将相所以多存七煞也。

  七煞之格局亦不一：煞用食制者，上也，煞旺食强而身健，极为贵格。如乙亥、乙酉、乙卯、丁丑，极等之贵也。

  煞用食制，不要露财透印，以财能转食生煞，而印能去食护煞也。然而财先食后，财生煞而食以制之，或印先食后，食太旺而印制，则格成大贵。如脱脱丞相命，壬辰、甲胡、丙戌、戊戌，辰中暗煞，壬以透之，戊坐四支，食太重而透甲印，以损太过，岂非贵格？若煞强食泄而印露，则破局矣。

  有七煞用印者，印能护煞，本非所宜，而印有情，便为贵格。如何参政命，丙寅、戊戌、壬戌、辛丑，戊与辛同通月令，是煞印有情也。

  亦有煞重身轻，用食则身不能当，不若转而就印，虽不通根月令，亦为无情而有情。格亦许贵，但不大耳。

  有煞而用财者，财以党煞，本非所喜，而或食被制，不能伏煞，而财以去印存食，便为贵格。如周丞相命，戊戌、甲子，丁未、庚戌，戊被制不能伏煞，时透庚财，即以清食者，生不足之煞。生煞即以制煞，两得其用，尤为大贵。

  又有身重煞轻，煞又化印，用神不清，而借财以清格，亦为贵格。如甲申、乙亥、丙戌、庚寅，刘运使命是也。

  更有杂气七煞，干头不透财以清用，亦可取贵。

  有煞而杂官者，或去官，或去煞，取清则贵。如岳统制命，癸卯、丁巳、庚寅、庚辰，去官留煞也。夫官为贵气，去官何如去煞？岂知月令偏官，煞为用而官非用，各从其重。若官格杂煞而去官留煞，不能如是之清矣。如沈郎中命，丙子、甲午、辛亥、辛卯，子冲午而克煞，是去煞留官也。

  有煞无食制而用印当者，如戊辰、甲寅、戊寅、戊午、赵员外命是也。

  至书有制煞不可太过之说，虽亦有理，然运行财印，亦能发福，不可执一也，乃若弃命从煞，则于外格详之。

- 原注（原文注解）：
  　　本章是八格详论中极为关键的一篇，专门说明七煞格（偏官格）的多种形态与成格条件。
  - 开篇点明七煞的本质：
    - "煞以攻身，似非美物"——七煞克身，表面上是凶险之力；
    - "百大贵之格，多存七煞"——然而历史上王侯将相，多有七煞入格者；
    - "控制得宜，煞为我用"——关键在于"驾驭"：如大英雄豪杰，处之有方，可成惊天动地之功。
  - 随后分类说明七煞格的各种成格路径：
    1) **煞用食制**：最上等的煞格，煞旺、食强、身健三者兼备；
    2) **煞用印绶**：印能护煞，须印有情方成贵格；
    3) **煞用财星**：财以去印存食，或清格助煞，使煞得其用；
    4) **煞杂官星**：需去官留煞或去煞留官，取清则贵；
    5) **煞无食制而用刃**：以阳刃当煞，形成刃煞对峙。
  - 末段提醒：
    - "制煞不可太过"有理，但也不可执一；
    - "弃命从煞"另属外格，非本章讨论重点。

- 分字分词释义：
  - 煞以攻身：七煞克制日主，象征压力与挑战。
  - 控制得宜：驾驭有方、节制有度。
  - 煞用食制：以食神克制七煞，使其为我所用。
  - 煞用印绶：以印星承接七煞之气，化煞生身。
  - 财以党煞：财星生助七煞，使煞更旺。
  - 去印存食：以财克去印星，保留食神制煞之用。
  - 煞杂官星：七煞与正官同见，需取清方贵。
  - 弃命从煞：日主弱极而从七煞之势，属外格。

- **规范化释义（primary_lang_explained）**：
  本章是子平真诠八格详论的核心篇章之一，专门讨论偏官（七煞）格。作者开宗明义：七煞虽以攻身为本，看似凶险，但历史上大贵之人，多有七煞入格者——关键在于"控制得宜"。如同大英雄豪杰，难以驾驭，但若处之有方，反能成就惊天动地之功业。

  作者随后详细分类七煞格的各种成格路径：
  1) **煞用食制**：最上等的煞格形态。要求煞旺、食强、身健三者兼备，以食神克煞而成格。但需注意：不宜露财透印，财会转食生煞，印会去食护煞。除非财先食后、或印先食后的特殊配置，方能成大贵格。
  2) **煞用印绶**：印本护煞，非上选，但若印有情（与日主、与煞皆有妥当的生克关系），亦可成贵格。尤其煞重身轻时，用食则身难当，转而就印反为得宜。
  3) **煞用财星**：财本党煞非喜，但在特定配置下（如财以去印存食），反能清格成贵。
  4) **煞杂官星**：官煞同见，需去一留一取清。去官留煞或去煞留官，视月令用神之重而定。
  5) **煞无食制而用刃**：以阳刃当煞，刃煞对峙，亦是一种成格之道。

- **完整对等诠释（secondary_lang_full）**：
  This chapter stands as one of the key discussions in the Eight Patterns system, focusing on the Seven Killings (偏官) pattern. The author opens by acknowledging that Killing attacks the Day Master and appears dangerous, yet points out that throughout history many of the truly eminent—kings, ministers, generals—have had Seven Killings prominently placed in their charts. The secret lies in proper control: like a great hero who seems unmanageable, when handled with skill the Killing can accomplish extraordinary feats.

  The chapter then classifies the various ways a Killing pattern can successfully form: (1) Killing controlled by Food God—the finest type, requiring strong Killing, strong Food, and robust Day Master working together; (2) Killing using Resource—where Resource receives Killing's energy and transforms it to nourish the Day Master; (3) Killing using Wealth—where Wealth clears away blocking Resource to preserve Food's controlling function; (4) Killing mixed with Officer—requiring clarification by removing one or the other; (5) Killing without Food control using Blade—where Yang Blade stands against Killing in direct confrontation. The author closes by noting that while "over-controlling Killing" has its pitfalls, one should not be rigid about any single approach, and that "abandoning life to follow Killing" belongs to the separate discussion of External Patterns.

- 核心要点：
  - 七煞格的本质："煞为我用"而非"煞害我身"——驾驭得当可成大贵。
  - 五种主要成格路径：食制、印承、财清、官煞取清、刃当煞。
  - 判断优先级：先看煞与身的强弱比较，再看有无食制或印承，最后看配置是否清纯。
  - 警示：制煞不可太过，亦不可不及；弃命从煞另属外格。

- 应用推演：
  1) 见七煞入格，先问：煞强还是身强？
  2) 再看：有无食神可制？有无印星可承？
  3) 判断成格类型：食制为上，印承次之，财清再次，刃当为险格。
  4) 检查清浊：官煞是否混杂？财印是否互碍？
  5) 预判行运：不同煞格类型，行运取舍完全不同（详见下章）。

- 反例与边界：
  - 见七煞就断凶，不看是否有食制或印承；
  - 煞旺无制而强行断为贵格；
  - 官煞混杂却不取清，格局不纯。

- 校勘与字词辨析：
  - "百大贵之格，多存七煞"：强调七煞与大贵之关联，非谓凡煞皆贵。
  - "如大英雄大豪杰，似难驾驭，而处之有方"：比喻七煞如英雄豪杰，需善加驾驭。"""
    normalized_text_zh: str = """"""
    subject: str = "七煞格的本质与多重形态"
    factor_refs: list = ['qisha', 'shayong_shizhi', 'shayong_yinshou', 'shaza_guanxing', 'kongzhi_deyi', 'engine_id', 'qishage_leixing', 'bazi_rule_engine', 'shashen_qiangruo', 'bazi_rule_engine', 'zhisha_liliang', 'bazi_rule_engine', 'guansha_qingzhuo', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_144', 'zhisha_liliang', 'rel_zpzq_145', 'guansha_qingzhuo', 'evi_zpzq_129', 'qishage_leixing', 'rule_qisha_gui', 'evi_zpzq_130', 'kongzhi_deyi', 'rule_qisha_jiyu', 'concept_challenge', 'concept_mastery']
    
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
        l1_anchor="zpzq_v1.0.0_七煞格的本质与多重形态_001_L1",
    )
    version: str = "1.0.0"
