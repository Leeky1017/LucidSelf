/**
 * TODO API 客户端
 * 
 * 对照文档: .kiro/docs/api_contracts.md §3.3
 */

import type {
  TodoEntry,
  TodoCreateRequest,
  TodoUpdateRequest,
  TodoListResponse,
  TodoListParams,
  TodoDailySummary,
} from "@/types/todo";
import { getStoredToken } from "./authApi";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

// ==================== HTTP 辅助 ====================

async function request<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const url = `${API_BASE}${endpoint}`;
  const token = getStoredToken();

  const response = await fetch(url, {
    ...options,
    headers: {
      "Content-Type": "application/json",
      ...(token && { Authorization: `Bearer ${token}` }),
      ...options.headers,
    },
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: response.statusText }));
    throw new Error(error.detail || error.error?.message || `Request failed: ${response.status}`);
  }

  return response.json();
}

function buildQueryString(params?: Record<string, string | number | undefined>): string {
  if (!params) return "";
  const searchParams = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined) {
      searchParams.append(key, String(value));
    }
  });
  const queryString = searchParams.toString();
  return queryString ? `?${queryString}` : "";
}

// ==================== API 方法 ====================

export const todoApi = {
  /**
   * 创建 TODO 条目
   */
  create: (data: TodoCreateRequest): Promise<TodoEntry> =>
    request("/api/v1/todo", {
      method: "POST",
      body: JSON.stringify(data),
    }),

  /**
   * 获取 TODO 列表
   */
  list: (params?: TodoListParams): Promise<TodoListResponse> =>
    request(`/api/v1/todo${buildQueryString(params as Record<string, string | number | undefined>)}`, {
      method: "GET",
    }),

  /**
   * 获取单条 TODO
   */
  get: (todoId: string): Promise<TodoEntry> =>
    request(`/api/v1/todo/${todoId}`, { method: "GET" }),

  /**
   * 更新 TODO
   */
  update: (todoId: string, data: TodoUpdateRequest): Promise<TodoEntry> =>
    request(`/api/v1/todo/${todoId}`, {
      method: "PATCH",
      body: JSON.stringify(data),
    }),

  /**
   * 删除 TODO
   */
  delete: (todoId: string): Promise<{ success: boolean }> =>
    request(`/api/v1/todo/${todoId}`, { method: "DELETE" }),

  /**
   * 获取每日汇总
   */
  getSummary: (date?: string): Promise<TodoDailySummary> =>
    request(`/api/v1/todo/summary${buildQueryString({ date })}`, { method: "GET" }),

  /**
   * 快速创建 TODO
   */
  quickTodo: (content: string): Promise<TodoEntry> =>
    todoApi.create({ content, entry_type: "todo" }),

  /**
   * 快速创建 DONE
   */
  quickDone: (content: string): Promise<TodoEntry> =>
    todoApi.create({ content, entry_type: "done" }),

  /**
   * 标记为完成
   */
  complete: (todoId: string): Promise<TodoEntry> =>
    todoApi.update(todoId, { status: "completed" }),

  /**
   * 标记为取消
   */
  cancel: (todoId: string): Promise<TodoEntry> =>
    todoApi.update(todoId, { status: "cancelled" }),
};

export default todoApi;
