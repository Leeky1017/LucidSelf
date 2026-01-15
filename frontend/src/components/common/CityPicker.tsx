'use client';

/**
 * 全球城市选择组件 - 级联选择版
 * 
 * 使用预处理的静态JSON数据，实现国家→省/州→城市三级级联选择
 * 支持全球246个国家/地区，17万+城市的极速本地检索
 */

import { useState, useEffect, useRef, useCallback, useMemo } from 'react';
import { MapPin, X, ChevronDown, Globe, Building, Loader2 } from 'lucide-react';
import { useTranslation, useLocale } from '@/lib/i18n';

// ==================== 类型定义 ====================

interface Country {
  code: string;
  name: string;
  name_zh: string;
  cities: number;
}

interface City {
  id: string;
  n: string;      // 本地名称
  a: string;      // ASCII名称
  lat: number;
  lng: number;
  tz: string;     // timezone
  p: number;      // population
}

interface Admin1 {
  name: string;
  name_local: string;
  cities: City[];
}

interface CountryData {
  country: string;
  name: string;
  name_zh: string;
  admin1s: Record<string, Admin1>;
}

interface SelectedCity {
  displayName: string;
  province: string;
  city: string;
  lat: number;
  lng: number;
  timezone: string;
  countryCode?: string;
}

interface CityPickerProps {
  value?: SelectedCity | null;
  onChange: (city: SelectedCity | null) => void;
  placeholder?: string;
}

// ==================== 数据缓存 ====================

const countriesCache: { data: Country[] | null } = { data: null };
const countryDataCache: Map<string, CountryData> = new Map();

async function loadCountries(): Promise<Country[]> {
  if (countriesCache.data) return countriesCache.data;
  
  const resp = await fetch('/data/cities/countries.json');
  const data = await resp.json();
  countriesCache.data = data;
  return data;
}

async function loadCountryData(countryCode: string): Promise<CountryData | null> {
  if (countryDataCache.has(countryCode)) {
    return countryDataCache.get(countryCode)!;
  }
  
  try {
    const resp = await fetch(`/data/cities/${countryCode}.json`);
    if (!resp.ok) return null;
    const data = await resp.json();
    countryDataCache.set(countryCode, data);
    return data;
  } catch {
    return null;
  }
}

// ==================== 组件 ====================

