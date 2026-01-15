import type { ComponentType } from "react";
import {
  Sparkles,
  Moon,
  Briefcase,
  Heart,
  TrendingUp
} from "lucide-react";

export type ViewMode = 'patterns' | 'insights';
export type CategoryFilter = 'all' | 'dream' | 'work' | 'relationship' | 'spiritual' | 'body';

export interface Pattern {
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

export interface CorePattern extends Pattern {
  importance: 'critical' | 'high' | 'medium';
}

export interface DeepInsight {
  id: string;
  title: string;
  synthesis: string;
  sources: number;
  timespan: string;
  generatedAt: string;
  lunarPhase: string;
  astroContext: string;
}

export const categoryConfig = {
  all: { icon: Sparkles, label: 'All Patterns', color: '#FFD700' },
  dream: { icon: Moon, label: 'Dream Symbols', color: '#7C4DFF' },
  work: { icon: Briefcase, label: 'Work Patterns', color: '#00BFA5' },
  relationship: { icon: Heart, label: 'Relationships', color: '#FF6B9D' },
  spiritual: { icon: Sparkles, label: 'Spiritual Growth', color: '#FFD700' },
  body: { icon: TrendingUp, label: 'Body Wisdom', color: '#4FC3F7' }
};
