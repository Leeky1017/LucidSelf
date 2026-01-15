"use client";

import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, User, Calendar, MapPin, LogOut, ChevronRight, Globe, Clock, Check } from "lucide-react";
import { useUser, type BirthData } from "@/contexts/UserContext";
import { useTranslation, useLocale } from "@/lib/i18n";
import { useTheme, THEMES } from "@/contexts/ThemeContext";
import { CityPicker } from "@/components/common/CityPicker";
import { EditableSelect } from "@/components/common/EditableSelect";

// 生成选项
const currentYear = new Date().getFullYear();
const years = Array.from({ length: 100 }, (_, i) => currentYear - i);
const months = Array.from({ length: 12 }, (_, i) => i + 1);
const hours = Array.from({ length: 24 }, (_, i) => i);
const minutes = Array.from({ length: 60 }, (_, i) => i);

// 获取某月的天数
function getDaysInMonth(year: number, month: number): number {
  return new Date(year, month, 0).getDate();
}

// 时辰映射
function getShichen(hour: number): string {
  const shichen = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥'];
  const index = Math.floor((hour + 1) % 24 / 2);
  return shichen[index];
}

// 城市信息类型
interface SelectedCity {
  displayName: string;
  province: string;
  city: string;
  lat: number;
  lng: number;
  timezone: string;
  countryCode?: string;
}

interface UserSettingsProps {
  onClose: () => void;
  onLanguageSettings?: () => void;
}

