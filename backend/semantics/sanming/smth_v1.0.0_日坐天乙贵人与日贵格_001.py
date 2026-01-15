"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.412418
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
    semantic_id="smth_v1.0.0_日坐天乙贵人与日贵格_001",
    book_id="sanming",
    engine_id="bazi"
)
class 日坐天乙贵人与日贵格(SemanticEntry):
    """
    - **原文（source_text）**：
      日贵者，自坐天乙是也。此格只有四日：丁酉、丁亥、癸巳、癸卯，主为人纯粹，有仁德，有姿色，不傲物气高。贵气聚于日，更有财食印相助，贵气为福。喜三...
    """
    
    original_text: str = """- **原文（source_text）**：
      日贵者，自坐天乙是也。此格只有四日：丁酉、丁亥、癸巳、癸卯，主为人纯粹，有仁德，有姿色，不傲物气高。贵气聚于日，更有财食印相助，贵气为福。喜三六合宅墓合，行贵人财旺运，发福。大忌刑冲破害空亡，运行再遇前忌，太岁加会，更见魁罡，定主贫夭。若别成格，不论。日贵须分昼夜，日生要癸卯、丁亥，夜生要癸巳、丁酉，日夜不皆为得体。经云：贵人者慈祥恺悌之号，德性尊重之名，遇财官印食则吉，值煞刃冲刑则凶，运遇魁罡，为害不浅。古歌曰：生日天干坐贵支，若见魁罡福不齐，年逢月禄不为喜，日贵重逢奇又奇。又：日德日贵主慈祥，财官印遇福荣昌，刑冲煞刃如来见，反吉为凶不可当。又；癸临蛇兔是英奇，丁向猪鸡一例推，切忌魁罡分昼夜，更防刑害失尊卑；运行嘉会名须重，命带空亡祸必随，贵重尊严持厚德，或逢前戒凶无疑。
      - 分字分词释义：
      - **日贵者，自坐天乙是也**：所谓“日贵”，是指日干所坐之支恰为该日的天乙贵人，故曰“自坐天乙”。
   - **此格只有四日：丁酉、丁亥、癸巳、癸卯**：限定四个日柱，分别对应火、火、水、水之日，日支皆为本日之贵人所在。
   - **贵气聚于日**：贵人之气集中在日柱，表示个人气质、德性与福荫主要由自身而来，而非完全依赖年、月等外缘。
   - **三合六合宅墓合**：指与日支相关的三合局、六合或墓库之合，若成局则有助于汇聚贵气与福禄。
   - **大忌刑冲破害空亡，更见魁罡**：贵人格最忌被冲刑刑害、落空亡，若再遇魁罡等刚烈之星，则贵气受损，反主贫夭。
   - **日贵须分昼夜**：强调白天出生与夜晚出生的不同搭配：日生（昼）以癸卯、丁亥为得体，夜生（夜）以癸巳、丁酉为得体。
   - **遇财官印食则吉，值煞刃冲刑则凶**：贵人之气若得财官印食调和则显福，若与七煞、羊刃、刑冲等同来，则福转为祸。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_06_069]` `[trigger: 日贵格定义]` `[factor_trigger: rigui_ge_presence]` `[role: 主干]` 日贵者，自坐天乙是也。此格只有四日：丁酉、丁亥、癸巳、癸卯。 → 《三命通会》卷六#日贵
  - `[ns_smth_06_070]` `[trigger: 贵气聚日]` `[factor_trigger: gui_qi_ju_ri AND cai_shi_yin]` `[role: 主干依赖]` 贵气聚于日，更有财食印相助，贵气为福。 → 《三命通会》卷六#日贵
  - `[ns_smth_06_071]` `[trigger: 大忌刑冲]` `[factor_trigger: da_ji_xingchong OR jian_kuigang]` `[role: 条件分支]` 大忌刑冲破害空亡，运行再遇前忌，太岁加会，更见魁罡，定主贫夭。 → 《三命通会》卷六#日贵
  - `[ns_smth_06_072]` `[trigger: 慈祥恺悌]` `[factor_trigger: cixiang_kaiti]` `[role: 总结]` 贵人者慈祥恺悌之号，德性尊重之名。 → 《三命通会》卷六#日贵

      - 白话原意：
      日贵格，是指日干直接坐在自己的天乙贵人之上，只有丁酉、丁亥、癸巳、癸卯四个日柱符合条件。命中有此四日之一，主其人性情端正、为人仁厚，有容人之量，也多具一定的仪表与气度；这种“贵气”集中在日柱本人身上，再得财星、食神、印绶等配合时，往往能化为实在的福禄与名望。
      但日贵格并非一见贵人便必然大贵。原文强调：此格须分昼夜，癸卯、丁亥宜日生，癸巳、丁酉宜夜生，以昼夜阴阳相配，方为得体。又因日贵多主温厚、慈祥之德，一旦柱中刑冲太重、或与魁罡、煞刃相会，贵气即转为凶象，反见贫薄、短寿之应。故日贵格贵在守德、贵在不受刑克；若能在吉运中逢财官印食，则“贵气为福”，若逢煞刃冲刑，则“反吉为凶”。
      - 核心要点：
      - 本格所据仅有四日：丁酉、丁亥、癸巳、癸卯，皆为日干自坐天乙贵人。
   - 特点在于“贵气聚于日”，重在本人品德与气质，而非外在权势本身。
   - 宜分昼夜搭配：癸卯、丁亥宜日生，癸巳、丁酉宜夜生，以合阴阳之体。
   - 喜财官印食相生相辅；忌刑冲破害、空亡、魁罡等刚猛之星破坏贵气。
      - 详细解说：
      与前文“日德”偏重于道德善性、“魁罡”偏重于刚烈威权相比，日贵格所呈现的是一种以“慈祥恺悌”为特征的贵气。天乙贵人本是八字体系中最具护佑意味的神煞之一，自坐天乙，等于把这种护佑之力安置在日主自身之上，因此原文才说“贵气聚于日”。
      实务判断时，一方面要看日贵本身是否得体（是否符合昼夜之别），另一方面要看其所遇之星：若财官印食得所，往往体现为“有德有位”：既有地位，又能以柔和、仁厚的方式持权；若反而多遇煞刃、刑冲、魁罡，则可能表现为性情过于刚烈、易遭非议谗构，甚至有贫夭之虞。原文几首歌诀，反复强调“见魁罡则福不齐”“刑冲煞刃如来见，反吉为凶不可当”，皆可视为对格局易损性的提醒。
      综观全段，日贵格不宜单凭一条贵人神煞就断富贵，而应放在整体格局之中：若原局另有成格，则日贵只是加分项；若原局破损甚多，则日贵之气也难以独力回天。
      - **校勘与字词辨析（双语）**：
      - 原文“日贵者，自坐天乙是也”一句，本稿在释义中明确为“日干之坐支为天乙贵人”的技术定义。
   - “日贵须分昼夜，日生要癸卯、丁亥，夜生要癸巳、丁酉”之语，本稿未作更改，只在白话中解释为阴阳得体的要求。
  - 原文多首歌诀，本稿择要引述关键句，以点明“见魁罡则福不齐”“刑冲煞刃则反吉为凶”等主要判断要点，未逐句展开命例。
  - **English**：
    - The sentence "Day-Noble means sitting on Tianyi Noble" is clarified in the glossary as the technical definition "day stem's sitting branch is the Tianyi Noble."
    - Key judgment points such as "noble brings fortune but not all fortunes are equal" and "punishment-clash-kill-blade turns good to bad" are extracted without expanding each example."""
    normalized_text_zh: str = """"""
    subject: str = "日坐天乙贵人与日贵格"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_marker_17', 'bazi_semantic', 'new_candidate', 'bazi_semantic', 'bazi_state_yinyang', 'bazi_semantic', 'bazi_state_strength_4', 'bazi_semantic', 'bazi_condition_factor_152', 'bazi_semantic', 'bazi_condition_factor_153', 'bazi_semantic', 'source_ref', 'rel_smth_06_052', 'rigui_ge_presence', 'rel_smth_06_053', 'zhouye_yinyang_pipei', 'rel_smth_06_054', 'kuigang_chonggui_risk', 'evi_smth_06_052', 'rigui_ge_presence', 'rule_rigui', 'evi_smth_06_053', 'zhouye_yinyang_pipei', 'rule_zhouye', 'evi_smth_06_054', 'kuigang_chonggui_risk', 'rule_kuigang', 'map_smth_06_035', 'map_smth_06_036']
    
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
        l1_anchor="smth_v1.0.0_日坐天乙贵人与日贵格_001_L1",
    )
    version: str = "1.0.0"
