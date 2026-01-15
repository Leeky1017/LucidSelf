# Data 数据资产详细结构

## 目录总览

```
data/
├── rules/                # 规则文件
├── factor_ontology/      # 因子本体
├── logic_chains/         # 逻辑链
├── knowledge_graph/      # 知识图谱配置
├── scenario_templates/   # 场景模板
├── schema_staging/       # Schema暂存
├── dream/                # 解梦数据
├── yijing/               # 周易数据
├── tarot/                # 塔罗数据
├── solar_terms/          # 节气数据
├── engines/              # 引擎配置
├── archive/              # 归档数据
├── golden_set/           # 黄金测试集
├── sources/              # 原始数据源
├── system/               # 系统数据
└── cities500.txt         # 城市数据库 (38MB)
```

---

## 1. rules/ - 规则文件

各引擎的YAML规则定义

```
rules/
├── README.md             # 规则说明
├── registry.json         # 规则注册表
│
├── astro/                # 西方占星规则
│   ├── core.yaml         # 核心规则
│   ├── aspects.yaml      # 相位规则
│   └── houses.yaml       # 宫位规则
│
├── bazi/                 # 八字规则
│   ├── core.yaml         # 核心规则
│   ├── ten_gods.yaml     # 十神规则
│   ├── dayun.yaml        # 大运规则
│   ├── combinations.yaml # 合化规则
│   └── clashes.yaml      # 冲克规则
│
├── dream/                # 解梦规则
│   ├── symbols.yaml      # 符号规则
│   ├── themes.yaml       # 主题规则
│   └── emotions.yaml     # 情绪规则
│
├── tarot/                # 塔罗规则
│   ├── major.yaml        # 大阿卡纳
│   ├── minor.yaml        # 小阿卡纳
│   └── spreads.yaml      # 牌阵规则
│
├── yijing/               # 周易规则
│   ├── hexagrams.yaml    # 卦象规则
│   ├── lines.yaml        # 爻辞规则
│   └── trigrams.yaml     # 八卦规则
│
├── ziwei/                # 紫微规则
│   ├── stars.yaml        # 星曜规则
│   ├── palaces.yaml      # 宫位规则
│   └── sihua.yaml        # 四化规则
│
├── psychology/           # 心理学规则
│   ├── archetypes.yaml   # 原型规则
│   ├── dreams.yaml       # 梦境规则
│   └── symbols.yaml      # 符号规则
│
└── generated/            # 生成的规则 (33个文件)
```

---

## 2. factor_ontology/ - 因子本体

因子系统定义与分类

```
factor_ontology/
├── namespace.yaml        # 命名空间定义
├── factor_schema.yaml    # 因子Schema (7.6KB)
│
├── candidates/           # 候选因子 (8个引擎)
│   ├── astro.yaml
│   ├── bazi.yaml
│   ├── dream.yaml
│   ├── tarot.yaml
│   ├── yijing.yaml
│   ├── ziwei.yaml
│   └── ...
│
└── certified/            # 认证因子 (8个引擎)
    ├── astro.yaml
    ├── bazi.yaml
    ├── dream.yaml
    ├── tarot.yaml
    ├── yijing.yaml
    ├── ziwei.yaml
    └── ...
```

---

## 3. logic_chains/ - 逻辑链

从典籍提取的推理链

```
logic_chains/
├── build_report.md           # 构建报告
├── build_report_v2.json      # V2报告
├── build_report_v2.md        # V2报告MD
├── book_quality_thresholds.yaml  # 质量阈值
│
├── # 西方占星 (~22MB)
├── planets_in_transit.yaml        # 行星过境 (19MB)
├── astrology_of_personality.yaml  # 占星人格 (2.6MB)
├── tetrabiblos.yaml               # 四书
├── the_inner_sky.yaml             # 内在天空
├── the_astrological_houses.yaml   # 占星宫位
├── christian_astrology,_vol._1_and_2.yaml
│
├── # 塔罗 (~1.4MB)
├── 78_degrees_of_wisdom.yaml      # 78度智慧
├── learning_the_tarot.yaml        # 学习塔罗
├── the_book_of_thoth.yaml         # 托特之书
├── waite_pictorial_key_to_the_tarot.yaml
│
├── # 解梦 (~10MB)
├── dreams_visions_symbol_dictionary.yaml  # 符号词典 (3MB)
├── the_dreams_&_visions_symbol_dictionary.yaml
├── the_archetypes_and_the_collective_unconscious.yaml  # 原型 (5.6MB)
├── the_interpretation_of_dreams.yaml
├── llewellyns_complete_dictionary_of_dreams.yaml
│
├── # 周易 (5.3MB)
├── 周易.yaml
│
├── # 八字 (~32MB)
├── 三命通会.yaml                  # 最大 (26MB)
├── 穷通宝鉴.yaml                  # (2.8MB)
├── 子平真诠.yaml
├── 渊海子平.yaml
├── 滴天髓.yaml
├── 梦林玄解.yaml
│
├── # 紫微
├── 紫微斗数全书.yaml
│
├── # 解梦
├── 周公解梦.yaml
│
└── archive/                       # 归档
```

**总计**: ~70MB逻辑链数据

---

## 4. knowledge_graph/ - 知识图谱配置

```
knowledge_graph/
├── aggregation_rules.yaml    # 聚合规则
├── authority_config.yaml     # 权威配置
├── conflict_templates.yaml   # 冲突模板
├── dimension_config.yaml     # 维度配置
├── selector_config.yaml      # 选择器配置
├── exports/                  # 导出目录
└── snapshots/                # 快照目录
```

---

## 5. scenario_templates/ - 场景模板

```
scenario_templates/
├── career.yaml           # 事业场景
├── relationship.yaml     # 感情场景
├── health.yaml           # 健康场景
├── wealth.yaml           # 财富场景
├── decision.yaml         # 决策场景
├── timing.yaml           # 择时场景
└── general.yaml          # 通用场景
```

---

## 6. schema_staging/ - Schema暂存

用于代码生成的中间Schema

```
schema_staging/
├── bazi/                 # 八字Schema
├── astro/                # 占星Schema
├── dream/                # 解梦Schema
├── tarot/                # 塔罗Schema
├── yijing/               # 周易Schema
├── ziwei/                # 紫微Schema
└── ... (共82个文件)
```

---

## 7. 其他数据目录

### dream/
```
dream/
├── symbols.yaml          # 梦境符号
├── themes.yaml           # 梦境主题
├── emotions.yaml         # 情绪映射
└── categories.yaml       # 分类定义
```

### yijing/
```
yijing/
├── hexagrams.yaml        # 64卦
└── trigrams.yaml         # 八卦
```

### tarot/
```
tarot/
└── deck.yaml             # 塔罗牌组
```

### solar_terms/
```
solar_terms/
└── terms_1900_2100.yaml  # 节气表
```

### engines/
```
engines/
└── config.yaml           # 引擎配置
```

---

## 数据统计

| 类别 | 文件数 | 总大小 |
|------|--------|--------|
| rules/ | ~60 | ~1MB |
| factor_ontology/ | ~18 | ~100KB |
| logic_chains/ | ~30 | ~70MB |
| schema_staging/ | ~82 | ~5MB |
| cities500.txt | 1 | 38MB |
| **总计** | ~200 | ~115MB |
