# QUALITY_GATES（质量门禁）

每条门禁包含：指标/命令/判定标准/失败阻断策略。

## Gate-0（基础）
- 指标：身份隔离/安全/版本/生产默认值/可观测基线齐备。
- 命令：`openspec validate --specs --strict --no-interactive`
- 判定：Gate-0 相关 specs 通过严格校验；关键任务达到发布要求（按各 spec `tasks.md`）。
- 阻断：失败则阻断任何对外发布/晋级。

## Gate-1（语义可靠性）
- 指标：证据链与引用可审计；语义层契约稳定；抽取质量门禁与回归基线定义完备。
- 命令：`openspec validate --specs --strict --no-interactive` + `openspec list --specs`
- 判定：Gate-1 相关 specs 的验收口径明确且可执行。
- 阻断：失败则阻断语义/语料晋级与对外解释输出。

## Gate-2（工程与运行就绪）
- 指标：端到端契约与交接校验明确；发布/回滚与运行手册齐备；关键路径可观测。
- 命令：`openspec validate --specs --strict --no-interactive` + `openspec list --changes`
- 判定：Gate-2 相关 specs 的门禁阻断策略与运维定位口径明确。
- 阻断：失败则阻断部署晋级与规模化流量。

## Gate-3（商业化就绪）
- 指标：权益/计费与商业就绪门禁完备；审批链与支持体系有证据产物。
- 命令：`openspec validate --specs --strict --no-interactive`
- 判定：商业化相关 specs 的验收口径明确且可审计。
- 阻断：失败则阻断对客户开放与商业发布。

## 资产门禁（资产层）
- 指标：许可/血缘/QA/冲突处置可追溯；失败样本与例外审批可审计。
- 命令：`openspec validate --specs --strict --no-interactive`（资产层附加验证按各 spec `acceptance.md`）。
- 判定：资产层相关 specs 的验收口径明确且可执行。
- 阻断：失败则阻断语料发布与依赖该资产的用户可见输出。