export function UserSettings({ onClose, onLanguageSettings }: UserSettingsProps) {
  const { t, dir } = useTranslation();
  const { locale, availableLocales } = useLocale();
  const { user, updateBirthData, logout } = useUser();
  const { theme, setTheme } = useTheme();
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState<Partial<BirthData>>({});
  const [selectedCity, setSelectedCity] = useState<SelectedCity | null>(null);
  const [isSaving, setIsSaving] = useState(false);

  // 初始化编辑数据
  useEffect(() => {
    if (isEditing && user?.birthData) {
      setEditData({
        year: user.birthData.year,
        month: user.birthData.month,
        day: user.birthData.day,
        hour: user.birthData.hour,
        minute: user.birthData.minute || 0,
        sexAtBirth: user.birthData.sexAtBirth,
      });
      if (user.birthData.city) {
        setSelectedCity({
          displayName: user.birthData.city,
          province: '',
          city: user.birthData.city,
          lat: user.birthData.latitude || 0,
          lng: user.birthData.longitude || 0,
          timezone: user.birthData.timezone || 'Asia/Shanghai',
        });
      }
    }
  }, [isEditing, user?.birthData]);

  // 根据年月计算有效天数
  const validDays = editData.year && editData.month 
    ? getDaysInMonth(editData.year, editData.month) 
    : 31;

  // 当年月变化时，自动修正无效的日期
  useEffect(() => {
    if (editData.day && editData.day > validDays) {
      setEditData(prev => ({ ...prev, day: validDays }));
    }
  }, [editData.year, editData.month, validDays, editData.day]);

  const handleSave = async () => {
    if (editData.year && editData.month && editData.day && editData.hour !== undefined && editData.sexAtBirth && selectedCity) {
      setIsSaving(true);
      const completeBirthData: BirthData = {
        year: editData.year,
        month: editData.month,
        day: editData.day,
        hour: editData.hour,
        minute: editData.minute || 0,
        sexAtBirth: editData.sexAtBirth,
        city: selectedCity.displayName,
        latitude: selectedCity.lat,
        longitude: selectedCity.lng,
        timezone: selectedCity.timezone,
      };
      await updateBirthData(completeBirthData);
      setIsSaving(false);
      setIsEditing(false);
    }
  };

  const handleLogout = () => {
    logout();
    onClose();
  };

  const isFormValid = editData.year && editData.month && editData.day && 
                      editData.hour !== undefined && editData.sexAtBirth && selectedCity;

  return (
    <motion.div
      className="settings-page"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      dir={dir}
    >
      <div className="settings-container">
        <div className="settings-header">
          <h2>{t.settings.title}</h2>
          <button className="close-btn" onClick={onClose}>
            <X size={20} />
          </button>
        </div>

        <div className="settings-content">
          {/* 语言设置 - 导航入口 */}
          {onLanguageSettings && (
            <div className="settings-section">
              <div className="section-title">{t.settings.language}</div>
              <button className="nav-item" onClick={onLanguageSettings}>
                <Globe size={18} />
                <div className="nav-content">
                  <span className="nav-label">{t.settings.selectLanguage}</span>
                  <span className="nav-value">{availableLocales[locale].nativeName}</span>
                </div>
                <ChevronRight size={18} />
              </button>
            </div>
          )}

          {/* 主题设置 */}
          <div className="settings-section">
            <div className="section-title">{t.settings.theme}</div>
            <div className="theme-grid">
              {THEMES.map(themeItem => (
                <button
                  key={themeItem.id}
                  className={`theme-card ${theme === themeItem.id ? 'active' : ''} theme-${themeItem.id}`}
                  onClick={() => setTheme(themeItem.id)}
                >
                  <span className="theme-preview" data-theme-preview={themeItem.id}></span>
                  <span className="theme-name">{locale === 'zh' ? themeItem.nameZh : themeItem.name}</span>
                </button>
              ))}
            </div>
          </div>

          {/* 用户信息 */}
          <div className="settings-section">
            <div className="section-title">{t.nav.profile}</div>

            <div className="info-card">
              <div className="info-row">
                <User size={18} />
                <div className="info-content">
                  <span className="info-label">{t.profile.name}</span>
                  <span className="info-value">{user?.name || t.profile.guest}</span>
                </div>
              </div>
            </div>
          </div>

          {/* 出生信息 */}
          <div className="settings-section birth-section">
            <div className="section-header">
              <div className="section-title">{t.profile.birthInfo}</div>
              {!isEditing && (
                <button className="edit-btn" onClick={() => setIsEditing(true)}>
                  {t.common.edit}
                </button>
              )}
            </div>

            <AnimatePresence mode="wait">
              {isEditing ? (
                <motion.div 
                  className="birth-edit-form"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -10 }}
                  key="edit"
                >
                  {/* 出生日期 */}
                  <div className="form-section">
                    <label className="form-label">{t.profile.dateOfBirth}</label>
                    <div className="date-row">
                      <EditableSelect
                        label={t.profile.birthYear}
                        value={editData.year || 1990}
                        onChange={(v) => setEditData({ ...editData, year: v })}
                        options={years.map(y => ({ value: y, label: String(y) }))}
                        min={1920}
                        max={currentYear}
                      />
                      <EditableSelect
                        label={t.profile.birthMonth}
                        value={editData.month || 1}
                        onChange={(v) => setEditData({ ...editData, month: v })}
                        options={months.map(m => ({ value: m, label: String(m) }))}
                        min={1}
                        max={12}
                      />
                      <EditableSelect
                        label={t.profile.birthDay}
                        value={editData.day || 1}
                        onChange={(v) => setEditData({ ...editData, day: v })}
                        options={Array.from({ length: validDays }, (_, i) => ({ value: i + 1, label: String(i + 1) }))}
                        min={1}
                        max={validDays}
                      />
                    </div>
                  </div>

                  {/* 出生时间 */}
                  <div className="form-section">
                    <label className="form-label">{t.profile.timeOfBirth}</label>
                    <div className="time-row">
                      <EditableSelect
                        label={t.profile.birthHour}
                        value={editData.hour ?? 12}
                        onChange={(v) => setEditData({ ...editData, hour: v })}
                        options={hours.map(h => ({ value: h, label: String(h).padStart(2, '0') }))}
                        min={0}
                        max={23}
                        formatDisplay={(v) => String(v).padStart(2, '0')}
                      />
                      <span className="time-separator">:</span>
                      <EditableSelect
                        label={t.profile.birthMinute}
                        value={editData.minute ?? 0}
                        onChange={(v) => setEditData({ ...editData, minute: v })}
                        options={minutes.map(m => ({ value: m, label: String(m).padStart(2, '0') }))}
                        min={0}
                        max={59}
                        formatDisplay={(v) => String(v).padStart(2, '0')}
                      />
                      {locale === 'zh' && (
                        <div className="shichen-badge">
                          {getShichen(editData.hour || 0)}时
                        </div>
                      )}
                    </div>
                  </div>

                  {/* 出生性别 */}
                  <div className="form-section">
                    <label className="form-label">{t.profile.sexAtBirth}</label>
                    <div className="sex-selector">
                      <button
                        type="button"
                        className={`sex-btn ${editData.sexAtBirth === "male" ? "active" : ""}`}
                        onClick={() => setEditData({ ...editData, sexAtBirth: "male" })}
                      >
                        {t.profile.male}
                      </button>
                      <button
                        type="button"
                        className={`sex-btn ${editData.sexAtBirth === "female" ? "active" : ""}`}
                        onClick={() => setEditData({ ...editData, sexAtBirth: "female" })}
                      >
                        {t.profile.female}
                      </button>
                    </div>
                  </div>

                  {/* 出生地点 */}
                  <div className="form-section">
                    <label className="form-label">{t.profile.birthPlace}</label>
                    <CityPicker
                      value={selectedCity}
                      onChange={setSelectedCity}
                      placeholder={t.profile.searchCity}
                    />
                    {selectedCity && (
                      <div className="city-info">
                        <span className="coords">{selectedCity.lat.toFixed(2)}°N, {selectedCity.lng.toFixed(2)}°E</span>
                        <span className="timezone">{selectedCity.timezone}</span>
                      </div>
                    )}
                  </div>

                  {/* 操作按钮 */}
                  <div className="form-actions">
                    <button className="cancel-btn" onClick={() => setIsEditing(false)}>
                      {t.common.cancel}
                    </button>
                    <button 
                      className={`save-btn ${!isFormValid ? 'disabled' : ''}`} 
                      onClick={handleSave}
                      disabled={!isFormValid || isSaving}
                    >
                      {isSaving ? (
                        <span className="saving">...</span>
                      ) : (
                        <>
                          <Check size={16} />
                          {t.common.save}
                        </>
                      )}
                    </button>
                  </div>
                </motion.div>
              ) : (
                <motion.div 
                  className="birth-display"
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -10 }}
                  key="display"
                >
                  {user?.birthData ? (
                    <>
                      <div className="info-row">
                        <div className="info-icon">
                          <Calendar size={18} />
                        </div>
                        <div className="info-content">
                          <span className="info-label">{t.profile.date}</span>
                          <span className="info-value">
                            {user.birthData.year}/{String(user.birthData.month).padStart(2, '0')}/{String(user.birthData.day).padStart(2, '0')}
                          </span>
                        </div>
                      </div>
                      <div className="info-row">
                        <div className="info-icon">
                          <Clock size={18} />
                        </div>
                        <div className="info-content">
                          <span className="info-label">{t.profile.time}</span>
                          <span className="info-value">
                            {String(user.birthData.hour).padStart(2, "0")}:{String(user.birthData.minute || 0).padStart(2, "0")}
                            {locale === 'zh' && (
                              <span className="shichen-text">（{getShichen(user.birthData.hour)}时）</span>
                            )}
                          </span>
                        </div>
                      </div>
                      {user.birthData.sexAtBirth && (
                        <div className="info-row">
                          <div className="info-icon">
                            <User size={18} />
                          </div>
                          <div className="info-content">
                            <span className="info-label">{t.profile.sexAtBirth}</span>
                            <span className="info-value">
                              {user.birthData.sexAtBirth === 'male' ? t.profile.male : t.profile.female}
                            </span>
                          </div>
                        </div>
                      )}
                      {user.birthData.city && (
                        <div className="info-row">
                          <div className="info-icon">
                            <MapPin size={18} />
                          </div>
                          <div className="info-content">
                            <span className="info-label">{t.profile.birthPlace}</span>
                            <span className="info-value">{user.birthData.city}</span>
                            {(user.birthData.latitude && user.birthData.longitude) && (
                              <span className="info-sub">
                                {user.birthData.latitude.toFixed(2)}°N, {user.birthData.longitude.toFixed(2)}°E
                                {user.birthData.timezone && ` · ${user.birthData.timezone}`}
                              </span>
                            )}
                          </div>
                        </div>
                      )}
                    </>
                  ) : (
                    <div className="no-data">
                      <p>{t.profile.noBirthData}</p>
                      <button className="setup-btn" onClick={() => setIsEditing(true)}>
                        {t.profile.setupNow || '立即设置'}
                      </button>
                    </div>
                  )}
                </motion.div>
              )}
            </AnimatePresence>
          </div>

          {/* 退出登录 */}
          <div className="settings-section">
            <button className="logout-btn" onClick={handleLogout}>
              <LogOut size={18} />
              <span>{t.nav.logout}</span>
              <ChevronRight size={18} />
            </button>
          </div>
        </div>
      </div>

      <style jsx>{`
        .settings-page {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          width: 100vw;
          min-height: 100vh;
          background: var(--bg-middle);
          display: flex;
          align-items: flex-start;
          justify-content: center;
          padding: var(--space-2xl);
          z-index: 200;
          overflow-y: auto;
        }

        .settings-container {
          width: 100%;
          max-width: 1200px;
          background: transparent;
          border: none;
          border-radius: 0;
          overflow: visible;
        }

        .settings-content {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
          gap: var(--space-xl);
          padding: var(--space-xl) 0;
        }

        @media (min-width: 768px) {
          .settings-content {
            grid-template-columns: repeat(2, 1fr);
          }
        }

        @media (min-width: 1024px) {
          .settings-content {
            grid-template-columns: repeat(3, 1fr);
          }
        }

        .settings-header {
          display: flex;
          align-items: center;
          justify-content: space-between;
          padding: var(--space-lg);
          border-bottom: 1px solid var(--card-border);
        }

        .settings-header h2 {
          font-family: Playfair Display, serif;
          font-size: 1.5rem;
          font-weight: 400;
          margin: 0;
          color: var(--text-primary);
        }

        .close-btn {
          display: flex;
          align-items: center;
          justify-content: center;
          width: 36px;
          height: 36px;
          background: none;
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          color: var(--text-secondary);
          cursor: pointer;
          transition: all 0.2s;
        }

        .close-btn:hover {
          background: var(--bg-middle);
          color: var(--text-primary);
        }

        .settings-section {
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-lg);
          padding: var(--space-lg);
          margin-bottom: 0;
        }

        .section-header {
          display: flex;
          align-items: center;
          justify-content: space-between;
          margin-bottom: var(--space-sm);
        }

        .section-title {
          font-size: 0.75rem;
          font-weight: 500;
          color: var(--text-tertiary);
          text-transform: uppercase;
          letter-spacing: 0.1em;
          margin-bottom: var(--space-sm);
        }

        .section-header .section-title {
          margin-bottom: 0;
        }

        .edit-btn {
          background: none;
          border: none;
          font-size: 0.85rem;
          color: var(--accent-gold);
          cursor: pointer;
          transition: opacity 0.2s;
        }

        .edit-btn:hover {
          opacity: 0.8;
        }

        .info-card {
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-lg);
          padding: var(--space-md);
        }

        .info-row {
          display: flex;
          align-items: center;
          gap: var(--space-md);
          padding: var(--space-sm) 0;
          color: var(--text-secondary);
        }

        .info-row:not(:last-child) {
          border-bottom: 1px solid var(--card-border);
        }

        .info-content {
          flex: 1;
          display: flex;
          flex-direction: column;
          gap: 2px;
        }

        .info-label {
          font-size: 0.75rem;
          color: var(--text-tertiary);
        }

        .info-value {
          font-size: 0.95rem;
          color: var(--text-primary);
        }

        .info-sub {
          font-size: 0.75rem;
          color: var(--accent-gold);
          margin-top: 2px;
        }

        .no-data {
          color: var(--text-tertiary);
          font-size: 0.9rem;
          text-align: center;
          padding: var(--space-xl);
        }

        .no-data p {
          margin: 0 0 var(--space-md) 0;
        }

        .setup-btn {
          background: var(--accent-gold);
          color: white;
          border: none;
          padding: var(--space-sm) var(--space-lg);
          border-radius: var(--radius-md);
          font-size: 0.9rem;
          cursor: pointer;
          transition: opacity 0.2s;
        }

        .setup-btn:hover {
          opacity: 0.9;
        }

        /* Birth Section */
        .birth-section {
          grid-column: span 1;
        }

        @media (min-width: 768px) {
          .birth-section {
            grid-column: span 2;
          }
        }

        .birth-display {
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-lg);
          padding: var(--space-md);
        }

        .birth-display .info-row {
          display: flex;
          align-items: flex-start;
          gap: var(--space-md);
          padding: var(--space-md) 0;
        }

        .birth-display .info-row:not(:last-child) {
          border-bottom: 1px solid var(--card-border);
        }

        .birth-display .info-icon {
          width: 36px;
          height: 36px;
          display: flex;
          align-items: center;
          justify-content: center;
          background: var(--glow-color);
          border-radius: var(--radius-md);
          color: var(--accent-gold);
          flex-shrink: 0;
        }

        .shichen-text {
          color: var(--accent-gold);
          font-size: 0.85rem;
          margin-left: var(--space-xs);
        }

        /* Birth Edit Form */
        .birth-edit-form {
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-lg);
          padding: var(--space-lg);
        }

        .form-section {
          margin-bottom: var(--space-lg);
        }

        .form-section:last-of-type {
          margin-bottom: 0;
        }

        .form-label {
          display: block;
          font-size: 0.9rem;
          font-weight: 500;
          color: var(--text-primary);
          margin-bottom: var(--space-sm);
        }

        .date-row, .time-row {
          display: flex;
          gap: var(--space-md);
          align-items: flex-end;
        }

        .time-separator {
          font-size: 1.5rem;
          color: var(--text-tertiary);
          padding-bottom: var(--space-sm);
        }

        .shichen-badge {
          padding: var(--space-sm) var(--space-md);
          background: var(--glow-color);
          border-radius: var(--radius-md);
          font-size: 0.9rem;
          color: var(--accent-gold);
          white-space: nowrap;
          margin-bottom: 2px;
        }

        .sex-selector {
          display: flex;
          gap: var(--space-sm);
        }

        .sex-btn {
          flex: 1;
          padding: var(--space-md);
          background: var(--card-bg);
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
          background: var(--accent-gold);
          border-color: var(--accent-gold);
          color: white;
        }

        .city-info {
          display: flex;
          gap: var(--space-md);
          margin-top: var(--space-sm);
          font-size: 0.8rem;
        }

        .city-info .coords {
          color: var(--text-tertiary);
        }

        .city-info .timezone {
          color: var(--accent-gold);
        }

        .form-actions {
          display: flex;
          gap: var(--space-md);
          margin-top: var(--space-xl);
          padding-top: var(--space-lg);
          border-top: 1px solid var(--card-border);
        }

        .cancel-btn, .save-btn {
          flex: 1;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: var(--space-xs);
          padding: var(--space-md);
          border-radius: var(--radius-md);
          font-size: 0.95rem;
          font-weight: 500;
          cursor: pointer;
          transition: all 0.2s;
        }

        .cancel-btn {
          background: none;
          border: 1px solid var(--card-border);
          color: var(--text-secondary);
        }

        .cancel-btn:hover {
          background: var(--card-bg);
          border-color: var(--text-tertiary);
        }

        .save-btn {
          background: var(--accent-gold);
          border: none;
          color: white;
        }

        .save-btn:hover:not(.disabled) {
          opacity: 0.9;
        }

        .save-btn.disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }

        .logout-btn {
          display: flex;
          align-items: center;
          gap: var(--space-md);
          width: 100%;
          padding: var(--space-md);
          background: none;
          border: 1px solid var(--card-border);
          border-radius: var(--radius-lg);
          color: #e53935;
          cursor: pointer;
          transition: all 0.2s;
        }

        .logout-btn span {
          flex: 1;
          text-align: left;
        }

        .logout-btn:hover {
          background: rgba(229, 57, 53, 0.1);
          border-color: rgba(229, 57, 53, 0.3);
        }

        .nav-item {
          display: flex;
          align-items: center;
          gap: var(--space-md);
          width: 100%;
          padding: var(--space-md);
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-lg);
          color: var(--text-secondary);
          cursor: pointer;
          transition: all 0.2s;
          text-align: left;
        }

        .nav-item:hover {
          background: var(--card-bg);
          border-color: var(--accent-gold);
        }

        .nav-content {
          flex: 1;
          display: flex;
          flex-direction: column;
          gap: 2px;
        }

        .nav-label {
          font-size: 0.9rem;
          color: var(--text-primary);
        }

        .nav-value {
          font-size: 0.8rem;
          color: var(--accent-gold);
        }

        .theme-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(100px, 1fr));
          gap: var(--space-sm);
        }

        .theme-card {
          display: flex;
          flex-direction: column;
          align-items: center;
          gap: var(--space-xs);
          padding: var(--space-md);
          background: var(--bg-middle);
          border: 2px solid var(--card-border);
          border-radius: var(--radius-lg);
          cursor: pointer;
          transition: all 0.2s;
        }

        .theme-card:hover {
          border-color: var(--accent-gold);
        }

        .theme-card.active {
          border-color: var(--accent-gold);
          background: var(--accent-gold);
        }

        .theme-card.active .theme-name {
          color: white;
        }

        .theme-preview {
          width: 32px;
          height: 32px;
          border-radius: 50%;
          border: 2px solid var(--card-border);
        }

        .theme-preview[data-theme-preview="light"] {
          background: linear-gradient(135deg, #fff 50%, #fafafa 50%);
          border-color: #e8e8e8;
        }

        .theme-preview[data-theme-preview="dark"] {
          background: linear-gradient(135deg, #151515 50%, #0a0a0a 50%);
          border-color: #242424;
        }

        .theme-preview[data-theme-preview="cyber"] {
          background: linear-gradient(135deg, #00f0ff 50%, #0a0a12 50%);
          border-color: #1a1a3a;
        }

        .theme-preview[data-theme-preview="kawaii"] {
          background: linear-gradient(135deg, #ff8fab 50%, #fff5f7 50%);
          border-color: #ffe0e8;
        }

        .theme-preview[data-theme-preview="nature"] {
          background: linear-gradient(135deg, #7cb342 50%, #f5f9f0 50%);
          border-color: #d5e8c8;
        }

        .theme-name {
          font-size: 0.8rem;
          color: var(--text-primary);
          font-weight: 500;
        }
      `}</style>
    </motion.div>
  );
}
