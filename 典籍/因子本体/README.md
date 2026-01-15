# 因子本体 (Factor Ontology)

> **版本**: 1.0 | **创建日期**: 2024-12-04

## 目录结构

```
因子本体/
├── bazi/           # 八字体系因子
├── ziwei/          # 紫微体系因子
├── astro/          # 占星体系因子
├── dream/          # 梦境体系因子
├── yijing/         # 周易体系因子
├── tarot/          # 塔罗体系因子
└── cross_system/   # 跨体系中立因子
```

## 因子分类

每个体系目录包含以下类别文件:
- `structure.yaml` - 结构类因子
- `state.yaml` - 状态类因子  
- `relation.yaml` - 关系类因子
- `temporal.yaml` - 时间类因子
- `energy.yaml` - 能量/情绪类因子

## 命名规范

**格式**: `[system_]category_name`

**约束**:
- 全小写字母
- 下划线分隔
- 纯英文（禁止中文/拼音）
- 语义清晰

**前缀**:
- `bazi_` - 八字专属
- `ziwei_` - 紫微专属
- `astro_` - 占星专属
- `dream_` - 梦境专属
- `yijing_` - 周易专属
- `tarot_` - 塔罗专属
- 无前缀 - 通用基础因子

## 因子状态

| 状态 | 定义 |
|------|------|
| existing | 已正式入库，可被规则引用 |
| new_candidate | 候选因子，仅在精校文档中标注 |

## 使用方式

1. **查询因子**: 按体系目录查找对应YAML文件
2. **新增因子**: 提交因子变更提案 (`openspec/changes/add-factors-*`)
3. **升级状态**: 通过评审后从 `new_candidate` 升级为 `existing`

## 关联文档

- 命名空间规范: `data/factor_ontology/namespace.yaml`
- 因子Schema: `data/factor_ontology/factor_schema.yaml`
- 总览文档: `典籍/因子本体_总览_v1.md`
