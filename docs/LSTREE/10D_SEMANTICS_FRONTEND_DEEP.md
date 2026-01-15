# 第四部分：语义库与前端 - 极致细化版

---

# 1. backend/semantics/ - 语义片段库详解

## 1.1 什么是语义片段？

**最简单的理解**：
语义片段 = 从古籍中提取的一条命理规则 + 解读

```
【原始典籍文字】
《三命通会》卷二：
"甲木生于子月，水旺木相，得生扶之力，
若八字中有火暖局，则木得水生而不寒，
主人聪明伶俐，学业有成..."

【提取后的语义片段】
{
  id: "sanming_jia_zi_001",
  factors: ["甲木", "子月", "水旺"],
  conditions: ["日干=甲", "月支=子"],
  interpretation: "甲木生于子月，水旺木相...",
  keywords: ["聪明", "学业"],
  confidence: 0.85
}
```

## 1.2 语义库的结构

```
semantics/
├── core/                      # 核心模块
│   ├── __init__.py
│   ├── base.py               # 语义片段基类
│   ├── loader.py             # 加载器
│   ├── matcher.py            # 匹配器
│   ├── registry.py           # 注册表
│   └── models.py             # 数据模型
│
├── # 八字相关（约1000条）
├── sanming/                   # 三命通会（622条）
├── yuanhaiziping/             # 渊海子平（78条）
├── qiongtongbaojian/          # 穷通宝鉴（127条）
├── zipingzhenquan/            # 子平真诠（70条）
├── dts/                       # 滴天髓（107条）
│
├── # 占星相关（约1000条）
├── planets_in_transit/        # 行星过境（645条）
├── astrology_personality/     # 占星人格（85条）
├── the_inner_sky/             # 内在天空（70条）
├── tetrabiblos/               # 四书（70条）
├── christian_astrology/       # 基督占星（40条）
├── astrological_houses/       # 占星宫位（29条）
│
├── # 塔罗相关（约280条）
├── learning_tarot/            # 学习塔罗（118条）
├── book_of_thoth/             # 托特之书（89条）
├── pollack_tarot/             # Pollack塔罗（54条）
├── waite_tarot/               # 韦特塔罗（22条）
│
├── # 解梦相关（约540条）
├── dreams_visions_dict/       # 梦境符号词典（229条）
├── interpretation_dreams/     # 梦的解析（64条）
├── zhougong/                  # 周公解梦（27条）
├── mlxj/                      # 梦林玄解（205条）
│
├── # 心理学相关（约160条）
├── archetypes_unconscious/    # 集体无意识原型（148条）
├── collected_works/           # 荣格全集（12条）
│
├── # 紫微相关（256条）
├── ziwei/                     # 紫微斗数全书
│
└── # 周易相关（64条）
    └── zhouyi/                # 周易
```

## 1.3 core/base.py - 语义片段基类

```python
# backend/semantics/core/base.py

from pydantic import BaseModel
from typing import List, Optional, Dict
from enum import Enum

class SnippetSource(str, Enum):
    """片段来源类型"""
    CHINESE_CLASSIC = "chinese_classic"    # 中国经典
    WESTERN_ASTRO = "western_astro"        # 西方占星
    TAROT = "tarot"                        # 塔罗
    DREAM = "dream"                        # 解梦
    PSYCHOLOGY = "psychology"              # 心理学
    YIJING = "yijing"                      # 周易

class SemanticSnippet(BaseModel):
    """
    语义片段基类
    
    这是从典籍中提取的最小知识单元
    """
    
    # === 标识信息 ===
    id: str                           # 唯一ID，如 "sanming_001"
    source_book: str                  # 来源书籍，如 "三命通会"
    source_chapter: str               # 来源章节，如 "卷二·论天干"
    source_type: SnippetSource        # 来源类型
    
    # === 触发条件 ===
    factor_refs: List[str]            # 因子引用，如 ["甲木", "子水"]
    conditions: List[Dict]            # 详细条件
    # 条件示例：
    # [
    #   {"type": "day_stem", "value": "甲", "operator": "equals"},
    #   {"type": "month_branch", "value": "子", "operator": "equals"}
    # ]
    
    # === 内容 ===
    original_text: str                # 原文
    interpretation: str               # 解读/白话翻译
    keywords: List[str]               # 关键词
    
    # === 元数据 ===
    confidence: float                 # 置信度 0-1
    authority: int                    # 权威等级 1-5
    dimension: str                    # 所属维度（性格/事业/感情...）
    sentiment: str                    # 情感倾向（正面/负面/中性）
    
    # === 关联信息 ===
    related_snippets: List[str] = []  # 相关片段ID
    conflicts_with: List[str] = []    # 冲突片段ID
    logic_chain_ref: Optional[str]    # 逻辑链引用
    
    # === 使用统计 ===
    usage_count: int = 0              # 使用次数
    feedback_score: float = 0.0       # 用户反馈评分
    
    def matches(self, input_data: dict) -> bool:
        """
        检查是否匹配输入数据
        """
        for condition in self.conditions:
            if not self._check_condition(condition, input_data):
                return False
        return True
    
    def _check_condition(self, condition: dict, data: dict) -> bool:
        """检查单个条件"""
        # 获取实际值
        actual = self._get_value(data, condition["type"])
        expected = condition["value"]
        operator = condition.get("operator", "equals")
        
        if operator == "equals":
            return actual == expected
        elif operator == "in":
            return actual in expected
        elif operator == "contains":
            return expected in str(actual)
        # ... 更多操作符
        return False
```

