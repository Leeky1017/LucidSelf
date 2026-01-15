/**
 * 认证类型定义
 * 
 * 对照后端契约: backend/core/contracts/auth_models.py
 * 对照文档: .kiro/docs/api_contracts.md §3.1
 */

export type AuthProvider = "apple" | "google" | "email";

// ==================== 请求类型 ====================

export interface AppleSignInRequest {
  identity_token: string;
  authorization_code: string;
  user_info?: {
    email?: string;
    name?: string;
  };
}

export interface GoogleSignInRequest {
  id_token: string;
  access_token?: string;
}

export interface EmailSignupRequest {
  email: string;
  password: string;
  name?: string;
}

export interface EmailLoginRequest {
  email: string;
  password: string;
}

export interface EmailVerifyRequest {
  email: string;
  code: string;
}

export interface RefreshTokenRequest {
  refresh_token: string;
}

// ==================== 响应类型 ====================

export interface TokenPair {
  access_token: string;
  refresh_token: string;
  token_type: "Bearer";
  expires_in: number;
}

export interface UserInfo {
  user_id: string;
  email?: string;
  name?: string;
  provider: AuthProvider;
  tier: "free" | "plus";
  created_at: string;
}

// ==================== 状态类型 ====================

export interface AuthState {
  isAuthenticated: boolean;
  isLoading: boolean;
  user: UserInfo | null;
  token: TokenPair | null;
}

// ==================== 错误类型 ====================

export interface AuthError {
  code: string;
  message: string;
}

export const AUTH_ERROR_CODES = {
  INVALID_TOKEN: "AUTH_INVALID_TOKEN",
  TOKEN_EXPIRED: "AUTH_TOKEN_EXPIRED",
  INVALID_CREDENTIALS: "AUTH_INVALID_CREDENTIALS",
  EMAIL_NOT_VERIFIED: "AUTH_EMAIL_NOT_VERIFIED",
  USER_NOT_FOUND: "AUTH_USER_NOT_FOUND",
  EMAIL_ALREADY_EXISTS: "AUTH_EMAIL_ALREADY_EXISTS",
} as const;
