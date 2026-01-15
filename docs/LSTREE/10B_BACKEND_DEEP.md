# 第二部分：Backend后端 - 极致细化版

> 把后端每一个模块、每一个文件的功能都解释清楚

---

# 1. backend/api/ - API层详解

## 1.1 main.py - 程序入口

**这是什么？**
整个后端程序的"大门"，程序从这里开始运行。

**代码做了什么？**
```python
# backend/api/main.py 的核心内容

from fastapi import FastAPI
from .routes import analyze, auth, dream, ...
from .middleware import auth_middleware, logging_middleware

# 1. 创建应用实例
app = FastAPI(
    title="LucidSelf API",           # 应用名称
    description="命理分析API",        # 描述
    version="1.0.0"                   # 版本
)

# 2. 注册中间件（门卫）
app.add_middleware(logging_middleware)    # 记录每个请求
app.add_middleware(auth_middleware)       # 检查登录状态

# 3. 注册路由（服务窗口）
app.include_router(analyze.router, prefix="/analyze")
app.include_router(auth.router, prefix="/auth")
app.include_router(dream.router, prefix="/dream")
# ...更多路由

# 4. 启动事件
@app.on_event("startup")
async def startup():
    # 连接数据库
    await database.connect()
    # 加载规则
    rules_engine.load_rules()
    print("服务器启动完成！")

# 5. 关闭事件
@app.on_event("shutdown")
async def shutdown():
    # 关闭数据库连接
    await database.disconnect()
    print("服务器已关闭")
```

**术语解释**：
| 术语 | 含义 | 类比 |
|------|------|------|
| `FastAPI` | Web框架 | 餐厅管理系统 |
| `app` | 应用实例 | 这家餐厅 |
| `middleware` | 中间件 | 门卫 |
| `router` | 路由 | 服务窗口 |
| `startup` | 启动事件 | 开店准备 |
| `shutdown` | 关闭事件 | 打烊收尾 |

---

## 1.2 models.py - 数据格式定义

**这是什么？**
定义API接收和返回的数据格式，像"订单模板"。

**为什么需要？**
- 验证用户输入是否正确
- 确保数据格式统一
- 自动生成API文档

**代码示例**：
```python
# backend/api/models.py

from pydantic import BaseModel, Field
from datetime import date, time
from typing import Optional

class AnalyzeRequest(BaseModel):
    """分析请求的数据格式"""
    
    birth_date: date = Field(
        ...,                              # ... 表示必填
        description="出生日期",
        example="1990-01-15"
    )
    
    birth_time: time = Field(
        ...,
        description="出生时间",
        example="08:00:00"
    )
    
    birth_place: str = Field(
        ...,
        description="出生地点",
        example="北京",
        min_length=1,                     # 最少1个字符
        max_length=100                    # 最多100个字符
    )
    
    gender: Optional[str] = Field(
        None,                             # None表示可选
        description="性别（可选）",
        example="male"
    )

class AnalyzeResponse(BaseModel):
    """分析响应的数据格式"""
    
    status: str = Field(..., example="success")
    
    bazi: dict = Field(
        ...,
        description="八字结果",
        example={"year": "甲子", "month": "丙寅", ...}
    )
    
    interpretation: str = Field(
        ...,
        description="解读文字",
        example="日主庚金，生于寅月..."
    )
```

**验证过程**：
```
用户发送：{"birth_date": "1990-01-15", ...}
           ↓
Pydantic自动验证：
  ✓ birth_date 是有效日期
  ✓ birth_time 是有效时间
  ✓ birth_place 长度在1-100之间
           ↓
验证通过 → 继续处理
验证失败 → 返回错误信息
```

---

## 1.3 routes/ - 路由目录详解

### 1.3.1 每个路由文件的作用

