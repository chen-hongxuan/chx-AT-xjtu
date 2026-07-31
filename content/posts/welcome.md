---
title: "welcome"
date: 2026-07-31T00:00:00+08:00
slug: "getting-started"
description: "第一篇示例笔记，用来确认公式、代码块和树形标签均已生效。"
tags: []
math: true
draft: false
---

这是博客的第一篇笔记。以后可以删除这篇示例，或把它当作写作模板。

## 数学公式

行内公式：特征值满足 $A\boldsymbol{v}=\lambda\boldsymbol{v}$。

独立公式：

$$
\det(A - \lambda I) = 0
$$

## 代码块

```python
import numpy as np

A = np.array([[2, 1], [1, 2]])
values, vectors = np.linalg.eig(A)
print(values)
```

## 标签如何工作

本文标有“线性代数”和“Python”。在“数学”这个父标签页面中，也能找到这篇文章，因为父标签会自动收集所有子标签的文章。
