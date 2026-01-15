"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.559550
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
    semantic_id="yhzp_v1.0.0_弃命从杀论_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 弃命从杀论(SemanticEntry):
    """
    - **原文（source_text）**：  
  弃命从杀论。  
  甲乙无根，怕逢申酉；杀合逢之，双目必朽。乙木酉月，见水为奇；有根丑绝，无根寅危。乙木坐酉，庚丁透露；二库归根，孤神得失。丙火...
    """
    
    original_text: str = """- **原文（source_text）**：  
  弃命从杀论。  
  甲乙无根，怕逢申酉；杀合逢之，双目必朽。乙木酉月，见水为奇；有根丑绝，无根寅危。乙木坐酉，庚丁透露；二库归根，孤神得失。丙火申提，无根从杀；有根南旺，脱根寿促。阳火无根，水乡必忌。阴火无根，水乡有救。阴火酉月，弃命就财；北方入格，南则为灾。戊己亥月，身弱为弃；卯月同推，嫌根劫比。庚金无根，寅宫火局；南方有贵，须防寿促。辛巳阴柔，休囚官杀；运限加金，聪明显达。壬日戌提，癸干未月；运喜东方，逢冲则绝。弃命从财，须要会财。弃命从杀，须要会杀。从财忌杀；从杀喜财；命逢根气，命殒无猜。


- **分字分词释义**：
  - **甲乙无根怕逢申酉**：甲乙木无根，怕逢申酉金地。
  - **杀合逢之双目必朽**：杀星逢合，双目必损。
  - **丙火申提无根从杀有根南旺脱根寿促**：丙火申月无根从杀，有根南旺，脱根寿短。
  - **阳火无根水乡必忌阴火无根水乡有救**：阳火无根忌水，阴火无根喜水。
  - **阴火酉月弃命就财**：阴火酉月弃命从财。
  - **戊己亥月身弱为弃**：戊己土亥月身弱弃命。
  - **庚金无根寅宫火局南方有贵须防寿促**：庚金无根遇火局南方贵但寿短。
  - **弃命从财须要会财弃命从杀须要会杀**：从财须会财，从杀须会杀。
  - **从财忌杀从杀喜财**：从财忌见杀，从杀喜见财。
  - **命逢根气命殒无猜**：命逢根气反破格致凶。
- **规范化释义（primary_lang_explained）**：  
  《弃命从杀论》系统阐述"从格"与"弃命"理论——当日主极弱无根时，不再扶助日主，转而顺从财官杀的强势，形成特殊格局。**甲乙木无根从杀**：甲乙无根怕逢申酉杀地，杀合逢之双目必朽；乙木酉月见水为奇，有根丑绝无根寅危；乙木坐酉庚丁透露，二库归根孤神得失。**丙丁火无根从杀/从财**：丙火申提无根从杀有根南旺脱根寿促；阳火无根水乡必忌，阴火无根水乡有救；阴火酉月弃命就财北方入格南则为灾。**戊己土无根弃命**：戊己亥月身弱为弃，卯月同推嫌根劫比。**庚辛金无根从杀**：庚金无根寅宫火局南方有贵须防寿促；辛巳阴柔休囚官杀运限加金聪明显达。**壬癸水无根从财/从杀**：壬日戌提癸干未月运喜东方逢冲则绝。**从格总则**：弃命从财须要会财，弃命从杀须要会杀；从财忌杀从杀喜财；命逢根气命殒无猜（若有一点根气反而破格致凶）。

- **完整对等诠释（secondary_lang_full）**：  
  **Abandon-Self Follow-Killing Treatise**: Systematic exposition of "Following Patterns" and "Abandon-Self" theory—when Day Master is extremely weak without roots, instead of bolstering Day Master, one follows the strong momentum of Wealth, Officer, or Killing to form special patterns. **Jia-Yi Wood Rootless Following Killing**: Jia-Yi when rootless fear meeting Shen-You Killing positions; when Killing-Harmony meet together, both eyes certainly decay. Yi Wood in You Month seeing Water is extraordinary; having roots meets extinction in Chou, rootless faces danger in Yin. Yi Wood sitting You with Geng-Ding transparent exposed; two storehouses return to roots, solitary spirit gains or loses. **Bing-Ding Fire Rootless Following Killing/Wealth**: Bing Fire with Shen stem when rootless follows Killing; having roots prospers in South, shedding roots shortens longevity. Yang Fire rootless must avoid Water directions; Yin Fire rootless has rescue in Water directions. Yin Fire in You Month abandons self to follow Wealth; Northern direction enters pattern, Southern brings disaster. **Wu-Ji Earth Rootless Abandon-Self**: Wu-Ji in Hai Month with weak body abandons; Mao Month follows the same reasoning, dislikes roots-rob-parallels. **Geng-Xin Metal Rootless Following Killing**: Geng Metal rootless in Yin palace Fire bureau; Southern direction has nobility yet must guard against shortened longevity. Xin-Si is yin-soft with declining-imprisoned Officer-Killing; fortune cycles adding Metal brings intelligence-distinction. **Ren-Gui Water Rootless Following Wealth/Killing**: Ren Day with Xu stem, Gui Stem with Wei Month; fortune favors Eastern direction, meeting clash brings termination. **Following Pattern Principles**: Abandon-self-follow-Wealth requires Wealth convergence; abandon-self-follow-Killing requires Killing convergence. Following Wealth taboos Killing; following Killing favors Wealth. If fate encounters root-qi, fate terminates without doubt (if possessing even slight roots, paradoxically breaks pattern bringing fierceness).

- **核心要点**：  
  - 系统阐述从格/弃命理论：日主极弱无根时顺从财官杀形成特殊格局  
  - 详述十干在无根状态下的从财/从杀条件与吉凶（如阳火忌水、阴火喜水等）  
  - 从格总则：从财须会财忌杀、从杀须会杀喜财、命逢根气反破格致凶  
  - 强调"弃命"与"有根"的临界判断，有一点根气即不可从

- **详细解说**：  《弃命从杀论》系统阐述从格与弃命理论。**甲乙木从杀**——"甲乙无根，怕逢申酉；杀合逢之，双目必朽"揭示甲乙无根从杀之法。**丙丁火从杀/从财**——"丙火申提，无根从杀；有根南旺，脱根寿促"；"阴火酉月，弃命就财"阐述丙丁从格条件。**戊己土弃命**——"戊己亥月，身弱为弃；卯月同推，嫌根劫比"揭示土无根弃命之法。**庚辛金从杀**——"庚金无根，寅宫火局；南方有贵，须防寿促"阐述金从杀条件。**壬癸水从格**——"壬日戌提，癸干未月；运喜东方，逢冲则绝"揭示水从格之法。**从格总则**——"弃命从财，须要会财；弃命从杀，须要会杀"；"从财忌杀，从杀喜财；命逢根气，命殒无猜"点明从格核心法则。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_485]` `[trigger: 甲乙从杀]` `[factor_trigger: jiayi_wugen_feng_shenyou AND shahu_shuangmu_bixiu]` `[role: 条件分支]` 甲乙无根怕逢申酉；杀合逢之双目必朽；甲乙从杀之法。 → 《渊海子平·弃命从杀论》
  - `[ns_yhzp_486]` `[trigger: 丙火从杀]` `[factor_trigger: binghuo_shenti_wugen_congsha AND yougen_nanwang_tuogen_shoucu]` `[role: 条件分支]` 丙火申提无根从杀；有根南旺脱根寿促；丙火从杀条件。 → 《渊海子平·弃命从杀论》
  - `[ns_yhzp_487]` `[trigger: 阴阳火水]` `[factor_trigger: yanghuo_wugen_shuixiang_ji AND yinhuo_wugen_shuixiang_you AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 阳火无根水乡必忌；阴火无根水乡有救；阴阳差异。 → 《渊海子平·弃命从杀论》
  - `[ns_yhzp_488]` `[trigger: 弃命就财]` `[factor_trigger: yinhuo_youyue_qiming_jiucai AND beifang_ruge AND nanfang_weizai AND caiyin AND caiyin_qing_guansha_zu AND changyin]` `[role: 条件分支]` 阴火酉月弃命就财；北方入格南则为灾；从财之法。 → 《渊海子平·弃命从杀论》
  - `[ns_yhzp_489]` `[trigger: 从财会财]` `[factor_trigger: qiming_congcai_xuyao_huicai AND qiming_congsha_xuyao_huisha]` `[role: 主干]` 弃命从财须要会财；弃命从杀须要会杀；从格总则。 → 《渊海子平·弃命从杀论》
  - `[ns_yhzp_490]` `[trigger: 从财忌杀]` `[factor_trigger: congcai_ji_sha AND congsha_xi_cai AND genqi_poge AND congcai AND ji_sha]` `[role: 例外处理]` 从财忌杀从杀喜财；命逢根气命殒无猜；从格禁忌。 → 《渊海子平·弃命从杀论》
  - `[ns_yhzp_491]` `[trigger: 弃命从杀纲领]` `[factor_trigger: qiming_congsha_lun AND shigan_wugen_congge AND huicai_huisha AND genqi_poge]` `[role: 总结]` 弃命从杀论以十干无根从格、会财会杀、根气破格为核心，阐述从格弃命理论。 → 《渊海子平·弃命从杀论》"""
    normalized_text_zh: str = """"""
    subject: str = "弃命从杀论"
    factor_refs: list = ['abandon_follow_killing', 'abandon_follow_wealth', 'following_pattern', 'convene_wealth_killing', 'root_qi_breaks']
    
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
        l1_anchor="yhzp_v1.0.0_弃命从杀论_001_L1",
    )
    version: str = "1.0.0"
