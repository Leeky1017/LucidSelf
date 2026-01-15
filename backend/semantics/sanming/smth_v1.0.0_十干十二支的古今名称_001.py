"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.227853
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
    semantic_id="smth_v1.0.0_十干十二支的古今名称_001",
    book_id="sanming",
    engine_id="bazi"
)
class 十干十二支的古今名称(SemanticEntry):
    """
    - **原文（source_text）**：
  其十干曰阏逢、旃蒙、柔兆、疆圉、著雍、屠维、上章、重光、玄默、昭阳。十二支曰困敦、赤奋若、摄提格、单阏、执徐、大荒落、敦牂、恊洽、涒滩、作噩、阉茂、大...
    """
    
    original_text: str = """- **原文（source_text）**：
  其十干曰阏逢、旃蒙、柔兆、疆圉、著雍、屠维、上章、重光、玄默、昭阳。十二支曰困敦、赤奋若、摄提格、单阏、执徐、大荒落、敦牂、恊洽、涒滩、作噩、阉茂、大渊献。蔡邕独断曰：于干也，其名有十，亦曰十母，即今甲、乙、丙、丁、戊、己、庚、辛、壬、癸是也。支，枝也，其名一有二，亦曰十二子，即今子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥是也。

- **分字分词释义**：
  - **阏逢等十名**：十干的上古名称。
  - **困敦等十二名**：十二支的上古名称。
  - **十母**：十干又称十母。
  - **十二子**：十二支又称十二子。
  - **甲乙丙丁戊己庚辛壬癸**：十干现代名称。
  - **子丑寅卯辰巳午未申酉戌亥**：十二支现代名称。

- **规范化释义（primary_lang_explained）**：
  十天干的上古名称为：阏逢、旃蒙、柔兆、疆圉、著雍、屠维、上章、重光、玄默、昭阳。十二地支的上古名称为：困敦、赤奋若、摄提格、单阏、执徐、大荒落、敦牂、恊洽、涒滩、作噩、阉茂、大渊献。东汉蔡邕在《独断》中说：关于天干，其名有十个，又叫"十母"，就是现在的甲、乙、丙、丁、戊、己、庚、辛、壬、癸。地支，就是树枝的"枝"，其名有十二个，又叫"十二子"，就是现在的子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥。

- **完整对等诠释（secondary_lang_full）**：
  The ten Heavenly Stems had ancient names: Yanfeng, Zhanmeng, Rouzhao, Qiangyu, Zhuoyong, Tuwei, Shangzhang, Chongguang, Xuanmo, and Zhaoyang. The twelve Earthly Branches had ancient names: Kundun, Chifenruo, Shetige, Shan'e, Zhixu, Dahuangluo, Dunzang, Xiehe, Tuantan, Zuo'e, Yanmao, and Dayuanxian. Cai Yong of the Eastern Han Dynasty stated in his "Duoduan": "Regarding the Stems, there are ten names, also called 'Ten Mothers,' which are the present-day Jia, Yi, Bing, Ding, Wu, Ji, Geng, Xin, Ren, Gui. The Branches, meaning tree branches, have twelve names, also called 'Twelve Children,' which are the present-day Zi, Chou, Yin, Mao, Chen, Si, Wu, Wei, Shen, You, Xu, Hai."

- **核心要点**：
  - 十干有上古名称和现代名称两套系统
  - 十二支也有上古名称和现代名称两套系统
  - 十干又称"十母"，十二支又称"十二子"
  - 蔡邕《独断》为重要文献来源

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_139]` `[trigger: 干支古今名称]` `[factor_trigger: ganzhi_names AND ten_mothers]` `[role: 主干]` 其十干曰阏逢、旃蒙、柔兆等。蔡邕独断曰：于干也，其名有十，亦曰十母，即今甲、乙、丙、丁等。支，枝也，其名有十二，亦曰十二子。 → 《三命通会》卷一#十干十二支的古今名称

- **详细解说**：
  此条列举干支的古今名称对照。十干的上古名称（阏逢等）和十二支的上古名称（困敦等）都十分古奥，后来简化为甲乙丙丁等和子丑寅卯等。引用东汉学者蔡邕《独断》的权威说法，指出天干有十个，象征生育万物，故称"十母"；地支有十二个，如同树木的枝条，故称"十二子"。母子关系暗示了干支之间的生发关系，体现了阴阳配合、母生子的宇宙观。

- **校勘与字词辨析（双语）**：
  - **中文**：蔡邕（132-192），东汉文学家、书法家。《独断》为其考证古代制度的著作。"其名一有二"疑为"其名有十二"之误。
  - **English**: Cai Yong (132-192 CE) was an Eastern Han scholar and calligrapher. "Duoduan" (Sole Decisions) is his work examining ancient institutions. The phrase likely means "there are twelve names.""""
    normalized_text_zh: str = """"""
    subject: str = "十干十二支的古今名称"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_十干十二支的古今名称_001_L1",
    )
    version: str = "1.0.0"