## 1.4 一个具体的语义模块详解

### 1.4.1 sanming/ - 三命通会模块

```
sanming/
├── __init__.py                    # 模块入口
├── heavenly_stems/                # 天干相关片段
│   ├── __init__.py
│   ├── jia.py                     # 甲木相关（约50条）
│   ├── yi.py                      # 乙木相关
│   ├── bing.py                    # 丙火相关
│   └── ...                        # 其他天干
├── earthly_branches/              # 地支相关片段
│   ├── __init__.py
│   ├── zi.py                      # 子水相关
│   └── ...                        # 其他地支
├── ten_gods/                      # 十神相关片段
│   ├── __init__.py
│   ├── bijian.py                  # 比肩相关
│   ├── jiecai.py                  # 劫财相关
│   └── ...                        # 其他十神
├── combinations/                  # 合化相关片段
│   ├── stems_combination.py       # 天干合
│   └── branches_combination.py    # 地支合
└── special_patterns/              # 特殊格局
    ├── cong_patterns.py           # 从格
    └── hua_patterns.py            # 化格
```

### 1.4.2 一个具体的片段文件

```python
# backend/semantics/sanming/heavenly_stems/jia.py

"""
三命通会 - 甲木相关语义片段

本模块包含《三命通会》中关于甲木日主的所有解读
"""

from ..core.base import SemanticSnippet, SnippetSource

# 片段列表
SNIPPETS = [
    
    SemanticSnippet(
        id="sanming_jia_001",
        source_book="三命通会",
        source_chapter="卷二·论天干·甲木",
        source_type=SnippetSource.CHINESE_CLASSIC,
        
        factor_refs=["甲木", "日主"],
        conditions=[
            {"type": "day_stem", "value": "甲", "operator": "equals"}
        ],
        
        original_text="""
甲木为阳木，参天之木，森林之象。
其性刚直，不屈不挠，喜阳光雨露。
""",
        
        interpretation="""
甲木日主的人，性格正直刚强，有主见，不轻易妥协。
就像参天大树一样，有向上生长的强烈愿望。
喜欢阳光（丙火）的温暖和雨露（壬癸水）的滋润。
""",
        
        keywords=["刚直", "主见", "不屈", "向上"],
        confidence=0.9,
        authority=5,  # 三命通会是最权威的八字典籍
        dimension="性格",
        sentiment="中性",
        
        related_snippets=["sanming_jia_002", "yuanhai_jia_001"],
        logic_chain_ref="sanming_lc_jia_001"
    ),
    
    SemanticSnippet(
        id="sanming_jia_zi_001",
        source_book="三命通会",
        source_chapter="卷二·论天干·甲木生于子月",
        source_type=SnippetSource.CHINESE_CLASSIC,
        
        factor_refs=["甲木", "子月", "水旺"],
        conditions=[
            {"type": "day_stem", "value": "甲", "operator": "equals"},
            {"type": "month_branch", "value": "子", "operator": "equals"}
        ],
        
        original_text="""
甲木生于子月，水旺木相，得生扶之力。
若八字中有火暖局，则木得水生而不寒。
无火则木漂，虽有才华而难以施展。
""",
        
        interpretation="""
甲木在子月（冬季农历十一月）出生，此时水气最旺。
水生木，对甲木有生扶作用，但也可能太冷。

如果八字中有丙火或丁火，就能温暖整个命局，
这样的人聪明有才华，而且能够发挥出来。

如果八字中没有火，虽然也有才能，但容易怀才不遇，
性格可能偏内向或有些清高。
""",
        
        keywords=["水旺木相", "需要火暖", "聪明", "才华"],
        confidence=0.85,
        authority=5,
        dimension="性格",
        sentiment="中性",
        
        related_snippets=["qiongtong_jia_zi_001"],
        conflicts_with=[]
    ),
    
    # ... 更多片段
]

def get_all_snippets():
    """获取本模块所有片段"""
    return SNIPPETS

def get_snippet_by_id(snippet_id: str):
    """根据ID获取片段"""
    for snippet in SNIPPETS:
        if snippet.id == snippet_id:
            return snippet
    return None

def match_snippets(input_data: dict):
    """匹配输入数据的片段"""
    matched = []
    for snippet in SNIPPETS:
        if snippet.matches(input_data):
            matched.append(snippet)
    return matched
```

