"""
Auto-generated semantic module for yuanhaiziping
Generated at: 2025-12-05T13:30:19.558803
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
    semantic_id="yhzp_v1.0.0_2__伤官说_001",
    book_id="yuanhaiziping",
    engine_id="bazi"
)
class 2伤官说(SemanticEntry):
    """
    - **原文（source_text）**：
  伤官若伤尽，却喜见官星。伤官若论财，见祸不轻来。伤官若用印，克杀不如刑。伤官若论财，带合有声名。伤官用财，不宜印乡。伤官见官，印运不妨。杂气财官，印俱...
    """
    
    original_text: str = """- **原文（source_text）**：
  伤官若伤尽，却喜见官星。伤官若论财，见祸不轻来。伤官若用印，克杀不如刑。伤官若论财，带合有声名。伤官用财，不宜印乡。伤官见官，印运不妨。杂气财官，印俱不忌。两戊合一癸，得再嫁。妻财受克，生子不育。印绶比肩，不忌财乡。印绶多根，身旺必贫。印绶被伤，克父母。官杀混杂，克父母。财多身弱，克父母。干与支同克妻。辛卯、戊寅不怕杀多。女命比肩，即姊妹贪合，多谎诈。财有劫，不怕露就杀。火命人最好，月支属火，干头有木提出火矣！癸酉弱格，见杀必凶。官贵太盛，旺处必倾。土命不论胞胎，只论日时，不怕官杀混杂；阳干方论，阴干不取。子怕寅午火，不怕水。寅木不怕金。巳金不怕火。己土不怕木。午火不怕水。未同申金不怕水。己土戌土不怕木。卯木怕酉金。辰土怕寅木。乙日五月不怕杀。四柱元有病，要去病；不去病不发。

- **分字分词释义**：
  - **伤官伤尽**：四柱中伤官纯一无杂官星，或伤官将官星完全制伏，谓之"伤尽"。
  - **却喜见官星**：伤官伤尽之后，行官星运反而可以发福，因为原局已无官可伤。
  - **伤官用财**：伤官生财格，以财星为用神。
  - **不宜印乡**：伤官用财格忌行印运，因印克伤官，破坏生财之源。
  - **印运不妨**：伤官见官格，若有印星通关，行印运反而无碍。
  - **杂气财官**：辰戌丑未月令中的杂气财官。
  - **两戊合一癸**：二戊争合一癸，女命主再嫁。
  - **妻财受克**：财星被克制，主妻不育或克妻。
  - **印绶多根**：印星过多而身旺太过，反为贫命。
  - **干与支同克妻**：天干地支皆克财星，主克妻。
  - **辛卯戊寅不怕杀多**：特殊日柱配合，不惧七杀。
  - **姊妹贪合**：女命比肩多，主姊妹争夫、贪合他人之夫。
  - **露就杀**：财星外露而生杀。
  - **四柱元有病要去病**：命局有病需有药医治，去病方能发福。

- **规范化释义（primary_lang_explained）**：
  本篇汇集伤官格的各种变格和要诀。伤官若伤尽（伤官制官殆尽），反喜见官星运，因原局已无官可伤。伤官若用财为用神，见祸患则灾不轻。伤官用印护身，克杀不如行刑冲运。伤官论财格若带干合，可得声名。伤官用财格不宜行印运（印克伤官）。伤官见官格，行印运则无妨（印通关化解）。杂气月令的财官，印星皆不为忌。女命两戊合一癸，主再嫁。妻财受克，主生子不育或克妻。印绶与比肩同见，不忌财运。印绶多根而身旺，反主贫穷。印绶被伤，主克父母。官杀混杂、财多身弱，皆主克父母。天干地支皆克财，主克妻。辛卯日、戊寅日不怕杀多。女命比肩多，主姊妹贪合、多谎诈。财星有劫财，不怕财露而生杀。火命人最好月支属火、干透甲乙木生火。癸酉弱格见杀必凶。官贵太盛，旺极必衰。土命只论日时不论胎月，不怕官杀混杂，但只论阳干不论阴干。子水怕寅午火不怕水。寅木不怕金。巳金不怕火。己土不怕木。午火不怕水。未土申金不怕水。己土戌土不怕木。卯木怕酉金。辰土怕寅木。乙日五月不怕杀。四柱有病需去病，不去病则不发达。

