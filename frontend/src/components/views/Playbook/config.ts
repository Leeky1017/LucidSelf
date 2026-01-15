import type { Engine, SourceInfo } from "./types";

export const engines: Engine[] = [
  { id: "bazi", name: "八字", category: "eastern", enabled: true },
  { id: "ziwei", name: "紫微斗数", category: "eastern", enabled: true },
  { id: "mingli", name: "命理", category: "eastern", enabled: true },
  { id: "tarot", name: "Tarot", category: "western", enabled: true },
  { id: "astrology", name: "Astrology", category: "western", enabled: true },
  { id: "runes", name: "Runes", category: "western", enabled: true },
  { id: "iching", name: "I Ching", category: "eastern", enabled: true },
  { id: "numerology", name: "Numerology", category: "western", enabled: true },
];

export const sourceInfo: Record<string, SourceInfo> = {
  八字: {
    name: "八字",
    color: "#C5A572",
    description: "Four Pillars of Destiny",
    philosophy: "Based on birth time analysis, revealing life patterns and potential through the interplay of heavenly stems and earthly branches.",
  },
  紫微斗数: {
    name: "紫微斗数",
    color: "#7C4DFF",
    description: "Purple Star Astrology",
    philosophy: "Ancient Chinese system mapping 108 stars across 12 palaces to reveal destiny, personality, and life trajectory.",
  },
  命理: {
    name: "命理",
    color: "#00BFA5",
    description: "Comprehensive Life Analysis",
    philosophy: "Integrates multiple traditional systems to provide holistic life guidance and pattern recognition.",
  },
  Tarot: {
    name: "Tarot",
    color: "#FF6B9D",
    description: "Archetypal Card Reading",
    philosophy: "Uses symbolic imagery to access intuition and reveal unconscious patterns influencing current situations.",
  },
  Astrology: {
    name: "Astrology",
    color: "#4FC3F7",
    description: "Western Astrology",
    philosophy: "Maps celestial positions at birth to understand personality, timing, and life cycles through zodiac signs and planetary aspects.",
  },
};