## 1.5 core/loader.py - 加载器详解

```python
# backend/semantics/core/loader.py

import importlib
from pathlib import Path
from typing import List, Dict
from .base import SemanticSnippet

class SnippetLoader:
    """
    语义片段加载器
    
    职责：
    1. 扫描semantics目录下所有模块
    2. 动态导入各模块
    3. 收集所有片段
    4. 构建索引
    """
    
    def __init__(self):
        self.snippets: Dict[str, SemanticSnippet] = {}  # id -> snippet
        self.index: Dict[str, List[str]] = {}           # factor -> snippet_ids
        self.loaded = False
    
    def load_all(self):
        """加载所有语义片段"""
        if self.loaded:
            return
        
        semantics_dir = Path(__file__).parent.parent
        
        # 遍历所有子目录（每个书籍一个目录）
        for book_dir in semantics_dir.iterdir():
            if book_dir.is_dir() and not book_dir.name.startswith("_"):
                if book_dir.name == "core":
                    continue  # 跳过core目录
                self._load_book(book_dir)
        
        self._build_index()
        self.loaded = True
        print(f"已加载 {len(self.snippets)} 条语义片段")
    
    def _load_book(self, book_dir: Path):
        """加载一本书的所有片段"""
        # 导入书籍模块
        module_name = f"backend.semantics.{book_dir.name}"
        try:
            book_module = importlib.import_module(module_name)
            
            # 尝试调用 get_all_snippets()
            if hasattr(book_module, "get_all_snippets"):
                snippets = book_module.get_all_snippets()
                for snippet in snippets:
                    self.snippets[snippet.id] = snippet
            
            # 递归加载子模块
            for sub_dir in book_dir.iterdir():
                if sub_dir.is_dir() and not sub_dir.name.startswith("_"):
                    self._load_submodule(book_dir.name, sub_dir)
                    
        except ImportError as e:
            print(f"警告：无法加载模块 {module_name}: {e}")
    
    def _build_index(self):
        """
        构建因子索引
        
        索引结构：
        {
            "甲木": ["sanming_jia_001", "sanming_jia_002", ...],
            "子水": ["sanming_jia_zi_001", ...],
            ...
        }
        
        这样查询时可以快速找到相关片段
        """
        for snippet_id, snippet in self.snippets.items():
            for factor in snippet.factor_refs:
                if factor not in self.index:
                    self.index[factor] = []
                self.index[factor].append(snippet_id)
    
    def get_by_factors(self, factors: List[str]) -> List[SemanticSnippet]:
        """
        根据因子获取相关片段
        
        参数：
            factors: 因子列表，如 ["甲木", "子水"]
            
        返回：
            包含这些因子的片段列表
        """
        if not self.loaded:
            self.load_all()
        
        # 找到所有包含任一因子的片段ID
        candidate_ids = set()
        for factor in factors:
            if factor in self.index:
                candidate_ids.update(self.index[factor])
        
        # 获取片段对象
        return [self.snippets[sid] for sid in candidate_ids]
```

