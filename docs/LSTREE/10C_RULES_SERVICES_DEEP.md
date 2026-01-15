# 第三部分：规则引擎与服务层 - 极致细化版

---

# 1. backend/rules/ - 规则引擎详解

## 1.1 什么是规则引擎？

**最简单的理解**：
规则引擎 = 一个"裁判"，根据规则判断情况

```
【没有规则引擎】
if bazi.day_stem == "甲" and bazi.month_branch == "子":
    return "甲木生于子月，水旺木相..."
elif bazi.day_stem == "甲" and bazi.month_branch == "寅":
    return "甲木生于寅月，木旺..."
# ... 几千个if-else，代码无法维护

【有规则引擎】
规则存在YAML文件中，程序自动读取和匹配
添加新规则只需要编辑YAML，不用改代码
```

## 1.2 规则引擎的组成

```
rules/
├── engine.py        # 引擎核心：执行规则匹配
├── condition.py     # 条件解析：理解规则的条件部分
├── conflict.py      # 冲突处理：多规则命中时如何选择
├── context.py       # 上下文：保存当前分析的信息
├── coverage.py      # 覆盖率：统计规则覆盖情况
├── dimension.py     # 维度处理：处理不同维度的规则
├── changelog.py     # 变更日志：记录规则变化
├── reloader.py      # 热重载：不重启更新规则
└── tests/           # 测试
```

## 1.3 engine.py - 引擎核心详解

```python
# backend/rules/engine.py

class RulesEngine:
    """
    规则引擎核心
    
    职责：
    1. 加载规则文件
    2. 接收输入数据
    3. 匹配符合条件的规则
    4. 返回匹配结果
    """
    
    def __init__(self):
        self.rules = []              # 所有规则
        self.index = {}              # 规则索引（加速查找）
        self.context = Context()     # 当前上下文
        
    def load_rules(self, rules_dir: str = "data/rules/"):
        """
        加载规则文件
        
        步骤：
        1. 扫描rules目录下所有YAML文件
        2. 解析每个文件
        3. 验证规则格式
        4. 构建索引
        """
        for yaml_file in Path(rules_dir).glob("**/*.yaml"):
            rules_data = yaml.safe_load(yaml_file.read_text())
            for rule_data in rules_data.get("rules", []):
                rule = Rule.from_dict(rule_data)
                self.rules.append(rule)
                self._add_to_index(rule)
        
        print(f"已加载 {len(self.rules)} 条规则")
    
    def match(self, input_data: dict) -> List[MatchResult]:
        """
        匹配规则
        
        参数：
            input_data: 输入数据（八字、星盘等）
            
        返回：
            匹配到的规则列表，按优先级排序
        """
        # 设置上下文
        self.context.set_input(input_data)
        
        # 收集匹配结果
        matches = []
        
        # 遍历规则（实际使用索引加速）
        for rule in self._get_candidate_rules(input_data):
            if self._check_conditions(rule, input_data):
                match_result = MatchResult(
                    rule=rule,
                    confidence=self._calculate_confidence(rule, input_data),
                    matched_factors=self._get_matched_factors(rule, input_data)
                )
                matches.append(match_result)
        
        # 处理冲突
        matches = self._resolve_conflicts(matches)
        
        # 按优先级排序
        matches.sort(key=lambda x: x.confidence, reverse=True)
        
        return matches
    
    def _check_conditions(self, rule: Rule, input_data: dict) -> bool:
        """
        检查规则条件是否满足
        
        示例规则条件：
        conditions:
          - type: day_stem
            value: 甲
          - type: month_branch
            value: 子
            
        需要同时满足：日干是甲 AND 月支是子
        """
        for condition in rule.conditions:
            if not self._evaluate_condition(condition, input_data):
                return False
        return True
    
    def _evaluate_condition(self, condition: dict, input_data: dict) -> bool:
        """评估单个条件"""
        cond_type = condition["type"]
        expected_value = condition["value"]
        operator = condition.get("operator", "equals")  # 默认等于
        
        # 获取实际值
        actual_value = self._get_value(input_data, cond_type)
        
        # 比较
        if operator == "equals":
            return actual_value == expected_value
        elif operator == "in":
            return actual_value in expected_value
        elif operator == "contains":
            return expected_value in actual_value
        elif operator == "greater_than":
            return actual_value > expected_value
        # ... 更多操作符
```

