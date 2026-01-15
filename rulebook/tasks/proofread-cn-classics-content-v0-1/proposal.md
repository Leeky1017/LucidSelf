# Proposal: proofread-cn-classics-content-v0-1

## Why
中文典籍“编辑/规范化”资产存在卷级结构不完整（缺 L2 或缺因子层），且模板引用口径不一致，无法作为可稳定复用的精校资产进入发布与后续工程抽象。

## What Changes
- 建立并执行 OpenSpec change：`openspec/changes/proofread-cn-classics-content-v0-1/`
- 固化中文典籍逐卷推进顺序（不含记纂渊海），按卷补齐 L2 + 因子层并对齐模板 V0.1
- 优先补齐《梦林玄解》中缺失 L2/因子层的卷
- 必要时修正文档内“精校依据/模板版本”引用到 `典籍/精校模板_L1L2.md`（V0.1）

## Impact
- Affected specs: `openspec/specs/proofreading-workflow-qa/*`
- Affected code: NONE (本任务以内容资产修改为主)
- Breaking change: NO
- User benefit: 中文典籍精校资产结构完整、口径统一、可审计可复现，避免“卷级缺口”进入下游
