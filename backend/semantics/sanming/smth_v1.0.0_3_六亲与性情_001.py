"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.080888
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
    semantic_id="smth_v1.0.0_3_六亲与性情_001",
    book_id="sanming",
    engine_id="bazi"
)
class 3六亲与性情(SemanticEntry):
    """
    - 原文（source_text）：
  土厚而掩火无光，水盛则漂木无定。
  五行不可太盛，八字须得中和。
  土止水流全福寿，水无土止必伤残。
  木盛多仁，土薄寡信；水旺居垣须有智，金坚主义却能...
    """
    
    original_text: str = """- 原文（source_text）：
  土厚而掩火无光，水盛则漂木无定。
  五行不可太盛，八字须得中和。
  土止水流全福寿，水无土止必伤残。
  木盛多仁，土薄寡信；水旺居垣须有智，金坚主义却能为。
  金水聪明而好色，水土混杂必多愚。
  遐龄得于中和，夭寿丧于偏枯。
  辰戌克制并冲，必犯刑名；子卯相刑，门户全无礼德。
  弃印就财明偏正，弃干从煞论刚柔。
  伤官无财可倚，虽巧必贫；食神制煞逢枭，不贫则夭。
  男多阳刃必重婚，女犯伤官须再嫁。
  贫贱者皆因官处遭伤，孤寡者只为财神被劫。
  财临旺地人多福，官遇长生命必荣。
  去煞留官方论福，去官留煞不为卑。
  岂知遇正官却终俸禄，逢七煞乃有声名。
  逢伤官反见夫，财命有气；遇枭神而丧子，福气无依。
  天干煞显无制者贱，地支财伏暗生者奇。
  三戌冲辰祸不浅，两干不杂利名齐。
  丙子辛卯相刑，荒淫滚浪；子午卯酉全备，酒色昏迷。
  因财致祸，贪食种疾。
  侄男为嗣，义女为妻。
  日时相冲，卯酉始生必主迁移；造化因逢戌亥，平生敬信神祗。
  阴克阴，阳克阳，财神有用；官无官，鬼无鬼，太旺倾危。
  得局失垣，平生不遂；归垣得局，早岁轩昂。
  命遇枭神而与富家营运，龙藏亥卯经商利赂丝缗。
  财官俱败者死，食神逢枭者凶。
  丁巳孤鸾，命遇聪明诗女；裸形沐浴，日犯浊滥荒淫。
  丁逢卯日遇巳土，饕食之人；亥乃浆神逢酉金，嗜杯之客。
  归禄得财而获福，无财归禄必须贫。
  财印混杂，终为受困；偏正错乱，必致伤身。
  太岁忌逢战斗，羊刃不喜刑冲。
  庚逢丙扰，多有不仁；癸从戊合，少长无情。
  不从不化，淹留仕路之人；得化得从，显达功名之士。
  化行禄旺者生，化归禄绝者死。
  生地相逢，壮年不禄；时归败地，老后无终。
  丁坐酉金，丙辛遇之绝嗣；财临煞位，父死而不归家。
  八专干支同类，煞运煞年多凶。
  若能详观玩览，贵贱万不失一。

- 分字分词释义：
  - **木盛多仁**：木主仁。
  - **子卯相刑**：无礼之刑。
  - **弃印就财**：贪财坏印。
  - **弃干从煞**：从煞格。
  - **孤鸾**：丁巳、甲寅等日。
  - **浆神**：水酒。
  - **八专**：甲寅、乙卯等干支同气。

- 规范化释义（primary_lang_explained）：  
  本段把元理赋从抽象的五行生克，推进到对性情与六亲的具体判断。前几句仍然围绕“太盛则伤”“中和为贵”展开：土厚掩火、水盛漂木，说明过度的防御与情绪泛滥都会遮蔽一个人的光亮与定力；土止水流则福寿双全，水无土止必至损残，则把“节制欲望、稳住情绪”视为长寿与安稳的前提。接着用“木盛多仁、土薄寡信、水旺居垣须有智、金坚主义却能为”这一组句子，把五行与品性挂钩：木多者重情重义，土薄者欠缺信用，水旺而有根者机敏聪慧，金坚者主见强、执行力高；金水清而聪明好色，水土杂而多愚，则是提醒聪明与放纵往往相伴而生。  
  中段大篇幅讲六亲与具体事件：辰戌冲刑、子卯相刑，指向官非、名誉受损与家门失礼；弃印就财、弃干从煞，则是通过“贪财坏印”“从煞取势”两种极端，说明性格与命运选择的不同走向。诸如“伤官无财虽巧必贫”“食神制煞逢枭不贫则夭”“男多阳刃必重婚，女犯伤官须再嫁”“贫贱因官处遭伤，孤寡因财星被劫”等句，则把十神与六亲关系一一对照：官煞受损则仕途与社会地位不佳，财被夺则婚姻与亲情薄弱。末段关于孤鸾、沐浴、浆神、八专与太岁、羊刃的组合，则进一步指出：桃花与欲望、修行与孤寡、早发与夭折，都不是单一神煞决定，而是在“得局失垣、归垣得局”的整体结构里，被五行与运势共同触发。  

- 完整对等诠释（secondary_lang_full）：  
  This portion moves the discussion from abstract Five‑Element dynamics into concrete judgments about temperament and kinship. The opening images of thick Earth smothering Fire or surging Water causing Wood to drift are still about excess and deficiency, but now they clearly point to psychological states: overprotection and rigidity smother initiative; uncontrolled emotion or desire uproots stability. When Earth stops Water and both remain in proportion, blessing and longevity are complete; when Water lacks any such containment, harm and disability are likely. The lines "abundant Wood yields benevolence, thin Earth lacks trustworthiness; strong Water sitting on its proper ground must be intelligent; firm Metal has convictions and can act" explicitly tie each element to particular ethical and cognitive traits, while "clear Metal‑Water gives brilliance and lust; muddied Water‑Earth produces foolishness" warns that brilliance and sensuality often travel together, and that confusion of drives easily dulls the mind.  
  The middle and later lines apply these associations to relational and biographical events. Combinations like Chen–Xu clashes or Zi–Mao punishments correspond to legal troubles, damaged reputation and breakdown of family etiquette. "Abandoning Seals to chase Wealth" and "abandoning the stem to follow Killing" depict two extreme life strategies: sacrificing roots for gain, or surrendering the self to overwhelming external force. Formulas such as "Wounded Officer without Wealth: skilful yet poor", "Food God controlling Killing but meeting the Devouring Seal: not poor then short‑lived", "men with much Yang Blade will remarry; women with strong Wounded Officer must marry again" and "poverty arises when Officials are damaged; loneliness when Wealth is robbed" map specific Ten‑Spirit patterns to careers, marriages and family roles. The closing cluster on lone‑bird days, bathing/"naked" positions, wine spirits, Eight Exclusives, and interactions with the year ruler and Blade underline that lust, asceticism, early rise or early death are never the product of a single symbol: they crystallise where patterns of configuration and rooting combine with luck cycles to activate or soften what the natal chart promises.  

- 核心要点：
  - **性情**：五行定性情。
  - **婚姻**：孤鸾、沐浴、伤官。
  - **六亲**：财印、官煞。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_009]` `[trigger: 五行性情]` `[factor_trigger: wuxing_xingqing AND musheng_duoren]` `[role: 主干]` 木盛多仁，土薄寡信；水旺居垣须有智，金坚主义却能为。 → 《三命通会》卷十二#六亲与性情
  - `[ns_smth_12_010]` `[trigger: 中和遐龄]` `[factor_trigger: zhonghe_xialing AND yaoshou_pianku]` `[role: 主干依赖]` 遐龄得于中和，夭寿丧于偏枯。 → 《三命通会》卷十二#六亲与性情
  - `[ns_smth_12_011]` `[trigger: 伤官再嫁]` `[factor_trigger: shangguan_zaijia AND yanggren_chonghun]` `[role: 条件分支]` 男多阳刃必重婚，女犯伤官须再嫁。 → 《三命通会》卷十二#六亲与性情
  - `[ns_smth_12_012]` `[trigger: 归禄得财]` `[factor_trigger: guilu_decai AND wucai_guilu_bipin]` `[role: 总结]` 归禄得财而获福，无财归禄必须贫。 → 《三命通会》卷十二#六亲与性情"""
    normalized_text_zh: str = """"""
    subject: str = "3 六亲与性情"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_wuxing_1', 'bazi_semantic', 'bazi_state_factor_95', 'bazi_semantic', 'bazi_relation_factor_37', 'bazi_semantic', 'bazi_relation_shangguan_2', 'bazi_semantic', 'bazi_condition_zi', 'devouring_seal_takes_food', 'bazi_temporal_factor_3', 'bazi_semantic', 'source_ref', 'rel_smth_12_007', 'core_factor', 'rel_smth_12_008', 'cond_factor', 'rel_smth_12_009', 'risk_factor', 'evi_smth_12_007', 'core_factor', 'rule_name7', 'evi_smth_12_008', 'cond_factor', 'rule_name8', 'evi_smth_12_009', 'risk_factor', 'rule_name9', 'map_smth_12_005', 'map_smth_12_006']
    
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
        l1_anchor="smth_v1.0.0_3_六亲与性情_001_L1",
    )
    version: str = "1.0.0"
