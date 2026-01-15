"use client";

import { useState, useEffect, useCallback } from "react";
import { api } from "@/lib/api";
import type { PlaybookReadingResponse, EngineInfo, BirthData } from "@/lib/api";

const DEFAULT_USER_ID = "default_user";

interface UsePlaybookResult {
  reading: PlaybookReadingResponse | null;
  engines: EngineInfo[];
  loading: boolean;
  error: string | null;
  getReading: (birthData: BirthData, engines?: string[], timeScope?: string) => Promise<void>;
  refreshEngines: () => Promise<void>;
}

export function usePlaybook(userId: string = DEFAULT_USER_ID): UsePlaybookResult {
  const [reading, setReading] = useState<PlaybookReadingResponse | null>(null);
  const [engines, setEngines] = useState<EngineInfo[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // 加载引擎列表
  const loadEngines = useCallback(async () => {
    try {
      const response = await api.playbook.getEngines();
      setEngines(response.engines);
    } catch (err) {
      console.error("Failed to load engines:", err);
    }
  }, []);

  // 获取解读
  const getReading = useCallback(async (
    birthData: BirthData,
    selectedEngines?: string[],
    timeScope: string = "day"
  ) => {
    try {
      setLoading(true);
      setError(null);
      
      const response = await api.playbook.getReading({
        user_id: userId,
        birth_data: birthData,
        engines: selectedEngines || engines.filter(e => e.enabled).map(e => e.id),
        time_scope: timeScope as 'day' | 'week' | 'month' | 'year',
      });
      
      setReading(response);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to get reading");
      console.error("Failed to get reading:", err);
    } finally {
      setLoading(false);
    }
  }, [userId, engines]);

  // 初始加载引擎
  useEffect(() => {
    loadEngines();
  }, [loadEngines]);

  return {
    reading,
    engines,
    loading,
    error,
    getReading,
    refreshEngines: loadEngines,
  };
}

export default usePlaybook;
