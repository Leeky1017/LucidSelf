"use client";

import { useState } from "react";
import type { ComponentType } from "react";
import { motion } from "framer-motion";
import { Clock, Calendar, CalendarDays, CalendarRange, Inbox } from "lucide-react";
import type { Theme } from "@/types/common";
import type { TimeScale, PersonalTimelineEntry, LucidTimelineEntry } from "./types";
import { useTranslation } from "@/lib/i18n";

interface TimelineViewProps {
  theme: Theme;
}

export function TimelineView({ theme }: TimelineViewProps) {
  const { t } = useTranslation();
  const [timeScale, setTimeScale] = useState<TimeScale>("day");

  // Real data will come from backend API
  const personalTimeline: PersonalTimelineEntry[] = [];
  const lucidTimeline: LucidTimelineEntry[] = [];

  const scaleOptions: { value: TimeScale; label: string; icon: ComponentType<{ size?: number }> }[] = [
    { value: "hour", label: t.timeline.hour, icon: Clock },
    { value: "day", label: t.timeline.day, icon: Calendar },
    { value: "month", label: t.timeline.month, icon: CalendarDays },
    { value: "year", label: t.timeline.year, icon: CalendarRange },
  ];

  const getEntryTypeLabel = (kind: string) => {
    switch (kind) {
      case "dream": return t.timeline.dreamType;
      case "reflection": return t.timeline.reflectionType;
      default: return t.timeline.eventType;
    }
  };

  return (
    <div className="timeline-view">
      <div className="timeline-header">
        <div>
          <h1 className="view-title">{t.timeline.title}</h1>
          <p className="view-subtitle">{t.timeline.subtitle}</p>
        </div>

        <div className="scale-selector">
          {scaleOptions.map((option) => (
            <button
              key={option.value}
              className={`scale-button ${timeScale === option.value ? "active" : ""}`}
              type="button"
              onClick={() => setTimeScale(option.value)}
            >
              <option.icon size={14} />
              <span>{option.label}</span>
            </button>
          ))}
        </div>
      </div>

      <div className="dual-timeline">
        <div className="timeline-column personal-column">
          <div className="column-header">
            <h2 className="column-title">{t.timeline.yourRecords}</h2>
            <span className="entry-count">{personalTimeline.length} {t.timeline.entries}</span>
          </div>

          <div className="timeline-entries">
            {personalTimeline.length === 0 ? (
              <div className="empty-state">
                <Inbox size={40} strokeWidth={1} />
                <p>{t.timeline.noEvents}</p>
              </div>
            ) : (
              personalTimeline.map((entry, index) => (
                <motion.div
                  key={entry.id}
                  className="timeline-entry personal-entry"
                  initial={{ opacity: 0, x: -16 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.08, duration: 0.4 }}
                >
                  <div className="entry-marker" />
                  <div className="entry-content">
                    <time className="entry-time">{entry.time}</time>
                    <h3 className="entry-label">{entry.title}</h3>
                    <p className="entry-text">{entry.description}</p>
                    <span className={`entry-tag entry-tag-${entry.kind}`}>
                      {getEntryTypeLabel(entry.kind)}
                    </span>
                  </div>
                </motion.div>
              ))
            )}
          </div>
        </div>

        <div className="center-axis">
          <div className="axis-line" />
        </div>

        <div className="timeline-column lucid-column">
          <div className="column-header">
            <h2 className="column-title">{t.timeline.lucidInsights}</h2>
            <span className="entry-count">{lucidTimeline.length} {t.timeline.nInsights}</span>
          </div>

          <div className="timeline-entries">
            {lucidTimeline.length === 0 ? (
              <div className="empty-state">
                <Inbox size={40} strokeWidth={1} />
                <p>{t.timeline.noEvents}</p>
              </div>
            ) : (
              lucidTimeline.map((entry, index) => (
                <motion.div
                  key={entry.id}
                  className="timeline-entry lucid-entry"
                  initial={{ opacity: 0, x: 16 }}
                  animate={{ opacity: 1, x: 0 }}
                  transition={{ delay: index * 0.08, duration: 0.4 }}
                >
                  <div className="entry-marker lucid-marker" />
                  <div className="entry-content">
                    <time className="entry-time">{entry.time}</time>
                    <h3 className="entry-label">{entry.title}</h3>
                    <p className="entry-text">{entry.insight}</p>
                    <div className="confidence-bar">
                      <div
                        className="confidence-fill"
                        style={{ width: `${Math.round(entry.confidence * 100)}%` }}
                      />
                      <span className="confidence-label">
                        {Math.round(entry.confidence * 100)}% {t.timeline.confidence}
                      </span>
                    </div>
                  </div>
                </motion.div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
