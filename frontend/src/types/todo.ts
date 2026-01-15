/**
 * TODO 类型定义
 * 
 * 对照后端契约: backend/core/contracts/todo_models.py
 * 对照文档: .kiro/docs/api_contracts.md §3.3
 */

export type TodoType = "todo" | "done";
export type TodoStatus = "pending" | "completed" | "cancelled";

// ==================== 常量 ====================

export const TODO_CONTENT_MAX_LENGTH = 100;
export const TODO_DAILY_LIMIT = 50;

// ==================== 实体类型 ====================

export interface TodoEntry {
  todo_id: string;
  user_id: string;
  content: string;
  entry_type: TodoType;
  status: TodoStatus;
  created_at: string;
  completed_at?: string;
  extracted_intent?: Record<string, unknown>;
  linked_insight_id?: string;
}

// ==================== 请求类型 ====================

export interface TodoCreateRequest {
  content: string;
  entry_type: TodoType;
}

export interface TodoUpdateRequest {
  content?: string;
  status?: TodoStatus;
}

export interface TodoListParams {
  date?: string;           // YYYY-MM-DD，默认今天
  entry_type?: TodoType;
  status?: TodoStatus;
  limit?: number;          // 默认 50
  offset?: number;
}

// ==================== 响应类型 ====================

export interface TodoListResponse {
  entries: TodoEntry[];
  total: number;
  has_more: boolean;
}

export interface TodoDailySummary {
  user_id: string;
  date: string;
  total_count: number;
  todo_count: number;
  done_count: number;
  completed_count: number;
  entries: TodoEntry[];
}

// ==================== 辅助函数 ====================

/**
 * 校验 TODO 内容长度
 */
export function validateTodoContent(content: string): boolean {
  const trimmed = content.trim();
  return trimmed.length >= 1 && trimmed.length <= TODO_CONTENT_MAX_LENGTH;
}

/**
 * 获取内容长度信息
 */
export function getContentLengthInfo(content: string): {
  current: number;
  max: number;
  remaining: number;
  isValid: boolean;
} {
  const current = content.trim().length;
  return {
    current,
    max: TODO_CONTENT_MAX_LENGTH,
    remaining: TODO_CONTENT_MAX_LENGTH - current,
    isValid: current >= 1 && current <= TODO_CONTENT_MAX_LENGTH,
  };
}