| 文件 | API地址 | 功能 | 详细说明 |
|------|---------|------|----------|
| `analyze.py` | `/analyze` | 综合分析 | 输入生日，返回八字+解读 |
| `auth.py` | `/auth/login`, `/auth/register` | 认证 | 用户登录、注册、登出 |
| `dream.py` | `/dream/interpret` | 解梦 | 输入梦境描述，返回解读 |
| `geocoding.py` | `/geocoding/search` | 地理编码 | 把地名转成经纬度 |
| `health.py` | `/health` | 健康检查 | 检查服务器是否正常 |
| `insights.py` | `/insights` | 洞察 | 获取个性化洞察 |
| `interpret.py` | `/interpret` | 解读 | 通用解读接口 |
| `patterns.py` | `/patterns` | 模式识别 | 识别命盘中的格局 |
| `playbook.py` | `/playbook` | 行动手册 | 生成每日/周/月建议 |
| `scheduler.py` | `/scheduler` | 调度器 | 定时任务管理 |
| `subscription.py` | `/subscription` | 订阅 | 会员订阅管理 |
| `timeline.py` | `/timeline` | 时间线 | 过去和未来的重要时间点 |
| `todo.py` | `/todo` | 待办 | 行动建议待办事项 |
| `user.py` | `/user` | 用户 | 用户信息管理 |
| `versions.py` | `/versions` | 版本 | 命盘版本历史 |

### 1.3.2 一个路由文件的完整解析

```python
# backend/api/routes/analyze.py 完整解析

from fastapi import APIRouter, Depends, HTTPException
from ..models import AnalyzeRequest, AnalyzeResponse
from ...calculators.bazi import BaziCalculator
from ...services.narrative import NarrativeService
from ...core.geocoding import GeocodingService

# 创建路由器
router = APIRouter(
    prefix="/analyze",          # 所有路由都以 /analyze 开头
    tags=["分析"]               # API文档中的分组
)

# 依赖项：获取各种服务
def get_bazi_calculator():
    return BaziCalculator()

def get_narrative_service():
    return NarrativeService()

# 定义API接口
@router.post(
    "/",                                    # 完整地址: POST /analyze/
    response_model=AnalyzeResponse,         # 返回数据格式
    summary="综合命盘分析",                  # API文档标题
    description="输入出生信息，返回八字分析"  # API文档描述
)
async def analyze(
    request: AnalyzeRequest,                           # 请求数据
    bazi_calc: BaziCalculator = Depends(get_bazi_calculator),     # 注入计算器
    narrative: NarrativeService = Depends(get_narrative_service)  # 注入叙事服务
):
    """
    综合命盘分析接口
    
    处理步骤：
    1. 验证请求数据
    2. 地名转经纬度
    3. 计算八字
    4. 生成解读
    5. 返回结果
    """
    try:
        # 步骤1: 数据已经被Pydantic自动验证
        
        # 步骤2: 获取经纬度（占星需要）
        location = await GeocodingService().geocode(request.birth_place)
        
        # 步骤3: 计算八字
        bazi_result = bazi_calc.calculate(
            birth_date=request.birth_date,
            birth_time=request.birth_time,
            location=location
        )
        
        # 步骤4: 生成解读
        interpretation = await narrative.generate(bazi_result)
        
        # 步骤5: 返回结果
        return AnalyzeResponse(
            status="success",
            bazi=bazi_result.to_dict(),
            interpretation=interpretation
        )
        
    except ValueError as e:
        # 输入错误
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # 服务器错误
        raise HTTPException(status_code=500, detail="服务器内部错误")
```

**代码注解**：
| 代码 | 作用 |
|------|------|
| `@router.post("/")` | 装饰器，定义这是一个POST接口 |
| `async def` | 异步函数，可以同时处理多个请求 |
| `Depends(...)` | 依赖注入，自动创建需要的对象 |
| `HTTPException` | 返回错误给客户端 |
| `status_code=400` | HTTP状态码，400=客户端错误 |
| `status_code=500` | 500=服务器错误 |

---

## 1.4 middleware/ - 中间件详解

**什么是中间件？**
每个请求都要经过的"检查站"。

```
请求进来
    ↓
┌─────────────────────────────────────────┐
│  中间件1：日志记录                        │
│  记录：谁在什么时候请求了什么              │
└────────────────────┬────────────────────┘
                     ↓
┌─────────────────────────────────────────┐
│  中间件2：认证检查                        │
│  检查：用户是否登录                       │
└────────────────────┬────────────────────┘
                     ↓
┌─────────────────────────────────────────┐
│  中间件3：限流保护                        │
│  检查：请求频率是否过高                   │
└────────────────────┬────────────────────┘
                     ↓
              路由处理请求
                     ↓
              原路返回响应
```

