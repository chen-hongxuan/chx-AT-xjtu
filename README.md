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

公式默认继续使用 MathJax/LaTeX. 如果一篇文章希望改用 Typst, 在 Front
Matter 中增加:

```yaml
math_engine: typst
```

此时该文章 `$...$` 和 `$$...$$` 内部使用 Typst 数学语法, 例如:

```markdown
$sum_(i=1)^n i$

$$
mat(1, 2; 3, 4)
$$
```

不写 `math_engine`（或写 `math_engine: mathjax`）时, 旧文章的 LaTeX 行为
完全不变. 可复用的 Typst 定义放在 `typst/math-preamble.typ`; 修改它会让
相关 SVG 在下一次构建时自动失效并重新生成. GitHub Actions 只在网站中
确实出现 Typst 公式时安装固定版本的 Typst, 然后把公式编译成透明 SVG.
目前是按文章切换引擎, `math_engine` 应直接写在该文章顶层 Front Matter 中.

也可以在同一篇文章中只把个别公式交给 Typst. 这种写法与 Obsidian 的
Typst Mate Processor ID 兼容, 网站构建时会自动去掉 `typ:` 标记:

```markdown
旧 LaTeX 公式保持不变: $\frac{a}{b}$

Typst 行内公式: $typ:sum_(i=1)^n i$

$$typ
mat(1, 2; 3, 4)
$$
```

未标注的公式仍服从文章的 `math_engine`: 默认使用 MathJax; 只有写了
`math_engine: typst` 的文章才会默认使用 Typst. 块公式按照 Typst Mate
的语法把 Processor ID 写成 `$$typ`; 构建程序也兼容 `$$typ:`.
## 范畴论交换图

在 Obsidian 的 Community plugins 中搜索并安装 `TikZJax`, 然后启用它.
交换图使用 `tikz` 代码块和 `tikz-cd` 语法. 例如:

````markdown
```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large, column sep=large]
A \arrow[r, "f"] \arrow[d, "g"'] & B \arrow[d, "h"] \\
C \arrow[r, "k"'] & D
\end{tikzcd}
\end{document}
```
````


```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large, column sep=large]
A \arrow[r, "f"] \arrow[d,dashed, "g"'] & B \arrow[d, "h"] \\
C \arrow[r, "k"'] & D
\end{tikzcd}
\end{document}
```

```tikz
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}
A\arrow[r,"f"]\arrow[rd,"g",hook] & B\arrow[d,"h"]\\
C\arrow[r,"k"]&D
\end{tikzcd}
\end{document}
```

不要在代码块中添加 `\documentclass`; Obsidian 插件和博客构建程序会自动
使用 `standalone` 文档类. 发布时, GitHub Actions 会把同一份源码编译成
静态 SVG, 因此网页端不需要重新运行 LaTeX. 新图首次部署会稍慢, 已编译
的图会按源码缓存.

## 标签树

修改 `data/tag_tree.yaml` 可以新增、重命名或调整父子标签；文章只需要填写最具体的叶子标签。父标签页面会自动汇总其全部后代标签的文章。Hugo 会在构建时为标签树中的每个节点自动生成页面，不需要再手工复制 `content/tags/` 下的文件夹。

## 本地预览

安装 Hugo 后，在仓库根目录运行：

```powershell
hugo server
```

浏览器打开终端显示的本地地址即可预览。无需把生成的 `public/` 文件夹提交到仓库。

普通公式和文章可直接用 Hugo 预览. `tikz` 交换图在编辑时以 Obsidian 的
TikZJax 预览为准; 网页中的 SVG 会在推送到 GitHub 后由发布流程生成.

`hugo server` 不会运行 Hugo 之后的 Typst SVG 编译步骤. 如需在本地检查
最终网页效果, 请先安装 Typst 0.15.1; 若公式里含中文, 建议同时安装
`Noto Sans CJK SC` 字体. 然后运行:

```powershell
hugo build --baseURL http://localhost:1313/
python scripts/render_typst_math.py --public public --cache .cache/typst-svg --preamble typst/math-preamble.typ
python -m http.server 1313 --directory public
```

然后打开 `http://localhost:1313/`. 这只影响本地生成的 `public/` 和缓存,
不会改写 `content/` 中的 Obsidian 源文件.
