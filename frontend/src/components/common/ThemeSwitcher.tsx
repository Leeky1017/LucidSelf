'use client';

/**
 * 主题切换器组件
 */

import { useState, useRef, useEffect } from 'react';
import { Palette } from 'lucide-react';
import { useTheme, THEMES, Theme } from '@/contexts/ThemeContext';
import { useLocale } from '@/lib/i18n';

export function ThemeSwitcher() {
  const { theme, setTheme } = useTheme();
  const { locale } = useLocale();
  const [isOpen, setIsOpen] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  // 点击外部关闭
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const currentTheme = THEMES.find(t => t.id === theme);

  return (
    <div className="theme-switcher" ref={containerRef}>
      <button 
        className="theme-trigger"
        onClick={() => setIsOpen(!isOpen)}
        title={locale === 'zh' ? '切换主题' : 'Switch theme'}
      >
        <Palette size={18} />
        <span className="theme-name-small">{locale === 'zh' ? currentTheme?.nameZh : currentTheme?.name}</span>
      </button>

      {isOpen && (
        <div className="theme-dropdown">
          <div className="theme-title">
            {locale === 'zh' ? '选择主题' : 'Select Theme'}
          </div>
          <div className="theme-list">
            {THEMES.map(t => (
              <button
                key={t.id}
                className={`theme-option ${theme === t.id ? 'active' : ''}`}
                onClick={() => {
                  setTheme(t.id);
                  setIsOpen(false);
                }}
              >
                <span className={`theme-dot theme-dot-${t.id}`}></span>
                <span className="option-name">
                  {locale === 'zh' ? t.nameZh : t.name}
                </span>
              </button>
            ))}
          </div>
        </div>
      )}

      <style jsx>{`
        .theme-switcher {
          position: relative;
        }

        .theme-trigger {
          display: flex;
          align-items: center;
          gap: 6px;
          padding: 8px 12px;
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          color: var(--text-secondary);
          cursor: pointer;
          transition: all 0.2s;
        }

        .theme-trigger:hover {
          border-color: var(--accent-gold);
          color: var(--accent-gold);
        }

        .theme-name-small {
          font-size: 0.8rem;
        }

        .theme-dropdown {
          position: absolute;
          top: 100%;
          right: 0;
          margin-top: 8px;
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-lg);
          box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
          z-index: 100;
          min-width: 180px;
          overflow: hidden;
        }

        .theme-title {
          padding: 12px 16px;
          font-size: 0.75rem;
          font-weight: 600;
          text-transform: uppercase;
          letter-spacing: 0.05em;
          color: var(--text-tertiary);
          border-bottom: 1px solid var(--card-border);
        }

        .theme-list {
          padding: 8px;
        }

        .theme-option {
          display: flex;
          align-items: center;
          gap: 12px;
          width: 100%;
          padding: 10px 12px;
          background: none;
          border: none;
          border-radius: var(--radius-md);
          color: var(--text-primary);
          cursor: pointer;
          transition: all 0.15s;
          text-align: left;
        }

        .theme-option:hover {
          background: var(--bg-middle);
        }

        .theme-option.active {
          background: var(--accent-gold);
          color: white;
        }

        .theme-dot {
          width: 16px;
          height: 16px;
          border-radius: 50%;
          border: 2px solid var(--card-border);
        }

        .theme-dot-light {
          background: linear-gradient(135deg, #fff 50%, #fafafa 50%);
          border-color: #e8e8e8;
        }

        .theme-dot-dark {
          background: linear-gradient(135deg, #151515 50%, #0a0a0a 50%);
          border-color: #242424;
        }

        .theme-dot-cyber {
          background: linear-gradient(135deg, #00f0ff 50%, #0a0a12 50%);
          border-color: #1a1a3a;
        }

        .theme-dot-kawaii {
          background: linear-gradient(135deg, #ff8fab 50%, #fff5f7 50%);
          border-color: #ffe0e8;
        }

        .theme-dot-nature {
          background: linear-gradient(135deg, #7cb342 50%, #f5f9f0 50%);
          border-color: #d5e8c8;
        }

        .option-name {
          font-size: 0.9rem;
          font-weight: 500;
        }
      `}</style>
    </div>
  );
}

export default ThemeSwitcher;
