# 典籍 原典与本体详细结构

## 目录总览

```
典籍/
├── 中文典籍/                    # 中国传统命理典籍
├── texts/                       # 西方原典
├── 因子本体/                    # 因子系统定义
├── agent_tasks/                 # Agent任务
│
├── # 指导文档
├── 典籍精校与结构化总项目说明.md  # 总项目说明 (38KB)
├── 典籍结构化作业手册.md         # 作业手册 (24KB)
├── Schema工程说明.md            # Schema说明 (11KB)
├── 因子本体_总览_v1.md          # 因子本体总览 (11KB)
├── 精校模板_L1L2.md             # L1/L2精校模板 (30KB)
└── 结构化提取_L3L4_v2.md        # L3/L4提取模板 (21KB)
```

---

## 1. 中文典籍/ - 传统命理典籍

```
中文典籍/
├── 三命通会/                    # 明·万民英 (八字经典)
│   ├── 卷一/                    # 论天干地支
│   ├── 卷二/                    # 论十神
│   ├── ...
│   └── 卷十二/                  # 论杂格
│
├── 子平真诠/                    # 清·沈孝瞻 (八字理论)
│   ├── 论十神/
│   ├── 论格局/
│   ├── 论用神/
│   └── 论行运/
│
├── 渊海子平/                    # 宋·徐子平 (八字源流)
│   ├── 卷上/
│   └── 卷下/
│
├── 穷通宝鉴/                    # 清·余春台 (调候用神)
│   ├── 论十天干/
│   ├── 论月令/
│   ├── 论调候/
│   └── 论节气/
│
├── 滴天髓/                      # 明·刘伯温 (八字精要)
│   ├── 通神论/
│   ├── 天干论/
│   ├── 地支论/
│   └── 形气论/
│
├── 紫微斗数全书/                # 紫微经典
│   ├── 论星曜/
│   ├── 论宫位/
│   ├── 论四化/
│   └── 论格局/
│
├── 周易/                        # 周易经传
│   ├── 上经/                    # 乾至离 (30卦)
│   ├── 下经/                    # 咸至未济 (34卦)
│   ├── 系辞传/
│   └── 说卦传/
│
├── 周公解梦/                    # 解梦典籍
│   ├── 天地日月/
│   ├── 人物身体/
│   └── 动物植物/
│
├── 梦林玄解/                    # 明·陈士元 (解梦大全)
│   ├── 总论/
│   ├── 天象类/
│   ├── 人事类/
│   ├── 器物类/
│   └── ... (36个分类)
│
└── archive/                     # 归档旧版本 (11项)
```

---

## 2. texts/ - 西方原典

```
texts/
├── README.md                    # 西方典籍说明 (11KB)
├── Western_Texts_Template.md    # 西方文本模板 (32KB)
├── L3L4_Extraction_Template.md  # L3/L4提取模板 (13KB)
│
├── # 占星系列
├── Planets in Transit/          # Robert Hand (13章)
│   ├── Chapter_01_Introduction/
│   ├── Chapter_02_Sun/
│   ├── Chapter_03_Moon/
│   └── ...
│
├── astrology of personality/    # Dane Rudhyar
│   ├── Part_1/
│   ├── Part_2/
│   └── Part_3/
│
├── The Inner Sky/               # Steven Forrest (14章)
│   ├── Chapter_01/
│   ├── Chapter_02/
│   └── ...
│
├── Tetrabiblos/                 # Ptolemy (6部分)
│   ├── Book_1/
│   ├── Book_2/
│   ├── Book_3/
│   └── Book_4/
│
├── Christian Astrology, vol. 1 and 2/  # William Lilly
│   ├── Volume_1/
│   └── Volume_2/
│
├── The Astrological Houses/     # Dane Rudhyar (4章)
│
├── # 塔罗系列
├── 78 Degrees of Wisdom/        # Rachel Pollack
│   ├── Major_Arcana/
│   └── Minor_Arcana/
│
├── Learning the Tarot/          # Joan Bunning
│   ├── Lessons/
│   └── Cards/
│
├── The book of Thoth/           # Aleister Crowley (10章)
│   ├── Part_1/
│   ├── Part_2/
│   └── Part_3/
│
├── Waite Pictorial Key to the Tarot/  # A.E. Waite (8章)
│
├── # 心理学系列
├── The Archetypes and the Collective Unconscious/  # Jung (13章)
│   ├── Part_1_Archetypes/
│   ├── Part_2_Collective/
│   └── Part_3_Individual/
│
├── the collected works/         # Jung全集 (5卷)
│
├── The Interpretation of Dreams/  # Freud (12章)
│   ├── Chapter_01/
│   ├── Chapter_02/
│   └── ...
│
├── # 解梦词典
├── The Dreams & Visions Symbol Dictionary/  # (25章)
│   ├── A/
│   ├── B/
│   └── ... (按字母分)
│
└── Llewellyns Complete Dictionary of Dreams/
```

