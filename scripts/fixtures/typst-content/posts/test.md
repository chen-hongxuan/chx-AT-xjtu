---
title: "Typst renderer fixture"
date: 2026-08-26T00:00:00+08:00
math: true
math_engine: typst
draft: false
---

Inline formula: $sum_(i=1)^n i$.

Inline source ending in a comment: $x + 1 // keep the closing delimiter safe$.

Chinese text in math: $text("中文")$.

Tall inline formula: $sum_(i=1)^n frac(1, sqrt(x_i))$.

$$
mat(1, 2; 3, 4)
$$

> [!note]
> A formula inside an Obsidian callout:
> $$
> cases(x &"if" x > 0, -x &"otherwise")
> $$

$$
x + y
// A final-line comment must not swallow the generated delimiter.
$$

```text
$this is code, not math$
```
