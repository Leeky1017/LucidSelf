# 第五部分：脚本与数据处理 - 极致细化版

---

# 1. scripts/codegen/ - 代码生成器详解

## 1.1 为什么需要代码生成？

```
【问题】
- 有30本典籍，每本几百条规则
- 手动写Python代码太慢太容易出错
- 规则更新后要重新写代码

【解决方案】
- 把规则写在YAML文件中（人可读）
- 用程序自动生成Python代码
- 规则更新后重新运行生成器
```

## 1.2 代码生成流程

```
典籍原文（人工结构化）
      ↓
┌─────────────────────────────────────────────────────────────┐
│  典籍/中文典籍/三命通会/                                      │
│    ├── 卷一_L3.yaml                                          │
│    ├── 卷二_L3.yaml                                          │
│    └── ...                                                   │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
scripts/logic_chain_builder/  (构建逻辑链)
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  data/logic_chains/三命通会.yaml                             │
│    - 26MB的逻辑链数据                                        │
│    - 包含所有提取的规则                                       │
└─────────────────────────────┬───────────────────────────────┘
                              ↓
scripts/codegen/semantic_generator.py  (生成代码)
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  backend/semantics/sanming/                                  │
│    ├── __init__.py                                           │
│    ├── heavenly_stems/                                       │
│    │   ├── jia.py  (自动生成的Python代码)                    │
│    │   └── ...                                               │
│    └── ...                                                   │
└─────────────────────────────────────────────────────────────┘
```

## 1.3 codegen/ 目录结构

```
codegen/
├── __init__.py              # 模块入口
├── __main__.py              # CLI入口（python -m scripts.codegen）
├── cli.py                   # 命令行接口
│
├── # 核心生成器
├── base.py                  # 生成器基类
├── semantic_generator.py    # 语义代码生成（最重要，55KB）
├── rule_generator.py        # 规则代码生成
├── factor_generator.py      # 因子代码生成
├── engine_mapping.py        # 引擎映射生成
│
├── # 支持模块
├── models.py                # 生成器数据模型
├── validation.py            # 生成代码验证
├── manifest.py              # 生成清单管理
├── exceptions.py            # 异常定义
│
├── # 运维工具
├── hot_reload.py            # 热重载支持
├── rollback.py              # 回滚机制
├── reporter.py              # 生成报告
├── error_report.py          # 错误报告
│
└── tests/                   # 测试
```

## 1.4 semantic_generator.py 详解

