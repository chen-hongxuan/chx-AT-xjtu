---
title: "Typst processor fixture"
date: 2026-08-26T00:00:00+08:00
math: true
draft: false
---

Unmarked LaTeX stays with MathJax: $\frac{1}{2}$.

Marked inline Typst: $typ:sum_(i=1)^n i$.

$$typ
mat(1, 2; 3, 4)
$$

Single-line marked block: $$typ sum_(i=1)^n i$$

Ordinary MathJax containing the word typ stays MathJax:

$$ typ
x + y
$$
