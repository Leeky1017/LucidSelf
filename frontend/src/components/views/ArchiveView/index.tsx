"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Calendar,
  TrendingUp,
  TrendingDown,
  Minus,
  Sparkles,
  X,
  ChevronRight,
  Repeat,
  Zap,
  Moon
} from "lucide-react";
import type { Theme } from "@/types/common";
import type { ViewMode, CategoryFilter, Pattern, CorePattern, DeepInsight } from "./types";
import { categoryConfig } from "./types";
import { useTranslation } from "@/lib/i18n";

interface Chapter {
  title: string;
  period: string;
  theme: string;
  startDate: Date;
  endDate: Date;
}

interface ArchiveViewProps {
  theme: Theme;
}

export function ArchiveView({ theme }: ArchiveViewProps) {
  const { t } = useTranslation();
  const [viewMode, setViewMode] = useState<ViewMode>('patterns');
  const [categoryFilter, setCategoryFilter] = useState<CategoryFilter>('all');
  const [selectedPattern, setSelectedPattern] = useState<Pattern | null>(null);

  // Real data will come from backend API
  const currentChapter: Chapter = {
    title: '',
    period: '',
    theme: '',
    startDate: new Date(),
    endDate: new Date(Date.now() + 365 * 24 * 60 * 60 * 1000)
  };
  const corePatterns: CorePattern[] = [];
  const allPatterns: Pattern[] = [];
  const deepInsights: DeepInsight[] = [];

  // Calculate chapter progress
  const now = new Date();
  const totalDuration = currentChapter.endDate.getTime() - currentChapter.startDate.getTime();
  const elapsed = now.getTime() - currentChapter.startDate.getTime();
  const progressPercent = Math.min(Math.max(elapsed / totalDuration, 0), 1);

  const filteredPatterns = allPatterns.filter(p =>
    categoryFilter === 'all' || p.category === categoryFilter
  );

  const secondaryPatterns = filteredPatterns.filter(p =>
    !corePatterns.find(cp => cp.id === p.id)
  );

  return (
    <div className="archive">
      {/* Header */}
      <div className="archive-header">
        <div>
          <h1 className="view-title">{t.archive.title}</h1>
          <p className="view-subtitle">{t.archive.subtitle}</p>
        </div>

        <div className="view-toggle">
          <button
            className={`toggle-button ${viewMode === 'patterns' ? 'active' : ''}`}
            onClick={() => setViewMode('patterns')}
          >
            <Repeat size={16} />
            <span>{t.archive.patterns}</span>
          </button>
          <button
            className={`toggle-button ${viewMode === 'insights' ? 'active' : ''}`}
            onClick={() => setViewMode('insights')}
          >
            <Zap size={16} />
            <span>{t.insights.deepInsights}</span>
          </button>
        </div>
      </div>

      {/* Content */}
      <motion.div
        key={viewMode}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.4 }}
      >
        {viewMode === 'patterns' && (
          <div className="patterns-view">
            {/* Current Chapter Hero */}
            <div className="chapter-hero">
              <div className="chapter-header">
                <Calendar size={20} />
                <div className="chapter-title-group">
                  <h2 className="chapter-title">{currentChapter.title}</h2>
                  <p className="chapter-period">{currentChapter.period}</p>
                </div>
              </div>

              {/* Compact Progress Bar */}
              <div className="chapter-progress-bar">
                <div className="progress-info">
                  <span className="progress-percent">{Math.round(progressPercent * 100)}%</span>
                  <span className="progress-label">{t.archive.chapterProgress}</span>
                </div>
                <div className="progress-track">
                  <div
                    className="progress-fill"
                    style={{ width: `${progressPercent * 100}%` }}
                  />
                </div>
              </div>

              <p className="chapter-theme">{currentChapter.theme}</p>

              {/* Core Patterns */}
              <div className="core-patterns-grid">
                {corePatterns.map((pattern, index) => (
                  <motion.div
                    key={pattern.id}
                    className={`core-pattern-card importance-${pattern.importance}`}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.1 }}
                    whileHover={{ y: -4 }}
                    onClick={() => setSelectedPattern(pattern)}
                  >
                    <div className="core-pattern-header">
                      <h3 className="core-pattern-name">{pattern.name}</h3>
                      <div className="trend-indicator">
                        {pattern.trend === 'up' && <TrendingUp size={16} className="trend-up" />}
                        {pattern.trend === 'down' && <TrendingDown size={16} className="trend-down" />}
                        {pattern.trend === 'stable' && <Minus size={16} className="trend-stable" />}
                        <span className="frequency-count">{pattern.frequency}×</span>
                      </div>
                    </div>

                    {/* Mini Trend Chart */}
                    <div className="mini-chart">
                      {pattern.frequencyData.map((value, i) => {
                        const maxValue = Math.max(...pattern.frequencyData);
                        const height = (value / maxValue) * 100;
                        return (
                          <div key={i} className="chart-bar-container">
                            <div
                              className="chart-bar"
                              style={{ height: `${height}%` }}
                            />
                          </div>
                        );
                      })}
                    </div>

                    <div className="core-pattern-tags">
                      {pattern.astrologyTag && (
                        <span className="astro-tag">{pattern.astrologyTag}</span>
                      )}
                      {pattern.psychologyTag && (
                        <span className="psych-tag">{pattern.psychologyTag}</span>
                      )}
                    </div>

                    <p className="core-pattern-description">{pattern.description}</p>

                    {pattern.aiInsight && (
                      <div className="ai-insight">
                        <Sparkles size={14} />
                        <p>{pattern.aiInsight}</p>
                      </div>
                    )}

                    <div className="core-pattern-footer">
                      <span className="last-seen">{t.archive.last}: {pattern.lastSeen}</span>
                      <span className="related-count">{pattern.relatedRecords} {t.archive.records}</span>
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>

            {/* Category Filter */}
            <div className="category-filter">
              {(Object.keys(categoryConfig) as CategoryFilter[]).map(cat => {
                const config = categoryConfig[cat];
                const Icon = config.icon;
                const count = cat === 'all'
                  ? allPatterns.length
                  : allPatterns.filter(p => p.category === cat).length;

                return (
                  <button
                    key={cat}
                    className={`category-button ${categoryFilter === cat ? 'active' : ''}`}
                    onClick={() => setCategoryFilter(cat)}
                  >
                    <Icon size={16} />
                    <span>{config.label}</span>
                    <span className="count-badge">{count}</span>
                  </button>
                );
              })}
            </div>

            {/* All Patterns Grid */}
            {secondaryPatterns.length > 0 && (
              <div className="patterns-section">
                <h3 className="section-title">{t.patterns.allPatterns}</h3>
                <div className="patterns-grid">
                  {secondaryPatterns.map((pattern, index) => (
                    <motion.div
                      key={pattern.id}
                      className="pattern-card"
                      initial={{ opacity: 0, scale: 0.95 }}
                      animate={{ opacity: 1, scale: 1 }}
                      transition={{ delay: index * 0.08 }}
                      whileHover={{ y: -4 }}
                      onClick={() => setSelectedPattern(pattern)}
                    >
                      <div className="pattern-header">
                        <h4 className="pattern-name">{pattern.name}</h4>
                        <div className="pattern-trend">
                          {pattern.trend === 'up' && <TrendingUp size={14} className="trend-up" />}
                          {pattern.trend === 'down' && <TrendingDown size={14} className="trend-down" />}
                          {pattern.trend === 'stable' && <Minus size={14} className="trend-stable" />}
                          <span className="frequency-badge">{pattern.frequency}×</span>
                        </div>
                      </div>

                      <p className="pattern-description">{pattern.description}</p>

                      <div className="pattern-tags">
                        {pattern.astrologyTag && (
                          <span className="tag astro">{pattern.astrologyTag}</span>
                        )}
                        {pattern.psychologyTag && (
                          <span className="tag psych">{pattern.psychologyTag}</span>
                        )}
                      </div>

                      {pattern.aiInsight && (
                        <div className="pattern-insight">
                          <Sparkles size={12} />
                          <p>{pattern.aiInsight}</p>
                        </div>
                      )}

                      <div className="pattern-footer">
                        <span className="last-seen">{pattern.lastSeen}</span>
                        <button className="view-records">
                          {pattern.relatedRecords} {t.archive.records}
                          <ChevronRight size={14} />
                        </button>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {viewMode === 'insights' && (
          <div className="insights-section">
            <div className="section-intro">
              <TrendingUp size={24} className="intro-icon" />
              <p className="intro-text">
                {t.insights.synthesizedDesc}
              </p>
            </div>

            <div className="insights-list">
              {deepInsights.map((insight, index) => (
                <motion.article
                  key={insight.id}
                  className="insight-card"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.15 }}
                  whileHover={{ y: -4 }}
                >
                  <div className="insight-header">
                    {/* Generation Timestamp */}
                    <div className="insight-timestamp">
                      <Sparkles size={14} />
                      <span>{t.insights.generatedOn} {insight.generatedAt}</span>
                      <span className="timestamp-divider">·</span>
                      <span className="lunar-phase">{insight.lunarPhase}</span>
                    </div>

                    <h3 className="insight-title">{insight.title}</h3>

                    {/* Astro Context */}
                    <div className="astro-context">
                      <Moon size={14} className="astro-icon" />
                      <span>{insight.astroContext}</span>
                    </div>

                    <div className="insight-meta">
                      <span className="meta-item">{insight.sources} {t.insights.sources.toLowerCase()}</span>
                      <span className="meta-divider">•</span>
                      <span className="meta-item">{insight.timespan}</span>
                    </div>
                  </div>

                  <blockquote className="insight-synthesis">
                    {insight.synthesis}
                  </blockquote>

                  <button className="explore-button">{t.insights.exploreSources}</button>
                </motion.article>
              ))}
            </div>
          </div>
        )}
      </motion.div>

      {/* Pattern Detail Modal */}
      <AnimatePresence>
        {selectedPattern && (
          <motion.div
            className="pattern-modal-overlay"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSelectedPattern(null)}
          >
            <motion.div
              className="pattern-modal"
              initial={{ opacity: 0, scale: 0.95, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 20 }}
              onClick={(e) => e.stopPropagation()}
            >
              <div className="modal-header">
                <div>
                  <h2 className="modal-title">{selectedPattern.name}</h2>
                  <div className="modal-meta">
                    {selectedPattern.astrologyTag && (
                      <span className="meta-tag astro">{selectedPattern.astrologyTag}</span>
                    )}
                    {selectedPattern.psychologyTag && (
                      <span className="meta-tag psych">{selectedPattern.psychologyTag}</span>
                    )}
                  </div>
                </div>
                <button className="close-button" onClick={() => setSelectedPattern(null)}>
                  <X size={24} />
                </button>
              </div>

              <div className="modal-content">
                {/* Frequency Chart */}
                <div className="detail-section">
                  <h4 className="detail-title">
                    <TrendingUp size={18} />
                    {t.archive.frequencyTimeline}
                  </h4>
                  <div className="frequency-chart">
                    {selectedPattern.frequencyData.map((value, i) => {
                      const maxValue = Math.max(...selectedPattern.frequencyData);
                      const height = (value / maxValue) * 100;
                      const months = ['Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov'];
                      return (
                        <div key={i} className="chart-column">
                          <div className="chart-bar-wrapper">
                            <div
                              className="chart-bar-full"
                              style={{ height: `${height}%` }}
                            >
                              <span className="bar-value">{value}</span>
                            </div>
                          </div>
                          <span className="chart-label">{months[i]}</span>
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* AI Insight */}
                {selectedPattern.aiInsight && (
                  <div className="detail-section insight-box">
                    <Sparkles size={18} />
                    <div>
                      <h4 className="detail-title">{t.archive.aiInsight}</h4>
                      <p className="insight-content">{selectedPattern.aiInsight}</p>
                    </div>
                  </div>
                )}

                {/* Examples */}
                <div className="detail-section">
                  <h4 className="detail-title">{t.archive.commonContexts}</h4>
                  <div className="examples-list">
                    {selectedPattern.examples.map((example, i) => (
                      <div key={i} className="example-item">
                        <span className="example-bullet">•</span>
                        <span>{example}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Related Records */}
                <div className="detail-section">
                  <h4 className="detail-title">{t.archive.relatedRecords}</h4>
                  <button className="records-link">
                    {t.archive.viewAllRecords.replace('{n}', String(selectedPattern.relatedRecords))}
                    <ChevronRight size={16} />
                  </button>
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
