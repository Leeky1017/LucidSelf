"use client";

import { motion } from "framer-motion";
import type { View } from "@/types/common";
import { modules } from "./data";

interface ModuleGridProps {
  onModuleClick: (moduleId: View) => void;
}

export function ModuleGrid({ onModuleClick }: ModuleGridProps) {
  return (
    <div className="module-grid">
      {modules.map((module, index) => (
        <motion.button
          key={module.id}
          className="module-card"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: index * 0.1, duration: 0.4 }}
          whileHover={{ y: -4 }}
          onClick={() => onModuleClick(module.id)}
        >
          <div className="module-icon" style={{ color: module.color }}>
            <module.icon size={24} strokeWidth={1.5} />
          </div>
          <div className="module-content">
            <h4 className="module-name">{module.name}</h4>
            <p className="module-description">{module.description}</p>
          </div>
        </motion.button>
      ))}
    </div>
  );
}
