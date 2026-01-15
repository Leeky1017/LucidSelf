"use client";

import { useState, useCallback, MouseEvent, useEffect, useRef } from "react";
import type { ReactNode } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Settings,
  X,
  Clock,
  Calendar,
  CalendarDays,
  CalendarRange,
  Check,
  Loader2,
  AlertTriangle,
} from "lucide-react";
import type { TimeScope, ReadingParagraph } from "./types";
import { engines, sourceInfo } from "./config";
import { api, type BirthData, type PlaybookReadingResponse } from "@/lib/api";
import { useTranslation, useLocale } from "@/lib/i18n";

// ===== Markdown 解析 =====
interface ContentSection {
  type: "heading" | "paragraph" | "list-item";
  content: string;
}

function parseMarkdownContent(text: string): ContentSection[] {
  const sections: ContentSection[] = [];
  const lines = text.split("\n");
  
  let currentParagraph = "";
  
  for (const line of lines) {
    const trimmed = line.trim();
    
    // 跳过空行，但先保存当前段落
    if (!trimmed) {
      if (currentParagraph) {
        sections.push({ type: "paragraph", content: currentParagraph.trim() });
        currentParagraph = "";
      }
      continue;
    }
    
    // 标题 (### 或 **)
    if (trimmed.startsWith("###") || trimmed.startsWith("**")) {
      // 先保存之前的段落
      if (currentParagraph) {
        sections.push({ type: "paragraph", content: currentParagraph.trim() });
        currentParagraph = "";
      }
      
      let headingText = trimmed
        .replace(/^###\s*/, "")
        .replace(/^\*\*/, "")
        .replace(/\*\*$/, "")
        .replace(/\*\*[:：]\s*/, "")
        .trim();
      
      if (headingText) {
        sections.push({ type: "heading", content: headingText });
      }
      continue;
    }
    
    // 列表项 (- 或数字.)
    if (trimmed.match(/^[-•]\s+/) || trimmed.match(/^\d+\.\s+/)) {
      if (currentParagraph) {
        sections.push({ type: "paragraph", content: currentParagraph.trim() });
        currentParagraph = "";
      }
      
      const listContent = trimmed
        .replace(/^[-•]\s+/, "")
        .replace(/^\d+\.\s+/, "")
        .trim();
      
      sections.push({ type: "list-item", content: listContent });
      continue;
    }
    
    // 普通文本，累积到段落
    currentParagraph += (currentParagraph ? " " : "") + trimmed;
  }
  
  // 保存最后的段落
  if (currentParagraph) {
    sections.push({ type: "paragraph", content: currentParagraph.trim() });
  }
  
  return sections;
}

function getHeadingIcon(heading: string): string {
  const h = heading.toLowerCase();
  
  if (h.includes("主题") || h.includes("theme") || h.includes("概览")) return "✦";
  if (h.includes("宜") || h.includes("适合") || h.includes("recommend")) return "✓";
  if (h.includes("慎") || h.includes("避") || h.includes("caution") || h.includes("风险")) return "⚠";
  if (h.includes("建议") || h.includes("advice") || h.includes("策略")) return "→";
  if (h.includes("机会") || h.includes("opportunity")) return "★";
  if (h.includes("关键") || h.includes("key") || h.includes("节点")) return "◆";
  if (h.includes("关键词") || h.includes("keyword")) return "◇";
  
  return "•";
}

// ===== 前端会话缓存 =====
// 防止同一会话内重复请求同一数据
interface CacheEntry {
  data: PlaybookReadingResponse;
  timestamp: number;
}

const sessionCache = new Map<string, CacheEntry>();

// 获取 ISO 周数（与后端 Python isocalendar 保持一致）
function getISOWeek(date: Date): { year: number; week: number } {
  const d = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
  const dayNum = d.getUTCDay() || 7;
  d.setUTCDate(d.getUTCDate() + 4 - dayNum);
  const yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
  const weekNo = Math.ceil((((d.getTime() - yearStart.getTime()) / 86400000) + 1) / 7);
  return { year: d.getUTCFullYear(), week: weekNo };
}

function getCacheKey(userId: string, timeScope: string): string {
  const today = new Date();
  let dateKey: string;
  
  switch (timeScope) {
    case "day":
      dateKey = today.toISOString().split("T")[0];
      break;
    case "week":
      // 使用 ISO 周数，与后端 Python isocalendar() 一致
      const { year, week } = getISOWeek(today);
      dateKey = `${year}-W${String(week).padStart(2, "0")}`;
      break;
    case "month":
      dateKey = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}`;
      break;
    case "year":
      dateKey = String(today.getFullYear());
      break;
    default:
      dateKey = today.toISOString().split("T")[0];
  }
  
  return `playbook:${userId}:${timeScope}:${dateKey}`;
}

function getFromCache(key: string): PlaybookReadingResponse | null {
  const entry = sessionCache.get(key);
  if (!entry) return null;
  
  // 会话内缓存有效期: 10分钟
  const maxAge = 10 * 60 * 1000;
  if (Date.now() - entry.timestamp > maxAge) {
    sessionCache.delete(key);
    return null;
  }
  
  return entry.data;
}

function setToCache(key: string, data: PlaybookReadingResponse): void {
  sessionCache.set(key, { data, timestamp: Date.now() });
}

interface PlaybookProps {
  onClose: () => void;
  birthData?: BirthData | null;
  userId?: string;
}

export function Playbook({ onClose, birthData, userId }: PlaybookProps) {
  const { t } = useTranslation();
  const { locale } = useLocale();
  const [showSettings, setShowSettings] = useState(false);
  const [activeEngines, setActiveEngines] = useState(engines);
  const [timeScope, setTimeScope] = useState<TimeScope>("day");
  const [selectedSource, setSelectedSource] = useState<string | null>(null);
  const [popoverPosition, setPopoverPosition] = useState<{ x: number; y: number } | null>(null);

  // API状态
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [reading, setReading] = useState<{
    summary: string;
    readings: Array<{
      engine: string;
      content: string;
      highlights: string[];
    }>;
  } | null>(null);

  // 获取解读（带缓存）
  const fetchReading = useCallback(async () => {
    if (!birthData || !userId) {
      setReading(null);
      setLoading(false);
      return;
    }

    // 前置校验
    if (
      birthData.latitude === undefined ||
      birthData.longitude === undefined ||
      birthData.timezone === undefined
    ) {
      setError(t.playbook.missingLocation);
      setReading(null);
      setLoading(false);
      return;
    }

    // ===== 检查前端缓存 =====
    const cacheKey = getCacheKey(userId, timeScope);
    const cached = getFromCache(cacheKey);
    if (cached) {
      console.log(`[Playbook] Cache HIT: ${cacheKey}`);
      setReading({
        summary: cached.paragraphs.map(p => p.text).join("\n\n"),
        readings: cached.paragraphs.map((p, i) => ({
          engine: `Engine ${i + 1}`,
          content: p.text,
          highlights: p.inline_sources?.map(s => s.sources.join(", ")) || [],
        })),
      });
      setLoading(false);
      return;
    }

    console.log(`[Playbook] Cache MISS: ${cacheKey}, fetching...`);
    setLoading(true);
    setError(null);

    try {
      const response = await api.playbook.getReading({
        user_id: userId,
        birth_data: birthData,
        engines: activeEngines.filter(e => e.enabled).map(e => e.id),
        time_scope: timeScope,
        language: locale,
      });

      // ===== 写入前端缓存 =====
      setToCache(cacheKey, response);
      console.log(`[Playbook] Cached: ${cacheKey}`);

      if (response.paragraphs && response.paragraphs.length > 0) {
        setReading({
          summary: response.paragraphs.map(p => p.text).join("\n\n"),
          readings: response.paragraphs.map((p, i) => ({
            engine: `Engine ${i + 1}`,
            content: p.text,
            highlights: p.inline_sources?.map(s => s.sources.join(", ")) || [],
          })),
        });
      } else {
        setReading(null);
      }
    } catch (err) {
      const message = err instanceof Error ? err.message : t.common.error;
      setError(`${t.playbook.backendError}: ${message}`);
      setReading(null);
    } finally {
      setLoading(false);
    }
  }, [birthData, userId, activeEngines, timeScope, locale]);

  // 当有出生信息时自动获取解读
  useEffect(() => {
    if (birthData && userId) {
      fetchReading();
    } else {
      setLoading(false);
    }
  }, [birthData, userId, timeScope]);

  const toggleEngine = (id: string) => {
    setActiveEngines((prev) => prev.map((e) => (e.id === id ? { ...e, enabled: !e.enabled } : e)));
  };

  const enabledCount = activeEngines.filter((e) => e.enabled).length;

  const handleSourceClick = (event: MouseEvent, sources: string[]) => {
    event.preventDefault();
    event.stopPropagation();

    const rect = (event.target as HTMLElement).getBoundingClientRect();
    const viewportHeight = window.innerHeight;
    const popoverHeight = 400; // 估算 popover 高度

    // 水平位置：点击元素的中心
    let x = rect.left + rect.width / 2;

    // 垂直位置：优先屏幕中央，确保不超出边界
    let y = viewportHeight / 2 - popoverHeight / 2;

    // 边界检测：确保不超出顶部
    if (y < 20) y = 20;
    // 边界检测：确保不超出底部
    if (y + popoverHeight > viewportHeight - 20) {
      y = viewportHeight - popoverHeight - 20;
    }

    setPopoverPosition({ x, y });
    setSelectedSource(sources[0]);
  };

  const handleClosePopover = useCallback(() => {
    setSelectedSource(null);
    setPopoverPosition(null);
  }, []);

  const renderTextWithSources = (paragraph: ReadingParagraph, paragraphIndex: number) => {
    const { text, inlineSources } = paragraph;
    const parts: ReactNode[] = [];
    let lastIndex = 0;

    const sortedSources = [...inlineSources].sort((a, b) => a.start - b.start);

    sortedSources.forEach((source, idx) => {
      if (source.start > lastIndex) {
        parts.push(
          <span key={`text-${paragraphIndex}-${idx}`}>
            {text.substring(lastIndex, source.start)}
          </span>,
        );
      }

      const color = sourceInfo[source.sources[0]]?.color || "#C5A572";
      parts.push(
        <span
          key={`source-${paragraphIndex}-${idx}`}
          className="sourced-text"
          style={{
            color,
            cursor: "pointer",
            borderBottom: `1px dotted ${color}`,
          }}
          onClick={(event) => handleSourceClick(event, source.sources)}
        >
          {text.substring(source.start, source.end)}
        </span>,
      );

      lastIndex = source.end;
    });

    if (lastIndex < text.length) {
      parts.push(
        <span key={`text-${paragraphIndex}-end`}>
          {text.substring(lastIndex)}
        </span>,
      );
    }

    return parts;
  };

  return (
    <motion.div className="playbook" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
      <div className="playbook-header">
        <div>
          <h1 className="view-title">{t.playbook.title}</h1>
          <p className="view-subtitle">
            {t.playbook.enginesActive.replace('{n}', String(enabledCount))}
          </p>
        </div>
        <div className="playbook-actions">
          <div className="scale-selector">
            {(["day", "week", "month", "year"] as TimeScope[]).map((scope) => (
              <button
                key={scope}
                className={`scale-button ${timeScope === scope ? "active" : ""}`}
                type="button"
                onClick={() => setTimeScope(scope)}
              >
                {scope === "day" ? (
                  <><Clock size={14} /><span>{t.playbook.day}</span></>
                ) : scope === "week" ? (
                  <><Calendar size={14} /><span>{t.playbook.week}</span></>
                ) : scope === "month" ? (
                  <><CalendarDays size={14} /><span>{t.playbook.month}</span></>
                ) : (
                  <><CalendarRange size={14} /><span>{t.playbook.year}</span></>
                )}
              </button>
            ))}
          </div>
          <button type="button" className="action-button" onClick={() => setShowSettings(!showSettings)}>
            <Settings size={16} />
            {t.playbook.engineSettings}
          </button>
          <button type="button" className="action-button" onClick={onClose}>
            <X size={16} />
          </button>
        </div>
      </div>

      <AnimatePresence>
        {showSettings && (
          <motion.div
            className="settings-panel"
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.3 }}
          >
            <div className="settings-content">
              <div className="settings-header">
                <div>
                  <h3 className="settings-title">{t.playbook.engineSettings}</h3>
                  <p className="settings-description">{t.playbook.chooseEngines}</p>
                </div>
              </div>
              <div className="engines-grid">
                {activeEngines.map((engine) => (
                  <button
                    key={engine.id}
                    className={`engine-toggle ${engine.enabled ? "active" : ""}`}
                    type="button"
                    onClick={() => toggleEngine(engine.id)}
                  >
                    <div className="engine-toggle-inner">
                      <span className="engine-name">{engine.name}</span>
                      <span className="engine-category">
                        {engine.category === "eastern" ? t.playbook.eastern : t.playbook.western}
                      </span>
                    </div>
                    <div className="engine-check">
                      {engine.enabled && <Check size={14} />}
                    </div>
                  </button>
                ))}
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      <div className="reading-content">
        <h2 className="reading-title">{t.playbook.todaySynthesis}</h2>

        {/* 错误提示 */}
        {error && (
          <div className="error-box">
            <AlertTriangle size={18} />
            <div className="error-text">
              <div>{error}</div>
              <div className="error-hint">
                {t.playbook.errorHint}
              </div>
            </div>
          </div>
        )}

        {/* 加载状态 */}
        {loading && (
          <div className="loading-state">
            <Loader2 size={32} className="spinner" />
            <p>{t.common.loading}</p>
          </div>
        )}

        {/* API返回的解读 - 解析 Markdown 格式 */}
        {reading && !loading && !error && (
          <div className="reading-formatted">
            {reading.readings.map((r, index) => {
              // 解析 Markdown 内容为结构化数据
              const sections = parseMarkdownContent(r.content);
              
              return (
                <div key={index} className="reading-article">
                  {sections.map((section, sIdx) => (
                    <div key={sIdx} className={`reading-section ${section.type}`}>
                      {section.type === "heading" && (
                        <h3 className="section-heading">
                          <span className="heading-icon">{getHeadingIcon(section.content)}</span>
                          <span className="heading-text">{section.content}</span>
                        </h3>
                      )}
                      {section.type === "paragraph" && (
                        <p className="section-paragraph">{section.content}</p>
                      )}
                      {section.type === "list-item" && (
                        <div className="section-list-item">
                          <span className="list-marker">•</span>
                          <span className="list-content">{section.content}</span>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              );
            })}
          </div>
        )}

        {/* Prompt to load reading when no data */}
        {!reading && !loading && !error && (
          <div className="empty-reading-prompt">
            <p>{t.playbook.noReading}</p>
          </div>
        )}
      </div>

      {selectedSource && popoverPosition && (
        <>
          <div className="popover-backdrop" onClick={handleClosePopover} />
          <div
            className="source-popover"
            style={{
              left: popoverPosition.x,
              top: popoverPosition.y,
            }}
          >
            <div className="source-popover-inner">
              <div className="source-popover-header">
                <div className="source-popover-title">
                  <span
                    className="source-dot"
                    style={{ backgroundColor: sourceInfo[selectedSource]?.color || "#C5A572" }}
                  />
                  <span className="source-name">{sourceInfo[selectedSource]?.name || selectedSource}</span>
                </div>
                <button type="button" className="popover-close" onClick={handleClosePopover}>
                  <X size={16} />
                </button>
              </div>
              <p className="source-description">{sourceInfo[selectedSource]?.description}</p>
              <p className="source-philosophy">{sourceInfo[selectedSource]?.philosophy}</p>
              <div className="source-evidence">
                <div className="evidence-label">Why this conclusion?</div>
                <p className="evidence-text">
                  The interpretation draws from {sourceInfo[selectedSource]?.name}'s core principles,
                  analyzing the interplay of symbolic elements in your current life context.
                  This reading synthesizes patterns across multiple data points to reveal deeper meaning.
                </p>
              </div>
              <div className="source-origin">
                <div className="origin-label">Source Text</div>
                <p className="origin-text">《{sourceInfo[selectedSource]?.name === "八字" ? "滴天髓" : sourceInfo[selectedSource]?.name === "Tarot" ? "The Pictorial Key to the Tarot" : "I Ching"}》Chapter: {selectedSource === "八字" ? "天干论" : selectedSource === "Tarot" ? "Major Arcana" : "Hexagram Analysis"}</p>
              </div>
            </div>
          </div>
        </>
      )}
    </motion.div>
  );
}
