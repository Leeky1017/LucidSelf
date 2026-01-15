"use client";

import { motion } from "framer-motion";
import { Sparkles, Moon, ListTodo, CheckCircle2, GitBranch } from "lucide-react";
import type { Theme, View } from "@/types/common";
import { ModuleGrid } from "@/components/modules/ModuleGrid";
import { useTranslation } from "@/lib/i18n";

interface NowViewProps {
  theme: Theme;
  onModuleClick: (moduleId: View) => void;
}

export function NowView({ theme, onModuleClick }: NowViewProps) {
  const { t } = useTranslation();

  return (
    <div className="now-view">
      {/* Life Version Status Bar */}
      <motion.div
        className="version-status-bar"
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
        onClick={() => onModuleClick('life-version')}
      >
        <GitBranch size={14} />
        <span className="status-version">Life Version</span>
        <span className="status-hint">查看人生蓝图 →</span>
      </motion.div>

      {/* Compact Insight */}
      <motion.div
        className="compact-insight"
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.1 }}
      >
        <time className="insight-time">{t.nowView.now}</time>
        <p className="insight-text">{t.nowView.focusMessage}</p>
      </motion.div>

      {/* Primary Tools */}
      <motion.div
        className="primary-tools"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2, duration: 0.6 }}
      >
        {/* Playbook Tool */}
        <motion.button
          className="primary-tool playbook-tool"
          onClick={() => onModuleClick('playbook')}
          whileHover={{ y: -4 }}
        >
          <div className="tool-header">
            <div className="tool-icon" style={{ color: 'var(--accent-gold)' }}>
              <Sparkles size={28} strokeWidth={1.5} />
            </div>
            <h3 className="tool-title">{t.nowView.playbook}</h3>
          </div>
          
          <div className="tool-preview">
            <p className="playbook-desc">{t.nowView.playbookDesc}</p>
            <div className="playbook-engines">
              <span className="engine-indicator active">{t.engines.bazi.name}</span>
              <span className="engine-indicator active">{t.engines.ziwei.name}</span>
              <span className="engine-indicator active">{t.engines.tarot.name}</span>
              <span className="engine-indicator active">{t.engines.astro.name}</span>
              <span className="engine-indicator">+4</span>
            </div>
          </div>

          <div className="tool-action">{t.nowView.viewReading}</div>
        </motion.button>

        {/* Dream Journal Tool */}
        <motion.button
          className="primary-tool dream-tool"
          onClick={() => onModuleClick('dream')}
          whileHover={{ y: -4 }}
        >
          <div className="tool-header">
            <div className="tool-icon" style={{ color: 'var(--accent-violet)' }}>
              <Moon size={28} strokeWidth={1.5} />
            </div>
            <h3 className="tool-title">{t.nowView.dreamJournal}</h3>
          </div>
          
          <div className="tool-preview">
            <div className="preview-item">
              <span className="preview-date">{t.nowView.lastNight}</span>
              <p className="preview-text">---</p>
            </div>
            <div className="preview-item">
              <span className="preview-date">{t.nowView.daysAgo.replace('{n}', '2')}</span>
              <p className="preview-text">---</p>
            </div>
          </div>

          <div className="tool-action">{t.nowView.openJournal}</div>
        </motion.button>

        {/* Today Tool */}
        <motion.button
          className="primary-tool today-tool"
          onClick={() => onModuleClick('todo')}
          whileHover={{ y: -4 }}
        >
          <div className="tool-header">
            <div className="tool-icon" style={{ color: 'var(--accent-emerald)' }}>
              <ListTodo size={28} strokeWidth={1.5} />
            </div>
            <h3 className="tool-title">{t.nowView.today}</h3>
          </div>
          
          <div className="tool-preview">
            <p className="playbook-desc">{t.nowView.trackDaily}</p>
            <div className="today-stats">
              <span className="stat-badge">
                <CheckCircle2 size={14} />
                {t.nowView.todoStatus}
              </span>
            </div>
          </div>

          <div className="tool-action">{t.nowView.recordNow}</div>
        </motion.button>
      </motion.div>

      {/* Other Tools */}
      <motion.div
        className="other-tools-section"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4, duration: 0.6 }}
      >
        <h2 className="section-title">{t.nowView.moreTools}</h2>
        <ModuleGrid onModuleClick={onModuleClick} />
      </motion.div>
    </div>
  );
}
