/**
 * 订阅 API 客户端
 * 
 * 对照文档: .kiro/docs/api_contracts.md §3.2
 */

import type {
  SubscriptionStatus,
  AppleReceiptRequest,
  GooglePurchaseRequest,
  VerifyResponse,
  PlanInfo,
} from "@/types/subscription";
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

// ==================== API 方法 ====================

export const subscriptionApi = {
  /**
   * 获取订阅状态
   */
  getStatus: (): Promise<SubscriptionStatus> =>
    request("/api/v1/subscription", { method: "GET" }),

  /**
   * 验证 Apple 收据
   */
  verifyApple: (data: AppleReceiptRequest): Promise<VerifyResponse> =>
    request("/api/v1/subscription/verify/apple", {
      method: "POST",
      body: JSON.stringify(data),
    }),

  /**
   * 验证 Google 购买
   */
  verifyGoogle: (data: GooglePurchaseRequest): Promise<VerifyResponse> =>
    request("/api/v1/subscription/verify/google", {
      method: "POST",
      body: JSON.stringify(data),
    }),

  /**
   * 取消订阅
   */
  cancel: (): Promise<{ success: boolean }> =>
    request("/api/v1/subscription/cancel", { method: "POST" }),

  /**
   * 获取套餐列表
   */
  getPlans: (): Promise<PlanInfo[]> =>
    request("/api/v1/subscription/plans", { method: "GET" }),

  /**
   * 检查是否为 Plus 会员
   */
  isPlusMember: async (): Promise<boolean> => {
    try {
      const status = await subscriptionApi.getStatus();
      return status.tier === "plus" && status.status === "active";
    } catch {
      return false;
    }
  },

  /**
   * 检查功能是否可用
   */
  canUseFeature: async (feature: keyof SubscriptionStatus["limits"]): Promise<boolean> => {
    try {
      const status = await subscriptionApi.getStatus();
      const value = status.limits[feature];
      if (typeof value === "boolean") return value;
      if (typeof value === "number") return value !== 0;
      return false;
    } catch {
      return false;
    }
  },
};

export default subscriptionApi;
