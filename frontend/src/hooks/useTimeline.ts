"use client";

import { useState, useCallback } from "react";
import { api } from "@/lib/api";

const DEFAULT_USER_ID = "default_user";

interface TimelineEvent {
  id: string;
  type: string;
  title: string;
  summary: string;
  timestamp: string;
}

interface PersonalEntry {
  id: string;
  type: string;
  content: string;
  timestamp: string;
  tags: string[];
}

interface LucidInsight {
  id: string;
  source: string;
  title: string;
  content: string;
  timestamp: string;
  relevance: number;
}

interface TimelineData {
  personal: PersonalEntry[];
  insights: LucidInsight[];
  events: TimelineEvent[];
  correlations: Array<{
    personal_id: string;
    insight_id: string;
    correlation_type: string;
    strength: number;
  }>;
  time_range: {
    start: string;
    end: string;
    scale: string;
  };
}

interface UseTimelineResult {
  data: TimelineData | null;
  loading: boolean;
  error: string | null;
  loadTimeline: (scale?: string, start?: string, end?: string) => Promise<void>;
}

export function useTimeline(userId: string = DEFAULT_USER_ID): UseTimelineResult {
  const [data, setData] = useState<TimelineData | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const loadTimeline = useCallback(async (
    scale: string = "day",
    start?: string,
    end?: string
  ) => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await api.timeline.getCombined({
        user_id: userId,
        scale: scale as 'hour' | 'day' | 'week' | 'month' | 'year',
        start,
        end,
        limit: 50,
      });
      
      setData(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load timeline");
      console.error("Failed to load timeline:", err);
    } finally {
      setLoading(false);
    }
  }, [userId]);

  return {
    data,
    loading,
    error,
    loadTimeline,
  };
}

export default useTimeline;
