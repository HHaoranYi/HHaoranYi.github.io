# 内容资产核对清单 (Content Inventory)

记录日期：2026-09-26  
基于分支：`redesign-v2`（基线 Tag：`legacy-v1`）

---

## 1. 个人资料与身份 (Profile & Identity)

| 项 | 旧版状态 | 新版处理方案 | 真实性/来源核实 |
|---|---|---|---|
| 姓名 | Haoran Yi | 保持不变 | 已确认 |
| 职称/身份 | MSc in Embedded Systems | PhD Researcher in Integrated Circuits and Systems | 补充资料候选，已确认方向 |
| 所属机构 | University of Twente | Linköping University | 补充资料候选 |
| 个人简介 | "Haoran Yi is a master student..." | 博士阶段学术简介，突出 IC、神经形态与 AI 硬件 | 需避免未发表/未流片夸大 |
| 研究方向 | Computer Architecture, Hardware Accelerator for DNN | Digital & Mixed-Signal IC Design, Neuromorphic Computing, Sparse AI Hardware, Hardware-Algorithm Co-design | 概括性方向 |
| 教育经历 | UTwente (MSc, 2025), QDU (BEng, 2022) | 补充 Linköping University (PhD)，保留 UTwente 与 QDU | 历史经历保留 |
| 简历 PDF | `static/uploads/resume.pdf` (40KB) | 路径保持不变，/cv/ 页面提供直接下载与查看链接 | 暂保留旧文件，待新 PDF 替换 |
| 社交链接 | Email, X (@HaoranYi_NL), GitHub, LinkedIn | 保持并统一配置，移除占位链接 | 已核验真实账号 |

---

## 2. 项目清单 (Projects)

| 项目 Slug | 来源 | 当前状态 | 规划处理 |
|---|---|---|---|
| `example` (ARM AI Deployment) | 旧仓库已有真实内容 | 已有文字，日期为 2023-April | 规范日期为 2023-04-01，移除 slides 占位，保留公开展示 |
| `external-project` | 旧仓库模板 | 已被注释 | 确认移出公开构建 |
| `wta-selector` | 《规划.txt》候选 | 待提供具体实现参数与验证细节 | 先建立标准项目结构并标记为 `draft: true` |
| `hybrid-attention-cim` | 《规划.txt》候选 | 待提供项目贡献与结果数据 | 先建立标准项目结构并标记为 `draft: true` |
| `neuromorphic-processor` | 《规划.txt》候选 | 硕士论文/数字 IC 项目 | 先建立标准项目结构并标记为 `draft: true` |
| `paper-agent` | 《规划.txt》候选 | 待确认仓库与开源状态 | 先建立标准项目结构并标记为 `draft: true` |

---

## 3. 论文清单 (Publications)

| 目录 | 标题 | 状态 | 规划处理 |
|---|---|---|---|
| `conference-paper` | "Tilele tiele tieleler" (Robert Ford) | 模板占位数据 | 标记 `draft: true`，不参与公开页面构建 |
| `journal-article` | "An example journal article" (Robert Ford) | 模板占位数据 | 标记 `draft: true`，不参与公开页面构建 |
| `preprint` | "An example preprint" (Robert Ford) | 模板占位数据 | 标记 `draft: true`，不参与公开页面构建 |

> **说明**：学术主页在无真实已发表论文时不展示虚假成果，/research/ 与首页 Publications 区块做条件式优雅隐藏或提示待更新。

---

## 4. 文章清单 (Blog / Posts)

| 旧路径 | 标题 | 类型 | 规划处理 |
|---|---|---|---|
| `post/getting-started/` | "Welcome to Hugo Blox" | 主题演示 | 迁入 `content/blog/`，设置旧别名跳转 |
| `post/writing-technical-content/` | "Writing technical content" | 主题演示 | 迁入 `content/blog/technical/` 样例，设置别名 |
| `post/blog-with-jupyter/` | "Display Jupyter Notebooks" | 主题演示 | 迁入 `content/blog/technical/` 样例，设置别名 |

---

## 5. 相册与多媒体 (Photography & Media)

| 资源 | 说明 | 规划处理 |
|---|---|---|
| `assets/media/albums/demo/` | 主题自带 Unsplash 演示图片 | 不作为个人摄影公开发布 |
| `content/photography/` | 新建相册结构 | 建立相册模板与样例，待用户放入精选原片 |