## 1.4 规则文件格式详解

```yaml
# data/rules/bazi/ten_gods.yaml

# 元信息
meta:
  name: 十神规则集
  version: 2.1.0
  author: LS Team
  last_updated: 2024-01-15
  description: 八字十神相关规则

# 规则列表
rules:
  # 规则1：比肩旺相
  - id: bazi_ten_god_001
    name: 比肩旺相格
    category: 十神
    subcategory: 比肩
    priority: 80                    # 优先级，0-100
    confidence: 0.85                # 置信度
    
    # 触发条件（所有条件都要满足）
    conditions:
      - type: ten_god_exists        # 条件类型
        value: 比肩                  # 期望值
      - type: ten_god_strength      # 十神强度
        value: 旺                    # 旺相休囚死
        
    # 额外条件（可选，满足其一即可）
    optional_conditions:
      - type: month_branch
        value: [寅, 卯]              # 月支为寅或卯
      - type: day_stem
        value: [甲, 乙]              # 日干为甲或乙
    
    # 匹配后的输出
    output:
      interpretation: |
        比肩旺相者，主性格独立，有主见，
        不喜受人约束，适合自主创业。
        兄弟朋友多，人缘较好，
        但也可能有争财争权之象。
      keywords:
        - 独立
        - 主见
        - 朋友多
      dimension: 性格
      sentiment: 中性
      
    # 关联语义片段
    semantic_refs:
      - sanming_bijian_001
      - ziping_bijian_003
      
    # 冲突规则（这些规则不能同时命中）
    conflicts_with:
      - bazi_ten_god_002
      
  # 规则2：比肩太过
  - id: bazi_ten_god_002
    name: 比肩太过
    conditions:
      - type: ten_god_count
        value: 比肩
        operator: greater_than
        threshold: 3                 # 比肩超过3个
    output:
      interpretation: |
        比肩太多者，主争夺心强，
        容易与人发生竞争冲突，
        需学会谦让与合作。
      sentiment: 负面
    # ... 更多配置
```

## 1.5 condition.py - 条件解析详解

```python
# backend/rules/condition.py

class ConditionParser:
    """
    条件解析器
    
    支持的条件类型：
    1. 简单比较：等于、不等于、大于、小于
    2. 包含关系：in、contains
    3. 复合条件：AND、OR、NOT
    4. 自定义函数：调用Python函数
    """
    
    # 条件类型注册表
    CONDITION_TYPES = {
        # 八字相关
        "day_stem": lambda data: data.get("bazi", {}).get("day", {}).get("stem"),
        "day_branch": lambda data: data.get("bazi", {}).get("day", {}).get("branch"),
        "month_branch": lambda data: data.get("bazi", {}).get("month", {}).get("branch"),
        "year_stem": lambda data: data.get("bazi", {}).get("year", {}).get("stem"),
        "ten_god_exists": lambda data, value: value in data.get("ten_gods", []),
        "ten_god_count": lambda data, value: data.get("ten_gods", []).count(value),
        "ten_god_strength": lambda data, value: data.get("strengths", {}).get(value),
        
        # 占星相关
        "sun_sign": lambda data: data.get("astro", {}).get("sun", {}).get("sign"),
        "moon_sign": lambda data: data.get("astro", {}).get("moon", {}).get("sign"),
        "asc_sign": lambda data: data.get("astro", {}).get("asc", {}).get("sign"),
        "has_aspect": lambda data, value: value in data.get("aspects", []),
        
        # 紫微相关
        "palace_star": lambda data, palace: data.get("ziwei", {}).get(palace, {}).get("main_star"),
        "has_sihua": lambda data, value: value in data.get("sihua", []),
    }
    
    def parse(self, condition: dict, input_data: dict) -> bool:
        """
        解析并评估条件
        
        参数：
            condition: 条件定义
            input_data: 输入数据
            
        返回：
            条件是否满足
        """
        cond_type = condition["type"]
        
        # 获取条件处理函数
        if cond_type not in self.CONDITION_TYPES:
            raise ValueError(f"未知条件类型: {cond_type}")
        
        handler = self.CONDITION_TYPES[cond_type]
        
        # 获取实际值
        if "value" in condition:
            actual = handler(input_data, condition["value"])
        else:
            actual = handler(input_data)
        
        # 比较操作
        operator = condition.get("operator", "equals")
        expected = condition.get("value")
        
        return self._compare(actual, expected, operator)
    
    def _compare(self, actual, expected, operator: str) -> bool:
        """执行比较"""
        if operator == "equals":
            return actual == expected
        elif operator == "not_equals":
            return actual != expected
        elif operator == "in":
            return actual in expected
        elif operator == "not_in":
            return actual not in expected
        elif operator == "contains":
            return expected in str(actual)
        elif operator == "greater_than":
            return actual > expected
        elif operator == "less_than":
            return actual < expected
        elif operator == "between":
            return expected[0] <= actual <= expected[1]
        elif operator == "exists":
            return actual is not None
        elif operator == "regex":
            import re
            return bool(re.match(expected, str(actual)))
        else:
            raise ValueError(f"未知操作符: {operator}")
```

