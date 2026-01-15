'use client';

import { useState, useEffect, useCallback, MouseEvent } from "react";
import type { ComponentType, ReactNode } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Moon,
  Sun,
  Sparkles,
  Clock,
  Calendar,
  CalendarDays,
  CalendarRange,
  TrendingUp,
  TrendingDown,
  Minus,
  Zap,
  Repeat,
  Plus,
  X,
  Tag,
  Lightbulb,
  Settings,
  ChevronRight,
  BookOpen,
  Check,
  Briefcase,
  Heart,
} from "lucide-react";
import SimpleRecorder from "@/components/SimpleRecorder";
import DetailedRecorder from "@/components/DetailedRecorder";
import type { DreamEntry as DreamEntryType } from "@/types/dream";

type View =
  | "now"
  | "timeline"
  | "archive"
  | "dream"
  | "playbook"
  | "journal"
  | "insights";
type Theme = "light" | "dark";

export default function Home() {
  const [view, setView] = useState<View>("now");
  const [theme, setTheme] = useState<Theme>("light");
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', theme);
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prev => prev === 'dark' ? 'light' : 'dark');
  };

  const handleModuleClick = (moduleId: View) => {
    setView(moduleId);
  };

  const handleBackToNow = () => {
    setView('now');
  };

  return (
    <div className="app-container">
      {/* Sidebar Navigation - Desktop Only */}
      <aside className={`sidebar desktop-only ${sidebarCollapsed ? 'collapsed' : ''}`}>
        <div className="sidebar-header">
          <div className="logo" onClick={handleBackToNow}>
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none" className="text-[color:var(--accent-gold)]">
              <circle cx="16" cy="16" r="12" stroke="currentColor" strokeWidth="1" opacity="0.3"/>
              <circle cx="16" cy="16" r="8" stroke="currentColor" strokeWidth="1" opacity="0.5"/>
              <circle cx="16" cy="16" r="4" stroke="currentColor" strokeWidth="1.5"/>
              <path d="M16 4 L16 28 M4 16 L28 16" stroke="currentColor" strokeWidth="0.5" opacity="0.2"/>
            </svg>
            {!sidebarCollapsed && (
              <div className="logo-text">
                <span className="logo-name">Lucid Self</span>
                <span className="logo-tagline">灵性伴侣</span>
              </div>
            )}
          </div>
        </div>

        <nav className="sidebar-nav">
          <button
            className={`sidebar-nav-item ${view === 'now' ? 'active' : ''}`}
            onClick={() => setView('now')}
          >
            <span className="nav-dot"></span>
            {!sidebarCollapsed && <span>Now</span>}
          </button>
          <button
            className={`sidebar-nav-item ${view === 'timeline' ? 'active' : ''}`}
            onClick={() => setView('timeline')}
          >
            <span className="nav-dot"></span>
            {!sidebarCollapsed && <span>Timeline</span>}
          </button>
          <button
            className={`sidebar-nav-item ${view === 'archive' ? 'active' : ''}`}
            onClick={() => setView('archive')}
          >
            <span className="nav-dot"></span>
            {!sidebarCollapsed && <span>Archive</span>}
          </button>
        </nav>

        <div className="sidebar-footer">
          <button 
            className="theme-toggle-sidebar"
            onClick={toggleTheme}
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
            onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
            aria-label="Toggle sidebar"
          >
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor">
              <path 
                d={sidebarCollapsed ? "M6 4L10 8L6 12" : "M10 4L6 8L10 12"} 
                strokeWidth="1.5" 
                strokeLinecap="round" 
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </div>
      </aside>

      {/* Mobile Header */}
      <header className="mobile-header mobile-only">
        <div className="logo-mobile" onClick={handleBackToNow}>
          <svg width="24" height="24" viewBox="0 0 32 32" fill="none" className="text-[color:var(--accent-gold)]">
            <circle cx="16" cy="16" r="12" stroke="currentColor" strokeWidth="1" opacity="0.3"/>
            <circle cx="16" cy="16" r="8" stroke="currentColor" strokeWidth="1" opacity="0.5"/>
            <circle cx="16" cy="16" r="4" stroke="currentColor" strokeWidth="1.5"/>
            <path d="M16 4 L16 28 M4 16 L28 16" stroke="currentColor" strokeWidth="0.5" opacity="0.2"/>
          </svg>
          <span>Lucid Self</span>
        </div>
        <button className="theme-toggle" onClick={toggleTheme} aria-label="Toggle theme">
          {theme === 'dark' ? <Moon size={20} /> : <Sun size={20} />}
        </button>
      </header>

      {/* Main Content */}
      <main className={`main-content ${sidebarCollapsed ? 'collapsed-sidebar' : ''}`}>
        <AnimatePresence mode="wait">
          <motion.div
            key={view}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ 
              duration: 0.5,
              ease: [0.4, 0, 0.2, 1]
            }}
            className="view-container"
          >
            {view === 'now' && (
              <NowView theme={theme} onModuleClick={handleModuleClick} />
            )}
            {view === 'timeline' && <TimelineView theme={theme} />}
            {view === 'archive' && <ArchiveView theme={theme} />}
            {view === 'dream' && <DreamJournal onClose={handleBackToNow} />}
            {view === 'playbook' && <Playbook onClose={handleBackToNow} />}
            {view === 'journal' && (
              <div className="placeholder-view">
                <h1>Reflection</h1>
                <p>Mindfulness journal coming soon</p>
              </div>
            )}
            {view === 'insights' && (
              <div className="placeholder-view">
                <h1>Insights</h1>
                <p>Growth tracking coming soon</p>
              </div>
            )}
          </motion.div>
        </AnimatePresence>
      </main>

      {/* Mobile Bottom Navigation */}
      <nav className="mobile-nav mobile-only">
        <button
          className={`mobile-nav-item ${view === 'now' ? 'active' : ''}`}
          onClick={() => setView('now')}
        >
          <div className="nav-dot"></div>
          <span>Now</span>
        </button>
        <button
          className={`mobile-nav-item ${view === 'timeline' ? 'active' : ''}`}
          onClick={() => setView('timeline')}
        >
          <div className="nav-dot"></div>
          <span>Timeline</span>
        </button>
        <button
          className={`mobile-nav-item ${view === 'archive' ? 'active' : ''}`}
          onClick={() => setView('archive')}
        >
          <div className="nav-dot"></div>
          <span>Archive</span>
        </button>
      </nav>
    </div>
  );
}

