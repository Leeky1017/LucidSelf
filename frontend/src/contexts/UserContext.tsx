"use client";

import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";
import { getStoredToken, clearStoredToken, authApi } from "@/lib/authApi";
import { api } from "@/lib/api";

export type SexAtBirth = "male" | "female";

export interface BirthData {
  year: number;
  month: number;
  day: number;
  hour: number;
  minute: number;
  sexAtBirth?: SexAtBirth;  // 出生性别（命理计算必需）
  city?: string;
  latitude?: number;
  longitude?: number;
  timezone?: string;
}

export interface UserProfile {
  userId: string;
  name: string;
  email?: string;
  birthData?: BirthData;
  preferences: {
    language: string;
    theme: string;
    enabledEngines: string[];
  };
  createdAt: string;
}

interface UserContextType {
  user: UserProfile | null;
  isLoggedIn: boolean;
  isLoading: boolean;
  logout: () => void;
  updateProfile: (profile: Partial<UserProfile>) => void;
  updateBirthData: (birthData: BirthData) => Promise<void>;
  refreshUser: () => Promise<void>;
}

const UserContext = createContext<UserContextType | undefined>(undefined);

export function UserProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<UserProfile | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // 从 JWT token 检查登录状态并获取用户信息
  const initializeUser = async () => {
    const token = getStoredToken();
    if (!token) {
      // 没有 token，未登录
      setUser(null);
      setIsLoading(false);
      return;
    }

    try {
      // 尝试从后端获取用户信息
      const userInfo = await authApi.me();

      // 从后端获取用户档案（包括 birthData）
      let birthData: BirthData | undefined = undefined;
      let preferences = {
        language: "zh",
        theme: "light",
        enabledEngines: ["bazi", "ziwei", "astro", "tarot"],
      };

      try {
        const profile = await api.user.getProfile(userInfo.user_id);
        if (profile.birth_data) {
          // 转换后端格式为前端格式
          birthData = {
            year: profile.birth_data.year,
            month: profile.birth_data.month,
            day: profile.birth_data.day,
            hour: profile.birth_data.hour,
            minute: profile.birth_data.minute,
            sexAtBirth: profile.birth_data.gender === "male" ? "male" : profile.birth_data.gender === "female" ? "female" : undefined,
            city: profile.birth_data.location,
            latitude: profile.birth_data.latitude,
            longitude: profile.birth_data.longitude,
            timezone: profile.birth_data.timezone,
          };
        }
        if (profile.preferences) {
          preferences = {
            language: profile.preferences.language || "zh",
            theme: profile.preferences.theme || "light",
            enabledEngines: profile.preferences.enabled_engines || ["bazi", "ziwei", "astro", "tarot"],
          };
        }
      } catch (e) {
        console.warn("Failed to fetch user profile, using defaults:", e);
      }

      const userProfile: UserProfile = {
        userId: userInfo.user_id,
        name: userInfo.name || userInfo.email?.split('@')[0] || 'User',
        email: userInfo.email,
        birthData,
        preferences,
        createdAt: new Date().toISOString(),
      };

      setUser(userProfile);
    } catch (error) {
      // Token 无效或过期，静默处理，用户以游客身份继续
      console.warn("Auth session expired, continuing as guest");
      clearStoredToken();
      setUser(null);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    initializeUser();
  }, []);

  const logout = () => {
    clearStoredToken();
    setUser(null);
  };

  const updateProfile = (profile: Partial<UserProfile>) => {
    if (user) {
      setUser({ ...user, ...profile });
    }
  };

  const updateBirthData = async (birthData: BirthData) => {
    if (user) {
      // 立即更新本地状态
      setUser({ ...user, birthData });
      
      // 同步保存到后端
      try {
        await api.user.updateProfile(user.userId, {
          birth_data: {
            year: birthData.year,
            month: birthData.month,
            day: birthData.day,
            hour: birthData.hour,
            minute: birthData.minute,
            timezone: birthData.timezone || "Asia/Shanghai",
            gender: birthData.sexAtBirth || "male",
            location: birthData.city,
            latitude: birthData.latitude,
            longitude: birthData.longitude,
          },
        });
        console.log("Birth data saved to backend");
      } catch (error) {
        console.error("Failed to save birth data to backend:", error);
        // 即使后端保存失败，本地状态已更新，不影响用户继续使用
      }
    }
  };

  const refreshUser = async () => {
    await initializeUser();
  };

  return (
    <UserContext.Provider
      value={{
        user,
        isLoggedIn: !!user,
        isLoading,
        logout,
        updateProfile,
        updateBirthData,
        refreshUser,
      }}
    >
      {children}
    </UserContext.Provider>
  );
}

export function useUser() {
  const context = useContext(UserContext);
  if (context === undefined) {
    throw new Error("useUser must be used within a UserProvider");
  }
  return context;
}
