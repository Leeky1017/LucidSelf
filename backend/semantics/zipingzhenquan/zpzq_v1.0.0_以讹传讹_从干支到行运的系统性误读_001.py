"""
Auto-generated semantic module for zipingzhenquan
Generated at: 2025-12-05T13:30:19.492212
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
    semantic_id="zpzq_v1.0.0_以讹传讹_从干支到行运的系统性误读_001",
    book_id="zipingzhenquan",
    engine_id="bazi"
)
class 以讹传讹从干支到行运的系统性误读(SemanticEntry):
    """
    - **原文（source_text）**：
  三十、论时说以讹传讹。
  八字本有定理，理之不明，遂生导端，妄言妄听，牢不可破。如论干支，则不知阴阳之理，而以俗书体象歌诀为确论；论格局，则不知专寻...
    """
    
    original_text: str = """- **原文（source_text）**：
  三十、论时说以讹传讹。
  八字本有定理，理之不明，遂生导端，妄言妄听，牢不可破。如论干支，则不知阴阳之理，而以俗书体象歌诀为确论；论格局，则不知专寻月令，而以拘泥外格为活变；论生克，则不察喜忌，而以伤旺扶弱为定法；论行运，则不问同中有导，而以干支相类为一例。

  究其缘由，一则书中用字轻重，不知其意，而谬生偏见；一则以鹆书无知妄作，误会其说，而深入迷途；一则论命取运，偶然湊合，而遂以己见为不易；一则以古人命式，亦有误收，即收之不误，又以己意入外格，尤为害人不浅。

  如壬申、癸丑、己丑、甲戌，本杂气财旺生官也，而以为乙亥时，作时上偏官论，岂知旺财生煞，将救死之不暇，于何取贵？

  此类甚多，皆误收格局也。如己未、壬申、戊子、庚申，本食神生财也，而欲弃月令，以为戊日庚申合禄之格，岂知本身自有财食，岂不甚美？又何劳以庚合乙，求局外之官乎？此类甚多，皆硬入外格也。

  人苟中无定见，察理不精，睹此谬论，岂能无惑？何况近日贵格不可解者，亦往往有之乎？岂知行术之人，必以贵命为指归，或将风闻为实据，或探其生日，而即以己意加之生时，谬造贵格，其人之八字，时多未确，即彼本身，亦不自知。若看命者不究其本，而徒以彼既富贵迁就其说以相从，无惑乎终身无解日矣！

- 原注（原文注解）：
  　　本章是在前一篇“拘泥格局”的基础上，再从更大视角批评：**命理系统中，从干支、格局、生克到行运，充满了因误读经典、鹦鹉学舌和硬套外格而造成的“以讹传讹”。**
  - 第一段总说四大问题：
    1) 论干支：不明阴阳、五行本理，却把俗书中的体象歌诀当成“铁律”；
    2) 论格局：不以月令为纲，反以外格为“活变”，把本末倒置当灵活；
    3) 论生克：不察用神喜忌，只凭“伤旺扶弱”的刻板公式判吉凶；
    4) 论行运：不看命局结构中的“同中有导”（格局内的主导关系），只按干支“字面相类”一刀切处理。

  - 第二段追溯原因，概括为四种“误源”：
    1) 不读懂原书用字轻重，误解其意而生偏见；
    2) 引用无知之“鹆书”（鹦鹉学舌之书），误会其说而越走越偏；
    3) 论命取运偶然凑巧，便以己见为定理，不再反省；
    4) 录入古人命式时本就有误，或即便命式无误，又加以外格想象，用以“硬造贵格”，流毒更广。

  - 接着举了两个典型错误案例：
    1) **壬申、癸丑、己丑、甲戌**：
       - 实为“杂气财旺生官”格局；
       - 却被当作“乙亥时上偏官格”来论贵；
       - 作者指出：此类局中旺财生煞，尚且忙于“救死”以防祸，哪里有余力谈贵？
    2) **己未、壬申、戊子、庚申**：
       - 本是“食神生财”佳局；
       - 有人却不论食财，只看“戊日庚申合禄”，硬说是“合禄贵格”；
       - 作者反问：本局自有财食已是美局，又何必舍月令而去求庚合乙之“局外官星”？

  - 最后一段从心理层面批评：
    - 行术之人往往“必以贵命为指归”，喜欢从结果倒推格局；
    - 甚至根据风闻或只知生日，自行补充生时，强造贵格；
    - 这些命式中的时柱多不确连当事人自己亦未必知道；
    - 若看命者不究其本，而徒以彼既富贵迁就其说以相从，无惑乎终身也无法把命理解清楚.

- 分字分词释义：
  - 导端：起头、开端，这里指错误之源.
  - 俗书体象歌诀：民间命书中的形体比象、歌诀之类，多为简化与二手转述.
  - 伤旺扶弱：常见简化公式，以为伤克旺而扶持弱者即可定吉凶.
  - 同中有导：同类之中自有主导与从属，指格局结构内的主线关系.
  - 鹆书：比喻鹦鹉学舌之书，无独立理解而机械抄袭前人.
  - 湊合：偶然相合，非长期普遍之验证.
  - 误收格局：把本不属某格的命式硬套进某格名目.
  - 硬入外格：强行归入外格体系，不顾月令用神.
  - 贵格不可解：现实中某些贵命，用错误理论难以解释，于是再造偏门说法.

