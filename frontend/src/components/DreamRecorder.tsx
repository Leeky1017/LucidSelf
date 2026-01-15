'use client';

/**
 * Dream Recorder - 双模式录制界面
 * Quick模式：快速捕捉关键词
 * Detailed模式：完整记录
 */

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  X, Sparkles, Calendar, Moon, Tag, Loader, Zap, FileText,
  Save, Send, AlertCircle
} from 'lucide-react';
import { dreamApi } from '@/lib/dreamApi';
import type { DreamEntry, DreamMode, UserLimits } from '@/types/dream';

interface DreamRecorderProps {
  onClose: () => void;
  onSave: (dream: DreamEntry) => void;
  editingDream?: DreamEntry;  // 如果有值，则是编辑模式
  userId: string;  // 用户ID，用于后端API调用
}

export default function DreamRecorder({ onClose, onSave, editingDream, userId }: DreamRecorderProps) {
  const [mode, setMode] = useState<DreamMode>(editingDream?.mode || 'quick');
  const [isGenerating, setIsGenerating] = useState(false);
  const [generateCount, setGenerateCount] = useState(editingDream?.generateCount || 0);
  const [userLimits, setUserLimits] = useState<UserLimits>({ dailyDreamsRemaining: 3, totalDreamsToday: 0 });
  
  // 表单状态
  const [rawInput, setRawInput] = useState(editingDream?.rawInput || '');
  const [mood, setMood] = useState(editingDream?.mood || '');  // 必需字段，移到前面
  const [generatedContent, setGeneratedContent] = useState(editingDream?.generatedContent || '');
  const [finalContent, setFinalContent] = useState(editingDream?.finalContent || '');
  
  // Detailed模式额外字段
  const [title, setTitle] = useState(editingDream?.title || '');
  const [clarity, setClarity] = useState(editingDream?.clarity || 3);
  const [tags, setTags] = useState(editingDream?.tags?.join(', ') || '');
  
  // 错误状态
  const [error, setError] = useState('');

  // 加载用户限制
  useEffect(() => {
    if (userId) {
      dreamApi.getUserLimits(userId).then(setUserLimits);
    }
  }, [userId]);

  // Generate 功能
  const handleGenerate = async () => {
    if (!rawInput.trim()) {
      setError('请先输入关键词或梦境描述');
      return;
    }

    if (!mood.trim()) {
      setError('请输入当时的心情（必需！如：激动、害怕、崩溃等）');
      return;
    }

    if (generateCount >= 3) {
      setError('已达到最大生成次数（3次）');
      return;
    }

    setIsGenerating(true);
    setError('');

    try {
      const response = await dreamApi.generate({
        keywords: rawInput,
        mood: mood,  // 必需参数
        userProfile: {
          bazi: {
            dayMaster: '甲木',
            currentLuck: '第6大运'
          },
          lunarPhase: 'Full Moon in Taurus'
        },
        canonicalSymbols: {
          // TODO: 从典籍数据库提取
        }
      });

      if (response.success && response.narrative) {
        setGeneratedContent(response.narrative);
        setFinalContent(response.narrative);
        setGenerateCount(prev => prev + 1);
      } else {
        setError(response.error || '生成失败，请稍后重试');
      }
    } catch (err) {
      setError('网络错误，请检查连接');
      console.error(err);
    } finally {
      setIsGenerating(false);
    }
  };

  // 保存草稿
  const handleSaveDraft = async () => {
    const dream: DreamEntry = {
      id: editingDream?.id || `dream_${Date.now()}`,
      status: 'draft',
      mode,
      rawInput,
      generatedContent,
      finalContent: finalContent || rawInput,
      title: mode === 'detailed' ? title : undefined,
      clarity: mode === 'detailed' ? clarity : undefined,
      tags: mode === 'detailed' && tags ? tags.split(',').map(t => t.trim()) : undefined,
      mood: mode === 'detailed' ? mood : undefined,
      generateCount,
      createdAt: editingDream?.createdAt || new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    try {
      await dreamApi.saveDraft(dream, userId);
      onSave(dream);
      onClose();
    } catch (err) {
      setError('保存失败');
    }
  };

  // 发布
  const handlePublish = async () => {
    if (!finalContent.trim() && !rawInput.trim()) {
      setError('请输入梦境内容');
      return;
    }

    if (userLimits.dailyDreamsRemaining <= 0) {
      setError('今日记录次数已用完（3/3）');
      return;
    }

    const dream: DreamEntry = {
      id: editingDream?.id || `dream_${Date.now()}`,
      status: 'published',
      mode,
      rawInput,
      generatedContent,
      finalContent: finalContent || rawInput,
      title: mode === 'detailed' ? title : `${new Date().toLocaleDateString()}的梦`,
      clarity: mode === 'detailed' ? clarity : undefined,
      tags: mode === 'detailed' && tags ? tags.split(',').map(t => t.trim()) : undefined,
      mood: mode === 'detailed' ? mood : undefined,
      generateCount,
      createdAt: editingDream?.createdAt || new Date().toISOString(),
      updatedAt: new Date().toISOString(),
      publishedAt: new Date().toISOString()
    };

    try {
      await dreamApi.publish(dream, userId);
      await dreamApi.consumeDreamLimit(userId);
      onSave(dream);
      onClose();
    } catch (err) {
      setError('发布失败');
    }
  };

  return (
    <motion.div
      className="dream-recorder-overlay"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      <motion.div
        className="dream-recorder"
        initial={{ scale: 0.95, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        exit={{ scale: 0.95, opacity: 0 }}
      >
        {/* Header */}
        <div className="recorder-header">
          <div className="header-left">
            <h2>Record Dream</h2>
            <span className="limits-badge">
              今日剩余: {userLimits.dailyDreamsRemaining}/3
            </span>
          </div>

          <div className="header-right">
            {/* 模式切换 */}
            <div className="mode-toggle">
              <button
                className={`mode-button ${mode === 'quick' ? 'active' : ''}`}
                onClick={() => setMode('quick')}
              >
                <Zap size={14} />
                <span>Quick</span>
              </button>
              <button
                className={`mode-button ${mode === 'detailed' ? 'active' : ''}`}
                onClick={() => setMode('detailed')}
              >
                <FileText size={14} />
                <span>Detailed</span>
              </button>
            </div>

            <button className="close-button" onClick={onClose}>
              <X size={20} />
            </button>
          </div>
        </div>

        {/* Error Message */}
        <AnimatePresence>
          {error && (
            <motion.div
              className="error-message"
              initial={{ height: 0, opacity: 0 }}
              animate={{ height: 'auto', opacity: 1 }}
              exit={{ height: 0, opacity: 0 }}
            >
              <AlertCircle size={16} />
              <span>{error}</span>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Content */}
        <div className="recorder-content">
          {/* Quick Mode */}
          {mode === 'quick' && (
            <motion.div
              className="quick-mode"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              key="quick"
            >
              <div className="input-label">
                <Sparkles size={14} />
                <span>关键词或简短描述</span>
                <span className="hint">（如: 飞、水、母亲 或一句话描述）</span>
              </div>
              
              <textarea
                className="quick-input"
                placeholder="立即记录你的梦境...&#10;&#10;可以是几个关键词，也可以是一句话。"
                value={rawInput}
                onChange={(e) => setRawInput(e.target.value)}
                autoFocus
                rows={4}
              />

              {/* Mood Input - 必需！ */}
              <div className="mood-input-section">
                <div className="input-label mood-label">
                  <Sparkles size={14} className="mood-icon" />
                  <span>当时的心情</span>
                  <span className="required-badge">必需</span>
                </div>
                <input
                  type="text"
                  className="mood-input"
                  placeholder="激动、幸福、紧张、害怕、崩溃..."
                  value={mood}
                  onChange={(e) => setMood(e.target.value)}
                />
              </div>

              {/* Generate Button */}
              <div className="generate-section">
                <button
                  className="generate-button"
                  onClick={handleGenerate}
                  disabled={isGenerating || generateCount >= 3 || !rawInput.trim()}
                >
                  {isGenerating ? (
                    <>
                      <Loader size={16} className="spinning" />
                      <span>生成中...</span>
                    </>
                  ) : (
                    <>
                      <Sparkles size={16} />
                      <span>Generate ({generateCount}/3)</span>
                    </>
                  )}
                </button>
                <p className="generate-hint">
                  AI 将基于《梦林玄解》和你的命理画像，将关键词和心情串联成简洁但意象丰富的梦境片段（200-400字）
                </p>
              </div>

              {/* Generated Content */}
              {generatedContent && (
                <motion.div
                  className="generated-content"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                >
                  <div className="content-label">
                    <Sparkles size={14} />
                    <span>AI 生成内容</span>
                    <span className="edit-hint">（可手动编辑）</span>
                  </div>
                  <textarea
                    className="content-editor"
                    value={finalContent}
                    onChange={(e) => setFinalContent(e.target.value)}
                  />
                </motion.div>
              )}
            </motion.div>
          )}

          {/* Detailed Mode */}
          {mode === 'detailed' && (
            <motion.div
              className="detailed-mode"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              key="detailed"
            >
              <input
                type="text"
                className="dream-title-input"
                placeholder="Dream Title"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />

              <div className="metadata-row">
                <div className="metadata-item">
                  <Calendar size={14} />
                  <span>{new Date().toLocaleDateString()}</span>
                </div>
                <div className="metadata-divider">•</div>
                <div className="metadata-item">
                  <Moon size={14} />
                  <span>{new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' })}</span>
                </div>
              </div>

              <div className="dream-input-section">
                <div className="input-label">
                  <Sparkles size={14} />
                  <span>关键词/简短描述</span>
                </div>
                <textarea
                  className="dream-keywords"
                  placeholder="飞、水、母亲..."
                  value={rawInput}
                  onChange={(e) => setRawInput(e.target.value)}
                  rows={3}
                />
                <button
                  className="generate-button-inline"
                  onClick={handleGenerate}
                  disabled={isGenerating || generateCount >= 3}
                >
                  <Sparkles size={14} />
                  Generate ({generateCount}/3)
                </button>
              </div>

              <textarea
                className="dream-content-input"
                placeholder="完整梦境内容..."
                value={finalContent}
                onChange={(e) => setFinalContent(e.target.value)}
                rows={12}
              />

              <div className="properties-grid">
                <div className="property-item">
                  <label>清晰度</label>
                  <div className="clarity-stars">
                    {[1, 2, 3, 4, 5].map((star) => (
                      <button
                        key={star}
                        className={`star ${star <= clarity ? 'active' : ''}`}
                        onClick={() => setClarity(star)}
                      >
                        ★
                      </button>
                    ))}
                  </div>
                </div>

                <div className="property-item">
                  <label>
                    <Tag size={14} />
                    <span>标签</span>
                  </label>
                  <input
                    type="text"
                    placeholder="Flying, Water, Mother..."
                    value={tags}
                    onChange={(e) => setTags(e.target.value)}
                  />
                </div>

                <div className="property-item">
                  <label>
                    <Sparkles size={14} />
                    <span>情绪</span>
                  </label>
                  <input
                    type="text"
                    placeholder="Peaceful, Anxious, Excited..."
                    value={mood}
                    onChange={(e) => setMood(e.target.value)}
                  />
                </div>
              </div>
            </motion.div>
          )}
        </div>

        {/* Footer Actions */}
        <div className="recorder-footer">
          <button className="action-btn secondary" onClick={handleSaveDraft}>
            <Save size={16} />
            <span>存草稿</span>
          </button>
          <button className="action-btn primary" onClick={handlePublish}>
            <Send size={16} />
            <span>保存</span>
          </button>
        </div>
      </motion.div>
    </motion.div>
  );
}