## 1.6 core/matcher.py - 匹配器详解

```python
# backend/semantics/core/matcher.py

from typing import List, Tuple
from .base import SemanticSnippet
from .loader import SnippetLoader

class SnippetMatcher:
    """
    语义片段匹配器
    
    根据用户的命盘数据，找到匹配的语义片段
    """
    
    def __init__(self):
        self.loader = SnippetLoader()
    
    def match(self, 
              input_data: dict,
              scenario: str = None,
              max_results: int = 20) -> List[Tuple[SemanticSnippet, float]]:
        """
        匹配语义片段
        
        参数：
            input_data: 命盘数据
                {
                    "bazi": {...},
                    "astro": {...},
                    "factors": ["甲木", "子水", ...]
                }
            scenario: 场景过滤（可选）
            max_results: 最大返回数量
            
        返回：
            [(片段, 匹配分数), ...] 按分数降序
        """
        # 确保已加载
        self.loader.load_all()
        
        # 1. 从因子获取候选片段
        factors = input_data.get("factors", [])
        candidates = self.loader.get_by_factors(factors)
        
        # 2. 详细匹配每个候选
        matches = []
        for snippet in candidates:
            if snippet.matches(input_data):
                score = self._calculate_score(snippet, input_data)
                matches.append((snippet, score))
        
        # 3. 场景过滤
        if scenario:
            matches = [(s, score) for s, score in matches 
                      if self._matches_scenario(s, scenario)]
        
        # 4. 按分数排序
        matches.sort(key=lambda x: x[1], reverse=True)
        
        # 5. 限制数量
        return matches[:max_results]
    
    def _calculate_score(self, 
                         snippet: SemanticSnippet, 
                         input_data: dict) -> float:
        """
        计算匹配分数
        
        评分因素：
        1. 条件匹配度（权重40%）
        2. 片段置信度（权重30%）
        3. 权威等级（权重20%）
        4. 历史表现（权重10%）
        """
        # 条件匹配度
        condition_score = self._calculate_condition_score(snippet, input_data)
        
        # 片段置信度
        confidence_score = snippet.confidence
        
        # 权威等级（1-5 → 0.2-1.0）
        authority_score = snippet.authority / 5.0
        
        # 历史表现（基于用户反馈）
        history_score = min(snippet.feedback_score / 5.0, 1.0) if snippet.feedback_score > 0 else 0.5
        
        # 加权平均
        final_score = (
            condition_score * 0.4 +
            confidence_score * 0.3 +
            authority_score * 0.2 +
            history_score * 0.1
        )
        
        return final_score
    
    def _calculate_condition_score(self, snippet, input_data) -> float:
        """计算条件匹配度"""
        total = len(snippet.conditions)
        matched = sum(1 for c in snippet.conditions 
                     if self._check_condition(c, input_data))
        return matched / total if total > 0 else 0
```

---

# 2. frontend/ - 前端详解

## 2.1 前端技术栈解释

```
【Next.js】
是什么：React的升级框架
作用：让React更容易做网站
特点：
  - 自动路由（不用手动配置URL）
  - 服务器渲染（首次加载更快）
  - 自动代码分割（只加载需要的代码）

【React】
是什么：用户界面库
作用：用组件方式搭建网页
特点：
  - 组件化（像搭积木）
  - 虚拟DOM（更新更快）
  - 单向数据流（数据清晰）

【TailwindCSS】
是什么：CSS工具库
作用：用类名写样式
特点：
  - 不用写CSS文件
  - 类名直观（bg-red-500 = 红色背景）
  - 响应式简单（md:w-1/2 = 中屏幕宽度50%）

【TypeScript】
是什么：带类型的JavaScript
作用：减少代码错误
特点：
  - 编译时检查类型
  - IDE提示更智能
  - 重构更安全
```

## 2.2 前端目录结构详解