export function CityPicker({ value, onChange, placeholder }: CityPickerProps) {
  const { t } = useTranslation();
  const { locale } = useLocale();
  const containerRef = useRef<HTMLDivElement>(null);
  
  // 级联选择状态
  const [countries, setCountries] = useState<Country[]>([]);
  const [selectedCountry, setSelectedCountry] = useState<string>('CN');
  const [countryData, setCountryData] = useState<CountryData | null>(null);
  const [selectedAdmin1, setSelectedAdmin1] = useState<string>('');
  const [selectedCityId, setSelectedCityId] = useState<string>('');
  
  // UI状态
  const [isOpen, setIsOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [activeDropdown, setActiveDropdown] = useState<'country' | 'admin1' | 'city' | null>(null);
  const [searchQuery, setSearchQuery] = useState('');

  // 初始化加载国家列表
  useEffect(() => {
    loadCountries().then(setCountries);
  }, []);

  // 加载国家数据
  useEffect(() => {
    if (selectedCountry) {
      setIsLoading(true);
      loadCountryData(selectedCountry).then(data => {
        setCountryData(data);
        setIsLoading(false);
        // 重置下级选择
        setSelectedAdmin1('');
        setSelectedCityId('');
      });
    }
  }, [selectedCountry]);

  // 点击外部关闭
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (containerRef.current && !containerRef.current.contains(event.target as Node)) {
        setIsOpen(false);
        setActiveDropdown(null);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // 获取admin1列表
  const admin1List = useMemo(() => {
    if (!countryData) return [];
    return Object.entries(countryData.admin1s)
      .map(([code, data]) => ({
        code,
        name: data.name,
        name_local: data.name_local,
        cityCount: data.cities.length,
      }))
      .sort((a, b) => b.cityCount - a.cityCount);
  }, [countryData]);

  // 获取城市列表
  const cityList = useMemo(() => {
    if (!countryData || !selectedAdmin1) return [];
    const admin1 = countryData.admin1s[selectedAdmin1];
    if (!admin1) return [];
    
    let cities = admin1.cities;
    
    // 搜索过滤
    if (searchQuery) {
      const q = searchQuery.toLowerCase();
      cities = cities.filter(c => 
        c.n.toLowerCase().includes(q) || 
        c.a.toLowerCase().includes(q)
      );
    }
    
    return cities.slice(0, 100); // 最多显示100个
  }, [countryData, selectedAdmin1, searchQuery]);

  // 选择城市
  const handleSelectCity = useCallback((city: City) => {
    const country = countries.find(c => c.code === selectedCountry);
    const admin1 = countryData?.admin1s[selectedAdmin1];
    
    const countryName = locale === 'zh' ? country?.name_zh : country?.name;
    const admin1Name = admin1?.name_local || admin1?.name || '';
    
    onChange({
      displayName: `${countryName} · ${admin1Name} · ${city.n}`,
      province: admin1Name,
      city: city.n,
      lat: city.lat,
      lng: city.lng,
      timezone: city.tz,
      countryCode: selectedCountry,
    });
    
    setSelectedCityId(city.id);
    setIsOpen(false);
    setActiveDropdown(null);
  }, [countries, countryData, selectedCountry, selectedAdmin1, locale, onChange]);

  // 清除选择
  const handleClear = (e: React.MouseEvent) => {
    e.stopPropagation();
    onChange(null);
    setSelectedCityId('');
  };

  // 获取国家显示名称
  const getCountryDisplayName = (c: Country) => {
    return locale === 'zh' ? c.name_zh : c.name;
  };

  // 常用国家（前10个）
  const topCountries = useMemo(() => {
    return countries.slice(0, 20);
  }, [countries]);

  return (
    <div className="city-picker" ref={containerRef}>
      {/* 显示区域 */}
      <div 
        className={`picker-display ${isOpen ? 'active' : ''}`}
        onClick={() => setIsOpen(true)}
      >
        <MapPin size={16} className="display-icon" />
        {value ? (
          <>
            <span className="display-value">{value.displayName}</span>
            <button type="button" className="clear-btn" onClick={handleClear}>
              <X size={14} />
            </button>
          </>
        ) : (
          <span className="display-placeholder">
            {placeholder || t.profile.birthPlace}
          </span>
        )}
      </div>

      {/* 级联选择面板 */}
      {isOpen && (
        <div className="cascade-panel">
          {/* 三级选择器 */}
          <div className="cascade-selectors">
            {/* 国家选择 */}
            <div className="selector-group">
              <label><Globe size={14} /> {locale === 'zh' ? '国家' : 'Country'}</label>
              <div 
                className={`selector-btn ${activeDropdown === 'country' ? 'active' : ''}`}
                onClick={() => setActiveDropdown(activeDropdown === 'country' ? null : 'country')}
              >
                <span>
                  {countries.find(c => c.code === selectedCountry)
                    ? getCountryDisplayName(countries.find(c => c.code === selectedCountry)!)
                    : '选择国家'}
                </span>
                <ChevronDown size={14} />
              </div>
              {activeDropdown === 'country' && (
                <div className="dropdown-list">
                  {topCountries.map(c => (
                    <button
                      key={c.code}
                      className={`dropdown-item ${selectedCountry === c.code ? 'selected' : ''}`}
                      onClick={() => {
                        setSelectedCountry(c.code);
                        setActiveDropdown('admin1');
                      }}
                    >
                      {getCountryDisplayName(c)}
                      <span className="item-count">{c.cities}</span>
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* 省/州选择 */}
            <div className="selector-group">
              <label><Building size={14} /> {locale === 'zh' ? '省/州' : 'State'}</label>
              <div 
                className={`selector-btn ${activeDropdown === 'admin1' ? 'active' : ''} ${!countryData ? 'disabled' : ''}`}
                onClick={() => countryData && setActiveDropdown(activeDropdown === 'admin1' ? null : 'admin1')}
              >
                {isLoading ? (
                  <Loader2 size={14} className="spinning" />
                ) : (
                  <>
                    <span>
                      {selectedAdmin1 && countryData?.admin1s[selectedAdmin1]
                        ? countryData.admin1s[selectedAdmin1].name_local || countryData.admin1s[selectedAdmin1].name
                        : locale === 'zh' ? '选择省/州' : 'Select state'}
                    </span>
                    <ChevronDown size={14} />
                  </>
                )}
              </div>
              {activeDropdown === 'admin1' && admin1List.length > 0 && (
                <div className="dropdown-list">
                  {admin1List.map(a1 => (
                    <button
                      key={a1.code}
                      className={`dropdown-item ${selectedAdmin1 === a1.code ? 'selected' : ''}`}
                      onClick={() => {
                        setSelectedAdmin1(a1.code);
                        setActiveDropdown('city');
                        setSearchQuery('');
                      }}
                    >
                      {a1.name_local || a1.name}
                      <span className="item-count">{a1.cityCount}</span>
                    </button>
                  ))}
                </div>
              )}
            </div>

            {/* 城市选择 */}
            <div className="selector-group city-selector">
              <label><MapPin size={14} /> {locale === 'zh' ? '城市' : 'City'}</label>
              <input
                type="text"
                className="city-search"
                placeholder={locale === 'zh' ? '搜索城市...' : 'Search city...'}
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                disabled={!selectedAdmin1}
                onFocus={() => setActiveDropdown('city')}
              />
              {activeDropdown === 'city' && cityList.length > 0 && (
                <div className="dropdown-list city-list">
                  {cityList.map(city => (
                    <button
                      key={city.id}
                      className={`dropdown-item ${selectedCityId === city.id ? 'selected' : ''}`}
                      onClick={() => handleSelectCity(city)}
                    >
                      <span className="city-name">{city.n}</span>
                      {city.n !== city.a && <span className="city-ascii">{city.a}</span>}
                    </button>
                  ))}
                </div>
              )}
            </div>
          </div>
        </div>
      )}

      <style jsx>{`
        .city-picker {
          position: relative;
          width: 100%;
        }

        .picker-display {
          display: flex;
          align-items: center;
          gap: var(--space-sm);
          padding: var(--space-sm) var(--space-md);
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          cursor: pointer;
          transition: border-color 0.2s;
          min-height: 42px;
        }

        .picker-display:hover,
        .picker-display.active {
          border-color: var(--accent-gold);
        }

        .display-icon {
          color: var(--text-tertiary);
          flex-shrink: 0;
        }

        .display-value {
          flex: 1;
          font-size: 0.95rem;
          color: var(--text-primary);
          text-align: left;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }

        .display-placeholder {
          flex: 1;
          font-size: 0.95rem;
          color: var(--text-tertiary);
          text-align: left;
        }

        .clear-btn {
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 4px;
          background: none;
          border: none;
          color: var(--text-tertiary);
          cursor: pointer;
          border-radius: var(--radius-sm);
        }

        .clear-btn:hover {
          color: var(--text-primary);
        }

        .cascade-panel {
          position: absolute;
          top: 100%;
          left: 0;
          right: 0;
          margin-top: 4px;
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-lg);
          box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
          z-index: 100;
          padding: var(--space-md);
        }

        .cascade-selectors {
          display: flex;
          gap: var(--space-sm);
        }

        .selector-group {
          flex: 1;
          position: relative;
        }

        .selector-group label {
          display: flex;
          align-items: center;
          gap: 4px;
          font-size: 0.75rem;
          color: var(--text-tertiary);
          margin-bottom: 4px;
          text-transform: uppercase;
          letter-spacing: 0.05em;
        }

        .selector-btn {
          display: flex;
          align-items: center;
          justify-content: space-between;
          gap: var(--space-xs);
          padding: var(--space-sm) var(--space-md);
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          cursor: pointer;
          font-size: 0.9rem;
          color: var(--text-primary);
          transition: all 0.15s;
        }

        .selector-btn:hover,
        .selector-btn.active {
          border-color: var(--accent-gold);
        }

        .selector-btn.disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }

        .selector-btn span {
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }

        .city-search {
          width: 100%;
          padding: var(--space-sm) var(--space-md);
          background: var(--bg-middle);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          font-size: 0.9rem;
          color: var(--text-primary);
          outline: none;
        }

        .city-search:focus {
          border-color: var(--accent-gold);
        }

        .city-search:disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }

        .city-search::placeholder {
          color: var(--text-tertiary);
        }

        .dropdown-list {
          position: absolute;
          top: 100%;
          left: 0;
          right: 0;
          margin-top: 4px;
          background: var(--card-bg);
          border: 1px solid var(--card-border);
          border-radius: var(--radius-md);
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
          max-height: 240px;
          overflow-y: auto;
          z-index: 10;
        }

        .dropdown-item {
          display: flex;
          align-items: center;
          justify-content: space-between;
          width: 100%;
          padding: var(--space-sm) var(--space-md);
          background: none;
          border: none;
          text-align: left;
          cursor: pointer;
          font-size: 0.9rem;
          color: var(--text-primary);
          transition: background 0.1s;
        }

        .dropdown-item:hover {
          background: var(--bg-middle);
        }

        .dropdown-item.selected {
          background: var(--accent-gold-10);
          color: var(--accent-gold);
        }

        .item-count {
          font-size: 0.75rem;
          color: var(--text-tertiary);
        }

        .city-name {
          font-weight: 500;
        }

        .city-ascii {
          font-size: 0.8rem;
          color: var(--text-tertiary);
          margin-left: var(--space-sm);
        }

        .spinning {
          animation: spin 1s linear infinite;
        }

        @keyframes spin {
          from { transform: rotate(0deg); }
          to { transform: rotate(360deg); }
        }

        @media (max-width: 640px) {
          .cascade-selectors {
            flex-direction: column;
          }
        }
      `}</style>
    </div>
  );
}

export default CityPicker;
