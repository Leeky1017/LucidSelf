'use client';

/**
 * Detailed Recorder - 沉浸式详细记录
 * 恢复旧版文档型编辑视图，专注于详细记录，不带 LLM
 */

import { useState } from 'react';
import { motion } from 'framer-motion';
import { X, Calendar, Moon, Sparkles, Tag } from 'lucide-react';
import type { DreamEntry } from '@/types/dream';

interface DetailedRecorderProps {
  onClose: () => void;
  onSave: (dream: DreamEntry) => void;
}

export default function DetailedRecorder({ onClose, onSave }: DetailedRecorderProps) {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [mood, setMood] = useState('');
  const [symbols, setSymbols] = useState('');

  const handleSave = () => {
    if (!title.trim() || !content.trim()) return;

    const dream: DreamEntry = {
      id: `dream_${Date.now()}`,
      status: 'published',
      mode: 'detailed',
      rawInput: content,
      generatedContent: '',
      finalContent: content,
      title: title,
      mood: mood || 'Neutral',
      tags: symbols ? symbols.split(',').map(s => s.trim()).filter(Boolean) : [],
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
      className="detailed-recording-view"
      initial={{ opacity: 0, x: 20 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -20 }}
      transition={{ duration: 0.3 }}
    >
      {/* Header */}
      <div className="recording-header">
        <button className="back-button" onClick={onClose}>
          <X size={20} />
          <span>Cancel</span>
        </button>
        <div className="header-status">
          <Moon size={16} className="status-icon" />
          <span>Recording Dream</span>
        </div>
        <button 
          className="save-button-header" 
          onClick={handleSave}
          disabled={!title.trim() || !content.trim()}
        >
          Save
        </button>
      </div>

      {/* Document Canvas */}
      <div className="document-canvas">
        <div className="document-content">
          {/* Title */}
          <input
            type="text"
            className="document-title"
            placeholder="Dream Title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            autoFocus
          />

          {/* Metadata Bar */}
          <div className="metadata-bar">
            <div className="metadata-item">
              <Calendar size={14} />
              <span>
                {new Date().toLocaleDateString("en-US", {
                  month: "short",
                  day: "numeric",
                  year: "numeric",
                })}
              </span>
            </div>
            <div className="metadata-divider">•</div>
            <div className="metadata-item">
              <Moon size={14} />
              <span>
                {new Date().toLocaleTimeString("en-US", { 
                  hour: "2-digit", 
                  minute: "2-digit" 
                })}
              </span>
            </div>
          </div>

          {/* Content */}
          <textarea
            className="document-body"
            placeholder="Describe your dream... What did you see? How did you feel? What symbols appeared in your dreamscape?"
            value={content}
            onChange={(e) => setContent(e.target.value)}
          />

          {/* Properties */}
          <div className="properties-section">
            <div className="property-group">
              <div className="property-label">
                <Sparkles size={14} />
                <span>Mood</span>
              </div>
              <input
                type="text"
                className="property-input"
                placeholder="How did this dream make you feel?"
                value={mood}
                onChange={(e) => setMood(e.target.value)}
              />
            </div>

            <div className="property-group">
              <div className="property-label">
                <Tag size={14} />
                <span>Symbols</span>
              </div>
              <input
                type="text"
                className="property-input"
                placeholder="Water, Flight, Door, Light..."
                value={symbols}
                onChange={(e) => setSymbols(e.target.value)}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Floating Save Button */}
      <button 
        className="floating-save" 
        onClick={handleSave}
        disabled={!title.trim() || !content.trim()}
      >
        <span>Save Dream</span>
      </button>
    </motion.div>
  );
}
