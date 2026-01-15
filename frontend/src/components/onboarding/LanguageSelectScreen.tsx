'use client';

/**
 * 首屏语言选择页面
 * 
 * 用户触达LS的第一个页面，必须选择语言才能继续
 */

import { motion } from 'framer-motion';
import { Check, Globe } from 'lucide-react';
import { useLocale, type Locale } from '@/lib/i18n';

interface LanguageSelectScreenProps {
  onContinue: () => void;
}

const LANGUAGE_OPTIONS = [
  { code: 'zh', nativeName: '中文', name: 'Chinese', flag: '🇨🇳' },
  { code: 'en', nativeName: 'English', name: 'English', flag: '🇺🇸' },
  { code: 'ja', nativeName: '日本語', name: 'Japanese', flag: '🇯🇵' },
  { code: 'ko', nativeName: '한국어', name: 'Korean', flag: '🇰🇷' },
  { code: 'es', nativeName: 'Español', name: 'Spanish', flag: '🇪🇸' },
  { code: 'de', nativeName: 'Deutsch', name: 'German', flag: '🇩🇪' },
  { code: 'fr', nativeName: 'Français', name: 'French', flag: '🇫🇷' },
  { code: 'it', nativeName: 'Italiano', name: 'Italian', flag: '🇮🇹' },
  { code: 'pt', nativeName: 'Português', name: 'Portuguese', flag: '🇧🇷' },
  { code: 'da', nativeName: 'Dansk', name: 'Danish', flag: '🇩🇰' },
  { code: 'ar', nativeName: 'العربية', name: 'Arabic', flag: '🇸🇦' },
] as const;

export function LanguageSelectScreen({ onContinue }: LanguageSelectScreenProps) {
  const { locale, setLocale } = useLocale();

  const handleSelect = (code: Locale) => {
    setLocale(code);
  };

  return (
    <div className="language-select-screen">
      <motion.div
        className="content"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        <div className="logo-area">
          <h1 className="brand">
            <span className="brand-lucid">Lucid</span>
            <span className="brand-self">Self</span>
          </h1>
          {locale === 'zh' && <p className="tagline">晴吾</p>}
        </div>

        <div className="language-section">
          <div className="section-header">
            <Globe size={20} />
            <span>Select your language</span>
          </div>

          <div className="language-grid">
            {LANGUAGE_OPTIONS.map((lang, index) => (
              <motion.button
                key={lang.code}
                className={`language-card ${locale === lang.code ? 'active' : ''}`}
                onClick={() => handleSelect(lang.code as Locale)}
                initial={{ opacity: 0, scale: 0.9 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: index * 0.05 }}
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                <span className="flag">{lang.flag}</span>
                <div className="lang-text">
                  <span className="native">{lang.nativeName}</span>
                  <span className="english">{lang.name}</span>
                </div>
                {locale === lang.code && (
                  <motion.div
                    className="check"
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                  >
                    <Check size={18} />
                  </motion.div>
                )}
              </motion.button>
            ))}
          </div>
        </div>

        <motion.button
          className="continue-btn"
          onClick={onContinue}
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
        >
          {{
            zh: '继续',
            en: 'Continue',
            ja: '続ける',
            ko: '계속하기',
            es: 'Continuar',
            de: 'Weiter',
            fr: 'Continuer',
            ar: 'متابعة',
            it: 'Continua',
            da: 'Fortsæt',
            pt: 'Continuar',
          }[locale] || 'Continue'}
        </motion.button>
      </motion.div>

      <style jsx>{`
        .language-select-screen {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background: linear-gradient(135deg, var(--bg-middle) 0%, var(--bg-deep) 100%);
          padding: var(--space-xl);
        }

        .content {
          width: 100%;
          max-width: 800px;
          text-align: center;
        }

        .logo-area {
          margin-bottom: var(--space-2xl);
        }

        .brand {
          font-family: Playfair Display, Noto Serif SC, serif;
          font-size: clamp(2.5rem, 5vw, 4rem);
          font-weight: 400;
          color: var(--text-primary);
          margin: 0;
          letter-spacing: -0.02em;
          display: flex;
          flex-direction: column;
          align-items: center;
          line-height: 1.1;
        }

        .brand-lucid {
          font-weight: 300;
          opacity: 0.9;
        }

        .brand-self {
          font-weight: 500;
        }

        .tagline {
          font-size: 1.2rem;
          color: var(--text-secondary);
          margin: var(--space-xs) 0 0 0;
          letter-spacing: 0.3em;
        }

        .language-section {
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-xl);
          padding: var(--space-xl);
          margin-bottom: var(--space-xl);
        }

        .section-header {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: var(--space-sm);
          font-size: 0.9rem;
          color: var(--text-secondary);
          margin-bottom: var(--space-lg);
        }

        .language-grid {
          display: grid;
          grid-template-columns: repeat(2, 1fr);
          gap: var(--space-md);
        }

        @media (min-width: 640px) {
          .language-grid {
            grid-template-columns: repeat(4, 1fr);
          }
        }

        .language-card {
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: var(--space-sm);
          padding: var(--space-lg) var(--space-md);
          background: var(--bg-middle);
          border: 2px solid transparent;
          border-radius: var(--radius-lg);
          cursor: pointer;
          transition: all 0.2s;
          position: relative;
        }

        .language-card:hover {
          background: var(--bg-deep);
          border-color: var(--card-border);
        }

        .language-card.active {
          background: var(--bg-deep);
          border-color: var(--accent-gold);
        }

        .flag {
          font-size: 2rem;
        }

        .lang-text {
          display: flex;
          flex-direction: column;
          gap: 2px;
        }

        .native {
          font-size: 1rem;
          font-weight: 500;
          color: var(--text-primary);
        }

        .english {
          font-size: 0.75rem;
          color: var(--text-tertiary);
        }

        .check {
          position: absolute;
          top: var(--space-sm);
          right: var(--space-sm);
          color: var(--accent-gold);
        }

        .continue-btn {
          min-width: 200px;
          padding: var(--space-md) var(--space-2xl);
          background: var(--accent-gold);
          border: none;
          border-radius: var(--radius-full);
          color: #fff;
          font-size: 1rem;
          font-weight: 500;
          cursor: pointer;
          transition: all 0.2s;
        }

        .continue-btn:hover {
          background: var(--accent-gold-dark);
        }
      `}</style>
    </div>
  );
}

export default LanguageSelectScreen;