```python
# scripts/codegen/semantic_generator.py

"""
语义代码生成器

这是最核心的生成器，负责把逻辑链YAML转成Python代码

输入：data/logic_chains/三命通会.yaml
输出：backend/semantics/sanming/*.py
"""

import yaml
from pathlib import Path
from jinja2 import Template

class SemanticGenerator:
    """语义片段代码生成器"""
    
    # Python代码模板
    SNIPPET_TEMPLATE = '''
# 自动生成的代码，请勿手动修改
# 生成时间：{{ generated_at }}
# 来源：{{ source_book }}

from backend.semantics.core.base import SemanticSnippet, SnippetSource

SNIPPETS = [
{% for snippet in snippets %}
    SemanticSnippet(
        id="{{ snippet.id }}",
        source_book="{{ snippet.source_book }}",
        source_chapter="{{ snippet.source_chapter }}",
        source_type=SnippetSource.{{ snippet.source_type }},
        
        factor_refs={{ snippet.factor_refs }},
        conditions={{ snippet.conditions }},
        
        original_text="""{{ snippet.original_text }}""",
        interpretation="""{{ snippet.interpretation }}""",
        
        keywords={{ snippet.keywords }},
        confidence={{ snippet.confidence }},
        authority={{ snippet.authority }},
        dimension="{{ snippet.dimension }}",
        sentiment="{{ snippet.sentiment }}",
        
        related_snippets={{ snippet.related_snippets }},
        logic_chain_ref="{{ snippet.logic_chain_ref }}"
    ),
{% endfor %}
]

def get_all_snippets():
    return SNIPPETS

def match_snippets(input_data: dict):
    return [s for s in SNIPPETS if s.matches(input_data)]
'''
    
    def __init__(self, logic_chains_dir: str, output_dir: str):
        self.logic_chains_dir = Path(logic_chains_dir)
        self.output_dir = Path(output_dir)
        self.manifest = {}  # 记录生成了什么
        
    def generate_all(self):
        """生成所有书籍的语义代码"""
        
        # 遍历所有逻辑链文件
        for yaml_file in self.logic_chains_dir.glob("*.yaml"):
            book_name = yaml_file.stem
            print(f"正在生成：{book_name}")
            
            try:
                self.generate_book(yaml_file)
                self.manifest[book_name] = {
                    "status": "success",
                    "generated_at": datetime.now().isoformat()
                }
            except Exception as e:
                print(f"生成失败：{book_name} - {e}")
                self.manifest[book_name] = {
                    "status": "failed",
                    "error": str(e)
                }
        
        # 保存清单
        self._save_manifest()
        
    def generate_book(self, yaml_file: Path):
        """生成单本书的语义代码"""
        
        # 1. 读取YAML
        with open(yaml_file, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # 2. 解析逻辑链
        snippets = self._parse_logic_chains(data)
        
        # 3. 按类别分组
        grouped = self._group_snippets(snippets)
        
        # 4. 创建输出目录
        book_dir = self.output_dir / self._to_module_name(yaml_file.stem)
        book_dir.mkdir(parents=True, exist_ok=True)
        
        # 5. 生成各子模块
        for category, category_snippets in grouped.items():
            self._generate_module(book_dir, category, category_snippets)
        
        # 6. 生成__init__.py
        self._generate_init(book_dir, grouped.keys())
        
    def _parse_logic_chains(self, data: dict) -> list:
        """解析逻辑链数据"""
        snippets = []
        
        for chain in data.get("logic_chains", []):
            snippet = {
                "id": chain.get("id"),
                "source_book": data.get("book_name"),
                "source_chapter": chain.get("chapter"),
                "source_type": self._get_source_type(data.get("book_name")),
                "factor_refs": chain.get("factors", []),
                "conditions": self._convert_conditions(chain.get("conditions", [])),
                "original_text": chain.get("original_text", ""),
                "interpretation": chain.get("interpretation", ""),
                "keywords": chain.get("keywords", []),
                "confidence": chain.get("confidence", 0.8),
                "authority": chain.get("authority", 3),
                "dimension": chain.get("dimension", "general"),
                "sentiment": chain.get("sentiment", "neutral"),
                "related_snippets": chain.get("related", []),
                "logic_chain_ref": chain.get("id")
            }
            snippets.append(snippet)
        
        return snippets
    
    def _generate_module(self, book_dir: Path, category: str, snippets: list):
        """生成一个子模块"""
        
        # 渲染模板
        template = Template(self.SNIPPET_TEMPLATE)
        code = template.render(
            generated_at=datetime.now().isoformat(),
            source_book=snippets[0]["source_book"] if snippets else "",
            snippets=snippets
        )
        
        # 写入文件
        module_file = book_dir / f"{category}.py"
        with open(module_file, 'w', encoding='utf-8') as f:
            f.write(code)
```

## 1.5 cli.py - 命令行接口

```python
# scripts/codegen/cli.py

import click
from .semantic_generator import SemanticGenerator
from .rule_generator import RuleGenerator
from .validation import CodeValidator

@click.group()
def cli():
    """LS代码生成工具"""
    pass

@cli.command()
@click.option('--type', '-t', 
              type=click.Choice(['semantic', 'rule', 'factor', 'all']),
              default='all',
              help='生成类型')
@click.option('--book', '-b', 
              help='指定书籍（可选）')
@click.option('--validate/--no-validate', 
              default=True,
              help='是否验证生成的代码')
def generate(type, book, validate):
    """
    生成代码
    
    示例：
        python -m scripts.codegen generate --type semantic
        python -m scripts.codegen generate --type rule --book 三命通会
    """
    if type == 'semantic' or type == 'all':
        generator = SemanticGenerator(
            logic_chains_dir='data/logic_chains',
            output_dir='backend/semantics'
        )
        if book:
            generator.generate_book(f'data/logic_chains/{book}.yaml')
        else:
            generator.generate_all()
    
    if type == 'rule' or type == 'all':
        generator = RuleGenerator(
            rules_dir='data/rules',
            output_dir='data/rules/generated'
        )
        generator.generate_all()
    
    # 验证
    if validate:
        validator = CodeValidator()
        results = validator.validate_all()
        if not results['success']:
            click.echo(f"验证失败：{results['errors']}")
            raise click.Abort()

@cli.command()
def rollback():
    """回滚到上一个版本"""
    from .rollback import RollbackManager
    manager = RollbackManager()
    manager.rollback()

@cli.command()
def status():
    """查看生成状态"""
    from .manifest import ManifestManager
    manager = ManifestManager()
    manager.print_status()

if __name__ == '__main__':
    cli()
```

