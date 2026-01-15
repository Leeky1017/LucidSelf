"use client";

import { useState, useEffect, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  CheckCircle2,
  Circle,
  Plus,
  X,
  Loader2,
  ListTodo,
  CheckCheck,
  Calendar,
  Trash2
} from "lucide-react";
import type { Theme } from "@/types/common";
import type {
  TodoEntry,
  TodoType,
  TodoDailySummary
} from "@/types/todo";
import { TODO_CONTENT_MAX_LENGTH } from "@/types/todo";
import { todoApi } from "@/lib/todoApi";
import { getStoredToken } from "@/lib/authApi";
import { useTranslation } from "@/lib/i18n";

interface TodoViewProps {
  onClose: () => void;
  theme: Theme;
  userId?: string;
}

export function TodoView({ onClose, theme, userId }: TodoViewProps) {
  const { t } = useTranslation();
  const [summary, setSummary] = useState<TodoDailySummary | null>(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // 输入状态
  const [inputContent, setInputContent] = useState("");
  const [inputType, setInputType] = useState<TodoType>("todo");

  // 加载今日数据（只使用后端 API）
  const loadSummary = useCallback(async () => {
    const token = getStoredToken();

    // 没有 token，显示错误
    if (!token) {
      setError(t.todo.loginRequired || "Please login to use this feature");
      setLoading(false);
      return;
    }

    try {
      setLoading(true);
      setError(null);
      const data = await todoApi.getSummary();
      setSummary(data);
    } catch (err: any) {
      console.error("Failed to load todo summary:", err?.message || err);
      setError(err?.message || t.todo.loadFailed || "Failed to load data");
    } finally {
      setLoading(false);
    }
  }, [t]);

  useEffect(() => {
    loadSummary();
  }, [loadSummary]);

  // 创建条目（只使用后端 API）
  const handleCreate = async () => {
    const content = inputContent.trim();
    if (!content) return;

    try {
      setSubmitting(true);
      setError(null);
      await todoApi.create({ content, entry_type: inputType });
      await loadSummary();
      setInputContent("");
    } catch (err: any) {
      console.error("Failed to create todo:", err?.message || err);
      setError(err?.message || t.todo.createFailed);
    } finally {
      setSubmitting(false);
    }
  };

  // 完成条目
  const handleToggle = async (entry: TodoEntry) => {
    if (entry.status === "completed") return;

    try {
      await todoApi.complete(entry.todo_id);
      await loadSummary();
    } catch (err: any) {
      console.error("Failed to toggle todo:", err?.message || err);
    }
  };

  // 删除条目
  const handleDelete = async (todoId: string) => {
    try {
      await todoApi.delete(todoId);
      await loadSummary();
    } catch (err: any) {
      console.error("Failed to delete todo:", err?.message || err);
    }
  };

  // 字符计数
  const charCount = inputContent.length;
  const isOverLimit = charCount > TODO_CONTENT_MAX_LENGTH;
  const canSubmit = charCount > 0 && !isOverLimit && !submitting;

  return (
    <div className="todo-view">
      {/* Header */}
      <div className="todo-header">
        <div className="header-left">
          <ListTodo size={24} strokeWidth={1.5} className="header-icon" />
          <h1 className="header-title">{t.todo.title}</h1>
        </div>
        <button className="close-btn" onClick={onClose}>
          <X size={20} />
        </button>
      </div>

      {/* Stats */}
      {summary && (
        <motion.div
          className="todo-stats"
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <div className="stat-item">
            <span className="stat-value">{summary.todo_count}</span>
            <span className="stat-label">{t.todo.pending}</span>
          </div>
          <div className="stat-divider" />
          <div className="stat-item">
            <span className="stat-value">{summary.done_count}</span>
            <span className="stat-label">{t.todo.done}</span>
          </div>
          <div className="stat-divider" />
          <div className="stat-item completed">
            <span className="stat-value">{summary.completed_count}</span>
            <span className="stat-label">{t.todo.completed}</span>
          </div>
        </motion.div>
      )}

      {/* Input Area */}
      <motion.div
        className="todo-input-area"
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
      >
        {/* Type Toggle */}
        <div className="type-toggle">
          <button
            className={`type-btn ${inputType === "todo" ? "active" : ""}`}
            onClick={() => setInputType("todo")}
          >
            <Circle size={16} />
            <span>TO-DO</span>
          </button>
          <button
            className={`type-btn ${inputType === "done" ? "active" : ""}`}
            onClick={() => setInputType("done")}
          >
            <CheckCheck size={16} />
            <span>DONE</span>
          </button>
        </div>

        {/* Input */}
        <div className="input-wrapper">
          <textarea
            className="todo-input"
            placeholder={inputType === "todo" ? t.todo.planPlaceholder : t.todo.donePlaceholder}
            value={inputContent}
            onChange={(e) => setInputContent(e.target.value)}
            maxLength={TODO_CONTENT_MAX_LENGTH + 10}
            rows={2}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey && canSubmit) {
                e.preventDefault();
                handleCreate();
              }
            }}
          />
          <div className="input-footer">
            <span className={`char-count ${isOverLimit ? "over" : ""}`}>
              {charCount}/{TODO_CONTENT_MAX_LENGTH}
            </span>
            <button
              className="submit-btn"
              disabled={!canSubmit}
              onClick={handleCreate}
            >
              {submitting ? (
                <Loader2 size={18} className="spinning" />
              ) : (
                <Plus size={18} />
              )}
            </button>
          </div>
        </div>

        {error && (
          <motion.div
            className="error-message"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
          >
            {error}
          </motion.div>
        )}
      </motion.div>

      {/* Entry List */}
      <div className="todo-list">
        {loading ? (
          <div className="loading-state">
            <Loader2 size={24} className="spinning" />
            <span>{t.common.loading}</span>
          </div>
        ) : summary?.entries.length === 0 ? (
          <div className="empty-state">
            <Calendar size={48} strokeWidth={1} />
            <p>{t.todo.noRecordsToday}</p>
            <span>{t.todo.trackTip}</span>
          </div>
        ) : (
          <AnimatePresence>
            {summary?.entries.map((entry, index) => (
              <motion.div
                key={entry.todo_id}
                className={`todo-item ${entry.status === "completed" ? "completed" : ""}`}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                exit={{ opacity: 0, x: 20 }}
                transition={{ delay: index * 0.05 }}
              >
                <button
                  className="toggle-btn"
                  onClick={() => handleToggle(entry)}
                  disabled={entry.status === "completed"}
                >
                  {entry.status === "completed" ? (
                    <CheckCircle2 size={20} className="checked" />
                  ) : (
                    <Circle size={20} />
                  )}
                </button>

                <div className="item-content">
                  <span className={`item-type ${entry.entry_type}`}>
                    {entry.entry_type === "todo" ? "TO-DO" : "DONE"}
                  </span>
                  <p className="item-text">{entry.content}</p>
                </div>

                <button
                  className="delete-btn"
                  onClick={() => handleDelete(entry.todo_id)}
                >
                  <Trash2 size={16} />
                </button>
              </motion.div>
            ))}
          </AnimatePresence>
        )}
      </div>
    </div>
  );
}

export default TodoView;
