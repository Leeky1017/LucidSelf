"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Loader2, Mail, Lock, Globe, Eye, EyeOff } from "lucide-react";
import { useTranslation, useLocale, type Locale, LOCALES } from "@/lib/i18n";

interface LoginPageProps {
  onEmailLogin?: (email: string, password: string) => Promise<void>;
  onEmailSignup?: (email: string, password: string, name: string) => Promise<void>;
  onLanguageSettings?: () => void;
}

export function LoginPage({ onEmailLogin, onEmailSignup, onLanguageSettings }: LoginPageProps) {
  const { t, dir } = useTranslation();
  const { locale, availableLocales } = useLocale();

  const [mode, setMode] = useState<"login" | "signup">("login");
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);



  const handleEmailSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email.trim() || !password.trim()) return;

    // 密码不能包含空格
    if (password.includes(' ')) {
      setError(t.auth.passwordNoSpaces);
      return;
    }

    // 注册时检查密码确认
    if (mode === "signup" && password !== confirmPassword) {
      setError(t.auth.passwordsNotMatch);
      return;
    }

    setLoading(true);
    setError(null);

    try {
      if (mode === "login" && onEmailLogin) {
        await onEmailLogin(email, password);
      } else if (mode === "signup" && onEmailSignup) {
        await onEmailSignup(email, password, name || email.split("@")[0]);
      }
    } catch (err: any) {
      setError(err.message || t.errors.unknownError);
    } finally {
      setLoading(false);
    }
  };

  const canSubmit = mode === "login"
    ? email.trim().length > 0 && password.trim().length >= 8
    : email.trim().length > 0 && password.trim().length >= 8 && confirmPassword.trim().length >= 8;

  return (
    <div className="login-page" dir={dir}>
      {/* 语言设置入口 - 右上角 */}
      {onLanguageSettings && (
        <button
          className="lang-btn"
          onClick={onLanguageSettings}
          aria-label={t.settings.selectLanguage}
        >
          <Globe size={18} />
          <span>{availableLocales[locale].nativeName}</span>
        </button>
      )}

      <motion.div
        className="login-card"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        {/* 品牌标识 - 上下叠放 */}
        <div className="brand-block">
          <h1 className="brand-name">
            <span className="brand-lucid">Lucid</span>
            <span className="brand-self">Self</span>
          </h1>
          {t.brand.tagline && <p className="brand-tagline">{t.brand.tagline}</p>}
        </div>

        {/* 哲学简介 */}
        <p className="philosophy-text">{t.brand.philosophy}</p>

        {/* Mode Tabs - 只有登录和注册两个 */}
        <div className="login-tabs">
          <button
            className={`tab ${mode === "login" ? "active" : ""}`}
            onClick={() => { setMode("login"); setError(null); }}
          >
            {t.auth.login}
          </button>
          <button
            className={`tab ${mode === "signup" ? "active" : ""}`}
            onClick={() => { setMode("signup"); setError(null); }}
          >
            {t.auth.signup}
          </button>
        </div>

        <AnimatePresence mode="wait">
          <motion.form
            key="email"
            className="login-form"
            onSubmit={handleEmailSubmit}
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
          >
            {mode === "signup" && (
              <div className="input-group">
                <input
                  type="text"
                  placeholder={t.profile.name}
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="login-input"
                />
              </div>
            )}
            <div className="input-group">
              <Mail size={18} className="input-icon" />
              <input
                type="email"
                placeholder={t.auth.emailPlaceholder}
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="login-input with-icon"
                autoFocus
              />
            </div>
            <div className="input-group">
              <Lock size={18} className="input-icon" />
              <input
                type={showPassword ? "text" : "password"}
                placeholder={t.auth.passwordPlaceholder}
                value={password}
                onChange={(e) => setPassword(e.target.value.replace(/\s/g, ''))}
                className="login-input with-icon with-eye"
              />
              <button
                type="button"
                className="eye-btn"
                onClick={() => setShowPassword(!showPassword)}
                aria-label={showPassword ? 'Hide password' : 'Show password'}
              >
                {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
              </button>
            </div>
            {mode === "signup" && (
              <div className="input-group">
                <Lock size={18} className="input-icon" />
                <input
                  type={showConfirmPassword ? "text" : "password"}
                  placeholder={t.auth.confirmPassword}
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value.replace(/\s/g, ''))}
                  className="login-input with-icon with-eye"
                />
                <button
                  type="button"
                  className="eye-btn"
                  onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                  aria-label={showConfirmPassword ? 'Hide password' : 'Show password'}
                >
                  {showConfirmPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                </button>
              </div>
            )}

            {error && (
              <motion.div
                className="login-error"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
              >
                {error}
              </motion.div>
            )}

            <button type="submit" className="login-button" disabled={!canSubmit || loading}>
              {loading ? (
                <Loader2 size={20} className="spinning" />
              ) : mode === "login" ? (
                t.auth.login
              ) : (
                t.auth.signup
              )}
            </button>
          </motion.form>
        </AnimatePresence>
      </motion.div>

      <style jsx>{`
        .login-page {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background: var(--bg-middle);
          position: relative;
        }

        .lang-btn {
          position: absolute;
          top: var(--space-lg);
          right: var(--space-lg);
          z-index: 10;
          display: flex;
          align-items: center;
          gap: var(--space-xs);
          padding: var(--space-sm) var(--space-md);
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-full);
          color: var(--text-secondary);
          font-size: 0.875rem;
          cursor: pointer;
          transition: all 0.2s;
        }

        .lang-btn:hover {
          background: var(--bg-middle);
          color: var(--text-primary);
        }

        .login-card {
          text-align: center;
          padding: var(--space-2xl);
          max-width: 400px;
          width: 100%;
        }

        .brand-block {
          margin-bottom: var(--space-md);
        }

        .brand-name {
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: 0;
          margin: 0;
          line-height: 1;
        }

        .brand-lucid {
          font-family: Playfair Display, Noto Serif SC, serif;
          font-size: 3rem;
          font-weight: 400;
          color: var(--text-primary);
          letter-spacing: 0.1em;
        }

        .brand-self {
          font-family: Playfair Display, Noto Serif SC, serif;
          font-size: 2.25rem;
          font-weight: 300;
          color: var(--accent-gold);
          letter-spacing: 0.15em;
          margin-top: -4px;
        }

        .brand-tagline {
          font-size: 0.9rem;
          color: var(--text-tertiary);
          margin: var(--space-sm) 0 0 0;
          letter-spacing: 0.3em;
        }

        .philosophy-text {
          font-size: 0.85rem;
          color: var(--text-secondary);
          margin: 0 0 var(--space-xl) 0;
          font-style: italic;
          opacity: 0.8;
        }

        .login-tabs {
          display: flex;
          gap: var(--space-xs);
          margin-bottom: var(--space-lg);
          padding: 4px;
          background: var(--card-bg);
          border-radius: var(--radius-full);
          border: 1px solid var(--card-border);
        }

        .login-tabs .tab {
          flex: 1;
          padding: var(--space-sm) var(--space-md);
          border: none;
          background: transparent;
          border-radius: var(--radius-full);
          font-size: 0.875rem;
          color: var(--text-secondary);
          cursor: pointer;
          transition: all 0.2s ease;
        }

        .login-tabs .tab:hover {
          color: var(--text-primary);
        }

        .login-tabs .tab.active {
          background: var(--text-primary);
          color: var(--background);
        }

        .login-form {
          display: flex;
          flex-direction: column;
          gap: var(--space-md);
        }

        .input-group {
          position: relative;
        }

        .input-icon {
          position: absolute;
          left: var(--space-md);
          top: 50%;
          transform: translateY(-50%);
          color: var(--text-tertiary);
          pointer-events: none;
        }

        .login-input {
          width: 100%;
          padding: var(--space-md);
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          font-size: 1rem;
          color: var(--text-primary);
          text-align: center;
          transition: border-color 0.2s, box-shadow 0.2s;
        }

        .login-input.with-icon {
          padding-left: calc(var(--space-md) * 2 + 18px);
          text-align: left;
        }

        .login-input.with-eye {
          padding-right: calc(var(--space-md) * 2 + 18px);
        }

        .eye-btn {
          position: absolute;
          right: var(--space-md);
          top: 50%;
          transform: translateY(-50%);
          background: transparent;
          border: none;
          padding: 4px;
          cursor: pointer;
          color: var(--text-tertiary);
          display: flex;
          align-items: center;
          justify-content: center;
          transition: color 0.2s;
        }

        .eye-btn:hover {
          color: var(--text-primary);
        }

        .login-input::placeholder {
          color: var(--text-tertiary);
        }

        .login-input:focus {
          outline: none;
          border-color: var(--accent-gold);
          box-shadow: 0 0 0 3px var(--glow-color);
        }

        .login-error {
          padding: var(--space-sm) var(--space-md);
          background: #fef2f2;
          border: 1px solid #fecaca;
          border-radius: var(--radius-md);
          color: #dc2626;
          font-size: 0.875rem;
          text-align: left;
        }

        .login-hint {
          font-size: 0.75rem;
          color: var(--text-tertiary);
          margin: 0;
        }

        .login-button {
          width: 100%;
          padding: var(--space-md);
          background: var(--accent-gold);
          border: none;
          border-radius: var(--radius-md);
          font-size: 1rem;
          font-weight: 500;
          color: #fff;
          cursor: pointer;
          transition: opacity 0.2s, transform 0.2s;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .login-button:disabled {
          opacity: 0.4;
          cursor: not-allowed;
        }

        .login-button:not(:disabled):hover {
          opacity: 0.9;
        }

        .login-button:not(:disabled):active {
          transform: scale(0.98);
        }

        .spinning {
          animation: spin 1s linear infinite;
        }

        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }
      `}</style>
    </div>
  );
}
