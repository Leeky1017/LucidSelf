"""
Auto-generated semantic module for sanming
Generated at: 2025-12-05T13:30:19.081149
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
    semantic_id="smth_v1.0.0_1_四言独步_节选_001",
    book_id="sanming",
    engine_id="bazi"
)
class 1四言独步节选(SemanticEntry):
    """
    - 原文（source_text）：
  先天何处，后天何处。要知来处，便知去处。
  四柱排定，三才次分。日干为主，配合元辰。
  神煞相绊，轻重较量。先观月令，论格推详。
  以日为主，专论财官。...
    """
    
    original_text: str = """- 原文（source_text）：
  先天何处，后天何处。要知来处，便知去处。
  四柱排定，三才次分。日干为主，配合元辰。
  神煞相绊，轻重较量。先观月令，论格推详。
  以日为主，专论财官。分其贵贱，妙法多端。
  独则易取，乱则难明。去留舒配，论格要精。
  日主高强，月提得令。用财为物，表实为正。
  年根为主，月令为中。日生百刻，时旺时空。
  干与支同，损财伤妻。岁运一类，破弃祖基。
  月令建禄，不住祖屋。一见财官，自然发福。
  用火愁水，用木愁金。轻重论分，祸福能真。
  五行生旺，不怕刑囚。东西南北，数尽方休。
  寅申巳亥，四生之局。用物身强，遇之发福。
  辰戌丑未，四库之神。人元三用，透旺为真。
  子午卯酉，四败之局。男犯兴衰，女犯孤独。
  进气退气，命物相争。进气不死，退气不生。
  财官临库，不冲不发。四柱支干，喜行相合。
  提纲有用，最怕刑冲。冲运则缓，冲用则凶。
  三奇透露，日主专强。寄根有力，福禄荣昌。
  十干化神，有影无形。无中生有，福禄难凭。
  十恶大败，格中大忌。若遇财官，反成富贵。
  格格推详，以煞为重。化煞为权，何愁损用。
  煞不离印，印不离煞。煞印相生，功名显达。
  官煞重逢，制伏有功。如行帝旺，遇之不凶。
  时煞无根，煞旺取贵。时煞多根，煞旺不利。
  八月官星，大忌卯丁。卯丁克破，有情无情。
  印绶根轻，旺中显达。印绶根多，旺中不发。
  印绶比肩，喜行财乡。印绶无比，忌见财伤。
  先财后印，反成其福。先印后财，反成其辱。
  财官印绶，大忌比肩。伤官七煞，反助为权。
  伤官用财，无官有子。伤官无财，子宫有死。
  时上偏财，怕逢兄弟。月印逢财，比肩不忌。
  伤官见官，格中大忌。不损用神，何愁官至。
  拱禄拱贵，填实则凶。提纲有用，论之不同。
  月令财官，遇之发福。名禄高强，比肩夺福。
  日禄居时，青云得路。庚日申时，透财归禄。
  壬骑龙背，见戌无情。寅多则富，辰多则荣。
  天元一气，地物相同。人命得此，位列三公。
  八字连珠，支神有用。造化逢之，名利必重。

- 规范化释义（primary_lang_explained）：  
  本段四言独步，用极精简的四言句，把子平命理的操作顺序与判断重心串成一条主线。它先从“先天、后天”的区分落笔，提醒命理者要分清原始气质与后天环境，再进入“四柱排定、三才次分”的工序：以日干为命主，配合年根、月令与时支，搭出天地人三才的骨架。接着用“先观月令，论格推详”点明总纲——一切格局高低，先从月令是否得用来判断，其次再看财官印绶在干支间的透藏、生克、合冲。  
  诗中用四生、四库、四败三组地支体系，将全局划分为“生发之地、聚蓄之地、破败之地”，并用“进气退气”说明五行旺衰的时序：进气者虽有冲克亦不致死绝，退气者即使一时无伤亦难长久。又以“格格推详，以煞为重”“煞不离印，印不离煞”总括用煞之道——带煞的格局，要么化煞为权，要么以印绶相生，忌煞孤、煞杂而无制。全段看似只是口诀，实则给出了一个从日主、月令、格局、神煞到岁运的完整审视路径。  

