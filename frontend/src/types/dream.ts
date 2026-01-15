/**
 * Dream Journal 类型定义
 */

export type DreamMode = 'quick' | 'detailed';
export type DreamStatus = 'draft' | 'published';

export interface DreamEntry {
  id: string;
  status: DreamStatus;
  mode: DreamMode;
  
  // 内容
  rawInput: string;              // 原始输入
  generatedContent?: string;     // AI生成内容
  finalContent: string;          // 最终内容
  
  // 完整模式额外字段
  title?: string;
  date?: string;
  clarity?: number;              // 1-5星
  tags?: string[];
  mood?: string;
  
  // 元数据
  generateCount: number;         // 已使用生成次数
  createdAt: string;
  updatedAt: string;
  publishedAt?: string;
}

export interface GenerateRequest {
  keywords: string;
  mood: string;  // 必需！当时的心情（激动、幸福、紧张、害怕、崩溃等）
  userProfile?: {
    bazi?: {
      dayMaster: string;
      currentLuck: string;
    };
    lunarPhase?: string;
  };
  dreamHistory?: Array<{ pattern: string }>;
  canonicalSymbols?: Record<string, string>;
}

export interface GenerateResponse {
  success: boolean;
  narrative?: string;
  tokensUsed?: number;
  model?: string;
  error?: string;
}

export interface UserLimits {
  dailyDreamsRemaining: number;  // 今日剩余梦境数（最多3个）
  totalDreamsToday: number;      // 今日已记录数
}
