"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559327
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
    semantic_id="yhzp_v1.0.0_杂论口诀_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 杂论口诀(SemanticEntry):
    """
    - **原文（source_text）**：
  看子平之法，专论财官；以月上财官为紧要；发觉在于日时，要消详于强弱。
  论官星不论格局，论格局不论官星。
  入格者，非富即贵；不入格者，非夭即贫。...
    """
    
    original_text: str = """- **原文（source_text）**：
  看子平之法，专论财官；以月上财官为紧要；发觉在于日时，要消详于强弱。
  论官星不论格局，论格局不论官星。
  入格者，非富即贵；不入格者，非夭即贫。
  官怕伤，财怕劫。印绶见财，愈多愈灾。
  伤官见官，为祸百端；若非疾病伤躯，必当官讼囚系、子丧妻伤。
  伤官见官，元有者重，元无者轻；重则迁徙，轻则刑责。
  伤官见官，心地勾曲，诡谲多诈，傲物气高；常以天下人不如己；贵人惮之，小人恶之。
  伤官用财者富，伤官劫财者贫。
  年上伤官，富贵不久；月上伤官，父母不完；日上伤官，难为妻妾；时上伤官，子孙无传。
  岁月伤官劫财，生于贫贱之家；日下时中有财官，先贫后富。
  岁月财官印绶，生于富贵之家；日时伤官劫财，先富后贫，伤损子息，无晚福。
  伤官见官、官杀混杂，为人好色多淫，作事小巧寒贱。
  乙木巳上为太乙，亥上登明；男好色，女淫滥。
  官杀混杂，有财者吉；无财印者凶。
  但看，财命有气，纵背禄而不贫；财绝命衰，纵建禄而不富。
  劫财败财，心高下贱，见者主贪婪。
  鬼中逢官须逼迫。彼克我（官杀）兮贵，我克彼（财）兮富。
  彼生我（印）兮以仗母力，长我精神；我生彼（食伤）兮，常怀逼迫。
  财入月令，勤俭悭吝。
  柱有劫财比刃多者，刑父伤妻，不聚财也。
  路伎商贾，须观落地之财。宰相须看得时正禄。
  七杀枭重，走遍他乡之客。伤官劫财，瞒心负赖之徒。
  重犯财官者，贵；重犯亡神者，夭。
  七杀宜制，独立为强。明杀合去，五行和气春风；暗杀合来，刑伤害己。
  时杀喜冲，喜刃无制；女多产厄，男犯刑名。
  二德无破，女必贤良，男多忠孝。
  伤官用印去财，方可驰名。伤官用财，伤官处须当发福。
  入格清奇者，富；入格不成者，贫。
  一格二格，非卿即相；三格四格，财官不纯，非隶卒多是九流。
  六阴朝阳，季月只作印看。
  吉神惟怕破害，凶神不喜刑冲。
  财官印食，定显慈祥之德；伤官劫刃，难逃寡恶之名。
  冲天无合，乃飘流之徒。
  六壬趋艮（寅），逢亥月者贫。
  马落空亡，操心落魄之人。
  离祖月合、逢冲过房、杀带三刑，母明父暗，多是偷生。
  财印偏官，庶出已定。
  干头灭烈，冉伯牛怨于苍天。
  时日冲刑，难免卜商、庄子之叹。
  刑多者，为人不义；合多者，疏者亦亲。合多主晦，冲多主凶。
  辰多好斗，戌多好讼。辰戌魁罡，多凶少吉。
  时日空亡，难为妻子。交驰驿马，别土离乡。
  食神干旺，胜似财官；顺食者食前方丈，倒食者箪食豆羹。
  食衰枭旺，不死也灾。
  水润下兮，文学显达；土稼穑兮，富贵经商。
  金水双清而为道，火土混浊而为僧。
  子午最嫌巳亥，卯酉切忌寅申。
  己入亥宫，见阴木终为损寿；时逢丙寅，则冠带簪缨。
  五行绝处，即是'胎元'；生日逢之，名曰'受气'。
  化者有十日：甲申、乙酉、庚寅、辛卯、壬午、癸未、丙子、丁丑、戊午、己丑，八字虽不入格，富贵亦是盈馀；另有福德秀气，各有天地神祇。
  论化之格，化之真者，名公巨卿；化之假者，孤儿异姓。逢龙即变化，飞龙在天，利见大人。
  又有冬逢炎热、夏草逢霜、阴鼠栖水、神龟宿火，有合无合，后学难知，得一分三，前贤不载。

- **分字分词释义**：
  - **专论财官**：子平法以财官为论命核心。
  - **官怕伤财怕劫**：官星怕伤官克制，财星怕劫财夺取。
  - **印绶见财愈多愈灾**：印格逢财星破印，财多则灾重。
  - **伤官见官为祸百端**：伤官克制官星，主官讼、刑伤、子丧妻伤。
  - **伤官用财者富**：伤官生财，才华转化为财富。
  - **伤官劫财者贫**：伤官配劫财，无财可依主贫。
  - **财官印食**：四吉神，代表富贵慈祥之德。
  - **伤官劫刃**：四凶神，代表寡恶刑伤之象。
  - **辰多好斗戌多好讼**：辰支多主好斗，戌支多主好诉讼。
  - **金水双清为道**：金水相生气质清澈，主智慧或修道。
  - **火土混浊为僧**：火土交杂气质浑浊，主出家或隐遁。
  - **食神干旺胜似财官**：食神旺于天干，其贵不亚于财官格。
  - **倒食者箪食豆羹**：偏印克食神，主贫乏困顿。

- **规范化释义（primary_lang_explained）**：
  本节汇集了大量论命口诀，涵盖财官、伤官、七杀、格局、神煞、性情等多个方面：
  - **财官为本**：论命专看财官，月令最重，日时次之。官怕伤，财怕劫。
  - **伤官见官**：最为祸患，主官讼、刑伤、诡诈。有根者重，无根者轻。伤官用财则富，用印去财亦贵。
  - **宫位吉凶**：伤官在年主富贵不久，在月损父母，在日妨妻，在时损子。反之，岁月财官印主生于富贵家，日时财官主晚年富贵。
  - **吉凶神煞**：财官印食主慈祥，伤官劫刃主寡恶。二德（天月德）主贤良。马落空亡主操心。
  - **特殊论断**：辰多好斗，戌多好讼。金水双清为道，火土浊为僧。食神干旺胜财官。倒食（偏印）克食主灾。
  - **化气与特殊日**：列举甲申、乙酉等十日为"化气"或"受气"之日，虽不入正格亦有富贵。化格真者贵，假者孤。

- **完整对等诠释（secondary_lang_full）**：
  **Miscellaneous Mnemonics**:
  - **Wealth & Officer Focus**: Ziping method focuses on Wealth and Officer. Month Pillar is critical; Day/Hour provide details. Officer fears Injury; Wealth fears Robbery.
  - **Injuring Officer Meeting Officer**: Source of hundred disasters—lawsuits, imprisonment, injury to spouse/children. "Scheming heart, arrogant nature." Use Wealth to create fortune; use Seal to remove Wealth for fame.
  - **Pillar Placement**: Injury in Year=short-lived wealth; in Month=parents incomplete; in Day=harm spouse; in Hour=no descendants. Wealth/Officer in Year/Month=born rich; in Day/Hour=rich later.
  - **Nature & Character**: Wealth/Officer/Seal/Food=benevolent; Injury/Rob/Blade=wicked. Two Virtues (Noble)=virtuous. Horse in Void=anxious/wandering.
  - **Special Judgments**: Abundant Chen=quarrelsome; abundant Xu=litigious. Metal/Water pure=Daoist; Fire/Earth turbid=Monk. Prosperous Eating God surpasses Wealth/Officer.
  - **Transformation**: Ten special days (e.g., Jia-Shen, Yi-You) possessing "Received Qi," indicating surplus wealth even without standard patterns. True transformation brings high rank; false transformation brings loneliness.

- **核心要点**：
  - **伤官见官**：百祸之源，需有财通关或印制伏
  - **财官印食**：四吉神，主富贵慈祥
  - **杀伤劫刃**：四凶神，主刑祸寡恶，宜制化
  - **宫位断法**：年月主早年/祖业，日时主晚年/子息
  - **五行性情**：金水清主道，火土浊主僧，水多智淫，辰戌斗讼

- **详细解说**：  《杂论口诀》汇集了子平法论命的实战口诀，堪称命理速断手册。全篇可分为六大主题：**财官为本**——"专论财官"确立论命核心，"官怕伤，财怕劫"点明吉神之忌。**伤官见官**——"伤官见官，为祸百端"是本篇重点，详述其凶象：官讼囚系、子丧妻伤、心地勾曲、傲物气高。但"伤官用财者富，用印去财方可驰名"提供了化解之道。**宫位断法**——年月日时各有断法：年上伤官富贵不久，月上损父母，日上妨妻，时上损子；反之岁月财官印主富贵家，日时伤劫主先富后贫。**四吉四凶**——财官印食为四吉神主慈祥，杀伤劫刃为四凶神主寡恶。**五行性情**——金水双清为道，火土混浊为僧；辰多好斗，戌多好讼。**化气特殊日**——甲申乙酉等十日虽不入正格亦有富贵，化之真者名公巨卿，假者孤儿异姓。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_615]` `[trigger: 专论财官]` `[factor_trigger: lunming AND zhuanlun_caiguan AND yueling_jinyao]` `[role: 主干]` 看子平之法，专论财官；以月上财官为紧要。 → 《渊海子平·杂论口诀》
  - `[ns_yhzp_616]` `[trigger: 官怕伤财怕劫]` `[factor_trigger: guanpa_shang AND caipa_jie AND yinshou_jiancai AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 官怕伤，财怕劫；印绶见财愈多愈灾。 → 《渊海子平·杂论口诀》
  - `[ns_yhzp_617]` `[trigger: 伤官见官百端]` `[factor_trigger: shangguan_jianguan AND huo_baiduan AND guansong_qiuxi AND liuqin_relationship]` `[role: 条件分支]` 伤官见官，为祸百端；若非疾病伤躯，必当官讼囚系、子丧妻伤。 → 《渊海子平·杂论口诀》
  - `[ns_yhzp_618]` `[trigger: 伤官用财富]` `[factor_trigger: shangguan_yongcai AND fu AND yongyin_chiming AND caiyin AND caiyin_qing_guansha_zu AND changyin AND injury_wealth]` `[role: 条件分支]` 伤官用财者富，伤官劫财者贫；伤官用印去财方可驰名。 → 《渊海子平·杂论口诀》
  - `[ns_yhzp_619]` `[trigger: 四宫伤官断]` `[factor_trigger: sigong_shangguan AND nian_yue_ri_shi_duanfa]` `[role: 条件分支]` 年上伤官富贵不久；月上伤官父母不完；日上伤官难为妻妾；时上伤官子孙无传。 → 《渊海子平·杂论口诀》
  - `[ns_yhzp_620]` `[trigger: 四吉四凶]` `[factor_trigger: siji_shen AND sixiong_shen AND cixiang_gua'e]` `[role: 条件分支]` 财官印食定显慈祥之德；伤官劫刃难逃寡恶之名。 → 《渊海子平·杂论口诀》
  - `[ns_yhzp_621]` `[trigger: 金水道火土僧]` `[factor_trigger: jinshui_shuangqing AND dao AND huotu_hunzhuo AND seng AND daoxue AND metal_water_clear]` `[role: 条件分支]` 金水双清而为道，火土混浊而为僧；五行性情判断。 → 《渊海子平·杂论口诀》
  - `[ns_yhzp_629]` `[trigger: 辰戌斗讼]` `[factor_trigger: chenduo_haodou AND xuduo_haosong AND kuigang AND chen_xu_abundant AND haodou_haosong]` `[role: 条件分支]` 辰多好斗，戌多好讼；辰戌魁罡多凶少吉。 → 《渊海子平·杂论口诀》
  - `[ns_yhzp_630]` `[trigger: 杂论口诀纲领]` `[factor_trigger: zalun_koujue AND shizhan_duanming]` `[role: 总结]` 杂论口诀汇集子平法实战断命口诀，涵盖财官伤官宫位性情化气等多方面。 → 《渊海子平·杂论口诀》"""
    normalized_text_zh: str = """"""
    subject: str = "杂论口诀"
    factor_refs: list = ['injuring_officer_meets_officer', 'auspicious_four', 'inauspicious_four', 'overturning_food', 'metal_water_clear']
    
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
        l1_anchor="yhzp_v1.0.0_杂论口诀_001_L1",
    )
    version: str = "1.0.0"
