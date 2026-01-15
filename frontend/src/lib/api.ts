/**
 * LucidSelf API 客户端
 * 
 * 统一的API调用接口，对接后端服务。
 */

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// ==================== 类型定义 ====================

export type SexAtBirth = "male" | "female";

export interface BirthData {
  year: number;
  month: number;
  day: number;
  hour: number;
  minute?: number;
  timezone?: string;
  sexAtBirth?: SexAtBirth;  // 出生性别（命理计算必需）
  city?: string;  // 与 UserContext.BirthData 保持一致
  latitude?: number;
  longitude?: number;
}

export interface PlaybookReadingRequest {
  user_id: string;
  birth_data: BirthData;
  engines?: string[];
  time_scope?: 'day' | 'week' | 'month' | 'year';
  language?: string;  // 输出语言: zh/en/es/de/ja/ko/fr/ar/it/da/pt
}

export interface InlineSource {
  start: number;
  end: number;
  sources: string[];
}

export interface ReadingParagraph {
  text: string;
  inline_sources: InlineSource[];
}

export interface PlaybookReadingResponse {
  reading_id: string;
  time_scope: string;
  paragraphs: ReadingParagraph[];
  sources_used: Record<string, unknown>;
  engines_used: string[];
  generated_at: string;
  processing_time_ms: number;
}

export interface EngineInfo {
  id: string;
  name: string;
  category: string;
  enabled: boolean;
}

export interface EnginesResponse {
  engines: EngineInfo[];
}

export interface DreamGenerateRequest {
  keywords: string;
  mood: string;
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

export interface DreamGenerateResponse {
  success: boolean;
  narrative?: string;
  tokensUsed?: number;
  model?: string;
  error?: string;
}

export interface DreamAnalyzeRequest {
  dream_text: string;
  user_id?: string;
}

export interface SymbolInfo {
  symbol: string;
  meaning: string;
  category: string;
  confidence: number;
}

export interface EmotionInfo {
  emotion: string;
  intensity: number;
}

export interface DreamAnalyzeResponse {
  symbols: SymbolInfo[];
  themes: string[];
  emotions: EmotionInfo[];
  factors: Record<string, unknown>;
}

export interface DreamEntry {
  id: string;
  user_id: string;
  status: string;
  mode: string;
  raw_input: string;
  generated_content?: string;
  final_content: string;
  title?: string;
  date?: string;
  clarity?: number;
  tags: string[];
  mood?: string;
  generate_count: number;
  created_at: string;
  updated_at: string;
  published_at?: string;
}

export interface DreamEntriesResponse {
  entries: DreamEntry[];
  total: number;
  has_more: boolean;
}

export interface DreamEntryCreateRequest {
  user_id: string;
  title?: string;
  rawInput: string;
  finalContent: string;
  generatedContent?: string;
  mood?: string;
  tags?: string[];
  clarity?: number;
  status?: string;
  mode?: string;
}

export interface DreamEntryCreateResponse {
  entry_id: string;
  created_at: string;
}

// ==================== User Profile 类型 ====================

export interface UserProfileBirthData {
  year: number;
  month: number;
  day: number;
  hour: number;
  minute: number;
  timezone: string;
  gender: string;
  location?: string;
  latitude?: number;
  longitude?: number;
}

export interface UserPreferences {
  language: string;
  theme: string;
  enabled_engines: string[];
  notification_enabled: boolean;
}

export interface UserProfileResponse {
  user_id: string;
  birth_data?: UserProfileBirthData;
  preferences: UserPreferences;
  created_at: string;
  updated_at: string;
}

export interface UserProfileUpdateRequest {
  birth_data?: {
    year: number;
    month: number;
    day: number;
    hour: number;
    minute?: number;
    timezone?: string;
    gender?: string;
    location?: string;
    latitude?: number;
    longitude?: number;
  };
  preferences?: Partial<UserPreferences>;
}

// ==================== HTTP 辅助函数 ====================

async function request<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const url = `${API_BASE}${endpoint}`;
  
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  });
  
  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: response.statusText }));
    throw new Error(error.detail || `Request failed: ${response.status}`);
  }
  
  return response.json();
}

