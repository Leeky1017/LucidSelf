"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412560
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
    semantic_id="smth_v1.0.0_论阳刃与极旺之险_001",
    book_id="sanming",
    engine_id="bazi"
)
class 论阳刃与极旺之险(SemanticEntry):
    """
    - **原文（source_text）**：

  论阳刃（前论羊刃煞与此参看）：阳者，阴阳之阳；刃者，刀刃之刃，即禄前一位，言旺越其分，故险。窃详：甲人见卯，卯中有乙木，乙为甲弟，能劫其兄之财，冲去...
    """
    
    original_text: str = """- **原文（source_text）**：

  论阳刃（前论羊刃煞与此参看）：阳者，阴阳之阳；刃者，刀刃之刃，即禄前一位，言旺越其分，故险。窃详：甲人见卯，卯中有乙木，乙为甲弟，能劫其兄之财，冲去酉中辛官，合其庚妻，庚乃甲之七煞，劫财冲官合煞，所以至凶。惟甲丙戊庚壬五阳干有刃，乙丁己辛癸五阴干无刃，故曰阳刃。惟见伤官与阳刃同祸，故乙见丙亦谓之刃，以丙伤其庚官，合辛煞，克其乙木，阴金克阴木至毒，所以凶与阳刃同。阳刃有三：有劫财刃，甲见乙是也，不利财官格；有护禄刃，甲见卯是也，大利归禄格；有背禄刃，乙丙是也，大利去官留煞局。《喜忌篇》云：劫财阳刃，切忌时逢，岁运并临，灾殃立至。独阳刃以时言，重于年月日也。假令甲日生人，时上见乙卯，此是真刃，命中既逢阳刃，伤妻破财，灾殃已胚胎矣。流年岁运再遇羊刃，是谓并临，见巳酉是冲岁君，见亥未戌是合岁君。阳刃，凶煞也；太岁，凶神也。太岁得吉神相扶，合则吉；若阳刃凶煞来冲合岁君，是谓攒凶聚煞，其祸难免。经云：“阳刃冲合岁君，勃然祸至”，此之谓也。中间亦要详辨：命元浅薄，遇此诚然；若命旺秉气深厚，或有天月德及赦文解救，止有浮实，亦无大咎。或日柱原有刃，见冲或合，岁运再临冲合，大凶；若岁冲合而运不冲合，运冲合而岁不冲合，其祸减半论。又曰：日干无气，时逢阳刃不为凶。言生日天元临死绝、衰病、暴败之地，不通月气，不能胜任财官，若逢阳刃，能劫财化煞，譬如兄力弱、财重，得弟分任，则可胜其财而为我用，所以不作凶论。夫身弱见财官，固喜阳刃分财合煞；若见食伤，身弱脱气，亦喜阳刃扶持；若见印绶，则非日干无气矣。先言忌阳刃者，身强力能任财，故不喜劫夺；后言喜阳刃者，身弱力不住财，故赖刃以分任也。

- 分字分词释义：

  - **阳刃**：即阳干之羊刃，为各阳日禄前一位的地支，象征气势过旺如刀刃在前。
  - **劫财刃、护禄刃、背禄刃**：分别指偏向分财、护禄、去官留煞的三种用法和倾向。
  - **阳干有刃，阴干无刃**：甲丙戊庚壬有专属羊刃支；乙丁己辛癸则以类比方式看“类刃”。
  - **阳刃冲合岁君，勃然祸至**：阳刃若与太岁相冲合，易在流年中触发重大事件。

- **规范化释义（primary_lang_explained）**：

  阳刃，是阳日禄前一位的“极旺之位”，其气既可为我所用，又可伤我。原文一方面强调其凶险：

  - 身强而又见阳刃，多主好胜、刚烈、争夺，易损财伤妻、招灾惹祸；
  - 尤其在岁运并临、与太岁冲合之时，凶象更重。

  另一方面也指出：

  - 对身弱而见财官过重者，阳刃有时反可分担财官之压，化为“护身之刃”；
  - 若配合得宜，亦可在武职、权力、竞争性行业中成就一番事业。

- 核心要点：

  - 阳刃本质是**阳气过旺的刀锋**：可为我所用，亦可伤己伤人。
  - 身强用财官者，忌再见阳刃；身弱被财官压制者，反而可借刃分财合煞。
  - 岁运并临、冲合太岁时，要特别警惕事故、官非、情感剧变等重大转折。

- 详细解说：

  可以把阳刃看作“高风险高杠杆”的能量点：

  - 对性格：多主刚烈、不服输、行动决断，但也容易偏激、急躁；
  - 对命运：在竞争环境中，阳刃之人往往更敢争、更敢抢，既可能一举成功，也可能因过度冒险而铩羽而归；
  - 对关系：阳刃与财、官纠缠不清时，易在婚姻、合作、上下级关系中产生强烈冲突。

  判断阳刃时，需要兼看：

  1. **身强身弱**：身强再见刃，多为“刀上加刀”；身弱见刃，有时反成“多一只手来分担”；
  2. **与用神关系**：用神为印、为食者，刃来易坏印、截食；用神为财、为煞者，刃有时可分任其重；
  3. **岁运触发方式**：原局虽有刃，若岁运不冲不合，则多为性格倾向；一旦岁运强烈触及，则应警惕事件化之风险。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_133]` `[trigger: 阳刃定义]` `[factor_trigger: yanggan_yangren AND liqian_yiwei]` `[role: 主干]` 阳刃者，禄前一位，言旺越其分，故险。甲人见卯，劫财冲官合煞，所以至凶。 → 《三命通会》卷六#论阳刃与极旺之险
  - `[ns_smth_06_134]` `[trigger: 三种阳刃]` `[factor_trigger: jiecairen OR huluuren OR beiluuren]` `[role: 主干依赖]` 阳刃有三：劫财刃不利财官格，护禄刃大利归禄格，背禄刃大利去官留煞局。 → 《三命通会》卷六#论阳刃与极旺之险
  - `[ns_smth_06_135]` `[trigger: 岁运并临]` `[factor_trigger: suiyun_binlin AND zaiyang_lizhi]` `[role: 条件分支]` 劫财阳刃切忌时逢，岁运并临，灾殃立至。阳刃冲合岁君，勃然祸至。 → 《三命通会》卷六#论阳刃与极旺之险
  - `[ns_smth_06_136]` `[trigger: 身弱用刃]` `[factor_trigger: riganwuqi AND yangren_buzuixiong]` `[role: 总结]` 日干无气，时逢阳刃不为凶。身弱见财官，喜阳刃分财合煞。 → 《三命通会》卷六#论阳刃与极旺之险

- **校勘与字词辨析（双语）**：

  - 原文中"阳刃有三"之分类，本稿在白话中以“劫财刃、护禄刃、背禄刃”统摄；具体日干、地支的对应，可在推命时细查。
  - “太岁得吉神相扶，合则吉”一句，本稿理解为太岁本身并非专主凶吉，关键在于与之相合者为何物。
  - 关于“日干无气，时逢阳刃不为凶”的反向论述，本稿在白话与详细解说中加以展开，以免读者只记其凶而忘其用。
  - **English**：
    - Balanced interpretation is provided to prevent readers from only remembering the inauspicious aspects while forgetting the practical uses."""
    normalized_text_zh: str = """"""
    subject: str = "论阳刃与极旺之险"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_28', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_qiangruo_1', 'bazi_semantic', 'bazi_state_degree_13', 'bazi_semantic', 'bazi_condition_factor_172', 'bazi_semantic', 'bazi_condition_factor_173', 'bazi_semantic', 'source_ref', 'rel_smth_06_091', 'yangren_ge_presence', 'rel_smth_06_092', 'shenqiangruo_renlihui', 'rel_smth_06_093', 'suiyun_binlin_risk', 'evi_smth_06_091', 'yangren_ge_presence', 'rule_yangren', 'evi_smth_06_092', 'tianyuede_jiejiu', 'rule_dejie', 'evi_smth_06_093', 'suiyun_binlin_risk', 'rule_binlin', 'map_smth_06_061', 'map_smth_06_062']
    
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
        l1_anchor="smth_v1.0.0_论阳刃与极旺之险_001_L1",
    )
    version: str = "1.0.0"
