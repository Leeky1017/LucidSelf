"use client";

import { motion } from "framer-motion";
import { Moon, Sun, Settings, Zap, GitBranch, Clock, Sparkles } from "lucide-react";
import type { View, Theme } from "@/types/common";
import { useTranslation } from "@/lib/i18n";

interface SidebarProps {
  view: View;
  theme: Theme;
  collapsed: boolean;
  onViewChange: (view: View) => void;
  onThemeToggle: () => void;
  onCollapseToggle: () => void;
  onBackToNow: () => void;
  onOpenSettings?: () => void;
  userName?: string;
}

export function Sidebar({
  view,
  theme,
  collapsed,
  onViewChange,
  onThemeToggle,
  onCollapseToggle,
  onBackToNow,
  onOpenSettings,
  userName,
}: SidebarProps) {
  const { t } = useTranslation();

  return (
    <aside className={`sidebar desktop-only ${collapsed ? 'collapsed' : ''}`}>
      <div className="sidebar-header">
        <div className="logo" onClick={onBackToNow}>
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none" className="text-[color:var(--accent-gold)]">
            <circle cx="16" cy="16" r="12" stroke="currentColor" strokeWidth="1" opacity="0.3"/>
            <circle cx="16" cy="16" r="8" stroke="currentColor" strokeWidth="1" opacity="0.5"/>
            <circle cx="16" cy="16" r="4" stroke="currentColor" strokeWidth="1.5"/>
            <path d="M16 4 L16 28 M4 16 L28 16" stroke="currentColor" strokeWidth="0.5" opacity="0.2"/>
          </svg>
          {!collapsed && (
            <div className="logo-text">
              <span className="logo-name">Lucid Self</span>
              <span className="logo-tagline">{t.brand.tagline}</span>
            </div>
          )}
        </div>
      </div>

      <nav className="sidebar-nav">
        {/* 执行层 - Now */}
        <button
          className={`sidebar-nav-item ${view === 'now' ? 'active' : ''}`}
          onClick={() => onViewChange('now')}
          title={t.sidebar.nowHint}
        >
          <Zap size={18} className="nav-icon" />
          {!collapsed && <span>{t.sidebar.now}</span>}
        </button>
        
        {/* 战略层 - Life Version */}
        <button
          className={`sidebar-nav-item ${view === 'life-version' || view === 'version-tree' ? 'active' : ''}`}
          onClick={() => onViewChange('life-version')}
          title={t.sidebar.lifeVersionHint}
        >
          <GitBranch size={18} className="nav-icon" />
          {!collapsed && <span>{t.sidebar.lifeVersion}</span>}
        </button>
        
        {/* 数据流层 - Timeline */}
        <button
          className={`sidebar-nav-item ${view === 'timeline' ? 'active' : ''}`}
          onClick={() => onViewChange('timeline')}
          title={t.sidebar.timelineHint}
        >
          <Clock size={18} className="nav-icon" />
          {!collapsed && <span>{t.sidebar.timeline}</span>}
        </button>
        
        {/* 分析层 - Insight (原Archive) */}
        <button
          className={`sidebar-nav-item ${view === 'insight' || view === 'archive' ? 'active' : ''}`}
          onClick={() => onViewChange('insight')}
          title={t.sidebar.insightHint}
        >
          <Sparkles size={18} className="nav-icon" />
          {!collapsed && <span>{t.sidebar.insight}</span>}
        </button>
      </nav>

      {/* 用户信息和设置 */}
      {onOpenSettings && (
        <div className="sidebar-user">
          <button className="user-btn" onClick={onOpenSettings}>
            <div className="user-avatar">
              {userName ? userName.charAt(0).toUpperCase() : "?"}
            </div>
            {!collapsed && (
              <>
                <span className="user-name">{userName || t.profile.guest}</span>
                <Settings size={16} className="settings-icon" />
              </>
            )}
          </button>
        </div>
      )}

      <div className="sidebar-footer">
        <button 
          className="theme-toggle-sidebar"
          onClick={onThemeToggle}
          aria-label="Toggle theme"
        >
          <motion.div
            initial={{ rotate: 0 }}
            animate={{ rotate: theme === 'dark' ? 0 : 180 }}
            transition={{ duration: 0.4, ease: [0.4, 0, 0.2, 1] }}
          >
            {theme === 'dark' ? <Moon size={16} /> : <Sun size={16} />}
          </motion.div>
        </button>
        
        <button
          className="collapse-toggle"
          onClick={onCollapseToggle}
          aria-label="Toggle sidebar"
        >
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor">
            <path 
              d={collapsed ? "M6 4L10 8L6 12" : "M10 4L6 8L10 12"} 
              strokeWidth="1.5" 
              strokeLinecap="round" 
              strokeLinejoin="round"
            />
          </svg>
        </button>
      </div>
    </aside>
  );
}