---

# 2. scripts/logic_chain_builder/ - 逻辑链构建器

## 2.1 什么是逻辑链？

```
【概念】
逻辑链 = 从典籍提取的推理链条

【例子】
原文："甲木生于子月，水旺木相"

提取的逻辑链：
{
  前提1: 日干 = 甲木
  前提2: 月支 = 子
  推论: 水旺木相
  
  因果关系:
    子月 → 水旺
    水旺 → 木得生
    木得生 → 木相（较旺）
}
```

## 2.2 逻辑链构建流程

```
典籍结构化文本（L3层）
        ↓
┌──────────────────────────────────────────────────────────────┐
│ 1. loader.py 加载                                            │
│    读取典籍/中文典籍/三命通会/各卷L3.yaml                      │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│ 2. builder.py 构建                                           │
│    提取因子、条件、结论                                        │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│ 3. edge_inferrer.py 推断边                                   │
│    建立因子之间的关系                                          │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│ 4. clusterer.py 聚类                                         │
│    把相似的逻辑链分组                                          │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│ 5. quality_scorer.py 质量评分                                 │
│    评估每条逻辑链的可靠性                                       │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│ 6. validator.py 验证                                         │
│    检查逻辑链的完整性和正确性                                    │
└─────────────────────────┬────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────────┐
│ 7. writer.py 输出                                            │
│    写入 data/logic_chains/三命通会.yaml                       │
└──────────────────────────────────────────────────────────────┘
```

## 2.3 builder.py 详解

```python
# scripts/logic_chain_builder/builder.py

class LogicChainBuilder:
    """
    逻辑链构建器
    
    从结构化典籍文本中提取逻辑推理链
    """
    
    def __init__(self):
        self.factor_extractor = FactorExtractor()
        self.condition_parser = ConditionParser()
        
    def build(self, source_data: dict) -> List[LogicChain]:
        """
        构建逻辑链
        
        输入示例：
        {
            "chapter": "论天干·甲木",
            "paragraphs": [
                {
                    "original": "甲木生于子月，水旺木相...",
                    "factors": ["甲木", "子月"],
                    "conditions": [...],
                    "conclusion": "水旺木相"
                }
            ]
        }
        """
        chains = []
        
        for para in source_data.get("paragraphs", []):
            chain = self._build_single_chain(para, source_data)
            if chain:
                chains.append(chain)
        
        return chains
    
    def _build_single_chain(self, paragraph: dict, context: dict) -> LogicChain:
        """构建单条逻辑链"""
        
        # 1. 提取因子
        factors = self.factor_extractor.extract(paragraph.get("original", ""))
        
        # 2. 解析条件
        conditions = self.condition_parser.parse(paragraph.get("conditions", []))
        
        # 3. 提取结论
        conclusion = paragraph.get("conclusion", "")
        
        # 4. 构建链
        chain = LogicChain(
            id=self._generate_id(context, paragraph),
            source=context.get("book_name"),
            chapter=context.get("chapter"),
            
            # 前提条件
            premises=[
                Premise(factor=f, condition=c)
                for f, c in zip(factors, conditions)
            ],
            
            # 结论
            conclusion=Conclusion(
                text=conclusion,
                factors=self._extract_conclusion_factors(conclusion)
            ),
            
            # 原文
            original_text=paragraph.get("original"),
            
            # 推理步骤
            reasoning_steps=self._extract_reasoning_steps(paragraph)
        )
        
        return chain
    
    def _extract_reasoning_steps(self, paragraph: dict) -> List[str]:
        """
        提取推理步骤
        
        从 "甲木生于子月，水旺木相" 提取：
        1. 子月 → 水当令（水最旺）
        2. 水旺 → 生木
        3. 木得生 → 木相（次旺）
        """
        # 使用规则或LLM提取推理步骤
        steps = []
        
        # 简化示例
        text = paragraph.get("original", "")
        if "生于" in text and "月" in text:
            steps.append(f"月支决定月令五行")
        if "旺" in text:
            steps.append(f"月令五行旺相")
        # ... 更多规则
        
        return steps
```

