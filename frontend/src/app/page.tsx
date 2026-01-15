"use client";

import { useState, useEffect } from "react";
import { AnimatePresence, motion } from "framer-motion";
import type { View, Theme } from "@/types/common";
import { Sidebar } from "@/components/layout/Sidebar";
import { MobileHeader } from "@/components/layout/MobileHeader";
import { MobileNav } from "@/components/layout/MobileNav";
import { NowView } from "@/components/views/NowView";
import { LifeVersionView } from "@/components/views/LifeVersionView";
import { TimelineView } from "@/components/views/TimelineView";
import { ArchiveView } from "@/components/views/ArchiveView";
import { DreamJournal } from "@/components/views/DreamJournal";
import { Playbook } from "@/components/views/Playbook";
import { TodoView } from "@/components/views/TodoView";
import { LoginPage } from "@/components/auth/LoginPage";
import { ProfileSetup } from "@/components/profile/ProfileSetup";
import { UserSettings } from "@/components/profile/UserSettings";
import { LanguageSelectScreen } from "@/components/onboarding/LanguageSelectScreen";
import { LanguagePage } from "@/components/settings/LanguagePage";
import { UserProvider, useUser, type BirthData } from "@/contexts/UserContext";

function AppContent() {
  const { user, isLoggedIn, isLoading, updateBirthData, refreshUser } = useUser();
  const [view, setView] = useState<View>("now");
  const [theme, setTheme] = useState<Theme>("light");
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false);
  const [showProfileSetup, setShowProfileSetup] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [showLanguagePage, setShowLanguagePage] = useState(false);
  // 首次访问标记（仅在未登录且未选择语言时显示语言选择页）
  const [showLanguageSelect, setShowLanguageSelect] = useState(false);

  useEffect(() => {
    document.documentElement.setAttribute("data-theme", theme);
  }, [theme]);

  // 新用户登录后显示设置页面
  useEffect(() => {
    if (isLoggedIn && user && !user.birthData) {
      setShowProfileSetup(true);
    }
  }, [isLoggedIn, user]);

  const toggleTheme = () => {
    setTheme((prev) => (prev === "dark" ? "light" : "dark"));
  };

  const handleModuleClick = (moduleId: View) => {
    setView(moduleId);
  };

  const handleBackToNow = () => {
    setView("now");
  };



  const handleProfileComplete = async (birthData: BirthData) => {
    await updateBirthData(birthData);
    setShowProfileSetup(false);
  };

  const handleProfileSkip = () => {
    setShowProfileSetup(false);
  };

  // 加载中
  if (isLoading) {
    return (
      <div className="loading-screen">
        <div className="loader" />
      </div>
    );
  }

  // 首次访问且要求显示语言选择页
  if (showLanguageSelect && !isLoggedIn) {
    return (
      <LanguageSelectScreen
        onContinue={() => setShowLanguageSelect(false)}
      />
    );
  }

  // 未登录 - 显示登录页
  if (!isLoggedIn) {
    const handleEmailLogin = async (email: string, password: string) => {
      const { authApi } = await import("@/lib/authApi");
      await authApi.emailLogin({ email, password });
      // Token 已保存，刷新用户状态
      await refreshUser();
    };

    const handleEmailSignup = async (email: string, password: string, name: string) => {
      const { authApi } = await import("@/lib/authApi");
      await authApi.emailSignup({ email, password, name });
      // Token 已保存，刷新用户状态
      await refreshUser();
    };

    return (
      <LoginPage
        onEmailLogin={handleEmailLogin}
        onEmailSignup={handleEmailSignup}
        onLanguageSettings={() => setShowLanguagePage(true)}
      />
    );
  }

  // 语言设置页面（可从登录页或设置页进入）
  if (showLanguagePage) {
    return <LanguagePage onBack={() => setShowLanguagePage(false)} />;
  }

  // 已登录但需要设置个人信息
  if (showProfileSetup) {
    return (
      <ProfileSetup
        userName={user?.name || ""}
        onComplete={handleProfileComplete}
        onSkip={handleProfileSkip}
      />
    );
  }

  // 设置页面
  if (showSettings) {
    return (
      <UserSettings
        onClose={() => setShowSettings(false)}
        onLanguageSettings={() => {
          setShowSettings(false);
          setShowLanguagePage(true);
        }}
      />
    );
  }

  // 转换birthData格式（保留城市/经纬度/时区）
  const apiBirthData = user?.birthData ? {
    year: user.birthData.year,
    month: user.birthData.month,
    day: user.birthData.day,
    hour: user.birthData.hour,
    minute: user.birthData.minute || 0,
    city: user.birthData.city,
    latitude: user.birthData.latitude,
    longitude: user.birthData.longitude,
    timezone: user.birthData.timezone || "Asia/Shanghai",
  } : null;

  const renderView = () => {
    switch (view) {
      case "now":
        return <NowView theme={theme} onModuleClick={handleModuleClick} />;
      case "life-version":
      case "version-tree":
        return <LifeVersionView userId={user?.userId} />;
      case "timeline":
        return <TimelineView theme={theme} />;
      case "insight":
      case "archive":
        return <ArchiveView theme={theme} />;
      case "dream":
        return <DreamJournal onClose={handleBackToNow} userId={user?.userId} />;
      case "playbook":
        return (
          <Playbook
            onClose={handleBackToNow}
            birthData={apiBirthData}
            userId={user?.userId}
          />
        );
      case "todo":
        return (
          <TodoView
            onClose={handleBackToNow}
            theme={theme}
            userId={user?.userId}
          />
        );
      case "journal":
      case "insights":
        return (
          <div className="placeholder-view">
            <h1>Coming Soon</h1>
            <p>This module is under development</p>
          </div>
        );
      default:
        return <NowView theme={theme} onModuleClick={handleModuleClick} />;
    }
  };

  return (
    <div className="app-container">
      <Sidebar
        view={view}
        theme={theme}
        collapsed={sidebarCollapsed}
        onViewChange={setView}
        onThemeToggle={toggleTheme}
        onCollapseToggle={() => setSidebarCollapsed(!sidebarCollapsed)}
        onBackToNow={handleBackToNow}
        onOpenSettings={() => setShowSettings(true)}
        userName={user?.name}
      />

      <MobileHeader
        theme={theme}
        onThemeToggle={toggleTheme}
        onBackToNow={handleBackToNow}
      />

      <main className="main-content">
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
            {renderView()}
          </motion.div>
        </AnimatePresence>
      </main>

      <MobileNav view={view} onViewChange={setView} />
    </div>
  );
}

export default function Home() {
  return (
    <UserProvider>
      <AppContent />
    </UserProvider>
  );
}
