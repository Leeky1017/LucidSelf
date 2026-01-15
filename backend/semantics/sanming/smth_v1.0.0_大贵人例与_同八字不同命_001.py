"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412597
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
    semantic_id="smth_v1.0.0_大贵人例与_同八字不同命_001",
    book_id="sanming",
    engine_id="bazi"
)
class 大贵人例与同八字不同命(SemanticEntry):
    """
    - **分字分词释义**：

  - **十干十二年生大贵人例**：指以十天干轮值六十年中的若干特定年份，配以指定的月、日、时，列为“大贵人应世”的标准命式。
  - **六甲年丁卯月乙未日戊寅时……...
    """
    
    original_text: str = """- **分字分词释义**：

  - **十干十二年生大贵人例**：指以十天干轮值六十年中的若干特定年份，配以指定的月、日、时，列为“大贵人应世”的标准命式。
  - **六甲年丁卯月乙未日戊寅时……六癸年丙辰月丙辰日戊子时**：逐年列举十组年、月、日、时的固定组合，理论上各对应一位“大贵人”。
  - **常术不能晓也**：谓此等命式若真能应大贵，必涉冥数机杳，非一般术数推算所能穷尽。
  - **天生大贵人，必有冥数气运以主之**：强调真正的大贵，不仅止于八字结构，更系时代机遇、家国格局等“冥数气运”所决定。
  - **年月日时多不足凭**：指出单凭四柱相同，不能武断命运完全相同；四柱只是条件之一。
  - **命同而遭遇各异的诸例**：通过缙绅、凡民、兄弟同产乃至走卒与名臣之对比，说明“同八字不同命”的现实。

- **规范化释义（primary_lang_explained）**：

  本节所列“十干十二年生大贵人例”，表面上是在说明：在六十年轮回中，每年各有一组特定的年、月、日、时，被视为“大贵人应世、建功立业”的命式。然而作者随即用大量实例指出：即便年月日时完全相同，现实人生中的贵贱、寿夭、祸福、子嗣多寡，仍大不相同。

  也就是说，这一节的重心，其实不在鼓吹“秘传大贵人口诀”，而是在提醒后学：

  - 同一八字可以落在截然不同的时代、家族与际遇中；
  - 真正的大贵，必然牵涉更大的历史与气运，而非靠几句口诀即可预定；
  - 将命理简化为“抄表格找自己是不是大贵人”，既不合实情，也容易误人。

- 核心要点：

  - **形式上**：列举十组合年、月、日、时，作为所谓“大贵人命式”的范本。
  - **实质上**：通过大量“命同而境遇大异”的案例，否定以此类口诀机械断命的做法。
  - 命理判断需结合**时代、家世、个人资质与抉择**，四柱只是条件之一，不能被神化。
  - 本节在整部《三命通会》中，起到对“命理绝对论”“一格定终身”的反思与纠偏作用。

- 详细解说：

  若只看“十干十二年生大贵人例”的表面，很容易把它误读为：

  > 找到与自己完全相同的年、月、日、时，即可断为大贵人。

  但原文在列举完十组命式后，立刻连篇累牍地举出反例：同一命式，有人官高而寿短，有人官小而寿长，有人多子，有人少子；甚至有人以贬戍而终，有人却得以安享天年，还有兄弟同产而功名先后悬殊，乃至走卒与名臣命同而祸福相反的故事。其用意十分鲜明：

  1. **打破“同八字必同命”的想象**  
     八字相同者，在现实中并不罕见，但其社会位置、机遇乃至性情抉择各不相同，因而人生结局自然悬殊。命式只给出“可能性结构”，并非已经写好的剧本。  
  2. **强调“冥数气运”与时代场域**  
     真正的大贵人，往往要置身于大变局、大时代：有国家需要这样的角色，有制度与机运容纳其位。若时代、家世与个人际遇不与之相合，即便八字结构相近，也难以显出同等层次的贵气。  
  3. **提醒术者要有统计与现实感**  
     作者列举缙绅与凡民、兄弟与同年朋友等诸多例子，意在告诉后来的命理师：判断之前，不妨多用“现实样本”来校验口诀，而不要只在纸面上推演。所谓“常术不能晓也”，其实也在暗示：术数有其边界，不能代替全部因果。

  对现代读者而言，这一节尤其值得重视：它提示我们在学习传统命理时，要同时保持**结构感**与**开放性**——既理解格局所提供的性格与路径倾向，又承认后天的教育、选择、制度与时代，同样深刻地参与塑造命运。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_145]` `[trigger: 大贵人例]` `[factor_trigger: shiganshiernian AND daguiren_mingshi]` `[role: 主干]` 十干十二年生大贵人例，以十天干轮值六十年中特定年份，列为大贵人应世的标准命式。 → 《三命通会》卷六#大贵人例与同八字不同命
  - `[ns_smth_06_146]` `[trigger: 命同遇异]` `[factor_trigger: sizhu_tongyi AND jingyugeyi]` `[role: 主干依赖]` 命同而遇异：即便年月日时完全相同，现实人生中的贵贱、寿夭、祸福、子嗣多寡，仍大不相同。 → 《三命通会》卷六#大贵人例与同八字不同命
  - `[ns_smth_06_147]` `[trigger: 冥数气运]` `[factor_trigger: mingshu_qiyun AND changshu_bunengxiao]` `[role: 条件分支]` 天生大贵人，必有冥数气运以主之。常术不能晓也。 → 《三命通会》卷六#大贵人例与同八字不同命
  - `[ns_smth_06_148]` `[trigger: 大贵人结论]` `[factor_trigger: mingli_feijiueding AND jiegougankaifangxing]` `[role: 总结]` 命理判断需结合时代、家世、个人资质与抛择，四柱只是条件之一。 → 《三命通会》卷六#大贵人例与同八字不同命

- **校勘与字词辨析（双语）**：

  - 文中举例人名（如黄懋、申价、朱衡、李庭龙、万某、饶才等），底本间或有字形、字号差异，本稿不逐一考订，只保留其“命同而境遇各异”的象征意义。
  - 原文多用“命同”一语，本稿在白话中统一理解为“四柱八字相同或极近”，以免与现代“命运完全相同”的绝对说法混淆。
  - “冥数气运”一词，本稿不作神秘化处理，而是理解为时代环境、社会结构与大势所汇成的总体条件。
  - 对《乐善录》等书名，仅作出处提示，不展开二次转述，避免与其他版本材料混杂。
  - **English**：
    - Original text preserved to avoid mixing with materials from other editions."""
    normalized_text_zh: str = """"""
    subject: str = "大贵人例与"同八字不同命""
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_marker', 'bazi_semantic', 'bazi_factor_59', 'bazi_semantic', 'bazi_state_factor_18', 'bazi_semantic', 'bazi_state_factor_19', 'bazi_semantic', 'bazi_condition_factor_178', 'bazi_semantic', 'bazi_condition_factor_179', 'bazi_semantic', 'source_ref', 'rel_smth_06_100', 'mingtong_zaoyuyi', 'rel_smth_06_101', 'sizhu_xiangsi', 'rel_smth_06_102', 'daguiren_fuhe', 'evi_smth_06_100', 'mingtong_zaoyuyi', 'rule_mingtong', 'evi_smth_06_101', 'mingshu_qiyun', 'rule_changshu', 'evi_smth_06_102', 'chaobazi_ganrao', 'rule_mingshu', 'map_smth_06_067', 'map_smth_06_068']
    
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
        l1_anchor="smth_v1.0.0_大贵人例与_同八字不同命_001_L1",
    )
    version: str = "1.0.0"