## 2.4 quality_scorer.py 详解

```python
# scripts/logic_chain_builder/quality_scorer.py

class QualityScorer:
    """
    逻辑链质量评分器
    
    评分维度：
    1. 完整性：因子、条件、结论是否齐全
    2. 一致性：与其他逻辑链是否矛盾
    3. 可追溯性：是否能追溯到原文
    4. 通用性：适用范围有多广
    """
    
    def score(self, chain: LogicChain) -> QualityScore:
        """计算质量分数"""
        
        # 完整性评分 (0-25分)
        completeness = self._score_completeness(chain)
        
        # 一致性评分 (0-25分)
        consistency = self._score_consistency(chain)
        
        # 可追溯性评分 (0-25分)
        traceability = self._score_traceability(chain)
        
        # 通用性评分 (0-25分)
        generality = self._score_generality(chain)
        
        total = completeness + consistency + traceability + generality
        
        return QualityScore(
            total=total,
            completeness=completeness,
            consistency=consistency,
            traceability=traceability,
            generality=generality,
            grade=self._get_grade(total)
        )
    
    def _score_completeness(self, chain: LogicChain) -> float:
        """
        完整性评分
        
        检查项：
        - 有因子引用？
        - 有条件定义？
        - 有结论？
        - 有原文？
        """
        score = 0
        
        if chain.premises and len(chain.premises) > 0:
            score += 6
        if all(p.condition for p in chain.premises):
            score += 6
        if chain.conclusion and chain.conclusion.text:
            score += 6
        if chain.original_text:
            score += 4
        if chain.reasoning_steps:
            score += 3
        
        return min(score, 25)
    
    def _score_consistency(self, chain: LogicChain) -> float:
        """
        一致性评分
        
        检查是否与其他逻辑链矛盾
        """
        # 获取相同因子组合的其他链
        similar_chains = self._find_similar_chains(chain)
        
        if not similar_chains:
            return 20  # 没有可比较的，给基础分
        
        # 计算结论相似度
        similarities = [
            self._calculate_conclusion_similarity(chain, other)
            for other in similar_chains
        ]
        
        avg_similarity = sum(similarities) / len(similarities)
        
        # 高相似度 = 高一致性
        return avg_similarity * 25
    
    def _get_grade(self, total: float) -> str:
        """转换为等级"""
        if total >= 90:
            return "A"
        elif total >= 80:
            return "B"
        elif total >= 70:
            return "C"
        elif total >= 60:
            return "D"
        else:
            return "F"
```

---

# 3. scripts/knowledge_graph_builder/ - 知识图谱构建器

## 3.1 什么是知识图谱？

```
【概念】
知识图谱 = 把知识点用"节点"和"边"连接起来

【例子】
节点：甲木、子水、比肩、寅月...
边：
  甲木 --属于--> 天干
  甲木 --五行--> 木
  子水 --属于--> 地支
  子水 --五行--> 水
  甲木 --生于--> 子月 --结果--> 水旺木相
```

## 3.2 知识图谱构建流程

```python
# scripts/knowledge_graph_builder/cli.py

"""
知识图谱构建命令行工具

使用：
  python -m scripts.knowledge_graph_builder build --source sanming
  python -m scripts.knowledge_graph_builder query "甲木"
  python -m scripts.knowledge_graph_builder export --format neo4j
"""

@click.command()
@click.option('--source', help='数据源（书籍名）')
def build(source):
    """构建知识图谱"""
    
    # 1. 加载逻辑链
    chains = load_logic_chains(source)
    
    # 2. 提取节点
    nodes = extract_nodes(chains)
    # 节点类型：因子、概念、书籍、章节
    
    # 3. 提取边
    edges = extract_edges(chains)
    # 边类型：属于、生克、合化、同出
    
    # 4. 构建图
    graph = KnowledgeGraph(nodes, edges)
    
    # 5. 计算属性
    graph.compute_pagerank()      # 重要性
    graph.compute_communities()   # 社区发现
    
    # 6. 保存
    graph.save(f"data/knowledge_graph/exports/{source}.json")
```