**中间件代码示例**：
```python
# backend/api/middleware/logging.py

import time
import logging

async def logging_middleware(request, call_next):
    """记录每个请求的日志"""
    
    # 请求开始时间
    start_time = time.time()
    
    # 记录请求信息
    logging.info(f"请求开始: {request.method} {request.url}")
    
    # 继续处理请求（调用下一个中间件或路由）
    response = await call_next(request)
    
    # 计算处理时间
    process_time = time.time() - start_time
    
    # 记录响应信息
    logging.info(f"请求完成: 状态码={response.status_code}, 耗时={process_time:.3f}秒")
    
    return response
```

---

# 2. backend/calculators/ - 计算器详解

## 2.1 整体架构

```
calculators/
├── __init__.py          # 入口，注册所有计算器
├── bazi/                # 八字计算器
├── astro/               # 西方占星计算器
├── ziwei/               # 紫微斗数计算器
├── dream/               # 解梦分析器
├── tarot/               # 塔罗解读器
└── yijing/              # 周易起卦器
```

**每个计算器的职责**：
```
输入：用户信息（生日、时间、地点等）
  ↓
处理：执行特定系统的计算逻辑
  ↓
输出：结构化的计算结果
```

---

## 2.2 bazi/ - 八字计算器详解

### 2.2.1 文件结构

| 文件 | 职责 | 类比 |
|------|------|------|
| `calculator.py` | 主计算逻辑 | 主厨 |
| `models.py` | 数据结构定义 | 菜品规格 |
| `service.py` | 对外服务接口 | 上菜员 |
| `dayun.py` | 大运计算 | 帮厨1 |
| `hidden_stems.py` | 藏干计算 | 帮厨2 |
| `solar_terms.py` | 节气判断 | 参考资料 |
| `ten_gods.py` | 十神计算 | 帮厨3 |

### 2.2.2 calculator.py 详解

```python
# backend/calculators/bazi/calculator.py

class BaziCalculator:
    """八字计算器 - 排八字的核心逻辑"""
    
    # 天干（10个）
    STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    
    # 地支（12个）
    BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", 
                "午", "未", "申", "酉", "戌", "亥"]
    
    def calculate(self, birth_datetime, location=None):
        """
        计算八字
        
        参数：
            birth_datetime: 出生日期时间
            location: 出生地点（用于真太阳时校正）
            
        返回：
            BaziResult: 包含四柱的完整八字
        """
        # 1. 校正真太阳时（不同地区时间有差异）
        true_solar_time = self._correct_solar_time(birth_datetime, location)
        
        # 2. 计算年柱
        year_pillar = self._calculate_year_pillar(true_solar_time)
        
        # 3. 计算月柱
        month_pillar = self._calculate_month_pillar(true_solar_time)
        
        # 4. 计算日柱
        day_pillar = self._calculate_day_pillar(true_solar_time)
        
        # 5. 计算时柱
        hour_pillar = self._calculate_hour_pillar(true_solar_time, day_pillar)
        
        # 6. 组装结果
        return BaziResult(
            year=year_pillar,
            month=month_pillar,
            day=day_pillar,
            hour=hour_pillar
        )
    
    def _calculate_year_pillar(self, dt):
        """
        计算年柱
        
        算法：
        1. 判断是否过了立春（年柱以立春为界）
        2. 用年份计算天干：(年份 - 4) % 10
        3. 用年份计算地支：(年份 - 4) % 12
        """
        year = dt.year
        
        # 检查是否过了立春
        lichun = self._get_lichun_date(year)
        if dt < lichun:
            year -= 1  # 未过立春，用上一年
        
        # 计算天干
        stem_index = (year - 4) % 10
        stem = self.STEMS[stem_index]
        
        # 计算地支
        branch_index = (year - 4) % 12
        branch = self.BRANCHES[branch_index]
        
        return Pillar(stem=stem, branch=branch)
```