---

## 3. 因子本体/ - 因子系统定义

```
因子本体/
├── README.md                    # 因子本体说明 (1.6KB)
│
├── astro/                       # 西占因子
│   ├── planets.yaml             # 行星因子
│   ├── signs.yaml               # 星座因子
│   ├── houses.yaml              # 宫位因子
│   ├── aspects.yaml             # 相位因子
│   └── README.md
│
├── bazi/                        # 八字因子
│   ├── stems.yaml               # 天干因子
│   ├── branches.yaml            # 地支因子
│   ├── ten_gods.yaml            # 十神因子
│   ├── combinations.yaml        # 合化因子
│   └── README.md
│
├── dream/                       # 解梦因子
│   ├── symbols.yaml             # 符号因子
│   ├── themes.yaml              # 主题因子
│   ├── emotions.yaml            # 情绪因子
│   ├── settings.yaml            # 场景因子
│   └── README.md
│
├── tarot/                       # 塔罗因子
│   ├── major.yaml               # 大阿卡纳
│   ├── minor.yaml               # 小阿卡纳
│   ├── suits.yaml               # 花色因子
│   ├── positions.yaml           # 位置因子
│   └── README.md
│
├── yijing/                      # 周易因子
│   ├── trigrams.yaml            # 八卦因子
│   ├── hexagrams.yaml           # 六十四卦
│   ├── lines.yaml               # 爻位因子
│   ├── changes.yaml             # 变化因子
│   └── README.md
│
├── ziwei/                       # 紫微因子
│   ├── stars.yaml               # 星曜因子
│   ├── palaces.yaml             # 宫位因子
│   ├── sihua.yaml               # 四化因子
│   ├── patterns.yaml            # 格局因子
│   └── README.md
│
└── cross_system/                # 跨系统因子
    └── unified.yaml             # 统一因子映射
```

---

## 4. 文档层次说明

### L1层 - 原文精校
- 保持原文完整性
- 标点断句
- 繁简转换

### L2层 - 结构化标注
- 章节划分
- 段落标记
- 引用标注

### L3层 - 因子提取
- 提取命理因子
- 建立因子关联
- 标注条件逻辑

### L4层 - 语义片段
- 生成推理片段
- 置信度评分
- 权威等级

---

## 5. 统计概览

| 类别 | 书籍数 | 章节数 | 状态 |
|------|--------|--------|------|
| 八字典籍 | 5 | ~50 | L3进行中 |
| 紫微典籍 | 1 | 8 | L2完成 |
| 周易典籍 | 1 | 64+ | L3完成 |
| 解梦典籍 | 2 | ~40 | L3进行中 |
| 西占典籍 | 6 | ~60 | L3完成 |
| 塔罗典籍 | 4 | ~30 | L3完成 |
| 心理学典籍 | 3 | ~30 | L3进行中 |
| **总计** | 22+ | 280+ | - |