```
frontend/
├── src/
│   ├── app/                    # 页面目录
│   │   ├── layout.tsx          # 根布局（所有页面共用）
│   │   ├── page.tsx            # 首页
│   │   ├── globals.css         # 全局样式
│   │   └── favicon.ico         # 网站图标
│   │
│   ├── components/             # 组件目录
│   │   ├── auth/               # 认证相关组件
│   │   ├── layout/             # 布局组件
│   │   ├── profile/            # 用户资料组件
│   │   ├── views/              # 各种视图组件
│   │   ├── DreamRecorder.tsx   # 梦境录入器
│   │   └── ...
│   │
│   ├── hooks/                  # 自定义钩子
│   │   ├── useAuth.ts          # 认证钩子
│   │   ├── useApi.ts           # API调用钩子
│   │   └── ...
│   │
│   ├── lib/                    # 工具函数库
│   │   ├── api.ts              # API客户端
│   │   ├── utils.ts            # 通用工具
│   │   └── ...
│   │
│   ├── types/                  # TypeScript类型定义
│   │   ├── bazi.ts             # 八字相关类型
│   │   ├── astro.ts            # 占星相关类型
│   │   └── ...
│   │
│   └── styles/                 # 样式文件
│
├── public/                     # 静态资源
├── package.json                # 依赖配置
├── tsconfig.json               # TypeScript配置
└── next.config.ts              # Next.js配置
```

## 2.3 组件详解

### 2.3.1 什么是组件？

```
【概念】
组件 = 可重用的界面部件

【例子】
一个"按钮"组件可以在很多地方使用：
- 登录页面的"登录"按钮
- 分析页面的"开始分析"按钮
- 设置页面的"保存"按钮

只需要写一次按钮的代码，到处可用
```

### 2.3.2 组件代码示例

```tsx
// frontend/src/components/views/BaziView.tsx

import React, { useState } from 'react';

/**
 * 八字结果显示组件
 * 
 * 职责：
 * 1. 显示八字四柱
 * 2. 显示十神信息
 * 3. 显示解读文字
 */

// 定义组件接收的参数类型
interface BaziViewProps {
  // 八字数据
  bazi: {
    year: { stem: string; branch: string };
    month: { stem: string; branch: string };
    day: { stem: string; branch: string };
    hour: { stem: string; branch: string };
  };
  // 十神列表
  tenGods?: string[];
  // 解读文字
  interpretation?: string;
  // 加载状态
  isLoading?: boolean;
}

// 组件函数
export default function BaziView({ 
  bazi, 
  tenGods, 
  interpretation,
  isLoading = false 
}: BaziViewProps) {
  
  // 状态：是否展开详细解读
  const [expanded, setExpanded] = useState(false);
  
  // 如果正在加载，显示加载动画
  if (isLoading) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500" />
        <span className="ml-4 text-gray-500">正在分析...</span>
      </div>
    );
  }
  
  return (
    <div className="bg-white rounded-lg shadow-md p-6">
      {/* 标题 */}
      <h2 className="text-2xl font-bold mb-4 text-gray-800">
        八字命盘
      </h2>
      
      {/* 四柱显示 */}
      <div className="grid grid-cols-4 gap-4 mb-6">
        {/* 年柱 */}
        <PillarCard 
          title="年柱" 
          stem={bazi.year.stem} 
          branch={bazi.year.branch} 
        />
        {/* 月柱 */}
        <PillarCard 
          title="月柱" 
          stem={bazi.month.stem} 
          branch={bazi.month.branch} 
        />
        {/* 日柱（日主） */}
        <PillarCard 
          title="日柱" 
          stem={bazi.day.stem} 
          branch={bazi.day.branch}
          isMain={true}  // 高亮日主
        />
        {/* 时柱 */}
        <PillarCard 
          title="时柱" 
          stem={bazi.hour.stem} 
          branch={bazi.hour.branch} 
        />
      </div>
      
      {/* 十神显示 */}
      {tenGods && tenGods.length > 0 && (
        <div className="mb-6">
          <h3 className="text-lg font-semibold mb-2">十神配置</h3>
          <div className="flex flex-wrap gap-2">
            {tenGods.map((god, index) => (
              <span 
                key={index}
                className="px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm"
              >
                {god}
              </span>
            ))}
          </div>
        </div>
      )}
      
      {/* 解读文字 */}
      {interpretation && (
        <div className="border-t pt-4">
          <div className="flex justify-between items-center mb-2">
            <h3 className="text-lg font-semibold">命理解读</h3>
            <button 
              onClick={() => setExpanded(!expanded)}
              className="text-blue-500 hover:text-blue-700"
            >
              {expanded ? '收起' : '展开全文'}
            </button>
          </div>
          <p className={`text-gray-600 leading-relaxed ${
            expanded ? '' : 'line-clamp-3'  // 不展开时只显示3行
          }`}>
            {interpretation}
          </p>
        </div>
      )}
    </div>
  );
}

// 子组件：柱卡片
function PillarCard({ 
  title, 
  stem, 
  branch,
  isMain = false 
}: {
  title: string;
  stem: string;
  branch: string;
  isMain?: boolean;
}) {
  return (
    <div className={`
      text-center p-4 rounded-lg
      ${isMain ? 'bg-yellow-100 border-2 border-yellow-400' : 'bg-gray-50'}
    `}>
      <div className="text-sm text-gray-500 mb-2">{title}</div>
      <div className="text-3xl font-bold">
        <span className="text-red-600">{stem}</span>
        <span className="text-blue-600">{branch}</span>
      </div>
      {isMain && (
        <div className="text-xs text-yellow-600 mt-1">日主</div>
      )}
    </div>
  );
}
```

