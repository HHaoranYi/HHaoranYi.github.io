# 内容编辑与维护指南 (Content Editing Guide)

本指南面向站长日常维护，说明如何更新个人主页、发布学术项目、撰写博客文章以及发布摄影作品。

---

## 1. 个人资料更新 (Profile)

个人主页首屏的学术资料由 `content/authors/admin/_index.md` 统一管理：
- **职称与单位**：修改 `role` 与 `organizations`。
- **简介**：编辑正文底部的文字段落（建议控制在 80–120 词）。
- **研究方向**：修改 `interests` 列表（建议保持 3–4 项核心方向）。
- **学术与社交链接**：修改 `social` 列表（支持 Email, X, GitHub, LinkedIn, Google Scholar）。
- **简历 PDF**：将最新简历放入 `static/uploads/resume.pdf`，无需修改任何代码即可全站同步生效。

---

## 2. 学术与工程项目 (Projects)

每个项目位于 `content/project/<slug>/index.md`：
- 使用结构化技术案例组织：
  - **Overview**：核心问题与研究目标
  - **Motivation**：研究动机
  - **Architecture**：架构与方法
  - **My Contribution**：个人独立贡献
  - **Key Results**：评估指标与实验结果
- 草稿管理：未完成或未公开的项目添加 `draft: true`。

---

## 3. 博客与写作 (Writing)

文章统一放置于 `content/blog/<article-slug>/index.md`：
- **分类标识**：
  - 技术文章：`kind: "technical"`（自动归入 `/blog/technical/`）
  - 个人随笔：`kind: "personal"`（自动归入 `/blog/personal/`）
- **功能特性**：
  - 开启长文目录：`toc: true`
  - 开启数学公式（LaTeX）：`math: true`
- **永久链接保障**：文章 URL 永远为 `/blog/<slug>/`，日后分类调整不会改变文章链接。

---

## 4. 摄影集 (Photography)

每个相册位于 `content/photography/<album-slug>/index.md`：
1. **原片准备**：
   使用提供的优化脚本清除相机 GPS/EXIF 隐私并压缩长边：
   ```bash
   python scripts/photography/optimize_photos.py <照片原图文件夹> content/photography/<相册名>/
   ```
2. **相册配置**：
   在 `index.md` 中配置相册标题、拍摄年份、拍摄地点和文字描述：
   ```yaml
   title: "相册标题"
   date: 2026-09-26
   location: "地点"
   photos:
     - src: "photo-01.webp"
       alt: "图片无障碍说明"
       caption: "展示给读者的图说"
   ```
3. 网页内置响应式大图查看器（支持键盘左右箭头切换与 Esc 关闭）。

---

## 5. 本地预览与上线

1. **本地预览**：
   ```powershell
   hugo server -D
   ```
   浏览器打开 `http://localhost:1313/` 实时预览。
2. **发布上线**：
   提交并推送到 GitHub `main` 分支，GitHub Actions 将自动执行打包构建与 GitHub Pages 部署。
