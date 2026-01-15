"use client";

import {
  createContext,
  useContext,
  useState,
  useEffect,
  useCallback,
  type ReactNode,
} from "react";
import type { AuthState, UserInfo, TokenPair } from "@/types/auth";
import { authApi, getStoredToken, clearStoredToken } from "@/lib/authApi";

interface AuthContextType extends AuthState {
  login: (email: string, password: string) => Promise<void>;
  signup: (email: string, password: string, name?: string) => Promise<void>;
  logout: () => Promise<void>;
  refreshToken: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<AuthState>({
    isAuthenticated: false,
    isLoading: true,
    user: null,
    token: null,
  });

  // 初始化：检查是否已登录
  useEffect(() => {
    const initAuth = async () => {
      const storedToken = getStoredToken();
      if (storedToken) {
        try {
          const user = await authApi.me();
          setState({
            isAuthenticated: true,
            isLoading: false,
            user,
            token: null, // token 存在 localStorage
          });
        } catch (err) {
          // Token 无效，清除
          clearStoredToken();
          setState({
            isAuthenticated: false,
            isLoading: false,
            user: null,
            token: null,
          });
        }
      } else {
        setState((prev) => ({ ...prev, isLoading: false }));
      }
    };

    initAuth();
  }, []);

  const login = useCallback(async (email: string, password: string) => {
    setState((prev) => ({ ...prev, isLoading: true }));
    try {
      const tokenPair = await authApi.emailLogin({ email, password });
      const user = await authApi.me();
      setState({
        isAuthenticated: true,
        isLoading: false,
        user,
        token: tokenPair,
      });
    } catch (err) {
      setState((prev) => ({ ...prev, isLoading: false }));
      throw err;
    }
  }, []);

  const signup = useCallback(
    async (email: string, password: string, name?: string) => {
      setState((prev) => ({ ...prev, isLoading: true }));
      try {
        const tokenPair = await authApi.emailSignup({ email, password, name });
        const user = await authApi.me();
        setState({
          isAuthenticated: true,
          isLoading: false,
          user,
          token: tokenPair,
        });
      } catch (err) {
        setState((prev) => ({ ...prev, isLoading: false }));
        throw err;
      }
    },
    []
  );

  const logout = useCallback(async () => {
    try {
      await authApi.logout();
    } catch (err) {
      console.error("Logout error:", err);
    } finally {
      setState({
        isAuthenticated: false,
        isLoading: false,
        user: null,
        token: null,
      });
    }
  }, []);

  const refreshToken = useCallback(async () => {
    try {
      const tokenPair = await authApi.refresh();
      setState((prev) => ({ ...prev, token: tokenPair }));
    } catch (err) {
      // 刷新失败，登出
      await logout();
      throw err;
    }
  }, [logout]);

  return (
    <AuthContext.Provider
      value={{
        ...state,
        login,
        signup,
        logout,
        refreshToken,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
