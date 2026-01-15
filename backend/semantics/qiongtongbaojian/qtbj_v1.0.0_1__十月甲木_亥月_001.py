"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.619986
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
    semantic_id="qtbj_v1.0.0_1__十月甲木_亥月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 1十月甲木亥月(SemanticEntry):
    """
    - **原文（source_text）**：
  十月甲木，庚丁为要，丙火次之。忌壬水泛身，须戊土制之。
  若庚丁两透，又加戊出干，名曰去浊留清，富贵之极，即乏丁火，亦稍有富贵。
  或甲多制戊，庚...
    """
    
    original_text: str = """- **原文（source_text）**：
  十月甲木，庚丁为要，丙火次之。忌壬水泛身，须戊土制之。
  若庚丁两透，又加戊出干，名曰去浊留清，富贵之极，即乏丁火，亦稍有富贵。
  或甲多制戊，庚金无根，平常人也。庚戊若透，虽出比劫，必定富而寿。
  或多比劫，只一庚出干，坐禄逢生乃为舍丁从庚，略富贵。或支见申亥，戊己得所，以救庚丁，可许科甲。若单己透，其力弱小，不过贡监而已。

- **分字分词释义**：
  - **庚丁为要**：庚金丁火最重要 / 首选用神 / 炼金暖木
  - **壬水泛身**：壬水泛滥淹没甲木 / 亥月大忌 / 水漂木
  - **戊土制之**：用戊土制约水 / 堤坝 / 药神
  - **去浊留清**：去除浊气保留清气 / 制水存火金 / 极贵格
  - **舍丁从庚**：放弃丁火改用庚金 / 变格 / 杀制比劫
  - **坐禄逢生**：坐在禄位或逢长生 / 庚坐申巳 / 有根有力
  - **贡监**：捐纳取得的国子监生 / 买来的功名 / 己土弱

- **规范化释义（primary_lang_explained）**：
  十月（亥月）的甲木（长生之地），庚金（修剪）和丁火（温暖/炼金）最为重要，丙火次之。忌讳壬水泛滥淹没甲木（亥中壬水当令），必须用戊土来制约水。
  如果庚金和丁火都透出，又加上戊土出干（制水护火），这叫“去浊留清”，是极富贵的命，即使缺乏丁火，也稍有富贵（财滋弱杀）。
  如果甲木比劫多克制戊土，且庚金无根，只是平常人。如果庚金和戊土都透出，即使比劫多出，也必定富贵长寿。
  如果比劫多，只有一个庚金透出，且庚金坐禄（申）或逢生（巳/辰），这叫“舍丁从庚”（不用食伤制杀，直接用杀制劫），属于略有富贵。或者地支见申亥，戊己土得地有力，来救护庚金和丁火，可以许诺科甲。如果只有己土透出，力量弱小，不过是贡监（买来的学历）而已。

- **完整对等诠释（secondary_lang_full）**：
  Jia Wood in the 10th Month (Pig Month, Birth Place): Geng Metal and Ding Fire are essential, followed by Bing Fire. It dreads Ren Water flooding the body, requiring Wu Earth to control it.
  If both Geng and Ding are revealed, plus Wu Earth appearing on the stem, it is called "Removing Turbidity Keeping Clarity", the extreme of wealth and nobility. Even lacking Ding, there is still some wealth and nobility (Wealth generating Killing).
  If Jia is numerous and controls Wu, and Geng has no root, one is an ordinary person. If Geng and Wu are revealed, even with Parallel Shoulders appearing, one is certainly wealthy and long-lived.
  If Parallel Shoulders are numerous and only one Geng is revealed, sitting on Lu (Shen) or meeting Birth, it is "Discarding Ding and Following Geng", denoting slight wealth and nobility. Or if branches see Shen/Hai, and Wu/Ji are well-placed to save Geng/Ding, Civil Service is promised. If only Ji is revealed, its power is weak, merely a Gongjian (purchased degree).

- **核心要点**：
  - **首要用神**：庚丁（炼金/制劫）。
  - **关键救应**：戊土（制壬水）。亥月水旺，必须止水防木漂。
  - **格局**：去浊留清（戊制壬，留庚丁）。
  - **舍丁从庚**：比劫多时，先用庚制劫。

- **详细解说**：
  亥月甲木长生，内部生机萌动，但外部寒冷水旺。
  - 最大的威胁是“水泛木浮”（壬水当令）。
  - 戊土是第一堤坝，无戊则庚沉丁灭。
  - “去浊留清”指制去忌神（水），保留用神（丁庚），使格局清纯。
  - 己土力弱（湿土），不能止水，故仅为贡监。

- **叙事素材（narrative_snippets）**：
  - `[ns_qttbj_157]` `[trigger: 亥月甲木]` `[factor_trigger: month_hai AND tiangan_jia AND tiangan_geng AND tiangan_ding AND tiangan_wu]` `[role: 主干]` 十月甲木，庚丁为要，丙火次之，忌壬水泛身，须戊土制之。 → 《穷通宝鉴·三冬甲木》#6.1
  - `[ns_qttbj_158]` `[trigger: 去浊留清]` `[factor_trigger: month_hai AND tiangan_jia AND geng_revealed AND ding_revealed AND wu_revealed AND remove_turbidity_keep_clarity]` `[role: 主干依赖]` 庚丁两透，又加戊出干，名曰去浊留清，富贵之极。 → 《穷通宝鉴·三冬甲木》#6.1
  - `[ns_qttbj_159]` `[trigger: 舍丁从庚]` `[factor_trigger: month_hai AND tiangan_jia AND shishen_parallel_excess AND geng_revealed AND geng_sitting_lu]` `[role: 条件分支]` 多比劫，只一庚出干，坐禄逢生乃为舍丁从庚，略富贵。 → 《穷通宝鉴·三冬甲木》#6.1
  - `[ns_qttbj_160]` `[trigger: 贡监]` `[factor_trigger: month_hai AND tiangan_jia AND ji_revealed AND NOT tiangan_wu]` `[role: 例外处理]` 若单己透，其力弱小，不过贡监而已。 → 《穷通宝鉴·三冬甲木》#6.1"""
    normalized_text_zh: str = """"""
    subject: str = "1. 十月甲木（亥月）"
    factor_refs: list = ['remove_turbidity_keep_clarity', 'discard_ding_follow_geng', 'gongjian']
    
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
        l1_anchor="qtbj_v1.0.0_1__十月甲木_亥月_001_L1",
    )
    version: str = "1.0.0"
