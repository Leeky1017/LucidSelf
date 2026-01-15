/**
 * 认证 API 客户端
 * 
 * 对照文档: .kiro/docs/api_contracts.md §3.1
 */

import type {
  AppleSignInRequest,
  GoogleSignInRequest,
  EmailSignupRequest,
  EmailLoginRequest,
  EmailVerifyRequest,
  TokenPair,
  UserInfo,
} from "@/types/auth";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

// ==================== Token 管理 ====================

const TOKEN_STORAGE_KEY = "ls_auth_token";
const REFRESH_TOKEN_KEY = "ls_refresh_token";

export function getStoredToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(TOKEN_STORAGE_KEY);
}

export function setStoredToken(token: TokenPair): void {
  if (typeof window === "undefined") return;
  localStorage.setItem(TOKEN_STORAGE_KEY, token.access_token);
  localStorage.setItem(REFRESH_TOKEN_KEY, token.refresh_token);
}

export function clearStoredToken(): void {
  if (typeof window === "undefined") return;
  localStorage.removeItem(TOKEN_STORAGE_KEY);
  localStorage.removeItem(REFRESH_TOKEN_KEY);
}

// ==================== HTTP 辅助 ====================

async function authRequest<T>(
  endpoint: string,
  options: RequestInit = {},
  isRetry = false
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
    const detail = error.detail;
    
    // Token 过期或无效时的处理
    if (response.status === 401 && !isRetry) {
      const refreshToken = typeof window !== "undefined" 
        ? localStorage.getItem(REFRESH_TOKEN_KEY) 
        : null;
      
      if (refreshToken && !endpoint.includes("/refresh")) {
        // 尝试刷新 Token
        try {
          const refreshResponse = await fetch(`${API_BASE}/api/v1/auth/refresh`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ refresh_token: refreshToken }),
          });
          
          if (refreshResponse.ok) {
            const newTokens = await refreshResponse.json();
            setStoredToken(newTokens);
            // 重试原请求
            return authRequest<T>(endpoint, options, true);
          }
        } catch {
          // 刷新失败，清除 Token
        }
      }
      
      // 刷新失败或无刷新 Token，清除并静默处理
      clearStoredToken();
      // 不抛出错误，让用户以游客身份继续
      console.warn("Token expired, continuing as guest");
    }
    
    const message = typeof detail === 'object' && detail !== null 
      ? detail.message || detail.code || JSON.stringify(detail)
      : detail || error.error?.message || `Request failed: ${response.status}`;
    throw new Error(message);
  }

  return response.json();
}

function post<T>(endpoint: string, data: unknown): Promise<T> {
  return authRequest<T>(endpoint, {
    method: "POST",
    body: JSON.stringify(data),
  });
}

function get<T>(endpoint: string): Promise<T> {
  return authRequest<T>(endpoint, { method: "GET" });
}

// ==================== API 方法 ====================

export const authApi = {
  /**
   * Apple Sign-In
   */
  appleSignIn: async (data: AppleSignInRequest): Promise<TokenPair> => {
    const result = await post<TokenPair>("/api/v1/auth/apple", data);
    setStoredToken(result);
    return result;
  },

  /**
   * Google Sign-In
   */
  googleSignIn: async (data: GoogleSignInRequest): Promise<TokenPair> => {
    const result = await post<TokenPair>("/api/v1/auth/google", data);
    setStoredToken(result);
    return result;
  },

  /**
   * 邮箱注册
   */
  emailSignup: async (data: EmailSignupRequest): Promise<TokenPair> => {
    const result = await post<TokenPair>("/api/v1/auth/email/signup", data);
    setStoredToken(result);
    return result;
  },

  /**
   * 邮箱登录
   */
  emailLogin: async (data: EmailLoginRequest): Promise<TokenPair> => {
    const result = await post<TokenPair>("/api/v1/auth/email/login", data);
    setStoredToken(result);
    return result;
  },

  /**
   * 邮箱验证
   */
  emailVerify: (data: EmailVerifyRequest): Promise<{ success: boolean }> =>
    post("/api/v1/auth/email/verify", data),

  /**
   * 刷新 Token
   */
  refresh: async (): Promise<TokenPair> => {
    const refreshToken = typeof window !== "undefined" 
      ? localStorage.getItem(REFRESH_TOKEN_KEY) 
      : null;
    
    if (!refreshToken) {
      throw new Error("No refresh token available");
    }

    const result = await post<TokenPair>("/api/v1/auth/refresh", {
      refresh_token: refreshToken,
    });
    setStoredToken(result);
    return result;
  },

  /**
   * 登出
   */
  logout: async (): Promise<void> => {
    try {
      await post("/api/v1/auth/logout", {});
    } finally {
      clearStoredToken();
    }
  },

  /**
   * 获取当前用户信息
   */
  me: (): Promise<UserInfo> => get("/api/v1/auth/me"),

  /**
   * 检查是否已登录
   */
  isLoggedIn: (): boolean => {
    return getStoredToken() !== null;
  },
};

export default authApi;