### 2.2.3 八字计算完整流程

```
输入：1990年1月15日 早上8点 北京

┌──────────────────────────────────────────────────────────┐
│ 步骤1：真太阳时校正                                       │
├──────────────────────────────────────────────────────────┤
│ 北京时间8:00 → 真太阳时约8:14                             │
│ （因为北京经度116.4°，与东八区标准120°有差异）            │
└────────────────────┬─────────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────────┐
│ 步骤2：计算年柱                                           │
├──────────────────────────────────────────────────────────┤
│ 1990年1月15日 < 1990年立春（2月4日）                      │
│ 所以用1989年计算                                          │
│ (1989-4) % 10 = 5 → 己                                   │
│ (1989-4) % 12 = 5 → 巳                                   │
│ 年柱 = 己巳                                               │
└────────────────────┬─────────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────────┐
│ 步骤3：计算月柱                                           │
├──────────────────────────────────────────────────────────┤
│ 1月15日在小寒(1/6)之后，大寒(1/20)之前                    │
│ 属于丑月                                                  │
│ 查表得月干：丁丑                                          │
│ 月柱 = 丁丑                                               │
└────────────────────┬─────────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────────┐
│ 步骤4：计算日柱                                           │
├──────────────────────────────────────────────────────────┤
│ 使用日柱算法（基于儒略日）                                 │
│ 1990年1月15日 = 甲子日                                    │
│ 日柱 = 甲子                                               │
└────────────────────┬─────────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────────┐
│ 步骤5：计算时柱                                           │
├──────────────────────────────────────────────────────────┤
│ 8:14 属于辰时 (7:00-9:00)                                │
│ 根据日干甲，查表得时干：戊辰                               │
│ 时柱 = 戊辰                                               │
└────────────────────┬─────────────────────────────────────┘
                     ↓
输出：己巳 丁丑 甲子 戊辰
```

### 2.2.4 models.py 数据结构

```python
# backend/calculators/bazi/models.py

from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class Stem(str, Enum):
    """天干枚举"""
    JIA = "甲"    # 阳木
    YI = "乙"     # 阴木
    BING = "丙"   # 阳火
    DING = "丁"   # 阴火
    WU = "戊"     # 阳土
    JI = "己"     # 阴土
    GENG = "庚"   # 阳金
    XIN = "辛"    # 阴金
    REN = "壬"    # 阳水
    GUI = "癸"    # 阴水

class Branch(str, Enum):
    """地支枚举"""
    ZI = "子"     # 子时 23:00-01:00，属水
    CHOU = "丑"   # 丑时 01:00-03:00，属土
    YIN = "寅"    # 寅时 03:00-05:00，属木
    MAO = "卯"    # 卯时 05:00-07:00，属木
    CHEN = "辰"   # 辰时 07:00-09:00，属土
    SI = "巳"     # 巳时 09:00-11:00，属火
    WU = "午"     # 午时 11:00-13:00，属火
    WEI = "未"    # 未时 13:00-15:00，属土
    SHEN = "申"   # 申时 15:00-17:00，属金
    YOU = "酉"    # 酉时 17:00-19:00，属金
    XU = "戌"     # 戌时 19:00-21:00，属土
    HAI = "亥"    # 亥时 21:00-23:00，属水

class Pillar(BaseModel):
    """柱（一对天干地支）"""
    stem: Stem          # 天干
    branch: Branch      # 地支
    
    @property
    def full_name(self) -> str:
        """完整名称，如'甲子'"""
        return f"{self.stem.value}{self.branch.value}"
    
    @property
    def element(self) -> str:
        """天干五行"""
        element_map = {
            "甲": "木", "乙": "木",
            "丙": "火", "丁": "火",
            "戊": "土", "己": "土",
            "庚": "金", "辛": "金",
            "壬": "水", "癸": "水"
        }
        return element_map[self.stem.value]

class BaziResult(BaseModel):
    """八字计算结果"""
    year: Pillar        # 年柱
    month: Pillar       # 月柱
    day: Pillar         # 日柱（日主）
    hour: Pillar        # 时柱
    
    # 额外信息
    ten_gods: Optional[List[str]] = None      # 十神
    hidden_stems: Optional[dict] = None       # 藏干
    dayun: Optional[List[dict]] = None        # 大运
    
    @property
    def day_master(self) -> str:
        """日主（日干）"""
        return self.day.stem.value
    
    def to_string(self) -> str:
        """转为字符串格式"""
        return f"{self.year.full_name} {self.month.full_name} {self.day.full_name} {self.hour.full_name}"
```

