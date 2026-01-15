# Frontend 前端应用详细结构

## 技术栈
- **框架**: Next.js 14 (App Router)
- **UI**: React 18 + TailwindCSS
- **语言**: TypeScript
- **包管理**: npm

## 目录总览

```
frontend/
├── src/                  # 源代码
│   ├── app/              # Next.js App Router
│   ├── components/       # React组件
│   ├── contexts/         # React Context
│   ├── hooks/            # 自定义Hooks
│   ├── lib/              # 工具库
│   ├── styles/           # 样式文件
│   └── types/            # TypeScript类型定义
├── public/               # 静态资源
├── package.json          # 依赖配置
├── tsconfig.json         # TypeScript配置
├── next.config.ts        # Next.js配置
├── eslint.config.mjs     # ESLint配置
├── postcss.config.mjs    # PostCSS配置
└── .env.local            # 环境变量
```

---

## 1. src/app/ - Next.js App Router

```
src/app/
├── layout.tsx            # 根布局
├── page.tsx              # 首页
├── globals.css           # 全局样式
├── favicon.ico           # 网站图标
└── [备份文件]
```

---

## 2. src/components/ - React组件

```
src/components/
├── # 录入器组件
├── DetailedRecorder.tsx  # 详细录入器
├── DreamRecorder.tsx     # 梦境录入器
├── SimpleRecorder.tsx    # 简单录入器
├── styles-recorders.css  # 录入器样式
│
├── auth/                 # 认证组件
├── layout/               # 布局组件
├── modules/              # 功能模块
├── profile/              # 个人资料组件
└── views/                # 视图组件 (22个)
```

### views/ 详细结构
```
views/
├── # 命理视图
├── BaziView/             # 八字视图
├── AstroView/            # 占星视图
├── TarotView/            # 塔罗视图
├── YijingView/           # 周易视图
├── ZiweiView/            # 紫微视图
├── DreamView/            # 解梦视图
│
├── # 功能视图
├── DashboardView/        # 仪表盘
├── TimelineView/         # 时间线
├── InsightsView/         # 洞察
├── SettingsView/         # 设置
└── ...
```

---

## 3. src/contexts/ - React Context

```
src/contexts/
├── AuthContext.tsx       # 认证上下文
└── ThemeContext.tsx      # 主题上下文
```

---

## 4. src/hooks/ - 自定义Hooks

```
src/hooks/
├── useAuth.ts            # 认证Hook
├── useApi.ts             # API请求Hook
├── useLocalStorage.ts    # 本地存储Hook
└── useTheme.ts           # 主题Hook
```

---

## 5. src/lib/ - 工具库

```
src/lib/
├── api.ts                # API客户端
├── utils.ts              # 通用工具
├── constants.ts          # 常量定义
├── validators.ts         # 验证器
└── formatters.ts         # 格式化工具
```

---

## 6. src/types/ - TypeScript类型

```
src/types/
├── api.ts                # API类型
├── bazi.ts               # 八字类型
├── astro.ts              # 占星类型
├── dream.ts              # 解梦类型
├── user.ts               # 用户类型
└── common.ts             # 通用类型
```

---

## 7. src/styles/ - 样式文件

```
src/styles/
├── globals.css           # 全局样式
├── components.css        # 组件样式
├── themes/               # 主题定义
└── utilities.css         # 工具类
```

---

## 8. public/ - 静态资源

```
public/
├── images/               # 图片资源
├── icons/                # 图标
├── fonts/                # 字体
└── manifest.json         # PWA清单
```

---

## 配置文件说明

| 文件 | 用途 |
|------|------|
| `package.json` | npm依赖与脚本 |
| `tsconfig.json` | TypeScript编译配置 |
| `next.config.ts` | Next.js运行时配置 |
| `eslint.config.mjs` | 代码规范检查 |
| `postcss.config.mjs` | CSS后处理 |
| `.env.local` | 本地环境变量 |

---

## 开发命令

```bash
npm run dev      # 启动开发服务器
npm run build    # 构建生产版本
npm run start    # 启动生产服务器
npm run lint     # 代码检查
```
