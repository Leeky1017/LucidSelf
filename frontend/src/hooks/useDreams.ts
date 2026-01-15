"use client";

import { useState, useEffect, useCallback } from "react";
import { api } from "@/lib/api";
import type { DreamEntry as APIDreamEntry, DreamGenerateResponse } from "@/lib/api";

// 默认用户ID（后续接入认证后替换）
const DEFAULT_USER_ID = "default_user";

export interface DreamEntry {
  id: string;
  date: string;
  time: string;
  title: string;
  content: string;
  mood: string;
  symbols: string[];
  interpretation?: {
    summary: string;
    symbolMeanings: Array<{ symbol: string; meaning: string }>;
    connection: string;
  };
  realityConnection?: {
    date: string;
    event: string;
    correlation: string;
  };
}

interface UseDreamsResult {
  dreams: DreamEntry[];
  loading: boolean;
  error: string | null;
  saveDream: (dream: {
    rawInput: string;
    finalContent: string;
    generatedContent?: string;
    title?: string;
    mood?: string;
    tags?: string[];
    clarity?: number;
    status?: string;
    mode?: string;
  }) => Promise<string | null>;
  generateNarrative: (keywords: string, mood: string) => Promise<DreamGenerateResponse>;
  refreshDreams: () => Promise<void>;
}

export function useDreams(userId: string = DEFAULT_USER_ID): UseDreamsResult {
  const [dreams, setDreams] = useState<DreamEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  // 将API响应转换为前端格式
  const transformDream = (apiDream: APIDreamEntry): DreamEntry => {
    const createdAt = new Date(apiDream.created_at);
    return {
      id: apiDream.id,
      date: createdAt.toISOString().split("T")[0],
      time: createdAt.toLocaleTimeString("en-US", { hour: "2-digit", minute: "2-digit" }),
      title: apiDream.title || `${createdAt.toLocaleDateString()}的梦`,
      content: apiDream.final_content,
      mood: apiDream.mood || "Neutral",
      symbols: apiDream.tags,
    };
  };

  // 加载梦境列表
  const loadDreams = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const response = await api.dream.getEntries({ user_id: userId, limit: 50 });
      setDreams(response.entries.map(transformDream));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to load dreams");
      console.error("Failed to load dreams:", err);
    } finally {
      setLoading(false);
    }
  }, [userId]);

  // 保存梦境
  const saveDream = useCallback(async (dream: {
    rawInput: string;
    finalContent: string;
    generatedContent?: string;
    title?: string;
    mood?: string;
    tags?: string[];
    clarity?: number;
    status?: string;
    mode?: string;
  }): Promise<string | null> => {
    try {
      const response = await api.dream.saveEntry({
        user_id: userId,
        rawInput: dream.rawInput,
        finalContent: dream.finalContent,
        generatedContent: dream.generatedContent,
        title: dream.title,
        mood: dream.mood,
        tags: dream.tags,
        clarity: dream.clarity,
        status: dream.status || "draft",
        mode: dream.mode || "quick",
      });
      
      // 刷新列表
      await loadDreams();
      
      return response.entry_id;
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to save dream");
      console.error("Failed to save dream:", err);
      return null;
    }
  }, [userId, loadDreams]);

  // 生成叙事
  const generateNarrative = useCallback(async (keywords: string, mood: string): Promise<DreamGenerateResponse> => {
    try {
      return await api.dream.generate({ keywords, mood });
    } catch (err) {
      console.error("Failed to generate narrative:", err);
      return {
        success: false,
        error: err instanceof Error ? err.message : "Generation failed",
      };
    }
  }, []);

  // 初始加载
  useEffect(() => {
    loadDreams();
  }, [loadDreams]);

  return {
    dreams,
    loading,
    error,
    saveDream,
    generateNarrative,
    refreshDreams: loadDreams,
  };
}

export default useDreams;