## 3.3 知识图谱数据结构

```yaml
# data/knowledge_graph/exports/bazi_graph.json

{
  "nodes": [
    {
      "id": "factor_jiamu",
      "label": "甲木",
      "type": "factor",
      "properties": {
        "category": "天干",
        "wuxing": "木",
        "yinyang": "阳",
        "pagerank": 0.0234,
        "community": 1
      }
    },
    {
      "id": "factor_zishui",
      "label": "子水",
      "type": "factor",
      "properties": {
        "category": "地支",
        "wuxing": "水",
        "yinyang": "阳",
        "pagerank": 0.0189,
        "community": 2
      }
    }
  ],
  
  "edges": [
    {
      "source": "factor_zishui",
      "target": "factor_jiamu",
      "type": "sheng",           # 水生木
      "properties": {
        "strength": 1.0,
        "source_book": "三命通会"
      }
    },
    {
      "source": "factor_jiamu",
      "target": "concept_muxiang",
      "type": "result",          # 结果
      "properties": {
        "condition": "生于子月",
        "confidence": 0.85
      }
    }
  ]
}
```

---

# 4. data/ - 数据目录详解

## 4.1 data/rules/ - 规则数据

### 4.1.1 规则文件结构

```yaml
# data/rules/bazi/ten_gods.yaml

# 文件头信息
meta:
  name: 十神规则集
  version: 2.1.0
  engine: bazi                    # 所属引擎
  last_updated: 2024-01-15
  
# 规则列表
rules:
  - id: bazi_ten_god_001
    name: 比肩旺相
    priority: 80
    conditions:
      - type: ten_god_exists
        value: 比肩
      - type: ten_god_strength
        value: 旺
    output:
      interpretation: "比肩旺相者..."
      dimension: 性格
      keywords: [独立, 主见]
    semantic_refs:
      - sanming_bijian_001
```

### 4.1.2 generated/ 目录说明

```
data/rules/generated/
├── bazi_sanming.yaml      # 从三命通会生成的规则
├── bazi_ziping.yaml       # 从子平真诠生成的规则
├── astro_planets.yaml     # 从行星过境生成的规则
└── ...

⚠️ 注意：这个目录的文件是自动生成的
         手动修改会在下次生成时被覆盖！
```

## 4.2 data/factor_ontology/ - 因子本体

### 4.2.1 什么是因子本体？

```
【概念】
因子本体 = 定义"因子是什么"的标准文件

【例子】
定义"甲木"这个因子：
{
  id: "stem_jia",
  name: "甲",
  category: "天干",
  properties: {
    wuxing: "木",
    yinyang: "阳",
    position: 1
  },
  relations: {
    合: "己",          # 甲己合
    冲: null,          # 天干无冲
    生: ["丙", "丁"],  # 木生火
    克: ["戊", "己"]   # 木克土
  }
}
```

### 4.2.2 目录结构

```
data/factor_ontology/
├── namespace.yaml           # 命名空间定义
├── factor_schema.yaml       # 因子Schema
│
├── candidates/              # 候选因子（待审核）
│   ├── bazi.yaml
│   ├── astro.yaml
│   └── ...
│
└── certified/               # 已认证因子（正式使用）
    ├── bazi.yaml
    ├── astro.yaml
    └── ...
```

### 4.2.3 审核流程

```
新因子定义
    ↓
放入 candidates/
    ↓
人工审核
    ├── 检查定义是否完整
    ├── 检查与现有因子是否冲突
    └── 检查引用是否正确
    ↓
审核通过
    ↓
移动到 certified/
    ↓
被代码使用
```

## 4.3 data/logic_chains/ - 逻辑链数据

### 4.3.1 文件内容示例