## 1.6 conflict.py - 冲突处理详解

```python
# backend/rules/conflict.py

class ConflictResolver:
    """
    规则冲突解决器
    
    当多条规则同时匹配时，如何选择？
    
    策略：
    1. 优先级：高优先级规则胜出
    2. 特异性：更具体的规则胜出
    3. 权威性：权威来源的规则胜出
    4. 多数决：多条规则支持的结论胜出
    5. 共存：允许多个结论同时存在
    """
    
    def resolve(self, matches: List[MatchResult]) -> List[MatchResult]:
        """
        解决冲突
        
        步骤：
        1. 分组：把结论相似的规则分到一组
        2. 组内处理：每组选出代表
        3. 组间处理：处理不同组之间的冲突
        """
        # 1. 按dimension分组
        groups = self._group_by_dimension(matches)
        
        # 2. 每组处理冲突
        resolved = []
        for dimension, group_matches in groups.items():
            if len(group_matches) == 1:
                resolved.extend(group_matches)
            else:
                # 检查是否有显式冲突
                conflicting = self._find_conflicts(group_matches)
                if conflicting:
                    winner = self._resolve_conflict(conflicting)
                    resolved.append(winner)
                    # 添加非冲突的
                    for m in group_matches:
                        if m not in conflicting:
                            resolved.append(m)
                else:
                    # 没有冲突，全部保留
                    resolved.extend(group_matches)
        
        return resolved
    
    def _resolve_conflict(self, conflicting: List[MatchResult]) -> MatchResult:
        """
        解决一组冲突规则
        """
        # 策略1：按优先级
        by_priority = sorted(conflicting, 
                            key=lambda x: x.rule.priority, 
                            reverse=True)
        if by_priority[0].rule.priority > by_priority[1].rule.priority:
            return by_priority[0]
        
        # 优先级相同，策略2：按特异性（条件数量）
        by_specificity = sorted(conflicting,
                               key=lambda x: len(x.rule.conditions),
                               reverse=True)
        if len(by_specificity[0].rule.conditions) > len(by_specificity[1].rule.conditions):
            return by_specificity[0]
        
        # 策略3：按置信度
        by_confidence = sorted(conflicting,
                              key=lambda x: x.confidence,
                              reverse=True)
        return by_confidence[0]
```

## 1.7 规则匹配完整流程图

