/**
 * 订阅类型定义
 * 
 * 对照后端契约: backend/core/contracts/subscription_models.py
 * 对照文档: .kiro/docs/api_contracts.md §3.2
 */

export type MembershipTier = "free" | "plus";
export type SubscriptionProvider = "apple" | "google" | "stripe";
export type SubscriptionStatusType = "active" | "cancelled" | "expired" | "grace_period";

// ==================== 限制配置 ====================

export interface TierLimits {
  daily_dreams: number;           // -1 表示无限
  daily_readings: number;         // -1 表示无限
  history_retention_days: number; // -1 表示永久
  advanced_engines: boolean;
  export_enabled: boolean;
  batch_enabled: boolean;
}

// ==================== 响应类型 ====================

export interface SubscriptionStatus {
  tier: MembershipTier;
  status: SubscriptionStatusType;
  provider?: SubscriptionProvider;
  expires_at?: string;
  auto_renew: boolean;
  limits: TierLimits;
}

export interface PlanInfo {
  plan_id: string;
  name: string;
  tier: MembershipTier;
  price: number;
  currency: string;
  period: "monthly" | "yearly";
  features: string[];
}

// ==================== 请求类型 ====================

export interface AppleReceiptRequest {
  receipt_data: string;
  transaction_id?: string;
}

export interface GooglePurchaseRequest {
  purchase_token: string;
  product_id: string;
}

// ==================== 验证响应 ====================

export interface VerifyResponse {
  success: boolean;
  tier: MembershipTier;
  expires_at?: string;
  error?: string;
}

// ==================== 常量 ====================

export const TIER_LIMITS: Record<MembershipTier, TierLimits> = {
  free: {
    daily_dreams: 3,
    daily_readings: 5,
    history_retention_days: 30,
    advanced_engines: false,
    export_enabled: false,
    batch_enabled: false,
  },
  plus: {
    daily_dreams: -1,
    daily_readings: -1,
    history_retention_days: -1,
    advanced_engines: true,
    export_enabled: true,
    batch_enabled: true,
  },
};
