"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.228718
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
    semantic_id="smth_v1.0.0_生处不生死处得生_生死反常格局总论_001",
    book_id="sanming",
    engine_id="bazi"
)
class 生处不生死处得生生死反常格局总论(SemanticEntry):
    """
    - **原文（source_text）**：
  庚申木、乙巳火土金生而还不生；丙午水、癸卯金木水死而还不死。土生申而不生于庚申，水生申而不生于戊申，火生寅而不生于甲寅，金生巳而不生于乙巳，木生亥而不...
    """
    
    original_text: str = """- **原文（source_text）**：
  庚申木、乙巳火土金生而还不生；丙午水、癸卯金木水死而还不死。土生申而不生于庚申，水生申而不生于戊申，火生寅而不生于甲寅，金生巳而不生于乙巳，木生亥而不生于辛亥，盖生处而反受制故也。得之者夭寿。水死卯而不死于癸卯，土死卯而不死于丁卯，木死午而不死于丙午，金死子而不死于庚子，火死酉而不死于辛酉，盖死处得生也。若得之者长寿。

- **分字分词释义**：
  - **生而还不生**：处在应当生旺的位置，却因为反受克制而不能真正生发。
  - **死而还不死**：处在应当死绝的位置，却因为另有生助而反得生机。
  - **生处而反受制**：本应生扶之地，反而成了被克之所。
  - **死处得生**：本应死绝之地，却反而获得生气。
  - **夭寿**：短命早亡。
  - **长寿**：寿命绵长。

- **规范化释义（primary_lang_explained）**：
  本段总论若干干支在长生死绝上的反常现象。庚申木、乙巳火，本应在土、金所生扶的位置，却因为同时又被克制，形成“生处而反受制”，所以叫“生而还不生”；丙午水、癸卯金，本在水、木之死绝之地，却又得到别处之气相生，形成“死处得生”，所以叫“死而还不死”。归纳起来，土虽然生申，却不生在庚申；水虽然生申，却不生在戊申；火虽然生寅，却不生在甲寅；金虽然生巳，却不生在乙巳；木虽然生亥，却不生在辛亥——都是“生地反被制服”，得此格者多主夭寿。反之，水虽死于卯，却不死在癸卯；土死于卯，却不死在丁卯；木死于午，却不死在丙午；金死于子，却不死在庚子；火死于酉，却不死在辛酉——都是“死中得生”，得此格者多主长寿。

- **完整对等诠释（secondary_lang_full）**：
  This passage summarizes several anomalous cases in the lifecycle stages of stems and branches. Gengshen Wood and Yisi Fire, in theory should be nourished by Earth and Metal, yet because they are simultaneously controlled, they are at a “birth-place that in fact does not generate,” hence “born yet not born.” Bingwu Water and Guimao Metal are located at positions where Water or Wood should be dead-extinct, yet they receive supporting qi from elsewhere, becoming “death-places that in fact obtain life,” hence “dead yet not dead.” In brief: although Earth generates Shen, it does not truly generate at Gengshen; although Water generates Shen, it does not truly generate at Wushen; although Fire generates Yin, it does not generate at Jiayin; although Metal generates Si, it does not generate at Yisi; although Wood generates Hai, it does not generate at Xinhai—these are all birth-positions that instead are constrained, and those who carry such patterns are mostly short‑lived. Conversely, though Water dies at Mao, it does not die at Guimao; Earth dies at Mao yet not at Dingmao; Wood dies at Wu yet not at Bingwu; Metal dies at Zi yet not at Gengzi; Fire dies at You yet not at Xinyou—these are death‑positions that instead obtain life, and those who carry such patterns are mostly long‑lived.

- **核心要点**：
  - 提出“生而不生、死而不死”的两类反常格局
  - 生处反受制，多主夭寿
  - 死处反得生，多主长寿
  - 判断时需同时看长生死绝与实际生克

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_01_247]` `[trigger: 生死反常格局]` `[factor_trigger: birth_place_not_generating_short_life AND death_place_obtains_life_longevity AND lifecycle_needs_actual_control_check]` `[role: 主干]` 庚申木、乙巳火土金生而还不生；丙午水、癸卯金木水死而还不死。土生申而不生于庚申，水生申而不生于戊申，火生寅而不生于甲寅，金生巳而不生于乙巳，木生亥而不生于辛亥，盖生处而反受制故也。得之者夭寿。水死卯而不死于癸卯，土死卯而不死于丁卯，木死午而不死于丙午，金死子而不死于庚子，火死酉而不死于辛酉，盖死处得生也。若得之者长寿。 → 《三命通会》卷一#生死反常格局

- **详细解说**：
  传统长生死绝只给出一个“名位”，但本段指出，还要看该位上真实的生克力量：如果名义上是生地，却又被强力制服，就会出现“生处不生”的现象，反主夭折；如果名义上是死地，却又暗合生助之气，就会出现“死处得生”的现象，反主长寿。这里列出的十个干支组合，就是典型的“生反不生、死反不死”的例子。实务推命时，遇到相关干支，不可以只凭“长生”或“死绝”二字下断，而要回到整体生克与强弱上来判断。

- **校勘与字词辨析（双语）**：
  - **中文**：“生而还不生”“死而还不死”是就气机实效而言，并非否定长生死绝之名位；“夭寿”“长寿”是寿命高低的总括说法。
  - **English**: “Born yet not born” and “dead yet not dead” describe the real effect of qi, not a denial of the formal lifecycle stage; “short‑lived” and “long‑lived” are global descriptions of lifespan outcome."""
    normalized_text_zh: str = """"""
    subject: str = "生处不生死处得生：生死反常格局总论"
    factor_refs: list = ['new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate', 'new_candidate']
    
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
        l1_anchor="smth_v1.0.0_生处不生死处得生_生死反常格局总论_001_L1",
    )
    version: str = "1.0.0"
