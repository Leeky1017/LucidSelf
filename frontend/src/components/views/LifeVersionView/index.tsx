"use client";

import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import {
  GitBranch,
  GitCommit,
  Target,
  TrendingUp,
  Shield,
  Heart,
  Loader2,
  Info,
  AlertCircle,
} from "lucide-react";
import { useTranslation } from "@/lib/i18n";
import "./styles.css";

interface LifeVersionViewProps {
  userId?: string;
}

export function LifeVersionView({ userId }: LifeVersionViewProps) {
  const { t } = useTranslation();
  const [loading, setLoading] = useState(true);
  const [versionData, setVersionData] = useState<{
    currentVersion: string;
    title: string;
    attributes: Record<string, number>;
  } | null>(null);

  const ATTRIBUTE_CONFIG = [
    { name: t.lifeVersion.career, key: "career", icon: Target },
    { name: t.lifeVersion.wealth, key: "wealth", icon: TrendingUp },
    { name: t.lifeVersion.health, key: "health", icon: Shield },
    { name: t.lifeVersion.relationship, key: "relationship", icon: Heart },
  ];

  useEffect(() => {
    setLoading(false);
    setVersionData(null);
  }, [userId]);

  if (loading) {
    return (
      <div className="life-version-view">
        <div className="loading-state">
          <Loader2 size={32} className="spinner" />
          <p>{t.common.loading}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="life-version-view">
      {/* 顶部状态栏 */}
      <motion.div
        className="version-header"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <div className="current-version-badge">
          <GitBranch size={20} />
          <span className="version-label">{t.lifeVersion.title}</span>
          <span className="version-number">--</span>
          <span className="version-title">{t.lifeVersion.waiting}</span>
        </div>
        <p className="version-tagline">{t.lifeVersion.tagline}</p>
      </motion.div>

      {/* 主内容区域 - 空状态 */}
      <div className="version-content">
        {/* 左侧：版本树 */}
        <motion.div
          className="version-tree-section"
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.2, duration: 0.5 }}
        >
          <h2 className="section-title">
            <GitCommit size={18} />
            {t.lifeVersion.versionHistory}
          </h2>
          <div className="empty-state">
            <AlertCircle size={48} className="empty-icon" />
            <h3>{t.lifeVersion.noVersionData}</h3>
            <p>{t.lifeVersion.noVersionHint}</p>
          </div>
        </motion.div>

        {/* 右侧：属性面板 */}
        <motion.div
          className="attributes-section"
          initial={{ opacity: 0, x: 20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ delay: 0.3, duration: 0.5 }}
        >
          <h2 className="section-title">
            <Target size={18} />
            {t.lifeVersion.growthDimensions}
          </h2>
          <div className="attributes-grid">
            {ATTRIBUTE_CONFIG.map((attr, index) => {
              const Icon = attr.icon;
              return (
                <motion.div
                  key={attr.key}
                  className="attribute-card empty"
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: 0.4 + index * 0.1 }}
                >
                  <div className="attr-header">
                    <Icon size={20} className="attr-icon" />
                    <span className="attr-name">{attr.name}</span>
                  </div>
                  <div className="attr-value">--</div>
                  <div className="attr-bar">
                    <div className="attr-bar-fill" style={{ width: 0 }} />
                  </div>
                </motion.div>
              );
            })}
          </div>

          {/* 大运进度 - 空状态 */}
          <div className="fortune-section">
            <h3 className="subsection-title">{t.lifeVersion.currentFortune}</h3>
            <div className="fortune-info empty">
              <p className="empty-hint">{t.lifeVersion.fortuneHint}</p>
            </div>
          </div>
        </motion.div>
      </div>

      {/* 底部：未来推演入口 */}
      <motion.div
        className="simulation-section"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5, duration: 0.5 }}
      >
        <div className="simulation-card">
          <div className="simulation-info">
            <Info size={20} />
            <div>
              <h3>{t.lifeVersion.futureSimulation}</h3>
              <p>{t.lifeVersion.simulationDesc}</p>
            </div>
          </div>
          <button className="simulation-btn" disabled>
            {t.lifeVersion.comingSoon}
          </button>
        </div>
      </motion.div>
    </div>
  );
}
