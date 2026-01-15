import type { ComponentType } from "react";
import { Lightbulb, BookOpen } from "lucide-react";
import type { View } from "@/types/common";

export interface Module {
  id: View;
  name: string;
  icon: ComponentType<{ size?: number; strokeWidth?: number }>;
  color: string;
  description: string;
}

export const modules: Module[] = [
  {
    id: 'journal',
    name: 'Reflection',
    icon: BookOpen,
    color: 'var(--accent-emerald)',
    description: 'Mindfulness journal',
  },
  {
    id: 'insights',
    name: 'Insights',
    icon: Lightbulb,
    color: 'var(--accent-amber)',
    description: 'Growth tracking',
  },
];
