'use client';

/**
 * Simple Recorder - 极简速记界面
 * 像一张纯粹的纸，只管记录，不带任何 LLM 功能
 */

import { useState } from 'react';
import { motion } from 'framer-motion';
import { X, Check } from 'lucide-react';
import type { DreamEntry } from '@/types/dream';

interface SimpleRecorderProps {
  onClose: () => void;
  onSave: (dream: DreamEntry) => void;
}

export default function SimpleRecorder({ onClose, onSave }: SimpleRecorderProps) {
  const [content, setContent] = useState('');

  const handleSave = () => {
    if (!content.trim()) return;

    const dream: DreamEntry = {
      id: `dream_${Date.now()}`,
      status: 'published',
      mode: 'quick',
      rawInput: content,
      generatedContent: '',
      finalContent: content,
      mood: '',
      generateCount: 0,
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      publishedAt: new Date().toISOString()
    };

    onSave(dream);
    onClose();
  };

  return (
    <motion.div
      className="simple-recorder-overlay"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      onClick={onClose}
    >
      <motion.div
        className="simple-recorder"
        initial={{ scale: 0.95, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.95, opacity: 0 }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* 极简 Header */}
        <div className="simple-header">
          <button 
            className="simple-close" 
            onClick={onClose}
            title="关闭"
          >
            <X size={20} />
          </button>
          
          <button 
            className="simple-save"
            onClick={handleSave}
            disabled={!content.trim()}
            title="保存"
          >
            <Check size={20} />
          </button>
        </div>

        {/* 纯粹的纸 */}
        <textarea
          className="simple-paper"
          placeholder="记录你的梦境..."
          value={content}
          onChange={(e) => setContent(e.target.value)}
          autoFocus
        />
      </motion.div>
    </motion.div>
  );
}
