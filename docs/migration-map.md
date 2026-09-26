# URL 迁移与兼容映射表 (URL Migration Map)

记录日期：2026-09-26  
维护者：Antigravity Agent

---

## 1. 核心架构映射 (Core Routes)

| 旧 URL | 新 URL | 处理方式 | 说明 |
|---|---|---|---|
| `/` | `/` | 保持不变 | 学术主页，首屏展示 Profile，导航为 Home / Research / CV |
| `/#about` | `/#about` | 保持不变 | 锚点兼容，用于页内快速定位 |
| `/#projects` | `/#projects` | 保持不变 | 锚点兼容 |
| `/#featured` | `/#publications` | 双锚点兼容 | 旧菜单指向 `#featured`，新版统一规范为 `#publications`，同时页面内保留兼容 id |
| `/#contact` | `/#contact` | 保持不变 | 锚点兼容 |
| 无 (新增) | `/research/` | 新增独立聚合页 | 聚合研究方向（Research Vision / Areas）、精选项目与论文 |
| 无 (新增) | `/cv/` | 新增入口页 | 承载简历展示与 PDF 下载 |
| `uploads/resume.pdf` | `/uploads/resume.pdf` | 保持不变 | 保留原有 CV 静态文件路径 |
| `/post/` | `/blog/` | 页面重定向 / 别名 | 统一写作入口，次级路径：`/blog/technical/` 与 `/blog/personal/` |
| 无 (新增) | `/photography/` | 新增相册入口 | 独立相册网格与图片浏览器 |

---

## 2. 页面别名 (Hugo Aliases) 配置表

在文章和页面的 Front Matter 中通过 `aliases` 实现静态重定向：

```yaml
# 旧文章重定向至 /blog/<slug>/
aliases:
  - /post/getting-started/
  - /post/writing-technical-content/
  - /post/blog-with-jupyter/
```

确保 `config/_default/hugo.yaml` 中设置：
```yaml
disableAliases: false
```
GitHub Pages 构建后将生成 HTML `<meta http-equiv="refresh">` 重定向页面，保障外部反向链接不失效。