function get<T>(endpoint: string, params?: Record<string, string | number | undefined>): Promise<T> {
  let url = endpoint;
  if (params) {
    const searchParams = new URLSearchParams();
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined) {
        searchParams.append(key, String(value));
      }
    });
    const queryString = searchParams.toString();
    if (queryString) {
      url += `?${queryString}`;
    }
  }
  return request<T>(url, { method: 'GET' });
}

function post<T>(endpoint: string, data: unknown): Promise<T> {
  return request<T>(endpoint, {
    method: 'POST',
    body: JSON.stringify(data),
  });
}

function put<T>(endpoint: string, data: unknown): Promise<T> {
  return request<T>(endpoint, {
    method: 'PUT',
    body: JSON.stringify(data),
  });
}

function del<T>(endpoint: string, params?: Record<string, string>): Promise<T> {
  let url = endpoint;
  if (params) {
    const searchParams = new URLSearchParams();
    Object.entries(params).forEach(([key, value]) => {
      if (value !== undefined) {
        searchParams.append(key, value);
      }
    });
    const queryString = searchParams.toString();
    if (queryString) {
      url += `?${queryString}`;
    }
  }
  return request<T>(url, { method: 'DELETE' });
}

// ==================== API 客户端 ====================

/**
 * 转换前端BirthData为后端格式
 * 前端: sexAtBirth + city
 * 后端: gender + location
 */
function transformBirthData(data: BirthData): Record<string, unknown> {
  return {
    year: data.year,
    month: data.month,
    day: data.day,
    hour: data.hour,
    minute: data.minute ?? 0,
    timezone: data.timezone ?? 'Asia/Shanghai',
    gender: data.sexAtBirth ?? 'male',  // 映射 sexAtBirth -> gender
    location: data.city,  // 映射 city -> location
    latitude: data.latitude,
    longitude: data.longitude,
  };
}

