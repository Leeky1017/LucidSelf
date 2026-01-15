# Semantics 语义片段库详细结构

## 概述

语义片段库 (`backend/semantics/`) 包含从30+本命理典籍中提取的结构化语义片段，用于规则引擎匹配和叙事生成。

## 目录总览

```
semantics/
├── core/                       # 核心加载器
├── README.md                   # 语义库说明
├── .codegen_manifest.json      # 代码生成清单
│
├── # 西方占星 (~1000条目)
├── planets_in_transit/         # 行星过境 (645)
├── astrology_personality/      # 占星人格 (85)
├── tetrabiblos/                # 四书 (70)
├── the_inner_sky/              # 内在天空 (70)
├── christian_astrology/        # 基督占星 (40)
├── astrological_houses/        # 占星宫位 (29)
│
├── # 塔罗 (~280条目)
├── learning_tarot/             # 学习塔罗 (118)
├── book_of_thoth/              # 托特之书 (89)
├── pollack_tarot/              # Pollack塔罗 (54)
├── waite_tarot/                # 韦特塔罗 (22)
│
├── # 解梦 (~540条目)
├── dreams_visions_dict/        # 梦境符号词典 (229)
├── interpretation_dreams/      # 梦的解析 (64)
├── llewellyns_dreams/          # Llewellyns (21)
├── zhougong/                   # 周公解梦 (27)
├── mlxj/                       # 梦林玄解 (205)
│
├── # 心理学 (~160条目)
├── archetypes_unconscious/     # 集体无意识原型 (148)
├── collected_works/            # 荣格全集 (12)
│
├── # 八字 (~900条目)
├── sanming/                    # 三命通会 (622)
├── yuanhaiziping/              # 渊海子平 (78)
├── qiongtongbaojian/           # 穷通宝鉴 (127)
├── zipingzhenquan/             # 子平真诠 (70)
├── dts/                        # 滴天髓 (107)
│
├── # 紫微 (256条目)
├── ziwei/                      # 紫微斗数全书
│
└── # 周易 (64条目)
    └── zhouyi/                 # 周易
```

---

## 1. 核心模块 - core/

```
core/
├── __init__.py           # 模块入口
├── base.py               # 基类定义
├── loader.py             # 片段加载器
├── matcher.py            # 片段匹配器
├── registry.py           # 片段注册表
├── models.py             # 数据模型
├── utils.py              # 工具函数
└── tests/                # 测试
```

### 核心类
- `SemanticSnippet`: 语义片段基类
- `SnippetLoader`: 片段加载器
- `SnippetMatcher`: 片段匹配器
- `SnippetRegistry`: 片段注册表

---

## 2. 西方占星系列

### planets_in_transit/ (645条目)
Robert Hand《Planets in Transit》
```
planets_in_transit/
├── __init__.py
├── sun_transits/         # 太阳过境
├── moon_transits/        # 月亮过境
├── mercury_transits/     # 水星过境
├── venus_transits/       # 金星过境
├── mars_transits/        # 火星过境
├── jupiter_transits/     # 木星过境
├── saturn_transits/      # 土星过境
├── uranus_transits/      # 天王星过境
├── neptune_transits/     # 海王星过境
└── pluto_transits/       # 冥王星过境
```

### astrology_personality/ (85条目)
Dane Rudhyar《Astrology of Personality》

### the_inner_sky/ (70条目)
Steven Forrest《The Inner Sky》

### tetrabiblos/ (70条目)
Ptolemy《Tetrabiblos》

---

## 3. 塔罗系列

### learning_tarot/ (118条目)
Joan Bunning《Learning the Tarot》
```
learning_tarot/
├── __init__.py
├── major_arcana/         # 大阿卡纳 (22)
├── wands/                # 权杖 (14)
├── cups/                 # 圣杯 (14)
├── swords/               # 宝剑 (14)
└── pentacles/            # 星币 (14)
```

### book_of_thoth/ (89条目)
Aleister Crowley《The Book of Thoth》

### waite_tarot/ (22条目)
A.E. Waite《Pictorial Key to the Tarot》

---

## 4. 解梦系列

### dreams_visions_dict/ (229条目)
```
dreams_visions_dict/
├── __init__.py
├── a_symbols/            # A开头符号
├── b_symbols/            # B开头符号
├── ...
└── z_symbols/            # Z开头符号
```

### archetypes_unconscious/ (148条目)
Carl Jung《The Archetypes and the Collective Unconscious》

### mlxj/ (205条目)
《梦林玄解》

---

## 5. 八字系列

### sanming/ (622条目，最大)
《三命通会》
```
sanming/
├── __init__.py
├── heavenly_stems/       # 天干论
├── earthly_branches/     # 地支论
├── ten_gods/             # 十神论
├── combinations/         # 合化论
├── clashes/              # 冲克论
├── formats/              # 格局论
└── dayun/                # 大运论
```

### qiongtongbaojian/ (127条目)
《穷通宝鉴》- 调候用神

### yuanhaiziping/ (78条目)
《渊海子平》

### zipingzhenquan/ (70条目)
《子平真诠》

### dts/ (107条目)
《滴天髓》

---

## 6. 紫微系列

### ziwei/ (256条目)
《紫微斗数全书》
```
ziwei/
├── __init__.py
├── major_stars/          # 主星
├── auxiliary_stars/      # 辅星
├── palaces/              # 宫位
├── sihua/                # 四化
└── patterns/             # 格局
```

---

## 7. 周易系列

### zhouyi/ (64条目)
《周易》
```
zhouyi/
├── __init__.py
├── upper_canon/          # 上经 (30卦)
└── lower_canon/          # 下经 (34卦)
```

---

## 8. 片段数据结构

```python
class SemanticSnippet(BaseModel):
    id: str                    # 片段ID
    source: str                # 来源书籍
    chapter: str               # 章节
    
    # 因子条件
    factor_refs: list[str]     # 因子引用
    conditions: list[Condition]  # 触发条件
    
    # 语义内容
    original_text: str         # 原文
    interpretation: str        # 解读
    keywords: list[str]        # 关键词
    
    # 元数据
    confidence: float          # 置信度 (0-1)
    authority: int             # 权威等级 (1-5)
    domain: str                # 领域
    
    # 逻辑链
    logic_chain_ref: str       # 逻辑链引用
    evidence_refs: list[str]   # 证据引用
```

---

## 9. 统计概览

| 来源类别 | 书籍数 | 片段数 | 状态 |
|----------|--------|--------|------|
| 西方占星 | 6 | ~1000 | 完成 |
| 塔罗 | 4 | ~280 | 完成 |
| 解梦 | 5 | ~540 | 完成 |
| 心理学 | 2 | ~160 | 完成 |
| 八字 | 5 | ~900 | 完成 |
| 紫微 | 1 | 256 | 完成 |
| 周易 | 1 | 64 | 完成 |
| **总计** | **24** | **~3200** | - |

---

## 10. 代码生成

语义片段由 `scripts/codegen/semantic_generator.py` 自动生成：

```bash
# 生成所有语义模块
python -m scripts.codegen generate --type semantic

# 生成特定书籍
python -m scripts.codegen generate --type semantic --book sanming
```

生成清单记录在 `.codegen_manifest.json`
