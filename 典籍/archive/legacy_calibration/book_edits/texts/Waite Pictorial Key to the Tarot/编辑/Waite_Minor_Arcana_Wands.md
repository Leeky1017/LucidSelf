# Waite Pictorial Key - Minor Arcana: Wands

**Book**: Waite Pictorial Key to the Tarot (1910)  
**Author**: Arthur Edward Waite  
**Suit**: Wands (Fire Element)  
**Agent**: Text-EN-Agent  
**Format**: L1+L2 Bilingual v2.1 (Simplified for Minor Arcana)

---

## Progress Tracker

**Wands Suit Status**: 14/14 complete ✅
- Number Cards: 10/10 (Ace-Ten) ✅
- Court Cards: 4/4 (Page, Knight, Queen, King) ✅
- L2.5 Bridge Layer: 14/14 ✅
- Factor Layer 8列: 14/14 ✅
- L2-Term Glossary 6列: 14/14 ✅

---

## Note on Minor Arcana Format

Waite's Minor Arcana descriptions are concise divinatory meanings, unlike the theological depth of Major Arcana. This file follows simplified v2.1 format:
- Source Text (Waite's original)
- Core Meaning (English paraphrase)
- Chinese Explanation (complete, not summary)
- Key Terms (3-5 bilingual terms per card)

---

## Wands - Fire Element

**Element**: Fire  
**Keywords**: Energy, passion, creativity, willpower, enterprise, spiritual force  
**Corresponds to**: Creative/spiritual realm, action, inspiration

**Wands Suite Factor Definitions**:
- `[ns_waite_w4]` `[trigger: minor_wands_four]` `[factor_trigger: minor_wands_four]` `[role: 主干]` Four of Wands represents country life, haven, concord—garland between four wands, celebration. → Waite Wands

---

### Ace of Wands

**Source Text**:
> "A hand issuing from a cloud grasps a stout wand or club. Divinatory Meanings: Creation, invention, enterprise, the powers which result in these; principle, beginning, source; birth, family, origin, and in a sense the virility which is behind them; the starting point of enterprises; according to another account, money, fortune, inheritance. Reversed: Fall, decadence, ruin, perdition, to perish also a certain clouded joy."

**Core**: **Creative Source & Beginning** – Divine hand from cloud grasps wand. Creation, invention, enterprise powers; principle, beginning, source; birth/family/origin and virility behind them; enterprise starting point. Also money/fortune/inheritance. **Reversed**: Fall, decadence, ruin, clouded joy.

**Chinese**: **创造源头与开端**——云中神手握权杖。创造、发明、事业之力；原则、开端、源头；诞生/家族/起源及其背后活力；事业起点。也指财富/财产/继承。**逆位**：堕落、衰败、毁灭、阴郁之喜。

#### L2 Semantic Extraction

- **Theme**: Primal creative fire and the beginning of enterprises, representing the seed moment when will and opportunity ignite
- **Natural Attributes**:
  - Symbolism: Divine Hand, Cloud, Wand/Club, Seed of Fire
  - Characteristics: Fiery, initiating, generative, life-giving, virile
  - Elements: Creation, invention, enterprise, birth, family, origin, inheritance
- **Functional Symbolism**:
  - Opens new ventures and inspires creation and invention
  - Launches projects, families, and lineages through concentrated willpower
  - Channels raw creative power into a decisive first step
- **Conditional Structure**:
  - **Necessary Conditions**: Presence of creative opportunity and willingness to act
  - **Enhancing Conditions**: Upright position; clear intention; proper timing for new beginnings
  - **Nullifying Conditions**: Reversed position; misdirected force leading to fall, decadence, ruin, or clouded joy
- **Multi-layered Interpretation**:
  - Literal Layer: New enterprise, creative project, birth, inheritance, financial opportunity
  - Symbolic Layer: The divine spark of creation descending into manifestation
  - Practical Layer: Time to initiate, launch, or birth something new with confidence
  - Psychological Layer: The awakening of creative will and the courage to begin

**Narrative Snippets**:
- `[ns_waite_wands_001]` `[trigger: ace_wands_creation]` `[factor_trigger: minor_wands_ace AND fire_element]` `[role: 主干]` A hand issuing from a cloud grasps a stout wand—creation, invention, enterprise, the powers which result in these. → Source Text
- `[ns_waite_wands_029]` `[trigger: ace_wands_virility]` `[factor_trigger: waite_wands_ace AND origin]` `[role: 条件分支]` Principle, beginning, source; birth, family, origin, and the virility behind them; starting point of enterprises. → Meaning
- `[ns_waite_wands_002]` `[trigger: ace_reversed]` `[factor_trigger: reversed_state AND wands_in_leaf]` `[role: 条件分支]` Reversed: Fall, decadence, ruin, perdition, to perish also a certain clouded joy. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Ace of Wands | 权杖王牌 | Seed of creative fire; first impulse of enterprise and birth | 创造之火的种子；事业与诞生的第一冲动 | minor_wands_ace | existing |
| Divine Hand | 神手 | Supernatural hand emerging from cloud, source of creative power | 自云中伸出的超然之手，象征创造之力的源头 | | new_candidate |
| Enterprise Powers | 事业之力 | Energies that create, invent, and launch ventures | 用于创造、发明、开启事业的能量 | | new_candidate |
| Virility / Source | 活力 / 源头 | Generative life-force behind birth, family and origin | 支撑诞生、家族与起源的生成性生命力 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Ace of Wands | minor_wands_ace | existing | Tarot Card | Seed of creative fire | tarot_semantic | Fire of Fire |
| Functional | New Enterprise | | new_candidate | Life Area | Launching projects | tarot_semantic | Starting point |
| State | Creation↔Decadence | | new_candidate | Condition | Upright/Reversed | tarot_semantic | Polarity |
| Relational | Wands↔Fire | | new_candidate | Element | Energy, will, spirit | tarot_semantic | Elemental link |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_001 | elemental_seed | minor_wands_ace | fire_element | Pure fire seed | When Ace of Wands channels pure fire element as first creative impulse | initiating | Waite #Ace_Wands |
| rel_wands_002 | polarity | minor_wands_ace | reversed_state | Creation vs Decadence | When Ace of Wands polarity shifts between creation (upright) and decadence (reversed) | opposing | Waite #Ace_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_001 | "Creation, invention, enterprise, the powers which result in these" | minor_wands_ace | Divine hand -> creative power -> enterprise | Ace = creative source | High | Yes | rule_wands_ace_creation |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_creative_fire | Primal creative impulse | bing_fire | sign_aries, planet_mars | fire_dream, birth_dream | creative_drive | First spark |
<!-- L2.5_END -->

---

### Two of Wands

**Source Text**:
> "A tall man looks from a battlemented roof over sea and shore; he holds a globe in his right hand, while a staff in his left rests on the battlement; another is fixed in a ring. The Rose and Cross and Lily should be noticed on the left side. Divinatory Meanings: Between the alternative readings there is no marriage possible; on the one hand, riches, fortune, magnificence; on the other, physical suffering, disease, chagrin, sadness, mortification. The design gives one suggestion; here is a lord overlooking his dominion and alternately contemplating a globe; it looks like the malady, the mortification, the sadness of Alexander amidst the grandeur of this world's wealth. Reversed: Surprise, wonder, enchantment, emotion, trouble, fear."

**Core**: **Dominion & Alexander's Malady** – Lord on battlement overlooking dominion, holds globe. **Contradictory**: Riches/magnificence vs suffering/sadness/mortification. Waite's interpretation: **"Alexander amidst world's wealth"** – melancholy of having conquered all yet unfulfilled. Rose, Cross, Lily visible. **Reversed**: Surprise, wonder, trouble, fear.

**Chinese**: **主宰与亚历山大之忧**——主人在城垛俯瞰领地，手持地球仪。**矛盾**：财富/壮丽vs痛苦/悲伤/屈辱。韦特诠释：**"世界财富中的亚历山大"**——征服一切却未满足的忧郁。可见玫瑰、十字、百合。**逆位**：惊讶、奇迹、烦恼、恐惧。

#### L2 Semantic Extraction

- **Theme**: Dominion and existential dissatisfaction—the tension between external greatness and inner emptiness ("Alexander's malady")
- **Natural Attributes**:
  - Symbolism: Lord on battlement, globe in hand, two wands, Rose-Cross-Lily
  - Characteristics: Commanding, strategic, far-seeing, emotionally restless, divided
  - Elements: Dominion, wealth, magnificence vs suffering, sadness, mortification
- **Functional Symbolism**:
  - Evaluates territory and future options from a position of power
  - Plans expansion while weighing what has been achieved against what still feels lacking
  - Represents the melancholy of conquest without inner fulfillment
- **Conditional Structure**:
  - **Necessary Conditions**: Position of power or achievement that prompts reflection
  - **Enhancing Conditions**: Upright position; wealth and broad dominion recognized
  - **Nullifying Conditions**: Reversed position; sudden events shake control, bringing surprise, wonder, trouble, and fear
- **Multi-layered Interpretation**:
  - Literal Layer: Business planning, surveying options, wealth with underlying sadness
  - Symbolic Layer: Alexander amidst world's wealth—the conqueror's ennui
  - Practical Layer: Time to assess what you have and plan next moves with awareness of inner needs
  - Psychological Layer: The recognition that external success does not guarantee inner satisfaction

**Narrative Snippets**:
- `[ns_waite_wands_003]` `[trigger: two_wands_dominion]` `[factor_trigger: minor_wands_two AND alexanders_malady]` `[role: 主干]` A tall man looks from a battlemented roof—here is a lord overlooking his dominion, like Alexander amidst the grandeur of this world's wealth. → Source Text
- `[ns_waite_wands_004]` `[trigger: hermetic_symbols]` `[factor_trigger: hermetic_emblems AND dominion]` `[role: 条件分支]` The Rose and Cross and Lily should be noticed on the left side—esoteric symbols framing worldly power. → Source Text
- `[ns_waite_wands_007]` `[trigger: two_wands_reflection]` `[factor_trigger: minor_wands_two AND reflection]` `[role: 主干]` He holds a globe in his right hand, while a staff in his left rests on the battlement—contemplating the world and his place in it. → Source Text
- `[ns_waite_wands_008]` `[trigger: two_wands_melancholy]` `[factor_trigger: minor_wands_two AND melancholy]` `[role: 条件分支]` The design gives one suggestion; here is a lord overlooking his dominion and alternately contemplating a globe; it looks like the malady, the mortification, the sadness of Alexander amidst the grandeur of this world's wealth. → Source Text

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Two of Wands | 权杖二 | Lord surveying his dominion while holding a globe | 手持地球仪俯瞰领地的领主 | minor_wands_two | existing |
| Dominion | 领地主宰 | Command over lands, wealth and influence | 对土地、财富与影响力的掌控 | | new_candidate |
| Alexander's Malady | 亚历山大之忧 | Melancholy of one who has conquered all yet feels unfulfilled | 征服一切却仍不满足的忧郁心态 | | new_candidate |
| Rose‑Cross‑Lily | 玫瑰‑十字‑百合 | Esoteric Christian‑Hermetic emblems framing the scene | 构成画面的基督‑赫尔墨斯象征徽记 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Two of Wands | minor_wands_two | existing | Tarot Card | Dominion, planning | tarot_semantic | Early Fire |
| Functional | Dominion & Planning | | new_candidate | Life Area | Assessing territory | tarot_semantic | Lord overlooking |
| State | Wealth vs Sadness | | new_candidate | Inner State | Success + dissatisfaction | tarot_semantic | Alexander's malady |
| Relational | Rose‑Cross‑Lily | | new_candidate | Symbolic System | Hermetic tradition | tarot_semantic | Esoteric emblems |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_003 | inner_conflict | minor_wands_two | alexanders_malady | Outer success vs inner void | When Two of Wands shows Alexander's malady: outer success with inner emptiness | paradoxical | Waite #Two_Wands |
| rel_wands_004 | symbolic_frame | minor_wands_two | hermetic_emblems | Rose-Cross-Lily | When Two of Wands Rose-Cross-Lily emblems provide Hermetic esoteric context | contextualizing | Waite #Two_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_002 | "sadness of Alexander amidst the grandeur of this world's wealth" | minor_wands_two | Conquest -> wealth -> unfulfillment | Two = existential dissatisfaction | High | Yes | rule_wands_two_malady |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_dominion_melancholy | Success without fulfillment | | sign_aries, planet_mars | globe_dream, tower_dream | existential_void | Alexander archetype |
<!-- L2.5_END -->

---

### Three of Wands

**Source Text**:
> "A calm, stately personage, with his back turned, looking from a cliff's edge at ships passing over the sea. Three staves are planted in the ground, and he leans slightly on one of them. Divinatory Meanings: He symbolizes established strength, enterprise, effort, trade, commerce, discovery; those are his ships, bearing his merchandise, which are sailing over the sea. The card also signifies able co-operation in business, as if the successful merchant prince were looking from his side towards yours with a view to help you. Reversed: The end of troubles, suspension or cessation of adversity, toil and disappointment."

**Core**: **Merchant Prince & Established Strength** – Figure at cliff edge watching **"his ships bearing his merchandise"** sailing sea. Established strength, enterprise, trade, commerce, discovery. Signifies **"able co-operation in business, successful merchant prince looking towards you to help."** **Reversed**: End of troubles, cessation of adversity.

**Chinese**: **商业王子与既定力量**——人物在悬崖边看**"其船只承载其商品"**航行。既定力量、事业、贸易、商业、发现。象征**"商业中有能力的合作，成功商业王子看向你以帮助"**。**逆位**：烦恼结束，逆境停止。

#### L2 Semantic Extraction

- **Theme**: Established strength and successful trade networks—the vantage point of a merchant prince watching his ventures move abroad
- **Natural Attributes**:
  - Symbolism: Cliff's edge, ships on sea, three staves planted, calm figure
  - Characteristics: Stable, outward-looking, expansive, patient, confident
  - Elements: Trade, commerce, discovery, cooperation, merchandise, distant shores
- **Functional Symbolism**:
  - Oversees enterprises and monitors ships/merchandise in motion
  - Forms cooperative partnerships that extend reach and influence
  - Represents the successful merchant prince offering help to others
- **Conditional Structure**:
  - **Necessary Conditions**: Established position from which to launch ventures
  - **Enhancing Conditions**: Upright position; active expansion and fruitful cooperation
  - **Nullifying Conditions**: Reversed position; troubles winding down, transition into calmer phase after struggle
- **Multi-layered Interpretation**:
  - Literal Layer: Business expansion, overseas ventures, trade partnerships, awaiting returns
  - Symbolic Layer: The consolidation of creative fire into established enterprise
  - Practical Layer: Time to expand, seek partners, and trust in ventures already launched
  - Psychological Layer: Confidence born of having built something real that now operates beyond you

**Narrative Snippets**:
- `[ns_waite_wands_005]` `[trigger: three_wands_merchant]` `[factor_trigger: minor_wands_three AND merchant_prince]` `[role: 主干]` He symbolizes established strength, enterprise, effort, trade, commerce, discovery; those are his ships, bearing his merchandise. → Core
- `[ns_waite_wands_006]` `[trigger: three_wands_coop]` `[factor_trigger: ships_merchandise AND vantage_position]` `[role: 条件分支]` The card signifies able co-operation in business, as if the successful merchant prince were looking from his side towards yours with a view to help you. → Function
- `[ns_waite_wands_030]` `[trigger: three_wands_reversal]` `[factor_trigger: waite_wands_three AND reversal]` `[role: 条件分支]` Reversed: end of troubles, cessation of adversity, toil and disappointment. → Relief

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Three of Wands | 权杖三 | Merchant watching his ships bearing merchandise | 看着载有自己商品之船只的商人 | minor_wands_three | existing |
| Merchant Prince | 商业王子 | Powerful trader whose ventures span distant shores | 事业遍及远方的强大商人 | | new_candidate |
| His Ships / Merchandise | 其船 / 商品 | Ventures and goods sent out into the world | 发送到世界各处的事业与货物 | | new_candidate |
| Able Co‑operation | 有能力合作 | Strong, mutually beneficial business partnership | 互相成就、具实力的商业合作关系 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Three of Wands | minor_wands_three | existing | Tarot Card | Established strength | tarot_semantic | Expansion phase |
| Functional | Trade & Cooperation | | new_candidate | Life Area | Commerce, partnerships | tarot_semantic | Merchant prince |
| State | Waiting for Returns | | new_candidate | Process Stage | Watching outcomes | tarot_semantic | Ships in motion |
| Relational | Expansion Over Sea | | new_candidate | Symbolic Motif | Overseas trade | tarot_semantic | Exploration |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_005 | venture_expansion | minor_wands_three | ships_merchandise | Ventures abroad | When Three of Wands ships represent established strength venturing abroad | expanding | Waite #Three_Wands |
| rel_wands_006 | cooperation | minor_wands_three | merchant_prince | Business help | When Three of Wands merchant prince offers cooperation and business support | supporting | Waite #Three_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_003 | "those are his ships, bearing his merchandise" | minor_wands_three | Ships -> ventures -> established strength | Three = trade expansion | High | Yes | rule_wands_three_trade |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_merchant_expansion | Successful ventures reaching far | | sign_sagittarius | ship_dream, sea_dream | entrepreneurial_vision | Merchant prince |
<!-- L2.5_END -->

---

### Four of Wands

**Source Text**:
> "From the four great staves planted in the foreground there is a great garland suspended; two female figures uplift nosegays; at their side is a bridge over a moat, leading to an old manorial house. Divinatory Meanings: They are for once almost on the surface--country life, haven of refuge, a species of domestic harvest-home, repose, concord, harmony, prosperity, peace, and the perfected work of these. Reversed: The meaning remains unaltered; it is prosperity, increase, felicity, beauty, embellishment."

**Core**: **Harvest-Home & Country Haven** – Four staves with garland, two women with flowers, bridge to manorial house. **"Country life, haven of refuge, domestic harvest-home, repose, concord, harmony, prosperity, peace, perfected work."** **Reversed**: Meaning unaltered – prosperity, increase, felicity, beauty.

**Chinese**: **丰收之家与乡村避风港**——四根权杖挂花环，两女持花束，桥通向庄园。**"乡村生活、避难所、家庭丰收归来、安息、和谐、繁荣、和平、完美之作"**。**逆位**：含义不变——繁荣、增长、幸福、美丽。

#### L2 Semantic Extraction

- **Theme**: Joyful homecoming and communal refuge—the secure base and celebration after work is brought to completion
- **Natural Attributes**:
  - Symbolism: Four staves with garland, two women with flowers, bridge over a moat, old manorial house
  - Characteristics: Festive, peaceful, harmonious, stable, welcoming
  - Elements: Country life, haven of refuge, domestic harvest-home, concord, harmony, prosperity, peace
- **Functional Symbolism**:
  - Marks milestones such as harvest-home, weddings, and community festivals
  - Signals a safe haven, domestic prosperity, and the perfected work of prior efforts
  - Creates a communal space where joy, rest, and harmony can be shared
- **Conditional Structure**:
  - **Necessary Conditions**: Some foundation of work already completed; a shared home or community context
  - **Enhancing Conditions**: Upright position; supportive relationships and a stable environment
  - **Nullifying Conditions**: Severe isolation, conflict, or instability that undermines the sense of refuge
- **Multi-layered Interpretation**:
  - Literal Layer: Celebrations at home, parties, weddings, homecomings, moving into a safe dwelling
  - Symbolic Layer: The house or community as sanctuary after labour—the perfected work that can now be enjoyed
  - Practical Layer: A time to consolidate gains, celebrate achievements, and invest in home and relationships
  - Psychological Layer: Feeling internally safe enough to relax, trust others, and let joy be visible

**Narrative Snippets**:
- `[ns_waite_wands_007]` `[trigger: four_wands_haven]` `[factor_trigger: minor_wands_four AND haven_refuge]` `[role: 主干]` Country life, haven of refuge, a species of domestic harvest-home, repose, concord, harmony, prosperity, peace. → Core
- `[ns_waite_wands_008]` `[trigger: four_wands_harvest]` `[factor_trigger: harvest_home AND always_honesty]` `[role: 条件分支]` The perfected work of these; reversed meaning remains unaltered: prosperity, increase, felicity, beauty. → Meaning
- `[ns_waite_wands_031]` `[trigger: four_wands_garland]` `[factor_trigger: waite_wands_four AND celebration]` `[role: 条件分支]` Four staves with garland, two women with flowers, bridge to manorial house—domestic celebration. → Symbol

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Four of Wands | 权杖四 | Celebration at a country haven/harvest‑home | 乡村避风港 / 丰收归来的庆典 | minor_wands_four | existing |
| Harvest‑Home | 丰收归来 | Domestic celebration of completed work and gathered harvest | 工作完成与收成归来的家庭庆祝 | | new_candidate |
| Haven of Refuge | 避难所 | Safe, peaceful place of rest and harmony | 安全、和平、可安息的空间 | | new_candidate |
| Perfected Work | 完美之作 | Labour brought to full completion and enjoyment | 劳作被完全成就并得以享受的状态 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Four of Wands | minor_wands_four | existing | Tarot Card | Celebration, stability | tarot_semantic | Stable hearth |
| Functional | Home Milestone | | new_candidate | Life Event | Weddings, harvest | tarot_semantic | Domestic completion |
| State | Harmony & Stability | | new_candidate | Condition | Concord, peace | tarot_semantic | Both directions favourable |
| Relational | Four = Structure | | new_candidate | Numerology | Foundation, square | tarot_semantic | Home archetype |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_007 | celebration | minor_wands_four | harvest_home | Domestic completion | When Four of Wands harvest-home celebrates domestic completion and perfected work | celebrating | Waite #Four_Wands |
| rel_wands_008 | stability | minor_wands_four | haven_refuge | Country life | When Four of Wands provides haven and refuge in harmonious country life | sheltering | Waite #Four_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_004 | "country life, haven of refuge, domestic harvest-home" | minor_wands_four | Garland + home -> celebration -> completion | Four = joyful stability | High | Yes | rule_wands_four_haven |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_harvest_celebration | Completion and communal joy | | sign_cancer, house_4 | home_dream, wedding_dream | belonging_security | Haven of refuge |
<!-- L2.5_END -->

---

### Five of Wands

**Source Text**:
> "A posse of youths, who are brandishing staves, as if in sport or strife. It is mimic warfare, and hereto correspond the Divinatory Meanings: Imitation, as, for example, sham fight, but also the strenuous competition and struggle of the search after riches and fortune. In this sense it connects with the battle of life. Hence some attributions say that it is a card of gold, gain, opulence. Reversed: Litigation, disputes, trickery, contradiction."

**Core**: **Mimic Warfare & Battle of Life** – Youths brandishing staves in **"sport or strife"**. **"Mimic warfare"** = sham fight, but also **"strenuous competition and struggle of search after riches and fortune"** = **"battle of life."** Thus: gold, gain, opulence. **Reversed**: Litigation, disputes, trickery.

**Chinese**: **模拟战争与生活之战**——青年挥舞权杖于**"运动或争斗"**。**"模拟战争"**=虚假战斗，也指**"追求财富的激烈竞争与奋斗"**=**"生活之战"**。故：黄金、收益、富裕。**逆位**：诉讼、争执、欺诈。

#### L2 Semantic Extraction

- **Theme**: Competitive struggle and training conflict—play‑fights that mirror the real battle for wealth, success, and position
- **Natural Attributes**:
  - Symbolism: Group of youths, crossing staves, lack of armour or bloodshed, chaotic but non‑fatal clash
  - Characteristics: Dynamic, noisy, high‑energy, contentious, experimental, slightly unruly
  - Elements: Sham fights, drills, contests, rivalry for riches and advancement, everyday "battle of life"
- **Functional Symbolism**:
  - Functions as a training ground where conflict skills, courage, and strategy are tested without total ruin
  - Highlights the competitive environment of career, business, or social standing where many strive for limited rewards
  - Warns that playful rivalry can escalate into real litigation, disputes, or trickery when stakes or egos grow too large
- **Conditional Structure**:
  - **Necessary Conditions**: Presence of peers or rivals; a shared arena (market, workplace, group) where comparison and contest are visible
  - **Enhancing Conditions**: Clear rules or boundaries keeping conflict within sport or practice; mutual recognition that struggle is for growth as well as gain
  - **Nullifying Conditions**: Absence of agreed rules, festering resentment, or greed that turns mimic warfare into destructive feud, lawsuits, or deceit
- **Multi-layered Interpretation**:
  - Literal Layer: Competitions, exams, negotiations, disputes, or market rivalries that demand effort and agility
  - Symbolic Layer: The archetype of life as a training battle in which one learns to fight without losing one's humanity
  - Practical Layer: A period of heightened competition where asserting oneself, learning conflict skills, and managing rivalry are central tasks
  - Psychological Layer: Inner tension between playful assertiveness and aggressive overreach—how one handles anger, ambition, and comparison

**Narrative Snippets**:
- `[ns_waite_wands_009]` `[trigger: five_wands_battle]` `[factor_trigger: minor_wands_five AND battle_of_life]` `[role: 主干]` Mimic warfare, strenuous competition and struggle of the search after riches and fortune—it connects with the battle of life. → Core
- `[ns_waite_wands_032]` `[trigger: five_wands_youths]` `[factor_trigger: waite_wands_five AND competition]` `[role: 条件分支]` A group of youths brandishing staves, as in sport or strife—importunity, strenuous competition. → Symbol
- `[ns_waite_wands_010]` `[trigger: five_wands_litigation]` `[factor_trigger: litigation AND antagonist]` `[role: 条件分支]` Reversed: Litigation, disputes, trickery, contradiction. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Five of Wands | 权杖五 | Mimic warfare symbolizing competitive struggle | 象征竞争奋斗的模拟战争 | minor_wands_five | existing |
| Mimic Warfare | 模拟战争 | Sham fight, non‑lethal training conflict | 非致命、用于训练的假战斗 | | new_candidate |
| Battle of Life | 生活之战 | Struggle for wealth, success and position | 为财富、成功与地位而战的生活之战 | | new_candidate |
| Strenuous Competition | 激烈竞争 | Intense contest for gain and advantage | 为获取收益与优势而进行的激烈竞争 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Five of Wands | minor_wands_five | existing | Tarot Card | Competitive struggle | tarot_semantic | Contest |
| Functional | Competition | | new_candidate | Life Area | Career rivalry | tarot_semantic | Search riches |
| State | Play-Fight vs Litigation | | new_candidate | Condition | Mimic vs real | tarot_semantic | Threshold |
| Relational | Battle of Life | | new_candidate | Archetype | Everyday struggle | tarot_semantic | Mars theme |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_009 | escalation | minor_wands_five | litigation | Play -> real battle | When reversed | intensifying | Waite #Five_Wands |
| rel_wands_010 | life_struggle | minor_wands_five | battle_of_life | Search for riches | When Five of Wands shows battle of life in competitive search for riches | striving | Waite #Five_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_005 | "mimic warfare... strenuous competition and struggle of the search after riches" | minor_wands_five | Sham fight -> competition -> fortune pursuit | Five = competitive striving | High | Yes | rule_wands_five_competition |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_competitive_struggle | Training conflict for life's battles | qisha_competition | sign_aries, planet_mars | fight_dream, competition_dream | competitive_drive | Battle of life |
<!-- L2.5_END -->

---

### Six of Wands

**Source Text**:
> "A laurelled horseman bears one staff adorned with a laurel crown; footmen with staves are at his side. Divinatory Meanings: The card has been so designed that it can cover several significations; on the surface, it is a victor triumphing, but it is also great news, such as might be carried in state by the King's courier; it is expectation crowned with its own desire, the crown of hope, and so forth. Reversed: Apprehension, fear, as of a victorious enemy at the gate; treachery, disloyalty, as of gates being opened to the enemy; also indefinite delay."

**Core**: **Victory & Expectation Crowned** – Laurelled horseman with laurel-crowned staff, footmen attend. **Multiple significations**: Victor triumphing, great news (King's courier), **"expectation crowned with its own desire, crown of hope."** **Reversed**: Fear of victorious enemy, treachery, gates opened to enemy, delay.

**Chinese**: **胜利与期望加冠**——戴桂冠骑士持桂冠权杖，步兵随行。**多重含义**：凯旋胜利，重大消息（国王信使），**"期望以其自身欲望加冠，希望之冠"**。**逆位**：恐惧胜利敌人，背叛，城门为敌开，延迟。

#### L2 Semantic Extraction

- **Theme**: Public victory and recognition—the crowning of hope when long‑held expectations are finally fulfilled
- **Natural Attributes**:
  - Symbolism: Laurelled horseman, laurel‑crowned staff, escorting footmen, processional movement through a crowd or town
  - Characteristics: Triumphant, visible, celebratory, dignified, supported rather than solitary
  - Elements: Victory parade, King's courier, great news, expectation crowned, crown of hope
- **Functional Symbolism**:
  - Announces success, good news, or promotion that is recognised by others, not only felt inwardly
  - Marks the moment when sustained effort and risk are rewarded with honour, reputation, or confirmation of status
  - Emphasises the role of supporters, teams, and messengers in carrying one person's victory out into the world
- **Conditional Structure**:
  - **Necessary Conditions**: A genuine achievement or positive development; an audience, network, or community capable of witnessing it
  - **Enhancing Conditions**: Upright position; humility, gratitude, and willingness to share credit with those who helped
  - **Nullifying Conditions**: Betrayal, disloyalty, fear of enemies "at the gate," or delays that hollow out the sense of triumph
- **Multi-layered Interpretation**:
  - Literal Layer: Success at work, public recognition, awards, good news delivered, or a victorious return from challenge
  - Symbolic Layer: The archetype of the hero welcomed home and crowned—the visible seal that hope and effort were not in vain
  - Practical Layer: A phase to step forward confidently, communicate achievements, and responsibly accept new honours or roles
  - Psychological Layer: Integration of self‑worth with outer validation—learning to receive praise without arrogance or dependence on applause

**Narrative Snippets**:
- `[ns_waite_wands_011]` `[trigger: six_wands_triumph]` `[factor_trigger: minor_wands_six AND expectation_crowned]` `[role: 主干]` A victor triumphing; great news such as might be carried in state by the King's courier; expectation crowned with its own desire, the crown of hope. → Core
- `[ns_waite_wands_012]` `[trigger: six_wands_news]` `[factor_trigger: good_news AND horse_motion]` `[role: 条件分支]` It is also great news, such as might be carried in state by the King's courier. → Meaning
- `[ns_waite_wands_033]` `[trigger: six_wands_reversal]` `[factor_trigger: waite_wands_six AND reversal]` `[role: 条件分支]` Reversed: Apprehension, fear of victorious enemy at gate; treachery, disloyalty, indefinite delay. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Six of Wands | 权杖六 | Laurelled rider returning in triumph | 戴桂冠的骑士凯旋归来 | minor_wands_six | existing |
| Victor Triumphing | 凯旋胜利 | Public victory and honour on display | 公开的胜利与荣耀展示 | | new_candidate |
| Expectation Crowned | 期望加冠 | Long-held hope receiving its reward | 长期期望获得回报之刻 | | new_candidate |
| Crown of Hope | 希望之冠 | Symbol that desire has been fulfilled and recognised | 欲望被成就并获承认的象征冠冕 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Six of Wands | minor_wands_six | existing | Tarot Card | Public victory | tarot_semantic | Achievement |
| Functional | News & Announcement | | new_candidate | Life Event | Good news, success | tarot_semantic | King's courier |
| State | Triumph vs Apprehension | | new_candidate | Condition | Secure vs fear | tarot_semantic | Enemy at gate |
| Relational | Laurel Crown | | new_candidate | Symbol | Victory, honour | tarot_semantic | Classical |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_011 | victory_announcement | minor_wands_six | good_news | Victor triumphing | When Six of Wands victor triumphantly announces good news of public success | proclaiming | Waite #Six_Wands |
| rel_wands_012 | hope_fulfillment | minor_wands_six | expectation_crowned | Desire fulfilled | When Six of Wands crowns long-held expectation with fulfillment | rewarding | Waite #Six_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_006 | "expectation crowned with its own desire, the crown of hope" | minor_wands_six | Expectation -> fulfillment -> public triumph | Six = hope rewarded | High | Yes | rule_wands_six_triumph |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_public_victory | Achievement recognized and celebrated | | planet_sun, sign_leo | victory_dream, parade_dream | achievement_recognition | Crown of hope |
<!-- L2.5_END -->

---

### Seven of Wands

**Source Text**:
| Seven of Wands | 权杖七 | One defender on high ground facing six below | 一名守方立于高处对抗六名来者 | minor_wands_seven | existing |
| Vantage Position | 制高点 | Elevated position giving tactical advantage | 提供战术优势的高位 | | new_candidate |
| Valour | 勇气 | Boldness to stand and resist despite being outnumbered | 在寡不敌众时仍坚守抵抗的勇气 | | new_candidate |
| Wordy Strife | 言辞争斗 | Heated discussion and verbal conflict | 剧烈的讨论与口舌之争 | | new_candidate |

**Narrative Snippets**:
- `[ns_waite_wands_026]` `[trigger: seven_wands_valour]` `[factor_trigger: minor_wands_seven AND valour]` `[role: 主干]` Six are attacking one, who has, however, the vantage position; strength in opposition, he may prove a formidable antagonist. → Core
- `[ns_waite_wands_034]` `[trigger: seven_wands_position]` `[factor_trigger: waite_wands_seven AND defence]` `[role: 条件分支]` It is valour; stiff competition in trade, negotiations, barter; wordy strife of discussion. → Meaning
- `[ns_waite_wands_035]` `[trigger: seven_wands_reversal]` `[factor_trigger: waite_wands_seven AND reversal]` `[role: 条件分支]` Reversed: Perplexity, embarrassments, anxiety; caution against indecision. → Shadow

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Seven of Wands | minor_wands_seven | existing | Tarot Card | Defensive stand | tarot_semantic | Resistance |
| Functional | Defence & Negotiation | | new_candidate | Life Area | Debates, trade wars | tarot_semantic | One vs many |
| State | Courage vs Indecision | | new_candidate | Condition | Brave vs hesitant | tarot_semantic | Cautionary |
| Relational | High Ground | | new_candidate | Archetype | Strategic advantage | tarot_semantic | Just cause |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_013 | defensive_stance | minor_wands_seven | vantage_position | One vs six | When Seven of Wands defender holds vantage position against outnumbering forces | resisting | Waite #Seven_Wands |
| rel_wands_014 | success_through_position | minor_wands_seven | valour | Enemies may not reach | When Seven of Wands valour prevails through tactical advantage enemies cannot reach | prevailing | Waite #Seven_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_007 | "six are attacking one, who has, however, the vantage position" | minor_wands_seven | Outnumbered -> vantage -> success | Seven = defensive success | High | Yes | rule_wands_seven_defence |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_defensive_courage | Standing firm against opposition | | sign_aries | battle_dream, defense_dream | resilience | Vantage position |
<!-- L2.5_END -->

---

### Eight of Wands

**Source Text**:
> "The card represents motion through the immovable-a flight of wands through an open country; but they draw to the term of their course. That which they signify is at hand; it may be even on the threshold. Divinatory Meanings: Activity in undertakings, the path of such activity, swiftness, as that of an express messenger; great haste, great hope, speed towards an end which promises assured felicity; generally, that which is on the move; also the arrows of love. Reversed: Arrows of jealousy, internal dispute, stingings of conscience, quarrels; and domestic disputes for persons who are married."

**Core**: **Motion & Swift Arrival** – Wands flying through open country, **"draw to term of course. That which they signify is at hand; may be on threshold."** Activity, swiftness (express messenger), great haste/hope, **speed towards end promising assured felicity.** That which is on move. Arrows of love. **Reversed**: Arrows of jealousy, internal dispute, conscience stings, domestic quarrels.

**Chinese**: **运动与快速到达**——权杖飞过开阔乡间，**"接近航程终点。它们所象征之事就在手边；可能就在门槛"**。活动、迅速（快递信使）、极大匆忙/希望，**速向承诺确定幸福的终点。**运动中之事。爱之箭。**逆位**：嫉妒之箭、内部争端、良心刺痛、家庭争吵。
 
#### L2 Semantic Extraction

- **Theme**: Swift movement toward an imminent outcome—the last stretch before events arrive and crystallise
- **Natural Attributes**:
  - Symbolism: Flight of wands across open country, no figures visible, trajectory drawing near to its destination
  - Characteristics: Fast, directional, unobstructed, time‑sensitive, charged with expectation
  - Elements: Activity in undertakings, path of action, express messenger, great haste and hope, arrows of love
- **Functional Symbolism**:
  - Signals rapid progress, news in transit, and developments that are already on the way and close at hand
  - Describes the final phase of a process where momentum carries things swiftly toward a promised end state of felicity
  - Includes the "arrows of love"—passionate impulses or messages that move quickly and can change circumstances
- **Conditional Structure**:
  - **Necessary Conditions**: A direction already chosen and energy committed; circumstances that allow motion rather than stagnation
  - **Enhancing Conditions**: Clear intention, timely communication, and willingness to ride the current rather than resist it
  - **Nullifying Conditions**: Jealousy, internal disputes, or domestic quarrels that twist the arrows into sources of hurt and delay
- **Multi-layered Interpretation**:
  - Literal Layer: Travel, fast correspondence, rapid project movement, sudden developments arriving sooner than expected
  - Symbolic Layer: Life phases where events accelerate and "what is meant" draws quickly into the field of experience
  - Practical Layer: Encourages decisive action, efficient communication, and readiness to respond as opportunities or issues land
  - Psychological Layer: The feeling of living on the threshold—excitement mixed with anxiety as change approaches and cannot be slowed easily

**Narrative Snippets**:
- `[ns_waite_wands_015]` `[trigger: eight_wands_swift]` `[factor_trigger: minor_wands_eight AND assured_felicity]` `[role: 主干]` Motion through the immovable—they draw to the term of their course; speed towards an end which promises assured felicity. → Core
- `[ns_waite_wands_036]` `[trigger: eight_wands_threshold]` `[factor_trigger: waite_wands_eight AND imminence]` `[role: 条件分支]` That which they signify is at hand; it may be even on the threshold—activity, swiftness, great haste. → Meaning
- `[ns_waite_wands_016]` `[trigger: eight_wands_arrows]` `[factor_trigger: love_jealousy AND strange_tidings]` `[role: 条件分支]` Also the arrows of love. Reversed: Arrows of jealousy, internal dispute, stingings of conscience. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Eight of Wands | 权杖八 | Flight of wands nearing the end of their course | 接近旅程终点的飞行权杖 | minor_wands_eight | existing |
| At Hand / On the Threshold | 在手边 / 门槛上 | Outcome is imminent and about to arrive | 结果迫近、即将到来 | | new_candidate |
| Assured Felicity | 确定的幸福 | End state promised as joyful and beneficial | 被预示为喜乐且有益的终点状态 | | new_candidate |
| Arrows of Love / Jealousy | 爱之箭 / 嫉妒之箭 | Passionate or envious impulses carried swiftly | 快速射出的爱意或嫉妒冲动 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Eight of Wands | minor_wands_eight | existing | Tarot Card | Swift motion | tarot_semantic | Pure movement |
| Functional | Rapid Development | | new_candidate | Process | Fast progress, news | tarot_semantic | Express messenger |
| State | Imminence | | new_candidate | Time Factor | At hand, threshold | tarot_semantic | Short time |
| Relational | Arrows Motif | | new_candidate | Symbol | Eros/jealousy | tarot_semantic | Passion projectile |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_015 | swift_arrival | minor_wands_eight | assured_felicity | Speed towards end | When Eight of Wands indicates swift arrival of assured felicity at hand | approaching | Waite #Eight_Wands |
| rel_wands_016 | passion_arrows | minor_wands_eight | love_jealousy | Love or envy | When Eight of Wands projects arrows of love (upright) or jealousy (reversed) | projecting | Waite #Eight_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_008 | "draw to the term of their course. That which they signify is at hand" | minor_wands_eight | Flight -> near end -> imminent | Eight = swift arrival | High | Yes | rule_wands_eight_swift |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_swift_movement | Rapid progress toward outcome | | sign_sagittarius, planet_mercury | flying_dream, arrow_dream | momentum_drive | At hand |
<!-- L2.5_END -->

---

### Nine of Wands

**Source Text**:
> "The figure leans upon his staff and has an expectant look, as if awaiting an enemy. Behind are eight other staves--erect, in orderly disposition, like a palisade. Divinatory Meanings: The card signifies strength in opposition. If attacked, the person will meet an onslaught boldly; and his build shews, that he may prove a formidable antagonist. With this main significance there are all its possible adjuncts--delay, suspension, adjournment. Reversed: Obstacles, adversity, calamity."

**Core**: **Strength in Opposition & Formidable Defender** – Figure awaiting enemy, eight staves behind like **"palisade" (defensive wall).** **"Strength in opposition. If attacked, will meet onslaught boldly; may prove formidable antagonist."** Adjuncts: delay, suspension, adjournment. **Reversed**: Obstacles, adversity, calamity.

**Chinese**: **对抗中的力量与强大防御者**——人物等待敌人，八根权杖在后如**"栅栏"（防御墙）**。**"对抗中的力量。若受攻击，将勇敢迎战；可能证明是强大对手"**。附属：延迟、暂停、休会。**逆位**：障碍、逆境、灾难。
 
#### L2 Semantic Extraction

- **Theme**: Wounded but unbroken defender—endurance in the face of repeated trials, delay, and ongoing opposition
- **Natural Attributes**:
  - Symbolism: Figure leaning upon his staff, bandaged head, eight upright staves behind like a palisade, watchful expression
  - Characteristics: Weary yet vigilant, guarded, battle‑scarred, cautious but determined to remain standing
  - Elements: Strength in opposition, formidable antagonist, delay, suspension, adjournment
- **Functional Symbolism**:
  - Represents guarding boundaries and territory after many previous struggles
  - Indicates persisting through postponements, setbacks, or adjournments while preparing for another onslaught
  - Warns that constant expectation of attack can harden into chronic defensiveness and tension
- **Conditional Structure**:
  - **Necessary Conditions**: History of struggle or repeated trials; some boundary, role, or territory that must be defended
  - **Enhancing Conditions**: Clear sense of what is being protected; willingness to stay alert and disciplined despite fatigue
  - **Nullifying Conditions**: Total collapse of will or health, or refusal to defend at all; denial of burnout that makes defence ineffective
- **Multi-layered Interpretation**:
  - Literal Layer: Security concerns, guarding projects or assets, defending legal or professional positions against challenge
  - Symbolic Layer: The archetype of the wounded defender who remains on watch, unwilling to yield hard‑won ground
  - Practical Layer: Advice to maintain boundaries, pace effort, and prepare for "one more round" without sacrificing recovery
  - Psychological Layer: Inner patterns of hyper‑vigilance, perseverance, and fear of being hurt again—need to balance resilience with rest

**Narrative Snippets**:
- `[ns_waite_wands_017]` `[trigger: nine_wands_opposition]` `[factor_trigger: minor_wands_nine AND oppression]` `[role: 主干]` Strength in opposition—if attacked, the person will meet an onslaught boldly and may prove a formidable antagonist. → Core
- `[ns_waite_wands_018]` `[trigger: nine_wands_delay]` `[factor_trigger: palisade AND activity_feeds]` `[role: 条件分支]` With this main significance there are all its possible adjuncts—delay, suspension, adjournment. → Meaning
- `[ns_waite_wands_037]` `[trigger: nine_wands_reversal]` `[factor_trigger: waite_wands_nine AND reversal]` `[role: 条件分支]` Reversed: obstacles, adversity, calamity. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Nine of Wands | 权杖九 | Wounded defender leaning on staff before a palisade | 倩杖站在栅栏前的受伤守卫者 | minor_wands_nine | existing |
| Strength in Opposition | 对抗中的力量 | Capacity to resist attack and stand firm | 在受攻时仍能坚守抵抗的能力 | | new_candidate |
| Palisade | 栅栏防线 | Row of staves forming a defensive barrier | 由权杖构成的防御屏障 | | new_candidate |
| Formidable Antagonist | 强大对手 | Opponent whose resilience makes victory difficult | 因韧性强而难以击败的对手 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Nine of Wands | minor_wands_nine | existing | Tarot Card | Endurance, guarded | tarot_semantic | Near completion |
| Functional | Boundary Defence | | new_candidate | Life Area | Protecting territory | tarot_semantic | Holding lines |
| State | Weary Vigilance | | new_candidate | Condition | Tired but standing | tarot_semantic | Before burnout |
| Relational | Delay / Suspension | | new_candidate | Process Note | Adjunct meanings | tarot_semantic | Time drag |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_017 | resilient_defence | minor_wands_nine | palisade | Strength in opposition | When Nine of Wands palisade provides resilient defense strength if attacked | resisting | Waite #Nine_Wands |
| rel_wands_018 | formidable_stance | minor_wands_nine | antagonist | Difficult to defeat | When Nine of Wands weary defender remains formidably standing to deter antagonists | deterring | Waite #Nine_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_009 | "strength in opposition. If attacked, will meet an onslaught boldly" | minor_wands_nine | Wounded -> still standing -> formidable | Nine = resilient defence | High | Yes | rule_wands_nine_opposition |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_wounded_defender | Endurance despite exhaustion | | sign_scorpio | barrier_dream, guard_dream | perseverance | Palisade |
<!-- L2.5_END -->

---

### Ten of Wands

**Source Text**:
> "A man oppressed by the weight of the ten staves which he is carrying. Divinatory Meanings: A card of many significances, and some of the readings cannot be harmonized. I set aside that which connects it with honour and good faith. The chief meaning is oppression simply, but it is also fortune, gain, any kind of success, and then it is the oppression of these things. It is also a card of false-seeming, disguise, perfidy. The place which the figure is approaching may suffer from the rods that he carries. Success is stultified if the Nine of Swords follows, and if it is a question of a lawsuit, there will be certain loss. Reversed: Contrarieties, difficulties, intrigues, and their analogies."

**Core**: **Oppression of Success & Burden** – Man oppressed by ten staves weight. **"Many significances... cannot be harmonized."** Chief: oppression, but also fortune/gain/success – then **"oppression of these things"** (burden of success). Also: false-seeming, disguise, perfidy. Place approaching may suffer from his rods. Success stultified if Nine Swords follows; lawsuit = certain loss. **Reversed**: Difficulties, intrigues.

**Chinese**: **成功的压迫与重负**——人被十根权杖重量压迫。**"多重含义...无法协调"**。主要：压迫，也指财富/收益/成功——然后**"这些事物的压迫"**（成功的重负）。也指：虚假表象、伪装、背信。接近之地可能受其杖所害。若九剑随后成功受挫；诉讼=必然损失。**逆位**：困难、阴谋。
 
#### L2 Semantic Extraction

- **Theme**: Oppressive burden of responsibilities and success—being weighed down by what one carries and has achieved
- **Natural Attributes**:
  - Symbolism: Man bent forward under the bundle of ten staves, carrying them toward a town or destination
  - Characteristics: Heavy, over‑loaded, strenuous, narrow field of vision, burdened yet still moving
  - Elements: Oppression, fortune, gain, success, oppression of these things, false‑seeming, disguise, perfidy, risk to the place approached
- **Functional Symbolism**:
  - Shows taking on too many tasks, obligations, or ambitions so that success itself becomes a weight
  - Indicates prosperity, responsibility, or roles that have accumulated to the point of limiting freedom and joy
  - Alerts to false‑seeming and disguise—outward success hiding strain, or burdens that may harm those one is approaching
- **Conditional Structure**:
  - **Necessary Conditions**: Substantial responsibilities or gains already accepted; a structure in which one person carries most of the load
  - **Enhancing Conditions**: External expectations, ambition, inability to delegate, and the belief that saying no will endanger success
  - **Nullifying Conditions**: Willingness to redistribute burdens, set limits, or relinquish false obligations before collapse or loss
- **Multi-layered Interpretation**:
  - Literal Layer: Overwork, burnout risk, too many projects or debts, legal or business pressures tied to prior success
  - Symbolic Layer: The archetype of the burden‑bearer—one who carries the rods of fortune until they become instruments of oppression
  - Practical Layer: Call to prioritise, delegate, and simplify commitments so that effort remains sustainable and does not damage outcomes
  - Psychological Layer: Inner sense of having to do everything oneself, hiding exhaustion behind a façade, fear that resting or asking for help will forfeit success

**Narrative Snippets**:
- `[ns_waite_wands_019]` `[trigger: ten_wands_oppression]` `[factor_trigger: minor_wands_ten AND nine_of_swords]` `[role: 主干]` The chief meaning is oppression simply, but it is also fortune, gain, success—and then it is the oppression of these things. → Core
- `[ns_waite_wands_020]` `[trigger: ten_wands_swords]` `[factor_trigger: oppression AND archway]` `[role: 条件分支]` Success is stultified if the Nine of Swords follows; if lawsuit, there will be certain loss. → Warning
- `[ns_waite_wands_038]` `[trigger: ten_wands_reversal]` `[factor_trigger: waite_wands_ten AND reversal]` `[role: 条件分支]` Reversed: contrarieties, difficulties, intrigues, and their analogies. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Ten of Wands | 权杖十 | Man oppressed by the weight of ten staves | 被十根权杖重量压迫之人 | minor_wands_ten | existing |
| Oppression of Success | 成功的压迫 | When gain and prosperity themselves become a heavy load | 收益与繁荣本身转为沉重负担 | | new_candidate |
| False‑Seeming / Disguise | 虚假表象 / 伪装 | Outward appearance hiding strain or bad intent | 掩盖压力或恶意的外在表象 | | new_candidate |
| Burden | 重负 | Excess load of duties, projects or expectations | 过量职责、项目或期望的负荷 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Ten of Wands | minor_wands_ten | existing | Tarot Card | Oppressive burden | tarot_semantic | Completion phase |
| Functional | Overload | | new_candidate | Life Area | Too many tasks | tarot_semantic | Success -> weight |
| State | Carryable vs Crushing | | new_candidate | Condition | Bearable vs breakdown | tarot_semantic | Threshold |
| Relational | Link to Nine of Swords | | new_candidate | Cross-Card | Success stultified | tarot_semantic | Lawsuit loss |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_019 | success_burden | minor_wands_ten | oppression | Fortune -> weight | When Ten of Wands success becomes oppressive burden weighing down achiever | oppressing | Waite #Ten_Wands |
| rel_wands_020 | cross_card | minor_wands_ten | nine_of_swords | Success stultified | When Ten of Wands followed by Nine of Swords indicates success stultified | negating | Waite #Ten_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_010 | "fortune, gain... and then it is the oppression of these things" | minor_wands_ten | Success -> burden -> oppression | Ten = success turned heavy | High | Yes | rule_wands_ten_burden |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_oppressive_success | Achievement becoming burden | | sign_capricorn, planet_saturn | carrying_dream, heavy_load_dream | burnout_overload | Oppression |
<!-- L2.5_END -->

---

**✅ Wands Number Cards Complete (10/14)**

> **Progress**: Ace-Ten完成，剩余Court Cards (Page, Knight, Queen, King)  
> **Next**: Wands Court Cards or 切换至Cups suit

---

## Wands Court Cards

### Page of Wands

**Source Text**:
> "In a scene similar to the former, a young man stands in the act of proclamation. He is unknown but faithful, and his tidings are strange. Divinatory Meanings: Dark young man, faithful, a lover, an envoy, a postman. Beside a man, he will bear favourable testimony concerning him. A dangerous rival, if followed by the Page of Cups. Has the chief qualities of his suit. He may signify family intelligence. Reversed: Anecdotes, announcements, evil news. Also indecision and the instability which accompanies it."

**Core**: **Faithful Messenger & Strange Tidings** – Young man in proclamation act. **Unknown but faithful**, tidings are strange. Dark young man, faithful, lover, envoy, postman. Bears favorable testimony. **Dangerous rival if followed by Page of Cups.** Has Wands suit qualities. May signify family intelligence. **Reversed**: Evil news, indecision, instability.

**Chinese**: **忠诚信使与奇异消息**——年轻人作宣告姿态。**未知但忠诚**，消息奇异。深色年轻人，忠诚，情人，使节，邮差。带来有利证词。**若后随圣杯侍从则为危险对手。**具权杖花色特质。可能指家族情报。**逆位**：坏消息、优柔寡断、不稳定。
 
#### L2 Semantic Extraction

- **Theme**: Fiery messenger and strange tidings—arrival of news that can start movement, desire, or family changes
- **Natural Attributes**:
  - Symbolism: Young man standing in the act of proclamation, staff in hand, desert‑like landscape, posture of announcement
  - Characteristics: Youthful, eager, exploratory, loyal, somewhat naïve but full of initiative and enthusiasm
  - Elements: Dark young man, faithful lover or envoy, postman, strange tidings, family intelligence, core qualities of the Wands suit
- **Functional Symbolism**:
  - Brings messages, invitations, and opportunities related to passion, creativity, travel, or family affairs
  - Acts as a herald whose news can set things in motion or shift the emotional climate around a situation
  - Can personify a Page‑of‑Wands type individual whose presence signals beginnings, experiments, or a new storyline
- **Conditional Structure**:
  - **Necessary Conditions**: A channel for communication—message, messenger, or announcement that can actually reach the querent
  - **Enhancing Conditions**: Openness to hearing and responding to news; contexts involving creative work, romance, or family networks
  - **Nullifying Conditions**: Refusal to listen, chronic indecision, or instability that scatters focus so that good news cannot be used
- **Multi-layered Interpretation**:
  - Literal Layer: Messages, emails, phone calls, visits, or announcements that carry offers, invitations, or news
  - Symbolic Layer: The archetype of the fiery herald who arrives from the horizon with information that awakens desire or initiative
  - Practical Layer: Encourages responding actively to opportunities, exploring new ventures, and noticing who plays the "messenger" role in current events
  - Psychological Layer: Inner urge to speak, express, or start something new—learning to handle excitement without tipping into restlessness or instability

**Narrative Snippets**:
- `[ns_waite_wands_021]` `[trigger: page_wands_faithful]` `[factor_trigger: minor_wands_page AND page_of_cups]` `[role: 主干]` He is unknown but faithful, and his tidings are strange. A dangerous rival if followed by the Page of Cups. → Core
- `[ns_waite_wands_039]` `[trigger: page_wands_envoy]` `[factor_trigger: waite_wands_page AND messenger]` `[role: 条件分支]` Dark young man, faithful, a lover, an envoy, a postman; may signify family intelligence. → Meaning
- `[ns_waite_wands_040]` `[trigger: page_wands_reversal]` `[factor_trigger: waite_wands_page AND reversal]` `[role: 条件分支]` Reversed: anecdotes, announcements, evil news; also indecision and instability. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Page of Wands | 权杖侍从 | Young fiery messenger bearing strange tidings | 带着奇异消息而来的火元素侍从 | minor_wands_page | existing |
| Faithful but Unknown | 忠诚但未知 | Messenger whose loyalty is proven though origin is not well known | 来历不明却忠诚可靠的信使 | | new_candidate |
| Strange Tidings | 奇异消息 | Unusual or surprising news that changes the situation | 改变局势的非同寻常消息 | | new_candidate |
| Dangerous Rival (if Page of Cups) | 危险对手（若连圣杯侍从） | Competitive suitor or rival when paired with Page of Cups | 与圣杯侍从组合时指竞争性的情敌或对手 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Page of Wands | minor_wands_page | existing | Tarot Card | Fiery messenger | tarot_semantic | Court Page |
| Functional | Message & Opportunity | | new_candidate | Life Area | News, invitations | tarot_semantic | Start movement |
| State | Loyal vs Unstable | | new_candidate | Condition | Faithful vs evil news | tarot_semantic | Fire stability |
| Relational | Rivalry with Page of Cups | | new_candidate | Cross-Card | Dangerous rival | tarot_semantic | Fire vs emotion |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_021 | messenger_role | minor_wands_page | strange_tidings | Faithful but unknown | When Page of Wands dark young man delivers faithful but strange tidings | delivering | Waite #Page_Wands |
| rel_wands_022 | cross_card_rivalry | minor_wands_page | page_of_cups | Dangerous rival | When Page of Wands followed by Page of Cups indicates dangerous rivalry | competing | Waite #Page_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_011 | "He is unknown but faithful, and his tidings are strange" | minor_wands_page | Unknown -> faithful -> strange news | Page = reliable messenger | High | Yes | rule_wands_page_tidings |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_fiery_messenger | Young bearer of activating news | | sign_aries | messenger_dream, news_dream | initiator_archetype | Strange tidings |
<!-- L2.5_END -->

---

### Knight of Wands

**Source Text**:
> "He is shewn as if upon a journey, armed with a short wand, and although mailed is not on a warlike errand. He is passing mounds or pyramids. The motion of the horse is a key to the character of its rider, and suggests the precipitate mood, or things connected therewith. Divinatory Meanings: Departure, absence, flight, emigration. A dark young man, friendly. Change of residence. Reversed: Rupture, division, interruption, discord."

**Core**: **Precipitate Journey & Departure** – On journey with short wand, mailed but **not warlike errand**. Passing mounds/pyramids. **"Motion of horse is key to rider's character, suggests precipitate mood."** Departure, absence, flight, emigration. Dark young man, friendly. Change of residence. **Reversed**: Rupture, division, discord.

**Chinese**: **急促旅程与出发**——持短权杖旅行中，有甲但**非战斗任务**。经过土丘/金字塔。**"马的动作是骑士性格关键，暗示急躁情绪"**。出发、缺席、飞行、移民。深色年轻人，友好。居住地改变。**逆位**：破裂、分裂、不和。
 
#### L2 Semantic Extraction

- **Theme**: Sudden movement and fiery departure—impulsive journeys and relocations set in motion
- **Natural Attributes**:
  - Symbolism: Armoured knight on a moving horse, short wand in hand, passing mounds or pyramids, posture of swift advance
  - Characteristics: Fast, restless, adventurous, precipitate; more about going than arriving, not strictly warlike
  - Elements: Departure, absence, flight, emigration, change of residence, dark young man who is friendly
- **Functional Symbolism**:
  - Represents travel, relocation, and energetic departures that quickly change circumstances
  - Personifies a Knight-of-Wands type figure whose entry or exit brings action, excitement, and sometimes disruption
  - Emphasises the "precipitate mood"—decisions and moves made in haste, driven by fire and restlessness
- **Conditional Structure**:
  - **Necessary Conditions**: A situation in which change of scene, travel, or departure is possible or being considered
  - **Enhancing Conditions**: Opportunities for movement, desire for adventure, and willingness to embrace risk and new horizons
  - **Nullifying Conditions**: Immobility through external blocks, or recklessness so great that it turns movement into rupture, division, and discord
- **Multi-layered Interpretation**:
  - Literal Layer: Journeys, moves, emigration, business trips, or sudden visits and departures
  - Symbolic Layer: The archetype of the fiery traveller who embodies change, momentum, and risk-taking
  - Practical Layer: Signals a phase to prepare for relocation or rapid developments, managing logistics so that haste does not create chaos
  - Psychological Layer: Inner restlessness and urge for freedom—need to integrate passion with forethought so that drive does not fracture relationships

**Narrative Snippets**:
- `[ns_waite_wands_022]` `[trigger: knight_wands_departure]` `[factor_trigger: minor_wands_knight AND departure]` `[role: 主干]` Departure, absence, flight, emigration. The motion of the horse is a key to the character of its rider, suggesting precipitate mood. → Core
- `[ns_waite_wands_041]` `[trigger: knight_wands_journey]` `[factor_trigger: waite_wands_knight AND journey]` `[role: 条件分支]` Shewn as if upon a journey, armed with a short wand, mailed but not on warlike errand. → Symbol
- `[ns_waite_wands_042]` `[trigger: knight_wands_reversal]` `[factor_trigger: waite_wands_knight AND reversal]` `[role: 条件分支]` Reversed: rupture, division, interruption, discord. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Knight of Wands | 权杖骑士 | Fiery traveller on a precipitate journey | 处于急促旅程中的火元素骑士 | minor_wands_knight | existing |
| Precipitate Mood | 急躁情绪 | Hasty, impetuous state driving quick action | 推动快速行动的急切冲动状态 | | new_candidate |
| Not Warlike Errand | 非战斗任务 | Journey in armour without explicit war mission | 身披铠甲但并非赴战的旅程 | | new_candidate |
| Change of Residence | 居住地改变 | Moving house, emigrating, or major shift of location | 搬家、移民或重大地点变动 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Knight of Wands | minor_wands_knight | existing | Tarot Card | Mobile Fire | tarot_semantic | Court Knight |
| Functional | Departure & Relocation | | new_candidate | Life Area | Travelling, emigrating | tarot_semantic | Change residence |
| State | Adventurous vs Disruptive | | new_candidate | Condition | Bold vs rupture | tarot_semantic | Edge of chaos |
| Relational | Horse Motion | | new_candidate | Symbol | Speed = temperament | tarot_semantic | Fire in motion |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_023 | precipitate_journey | minor_wands_knight | departure | Not warlike errand | When Knight of Wands departs on precipitate journey though mailed not for war | departing | Waite #Knight_Wands |
| rel_wands_024 | temperament_mirror | minor_wands_knight | horse_motion | Mood = horse speed | When Knight of Wands temperament mirrors horse's precipitate motion | reflecting | Waite #Knight_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_012 | "motion of the horse is a key to the character of its rider, suggests precipitate mood" | minor_wands_knight | Horse motion -> rider character -> precipitate | Knight = impetuous traveller | High | Yes | rule_wands_knight_precipitate |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_swift_departure | Sudden movement and relocation | | sign_sagittarius | journey_dream, horse_dream | restless_drive | Precipitate mood |
<!-- L2.5_END -->

---

### Queen of Wands

**Source Text**:
> "The Wands throughout this suit are always in leaf, as it is a suit of life and animation. Emotionally and otherwise, the Queen's personality corresponds to that of the King, but is more magnetic. Divinatory Meanings: A dark woman, countrywoman, friendly, chaste, loving, honourable. If the card beside her signifies a man, she is well disposed towards him; if a woman, she is interested in the Querent. Also, love of money, or a certain success in business. Reversed: Good, economical, obliging, serviceable. Signifies also--but in certain positions and in the neighbourhood of other cards tending in such directions--opposition, jealousy, even deceit and infidelity."

**Core**: **Magnetic Personality & Life Animation** – **"Wands always in leaf, suit of life and animation."** Queen's personality like King but **more magnetic**. Dark woman, countrywoman, friendly, chaste, loving, honorable. Well disposed to men beside her; interested in Querent if women. Love of money, business success. **Reversed**: Good, economical, serviceable. In certain positions: opposition, jealousy, deceit, infidelity.

**Chinese**: **磁性人格与生命活力**——**"权杖总有叶，生命与活力之花色"**。王后人格似国王但**更具磁性**。深色女性，乡村女性，友好、贞洁、有爱、可敬。对旁边男性友善；若女性则关注询问者。爱金钱，商业成功。**逆位**：善良、节俭、乐助。特定位置：对立、嫉妒、欺骗、不忠。

#### L2 Semantic Extraction

- **Theme**: Warm, magnetic feminine fire—life‑giving queen of the suit of life and animation
- **Natural Attributes**:
  - Symbolism: Enthroned queen with flowering wand, Wands in leaf as signs of life, poised yet relaxed presence
  - Characteristics: Charismatic, friendly, chaste, loving, honourable; more magnetic than the King in emotional radiance
  - Elements: Suit of life and animation, dark woman or countrywoman, love of money, success in business
- **Functional Symbolism**:
  - Signifies a supportive, warm, and capable woman who brings encouragement, protection, and practical help
  - Highlights talent for enterprise and enjoyment of material success without losing generosity
  - Can indicate a person whose interest or favour (toward the Querent or a man beside her) strongly influences outcomes
- **Conditional Structure**:
  - **Necessary Conditions**: Presence of a queen‑like, fiery feminine figure or role; a field where warmth, loyalty, and initiative matter
  - **Enhancing Conditions**: Contexts of cooperation, shared projects, or relational support where her magnetism can be expressed positively
  - **Nullifying Conditions**: Situations of rivalry, insecurity, or distorted fire that flip her into opposition, jealousy, deceit, or infidelity
- **Multi-layered Interpretation**:
  - Literal Layer: A dark or earthy woman, often friendly and honourable, who influences the Querent’s relationships or business affairs
  - Symbolic Layer: Archetype of magnetic feminine fire—life‑giving, animating presence that draws others into her orbit
  - Practical Layer: Period of benefiting from a warm ally or needing to embody her qualities of courage, generosity, and business sense
  - Psychological Layer: Integration of one’s own warm, passionate, and confident feminine side, including the shadow of jealousy or possessiveness

**Narrative Snippets**:
- `[ns_waite_wands_023]` `[trigger: queen_wands_magnetic]` `[factor_trigger: minor_wands_queen AND always_honesty]` `[role: 主干]` The Wands throughout this suit are always in leaf, as it is a suit of life and animation. The Queen's personality is more magnetic than the King. → Core
- `[ns_waite_wands_043]` `[trigger: queen_wands_character]` `[factor_trigger: waite_wands_queen AND character]` `[role: 条件分支]` Dark woman, countrywoman, friendly, chaste, loving, honourable; love of money, success in business. → Meaning
- `[ns_waite_wands_044]` `[trigger: queen_wands_reversal]` `[factor_trigger: waite_wands_queen AND reversal]` `[role: 条件分支]` Reversed: good, economical, serviceable; in certain positions: opposition, jealousy, deceit, infidelity. → Shadow
- `[ns_waite_wands_049]` `[trigger: queen_wands_business]` `[factor_trigger: waite_wands_queen AND business]` `[role: 条件分支]` Also, love of money, or a certain success in business. → Business
- `[ns_waite_wands_050]` `[trigger: queen_wands_interest]` `[factor_trigger: waite_wands_queen AND interest]` `[role: 条件分支]` If the card beside her signifies a man, she is well disposed towards him; if a woman, she is interested in the Querent. → Interest

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| Queen of Wands | 权杖王后 | Magnetic, life‑filled queen of the Fire suit | 充满生命力与磁性的火元素王后 | minor_wands_queen | existing |
| Suit of Life and Animation | 生命与活力花色 | Wands as living, leafy, animated fire | 权杖作为有叶且充满活力的火之花色 | | new_candidate |
| More Magnetic | 更具磁性 | Stronger emotional and social pull than the King | 比国王更具情感与社交吸引力 | | new_candidate |
| Love of Money | 爱金钱 | Affection for wealth and business success | 对财富与商业成功的偏好 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | Queen of Wands | minor_wands_queen | existing | Tarot Card | Feminine Fire | tarot_semantic | Court Queen |
| Functional | Supportive Leadership | | new_candidate | Life Role | Warm, business-savvy | tarot_semantic | Care + enterprise |
| State | Benevolence vs Jealousy | | new_candidate | Condition | Friendly vs opposition | tarot_semantic | Fire relational |
| Relational | Wands in Leaf | | new_candidate | Symbol | Living staves | tarot_semantic | Vitality sign |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_025 | magnetic_presence | minor_wands_queen | king_wands | More magnetic | When Queen of Wands exhibits more magnetic presence than King of same type | attracting | Waite #Queen_Wands |
| rel_wands_026 | living_fire | minor_wands_queen | wands_in_leaf | Suit of life | When Queen of Wands wands in leaf symbolize suit of life and animation | animating | Waite #Queen_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_013 | "Wands throughout this suit are always in leaf, as it is a suit of life and animation" | minor_wands_queen | Wands in leaf -> life + animation -> vitality | Queen = living fire | High | Yes | rule_wands_queen_vitality |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_magnetic_feminine_fire | Warm, charismatic female leadership | | sign_leo | queen_dream, fire_dream | anima_vitality | More magnetic |
<!-- L2.5_END -->

---

### King of Wands

**Source Text**:
> "The physical and emotional nature to which this card is attributed is dark, ardent, lithe, animated, impassioned, noble. The King uplifts a flowering wand, and wears, like his three correspondences in the remaining suits, what is called a cap of maintenance beneath his crown. He connects with the symbol of the lion, which is emblazoned on the back of his throne. Divinatory Meanings: Dark man, friendly, countryman, generally married, honest and conscientious. The card always signifies honesty, and may mean news concerning an unexpected heritage to fall in before very long. Reversed: Good, but severe; austere, yet tolerant."

**Core**: **Noble & Lion Symbol** – **"Dark, ardent, lithe, animated, impassioned, noble"** nature. Uplifts flowering wand, wears **cap of maintenance** beneath crown. **Connected with lion symbol** on throne back. Dark man, friendly, countryman, generally married, honest, conscientious. **Always signifies honesty.** May mean **unexpected heritage news**. **Reversed**: Good but severe; austere yet tolerant.

**Chinese**: **高贵与狮子符号**——**"深色、热情、柔韧、活力、激情、高贵"**本性。举起开花权杖，戴**维护之帽**于王冠下。**与狮子符号相连**在王座背。深色男性，友好，乡民，通常已婚，诚实、认真。**总是象征诚实。**可能指**意外遗产消息**。**逆位**：善良但严厉；苛刻却宽容。

#### L2 Semantic Extraction

- **Theme**: Noble, honest Fire king—embodied authority, integrity, and lion‑like strength
- **Natural Attributes**:
  - Symbolism: King uplifting a flowering wand, cap of maintenance beneath the crown, lion symbol emblazoned on the throne, composed but animated posture
  - Characteristics: Dark, ardent, lithe, animated, impassioned, noble; friendly yet capable of severity when needed
  - Elements: Honest and conscientious dark man, countryman, generally married, card that always signifies honesty, news of unexpected heritage
- **Functional Symbolism**:
  - Represents mature, principled leadership that channels fire into protection, guidance, and stewardship
  - Signifies a man or role that brings trustworthy support, firm decisions, and sometimes inheritance or elevation in status
  - Connects to the lion archetype—strength, kingship, and courageous guardianship rather than reckless dominance
- **Conditional Structure**:
  - **Necessary Conditions**: A context involving authority, responsibility, or rulership where integrity is central
  - **Enhancing Conditions**: Commitment to honesty, willingness to act nobly even when it requires discipline or sacrifice
  - **Nullifying Conditions**: Misuse of power, dishonesty, or refusal to accept rightful responsibility; stress conditions that harden warmth into excessive severity
- **Multi-layered Interpretation**:
  - Literal Layer: A specific dark, generally married man—honest, conscientious, friendly—whose influence is important to the Querent
  - Symbolic Layer: Archetype of noble Fire authority, akin to leonine kingship and sustained, living power (cap of maintenance)
  - Practical Layer: Encourages leading with integrity, offering firm but fair direction, and handling resources or inheritances conscientiously
  - Psychological Layer: Inner mature fire—the capacity to be passionate, strong, and authoritative without losing honesty, fairness, or compassion

**Narrative Snippets**:
- `[ns_waite_wands_024]` `[trigger: king_wands_lion]` `[factor_trigger: minor_wands_king AND lion_symbol]` `[role: 主干]` He connects with the symbol of the lion, which is emblazoned on the back of his throne. The card always signifies honesty. → Core
- `[ns_waite_wands_025]` `[trigger: king_wands_honesty]` `[factor_trigger: king_wands AND valour]` `[role: 条件分支]` Dark man, friendly, generally married, honest and conscientious. May mean news concerning an unexpected heritage. → Meaning
- `[ns_waite_wands_045]` `[trigger: king_wands_reversal]` `[factor_trigger: waite_wands_king AND reversal]` `[role: 条件分支]` Reversed: good, but severe; austere, yet tolerant. → Shadow

#### L2-Term Glossary

| English Term | Chinese Term | English Definition | Chinese Definition | factor_id | status |
|--------------|--------------|-------------------|-------------------|-----------|--------|
| King of Wands | 权杖国王 | Noble, ardent Fire king with lion symbolism | 具狮子象征的高贵火元素国王 | minor_wands_king | existing |
| Cap of Maintenance | 维护之帽 | Headpiece worn under the crown, sign of sustained office | 戴在王冠下、象征持续职分的帽子 | | new_candidate |
| Lion Symbol | 狮子符号 | Emblem of strength, kingship and fiery authority | 象征力量、王权与火性权柄的徽记 | | new_candidate |
| Always Honesty | 总是诚实 | Card that consistently signifies honesty and integrity | 恒常指向诚实与正直的牌 | | new_candidate |

#### Factor Layer

| Factor Type | Factor Label | Factor ID | Factor Source | Role/Position | Value/Constraints | engine_id | Notes |
|-------------|--------------|-----------|---------------|---------------|-------------------|-----------|-------|
| Structure | King of Wands | minor_wands_king | existing | Tarot Card | Mature Fire authority | tarot_semantic | Court King |
| Functional | Leadership & Stewardship | | new_candidate | Life Role | Guides, commands | tarot_semantic | Honest rulership |
| State | Warm Authority vs Severity | | new_candidate | Condition | Noble vs severe | tarot_semantic | Fire governance |
| Relational | Lion Archetype | | new_candidate | Archetype | Leo-like regal | tarot_semantic | Not equating |

<!-- L2.5_BEGIN -->
#### L2.5 Bridge Layer

**Factor Relation Layer**:

| Relation ID | Relation Type | Factor A | Factor B | Relation Nature | Condition Constraint | Effect Direction | source_ref |
|-------------|---------------|----------|----------|-----------------|----------------------|------------------|------------|
| rel_wands_027 | lion_connection | minor_wands_king | lion_symbol | Emblazoned on throne | When King of Wands lion symbol emblazoned on throne authorizes strength and kingship | authorizing | Waite #King_Wands |
| rel_wands_028 | honesty_signification | minor_wands_king | always_honesty | Card always signifies | When King of Wands always signifies honest and conscientious person | affirming | Waite #King_Wands |

**Evidence Chain Layer**:

| Evidence ID | Source Anchor | Involved Factors | Reasoning Step | Conclusion Direction | Confidence | Can Generate Rule | Target Rule ID |
|-------------|---------------|------------------|----------------|----------------------|------------|-------------------|----------------|
| evi_wands_014 | "The card always signifies honesty" | minor_wands_king | King -> always honesty -> integrity | King = honest authority | High | Yes | rule_wands_king_honesty |

**Cross-System Concept Mapping Layer**:

| Concept ID | Common Semantics | Bazi Correspondence | Astrology Correspondence | Dream Correspondence | Psychology Correspondence | Notes |
|------------|------------------|---------------------|--------------------------|----------------------|---------------------------|-------|
| concept_noble_fire_authority | Mature, honest masculine leadership | | sign_leo, planet_sun | king_dream, lion_dream | mature_animus | Lion symbolism |
<!-- L2.5_END -->

---

**🎉 WANDS SUIT COMPLETE (14/14)**

> **Achievement**: Wands全套完成 (Ace-Ten数字牌 + 4张Court Cards)  
> **Terms**: 44个双语术语 (14牌×3-4术语/牌)  
> **Waite Progress**: 36/92张 (39.1%)  
> **Next Suit**: Cups (Chalices) - 14张待精校

---
