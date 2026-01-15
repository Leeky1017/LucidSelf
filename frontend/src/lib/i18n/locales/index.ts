/**
 * 语言文件索引
 */
import type { Locale, Translations } from '../types';

import { zh } from './zh';
import { en } from './en';
import { es } from './es';
import { de } from './de';
import { ja } from './ja';
import { ko } from './ko';
import { fr } from './fr';
import { ar } from './ar';
import { it } from './it';
import { da } from './da';
import { pt } from './pt';

export const translations: Record<Locale, Translations> = {
  zh,
  en,
  es,
  de,
  ja,
  ko,
  fr,
  ar,
  it,
  da,
  pt,
};

export { zh, en, es, de, ja, ko, fr, ar, it, da, pt };
