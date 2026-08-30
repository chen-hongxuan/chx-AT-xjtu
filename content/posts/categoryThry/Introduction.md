---
date: 2026-08-25
tags:
  - category-theory
math: true
draft:
title: Introduction
---
#### 前言

教材是 Cambridge Studies in Advanced Mathematics 系列丛书的 *Basic Category Theory* , 作者是 Tom Leinster. 先前已经学习过一次了, 不过由于上次学完后就把这套知识搁置转而去学习数理逻辑了, 现在感觉技术细节已经遗忘的差不多了, 然而下一个阶段就要开始 Categorical Logic 的学习了, 所以需要快速重拾一下知识.

## Introduction

首先范畴论里最核心的概念就是 universal property , 中文译名叫"泛性质", 于是第一个问题是什么是泛性质. 教材给的第一个例子是一元集 $\bf 1$ , 我们按照范畴论的语言来描述它

>[!definition] Property $T(X)$
> 称一个集合 $X$ 具有性质 $T$ , 简记为 $T(X)$  , 当且仅当对于任意集合 $S$ 存在唯一映射 $f:S\to X$ .

显然集合 $\bf 1$ 具有性质 $T$ , 但是一个有趣的事实是

>[!theorem] Uniqueness of $T$ .
>对于任意的集合 $X$ , 若 $T(X)$ , 则存在 $X$ 到 $\bf 1$ 的双射.

这意味着如果我们把双射视作同构, 那么在同构意义下, 性质 $T$ 唯一地确定了集合 $\bf 1$ . 这就是我们所谓的泛性质, 课本中的原文如是说:

>Properties such as this are called ‘universal’ because they state how the object being described (in this case, the set 1) relates to the entire universe in which it lives (in this case, the universe of sets). The property begins with the words ‘for all sets X’, and therefore says something about the relationship between 1 and every set X: namely, that there is a unique map from X to 1.

注意这里的 Universe 是放在集合论范畴下的, 我们的语言仅有集合和映射. 下一个例子是环中的, 在这里范畴是全体环构成的类, 环之间的关系是环同态, 于是考虑一个环 $\mathbb Z$ , 刻画它的一个泛性质是

>[!theorem] Universal property of $\mathbb Z$ .
>对于环 $X$ 而言, 若对于任意环 $R$ , 存在唯一的环同态 $X\to R$ , 那么有环同构 $X\cong\mathbb Z$ .

下一个例子是在向量空间范畴内的, 在这里的对象是向量空间, 态射是线性映射, 那么对于一个以向量组 $\{v_i:i\in S\}$ 为基底的向量空间 $V$ , 我们该如何描述它呢? 我们看看它与这个向量空间范畴内的其他对象如何互动的: 对于任意向量空间 $W$ 以及从 $V$ 到 $W$ 的线性变换 $f$ , 我们可以通过指定各个基底被映射到哪里了来唯一地确定整个线性变换. 准确的表述如下:
对于固定的集合 $S$ 以及映射 $i:s\mapsto v_s$ , 那么 $V$ 的一个泛性质就是

```tikz size=large
\usepackage{tikz-cd}
\begin{document}\begin{tikzcd}[row sep=large,column sep=large]
S\arrow[r,"i"]\arrow[rd,"\forall\,{\rm function}\,f"']&V\arrow[d,dashed,"\exists!\,{\rm{linear}}\,{\overline{f}}"]\\
&\forall W
\end{tikzcd}\end{document}
```
总之泛性质就是描述范畴里一个对象如何通过态射与其他对象交互的特点, 范畴论里的 Adjoints, Limits, Representative 分别是三种不同的描述泛性质的方式.

## Exercise

### 0.13
#### a.
(Uniqueness) 对于任意的环同态 $f,g:\mathbb Z[x]\to R$ 满足 $f(x)=g(x)=r$ , 那么对于任意的多项式 $F\in\mathbb Z[x]$ , 假定 $$typ F=sum_(i<=0) F_i x^i$$ 那么一定有$$typ f(F)&=sum_(i<=n)F_i r^i\ &=g(F)$$ 从而 $f=g$ .
(Existence) 在唯一性里其实已经证明了, 在指定了$x$ 这个基础元素映射到哪里之后就可以自然的扩张到整个环 $\mathbb Z[x]$ 上了.
#### b.
令环 $A$ 及其中的元素 $a$ 也满足这个性质, 那么我们考虑两个方向的同态 $\phi:a\mapsto x$ 以及 $\psi:x\mapsto a$ , 由于 $A\to A$ 的满足 $a\mapsto a$ 的同态根据对 $A$ 的假设仅有 $\mathrm{id}_A$ , 因此有 $\psi\circ\phi={\rm id}_A$ ; 类似的论证可以得到 $\phi\circ\psi={\rm id}_{\mathbb Z[x]}$ , 从而这个 $\psi$ 即是满足 $\psi(x)=a$ 的同构, 而唯一性可以由 **(a)** 导出.

### 0.14
