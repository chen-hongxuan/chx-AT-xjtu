# chx-AT-xjtu

记录大学课程学习笔记的个人博客，内容以 `.markdown` 文件维护，支持数学公式、代码块和树形标签。

## 写一篇文章

在 `content/posts/` 下新建一个 `.markdown` 文件，复制下面的开头：

```markdown
---
title: "文章标题"
date: 2026-07-31T12:00:00+08:00
tags:
  - math-linear-algebra
math: true
draft: false
---

正文从这里开始。
```

标签必须使用 `data/tag_tree.yaml` 中已有的叶子标签。文章提交到 `main` 后，GitHub Pages 会自动更新。

## 数学公式与代码

- 行内公式：`$a^2+b^2=c^2$`
- 独立公式：`$$ ... $$` 或 `\[ ... \]`
- 代码块：用三个反引号包裹，并在首行写明语言，例如 `python`、`cpp` 或 `java`。

## 标签树

修改 `data/tag_tree.yaml` 可以新增、重命名或调整父子标签；文章只需要填写最具体的叶子标签。父标签页面会自动汇总其全部后代标签的文章。Hugo 会在构建时为标签树中的每个节点自动生成页面，不需要再手工复制 `content/tags/` 下的文件夹。

## 本地预览

安装 Hugo 后，在仓库根目录运行：

```powershell
hugo server
```

浏览器打开终端显示的本地地址即可预览。无需把生成的 `public/` 文件夹提交到仓库。