---

## 2.3 astro/ - 西方占星计算器详解

### 2.3.1 文件结构

| 文件 | 职责 | 说明 |
|------|------|------|
| `calculator.py` | 星盘计算 | 计算行星位置、宫位、相位 |
| `models.py` | 数据结构 | 行星、星座、宫位等模型 |
| `service.py` | 服务接口 | 对外提供服务 |

### 2.3.2 占星计算需要什么

```
【必需输入】
1. 出生日期：1990-01-15
2. 出生时间：08:00:00
3. 出生地点经度：116.4°E（北京）
4. 出生地点纬度：39.9°N（北京）

【为什么需要经纬度？】
- 星盘中的"宫位"与地理位置相关
- 上升点（ASC）随出生地变化
- 不同地点同一时刻看到的天空不同
```

### 2.3.3 星盘计算流程

```
┌──────────────────────────────────────────────────────────┐
│ 步骤1：获取精确时间                                       │
├──────────────────────────────────────────────────────────┤
│ 将本地时间转换为UTC时间                                   │
│ 1990-01-15 08:00 CST → 1990-01-15 00:00 UTC              │
└────────────────────┬─────────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────────┐
│ 步骤2：计算行星位置                                       │
├──────────────────────────────────────────────────────────┤
│ 使用天文历表计算每颗行星在黄道上的位置                     │
│ 太阳：摩羯座 24°15'                                       │
│ 月亮：双鱼座 12°30'                                       │
│ 水星：水瓶座 05°45'                                       │
│ ...（10颗主要星体）                                       │
└────────────────────┬─────────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────────┐
│ 步骤3：计算宫位                                           │
├──────────────────────────────────────────────────────────┤
│ 根据出生地经纬度计算12宫位置                               │
│ 第1宫（上升）：天蝎座 15°                                  │
│ 第2宫：射手座 12°                                         │
│ ...（12个宫位）                                           │
└────────────────────┬─────────────────────────────────────┘
                     ↓
┌──────────────────────────────────────────────────────────┐
│ 步骤4：计算相位                                           │
├──────────────────────────────────────────────────────────┤
│ 检查行星之间的角度关系                                    │
│ 太阳-月亮：六分相（60°）→ 和谐                            │
│ 火星-土星：四分相（90°）→ 紧张                            │
│ ...                                                      │
└────────────────────┬─────────────────────────────────────┘
                     ↓
输出：完整星盘数据
```

---

## 2.4 其他计算器概述

### 2.4.1 ziwei/ - 紫微斗数

```
【核心概念】
- 12宫位：命宫、兄弟宫、夫妻宫...
- 主星：紫微、天机、太阳、武曲...
- 辅星：文昌、文曲、左辅、右弼...
- 四化：化禄、化权、化科、化忌

【计算流程】
农历生日 → 定命宫位置 → 安主星 → 安辅星 → 四化飞入
```

### 2.4.2 dream/ - 解梦

```
【核心概念】
- 不是"计算"，而是"分析"
- 从梦境描述中提取关键元素
- 匹配符号库中的解释

【处理流程】
梦境描述 → NLP分词 → 提取符号 → 查询语义库 → 生成解读
```

### 2.4.3 tarot/ - 塔罗

```
【核心概念】
- 78张牌（22大阿卡纳 + 56小阿卡纳）
- 牌阵位置
- 正位/逆位

【处理流程】
抽牌结果 → 获取牌义 → 结合位置解读 → 综合分析
```

### 2.4.4 yijing/ - 周易

