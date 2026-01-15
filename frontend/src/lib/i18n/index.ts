/**
 * i18n 模块导出
 * 
 * 使用方式:
 * 
 * 1. 在根组件包裹 I18nProvider:
 *    ```tsx
 *    import { I18nProvider } from '@/lib/i18n';
 *    
 *    export default function App({ children }) {
 *      return <I18nProvider>{children}</I18nProvider>;
 *    }
 *    ```
 * 
 * 2. 在组件中使用翻译:
 *    ```tsx
 *    import { useTranslation } from '@/lib/i18n';
 *    
 *    function MyComponent() {
 *      const { t } = useTranslation();
 *      return <h1>{t.common.loading}</h1>;
 *    }
 *    ```
 * 
 * 3. 切换语言:
 *    ```tsx
 *    import { useLocale } from '@/lib/i18n';
 *    
 *    function LanguageSwitcher() {
 *      const { locale, setLocale, availableLocales } = useLocale();
 *      return (
 *        <select value={locale} onChange={e => setLocale(e.target.value)}>
 *          {Object.values(availableLocales).map(l => (
 *            <option key={l.code} value={l.code}>{l.nativeName}</option>
 *          ))}
 *        </select>
 *      );
 *    }
 *    ```
 */

// Context and hooks
export { I18nProvider, useI18n, useTranslation, useLocale } from './context';

// Types
export type { Locale, LocaleConfig, Translations } from './types';
export { LOCALES, DEFAULT_LOCALE } from './types';

// Translations (for server-side or direct access)
export { translations } from './locales';
