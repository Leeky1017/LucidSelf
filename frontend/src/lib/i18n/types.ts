/**
 * i18n 类型定义
 */

export type Locale = 'zh' | 'en' | 'es' | 'de' | 'ja' | 'ko' | 'fr' | 'ar' | 'it' | 'da' | 'pt';

export interface LocaleConfig {
  code: Locale;
  name: string;
  nativeName: string;
  dir: 'ltr' | 'rtl';
}

export const LOCALES: Record<Locale, LocaleConfig> = {
  zh: { code: 'zh', name: 'Chinese', nativeName: '中文', dir: 'ltr' },
  en: { code: 'en', name: 'English', nativeName: 'English', dir: 'ltr' },
  es: { code: 'es', name: 'Spanish', nativeName: 'Español', dir: 'ltr' },
  de: { code: 'de', name: 'German', nativeName: 'Deutsch', dir: 'ltr' },
  ja: { code: 'ja', name: 'Japanese', nativeName: '日本語', dir: 'ltr' },
  ko: { code: 'ko', name: 'Korean', nativeName: '한국어', dir: 'ltr' },
  fr: { code: 'fr', name: 'French', nativeName: 'Français', dir: 'ltr' },
  ar: { code: 'ar', name: 'Arabic', nativeName: 'العربية', dir: 'rtl' },
  it: { code: 'it', name: 'Italian', nativeName: 'Italiano', dir: 'ltr' },
  da: { code: 'da', name: 'Danish', nativeName: 'Dansk', dir: 'ltr' },
  pt: { code: 'pt', name: 'Portuguese', nativeName: 'Português', dir: 'ltr' },
};

export const DEFAULT_LOCALE: Locale = 'zh';

/**
 * 翻译键值结构
 */
export interface Translations {
  // 通用
  common: {
    loading: string;
    error: string;
    success: string;
    cancel: string;
    confirm: string;
    save: string;
    delete: string;
    edit: string;
    back: string;
    next: string;
    submit: string;
    close: string;
    search: string;
    noData: string;
    retry: string;
    // Location picker
    country: string;
    state: string;
    city: string;
    selectState: string;
    searchCity: string;
    // Theme
    switchTheme: string;
    selectTheme: string;
  };

  // 导航
  nav: {
    home: string;
    playbook: string;
    dreamJournal: string;
    timeline: string;
    patterns: string;
    insights: string;
    settings: string;
    profile: string;
    logout: string;
  };

  // 侧边栏导航
  sidebar: {
    now: string;
    lifeVersion: string;
    timeline: string;
    insight: string;
    // 提示文字
    nowHint: string;
    lifeVersionHint: string;
    timelineHint: string;
    insightHint: string;
  };

  // Life Version 页面
  lifeVersion: {
    title: string;
    tagline: string;
    waiting: string;
    versionHistory: string;
    noVersionData: string;
    noVersionHint: string;
    growthDimensions: string;
    career: string;
    wealth: string;
    health: string;
    relationship: string;
    currentFortune: string;
    fortuneHint: string;
    futureSimulation: string;
    simulationDesc: string;
    comingSoon: string;
  };

  // 认证
  auth: {
    login: string;
    signup: string;
    email: string;
    password: string;
    confirmPassword: string;
    forgotPassword: string;
    loginWithEmail: string;
    signupWithEmail: string;
    verificationCode: string;
    sendCode: string;
    resendCode: string;
    verifyEmail: string;
    emailPlaceholder: string;
    passwordPlaceholder: string;
    codePlaceholder: string;
    loginSuccess: string;
    signupSuccess: string;
    invalidCredentials: string;
    emailRequired: string;
    passwordRequired: string;
    passwordTooShort: string;
    passwordsNotMatch: string;
    passwordNoSpaces: string;
    emailInvalid: string;
    codeInvalid: string;
    codeSent: string;
    alreadyHaveAccount: string;
    noAccount: string;
  };

  // 个人资料设置
  profile: {
    title: string;
    subtitle: string;
    greeting: string;
    birthInfo: string;
    dateOfBirth: string;
    timeOfBirth: string;
    birthYear: string;
    birthMonth: string;
    birthDay: string;
    birthHour: string;
    birthMinute: string;
    birthPlace: string;
    sexAtBirth: string;
    sexRequired: string;
    male: string;
    female: string;
    timezone: string;
    selectYear: string;
    selectMonth: string;
    selectDay: string;
    selectHour: string;
    selectMinute: string;
    searchCity: string;
    selectProvince: string;
    selectCity: string;
    commonCities: string;
    timeHint: string;
    unknownTime: string;
    continue: string;
    skip: string;
    saveProfile: string;
    profileSaved: string;
    // Additional settings labels
    name: string;
    guest: string;
    date: string;
    time: string;
    noBirthData: string;
    setupNow: string;
    selectBirthPlace: string;
  };