export const api = {
  /**
   * Playbook API
   */
  playbook: {
    /**
     * 获取命理解读
     */
    getReading: (data: PlaybookReadingRequest): Promise<PlaybookReadingResponse> =>
      post('/api/v1/playbook/reading', {
        user_id: data.user_id,
        birth_data: transformBirthData(data.birth_data),
        engines: data.engines,
        time_scope: data.time_scope,
        language: data.language || 'zh',
      }),
    
    /**
     * 获取可用引擎列表
     */
    getEngines: (): Promise<EnginesResponse> =>
      get('/api/v1/playbook/engines'),
  },
  
  /**
   * Dream Journal API
   */
  dream: {
    /**
     * 生成梦境叙事
     */
    generate: (data: DreamGenerateRequest): Promise<DreamGenerateResponse> =>
      post('/api/v1/dream/generate', data),
    
    /**
     * 分析梦境
     */
    analyze: (data: DreamAnalyzeRequest): Promise<DreamAnalyzeResponse> =>
      post('/api/v1/dream/analyze', data),
    
    /**
     * 获取梦境列表
     */
    getEntries: (params: { user_id: string; limit?: number; offset?: number }): Promise<DreamEntriesResponse> =>
      get('/api/v1/dream/entries', params),
    
    /**
     * 保存梦境
     */
    saveEntry: (data: DreamEntryCreateRequest): Promise<DreamEntryCreateResponse> =>
      post('/api/v1/dream/entries', data),
    
    /**
     * 获取单个梦境
     */
    getEntry: (dreamId: string, userId: string): Promise<DreamEntry> =>
      get(`/api/v1/dream/entries/${dreamId}`, { user_id: userId }),
    
    /**
     * 删除梦境
     */
    deleteEntry: (dreamId: string, userId: string): Promise<{ success: boolean }> =>
      del(`/api/v1/dream/entries/${dreamId}`, { user_id: userId }),
  },
  
  /**
   * Timeline API
   */
  timeline: {
    /**
     * 获取合并时间线
     */
    getCombined: (params: {
      user_id: string;
      scale?: 'hour' | 'day' | 'week' | 'month' | 'year';
      start?: string;
      end?: string;
      limit?: number;
    }): Promise<{
      personal: Array<{ id: string; type: string; content: string; timestamp: string; tags: string[] }>;
      insights: Array<{ id: string; source: string; title: string; content: string; timestamp: string; relevance: number }>;
      events: Array<{ id: string; type: string; title: string; summary: string; timestamp: string }>;
      correlations: Array<{ personal_id: string; insight_id: string; correlation_type: string; strength: number }>;
      time_range: { start: string; end: string; scale: string };
    }> =>
      get('/api/v1/timeline/combined', params),
    
    /**
     * 获取个人记录时间线
     */
    getPersonal: (userId: string, limit?: number): Promise<Array<{
      id: string;
      type: string;
      content: string;
      timestamp: string;
      tags: string[];
    }>> =>
      get('/api/v1/timeline/personal', { user_id: userId, limit }),
    
    /**
     * 获取洞察时间线
     */
    getInsights: (userId: string, limit?: number): Promise<Array<{
      id: string;
      source: string;
      title: string;
      content: string;
      timestamp: string;
      relevance: number;
    }>> =>
      get('/api/v1/timeline/insights', { user_id: userId, limit }),
  },
  
  /**
   * Patterns API
   */
  patterns: {
    /**
     * 获取模式列表
     */
    getPatterns: (params: {
      user_id: string;
      category?: string;
      min_strength?: number;
      limit?: number;
    }): Promise<{
      patterns: Array<{
        id: string;
        name: string;
        category: string;
        description: string;
        frequency: string;
        strength: number;
        first_seen: string;
        last_seen: string;
        occurrences: number;
        tags: string[];
      }>;
      core_patterns: Array<{
        id: string;
        name: string;
        category: string;
        description: string;
        strength: number;
        insight: string;
      }>;
      total: number;
      categories: Record<string, number>;
    }> =>
      get('/api/v1/patterns', params),
    
    /**
     * 获取模式详情
     */
    getPatternDetail: (patternId: string, userId: string): Promise<{
      pattern: unknown;
      related_patterns: string[];
      recommendations: string[];
    }> =>
      get(`/api/v1/patterns/${patternId}`, { user_id: userId }),
  },
  
  /**
   * Insights API
   */
  insights: {
    /**
     * 获取深度洞察
     */
    getDeep: (params: {
      user_id: string;
      category?: string;
      depth?: 'surface' | 'medium' | 'deep';
      limit?: number;
    }): Promise<{
      insights: Array<{
        id: string;
        title: string;
        content: string;
        category: string;
        depth: string;
        confidence: number;
        sources: Array<{ type: string; id: string; title: string }>;
        created_at: string;
        actionable: boolean;
        action_suggestions: string[];
      }>;
      summary: string;
      total: number;
      generated_at: string;
    }> =>
      get('/api/v1/insights/deep', params),
    
    /**
     * 获取今日洞察
     */
    getDaily: (userId: string): Promise<{
      id: string;
      title: string;
      content: string;
      category: string;
      depth: string;
      confidence: number;
      action_suggestions: string[];
    }> =>
      get('/api/v1/insights/daily', { user_id: userId }),
    
    /**
     * 提交洞察反馈
     */
    submitFeedback: (data: {
      insight_id: string;
      helpful: boolean;
      comment?: string;
    }): Promise<{ success: boolean; message: string }> =>
      post('/api/v1/insights/feedback', data),
  },
  
  /**
   * User API
   */
  user: {
    /**
     * 获取用户档案
     */
    getProfile: (userId: string): Promise<UserProfileResponse> =>
      get('/api/v1/user/profile', { user_id: userId }),
    
    /**
     * 更新用户档案（包括 birth_data）
     */
    updateProfile: (userId: string, data: UserProfileUpdateRequest): Promise<UserProfileResponse> =>
      put(`/api/v1/user/profile?user_id=${encodeURIComponent(userId)}`, data),
    
    /**
     * 获取用户限制
     */
    getLimits: (userId: string): Promise<{
      daily_dreams: number;
      daily_readings: number;
      dreams_used_today: number;
      readings_used_today: number;
      dreams_remaining: number;
      readings_remaining: number;
      last_reset_date: string;
    }> =>
      get('/api/v1/user/limits', { user_id: userId }),
    
    /**
     * 消费限制额度
     */
    consumeLimit: (userId: string, limitType: 'dream' | 'reading'): Promise<{
      success: boolean;
      remaining: number;
    }> =>
      post(`/api/v1/user/limits/consume?user_id=${userId}&limit_type=${limitType}`, {}),
  },

  /**
   * Life Version API
   */
  versions: {
    /**
     * 获取版本集合
     */
    getVersionSet: (setId: string): Promise<{
      version_set: {
        set_id: string;
        user_id: string;
        scenario_id: string;
        domain: string;
        versions: Array<{
          version_id: string;
          title: string;
          subtitle: string;
          strategy: string[];
          key_actions: string[];
          expected_outcomes: Record<string, number>;
          risks: string[];
          costs: string[];
          suitable_for: string[];
          not_suitable_for: string[];
          confidence: number;
        }>;
        comparison_axes: string[];
        recommended_version_id: string;
      };
      comparison?: unknown;
    }> =>
      get(`/api/v1/versions/${setId}`),
    
    /**
     * 选择版本
     */
    selectVersion: (setId: string, versionId: string, notes?: string): Promise<{
      success: boolean;
      record_id: string;
      message: string;
    }> =>
      post(`/api/v1/versions/${setId}/select/${versionId}`, { notes }),
    
    /**
     * 获取人生导航建议
     */
    navigate: (setId: string, data?: {
      selected_version_id?: string;
      user_context?: Record<string, unknown>;
      deviation_reason?: string;
    }): Promise<{
      narrative: string;
      model_used: string;
      tokens_used: number;
      snippets_count: number;
      processing_time_ms: number;
    }> =>
      post(`/api/v1/versions/${setId}/navigate`, data || {}),
    
    /**
     * 获取版本树
     */
    getTree: (setId: string): Promise<{
      tree: {
        tree_id: string;
        user_id: string;
        root_node_id: string;
        current_node_id: string;
        nodes: Record<string, unknown>;
        scenario_id: string;
        domain: string;
        total_decisions: number;
        max_depth: number;
      };
      current_path: {
        tree_id: string;
        path: string[];
        decisions: string[];
        total_depth: number;
      };
    }> =>
      get(`/api/v1/versions/${setId}/tree`),
  },

  /**
   * Health Check API
   */
  health: {
    /**
     * 健康检查
     */
    check: (): Promise<{ status: string }> =>
      get('/health'),
    
    /**
     * 就绪检查
     */
    ready: (): Promise<{ status: string }> =>
      get('/ready'),
  },

  /**
   * Geocoding API
   */
  geocoding: {
    /**
     * 解析地点获取经纬度和时区
     */
    resolve: (data: {
      input_text: string;
      hint_country?: string;
      user_id?: string;
      hint_label?: string;
    }): Promise<PlaceResponse> =>
      post('/api/v1/geocoding/resolve', data),
    
    /**
     * 搜索地点
     */
    search: (params: {
      q: string;
      country?: string;
      limit?: number;
    }): Promise<{ results: PlaceResponse[]; total: number }> =>
      get('/api/v1/geocoding/search', params),
    
    /**
     * 获取中国常用城市列表
     */
    getChinaCommonCities: (): Promise<CommonCityResponse[]> =>
      get('/api/v1/geocoding/common-cities/china'),
    
    /**
     * 获取中国省份列表
     */
    getChinaProvinces: (): Promise<{ provinces: string[] }> =>
      get('/api/v1/geocoding/provinces/china'),
    
    /**
     * 获取指定省份下的城市列表
     */
    getCitiesByProvince: (province: string): Promise<{ province: string; cities: CommonCityResponse[] }> =>
      get(`/api/v1/geocoding/provinces/china/${encodeURIComponent(province)}/cities`),
  },
};

// ==================== Geocoding 类型 ====================

export interface PlaceResponse {
  place_id: string;
  country_code: string;
  city_name: string;
  lat: number;
  lng: number;
  timezone: string;
  source: string;
  admin1_name?: string;
  display_name: string;
}

export interface CommonCityResponse {
  name: string;
  province: string;
  lat: number;
  lng: number;
  timezone: string;
  display_name: string;
}

export default api;