- **规范化释义（primary_lang_explained）**：
  本章可看作对子平体系的“方法论自检”：
  - 命理本有相对严密的逻辑系统；
  - 但在长期传播中，若不理解原理，只背歌诀与格名，就必然越来越偏离.

  作者指出几条常见路径：
  - 从干支出发，不谈阴阳与五行，只以“形似”或“歌诀”判断；
  - 从格局出发，不谈月令用神，只以“外格名目”判断；
  - 从生克出发，不谈喜忌，只以“强者宜克、弱者宜扶”的公式判断；
  - 从行运出发，不谈原局结构，只看干支“同类”便作一例判断.

  这些做法的共同特征是：
  - **用表层的标签代替底层的逻辑**；
  - 以少数凑合案例当作普遍定律；
  - 不分清“命理原则”与“个案经验”。

 - **完整对等诠释（secondary_lang_full）**：  
  Behind these errors lies a chain of systematic misunderstandings: treating catchy rhymes and case collections as if they were doctrine, chasing external patterns while abandoning the Month令, applying “strong hurts, weak should be helped” formulas without reference to喜忌, or judging luck purely by干支类别 without asking how they enter the real structure. The common habit is to let surface labels replace the underlying logic of阴阳、五行 and useful gods.

  Such misreadings spread easily: once a few seemingly successful examples are wrapped in attractive格 names, later writers copy them without revisiting the original texts or checking the actual生克. Some even reverse‑engineer noble fates by manufacturing suitable时柱. The antidote is to form a firm view within the Month‑Useful‑God system, always returning to structure and use rather than being fascinated by names. Only then can we resist being misled by pretty but empty pattern labels.

  通过两个命式例子，作者示范了如何“回到月令用神”：
  - 先判断真正的格局（如杂气财旺生官、食神生财）；
  - 再看实际五行生克关系是否支持“贵格”之说；
  - 多数所谓“偏官贵格、合禄贵格”，在这一检验面前不攻自破.

- 详细解说：
  - 这一章不仅在讲命理，更在讲“如何对待知识体系”：
    - 经典文本的用字轻重，需细读而不只看表面；
    - 二手资料与流行说法要严加辨别；
    - 偶然成功经验不能直接晋升为“铁律”；
    - 任何理论都要能解释大多数真实命例，不能只追求“解释极少数贵命”.
  - 对现代命理工程化而言：
    - 本章提醒我们不要把未经验证的民间格名、歌诀直接当成特征；
    - 更不应反过来为了解释少数样本，去创造新格局标签；
    - 应以稳定的原理（用神、格局、生克）为主，以统计验证为辅.

- 核心要点：
  - “以讹传讹”的四个层面：
    1) 懂表不懂里：不懂用字与结构，仅记口号与歌诀；
    2) 信俗不信经：重鹦鹉书，轻经传本；
    3) 因果倒置：以偶然凑合之例，反推理论为“必然”；
    4) 造格迎合：为迎合贵命结果，硬造外格与时格.
  - 真正的学习路径应当是：
    - 先通用神与格局之理；
    - 再看经典命例与少量外格；
    - 最后才是判断某命是否真属外格，而非一开始就以外格为荣.

- 应用推演：
  1) 建立自己的“定见”：以月令用神体系与生克喜忌为根本，不轻易被新奇格名左右；
  2) 对于每一个流行说法（如某某格必贵）：
     - 先用原理逐条核对其是否合理；
     - 再查多例实际命盘验证；
  3) 对于解释不了的贵命：
     - 先怀疑自己对命局或生时的掌握是否准确；
     - 再怀疑是否还有未理解的结构，而不要急于发明新格名；
  4) 在教学与工程中，尽量减少“纯格名式断法”，多回到结构分析与数据验证.

- 反例与边界：
  - 逢人便讲“某年某命是某绝世贵格”，不解释其结构与用神；
  - 把网络、民间书中的格名不加筛选地全部收录进系统；
  - 遇到现实不合的命例，不反省格局理解，而是再造一层更玄的外格.

- 小例（示意）：
  - 一位已成名的企业家，其命局实属“食神生财”而非网络所传“某某贵格”，若系统以食财格解释其创业路径，会比生造贵格更贴近其实际经历；
  - 又有某命被广泛宣传为“时上偏官贵格”，细查则为“杂气财旺生官”，且行运配合，若系统仍执偏官格不放，容易高估其风险、低估其稳定性；
  - 对一批样本同时应用“外格说”和“用神格局说”，若后者在解释力与预测准确度上均明显优于前者，则应据此调低外格说的权重.

- 校勘与字词辨析：
  - “鹆书”一词，多本作“愚书”或“鹦书”，本精校从“鹆”字，取其“鹦鹉学舌”之意；
  - “贵格不可解”在不同版本中亦有作“贵命不可解”，本精校依底本用“贵格”，以突出本章批评的正是“格局迷信”。"""
    normalized_text_zh: str = """"""
    subject: str = "以讹传讹：从干支到行运的系统性误读"
    factor_refs: list = ['yie_chuane', 'yushu', 'wushou_geju', 'yingru_waige', 'engine_id', 'wudu_laiyuan', 'bazi_rule_engine', 'geming_kexin', 'bazi_rule_engine', 'waige_bianjie', 'bazi_rule_engine', 'source_ref', 'rel_zpzq_140', 'geming_kexin', 'rel_zpzq_141', 'wudu_laiyuan', 'evi_zpzq_126', 'waige_bianjie', 'rule_waige_wudu', 'concept_critical', 'concept_root_cause']
    
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
        l1_anchor="zpzq_v1.0.0_以讹传讹_从干支到行运的系统性误读_001_L1",
    )
    version: str = "1.0.0"
