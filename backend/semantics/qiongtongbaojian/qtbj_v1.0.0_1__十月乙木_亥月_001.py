"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.620114
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
    semantic_id="qtbj_v1.0.0_1__十月乙木_亥月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1十月乙木亥月(SemanticEntry):
    """
    - **原文（source_text）**：
  十月乙木，木不受气，而壬水司令，取丙为用，戊土次之。
  丙戊两透，科甲定然。有丙无戊，虽不科甲，亦入儒林。支多丙火，运入火乡，亦主显达。
  或水多...
    """
    
    original_text: str = """- **原文（source_text）**：
  十月乙木，木不受气，而壬水司令，取丙为用，戊土次之。
  丙戊两透，科甲定然。有丙无戊，虽不科甲，亦入儒林。支多丙火，运入火乡，亦主显达。
  或水多无戊，乙性漂浮，流荡之徒。若不见丙己，妻子难全，或一点壬水，即多见戊土，亦为不妙，得甲制戊，可许能干，但为人好生祸乱，构讼生非，男女一理。
  支成木局，时值小阳，此又如春木同旺，若有癸出，须取戊为尊，加以丙透，科甲之人。若无丙戊二字，自成自败，终非承受之辈。

- **分字分词释义**：
  - **木不受气**：木不受令 / 亥月特征 / 死地
  - **壬水司令**：壬水当权主事 / 印旺 / 水多
  - **儒林**：知识分子阶层 / 读书人 / 有丙无戊
  - **流荡之徒**：四处漂泊的人 / 水多无戊 / 凶象
  - **构讼生非**：构陷诉讼制造是非 / 土多木折 / 性格
  - **小阳春**：农历十月气候温暖 / 木局时 / 似春木
  - **自成自败**：自己成事自己失败 / 无丙戊 / 不能承受

- **规范化释义（primary_lang_explained）**：
  十月（亥月）的乙木，木不受气（死地），而且壬水（印）司令，取丙火（调候/泄秀）为用神，戊土（制水）次之。
  如果丙火和戊土都透出，科甲功名是一定的。有丙火无戊土，虽然不中科甲，也能进入儒林（读书人）。如果地支多丙火（如寅巳），大运进入火乡，也主显达。
  如果水多而没有戊土，乙木本性漂浮，是流荡之徒。如果不见丙火己土，妻子难全。或者只有一点壬水，却见到很多戊土，也不妙（财多身弱/土重木折），如果得甲木制戊土，可以许诺能干，但为人喜欢制造祸乱，构陷诉讼生是非，男女都是这个道理。
  如果地支合成木局（亥卯未），时节正值“小阳春”（十月），这又像春木一样旺盛，如果有癸水出干，必须取戊土为尊（制水），加上丙火透出，是科甲之人。如果没有丙戊这两个字，自成自败，终究不是能承受家业的人。

- **完整对等诠释（secondary_lang_full）**：
  Yi Wood in the 10th Month (Pig Month): Wood does not receive Qi, and Ren Water commands. Take Bing as Useful God, followed by Wu Earth.
  If both Bing and Wu are revealed, Civil Service is certain. With Bing but no Wu, though not Civil Service, one enters the Scholars' Forest. If branches have much Bing Fire, and Luck enters Fire lands, it also implies prominence.
  If Water is abundant without Wu, Yi Wood drifts; one becomes a vagrant. If Bing/Ji are not seen, wife and children are hard to keep. Or if there is a single point of Ren Water but much Wu Earth, it is also not good; obtaining Jia to control Wu promises capability, but the person loves creating chaos and litigation. This applies to both sexes.
  If branches form a Wood frame, and it is "Little Spring" (10th Month), it is as prosperous as Spring Wood. If Gui appears, one must take Wu as supreme; adding Bing revealed makes a Civil Service person. Without Bing/Wu, one succeeds and fails on one's own, ultimately not someone who can sustain success.

- **核心要点**：
  - **首要用神**：丙火（调候）。亥月水旺木寒。
  - **次要用神**：戊土（制水）。水泛木浮需堤坝。
  - **小阳春**：十月有几天气候温暖如春，若成木局，喜丙戊。

- **详细解说**：
  - 亥月是乙木死地，也是壬水旺地。
  - 最大的危险是“水泛木浮”，故戊土极重要。
  - 但寒气已生，丙火解冻是第一义。
  - “小阳春”：指农历十月，坤卦六阴极而一阳生（实际上复卦在子月，但十月往往气候反暖），若木旺，可用类似春木的方法（丙癸戊）。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_205]` `[trigger: 亥月乙木]` `[factor_trigger: month_hai AND tiangan_yi AND tiangan_bing AND tiangan_wu]` `[role: 主干]` 十月乙木，木不受气，而壬水司令，取丙为用，戊土次之。 → 《穷通宝鉴·三冬乙木》#10.1
  - `[ns_qttbj_206]` `[trigger: 流荡之徒]` `[factor_trigger: month_hai AND tiangan_yi AND water_excessive AND NOT tiangan_wu AND water_excess_wood_drift]` `[role: 例外处理]` 水多无戊，乙性漂浮，流荡之徒。 → 《穷通宝鉴·三冬乙木》#10.1
  - `[ns_qttbj_207]` `[trigger: 小阳春]` `[factor_trigger: month_hai AND tiangan_yi AND dizhi_wood_frame]` `[role: 条件分支]` 支成木局，时值小阳，此又如春木同旺。 → 《穷通宝鉴·三冬乙木》#10.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 十月乙木（亥月）"
    factor_refs: list = ['little_spring', 'vagrant', 'scholars_forest']
    
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
        l1_anchor="qtbj_v1.0.0_1__十月乙木_亥月_001_L1",
    )
    version: str = "1.0.0"
