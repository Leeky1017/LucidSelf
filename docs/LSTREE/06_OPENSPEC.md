# OpenSpec 变更管理详细结构

## 目录总览

```
openspec/
├── AGENTS.md             # AI助手指令 (29KB)
├── project.md            # 项目总体设计 (52KB)
├── specs/                # 技术规范
├── changes/              # 变更提案
└── notes/                # 笔记
```

---

## 1. 核心文档

### AGENTS.md - AI助手指令
- OpenSpec工作流程
- 变更提案格式
- 代码规范
- 测试要求

### project.md - 项目总体设计
- 系统架构
- 模块依赖
- 数据流
- 技术决策

---

## 2. specs/ - 技术规范

各核心模块的技术规范

```
specs/
├── bazi-engine/              # 八字引擎规范
│   └── spec.md
│
├── western-astro-engine/     # 西占引擎规范
│   └── spec.md
│
├── dream-engine/             # 解梦引擎规范
│   └── spec.md
│
├── inference-engine/         # 推理引擎规范
│   └── spec.md
│
├── llm-core/                 # LLM核心规范
│   └── spec.md
│
├── schema-core/              # Schema核心规范
│   └── spec.md
│
└── classic-texts-engine/     # 典籍引擎规范
    └── spec.md
```

### 规范内容结构
每个spec.md包含:
1. **目标** - 模块目标与边界
2. **接口** - API契约
3. **数据模型** - 核心数据结构
4. **依赖** - 模块依赖关系
5. **约束** - 设计约束
6. **测试** - 测试策略

---

## 3. changes/ - 变更提案

```
changes/
├── add-geocoding-service/    # 当前活跃变更
│   ├── change.md             # 变更描述
│   └── tasks.md              # 任务清单
│
└── archive/                  # 已归档变更 (17个)
    ├── fix-bazi-calculator/
    ├── add-llm-router/
    ├── implement-rules-engine/
    └── ...
```

### 变更提案格式
```markdown
# Change: [变更名称]

## 状态
- [ ] 提案
- [ ] 设计审核
- [ ] 实现中
- [ ] 测试
- [ ] 部署
- [ ] 归档

## 目标
[变更目标描述]

## 影响范围
- 模块: [受影响模块列表]
- API: [API变更]
- 数据: [数据变更]

## 实现计划
[具体步骤]

## 测试计划
[测试策略]

## 回滚计划
[回滚步骤]
```

---

## 4. 变更工作流

```
┌─────────────┐
│   提案      │ ← /openspec-proposal
├─────────────┤
│   审核      │ ← 技术评审
├─────────────┤
│   批准      │ ← 变更批准
├─────────────┤
│   实现      │ ← /openspec-apply
├─────────────┤
│   测试      │ ← 验证测试
├─────────────┤
│   部署      │ ← 生产部署
├─────────────┤
│   归档      │ ← /openspec-archive
└─────────────┘
```

---

## 5. Windsurf工作流

### /openspec-proposal
创建新变更提案:
1. 验证变更合理性
2. 检查spec冲突
3. 生成change.md和tasks.md
4. 更新project.md

### /openspec-apply
实现已批准变更:
1. 读取tasks.md
2. 按步骤实现
3. 更新任务状态
4. 运行测试

### /openspec-archive
归档已完成变更:
1. 验证所有任务完成
2. 更新specs/
3. 移动到archive/
4. 更新project.md

---

## 6. notes/ - 笔记

```
notes/
└── design_decisions.md   # 设计决策记录
```

记录重要设计决策:
- 技术选型
- 架构权衡
- 废弃方案

---

## 7. 规范管理原则

1. **单一来源**: 每个模块一个spec
2. **向后兼容**: API变更需兼容
3. **可追溯**: 所有变更有记录
4. **可测试**: 规范必须可验证
5. **可回滚**: 变更可以撤销