```
用户八字数据输入
        ↓
┌───────────────────────────────────────────────────────────────┐
│ 1. 上下文初始化                                               │
│    context.set_input(bazi_data)                              │
└──────────────────────────┬────────────────────────────────────┘
                           ↓
┌───────────────────────────────────────────────────────────────┐
│ 2. 规则预筛选（使用索引）                                      │
│    根据日干、月支等快速定位可能匹配的规则                       │
│    从10000条规则 → 筛选出500条候选                             │
└──────────────────────────┬────────────────────────────────────┘
                           ↓
┌───────────────────────────────────────────────────────────────┐
│ 3. 逐条检查条件                                               │
│    for rule in candidates:                                    │
│        if check_conditions(rule, data):                       │
│            matches.append(rule)                               │
│    500条候选 → 50条匹配                                        │
└──────────────────────────┬────────────────────────────────────┘
                           ↓
┌───────────────────────────────────────────────────────────────┐
│ 4. 冲突解决                                                   │
│    检查50条规则中的冲突                                        │
│    按优先级、特异性等策略选择                                   │
│    50条 → 35条（去除冲突的输者）                               │
└──────────────────────────┬────────────────────────────────────┘
                           ↓
┌───────────────────────────────────────────────────────────────┐
│ 5. 获取语义片段                                               │
│    每条匹配规则关联语义片段ID                                   │
│    从semantics/模块获取具体内容                                │
└──────────────────────────┬────────────────────────────────────┘
                           ↓
┌───────────────────────────────────────────────────────────────┐
│ 6. 组装输出                                                   │
│    返回 List[MatchResult]                                     │
│    包含：规则、置信度、语义片段                                 │
└───────────────────────────────────────────────────────────────┘
```

---

# 2. backend/services/ - 服务层详解

## 2.1 服务层的作用

```
【为什么需要服务层？】

没有服务层：
  API直接调用计算器、规则引擎、LLM
  代码耦合严重，难以维护

有服务层：
  API → 服务层 → 各个模块
  服务层负责编排和协调
  每个服务专注一个业务领域
```

## 2.2 narrative/ - 叙事服务详解

### 2.2.1 职责
把计算结果转换成用户能读懂的文字

### 2.2.2 文件结构

| 文件 | 职责 | 说明 |
|------|------|------|
| `generator.py` | 生成叙事 | 核心生成逻辑 |
| `prompt_builder.py` | 构建提示词 | 给AI的指令 |
| `snippet_service.py` | 语义片段选择 | 选择合适的片段 |

### 2.2.3 generator.py 详解

```python
# backend/services/narrative/generator.py

class NarrativeGenerator:
    """
    叙事生成器
    
    工作流程：
    1. 接收多引擎计算结果
    2. 选择相关语义片段
    3. 构建AI提示词
    4. 调用AI生成文字
    5. 后处理和格式化
    """
    
    def __init__(self):
        self.snippet_service = SnippetService()
        self.prompt_builder = PromptBuilder()
        self.llm_client = LLMClient()
    
    async def generate(self, 
                       engine_results: Dict[str, Any],
                       scenario: str = "general",
                       style: str = "professional") -> str:
        """
        生成叙事文本
        
        参数：
            engine_results: 各引擎的计算结果
                {
                    "bazi": BaziResult,
                    "astro": AstroResult,
                    "ziwei": ZiweiResult
                }
            scenario: 场景（career/relationship/health/general）
            style: 风格（professional/casual/poetic）
            
        返回：
            生成的叙事文本
        """
        # 1. 选择语义片段
        snippets = await self.snippet_service.select(
            engine_results=engine_results,
            scenario=scenario,
            max_snippets=10
        )
        
        # 2. 构建提示词
        prompt = self.prompt_builder.build(
            engine_results=engine_results,
            snippets=snippets,
            scenario=scenario,
            style=style
        )
        
        # 3. 调用AI
        raw_response = await self.llm_client.complete(
            prompt=prompt,
            model="medium",  # 使用中等复杂度模型
            max_tokens=2000
        )
        
        # 4. 后处理
        narrative = self._post_process(raw_response)
        
        return narrative
    
    def _post_process(self, raw_text: str) -> str:
        """后处理"""
        # 去除多余空白
        text = " ".join(raw_text.split())
        # 修正标点
        text = self._fix_punctuation(text)
        # 分段
        text = self._add_paragraphs(text)
        return text
```

### 2.2.4 prompt_builder.py 详解

