'use client';

/**
 * 独立的语言选择页面
 * 
 * 成熟App的标准设计：独立页面，而非嵌入式
 */

import { motion } from 'framer-motion';
import { ArrowLeft, Check, Globe } from 'lucide-react';
import { useTranslation, useLocale, type Locale, LOCALES } from '@/lib/i18n';

interface LanguagePageProps {
  onBack: () => void;
}

export function LanguagePage({ onBack }: LanguagePageProps) {
  const { t, dir } = useTranslation();
  const { locale, setLocale, availableLocales } = useLocale();

  const handleSelectLanguage = (code: Locale) => {
    setLocale(code);
    // 选择后短暂延迟返回，让用户看到选中效果
    setTimeout(() => onBack(), 300);
  };

  return (
    <motion.div
      className="language-page"
      initial={{ opacity: 0, x: 20 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -20 }}
      dir={dir}
    >
      {/* 顶部导航栏 */}
      <header className="page-header">
        <button className="back-btn" onClick={onBack} aria-label={t.common.back}>
          <ArrowLeft size={20} />
        </button>
        <h1 className="page-title">{t.settings.language}</h1>
        <div className="header-spacer" />
      </header>

      {/* 语言列表 */}
      <div className="language-list">
        {Object.values(availableLocales).map((lang, index) => (
          <motion.button
            key={lang.code}
            className={`language-item ${locale === lang.code ? 'active' : ''}`}
            onClick={() => handleSelectLanguage(lang.code as Locale)}
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.03 }}
          >
            <div className="lang-info">
              <span className="lang-native">{lang.nativeName}</span>
              <span className="lang-english">{lang.name}</span>
            </div>
            {locale === lang.code && (
              <motion.div
                className="check-icon"
                initial={{ scale: 0 }}
                animate={{ scale: 1 }}
              >
                <Check size={20} />
              </motion.div>
            )}
          </motion.button>
        ))}
      </div>

      {/* 说明文字 */}
      <p className="language-hint">
        {locale === 'zh' 
          ? '语言设置将立即生效，并自动保存。'
          : 'Language settings take effect immediately and are saved automatically.'}
      </p>

      <style jsx>{`
        .language-page {
          min-height: 100vh;
          background: var(--bg-middle);
          display: flex;
          flex-direction: column;
        }

        .page-header {
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: var(--space-md) var(--space-lg);
          background: var(--card-bg);
          border-bottom: 1px solid var(--card-border);
          position: sticky;
          top: 0;
          z-index: 10;
        }

        .back-btn {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 40px;
          height: 40px;
          background: none;
          border: none;
          border-radius: var(--radius-md);
          color: var(--text-secondary);
          cursor: pointer;
          transition: all 0.2s;
        }

        .back-btn:hover {
          background: var(--bg-middle);
          color: var(--text-primary);
        }

        .page-title {
          font-family: Playfair Display, serif;
          font-size: 1.125rem;
          font-weight: 500;
          color: var(--text-primary);
          margin: 0;
        }

        .header-spacer {
          width: 40px;
        }

        .language-list {
          flex: 1;
          padding: var(--space-md);
          display: flex;
          flex-direction: column;
          gap: 1px;
          background: var(--card-border);
          margin: var(--space-md);
          border-radius: var(--radius-lg);
          overflow: hidden;
        }

        .language-item {
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: var(--space-md) var(--space-lg);
          background: var(--card-bg);
          border: none;
          cursor: pointer;
          transition: background 0.15s;
          text-align: left;
        }

        .language-item:first-child {
          border-radius: var(--radius-md) var(--radius-md) 0 0;
        }

        .language-item:last-child {
          border-radius: 0 0 var(--radius-md) var(--radius-md);
        }

        .language-item:hover {
          background: var(--bg-middle);
        }

        .language-item.active {
          background: var(--card-bg);
        }

        .lang-info {
          display: flex;
          flex-direction: column;
          gap: 2px;
        }

        .lang-native {
          font-size: 1rem;
          font-weight: 500;
          color: var(--text-primary);
        }

        .lang-english {
          font-size: 0.8rem;
          color: var(--text-tertiary);
        }

        .check-icon {
          color: var(--accent-gold);
        }

        .language-hint {
          text-align: center;
          font-size: 0.8rem;
          color: var(--text-tertiary);
          padding: var(--space-md) var(--space-lg) var(--space-2xl);
          margin: 0;
        }
      `}</style>
    </motion.div>
  );
}

export default LanguagePage;
