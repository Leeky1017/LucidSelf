export type View =
  | "now"            // 执行层 - 当下掌控
  | "life-version"   // 战略层 - 人生版本蓝图
  | "timeline"       // 数据流层 - 时空轨迹
  | "insight"        // 分析层 - 深层洞察 (原Archive)
  | "dream"          // 子模块 - 梦境日记
  | "playbook"       // 子模块 - 人生攻略
  | "todo"           // 子模块 - 今日待办
  | "journal"        // 预留
  | "insights"       // 兼容旧路由
  | "archive"        // 兼容旧路由 -> insight
  | "version-tree";  // 兼容旧路由 -> life-version

export type Theme = "light" | "dark";

// 重新导出类型以便统一引用
export type { AuthProvider } from "./auth";
export type { MembershipTier, SubscriptionStatusType } from "./subscription";
export type { TodoType, TodoStatus } from "./todo";
