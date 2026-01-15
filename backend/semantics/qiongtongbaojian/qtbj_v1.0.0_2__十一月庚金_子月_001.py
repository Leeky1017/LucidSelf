"""
Auto-generated semantic module for qiongtongbaojian
Generated at: 2025-12-05T13:30:19.578382
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
    semantic_id="qtbj_v1.0.0_2__十一月庚金_子月_001",
    book_id="qiongtongbaojian",
    engine_id="bazi"
)
class 2十一月庚金子月(SemanticEntry):
    """
    - **原文（source_text）**：
  十一月庚金，天气严寒，仍取丁甲，次取丙火照暖。
  或丁甲两透，丙在支中，必主科甲。即无丙火，亦有衣衿。有丁无甲，亦可富中取贵。有甲无丁，只作常人。或...
    """
    
    original_text: str = """- **原文（source_text）**：
  十一月庚金，天气严寒，仍取丁甲，次取丙火照暖。
  或丁甲两透，丙在支中，必主科甲。即无丙火，亦有衣衿。有丁无甲，亦可富中取贵。有甲无丁，只作常人。或丙透丁藏，异途名望。丁藏有甲，武学可许。
  或重重丙火，可许一富，但不清高。丙戊生寅，或丙坐支寅，有一二者，富真贵假。若见癸透。一介寒儒。
  或支成水局，二见丙丁者，此乃伤官格，为人清雅，衣禄常盈，但子息艰难耳。
  或丙丁太多，名官杀混杂最无良。又怕身轻有损伤。如遇东南二运地，焉能挨得过时光。过于清冷，似有凄凉。柱中一派金水，不入火土之乡，主一生孤贫浪荡，难望有成也。

- **分字分词释义**：
  - **十一月**：子月 / 农历十一月 / 癸水当令
  - **天气严寒**：寒冬气候 / 金寒水冷 / 需火暖
  - **照暖**：照耀温暖 / 丙火调候 / 用神
  - **富中取贵**：富裕中求得贵气 / 有官无财 / 次吉
  - **异途名望**：非正途的名声 / 武职 / 次吉
  - **富真贵假**：财富真实贵气虚假 / 有富无贵 / 次吉
  - **一介寒儒**：一个贫寒读书人 / 穷酸 / 凶象
  - **伤官格**：伤官见官格 / 水局见丙丁 / 格局
  - **子息艰难**：子嗣困难 / 官杀受伤 / 凶象
  - **官杀混杂**：正官七杀混杂 / 丙丁太多 / 凶象

- **规范化释义（primary_lang_explained）**：
  十一月（子月）的庚金，天气严寒，仍然取丁火（炼金）和甲木（引丁），其次取丙火照暖（调候）。
  如果丁火甲木两透，丙火在支中，必主科甲。即使无丙火，也有秀才。有丁火无甲木，也可以富中取贵（有官无财生）。有甲木无丁火，只作常人（无炼）。或者丙火透出丁火藏支，异途名望。丁火藏支有甲木，武学可许。
  如果重重丙火（七杀多），可许一富，但不清高（杀重攻身？不，冬月丙火无力，多见反主暖局？原文“富真贵假”）。丙火戊土长生在寅，或者丙火坐支寅（丙寅），有一二个，富真贵假。如果见到癸水透出（伤官见官），一介寒儒。
  如果地支合成水局（伤官局），见到两个丙丁火，这是“伤官格”（伤官见官），为人清雅，衣禄常盈，但子息艰难（火被水伤，官杀为子）。
  如果丙丁太多，名“官杀混杂最无良”。又怕身轻有损伤。如果遇到东南（木火）二运地（火更旺），怎能挨得过时光（身弱不胜官杀）。过于清冷（水多无火），似有凄凉。柱中一派金水，不入火土之乡，主一生孤贫浪荡，难望有成。

- **完整对等诠释（secondary_lang_full）**：
  Geng Metal in the 11th Month (Rat Month): Weather is severe cold. Still use Ding/Jia, then Bing to warm.
  If Ding/Jia reveal and Bing is in branches, Civil Service is certain. Even without Bing, a scholar. With Ding but no Jia, nobility amidst wealth. With Jia but no Ding, ordinary. With Bing revealed and Ding hidden, alternative fame. Ding hidden with Jia, Military School allowed.
  If heavy Bing Fire, one is rich but not pure/aloof. Bing/Wu born in Yin, or Bing sitting on Yin, having 1-2, implies true wealth but fake nobility. If Gui reveals, a poor scholar.
  If branches form a Water Frame, seeing two Bing/Dings, this is "Hurting Officer Pattern" (Seeing Officer); the person is clear/elegant, always well-fed, but children are difficult.
  If Bing/Ding are too many, it is "Officer/Killing Mixed", most unscrupulous. Also fear weak body getting hurt. If meeting SE (Wood/Fire) Luck, how to survive? Too cold implies misery. A mass of Metal/Water in pillars, not entering Fire/Earth Luck, implies a life of lonely poverty and wandering, hard to achieve success.

- **核心要点**：
  - **首要用神**：丁甲丙。严寒需暖，顽金需炼。
  - **金水伤官**：子月伤官旺，喜见官（丙丁）。
  - **官杀混杂**：冬月不怕官杀混杂，因需火暖。但若身弱火多，反受其害。
  - **运势**：金水局喜火土运。"""
    normalized_text_zh: str = """"""
    subject: str = "2. 十一月庚金（子月）"
    factor_refs: list = ['poor_scholar', 'officer_killing_mixed', 'true_wealth_false_noble']
    
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
        l1_anchor="qtbj_v1.0.0_2__十一月庚金_子月_001_L1",
    )
    version: str = "1.0.0"
