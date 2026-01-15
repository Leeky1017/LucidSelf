# 命理体系

> 双体系并行：八字 + 西方占星

---

## 设计原则

### 为什么是这两个体系？

| 体系 | 覆盖用户群 | 理论成熟度 | 数据可计算性 |
|------|-----------|-----------|-------------|
| **八字** | 中国及东亚华人圈 | 千年沉淀 | ✅ 完全可编程 |
| **西方占星** | 欧美及全球化用户 | 两千年历史 | ✅ 完全可编程 |
| 紫微斗数 | 华人圈（较小众） | 成熟 | 可编程 |
| 塔罗/易经 | 小众 | 主观解读多 | 部分可编程 |

**结论**：八字 + 占星覆盖最广、最具商业价值、最易工程化。

---

## 八字体系（BaZi System）

### 核心计算模块

#### 1. 基础计算

| 模块 | 输入 | 输出 |
|------|------|------|
| 四柱计算 | 出生年月日时 | 年柱、月柱、日柱、时柱 |
| 十神推算 | 日主 + 八字 | 正官、七杀、正财、偏财、食神、伤官、比肩、劫财、正印、偏印 |
| 格局判定 | 十神配置 | 正财格、偏财格、正官格、七杀格、食神格等 |
| 五行强弱 | 八字 + 季节 | 各五行得分 |

#### 2. 动态计算

| 模块 | 更新周期 | 输出 |
|------|----------|------|
| 大运 | 每 10 年 | 当前大运干支、十神 |
| 流年 | 每年 | 流年干支与命局关系 |
| 流月 | 每月 | 流月干支（可选） |

#### 3. 因子输出

```python
class BaZiFactors:
    # 本命因子
    day_master: str              # 日主（如"甲木"）
    day_master_strength: float   # 日主强弱 0-1
    pattern: str                 # 格局（如"偏财格"）
    ten_gods: Dict[str, float]   # 十神分布权重
    
    # 五行
    elements: Dict[str, float]   # 金木水火土分布
    favorable_elements: List[str]  # 喜用神
    unfavorable_elements: List[str]  # 忌神
    
    # 动态因子
    current_dayun: DayunInfo     # 当前大运
    current_year: YearInfo       # 当前流年
    
    # 特殊结构
    special_patterns: List[str]  # 特殊格局（从格、化格等）
    clashes: List[ClashInfo]     # 冲合信息
```

---

## 西方占星体系（Astrology System）

### 核心计算模块

#### 1. 本命盘计算

| 模块 | 输入 | 输出 |
|------|------|------|
| 行星位置 | 出生时间+地点 | 10 大行星的黄道位置 |
| 宫位计算 | 出生时间+地点 | 12 宫位置（需出生时间精确） |
| 相位计算 | 行星位置 | 合相、刑、冲、拱、六合等 |
| 上升点 | 出生时间+地点 | 上升星座 |

#### 2. 动态计算（行运 Transit）

| 模块 | 更新周期 | 输出 |
|------|----------|------|
| 行运行星 | 实时 | 当前天象与本命盘的相位 |
| 太阳回归 | 每年 | 年度主题 |
| 月相 | 每月 | 新月/满月影响 |

#### 3. 因子输出

```python
class AstrologyFactors:
    # 三巨头
    sun_sign: str               # 太阳星座
    moon_sign: str              # 月亮星座
    rising_sign: str            # 上升星座
    
    # 行星落座
    planets: Dict[str, PlanetPosition]  # 行星 → 星座 + 宫位
    
    # 关键相位
    major_aspects: List[Aspect]  # 主要相位
    
    # 宫位主题
    houses: Dict[int, HouseInfo]  # 1-12宫信息
    
    # 动态因子
    current_transits: List[TransitAspect]  # 当前行运相位
    solar_return: SolarReturnChart  # 年度太阳回归盘
```

---

## 双体系融合

### 领域映射

用户的人生划分为多个领域，每个领域从两个体系各取因子：

| 领域 | 八字因子 | 占星因子 |
|------|---------|---------|
| **财富** | 财星（正财/偏财）、食伤生财 | 2宫、木星、金星相位 |
| **事业** | 官杀、印星 | 10宫、土星、太阳相位 |
| **感情** | 财星（男）/官杀（女）、桃花 | 7宫、金星、月亮相位 |
| **健康** | 日主强弱、忌神 | 6宫、火星、土星困难相位 |
| **学业** | 印星、食伤 | 9宫、水星、木星 |

### 融合策略

```python
def get_domain_factors(user_id: str, domain: str) -> DomainFactors:
    bazi = get_bazi_factors(user_id)
    astro = get_astrology_factors(user_id)
    
    # 双体系因子提取
    bazi_factors = DOMAIN_BAZI_MAPPING[domain](bazi)
    astro_factors = DOMAIN_ASTRO_MAPPING[domain](astro)
    
    # 融合分析
    return DomainFactors(
        bazi=bazi_factors,
        astro=astro_factors,
        combined_strength=combine_strength(bazi_factors, astro_factors),
        conflicts=find_conflicts(bazi_factors, astro_factors),
        reinforcements=find_reinforcements(bazi_factors, astro_factors),
    )
```

### 冲突处理

当两个体系给出矛盾信号时：

```
八字：偏财格，投资运佳
占星：土星刑木星，财务收缩

处理方式：
1. 不简单取平均
2. 在版本生成时呈现两种可能
3. LLM 叙事时解释差异来源
4. 让用户记忆层的反馈来校准哪个体系更准
```

---

## 本命数据输入要求

### 八字

| 字段 | 必需 | 说明 |
|------|------|------|
| 出生年 | ✅ | 公历年份 |
| 出生月 | ✅ | 公历月份 |
| 出生日 | ✅ | 公历日期 |
| 出生时 | ✅ | 时辰（2小时精度即可） |
| 性别 | ✅ | 影响大运顺逆 |

### 占星

| 字段 | 必需 | 说明 |
|------|------|------|
| 出生年月日 | ✅ | 公历日期 |
| 出生时间 | ⚠️ 高度建议 | 需精确到分钟（影响上升和宫位） |
| 出生地点 | ✅ | 需经纬度（影响宫位和上升） |

**注意**：如果用户不知道精确出生时间，占星部分只使用行星落座，不使用宫位系统。

---

## 技术依赖

### 八字

- 农历转换库（lunar-python 或自研）
- 节气计算
- 现有 `backend/calculators/bazi/` 可直接复用

### 占星

- 星历表（Swiss Ephemeris）
- 地理编码（经纬度转换）
- 宫位系统（Placidus 为默认）
- 现有 `backend/calculators/astrology/`（如已实现）

---

## MVP 实现范围

### Phase 1（MVP）

**八字**：
- ✅ 四柱计算
- ✅ 十神推算
- ✅ 格局判定
- ✅ 大运/流年

**占星**：
- ✅ 行星落座
- ✅ 太阳/月亮/上升
- ✅ 主要相位（合、刑、冲、拱）
- ⚠️ 宫位（仅当有精确出生时间）

### Phase 2（后续）

- 紫微斗数
- 更精细的占星技法（中点、小行星等）