  // Playbook
  playbook: {
    title: string;
    subtitle: string;
    dailyReading: string;
    weeklyReading: string;
    monthlyReading: string;
    yearlyReading: string;
    generateReading: string;
    generating: string;
    noReading: string;
    luckyColor: string;
    luckyNumber: string;
    luckyDirection: string;
    overallFortune: string;
    careerFortune: string;
    loveFortune: string;
    healthFortune: string;
    wealthFortune: string;
    advice: string;
    warning: string;
    // Time scope labels
    day: string;
    week: string;
    month: string;
    year: string;
    // Engine settings
    enginesActive: string;
    engineSettings: string;
    chooseEngines: string;
    eastern: string;
    western: string;
    // Reading content
    todaySynthesis: string;
    weekSynthesis: string;
    monthSynthesis: string;
    yearSynthesis: string;
    // Source popover
    whyConclusion: string;
    sourceText: string;
    // Errors
    missingLocation: string;
    backendError: string;
    errorHint: string;
  };

  // 梦境日记
  dream: {
    title: string;
    subtitle: string;
    newDream: string;
    quickRecord: string;
    detailedRecord: string;
    dreamContent: string;
    dreamContentPlaceholder: string;
    mood: string;
    moodOptions: {
      peaceful: string;
      anxious: string;
      joyful: string;
      fearful: string;
      confused: string;
      excited: string;
      sad: string;
      neutral: string;
    };
    clarity: string;
    clarityLevels: {
      veryVague: string;
      vague: string;
      moderate: string;
      clear: string;
      veryClear: string;
    };
    tags: string;
    addTag: string;
    generateInterpretation: string;
    interpretation: string;
    symbols: string;
    themes: string;
    emotions: string;
    saveDream: string;
    dreamSaved: string;
    noDreams: string;
    deleteDream: string;
    confirmDelete: string;
    // Additional UI labels
    simpleMode: string;
    recordDream: string;
    realityConnection: string;
    free: string;
    curious: string;
  };

  // 时间线
  timeline: {
    title: string;
    subtitle: string;
    today: string;
    thisWeek: string;
    thisMonth: string;
    allTime: string;
    dreams: string;
    readings: string;
    insights: string;
    noEvents: string;
    // Scale options
    hour: string;
    day: string;
    month: string;
    year: string;
    // Column headers
    yourRecords: string;
    lucidInsights: string;
    entries: string;
    nInsights: string;
    // Entry types
    dreamType: string;
    reflectionType: string;
    eventType: string;
    // Confidence
    confidence: string;
  };

  // 模式
  patterns: {
    title: string;
    subtitle: string;
    corePatterns: string;
    allPatterns: string;
    patternStrength: string;
    occurrences: string;
    firstSeen: string;
    lastSeen: string;
    relatedPatterns: string;
    recommendations: string;
    noPatterns: string;
    categories: {
      dream: string;
      work: string;
      relationship: string;
      spiritual: string;
      body: string;
      all: string;
    };
  };

  // 洞察
  insights: {
    title: string;
    subtitle: string;
    dailyInsight: string;
    deepInsights: string;
    confidence: string;
    sources: string;
    actionSuggestions: string;
    helpful: string;
    notHelpful: string;
    feedbackThanks: string;
    noInsights: string;
    categories: {
      selfAwareness: string;
      growth: string;
      warning: string;
      opportunity: string;
    };
    depths: {
      surface: string;
      medium: string;
      deep: string;
    };
    // Insight details
    generatedOn: string;
    exploreSources: string;
    synthesizedDesc: string;
  };

  // 归档
  archive: {
    title: string;
    subtitle: string;
    patterns: string;
    deepInsights: string;
    chapterProgress: string;
    frequencyTimeline: string;
    aiInsight: string;
    commonContexts: string;
    relatedRecords: string;
    viewAllRecords: string;
    last: string;
    records: string;
  };

  // 今日事项
  todo: {
    title: string;
    pending: string;
    done: string;
    completed: string;
    planPlaceholder: string;
    donePlaceholder: string;
    noRecordsToday: string;
    trackTip: string;
    createFailed: string;
    loginRequired: string;
    loadFailed: string;
  };

  // 设置
  settings: {
    title: string;
    language: string;
    selectLanguage: string;
    theme: string;
    lightTheme: string;
    darkTheme: string;
    systemTheme: string;
    notifications: string;
    enableNotifications: string;
    privacy: string;
    dataExport: string;
    deleteAccount: string;
    about: string;
    version: string;
    termsOfService: string;
    privacyPolicy: string;
  };

  // 错误消息
  errors: {
    networkError: string;
    serverError: string;
    notFound: string;
    unauthorized: string;
    forbidden: string;
    validationError: string;
    unknownError: string;
    tryAgainLater: string;
  };

  // 品牌
  brand: {
    tagline: string;  // 品牌副标语（中文为"晴吾"，其他语言为哲学性描述或空）
    philosophy: string;  // 哲学简介
    quickMode: string;
    quickModeHint: string;
    namePlaceholder: string;
    startExperience: string;
  };

  // Now视图
  nowView: {
    now: string;
    focusMessage: string;
    playbook: string;
    playbookDesc: string;
    viewReading: string;
    dreamJournal: string;
    lastNight: string;
    daysAgo: string;
    openJournal: string;
    today: string;
    trackDaily: string;
    todoStatus: string;
    recordNow: string;
    moreTools: string;
  };

  // 命理引擎（带解释）
  engines: {
    bazi: {
      name: string;
      description: string;
    };
    ziwei: {
      name: string;
      description: string;
    };
    astro: {
      name: string;
      description: string;
    };
    tarot: {
      name: string;
      description: string;
    };
    yijing: {
      name: string;
      description: string;
    };
    dream: {
      name: string;
      description: string;
    };
  };
}