```python
# backend/services/narrative/prompt_builder.py

class PromptBuilder:
    """
    提示词构建器
    
    构建给AI的指令，决定生成什么样的文字
    """
    
    # 风格模板
    STYLE_TEMPLATES = {
        "professional": """
你是一位专业的命理分析师，请用专业、客观的语言进行解读。
使用第二人称"您"，语气正式但不失亲和。
""",
        "casual": """
你是一位亲切的朋友，用轻松自然的语言解读命理信息。
使用"你"，语气随和，可以适当加入鼓励。
""",
        "poetic": """
你是一位富有诗意的解读者，用优美的语言描绘命运图景。
可以使用比喻、排比等修辞手法。
"""
    }
    
    # 场景模板
    SCENARIO_TEMPLATES = {
        "career": "重点分析事业发展、职业选择、工作机遇方面的信息。",
        "relationship": "重点分析感情婚姻、人际关系方面的信息。",
        "health": "重点分析健康状况、养生建议方面的信息。",
        "general": "进行全面综合的分析。"
    }
    
    def build(self, 
              engine_results: dict,
              snippets: List[Snippet],
              scenario: str,
              style: str) -> str:
        """
        构建完整的提示词
        """
        prompt = f"""
{self.STYLE_TEMPLATES[style]}

{self.SCENARIO_TEMPLATES[scenario]}

# 命盘信息

## 八字
{self._format_bazi(engine_results.get("bazi"))}

## 星盘（如有）
{self._format_astro(engine_results.get("astro"))}

## 紫微（如有）
{self._format_ziwei(engine_results.get("ziwei"))}

# 参考解读（来自经典文献）

{self._format_snippets(snippets)}

# 要求

请综合以上信息，生成一段完整的命理解读。
要求：
1. 结合多个系统的信息进行交叉验证
2. 对于不同系统结论一致的部分，加强表述
3. 对于结论有差异的部分，客观呈现，不要回避
4. 结尾给出积极正面的建议
5. 字数控制在800-1200字

# 开始解读
"""
        return prompt
    
    def _format_bazi(self, bazi_result) -> str:
        """格式化八字信息"""
        if not bazi_result:
            return "（无八字信息）"
        return f"""
四柱：{bazi_result.to_string()}
日主：{bazi_result.day_master}，五行属{bazi_result.day.element}
十神：{', '.join(bazi_result.ten_gods or [])}
"""

    def _format_snippets(self, snippets: List[Snippet]) -> str:
        """格式化语义片段"""
        if not snippets:
            return "（无参考解读）"
        result = []
        for i, snippet in enumerate(snippets, 1):
            result.append(f"""
【参考{i}】来源：{snippet.source}
{snippet.interpretation}
""")
        return "\n".join(result)
```

---

## 2.3 scenario/ - 场景服务详解

### 2.3.1 职责
识别用户想问什么类型的问题，分发给合适的处理器

### 2.3.2 router.py 详解

```python
# backend/services/scenario/router.py

class ScenarioRouter:
    """
    场景路由器
    
    判断用户的查询属于哪种场景，
    然后调用相应的处理流程
    """
    
    # 场景关键词
    SCENARIO_KEYWORDS = {
        "career": ["工作", "事业", "职业", "升职", "跳槽", "创业", 
                   "老板", "同事", "项目", "绩效", "薪资"],
        "relationship": ["感情", "婚姻", "恋爱", "对象", "结婚", "离婚",
                        "暗恋", "分手", "另一半", "桃花"],
        "health": ["健康", "身体", "疾病", "养生", "睡眠", "压力",
                  "运动", "饮食", "医院"],
        "wealth": ["财运", "投资", "理财", "赚钱", "亏损", "股票",
                  "房产", "收入"],
        "timing": ["什么时候", "时机", "择日", "何时", "吉日"],
    }
    
    async def route(self, 
                    user_query: str,
                    user_profile: dict = None) -> ScenarioContext:
        """
        路由用户查询到合适的场景
        
        参数：
            user_query: 用户的问题
            user_profile: 用户资料（可选，用于个性化）
            
        返回：
            ScenarioContext: 场景上下文
        """
        # 1. 关键词匹配
        scenario = self._match_by_keywords(user_query)
        
        # 2. 如果关键词无法确定，用AI判断
        if scenario == "uncertain":
            scenario = await self._classify_by_llm(user_query)
        
        # 3. 获取场景配置
        config = self._get_scenario_config(scenario)
        
        # 4. 创建上下文
        context = ScenarioContext(
            scenario=scenario,
            query=user_query,
            config=config,
            required_engines=config["engines"],  # 需要哪些计算引擎
            focus_dimensions=config["dimensions"]  # 重点维度
        )
        
        return context
    
    def _match_by_keywords(self, query: str) -> str:
        """通过关键词匹配场景"""
        scores = {}
        for scenario, keywords in self.SCENARIO_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw in query)
            if score > 0:
                scores[scenario] = score
        
        if not scores:
            return "general"
        
        # 返回得分最高的场景
        return max(scores, key=scores.get)
    
    def _get_scenario_config(self, scenario: str) -> dict:
        """获取场景配置"""
        configs = {
            "career": {
                "engines": ["bazi", "ziwei", "astro"],
                "dimensions": ["事业", "官运", "财运"],
                "rules_focus": ["十神-官杀", "宫位-官禄"],
                "template": "career_template.yaml"
            },
            "relationship": {
                "engines": ["bazi", "ziwei", "astro"],
                "dimensions": ["感情", "婚姻", "人缘"],
                "rules_focus": ["十神-财官", "宫位-夫妻"],
                "template": "relationship_template.yaml"
            },
            # ... 更多场景配置
        }
        return configs.get(scenario, configs["general"])
```