// NowView Component
function NowView({ theme, onModuleClick }: { theme: Theme; onModuleClick: (moduleId: View) => void }) {
  return (
    <div className="now-view">
      {/* Compact Insight */}
      <motion.div
        className="compact-insight"
        initial={{ opacity: 0, y: -10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6 }}
      >
        <time className="insight-time">NOW</time>
        <p className="insight-text">You are focusing on what truly matters</p>
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
            <h3 className="tool-title">Playbook</h3>
          </div>
          
          <div className="tool-preview">
            <p className="playbook-desc">Multi-dimensional life reading engine</p>
            <div className="playbook-engines">
              <span className="engine-indicator active">八字</span>
              <span className="engine-indicator active">紫微</span>
              <span className="engine-indicator active">Tarot</span>
              <span className="engine-indicator active">Astrology</span>
              <span className="engine-indicator">+4</span>
            </div>
          </div>

          <div className="tool-action">View Reading →</div>
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
            <h3 className="tool-title">Dream Journal</h3>
          </div>
          
          <div className="tool-preview">
            <div className="preview-item">
              <span className="preview-date">Last night</span>
              <p className="preview-text">The Infinite Library</p>
            </div>
            <div className="preview-item">
              <span className="preview-date">2 days ago</span>
              <p className="preview-text">Flying Over Water</p>
            </div>
          </div>

          <div className="tool-action">Open Journal →</div>
        </motion.button>
      </motion.div>

      {/* Other Tools */}
      <motion.div
        className="other-tools-section"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4, duration: 0.6 }}
      >
        <h2 className="section-title">More Tools</h2>
        <ModuleGrid onModuleClick={onModuleClick} />
      </motion.div>
    </div>
  );
}

// TimelineView Component
type TimeScale = "hour" | "day" | "month" | "year";

interface PersonalTimelineEntry {
  id: string;
  time: string;
  title: string;
  description: string;
  kind: "dream" | "reflection" | "event";
}

interface LucidTimelineEntry {
  id: string;
  time: string;
  title: string;
  insight: string;
  confidence: number;
}

