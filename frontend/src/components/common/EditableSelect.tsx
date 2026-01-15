'use client';

/**
 * 可编辑的下拉选择组件
 * 
 * 同时支持：
 * - 直接键盘输入数字
 * - 点击下拉选择
 * 
 * 这是"隐性双模式"设计：用户无需手动切换，两种交互方式都可用。
 */

import { useState, useRef, useEffect } from 'react';
import { ChevronDown } from 'lucide-react';

interface Option {
  value: number;
  label: string;
}

interface EditableSelectProps {
  value: number;
  onChange: (value: number) => void;
  options: Option[];
  min?: number;
  max?: number;
  label?: string;
  placeholder?: string;
  formatDisplay?: (value: number) => string;
}

export function EditableSelect({
  value,
  onChange,
  options,
  min = 0,
  max = Infinity,
  label,
  placeholder,
  formatDisplay,
}: EditableSelectProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [inputValue, setInputValue] = useState(formatDisplay ? formatDisplay(value) : String(value));
  const [isEditing, setIsEditing] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const dropdownRef = useRef<HTMLDivElement>(null);
  const activeItemRef = useRef<HTMLButtonElement>(null);

  // 同步外部value变化
  useEffect(() => {
    if (!isEditing) {
      setInputValue(formatDisplay ? formatDisplay(value) : String(value));
    }
  }, [value, isEditing, formatDisplay]);

  // 下拉打开时滚动到当前选中项
  useEffect(() => {
    if (isOpen && activeItemRef.current && dropdownRef.current) {
      const dropdown = dropdownRef.current;
      const activeItem = activeItemRef.current;
      const dropdownRect = dropdown.getBoundingClientRect();
      const itemRect = activeItem.getBoundingClientRect();
      
      // 计算需要滚动的位置，让选中项在视口中间
      const scrollTop = activeItem.offsetTop - dropdown.offsetHeight / 2 + itemRect.height / 2;
      dropdown.scrollTop = Math.max(0, scrollTop);
    }
  }, [isOpen]);

  // 点击外部关闭
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setIsOpen(false);
        setIsEditing(false);
        // 恢复显示值
        setInputValue(formatDisplay ? formatDisplay(value) : String(value));
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [value, formatDisplay]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const raw = e.target.value;
    setInputValue(raw);
    
    const num = parseInt(raw, 10);
    if (!isNaN(num) && num >= min && num <= max) {
      onChange(num);
    }
  };

  const handleInputFocus = () => {
    setIsEditing(true);
    setIsOpen(true);
    // 选中全部文字便于直接输入
    setTimeout(() => inputRef.current?.select(), 0);
  };

  const handleInputBlur = () => {
    setIsEditing(false);
    // 验证并修正值
    const num = parseInt(inputValue, 10);
    if (isNaN(num) || num < min || num > max) {
      setInputValue(formatDisplay ? formatDisplay(value) : String(value));
    } else {
      onChange(num);
      setInputValue(formatDisplay ? formatDisplay(num) : String(num));
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      setIsOpen(false);
      inputRef.current?.blur();
    } else if (e.key === 'Escape') {
      setIsOpen(false);
      setInputValue(formatDisplay ? formatDisplay(value) : String(value));
      inputRef.current?.blur();
    } else if (e.key === 'ArrowDown') {
      e.preventDefault();
      const currentIndex = options.findIndex(o => o.value === value);
      if (currentIndex < options.length - 1) {
        onChange(options[currentIndex + 1].value);
      }
    } else if (e.key === 'ArrowUp') {
      e.preventDefault();
      const currentIndex = options.findIndex(o => o.value === value);
      if (currentIndex > 0) {
        onChange(options[currentIndex - 1].value);
      }
    }
  };

  const handleSelectOption = (optValue: number) => {
    onChange(optValue);
    setInputValue(formatDisplay ? formatDisplay(optValue) : String(optValue));
    setIsOpen(false);
    setIsEditing(false);
  };

  const handleChevronClick = (e: React.MouseEvent) => {
    e.stopPropagation();
    setIsOpen(!isOpen);
  };

  return (
    <div className="editable-select" ref={containerRef}>
      {label && <label className="select-label">{label}</label>}
      <div className={`input-wrapper ${isOpen ? 'active' : ''}`}>
        <input
          ref={inputRef}
          type="text"
          inputMode="numeric"
          value={inputValue}
          onChange={handleInputChange}
          onFocus={handleInputFocus}
          onBlur={handleInputBlur}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          className="select-input"
        />
        <button 
          type="button" 
          className="chevron-btn"
          onClick={handleChevronClick}
          tabIndex={-1}
        >
          <ChevronDown size={16} />
        </button>
      </div>

      {isOpen && (
        <div className="dropdown" ref={dropdownRef}>
          {options.map((option) => (
            <button
              key={option.value}
              type="button"
              ref={option.value === value ? activeItemRef : undefined}
              className={`dropdown-item ${option.value === value ? 'active' : ''}`}
              onMouseDown={(e) => {
                e.preventDefault(); // 阻止blur
                handleSelectOption(option.value);
              }}
            >
              {option.label}
            </button>
          ))}
        </div>
      )}

      <style jsx>{`
        .editable-select {
          position: relative;
          display: flex;
          flex-direction: column;
          gap: 6px;
        }

        .select-label {
          font-size: 0.7rem;
          color: var(--text-tertiary);
          text-transform: uppercase;
          letter-spacing: 0.05em;
        }

        .input-wrapper {
          display: flex;
          align-items: center;
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          transition: border-color 0.2s;
        }

        .input-wrapper.active,
        .input-wrapper:focus-within {
          border-color: var(--accent-gold);
        }

        .select-input {
          flex: 1;
          padding: var(--space-sm);
          background: none;
          border: none;
          font-size: 0.95rem;
          color: var(--text-primary);
          outline: none;
          min-width: 0;
        }

        .select-input::placeholder {
          color: var(--text-tertiary);
        }

        .chevron-btn {
          display: flex;
          align-items: center;
          justify-content: center;
          padding: var(--space-sm);
          background: none;
          border: none;
          color: var(--text-tertiary);
          cursor: pointer;
        }

        .chevron-btn:hover {
          color: var(--text-primary);
        }

        .dropdown {
          position: absolute;
          top: 100%;
          left: 0;
          right: 0;
          margin-top: 4px;
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          max-height: 200px;
          overflow-y: auto;
          z-index: 100;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .dropdown-item {
          display: block;
          width: 100%;
          padding: var(--space-xs) var(--space-sm);
          background: none;
          border: none;
          font-size: 0.9rem;
          color: var(--text-secondary);
          text-align: left;
          cursor: pointer;
          transition: background 0.15s;
        }

        .dropdown-item:hover {
          background: var(--bg-middle);
          color: var(--text-primary);
        }

        .dropdown-item.active {
          background: var(--accent-gold);
          color: #fff;
        }
      `}</style>
    </div>
  );
}

export default EditableSelect;
