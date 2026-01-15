'use client';

/**
 * 主题上下文
 * 
 * 支持5种主题：light, dark, cyber, kawaii, nature
 * 主题设置保存到后端 user profile preferences
 */

import { createContext, useContext, useState, useEffect, ReactNode, useCallback } from 'react';
import { api } from '@/lib/api';
import { getStoredToken } from '@/lib/authApi';

export type Theme = 'light' | 'dark' | 'cyber' | 'kawaii' | 'nature';

export const THEMES: { id: Theme; name: string; nameZh: string }[] = [
  { id: 'light', name: 'Light', nameZh: '明亮' },
  { id: 'dark', name: 'Dark', nameZh: '暗黑' },
  { id: 'cyber', name: 'Cyber', nameZh: '赛博科技' },
  { id: 'kawaii', name: 'Kawaii', nameZh: '清纯可爱' },
  { id: 'nature', name: 'Nature', nameZh: '清新自然' },
];

interface ThemeContextValue {
  theme: Theme;
  setTheme: (theme: Theme) => void;
  userId: string | null;
  setUserId: (id: string | null) => void;
}

const ThemeContext = createContext<ThemeContextValue | undefined>(undefined);

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setThemeState] = useState<Theme>('light');
  const [mounted, setMounted] = useState(false);
  const [userId, setUserId] = useState<string | null>(null);

  // 初始化时从后端加载主题
  useEffect(() => {
    const loadTheme = async () => {
      const token = getStoredToken();
      if (token && userId) {
        try {
          const profile = await api.user.getProfile(userId);
          const savedTheme = profile.preferences?.theme as Theme;
          if (savedTheme && THEMES.some(t => t.id === savedTheme)) {
            setThemeState(savedTheme);
            document.documentElement.setAttribute('data-theme', savedTheme);
          }
        } catch (e) {
          console.warn('Failed to load theme from backend:', e);
        }
      }
      setMounted(true);
    };
    loadTheme();
  }, [userId]);

  // 设置主题并同步到后端
  const setTheme = useCallback(async (newTheme: Theme) => {
    setThemeState(newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
    
    // 同步到后端
    if (userId) {
      try {
        await api.user.updateProfile(userId, {
          preferences: { theme: newTheme },
        });
      } catch (e) {
        console.warn('Failed to save theme to backend:', e);
      }
    }
  }, [userId]);

  // 防止SSR闪烁
  if (!mounted) {
    return null;
  }

  return (
    <ThemeContext.Provider value={{ theme, setTheme, userId, setUserId }}>
      {children}
    </ThemeContext.Provider>
  );
}

export function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}