```
【核心概念】
- 64卦
- 6爻
- 变卦

【计算流程】
起卦方式 → 得到本卦 → 判断变爻 → 得到变卦 → 取卦辞爻辞
```

---

# 3. backend/core/ - 核心基础设施详解

## 3.1 contracts/ - 数据契约

**什么是数据契约？**
所有模块之间传递数据的"标准格式"，确保大家说的是同一种语言。

### 3.1.1 为什么需要统一契约

```
【没有契约的世界】

八字模块说：birth_date = "1990/01/15"
占星模块说：birthDate = "15-01-1990"
前端说：birth_date = "1990-01-15T00:00:00Z"

→ 混乱！每次传数据都要转换

【有契约的世界】

所有模块都遵守 unified_time.py 的定义：
birth_date = date(1990, 1, 15)

→ 统一！无需转换
```

### 3.1.2 核心契约文件

| 文件 | 定义什么 | 使用场景 |
|------|----------|----------|
| `base.py` | 基础模型 | 所有模型的父类 |
| `unified_time.py` | 时间格式 | 公历、农历、节气统一表示 |
| `unified_dimensions.py` | 维度映射 | 不同系统概念的对应关系 |
| `action_models.py` | 行动建议 | Playbook中的建议格式 |
| `narrative_models.py` | 叙事文本 | 生成的解读文本格式 |
| `engine_models.py` | 引擎结果 | 各计算器的输出格式 |

### 3.1.3 unified_time.py 详解

```python
# backend/core/contracts/unified_time.py

class UnifiedTime(BaseModel):
    """
    统一时间表示
    
    为什么需要？
    - 八字用农历
    - 占星用公历
    - 需要节气判断
    - 需要时区信息
    
    这个类把所有时间信息统一在一起
    """
    
    # 公历时间
    gregorian: datetime           # 2024-01-15 08:00:00
    
    # 农历时间
    lunar_year: int               # 农历年，如2023
    lunar_month: int              # 农历月，1-12
    lunar_day: int                # 农历日，1-30
    is_leap_month: bool = False   # 是否闰月
    
    # 节气信息
    solar_term: Optional[str] = None     # 当天节气，如"小寒"
    prev_solar_term: str                  # 前一个节气
    next_solar_term: str                  # 下一个节气
    days_to_next_term: int                # 距下一节气天数
    
    # 干支时间
    year_stem_branch: str                 # 年干支，如"甲子"
    month_stem_branch: str                # 月干支
    day_stem_branch: str                  # 日干支
    hour_stem_branch: str                 # 时干支
    
    # 时区信息
    timezone: str = "Asia/Shanghai"       # 时区
    utc_offset: int = 8                   # UTC偏移小时数
    
    @classmethod
    def from_datetime(cls, dt: datetime, location: str = None):
        """从datetime创建统一时间"""
        # 计算农历
        lunar = LunarCalendar.from_gregorian(dt)
        # 计算干支
        ganzhi = GanzhiCalculator.calculate(dt)
        # 计算节气
        terms = SolarTerms.get_terms(dt)
        # 组装
        return cls(
            gregorian=dt,
            lunar_year=lunar.year,
            lunar_month=lunar.month,
            lunar_day=lunar.day,
            ...
        )
```

---

## 3.2 llm/ - 大语言模型调用

### 3.2.1 整体架构

```
用户请求生成解读
        ↓
┌─────────────────────────────────────────────────────────┐
│                    LLM模块                               │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   orchestrator.py ─────────→ 编排复杂任务                │
│         ↓                                               │
│   router.py ───────────────→ 选择用哪个AI              │
│         ↓                                               │
│   client.py ───────────────→ 发送请求                  │
│         ↓                                               │
│   providers/ ──────────────→ 具体AI接口                │
│     ├── openai.py                                       │
│     ├── deepseek.py                                     │
│     └── anthropic.py                                    │
│         ↓                                               │
│   cost_monitor.py ─────────→ 记录成本                  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 3.2.2 router.py - AI选择策略

```python
# backend/core/llm/router.py

