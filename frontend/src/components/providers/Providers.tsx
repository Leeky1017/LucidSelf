'use client';

/**
 * 全局 Providers 包装器
 * 
 * 将所有客户端 Provider 集中在此处
 */

import React from 'react';
import { I18nProvider } from '@/lib/i18n';
import { UserProvider } from '@/contexts/UserContext';
import { AuthProvider } from '@/contexts/AuthContext';
import { ThemeProvider } from '@/contexts/ThemeContext';

interface ProvidersProps {
  children: React.ReactNode;
}

export function Providers({ children }: ProvidersProps) {
  return (
    <ThemeProvider>
      <I18nProvider>
        <AuthProvider>
          <UserProvider>
            {children}
          </UserProvider>
        </AuthProvider>
      </I18nProvider>
    </ThemeProvider>
  );
}

export default Providers;