### 2.3.3 样式类名解释

```
TailwindCSS类名速查：

【布局】
flex                  弹性布局
grid                  网格布局
grid-cols-4           4列
gap-4                 间距4单位

【尺寸】
w-full                宽度100%
h-64                  高度64单位
p-6                   内边距6单位
mb-4                  下外边距4单位

【颜色】
bg-white              白色背景
bg-blue-100           浅蓝色背景
text-gray-800         深灰色文字
border-yellow-400     黄色边框

【文字】
text-2xl              大号文字
font-bold             粗体
text-center           居中

【圆角和阴影】
rounded-lg            大圆角
rounded-full          全圆（圆形）
shadow-md             中等阴影

【响应式】
md:w-1/2              中等屏幕时宽度50%
lg:grid-cols-3        大屏幕时3列
```

## 2.4 hooks/ - 自定义钩子详解

### 2.4.1 什么是钩子？

```
【概念】
钩子（Hook）= 可复用的逻辑代码

【为什么需要？】
多个组件需要相同的逻辑，比如：
- 多个页面都需要检查登录状态
- 多个组件都需要调用API

把这些逻辑提取出来，就是"钩子"
```

### 2.4.2 useAuth.ts 详解

```tsx
// frontend/src/hooks/useAuth.ts

import { useState, useEffect, useContext, createContext } from 'react';
import { api } from '@/lib/api';

// 用户类型定义
interface User {
  id: string;
  email: string;
  name: string;
}

// 认证上下文类型
interface AuthContextType {
  user: User | null;           // 当前用户
  isLoading: boolean;          // 是否正在加载
  isAuthenticated: boolean;    // 是否已登录
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  register: (email: string, password: string, name: string) => Promise<void>;
}

// 创建上下文
const AuthContext = createContext<AuthContextType | null>(null);

/**
 * 认证钩子
 * 
 * 使用方式：
 * const { user, login, logout, isAuthenticated } = useAuth();
 */
export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}

/**
 * 认证提供者组件
 * 
 * 包裹整个应用，提供认证功能
 */
export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  
  // 页面加载时检查登录状态
  useEffect(() => {
    checkAuth();
  }, []);
  
  async function checkAuth() {
    try {
      // 尝试用存储的token获取用户信息
      const token = localStorage.getItem('token');
      if (token) {
        const userData = await api.get('/auth/me');
        setUser(userData);
      }
    } catch (error) {
      // token无效，清除
      localStorage.removeItem('token');
    } finally {
      setIsLoading(false);
    }
  }
  
  async function login(email: string, password: string) {
    const response = await api.post('/auth/login', { email, password });
    localStorage.setItem('token', response.token);
    setUser(response.user);
  }
  
  async function logout() {
    await api.post('/auth/logout');
    localStorage.removeItem('token');
    setUser(null);
  }
  
  async function register(email: string, password: string, name: string) {
    const response = await api.post('/auth/register', { email, password, name });
    localStorage.setItem('token', response.token);
    setUser(response.user);
  }
  
  const value = {
    user,
    isLoading,
    isAuthenticated: !!user,
    login,
    logout,
    register
  };
  
  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}
```