class LLMRouter:
    """
    AI路由器 - 决定用哪个AI模型
    
    选择依据：
    1. 任务复杂度
    2. 成本预算
    3. 响应速度
    4. 可用性
    """
    
    # 模型配置
    MODELS = {
        "simple": {
            "provider": "deepseek",
            "model": "deepseek-chat",
            "cost_per_1k": 0.001,        # 每千token成本
            "speed": "fast",
            "use_for": ["简单问答", "格式化"]
        },
        "medium": {
            "provider": "deepseek",
            "model": "deepseek-reasoner",
            "cost_per_1k": 0.01,
            "speed": "medium",
            "use_for": ["命理解读", "分析"]
        },
        "complex": {
            "provider": "anthropic",
            "model": "claude-3-opus",
            "cost_per_1k": 0.05,
            "speed": "slow",
            "use_for": ["复杂推理", "创意写作"]
        }
    }
    
    def select_model(self, task_type: str, budget: float = None):
        """
        选择合适的模型
        
        参数：
            task_type: 任务类型
            budget: 预算（可选）
        """
        if task_type in ["简单问答", "格式化"]:
            return self.MODELS["simple"]
        elif task_type in ["命理解读", "分析"]:
            return self.MODELS["medium"]
        else:
            return self.MODELS["complex"]
```

### 3.2.3 cost_monitor.py - 成本监控

```python
# backend/core/llm/cost_monitor.py

class CostMonitor:
    """
    AI成本监控
    
    为什么重要？
    - AI调用按token收费
    - 没有监控可能超支
    - 需要优化成本
    """
    
    def record_call(self, 
                    model: str,
                    input_tokens: int,
                    output_tokens: int,
                    user_id: str = None):
        """记录一次AI调用"""
        
        # 计算成本
        cost = self._calculate_cost(model, input_tokens, output_tokens)
        
        # 存入数据库
        self.db.insert({
            "timestamp": datetime.now(),
            "model": model,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": cost,
            "user_id": user_id
        })
        
        # 检查是否超预算
        if self._is_over_budget(user_id):
            raise BudgetExceededError("已超出预算限制")
        
        return cost
    
    def get_daily_cost(self, date: date = None):
        """获取某日总成本"""
        ...
    
    def get_user_cost(self, user_id: str, period: str = "month"):
        """获取用户某周期成本"""
        ...
```

---

## 3.3 geocoding/ - 地理编码服务

### 3.3.1 为什么需要地理编码

```
【问题】
用户输入：出生地 = "北京"
占星计算需要：经度 = 116.4°, 纬度 = 39.9°

【解决方案】
地理编码服务：把地名转成经纬度

"北京" → {lat: 39.9042, lng: 116.4074}
"上海" → {lat: 31.2304, lng: 121.4737}
"纽约" → {lat: 40.7128, lng: -74.0060}
```

### 3.3.2 服务架构

```python
# backend/core/geocoding/service.py

class GeocodingService:
    """地理编码服务"""
    
    def __init__(self):
        # 多个供应商，按优先级尝试
        self.providers = [
            GoogleGeocodingProvider(),
            BaiduGeocodingProvider(),
            NominatimProvider()          # 免费备选
        ]
        # 缓存
        self.cache = RedisCache()
        # 数据库
        self.repository = GeocodingRepository()
    
    async def geocode(self, place_name: str) -> Location:
        """
        将地名转换为经纬度
        
        查找顺序：
        1. 缓存（最快）
        2. 数据库（已查过的）
        3. 在线API（最慢但最全）
        """
        # 1. 查缓存
        cached = self.cache.get(f"geo:{place_name}")
        if cached:
            return Location.from_dict(cached)
        
        # 2. 查数据库
        db_result = await self.repository.find(place_name)
        if db_result:
            self.cache.set(f"geo:{place_name}", db_result.to_dict())
            return db_result
        
        # 3. 调用API
        for provider in self.providers:
            try:
                result = await provider.geocode(place_name)
                if result:
                    # 保存到数据库和缓存
                    await self.repository.save(place_name, result)
                    self.cache.set(f"geo:{place_name}", result.to_dict())
                    return result
            except Exception:
                continue  # 尝试下一个供应商
        
        raise GeocodingError(f"无法找到地点：{place_name}")
```
