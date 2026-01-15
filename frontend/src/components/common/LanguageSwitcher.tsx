'use client';

/**
 * 语言切换组件
 */

import React from 'react';
import { Globe } from 'lucide-react';
import { useLocale, type Locale } from '@/lib/i18n';

interface LanguageSwitcherProps {
  className?: string;
  showLabel?: boolean;
  variant?: 'dropdown' | 'buttons';
}

export function LanguageSwitcher({ 
  className = '', 
  showLabel = false,
  variant = 'dropdown',
}: LanguageSwitcherProps) {
  const { locale, setLocale, availableLocales } = useLocale();
  
  if (variant === 'buttons') {
    return (
      <div className={`flex flex-wrap gap-2 ${className}`}>
        {Object.values(availableLocales).map((l) => (
          <button
            key={l.code}
            onClick={() => setLocale(l.code as Locale)}
            className={`px-3 py-1.5 rounded-lg text-sm transition-colors ${
              locale === l.code
                ? 'bg-indigo-600 text-white'
                : 'bg-white/10 hover:bg-white/20 text-white/80'
            }`}
          >
            {l.nativeName}
          </button>
        ))}
      </div>
    );
  }
  
  return (
    <div className={`relative inline-flex items-center ${className}`}>
      {showLabel && (
        <Globe className="w-4 h-4 mr-2 text-white/60" />
      )}
      <select
        value={locale}
        onChange={(e) => setLocale(e.target.value as Locale)}
        className="appearance-none bg-white/10 border border-white/20 rounded-lg px-3 py-2 pr-8 text-white text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 cursor-pointer"
        style={{ direction: 'ltr' }}
      >
        {Object.values(availableLocales).map((l) => (
          <option 
            key={l.code} 
            value={l.code}
            className="bg-gray-800 text-white"
          >
            {l.nativeName}
          </option>
        ))}
      </select>
      <div className="absolute right-2 pointer-events-none">
        <svg className="w-4 h-4 text-white/60" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </div>
    </div>
  );
}

export default LanguageSwitcher;