const personalTimeline: PersonalTimelineEntry[] = [
  {
    id: "p1",
    time: "23:45",
    title: "Dream: The Infinite Library",
    description:
      "You recorded a vivid dream about an endless spiral library of glowing books.",
    kind: "dream",
  },
  {
    id: "p2",
    time: "14:30",
    title: "Afternoon reflection",
    description: "You noticed a wave of clarity after a short meditation break.",
    kind: "reflection",
  },
  {
    id: "p3",
    time: "09:10",
    title: "Morning pages",
    description:
      "Stream-of-consciousness writing about creative resistance and self-doubt.",
    kind: "reflection",
  },
];

const lucidTimeline: LucidTimelineEntry[] = [
  {
    id: "l1",
    time: "23:45",
    title: "Subconscious seeking knowledge",
    insight:
      "Recurring library symbolism points to a deep desire to understand yourself and the patterns in your life.",
    confidence: 0.92,
  },
  {
    id: "l2",
    time: "14:30",
    title: "Clarity after stillness",
    insight:
      "Your nervous system settles quickly when you pause, making you more receptive to insight.",
    confidence: 0.88,
  },
  {
    id: "l3",
    time: "09:10",
    title: "Creative resistance as protection",
    insight:
      "Resistance shows up strongest before important work. It may be protecting vulnerable parts of you.",
    confidence: 0.86,
  },
];

function getTimePositionPercent(time: string): number {
  const [hoursStr, minutesStr] = time.split(":");
  const hours = Number(hoursStr);
  const minutes = Number(minutesStr);

  if (!Number.isFinite(hours) || !Number.isFinite(minutes)) {
    return 50;
  }

  const totalMinutes = hours * 60 + minutes;
  const ratio = Math.min(Math.max(totalMinutes / (24 * 60), 0), 1);
  // Reverse: 24:00 at top (5%), 00:00 at bottom (95%)
  return 5 + (1 - ratio) * 90;
}