---

## 2.4 action_compiler/ - 行动编译器详解

### 2.4.1 职责
把命理洞察转化为具体的行动建议

### 2.4.2 工作流程

```
命理解读结果
      ↓
┌─────────────────────────────────────────────────────────┐
│ analyzer.py                                              │
│ 分析解读中的关键信息                                      │
│ 提取：机会、风险、时间窗口、重点领域                       │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│ compiler.py                                              │
│ 把分析结果编译成行动条目                                   │
│ 每条行动包含：内容、优先级、时间、类型                      │
└────────────────────────┬────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│ aggregator.py                                            │
│ 合并去重相似的建议                                        │
│ 按优先级排序                                              │
└────────────────────────┬────────────────────────────────┘
                         ↓
输出：行动建议列表
```

### 2.4.3 compiler.py 详解

```python
# backend/services/action_compiler/compiler.py

class ActionCompiler:
    """
    行动编译器
    
    把命理洞察编译成可执行的行动建议
    """
    
    # 行动模板
    ACTION_TEMPLATES = {
        "opportunity": {
            "positive": "这段时期{dimension}运势良好，建议{action}",
            "timing": "在{time_window}期间，是{action}的好时机"
        },
        "caution": {
            "negative": "近期{dimension}方面需注意，建议{action}",
            "avoid": "这段时期不宜{action}，可以{alternative}"
        },
        "development": {
            "growth": "从长远看，{dimension}方面可通过{action}来提升",
            "learning": "建议学习{skill}，有助于{benefit}"
        }
    }
    
    def compile(self, 
                analysis_result: AnalysisResult,
                user_context: dict = None) -> List[Action]:
        """
        编译行动建议
        
        参数：
            analysis_result: 分析结果
            user_context: 用户上下文（年龄、职业等）
            
        返回：
            行动建议列表
        """
        actions = []
        
        # 1. 处理机会类洞察
        for opportunity in analysis_result.opportunities:
            action = self._compile_opportunity(opportunity)
            actions.append(action)
        
        # 2. 处理风险类洞察
        for risk in analysis_result.risks:
            action = self._compile_caution(risk)
            actions.append(action)
        
        # 3. 处理发展类洞察
        for development in analysis_result.developments:
            action = self._compile_development(development)
            actions.append(action)
        
        # 4. 根据用户上下文调整
        if user_context:
            actions = self._personalize(actions, user_context)
        
        # 5. 设置优先级
        actions = self._prioritize(actions)
        
        return actions
    
    def _compile_opportunity(self, opportunity: dict) -> Action:
        """编译机会类行动"""
        template = self.ACTION_TEMPLATES["opportunity"]["positive"]
        content = template.format(
            dimension=opportunity["dimension"],
            action=opportunity["suggested_action"]
        )
        
        return Action(
            id=str(uuid.uuid4()),
            content=content,
            type="opportunity",
            dimension=opportunity["dimension"],
            priority=self._calculate_priority(opportunity),
            time_window=opportunity.get("time_window"),
            source_engines=opportunity.get("source_engines", []),
            confidence=opportunity.get("confidence", 0.8)
        )
```

