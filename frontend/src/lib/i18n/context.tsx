'use client';

/**
 * i18n React Context
 * 
 * 提供语言切换和翻译功能
 * 语言设置保存到后端 user profile preferences
 */

import React, { createContext, useContext, useState, useCallback, useEffect, useMemo } from 'react';
import type { Locale, Translations } from './types';
import { LOCALES, DEFAULT_LOCALE } from './types';
import { translations } from './locales';
import { api } from '@/lib/api';
import { getStoredToken } from '@/lib/authApi';

// ==================== Types ====================

interface I18nContextType {
  locale: Locale;
  setLocale: (locale: Locale) => void;
  t: Translations;
  dir: 'ltr' | 'rtl';
  availableLocales: typeof LOCALES;
  userId: string | null;
  setUserId: (id: string | null) => void;
}

// ==================== Context ====================

const I18nContext = createContext<I18nContextType | null>(null);

// ==================== Utils ====================

function getInitialLocale(): Locale {
  if (typeof window === 'undefined') {
    return DEFAULT_LOCALE;
  }
  
  // 从浏览器语言检测
  const browserLang = navigator.language.split('-')[0];
  if (browserLang in LOCALES) {
    return browserLang as Locale;
  }
  
  // 默认中文
  return DEFAULT_LOCALE;
}

// ==================== Provider ====================

interface I18nProviderProps {
  children: React.ReactNode;
  initialLocale?: Locale;
}

export function I18nProvider({ children, initialLocale }: I18nProviderProps) {
  const [locale, setLocaleState] = useState<Locale>(initialLocale || DEFAULT_LOCALE);
  const [isHydrated, setIsHydrated] = useState(false);
  const [userId, setUserId] = useState<string | null>(null);
  
  // 从后端加载语言设置
  useEffect(() => {
    const loadLocale = async () => {
      const token = getStoredToken();
      if (token && userId) {
        try {
          const profile = await api.user.getProfile(userId);
          const savedLocale = profile.preferences?.language as Locale;
          if (savedLocale && savedLocale in LOCALES) {
            setLocaleState(savedLocale);
            document.documentElement.lang = savedLocale;
            document.documentElement.dir = LOCALES[savedLocale].dir;
          }
        } catch (e) {
          console.warn('Failed to load locale from backend:', e);
        }
      } else if (!initialLocale) {
        setLocaleState(getInitialLocale());
      }
      setIsHydrated(true);
    };
    loadLocale();
  }, [initialLocale, userId]);
  
  // 切换语言并同步到后端
  const setLocale = useCallback(async (newLocale: Locale) => {
    setLocaleState(newLocale);
    if (typeof window !== 'undefined') {
      document.documentElement.lang = newLocale;
      document.documentElement.dir = LOCALES[newLocale].dir;
    }
    
    // 同步到后端
    if (userId) {
      try {
        await api.user.updateProfile(userId, {
          preferences: { language: newLocale },
        });
      } catch (e) {
        console.warn('Failed to save locale to backend:', e);
      }
    }
  }, [userId]);
  
  // 更新 HTML 属性
  useEffect(() => {
    if (isHydrated && typeof window !== 'undefined') {
      document.documentElement.lang = locale;
      document.documentElement.dir = LOCALES[locale].dir;
    }
  }, [locale, isHydrated]);
  
  // Memoize context value
  const contextValue = useMemo<I18nContextType>(() => ({
    locale,
    setLocale,
    t: translations[locale],
    dir: LOCALES[locale].dir,
    availableLocales: LOCALES,
    userId,
    setUserId,
  }), [locale, setLocale, userId]);
  
  return (
    <I18nContext.Provider value={contextValue}>
      {children}
    </I18nContext.Provider>
  );
}

// ==================== Hook ====================

export function useI18n(): I18nContextType {
  const context = useContext(I18nContext);
  if (!context) {
    throw new Error('useI18n must be used within an I18nProvider');
  }
  return context;
}

/**
 * 简化的翻译 hook
 * 返回当前语言的翻译对象
 */
export function useTranslation() {
  const { t, locale, dir } = useI18n();
  return { t, locale, dir };
}

/**
 * 语言切换 hook
 */
export function useLocale() {
  const { locale, setLocale, availableLocales } = useI18n();
  return { locale, setLocale, availableLocales };
}
