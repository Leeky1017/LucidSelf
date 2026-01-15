"use client";

import { Moon, Sun } from "lucide-react";
import type { Theme } from "@/types/common";

interface MobileHeaderProps {
  theme: Theme;
  onThemeToggle: () => void;
  onBackToNow: () => void;
}

export function MobileHeader({ theme, onThemeToggle, onBackToNow }: MobileHeaderProps) {
  return (
    <header className="mobile-header mobile-only">
      <div className="logo-mobile" onClick={onBackToNow}>
        <svg width="24" height="24" viewBox="0 0 32 32" fill="none" className="text-[color:var(--accent-gold)]">
          <circle cx="16" cy="16" r="12" stroke="currentColor" strokeWidth="1" opacity="0.3"/>
          <circle cx="16" cy="16" r="8" stroke="currentColor" strokeWidth="1" opacity="0.5"/>
          <circle cx="16" cy="16" r="4" stroke="currentColor" strokeWidth="1.5"/>
          <path d="M16 4 L16 28 M4 16 L28 16" stroke="currentColor" strokeWidth="0.5" opacity="0.2"/>
        </svg>
        <span>Lucid Self</span>
      </div>
      <button className="theme-toggle" onClick={onThemeToggle} aria-label="Toggle theme">
        {theme === 'dark' ? <Moon size={20} /> : <Sun size={20} />}
      </button>
    </header>
  );
}