---

## 2.5 memory/ - 记忆服务详解

### 2.5.1 职责
记住用户的历史信息，实现个性化和持续对话

### 2.5.2 为什么需要记忆？

```
【没有记忆】
每次对话都是全新的
用户："我上次问过事业..."
系统："抱歉，我不记得上次对话"

【有记忆】
用户："我上次问过事业..."
系统："是的，上次您问的是关于跳槽的时机，我建议..."

记忆让AI更像一个了解你的顾问
```

### 2.5.3 service.py 详解

```python
# backend/services/memory/service.py

class MemoryService:
    """
    记忆服务
    
    类型：
    1. 短期记忆：当前会话的对话历史
    2. 长期记忆：用户的命盘、偏好、历史洞察
    3. 工作记忆：当前任务的临时信息
    """
    
    def __init__(self):
        self.db = MongoDB()
        self.cache = Redis()
        self.encryption = EncryptionService()
    
    async def remember(self, 
                       user_id: str,
                       memory_type: str,
                       content: dict,
                       metadata: dict = None):
        """
        保存记忆
        
        参数：
            user_id: 用户ID
            memory_type: 记忆类型（short_term/long_term/working）
            content: 记忆内容
            metadata: 元数据（时间戳、来源等）
        """
        # 加密敏感信息
        encrypted_content = self.encryption.encrypt(content)
        
        memory = {
            "user_id": user_id,
            "type": memory_type,
            "content": encrypted_content,
            "metadata": metadata or {},
            "created_at": datetime.utcnow(),
            "expires_at": self._calculate_expiry(memory_type)
        }
        
        # 保存到数据库
        await self.db.memories.insert_one(memory)
        
        # 更新缓存
        cache_key = f"memory:{user_id}:{memory_type}"
        await self.cache.lpush(cache_key, json.dumps(memory))
    
    async def recall(self,
                     user_id: str,
                     memory_type: str = None,
                     query: str = None,
                     limit: int = 10) -> List[Memory]:
        """
        检索记忆
        
        参数：
            user_id: 用户ID
            memory_type: 记忆类型（可选）
            query: 查询关键词（可选，用于语义搜索）
            limit: 返回数量
            
        返回：
            相关记忆列表
        """
        # 构建查询
        filter_query = {"user_id": user_id}
        if memory_type:
            filter_query["type"] = memory_type
        
        # 从数据库查询
        memories = await self.db.memories.find(
            filter_query
        ).sort("created_at", -1).limit(limit).to_list()
        
        # 解密
        for memory in memories:
            memory["content"] = self.encryption.decrypt(memory["content"])
        
        # 如果有查询词，进行语义排序
        if query:
            memories = self._semantic_rank(memories, query)
        
        return [Memory.from_dict(m) for m in memories]
    
    async def forget(self, user_id: str, memory_id: str = None):
        """
        删除记忆（用户有权删除自己的数据）
        """
        if memory_id:
            await self.db.memories.delete_one({
                "user_id": user_id,
                "_id": ObjectId(memory_id)
            })
        else:
            # 删除用户所有记忆
            await self.db.memories.delete_many({"user_id": user_id})
```

### 2.5.4 encryption.py - 隐私保护

```python
# backend/services/memory/encryption.py

class EncryptionService:
    """
    加密服务 - 保护用户隐私
    
    为什么需要加密？
    - 出生日期是敏感信息
    - 命理解读涉及个人隐私
    - 即使数据库泄露，也不能直接读取
    """
    
    def __init__(self):
        # 从环境变量读取密钥
        self.key = os.environ.get("ENCRYPTION_KEY").encode()
        self.cipher_suite = Fernet(self.key)
    
    def encrypt(self, data: dict) -> str:
        """加密数据"""
        json_data = json.dumps(data)
        encrypted = self.cipher_suite.encrypt(json_data.encode())
        return base64.b64encode(encrypted).decode()
    
    def decrypt(self, encrypted_data: str) -> dict:
        """解密数据"""
        encrypted = base64.b64decode(encrypted_data.encode())
        decrypted = self.cipher_suite.decrypt(encrypted)
        return json.loads(decrypted.decode())
```
