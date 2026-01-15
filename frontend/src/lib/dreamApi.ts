/**
 * Dream Journal API 客户端
 * 
 * 所有数据通过后端 API 存储，不使用 localStorage
 */

import type { GenerateRequest, GenerateResponse, DreamEntry, UserLimits } from '@/types/dream';
import { api } from '@/lib/api';

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const dreamApi = {
  /**
   * 生成完整梦境叙事
   */
  async generate(request: GenerateRequest): Promise<GenerateResponse> {
    const response = await fetch(`${API_BASE}/api/dream-journal/generate`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        keywords: request.keywords,
        mood: request.mood,
        user_profile: request.userProfile ? {
          bazi: request.userProfile.bazi,
          lunar_phase: request.userProfile.lunarPhase
        } : undefined,
        dream_history: request.dreamHistory,
        canonical_symbols: request.canonicalSymbols
      }),
    });

    if (!response.ok) {
      throw new Error('生成失败，请稍后重试');
    }

    const data = await response.json();
    return {
      success: data.success,
      narrative: data.narrative,
      tokensUsed: data.tokens_used,
      model: data.model,
      error: data.error
    };
  },

  /**
   * 保存草稿到后端
   */
  async saveDraft(dream: DreamEntry, userId: string): Promise<{ success: boolean; dreamId: string }> {
    try {
      const result = await api.dream.saveEntry({
        user_id: userId,
        rawInput: dream.rawInput || '',
        finalContent: dream.finalContent || '',
        mood: dream.mood,
        tags: dream.tags,
        status: 'draft',
      });
      return { success: true, dreamId: result.entry_id };
    } catch (error) {
      console.error('Failed to save draft:', error);
      throw error;
    }
  },

  /**
   * 发布梦境到后端
   */
  async publish(dream: DreamEntry, userId: string): Promise<{ success: boolean; dreamId: string }> {
    try {
      const result = await api.dream.saveEntry({
        user_id: userId,
        rawInput: dream.rawInput || '',
        finalContent: dream.finalContent || '',
        mood: dream.mood,
        tags: dream.tags,
        status: 'published',
      });
      return { success: true, dreamId: result.entry_id };
    } catch (error) {
      console.error('Failed to publish dream:', error);
      throw error;
    }
  },

  /**
   * 获取梦境列表（从后端）
   */
  async getEntries(userId: string, status?: 'draft' | 'published'): Promise<DreamEntry[]> {
    try {
      const response = await api.dream.getEntries({ user_id: userId, limit: 100 });
      const entries = response.entries || [];
      
      // 转换后端格式为前端格式
      const mapped: DreamEntry[] = entries.map((e: any) => ({
        id: e.entry_id,
        status: e.status || 'published',
        mode: e.mode || 'quick',
        rawInput: e.rawInput || e.raw_input || '',
        generatedContent: e.generatedContent || e.generated_content,
        finalContent: e.finalContent || e.final_content || '',
        title: e.title,
        date: e.date,
        clarity: e.clarity,
        tags: e.tags || [],
        mood: e.mood,
        generateCount: e.generateCount || 0,
        createdAt: e.created_at,
        updatedAt: e.updated_at,
        publishedAt: e.published_at,
      }));
      
      // 根据 status 过滤
      if (status) {
        return mapped.filter((e) => e.status === status);
      }
      return mapped;
    } catch (error) {
      console.error('Failed to get entries:', error);
      return [];
    }
  },

  /**
   * 获取草稿列表
   */
  async getDrafts(userId: string): Promise<DreamEntry[]> {
    return this.getEntries(userId, 'draft');
  },

  /**
   * 获取已发布列表
   */
  async getPublished(userId: string): Promise<DreamEntry[]> {
    return this.getEntries(userId, 'published');
  },

  /**
   * 获取用户限制信息（从后端）
   */
  async getUserLimits(userId: string): Promise<UserLimits> {
    try {
      const limits = await api.user.getLimits(userId);
      return {
        dailyDreamsRemaining: limits.dreams_remaining,
        totalDreamsToday: limits.dreams_used_today
      };
    } catch (error) {
      console.error('Failed to get user limits:', error);
      // 返回默认值
      return {
        dailyDreamsRemaining: 3,
        totalDreamsToday: 0
      };
    }
  },

  /**
   * 消费梦境配额
   */
  async consumeDreamLimit(userId: string): Promise<boolean> {
    try {
      const result = await api.user.consumeLimit(userId, 'dream');
      return result.success;
    } catch (error) {
      console.error('Failed to consume dream limit:', error);
      return false;
    }
  }
};
