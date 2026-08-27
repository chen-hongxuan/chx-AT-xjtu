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

首先范畴论里最核心的概念就是 universal property , 中文译名叫"泛性质", 于是第一个问题是什么是泛性质. 教材给的第一个例子是一元集 $typ:upright(bold(1))$ , 我们按照范畴论的语言来描述它

>[!definition] Property $T(X)$
> 称一个集合 $X$ 具有性质 $T$ , 简记为 $T(X)$  , 当且仅当对于任意集合 $S$ 存在唯一映射 $typ:f:S->X$ .

显然集合 $\bf 1$ 具有性质 $I$ , 但是一个有趣的事实是

>[!theorem] Universal property of $\bf 1$ .
>对于任意的集合 $X$ , 若 $T(X)$ , 则存在 $X$ 到 $\bf 1$ 的双射.

这意味着如果我们把双射视作同构, 那么在同构意义下, 性质 $T$ 唯一地确定了集合 $\bf 1$ . 这就是我们所谓的泛性质, 课本中的原文如是说:

>Properties such as this are called ‘universal’ because they state how the object being described (in this case, the set 1) relates to the entire universe in which it lives (in this case, the universe of sets). The property begins with the words ‘for all sets X’, and therefore says something about the relationship between 1 and every set X: namely, that there is a unique map from X to 1.

注意这里的 Universe 是放在集合论宇宙下的, 我们的语言仅有集合和映射. 下一个例子是环中的, 在这里宇宙是全体环构成的类, 环之间的关系是环同态, 于是考虑一个环 $typ:ZZ$ , 刻画它的一个泛性质是

>[!theorem] Universal property of $typ:ZZ$ .
>对于环 $X$ 而言, 若对于任意环 $R$ , 存在唯一的环同态 $typ:X->R$ , 那么有环同构 $typ: X tilde.equiv ZZ$ .

当然泛性质也不只描述对象, 有时也会描述