- **完整对等诠释（secondary_lang_full）**：
  This section compiles various formulas and special cases for the Injuring Officer pattern. When Injuring Officer completely exhausts the Officer (fully subduing official stars), it paradoxically welcomes seeing Officer Star in fortune-running, as the original structure has no Officer left to harm. When Injuring Officer uses Wealth as its useful spirit, encountering disasters brings heavy misfortune. When Injuring Officer uses Seal to protect the self, controlling Killing through clashing works better than direct suppression. When Injuring Officer analyzes Wealth and carries combinations, it achieves reputation and fame. Injuring Officer using Wealth pattern should not go through Seal luck (Seal restrains Injuring Officer). Injuring Officer seeing Officer pattern finds Seal luck unproblematic (Seal bridges and resolves conflict). Mixed-element Wealth and Officer in tomb months find Seal stars non-threatening. For women's fates, two Wu combining with one Gui indicates remarriage. When Wife-Wealth receives restraint, it indicates difficulty bearing children or harming the wife. When Seal and Parallel appear together, Wealth luck is not feared. When Seal has many roots and Self is excessively strong, poverty results instead. When Seal is damaged, it indicates harming parents. Mixed Officer-Killing and Wealth-heavy with weak Self both indicate harming parents. When stems and branches both restrain Wealth, it indicates harming the wife. Xin-Mao and Wu-Yin days do not fear abundant Killing. Women's fates with many Parallels indicate sisters competing for husbands and deceitful nature. When Wealth has Rob-Wealth, exposed Wealth generating Killing is not feared. Fire destiny people benefit most from Fire in the month branch with Wood in stems to generate Fire. Gui-You weak pattern encountering Killing brings certain misfortune. When Officer-Nobility is excessively flourishing, extreme prosperity leads to decline. Earth destiny analyzes only Day and Hour, not Conception and Month, and does not fear mixed Officer-Killing; only Yang stems are analyzed, not Yin stems. Zi Water fears Yin-Wu Fire, not Water. Yin Wood does not fear Metal. Si Metal does not fear Fire. Ji Earth does not fear Wood. Wu Fire does not fear Water. Wei Earth and Shen Metal do not fear Water. Ji and Xu Earth do not fear Wood. Mao Wood fears You Metal. Chen Earth fears Yin Wood. Yi Day in fifth month does not fear Killing. Four Pillars originally having illness requires removing illness; without removing illness, prosperity cannot manifest.

- **核心要点**：
  - 伤官伤尽反喜见官，因原局已无官可伤
  - 伤官用财格忌印运，伤官见官格印运无妨
  - 两戊合一癸主女命再嫁
  - 印绶多根身旺反贫
  - 印绶被伤、官杀混杂、财多身弱皆克父母
  - 辛卯、戊寅特殊日柱不怕杀多
  - 女命比肩多主姊妹贪合
  - 火命人宜月支属火干透木
  - 四柱有病需去病方能发达

- **详细解说**：
  本篇为伤官格的补充要诀，以歌诀形式汇集各种特殊情况和变格规律。"伤官若伤尽，却喜见官星"是伤官格最精要的规律：当伤官已将官星完全制伏（伤尽），原局中无官可伤，此时行官星运反而可以发福，因为官星无从被伤。"伤官用财，不宜印乡；伤官见官，印运不妨"说明伤官配合不同用神时对印星的喜忌不同：用财则忌印（印克伤官破坏生财），见官则喜印（印通关化解伤官见官之忌）。"两戊合一癸，得再嫁"是女命特殊论断，二戊争合一癸主二夫争妻。"印绶多根，身旺必贫"说明印过旺身过强反为贫命，物极必反之理。"四柱元有病，要去病；不去病不发"是命理总纲，命局有病需有药医治，病去方能发达。篇中还列举诸多五行特殊配合，如"子怕寅午火，不怕水"等，皆为经验之谈。

- **叙事素材（narrative_snippets）**：
  - `[ns_yhzp_555]` `[trigger: 伤官伤尽]` `[factor_trigger: injuring_officer AND direct_officer]` `[role: 主干]` 伤官若伤尽，却喜见官星。 → 《渊海子平·伤官说》
  - `[ns_yhzp_556]` `[trigger: 伤官用财忌印]` `[factor_trigger: injuring_officer AND direct_wealth AND direct_seal]` `[role: 条件分支]` 伤官用财，不宜印乡。 → 《渊海子平·伤官说》
  - `[ns_yhzp_557]` `[trigger: 伤官见官喜印]` `[factor_trigger: injuring_officer AND direct_officer AND direct_seal]` `[role: 条件分支]` 伤官见官，印运不妨。 → 《渊海子平·伤官说》
  - `[ns_yhzp_558]` `[trigger: 印多身旺反贫]` `[factor_trigger: direct_seal AND day_master_strength]` `[role: 例外处理]` 印绶多根，身旺必贫。 → 《渊海子平·伤官说》
  - `[ns_yhzp_559]` `[trigger: 四柱去病]` `[factor_trigger: pattern_illness_medicine]` `[role: 总结]` 四柱元有病，要去病；不去病不发。 → 《渊海子平·伤官说》
  - `[ns_yhzp_560]` `[trigger: 两戊合癸再嫁]` `[factor_trigger: tiangan_wu AND tiangan_gui AND female_fate AND anchong_qugui AND angui AND guiguan]` `[role: 条件分支]` 两戊合一癸，得再嫁。 → 《渊海子平·伤官说》"""
    normalized_text_zh: str = """"""
    subject: str = "2. 伤官说"
    factor_refs: list = ['pattern_io_exhausted_proposal', 'pattern_io_wealth', 'pattern_io_officer', 'pattern_illness_medicine']
    
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
        l1_anchor="yhzp_v1.0.0_2__伤官说_001_L1",
    )
    version: str = "1.0.0"
