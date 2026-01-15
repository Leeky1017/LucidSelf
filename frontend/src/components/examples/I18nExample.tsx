'use client';

/**
 * i18n 使用示例
 * 
 * 演示如何在组件中使用国际化功能
 */

import React from 'react';
import { useTranslation, useLocale } from '@/lib/i18n';
import { LanguageSwitcher } from '@/components/common/LanguageSwitcher';

export function I18nExample() {
  const { t, locale, dir } = useTranslation();
  const { availableLocales } = useLocale();

  return (
    <div className="p-6 space-y-6" dir={dir}>
      {/* 语言切换器 */}
      <section className="space-y-2">
        <h2 className="text-lg font-semibold text-white">
          {t.settings.language}
        </h2>
        <LanguageSwitcher showLabel />
        <p className="text-sm text-white/60">
          {t.settings.selectLanguage}: {availableLocales[locale].nativeName}
        </p>
      </section>

      {/* 通用文本示例 */}
      <section className="space-y-2">
        <h2 className="text-lg font-semibold text-white">
          {t.common.loading}
        </h2>
        <div className="flex gap-2 flex-wrap">
          <button className="px-3 py-1 bg-indigo-600 text-white rounded">
            {t.common.save}
          </button>
          <button className="px-3 py-1 bg-red-600 text-white rounded">
            {t.common.delete}
          </button>
          <button className="px-3 py-1 bg-gray-600 text-white rounded">
            {t.common.cancel}
          </button>
        </div>
      </section>

      {/* 导航示例 */}
      <section className="space-y-2">
        <h2 className="text-lg font-semibold text-white">
          {t.nav.home}
        </h2>
        <nav className="flex gap-4 text-white/80">
          <span>{t.nav.playbook}</span>
          <span>{t.nav.dreamJournal}</span>
          <span>{t.nav.timeline}</span>
          <span>{t.nav.patterns}</span>
          <span>{t.nav.insights}</span>
        </nav>
      </section>

      {/* 认证示例 */}
      <section className="space-y-2">
        <h2 className="text-lg font-semibold text-white">
          {t.auth.login}
        </h2>
        <div className="space-y-2 max-w-sm">
          <input
            type="email"
            placeholder={t.auth.emailPlaceholder}
            className="w-full px-3 py-2 bg-white/10 border border-white/20 rounded text-white placeholder:text-white/40"
          />
          <input
            type="password"
            placeholder={t.auth.passwordPlaceholder}
            className="w-full px-3 py-2 bg-white/10 border border-white/20 rounded text-white placeholder:text-white/40"
          />
          <button className="w-full px-3 py-2 bg-indigo-600 text-white rounded">
            {t.auth.loginWithEmail}
          </button>
        </div>
      </section>

      {/* Profile 示例 */}
      <section className="space-y-2">
        <h2 className="text-lg font-semibold text-white">
          {t.profile.title}
        </h2>
        <p className="text-white/60">{t.profile.subtitle}</p>
        <div className="grid grid-cols-2 gap-4 max-w-md">
          <div>
            <label className="text-sm text-white/60">{t.profile.birthYear}</label>
            <select className="w-full mt-1 px-3 py-2 bg-white/10 border border-white/20 rounded text-white">
              <option>{t.profile.selectYear}</option>
            </select>
          </div>
          <div>
            <label className="text-sm text-white/60">{t.profile.birthMonth}</label>
            <select className="w-full mt-1 px-3 py-2 bg-white/10 border border-white/20 rounded text-white">
              <option>{t.profile.selectMonth}</option>
            </select>
          </div>
        </div>
        <div className="space-y-1">
          <label className="text-sm text-white/60">{t.profile.sexAtBirth}</label>
          <div className="flex gap-4">
            <button className="px-4 py-2 bg-blue-600 text-white rounded">
              {t.profile.male}
            </button>
            <button className="px-4 py-2 bg-pink-600 text-white rounded">
              {t.profile.female}
            </button>
          </div>
        </div>
      </section>

      {/* 梦境日记示例 */}
      <section className="space-y-2">
        <h2 className="text-lg font-semibold text-white">
          {t.dream.title}
        </h2>
        <p className="text-white/60">{t.dream.subtitle}</p>
        <textarea
          placeholder={t.dream.dreamContentPlaceholder}
          className="w-full px-3 py-2 bg-white/10 border border-white/20 rounded text-white placeholder:text-white/40 h-24"
        />
        <div className="space-y-1">
          <label className="text-sm text-white/60">{t.dream.mood}</label>
          <div className="flex gap-2 flex-wrap">
            {Object.entries(t.dream.moodOptions).map(([key, label]) => (
              <span key={key} className="px-2 py-1 bg-white/10 rounded text-sm text-white/80">
                {label}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* 错误消息示例 */}
      <section className="space-y-2">
        <h2 className="text-lg font-semibold text-white">
          {t.errors.networkError}
        </h2>
        <div className="space-y-1">
          {Object.entries(t.errors).map(([key, message]) => (
            <p key={key} className="text-red-400 text-sm">• {message}</p>
          ))}
        </div>
      </section>
    </div>
  );
}

export default I18nExample;