- 完整对等诠释（secondary_lang_full）：  
  This four‑character verse compresses the working method of Zi Ping astrology into a chain of decisive steps. It begins by distinguishing "what is innate" from "what is acquired," urging the reader to separate a person's original endowment from later circumstances. It then moves to the technical layout: set the Four Pillars, arrange the Three Powers of Heaven, Earth, and Man, and always treat the Day Stem as the sovereign while Year, Month, and Hour branches form the supporting structure. The line "First observe the month branch, then evaluate the pattern" states the master rule: the quality of any configuration is judged first by whether the month command truly supports it, and only then by how Wealth, Office, and Seals reveal themselves through stems and branches, clashing or combining with the Day Master.  
  The text groups the earthly branches into four birth places, four treasuries, and four defeat positions, sketching a geography of flourishing, storage, and decay. Through the idea of advancing and retreating qi, it teaches that when qi is advancing, even clashes and punishments may not bring collapse, while in retreating qi, apparent calm may hide decline. The repeated emphasis on Killing and Seal—"take each pattern seriously, with Killing as the key; transform Killing into authority; Killing never leaves Seal, Seal never leaves Killing"—encapsulates a strategy for handling harsh configurations: either elevate Killing to a form of legitimate power, or bind it to Seals so that it nourishes rather than destroys. On the surface this is a rhymed formula; in practice it offers a compact roadmap for reading a chart from Day Master and month command out to patterns, auxiliary spirits, and the timing of fate.  

- 核心要点：
  - **总纲**：先观月令，论格推详。
  - **财官**：专论财官。
  - **四地**：四生四库四败。
  - **煞印**：煞印相生。
  - **伤官**：伤官见官大忌。

- **叙事素材（narrative_snippets）**：
  - `[ns_smth_12_033]` `[trigger: 先天后天]` `[factor_trigger: xiantian_houtian AND laigui_zhichu]` `[role: 主干]` 先天何处，后天何处。要知来处，便知去处。四柱排定，三才次分。日干为主，配合元辰。 → 《三命通会》卷十二#四言独步（节选）
  - `[ns_smth_12_034]` `[trigger: 先观月令]` `[factor_trigger: xianguan_yueling AND lunge_tuxiang]` `[role: 主干依赖]` 先观月令，论格推详。以日为主，专论财官。分其贵贱，妙法多端。 → 《三命通会》卷十二#四言独步（节选）
  - `[ns_smth_12_035]` `[trigger: 四生四库]` `[factor_trigger: sisheng_siku AND sibai_zhiju]` `[role: 条件分支]` 寅申巳亥，四生之局。辰戌丑未，四库之神。子午卯酉，四败之局。 → 《三命通会》卷十二#四言独步（节选）
  - `[ns_smth_12_036]` `[trigger: 煞印相生]` `[factor_trigger: shayin_xiangsheng AND gongming_xianda]` `[role: 总结]` 煞不离印，印不离煞。煞印相生，功名显达。 → 《三命通会》卷十二#四言独步（节选）"""
    normalized_text_zh: str = """"""
    subject: str = "1 四言独步（节选）"
    factor_refs: list = ['new_candidate', 'new_candidate', 'engine_id', 'bazi_structure_factor_37', 'bazi_semantic', 'bazi_structure_month_command_geju', 'month_command_central', 'bazi_state_wangshuai', 'bazi_semantic', 'bazi_relation_factor_44', 'killing_with_seal', 'bazi_relation_shangguan_relation', 'wounded_vs_officer', 'bazi_condition_chongke', 'light_heavy_clash', 'bazi_geju', 'killing_first', 'bazi_factor_2', 'transform_killing', 'source_ref', 'rel_smth_12_031', 'core_factor', 'rel_smth_12_032', 'cond_factor', 'rel_smth_12_033', 'risk_factor', 'evi_smth_12_031', 'core_factor', 'rule_name31', 'evi_smth_12_032', 'cond_factor', 'rule_name32', 'evi_smth_12_033', 'risk_factor', 'rule_name33', 'map_smth_12_021', 'map_smth_12_022']
    
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
        l1_anchor="smth_v1.0.0_1_四言独步_节选_001_L1",
    )
    version: str = "1.0.0"