```yaml
# data/logic_chains/三命通会.yaml (26MB)

book_name: 三命通会
author: 万民英
dynasty: 明
total_chains: 6789

logic_chains:
  - id: sanming_lc_001
    chapter: 卷二·论天干
    section: 甲木
    
    # 前提条件
    premises:
      - factor: 甲木
        role: 日主
      - factor: 子
        role: 月支
    
    # 推理步骤
    reasoning:
      - step: 1
        from: 月支子
        to: 水当令
        relation: 月令五行
      - step: 2
        from: 水当令
        to: 水旺
        relation: 当令则旺
      - step: 3
        from: [甲木日主, 水旺]
        to: 木得生
        relation: 水生木
    
    # 结论
    conclusion:
      text: 甲木生于子月，水旺木相
      factors: [木相]
      dimension: 基础
    
    # 原文
    original_text: |
      甲木生于子月，水旺木相，得生扶之力。
      若八字中有火暖局，则木得水生而不寒。
    
    # 元数据
    confidence: 0.85
    quality_score: 82
    related_chains: [sanming_lc_002, sanming_lc_003]
```

## 4.4 data/scenario_templates/ - 场景模板

### 4.4.1 模板作用

```
用户问"我的事业怎么样？"
    ↓
场景识别 → career
    ↓
加载 career.yaml 模板
    ↓
根据模板决定：
  - 重点看哪些维度
  - 使用哪些引擎
  - 生成什么样的回答
```

### 4.4.2 模板内容示例

```yaml
# data/scenario_templates/career.yaml

name: 事业场景
description: 用于回答事业、工作相关问题

# 需要的引擎
engines:
  required:
    - bazi                # 八字必须
    - ziwei               # 紫微必须
  optional:
    - astro               # 占星可选

# 重点维度
focus_dimensions:
  - 官运                  # 升职、管理
  - 财运                  # 收入、财务
  - 事业                  # 工作状态
  - 人际                  # 同事、上司

# 规则筛选
rules_filter:
  dimensions:
    - 事业
    - 官运
    - 财运
  priority_min: 60

# 语义片段筛选
snippet_filter:
  keywords:
    - 工作
    - 事业
    - 职业
    - 官
    - 财

# 输出格式
output_format:
  sections:
    - name: 事业总体运势
      source: integration
    - name: 今年事业重点
      source: timeline
    - name: 职业发展建议
      source: action_compiler
  
  # 必须包含的内容
  must_include:
    - 当前运势概述
    - 有利时机提示
    - 注意事项
    - 行动建议
```

---

# 5. 数据处理完整流程

## 5.1 从典籍到用户的完整数据流

```
┌─────────────────────────────────────────────────────────────────┐
│                        第一阶段：人工处理                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  原始典籍PDF/图片                                                 │
│        ↓                                                         │
│  人工录入 + OCR校对                                               │
│        ↓                                                         │
│  典籍/中文典籍/三命通会/原文.txt  (L1层：精校原文)                 │
│        ↓                                                         │
│  人工结构化标注                                                   │
│        ↓                                                         │
│  典籍/中文典籍/三命通会/卷二_L3.yaml  (L3层：结构化)               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                        第二阶段：自动处理                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  scripts/logic_chain_builder/                                    │
│        ↓                                                         │
│  data/logic_chains/三命通会.yaml  (逻辑链)                        │
│        ↓                                                         │
│  scripts/codegen/                                                │
│        ↓                                                         │
│  backend/semantics/sanming/  (Python代码)                        │
│        ↓                                                         │
│  scripts/rule_converter/                                         │
│        ↓                                                         │
│  data/rules/generated/bazi_sanming.yaml  (规则文件)              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────┐
│                        第三阶段：运行时                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  用户输入生日                                                     │
│        ↓                                                         │
│  backend/calculators/bazi/  计算八字                             │
│        ↓                                                         │
│  backend/rules/engine.py  匹配规则                               │
│        ↓                                                         │
│  backend/semantics/sanming/  获取语义片段                        │
│        ↓                                                         │
│  backend/integration/  融合结果                                  │
│        ↓                                                         │
│  backend/services/narrative/  生成文字                           │
│        ↓                                                         │
│  返回给用户                                                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## 5.2 各环节数据量统计

| 阶段 | 数据项 | 数量 | 大小 |
|------|--------|------|------|
| 原始典籍 | 书籍 | 30+ | - |
| L3结构化 | 文件 | 200+ | ~5MB |
| 逻辑链 | 条目 | 50000+ | ~70MB |
| 语义片段 | Python模块 | 3000+ | ~10MB |
| 规则 | YAML条目 | 10000+ | ~5MB |
| 运行时匹配 | 每次请求 | 10-50条 | - |
