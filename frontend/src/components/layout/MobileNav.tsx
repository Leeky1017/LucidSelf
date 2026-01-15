"use client";

import { Zap, GitBranch, Clock, Sparkles } from "lucide-react";
import type { View } from "@/types/common";
import { useTranslation } from "@/lib/i18n";

interface MobileNavProps {
  view: View;
  onViewChange: (view: View) => void;
}

export function MobileNav({ view, onViewChange }: MobileNavProps) {
  const { t } = useTranslation();

  return (
    <nav className="mobile-nav mobile-only">
      <button
        className={`mobile-nav-item ${view === 'now' ? 'active' : ''}`}
        onClick={() => onViewChange('now')}
      >
        <Zap size={18} />
        <span>{t.sidebar.now}</span>
      </button>
      <button
        className={`mobile-nav-item ${view === 'life-version' || view === 'version-tree' ? 'active' : ''}`}
        onClick={() => onViewChange('life-version')}
      >
        <GitBranch size={18} />
        <span>{t.sidebar.lifeVersion}</span>
      </button>
      <button
        className={`mobile-nav-item ${view === 'timeline' ? 'active' : ''}`}
        onClick={() => onViewChange('timeline')}
      >
        <Clock size={18} />
        <span>{t.sidebar.timeline}</span>
      </button>
      <button
        className={`mobile-nav-item ${view === 'insight' || view === 'archive' ? 'active' : ''}`}
        onClick={() => onViewChange('insight')}
      >
        <Sparkles size={18} />
        <span>{t.sidebar.insight}</span>
      </button>
    </nav>
  );
}
