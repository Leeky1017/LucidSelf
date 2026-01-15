"use client";

import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import type { BirthData } from "@/contexts/UserContext";
import { useTranslation, useLocale } from "@/lib/i18n";
import { CityPicker } from "@/components/common/CityPicker";
import { EditableSelect } from "@/components/common/EditableSelect";

// 生成选项
const currentYear = new Date().getFullYear();
const years = Array.from({ length: 100 }, (_, i) => currentYear - i);
const months = Array.from({ length: 12 }, (_, i) => i + 1);
const hours = Array.from({ length: 24 }, (_, i) => i);
const minutes = Array.from({ length: 60 }, (_, i) => i);

// 选中的城市信息
interface SelectedCity {
  displayName: string;
  province: string;
  city: string;
  lat: number;
  lng: number;
  timezone: string;
  countryCode?: string;
}

interface ProfileSetupProps {
  onComplete: (birthData: BirthData) => void;
  onSkip: () => void;
  userName: string;
}

// 获取某月的天数
function getDaysInMonth(year: number, month: number): number {
  return new Date(year, month, 0).getDate();
}

export function ProfileSetup({ onComplete, onSkip, userName }: ProfileSetupProps) {
  const { t } = useTranslation();
  const { locale } = useLocale();
  
  const [birthData, setBirthData] = useState<Partial<BirthData>>({
    year: 1990,
    month: 1,
    day: 1,
    hour: 12,
    minute: 0,
    sexAtBirth: undefined,
    city: "",
  });
  
  // 城市选择
  const [selectedCity, setSelectedCity] = useState<SelectedCity | null>(null);
  
  // 根据年月计算有效天数
  const validDays = birthData.year && birthData.month 
    ? getDaysInMonth(birthData.year, birthData.month) 
    : 31;
  
  // 当年月变化时，自动修正无效的日期
  useEffect(() => {
    if (birthData.day && birthData.day > validDays) {
      setBirthData(prev => ({ ...prev, day: validDays }));
    }
  }, [birthData.year, birthData.month, validDays, birthData.day]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (birthData.year && birthData.month && birthData.day && birthData.hour !== undefined && birthData.sexAtBirth) {
      const completeBirthData: BirthData = {
        year: birthData.year,
        month: birthData.month,
        day: birthData.day,
        hour: birthData.hour,
        minute: birthData.minute || 0,
        sexAtBirth: birthData.sexAtBirth,
        city: selectedCity?.displayName || "",
        latitude: selectedCity?.lat,
        longitude: selectedCity?.lng,
        timezone: selectedCity?.timezone || "Asia/Shanghai",
      };
      onComplete(completeBirthData);
    }
  };
  
  // 所有字段必填：日期、时间、性别、出生地
  const isFormValid = birthData.year && birthData.month && birthData.day && 
                      birthData.hour !== undefined && birthData.sexAtBirth && selectedCity;

  return (
    <div className="setup-page">
      <motion.div
        className="setup-card"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <h1 className="setup-title">{t.profile.title}</h1>
        <p className="setup-subtitle">{t.profile.greeting.replace('{name}', userName)}</p>

        <form className="setup-form" onSubmit={handleSubmit}>
          {/* 出生日期 - 使用EditableSelect支持输入+下拉 */}
          <div className="form-section">
            <label className="section-label">{t.profile.dateOfBirth}</label>
            <div className="form-row">
              <EditableSelect
                label={t.profile.birthYear}
                value={birthData.year || 1990}
                onChange={(v) => setBirthData({ ...birthData, year: v })}
                options={years.map(y => ({ value: y, label: String(y) }))}
                min={1920}
                max={currentYear}
              />
              <EditableSelect
                label={t.profile.birthMonth}
                value={birthData.month || 1}
                onChange={(v) => setBirthData({ ...birthData, month: v })}
                options={months.map(m => ({ value: m, label: String(m) }))}
                min={1}
                max={12}
              />
              <EditableSelect
                label={t.profile.birthDay}
                value={birthData.day || 1}
                onChange={(v) => setBirthData({ ...birthData, day: v })}
                options={Array.from({ length: validDays }, (_, i) => ({ value: i + 1, label: String(i + 1) }))}
                min={1}
                max={validDays}
              />
            </div>
          </div>

          {/* 出生时间 - 使用EditableSelect支持输入+下拉 */}
          <div className="form-section">
            <label className="section-label">{t.profile.timeOfBirth}</label>
            <div className="form-row time-row">
              <EditableSelect
                label={t.profile.birthHour}
                value={birthData.hour ?? 12}
                onChange={(v) => setBirthData({ ...birthData, hour: v })}
                options={hours.map(h => ({ value: h, label: String(h).padStart(2, '0') }))}
                min={0}
                max={23}
                formatDisplay={(v) => String(v).padStart(2, '0')}
              />
              <span className="time-sep">:</span>
              <EditableSelect
                label={t.profile.birthMinute}
                value={birthData.minute ?? 0}
                onChange={(v) => setBirthData({ ...birthData, minute: v })}
                options={minutes.map(m => ({ value: m, label: String(m).padStart(2, '0') }))}
                min={0}
                max={59}
                formatDisplay={(v) => String(v).padStart(2, '0')}
              />
              {locale === 'zh' && (
                <div className="shichen-display">
                  {getShichen(birthData.hour || 0)}时
                </div>
              )}
            </div>
            <p className="time-hint">{t.profile.timeHint}</p>
          </div>

          {/* 出生性别 */}
          <div className="form-section">
            <label className="section-label">{t.profile.sexAtBirth} <span className="required">*</span></label>
            <div className="sex-selector">
              <button
                type="button"
                className={`sex-btn ${birthData.sexAtBirth === "male" ? "active" : ""}`}
                onClick={() => setBirthData({ ...birthData, sexAtBirth: "male" })}
              >
                {t.profile.male}
              </button>
              <button
                type="button"
                className={`sex-btn ${birthData.sexAtBirth === "female" ? "active" : ""}`}
                onClick={() => setBirthData({ ...birthData, sexAtBirth: "female" })}
              >
                {t.profile.female}
              </button>
            </div>
          </div>

          {/* 出生地 - 使用CityPicker组件（必填） */}
          <div className="form-section">
            <label className="section-label">{t.profile.birthPlace} <span className="required">*</span></label>
            <CityPicker
              value={selectedCity}
              onChange={setSelectedCity}
              placeholder={t.profile.searchCity}
            />
            {selectedCity && (
              <div className="place-info">
                <span className="place-coords">
                  {selectedCity.lat.toFixed(2)}°N, {selectedCity.lng.toFixed(2)}°E
                </span>
                <span className="place-tz">{selectedCity.timezone}</span>
              </div>
            )}
          </div>

          <button 
            type="submit" 
            className={`submit-button ${!isFormValid ? "disabled" : ""}`}
            disabled={!isFormValid}
          >
            {t.profile.continue}
          </button>
          {(!birthData.sexAtBirth || !selectedCity) && (
            <p className="validation-hint">
              {!birthData.sexAtBirth && t.profile.sexRequired}
              {!birthData.sexAtBirth && !selectedCity && ' / '}
              {!selectedCity && (locale === 'zh' ? '请选择出生地点' : 'Please select birth place')}
            </p>
          )}
        </form>
      </motion.div>

      <style jsx>{`
        .setup-page {
          min-height: 100vh;
          display: flex;
          align-items: center;
          justify-content: center;
          background: var(--bg-middle);
          padding: var(--space-lg);
        }

        .setup-card {
          text-align: center;
          padding: var(--space-2xl) var(--space-3xl);
          max-width: 720px;
          width: 100%;
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-xl);
        }

        @media (min-width: 768px) {
          .setup-card {
            padding: var(--space-3xl) var(--space-4xl);
          }
        }

        .setup-title {
          font-family: Playfair Display, Noto Serif SC, serif;
          font-size: clamp(1.75rem, 3vw, 2.5rem);
          font-weight: 400;
          color: var(--text-primary);
          margin: 0 0 var(--space-xs) 0;
          letter-spacing: -0.02em;
        }

        .setup-subtitle {
          font-size: 1rem;
          color: var(--text-secondary);
          margin: 0 0 var(--space-2xl) 0;
        }

        .setup-form {
          display: grid;
          gap: var(--space-xl);
        }

        @media (min-width: 640px) {
          .setup-form {
            grid-template-columns: 1fr 1fr;
          }
          
          .setup-form .form-section:nth-child(3),
          .setup-form .form-section:nth-child(4) {
            grid-column: span 1;
          }
          
          .setup-form .submit-button,
          .setup-form .validation-hint {
            grid-column: span 2;
          }
        }

        .form-section {
          text-align: left;
        }

        .section-label {
          display: block;
          font-size: 0.9rem;
          font-weight: 500;
          color: var(--text-primary);
          margin-bottom: var(--space-sm);
        }

        .form-row {
          display: flex;
          gap: var(--space-md);
        }

        .time-row {
          align-items: flex-end;
        }

        .time-sep {
          font-size: 1.5rem;
          color: var(--text-tertiary);
          padding-bottom: var(--space-sm);
        }

        .shichen-display {
          padding: var(--space-sm) var(--space-md);
          background: var(--glow-color);
          border-radius: var(--radius-md);
          font-size: 0.9rem;
          color: var(--accent-gold);
          white-space: nowrap;
          margin-bottom: 2px;
        }

        .form-group {
          flex: 1;
          display: flex;
          flex-direction: column;
          gap: 6px;
          text-align: left;
        }

        .form-group.full-width {
          flex: none;
          width: 100%;
        }

        .form-group label {
          font-size: 0.7rem;
          color: var(--text-tertiary);
          text-transform: uppercase;
          letter-spacing: 0.05em;
        }

        .select-wrapper {
          position: relative;
        }

        .select-wrapper select {
          width: 100%;
          padding: var(--space-sm) var(--space-xl) var(--space-sm) var(--space-sm);
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          font-size: 0.95rem;
          color: var(--text-primary);
          cursor: pointer;
          appearance: none;
          transition: border-color 0.2s;
        }

        .select-wrapper select:focus {
          outline: none;
          border-color: var(--accent-gold);
        }

        .select-icon {
          position: absolute;
          right: var(--space-sm);
          top: 50%;
          transform: translateY(-50%);
          color: var(--text-tertiary);
          pointer-events: none;
        }

        /* Place Picker */
        .place-picker {
          position: relative;
        }

        .search-input-wrapper {
          position: relative;
          display: flex;
          align-items: center;
        }

        .search-icon {
          position: absolute;
          left: var(--space-sm);
          color: var(--text-tertiary);
          pointer-events: none;
        }

        .search-input {
          width: 100%;
          padding: var(--space-sm) var(--space-xl) var(--space-sm) var(--space-2xl);
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          font-size: 0.95rem;
          color: var(--text-primary);
          transition: border-color 0.2s;
        }

        .search-input:focus {
          outline: none;
          border-color: var(--accent-gold);
        }

        .search-input::placeholder {
          color: var(--text-tertiary);
        }

        .clear-btn {
          position: absolute;
          right: var(--space-sm);
          background: none;
          border: none;
          color: var(--text-tertiary);
          cursor: pointer;
          padding: 4px;
          display: flex;
          align-items: center;
          justify-content: center;
        }

        .clear-btn:hover {
          color: var(--text-primary);
        }

        .dropdown {
          position: absolute;
          top: 100%;
          left: 0;
          right: 0;
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          margin-top: 4px;
          max-height: 300px;
          overflow-y: auto;
          z-index: 100;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .dropdown-header {
          padding: var(--space-sm) var(--space-md);
          font-size: 0.75rem;
          color: var(--text-tertiary);
          text-transform: uppercase;
          letter-spacing: 0.05em;
          border-bottom: 1px solid var(--card-border);
        }

        .dropdown-item {
          display: flex;
          align-items: center;
          gap: var(--space-sm);
          width: 100%;
          padding: var(--space-sm) var(--space-md);
          background: none;
          border: none;
          text-align: left;
          font-size: 0.9rem;
          color: var(--text-primary);
          cursor: pointer;
          transition: background 0.15s;
        }

        .dropdown-item:hover {
          background: var(--bg-middle);
        }

        .dropdown-item span {
          flex: 1;
        }

        .place-info {
          display: flex;
          justify-content: space-between;
          margin-top: var(--space-xs);
          padding: var(--space-xs) var(--space-sm);
          background: var(--glow-color);
          border-radius: var(--radius-sm);
        }

        .place-coords, .place-tz {
          font-size: 0.75rem;
          color: var(--accent-gold);
        }

        .submit-button {
          width: 100%;
          padding: var(--space-md);
          background: var(--accent-gold);
          border: none;
          border-radius: var(--radius-md);
          font-size: 1rem;
          font-weight: 500;
          color: #fff;
          cursor: pointer;
          margin-top: var(--space-sm);
          transition: opacity 0.2s;
        }

        .submit-button:hover:not(.disabled) {
          opacity: 0.9;
        }

        .submit-button.disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }

        .validation-hint {
          font-size: 0.8rem;
          color: var(--accent-gold);
          text-align: center;
          margin-top: var(--space-sm);
        }

        /* 时间模式切换 */
        .time-mode-toggle {
          display: flex;
          gap: var(--space-xs);
          margin-bottom: var(--space-sm);
        }

        .mode-btn {
          flex: 1;
          padding: var(--space-xs) var(--space-sm);
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-sm);
          font-size: 0.8rem;
          color: var(--text-secondary);
          cursor: pointer;
          transition: all 0.2s;
        }

        .mode-btn.active {
          background: var(--accent-gold);
          border-color: var(--accent-gold);
          color: #fff;
        }

        .time-input {
          width: 100%;
          padding: var(--space-sm);
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          font-size: 1rem;
          color: var(--text-primary);
        }

        .time-input:focus {
          outline: none;
          border-color: var(--accent-gold);
        }

        .time-hint {
          font-size: 0.75rem;
          color: var(--text-tertiary);
          margin-top: var(--space-xs);
        }

        /* 性别选择 */
        .section-hint {
          font-size: 0.75rem;
          color: var(--text-tertiary);
          margin: 0 0 var(--space-sm) 0;
        }

        .required {
          color: #e74c3c;
        }

        .sex-selector {
          display: flex;
          gap: var(--space-md);
        }

        .sex-btn {
          flex: 1;
          padding: var(--space-md);
          background: var(--bg-middle);
          border: 2px solid var(--card-border);
          border-radius: var(--radius-md);
          font-size: 0.95rem;
          color: var(--text-secondary);
          cursor: pointer;
          transition: all 0.2s;
        }

        .sex-btn:hover {
          border-color: var(--accent-gold);
          color: var(--text-primary);
        }

        .sex-btn.active {
          background: var(--glow-color);
          border-color: var(--accent-gold);
          color: var(--accent-gold);
        }

        .skip-button {
          width: 100%;
          padding: var(--space-sm);
          background: none;
          border: none;
          font-size: 0.85rem;
          color: var(--text-tertiary);
          cursor: pointer;
          margin-top: var(--space-sm);
          transition: color 0.2s;
        }

        .skip-button:hover {
          color: var(--text-secondary);
        }

        @media (max-width: 480px) {
          .form-row {
            flex-direction: column;
            gap: var(--space-sm);
          }
          .time-row {
            flex-direction: row;
          }
          .time-sep {
            display: block;
          }
        }
      `}</style>
    </div>
  );
}

function getShichen(hour: number): string {
  const shichen = [
    "子", "子", "丑", "丑", "寅", "寅",
    "卯", "卯", "辰", "辰", "巳", "巳",
    "午", "午", "未", "未", "申", "申",
    "酉", "酉", "戌", "戌", "亥", "亥"
  ];
  return shichen[hour] || "子";
}