### 2.4.3 useApi.ts 详解

```tsx
// frontend/src/hooks/useApi.ts

import { useState, useCallback } from 'react';
import { api } from '@/lib/api';

/**
 * API调用钩子
 * 
 * 使用方式：
 * const { data, error, isLoading, execute } = useApi('/analyze');
 * 
 * // 调用API
 * execute({ birth_date: '1990-01-15', ... });
 */
export function useApi<T>(endpoint: string) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  
  const execute = useCallback(async (payload?: any) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await api.post<T>(endpoint, payload);
      setData(response);
      return response;
    } catch (err: any) {
      const errorMessage = err.message || '请求失败';
      setError(errorMessage);
      throw err;
    } finally {
      setIsLoading(false);
    }
  }, [endpoint]);
  
  return { data, error, isLoading, execute };
}

// 使用示例
function AnalyzePage() {
  const { data, error, isLoading, execute } = useApi('/analyze');
  
  const handleSubmit = async (formData) => {
    try {
      await execute(formData);
      // 成功后的处理
    } catch {
      // 错误处理
    }
  };
  
  return (
    <div>
      {isLoading && <LoadingSpinner />}
      {error && <ErrorMessage>{error}</ErrorMessage>}
      {data && <BaziView bazi={data.bazi} />}
    </div>
  );
}
```

## 2.5 types/ - 类型定义详解

```tsx
// frontend/src/types/bazi.ts

/**
 * 八字相关类型定义
 * 
 * 这些类型必须与后端的 core/contracts/ 保持一致！
 */

// 天干类型
export type Stem = '甲' | '乙' | '丙' | '丁' | '戊' | 
                   '己' | '庚' | '辛' | '壬' | '癸';

// 地支类型
export type Branch = '子' | '丑' | '寅' | '卯' | '辰' | '巳' |
                     '午' | '未' | '申' | '酉' | '戌' | '亥';

// 柱类型
export interface Pillar {
  stem: Stem;
  branch: Branch;
}

// 八字结果类型
export interface BaziResult {
  year: Pillar;
  month: Pillar;
  day: Pillar;
  hour: Pillar;
  tenGods?: string[];
  hiddenStems?: Record<string, string[]>;
}

// 分析请求类型
export interface AnalyzeRequest {
  birthDate: string;      // ISO格式日期
  birthTime: string;      // HH:mm格式
  birthPlace: string;     // 地点名称
  gender?: 'male' | 'female';
}

// 分析响应类型
export interface AnalyzeResponse {
  status: 'success' | 'error';
  bazi: BaziResult;
  interpretation: string;
  actions?: ActionItem[];
}

// 行动建议类型
export interface ActionItem {
  id: string;
  content: string;
  priority: 'high' | 'medium' | 'low';
  timeWindow?: string;
}
```

## 2.6 lib/api.ts - API客户端详解

```tsx
// frontend/src/lib/api.ts

/**
 * API客户端
 * 
 * 封装所有后端API调用
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

class ApiClient {
  private baseUrl: string;
  
  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }
  
  private getHeaders(): HeadersInit {
    const headers: HeadersInit = {
      'Content-Type': 'application/json',
    };
    
    // 添加认证token
    const token = localStorage.getItem('token');
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    
    return headers;
  }
  
  async get<T>(endpoint: string): Promise<T> {
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'GET',
      headers: this.getHeaders(),
    });
    
    return this.handleResponse<T>(response);
  }
  
  async post<T>(endpoint: string, data?: any): Promise<T> {
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'POST',
      headers: this.getHeaders(),
      body: data ? JSON.stringify(data) : undefined,
    });
    
    return this.handleResponse<T>(response);
  }
  
  private async handleResponse<T>(response: Response): Promise<T> {
    // 检查HTTP状态
    if (!response.ok) {
      if (response.status === 401) {
        // 未授权，清除token并跳转登录
        localStorage.removeItem('token');
        window.location.href = '/login';
      }
      
      const error = await response.json();
      throw new Error(error.detail || '请求失败');
    }
    
    return response.json();
  }
}

export const api = new ApiClient(API_BASE_URL);
```
