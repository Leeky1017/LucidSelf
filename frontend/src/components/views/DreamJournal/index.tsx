"use client";

import { useState, useEffect, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Moon, Plus, X, Tag, Lightbulb, Sparkles, Sun, Calendar, Loader2 } from "lucide-react";
import type { Theme } from "@/types/common";
import type { DreamEntry } from "./types";
import SimpleRecorder from "@/components/SimpleRecorder";
import DetailedRecorder from "@/components/DetailedRecorder";
import type { DreamEntry as DreamEntryType } from "@/types/dream";
import { api } from "@/lib/api";
import { useTranslation, useLocale } from "@/lib/i18n";

interface DreamJournalProps {
  onClose: () => void;
  userId?: string;
}

export function DreamJournal({ onClose, userId }: DreamJournalProps) {
  const { t } = useTranslation();
  const { locale } = useLocale();
  const [dreams, setDreams] = useState<DreamEntry[]>([]);
  const [showSimple, setShowSimple] = useState(false);
  const [showDetailed, setShowDetailed] = useState(false);
  const [selectedDream, setSelectedDream] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  // 加载梦境列表
  const loadDreams = useCallback(async () => {
    if (!userId) {
      // No user, show empty state
      setDreams([]);
      setLoading(false);
      return;
    }

    try {
      setLoading(true);
      const response = await api.dream.getEntries({ user_id: userId, limit: 50 });
      const loadedDreams: DreamEntry[] = response.entries.map(entry => ({
        id: entry.id,
        date: new Date(entry.created_at).toISOString().split("T")[0],
        time: new Date(entry.created_at).toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit" }),
        title: entry.title || "梦境记录",
        content: entry.final_content,
        mood: entry.mood || "Neutral",
        symbols: entry.tags,
      }));
      setDreams(loadedDreams);
    } catch (err) {
      console.error("Failed to load dreams:", err);
      setDreams([]);
    } finally {
      setLoading(false);
    }
  }, [userId]);

  useEffect(() => {
    loadDreams();
  }, [loadDreams]);

  // 处理保存梦境（从DreamRecorder回调）
  const handleSaveDream = async (dream: DreamEntryType) => {
    // 如果有userId，保存到后端
    if (userId) {
      try {
        await api.dream.saveEntry({
          user_id: userId,
          rawInput: dream.rawInput,
          finalContent: dream.finalContent,
          generatedContent: dream.generatedContent,
          title: dream.title,
          mood: dream.mood,
          tags: dream.tags,
          clarity: dream.clarity,
          status: dream.status,
          mode: dream.mode,
        });
        // 重新加载列表
        await loadDreams();
        return;
      } catch (err) {
        console.error("Failed to save dream:", err);
      }
    }

    // 本地保存（fallback）
    const legacyDream: DreamEntry = {
      id: dream.id,
      date: new Date(dream.createdAt).toISOString().split("T")[0],
      time: new Date(dream.createdAt).toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit" }),
      title: dream.title || `${new Date(dream.createdAt).toLocaleDateString()} 的梦`,
      content: dream.finalContent,
      mood: dream.mood || "Neutral",
      symbols: dream.tags || [],
    };

    setDreams([legacyDream, ...dreams]);
  };

  const selectedDreamData = dreams.find((d) => d.id === selectedDream);

  // 条件渲染：Detailed 时完全替换视图（Figma v2 模式）
  if (showDetailed) {
    return (
      <DetailedRecorder
        onClose={() => setShowDetailed(false)}
        onSave={handleSaveDream}
      />
    );
  }

  // Simple 时也完全替换视图
  if (showSimple) {
    return (
      <SimpleRecorder
        onClose={() => setShowSimple(false)}
        onSave={handleSaveDream}
      />
    );
  }

  // 列表视图
  return (
    <motion.div
      className="dream-journal"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      <div className="journal-header">
        <div>
          <h1 className="journal-title">{t.dream.title}</h1>
          <p className="journal-subtitle">{t.dream.subtitle}</p>
        </div>

        <div className="header-actions">
          <button className="action-button secondary" onClick={() => setShowSimple(true)}>
            <Plus size={20} />
            <span>{t.dream.simpleMode}</span>
          </button>
          <button className="action-button primary" onClick={() => setShowDetailed(true)}>
            <Plus size={20} />
            <span>{t.dream.recordDream}</span>
          </button>
          <button className="action-button" onClick={onClose}>
            <X size={20} />
          </button>
        </div>
      </div>

      <div className="dream-list">
        {dreams.map((dream, index) => (
          <motion.article
            key={dream.id}
            className={`dream - card ${selectedDream === dream.id ? "expanded" : ""} `}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            onClick={() => setSelectedDream(selectedDream === dream.id ? null : dream.id)}
          >
            <div className="dream-card-header">
              <div className="dream-meta">
                <Moon size={16} className="dream-icon" />
                <time className="dream-date">
                  {new Date(dream.date).toLocaleDateString(locale, {
                    month: "short",
                    day: "numeric",
                    year: "numeric",
                  })}
                  {" "}• {dream.time}
                </time>
              </div>
              <span className="dream-mood">{dream.mood}</span>
            </div>

            <h3 className="dream-title">{dream.title}</h3>

            <p className="dream-content">
              {selectedDream === dream.id
                ? dream.content
                : dream.content.length > 150
                  ? `${dream.content.substring(0, 150)}...`
                  : dream.content}
            </p>

            <div className="dream-symbols">
              {dream.symbols.map((symbol) => (
                <span key={symbol} className="symbol-tag">
                  <Tag size={12} />
                  {symbol}
                </span>
              ))}
            </div>

            <AnimatePresence>
              {selectedDream === dream.id && dream.interpretation && (
                <motion.div
                  className="dream-expanded"
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  exit={{ opacity: 0, height: 0 }}
                  transition={{ duration: 0.3 }}
                >
                  <div className="interpretation-section">
                    <div className="section-header">
                      <Lightbulb size={18} />
                      <h4>{t.dream.interpretation}</h4>
                    </div>
                    <p className="interpretation-summary">{dream.interpretation.summary}</p>

                    <div className="symbol-meanings">
                      {dream.interpretation.symbolMeanings.map((item, idx) => (
                        <div key={idx} className="symbol-meaning">
                          <span className="meaning-symbol">{item.symbol}</span>
                          <span className="meaning-arrow">→</span>
                          <span className="meaning-text">{item.meaning}</span>
                        </div>
                      ))}
                    </div>

                    <div className="connection-insight">
                      <Sparkles size={16} />
                      <p>{dream.interpretation.connection}</p>
                    </div>
                  </div>

                  {dream.realityConnection && (
                    <div className="reality-section">
                      <div className="section-header">
                        <Sun size={18} />
                        <h4>{t.dream.realityConnection}</h4>
                      </div>
                      <div className="reality-event">
                        <Calendar size={14} />
                        <span>
                          {new Date(dream.realityConnection.date).toLocaleDateString(locale, {
                            month: "short",
                            day: "numeric",
                          })}
                        </span>
                      </div>
                      <p className="reality-description">{dream.realityConnection.event}</p>
                      <div className="correlation-insight">
                        <p>{dream.realityConnection.correlation}</p>
                      </div>
                    </div>
                  )}
                </motion.div>
              )}
            </AnimatePresence>
          </motion.article>
        ))}
      </div>
    </motion.div>
  );
}