function TimelineView({ theme }: { theme: Theme }) {
  const [timeScale, setTimeScale] = useState<TimeScale>("day");

  const scaleOptions: { value: TimeScale; label: string; icon: ComponentType<{ size?: number }> }[] = [
    { value: "hour", label: "Hour", icon: Clock },
    { value: "day", label: "Day", icon: Calendar },
    { value: "month", label: "Month", icon: CalendarDays },
    { value: "year", label: "Year", icon: CalendarRange },
  ];

  return (
    <div className="timeline-view">
      <div className="timeline-header">
        <div>
          <h1 className="view-title">Timeline</h1>
          <p className="view-subtitle">Your inner and outer journey across time</p>
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
            <h2 className="column-title">Your records</h2>
            <span className="entry-count">{personalTimeline.length} entries</span>
          </div>

          <div className="timeline-entries">
            {personalTimeline.map((entry, index) => (
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
                    {entry.kind === "dream"
                      ? "Dream"
                      : entry.kind === "reflection"
                      ? "Reflection"
                      : "Event"}
                  </span>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        <div className="center-axis">
          <div className="axis-line" />
        </div>

        <div className="timeline-column lucid-column">
          <div className="column-header">
            <h2 className="column-title">Lucid insights</h2>
            <span className="entry-count">{lucidTimeline.length} insights</span>
          </div>

          <div className="timeline-entries">
            {lucidTimeline.map((entry, index) => (
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
                      {Math.round(entry.confidence * 100)}% confidence
                    </span>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

// ArchiveView - Full Figma v2 implementation
type ViewMode = 'patterns' | 'insights';
type CategoryFilter = 'all' | 'dream' | 'work' | 'relationship' | 'spiritual' | 'body';

interface Pattern {
  id: string;
  name: string;
  category: 'dream' | 'work' | 'relationship' | 'spiritual' | 'body';
  frequency: number;
  trend: 'up' | 'down' | 'stable';
  lastSeen: string;
  description: string;
  examples: string[];
  astrologyTag?: string;
  psychologyTag?: string;
  aiInsight?: string;
  relatedRecords: number;
  frequencyData: number[];
  peakMonth?: string;
}

interface CorePattern extends Pattern {
  importance: 'critical' | 'high' | 'medium';
}

interface DeepInsight {
  id: string;
  title: string;
  synthesis: string;
  sources: number;
  timespan: string;
  generatedAt: string;
  lunarPhase: string;
  astroContext: string;
}

const currentChapter = {
  title: '第6大运',
  period: '2024.03 - 2034.03',
  theme: '木星扩张期 · 巨蟹月亮回归',
  startDate: new Date('2024-03-01'),
  endDate: new Date('2034-03-01')
};

const corePatterns: CorePattern[] = [
  {
    id: 'core-1',
    name: 'Water Symbolism',
    category: 'dream',
    frequency: 15,
    trend: 'up',
    lastSeen: '2 days ago',
    description: 'Recurring water imagery in dreams - emotional depth exploration',
    examples: ['Ocean dreams', 'Rain meditation', 'River walking'],
    astrologyTag: '巨蟹月亮',
    psychologyTag: '情感安全',
    aiInsight: 'This pattern peaks during emotional transitions and full moon cycles',
    relatedRecords: 12,
    frequencyData: [3, 5, 4, 7, 9, 15],
    peakMonth: 'Nov',
    importance: 'critical'
  },
  {
    id: 'core-2',
    name: 'Creative Resistance',
    category: 'work',
    frequency: 8,
    trend: 'down',
    lastSeen: '1 week ago',
    description: 'Morning creative blocks - guardian before transformation',
    examples: ['Morning pages resistance', 'Delayed starts', 'Overthinking'],
    astrologyTag: '第5宫课题',
    psychologyTag: '自我表达',
    aiInsight: 'Resistance decreases as you embrace imperfection',
    relatedRecords: 8,
    frequencyData: [12, 11, 10, 9, 8, 8],
    peakMonth: 'Aug',
    importance: 'high'
  },
  {
    id: 'core-3',
    name: 'Body Wisdom',
    category: 'body',
    frequency: 18,
    trend: 'stable',
    lastSeen: 'Yesterday',
    description: 'Physical sensations precede intellectual understanding',
    examples: ['Post-yoga clarity', 'Walking epiphanies', 'Dance integration'],
    astrologyTag: '第6宫',
    psychologyTag: '身心整合',
    aiInsight: 'Your body knows truth 2-3 days before your mind',
    relatedRecords: 15,
    frequencyData: [16, 18, 17, 19, 18, 18],
    peakMonth: 'Stable',
    importance: 'critical'
  }
];

const allPatterns: Pattern[] = [
  ...corePatterns,
  {
    id: '4',
    name: 'Flight Dreams',
    category: 'dream',
    frequency: 7,
    trend: 'up',
    lastSeen: '3 days ago',
    description: 'Lucid flying experiences - liberation from limiting beliefs',
    examples: ['Soaring over water', 'Cloud navigation', 'Weightless joy'],
    astrologyTag: '第9宫',
    psychologyTag: '自由渴望',
    aiInsight: 'Flying dreams increase when you release control',
    relatedRecords: 7,
    frequencyData: [2, 3, 4, 5, 6, 7]
  },
  {
    id: '5',
    name: 'Relationship Mirrors',
    category: 'relationship',
    frequency: 11,
    trend: 'stable',
    lastSeen: '5 days ago',
    description: 'People reflecting your shadow aspects',
    examples: ['Conflict patterns', 'Projection awareness', 'Boundary work'],
    astrologyTag: '第7宫',
    psychologyTag: '投射整合',
    aiInsight: 'What triggers you reveals what needs healing',
    relatedRecords: 11,
    frequencyData: [10, 11, 12, 11, 10, 11]
  },
  {
    id: '6',
    name: 'Intuitive Hits',
    category: 'spiritual',
    frequency: 13,
    trend: 'up',
    lastSeen: 'Today',
    description: 'Sudden knowing without logical reasoning',
    examples: ['Déjà vu moments', 'Precognitive dreams', 'Synchronicities'],
    astrologyTag: '第12宫',
    psychologyTag: '直觉开发',
    aiInsight: 'Trust increases accuracy by 40%',
    relatedRecords: 13,
    frequencyData: [5, 7, 9, 10, 12, 13]
  },
  {
    id: '7',
    name: 'Performance Anxiety',
    category: 'work',
    frequency: 6,
    trend: 'down',
    lastSeen: '2 weeks ago',
    description: 'Fear of being seen in professional settings',
    examples: ['Presentation nerves', 'Imposter syndrome', 'Perfectionism'],
    astrologyTag: '第10宫',
    psychologyTag: '自我价值',
    aiInsight: 'Decreasing as you build self-trust',
    relatedRecords: 6,
    frequencyData: [10, 9, 8, 7, 6, 6]
  }
];

const deepInsights: DeepInsight[] = [
  {
    id: '1',
    title: 'The Spiral of Self-Discovery',
    synthesis: 'Your journey follows a spiral pattern - you revisit similar themes at progressively deeper levels. What felt like going in circles was actually ascending. The water symbolism that appeared 6 months ago was about emotional safety; now it\'s about spiritual depth.',
    sources: 24,
    timespan: '3 months',
    generatedAt: 'Nov 15, 2024',
    lunarPhase: 'Full Moon in Taurus',
    astroContext: '金星逆行 · 第8宫活跃'
  },
  {
    id: '2',
    title: 'Creative Flow and Resistance',
    synthesis: 'Resistance is not your enemy but a guardian. It appears strongest before your most transformative work. Your creative blocks are actually protective mechanisms - they emerge when you\'re about to break through old identity structures.',
    sources: 18,
    timespan: '6 weeks',
    generatedAt: 'Oct 28, 2024',
    lunarPhase: 'New Moon in Scorpio',
    astroContext: '火星六分土星 · 第5宫强化'
  },
  {
    id: '3',
    title: 'The Body Knows First',
    synthesis: 'Physical sensations precede intellectual understanding by 2-3 days. Your body processes truth before your mind accepts it. Tracking body wisdom patterns shows 89% correlation with later realizations.',
    sources: 32,
    timespan: '4 months',
    generatedAt: 'Sep 12, 2024',
    lunarPhase: 'Waxing Crescent',
    astroContext: '水星入处女 · 第6宫回归'
  }
];

const categoryConfig = {
  all: { icon: Sparkles, label: 'All Patterns', color: '#FFD700' },
  dream: { icon: Moon, label: 'Dream Symbols', color: '#7C4DFF' },
  work: { icon: Briefcase, label: 'Work Patterns', color: '#00BFA5' },
  relationship: { icon: Heart, label: 'Relationships', color: '#FF6B9D' },
  spiritual: { icon: Sparkles, label: 'Spiritual Growth', color: '#FFD700' },
  body: { icon: TrendingUp, label: 'Body Wisdom', color: '#4FC3F7' }
};

function ArchiveView({ theme }: { theme: Theme }) {
  const [viewMode, setViewMode] = useState<ViewMode>('patterns');
  const [categoryFilter, setCategoryFilter] = useState<CategoryFilter>('all');
  const [selectedPattern, setSelectedPattern] = useState<Pattern | null>(null);

  // Calculate chapter progress
  const now = new Date();
  const totalDuration = currentChapter.endDate.getTime() - currentChapter.startDate.getTime();
  const elapsed = now.getTime() - currentChapter.startDate.getTime();
  const progressPercent = Math.min(Math.max(elapsed / totalDuration, 0), 1);
  const circumference = 2 * Math.PI * 54; // radius = 54

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
          <h1 className="view-title">Archive</h1>
          <p className="view-subtitle">Patterns and deep insights from your journey</p>
        </div>

        <div className="view-toggle">
          <button
            className={`toggle-button ${viewMode === 'patterns' ? 'active' : ''}`}
            onClick={() => setViewMode('patterns')}
          >
            <Repeat size={16} />
            <span>Patterns</span>
          </button>
          <button
            className={`toggle-button ${viewMode === 'insights' ? 'active' : ''}`}
            onClick={() => setViewMode('insights')}
          >
            <Zap size={16} />
            <span>Deep Insights</span>
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
                  <span className="progress-label">当前大运进度</span>
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
                      <span className="last-seen">Last: {pattern.lastSeen}</span>
                      <span className="related-count">{pattern.relatedRecords} records</span>
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
                <h3 className="section-title">All Patterns</h3>
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
                          {pattern.relatedRecords} records
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
                These are synthesized understandings drawn from multiple entries across time
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
                      <span>Generated on {insight.generatedAt}</span>
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
                      <span className="meta-item">{insight.sources} sources</span>
                      <span className="meta-divider">•</span>
                      <span className="meta-item">{insight.timespan}</span>
                    </div>
                  </div>

                  <blockquote className="insight-synthesis">
                    {insight.synthesis}
                  </blockquote>

                  <button className="explore-button">Explore Sources →</button>
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
                    Frequency Timeline (6 months)
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
                      <h4 className="detail-title">AI Insight</h4>
                      <p className="insight-content">{selectedPattern.aiInsight}</p>
                    </div>
                  </div>
                )}

                {/* Examples */}
                <div className="detail-section">
                  <h4 className="detail-title">Common Contexts</h4>
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
                  <h4 className="detail-title">Related Records</h4>
                  <button className="records-link">
                    View all {selectedPattern.relatedRecords} dreams, reflections, and events
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

// DreamJournal Component (adapted from Figma v2)
interface DreamEntry {
  id: string;
  date: string;
  time: string;
  title: string;
  content: string;
  mood: string;
  symbols: string[];
  interpretation?: {
    summary: string;
    symbolMeanings: { symbol: string; meaning: string }[];
    connection: string;
  };
  realityConnection?: {
    date: string;
    event: string;
    correlation: string;
  };
}

const mockDreams: DreamEntry[] = [
  {
    id: "1",
    date: "2024-11-15",
    time: "23:45",
    title: "The Infinite Library",
    content:
      "I found myself in a vast library with endless shelves spiraling upward into darkness. Each book glowed with a soft, warm light—some golden, others silver or deep blue. I knew instinctively that these weren't ordinary books; they contained answers to questions I hadn't yet learned to ask.",
    mood: "Curious",
    symbols: ["Books", "Light", "Spirals", "Knowledge"],
    interpretation: {
      summary:
        "Your subconscious is signaling a deep hunger for wisdom and self-knowledge. The infinite nature of the library suggests you're becoming aware of how much there is to discover—both in the external world and within yourself.",
      symbolMeanings: [
        { symbol: "Books", meaning: "Accumulated knowledge, life lessons yet to be learned" },
        { symbol: "Spirals", meaning: "Spiritual evolution, the cyclical nature of growth" },
        { symbol: "Shifting Letters", meaning: "The fluid nature of truth; understanding changes with perspective" },
      ],
      connection:
        "This dream reflects your current life phase of seeking deeper meaning. The library represents your inner wisdom—vast, but requiring patience to access.",
    },
    realityConnection: {
      date: "2024-11-15",
      event: 'Started reading "The Book of Symbols" • Attended wisdom circle',
      correlation:
        "Your waking exploration of symbolic language is creating a resonance in your dream world. The subconscious is processing your conscious seeking.",
    },
  },
  {
    id: "2",
    date: "2024-11-12",
    time: "04:30",
    title: "Flying Over Water",
    content:
      "I was gliding effortlessly above a calm ocean at sunset. The water reflected golden and pink light, creating a mirror between sky and sea.",
    mood: "Peaceful",
    symbols: ["Water", "Flight", "Sunset", "Mirror"],
  },
];

function DreamJournal({ onClose }: { onClose: () => void }) {
  const [dreams, setDreams] = useState<DreamEntry[]>(mockDreams);
  const [showSimple, setShowSimple] = useState(false);
  const [showDetailed, setShowDetailed] = useState(false);
  const [selectedDream, setSelectedDream] = useState<string | null>(null);

  // 处理保存梦境（从DreamRecorder回调）
  const handleSaveDream = (dream: DreamEntryType) => {
    // 转换新数据结构到旧数据结构（兼容现有UI）
    const legacyDream: DreamEntry = {
      id: dream.id,
      date: new Date(dream.createdAt).toISOString().split("T")[0],
      time: new Date(dream.createdAt).toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit" }),
      title: dream.title || `${new Date(dream.createdAt).toLocaleDateString()}的梦`,
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
          <h1 className="journal-title">Dream Journal</h1>
          <p className="journal-subtitle">Where your subconscious speaks in symbols</p>
        </div>

        <div className="header-actions">
          <button className="action-button secondary" onClick={() => setShowSimple(true)}>
            <Plus size={20} />
            <span>Simple</span>
          </button>
          <button className="action-button primary" onClick={() => setShowDetailed(true)}>
            <Plus size={20} />
            <span>Record Dream</span>
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
            className={`dream-card ${selectedDream === dream.id ? "expanded" : ""}`}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.08 }}
            onClick={() => setSelectedDream(selectedDream === dream.id ? null : dream.id)}
          >
            <div className="dream-card-header">
              <div className="dream-meta">
                <Moon size={16} className="dream-icon" />
                <time className="dream-date">
                  {new Date(dream.date).toLocaleDateString("en-US", {
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
                      <h4>Interpretation</h4>
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
                        <h4>Reality Connection</h4>
                      </div>
                      <div className="reality-event">
                        <Calendar size={14} />
                        <span>
                          {new Date(dream.realityConnection.date).toLocaleDateString("en-US", {
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

// Playbook Component (adapted from Figma v2)
type TimeScope = "day" | "week" | "month" | "year";

interface Engine {
  id: string;
  name: string;
  category: "eastern" | "western";
  enabled: boolean;
}

interface SourceInfo {
  name: string;
  color: string;
  description: string;
  philosophy: string;
}

interface InlineSource {
  start: number;
  end: number;
  sources: string[];
}

interface ReadingParagraph {
  text: string;
  inlineSources: InlineSource[];
}

const engines: Engine[] = [
  { id: "bazi", name: "八字", category: "eastern", enabled: true },
  { id: "ziwei", name: "紫微斗数", category: "eastern", enabled: true },
  { id: "mingli", name: "命理", category: "eastern", enabled: true },
  { id: "dayun", name: "大运流年", category: "eastern", enabled: true },
  { id: "tarot", name: "Tarot", category: "western", enabled: true },
  { id: "astrology", name: "Astrology", category: "western", enabled: true },
  { id: "iching", name: "I Ching", category: "western", enabled: true },
  { id: "numerology", name: "Numerology", category: "western", enabled: true },
];

const sourceInfo: Record<string, SourceInfo> = {
  八字: {
    name: "八字",
    color: "#C5A572",
    description: "Four Pillars of Destiny",
    philosophy:
      "Ancient Chinese cosmology analyzing the interplay of five elements and yin-yang forces at the moment of birth.",
  },
  Astrology: {
    name: "Astrology",
    color: "#C5A572",
    description: "Western Astrology",
    philosophy:
      "Celestial divination examining planetary positions and their influence on human consciousness and life events.",
  },
  Tarot: {
    name: "Tarot",
    color: "#7C4DFF",
    description: "Tarot Archetypal Reading",
    philosophy:
      "Symbolic system revealing subconscious patterns through archetypal imagery and intuitive interpretation.",
  },
  大运流年: {
    name: "大运流年",
    color: "#00BFA5",
    description: "Life Cycles & Annual Influences",
    philosophy:
      "Chinese metaphysics tracking 10-year major cycles and yearly energetic shifts in personal destiny.",
  },
  "I Ching": {
    name: "I Ching",
    color: "#00BFA5",
    description: "Book of Changes",
    philosophy:
      "Ancient oracle system using hexagrams to reveal the dynamic nature of situations and appropriate responses.",
  },
  紫微斗数: {
    name: "紫微斗数",
    color: "#9C27B0",
    description: "Purple Star Astrology",
    philosophy:
      "Sophisticated Chinese system mapping 108 stars across 12 palaces to reveal life purpose and destiny patterns.",
  },
  Numerology: {
    name: "Numerology",
    color: "#FF6B6B",
    description: "Pythagorean Numerology",
    philosophy:
      "Mathematical divination revealing soul purpose and life lessons through the vibrational essence of numbers.",
  },
};

const dayReading: ReadingParagraph[] = [
  {
    text:
      "Today, you stand at a threshold moment. Your chart carries both visionary and grounded qualities—you dream of new worlds while staying rooted in wisdom.",
    inlineSources: [{ start: 86, end: 163, sources: ["八字", "Astrology"] }],
  },
  {
    text:
      "The Hermit archetype walks with you today, suggesting a soul drawn to inner illumination. You are here to seek truth not in the outer world, but in the depths of consciousness.",
    inlineSources: [{ start: 0, end: 99, sources: ["Tarot"] }],
  },
  {
    text:
      "Today's energy carries the signature of Hexagram 20—Contemplation. This is a day for observation rather than action.",
    inlineSources: [{ start: 37, end: 88, sources: ["I Ching"] }],
  },
  {
    text:
      "Saturn currently transits your 12th house, amplifying today's introspective quality. What feels like withdrawal is actually preparation.",
    inlineSources: [{ start: 0, end: 66, sources: ["Astrology"] }],
  },
  {
    text:
      "All systems converge on this truth for today: Honor the stillness. Your breakthrough comes not from doing, but from being.",
    inlineSources: [{ start: 0, end: 44, sources: ["八字", "Tarot", "I Ching"] }],
  },
];

function Playbook({ onClose }: { onClose: () => void }) {
  const [showSettings, setShowSettings] = useState(false);
  const [activeEngines, setActiveEngines] = useState<Engine[]>(engines);
  const [timeScope, setTimeScope] = useState<TimeScope>("day");
  const [selectedSource, setSelectedSource] = useState<string | null>(null);
  const [popoverPosition, setPopoverPosition] = useState<{ x: number; y: number } | null>(null);

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

  // Backdrop click handling is now done via onClick on the backdrop div

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

  const getScopeLabel = () => {
    const labels: Record<TimeScope, string> = {
      day: "Today",
      week: "This Week",
      month: "This Month",
      year: "This Year",
    };
    return labels[timeScope];
  };

  return (
    <motion.div className="playbook" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
      <div className="playbook-header">
        <div>
          <h1 className="view-title">Playbook</h1>
          <p className="view-subtitle">
            {enabledCount} engines active
          </p>
        </div>
        <div className="playbook-actions">
          <div className="scale-selector">
            {(["day", "week", "month", "year"] as TimeScope[]).map((scope) => (
              <button
                key={scope}
                className={`scale-button ${timeScope === scope ? "active" : ""}`}
                type="button"
                onClick={() => setTimeScope(scope as "day" | "week" | "month" | "year")}
              >
                {scope === "day" ? (
                  <><Clock size={14} /><span>Day</span></>
                ) : scope === "week" ? (
                  <><Calendar size={14} /><span>Week</span></>
                ) : scope === "month" ? (
                  <><CalendarDays size={14} /><span>Month</span></>
                ) : (
                  <><CalendarRange size={14} /><span>Year</span></>
                )}
              </button>
            ))}
          </div>
          <button type="button" className="action-button" onClick={() => setShowSettings(!showSettings)}>
            <Settings size={16} />
            Engines
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
                  <h3 className="settings-title">Engines</h3>
                  <p className="settings-description">Choose which systems are active in your reading.</p>
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
                        {engine.category === "eastern" ? "Eastern" : "Western"}
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
        <h2 className="reading-title">Today's Synthesis</h2>
        <div className="reading-paragraphs">
          {dayReading.map((paragraph, index) => (
            <p key={index} className="reading-paragraph">
              {renderTextWithSources(paragraph, index)}
            </p>
          ))}
        </div>
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

// ModuleGrid - Figma v2 implementation
interface Module {
  id: View;
  name: string;
  icon: ComponentType<{ size?: number; strokeWidth?: number }>;
  color: string;
  description: string;
}

const modules: Module[] = [
  {
    id: 'journal',
    name: 'Reflection',
    icon: BookOpen,
    color: '#6B6B6B',
    description: 'Daily mindfulness practice',
  },
  {
    id: 'insights',
    name: 'Insights',
    icon: TrendingUp,
    color: '#C5A572',
    description: 'Track your spiritual growth',
  },
];

function ModuleGrid({ onModuleClick }: { onModuleClick: (moduleId: View) => void }) {
  return (
    <div className="module-grid">
      {modules.map((module, index) => (
        <motion.button
          key={module.id}
          className="module-card"
          onClick={() => onModuleClick(module.id)}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{
            delay: index * 0.08,
            duration: 0.5,
            ease: [0.4, 0, 0.2, 1],
          }}
          whileHover={{ y: -4 }}
        >
          <div className="module-icon" style={{ color: module.color }}>
            <module.icon size={24} strokeWidth={1.5} />
          </div>

          <div className="module-content">
            <h3 className="module-name">{module.name}</h3>
            <p className="module-description">{module.description}</p>
          </div>
        </motion.button>
      ))}
    </div>
  );
}
