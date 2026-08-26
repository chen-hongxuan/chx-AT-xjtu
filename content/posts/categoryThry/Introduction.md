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

首先范畴论里最核心的概念就是 universal property , 中文译名叫"泛性质", 于是第一个问题是什么是泛性质. 教材给的第一个例子是一元集 $typ:bold(1)$ , 我们按照范畴论的语言来描述它

>[!definition] Property $I(X)$
> 称一个集合 $X$ 具有性质 $I$ , 简记为 $I(X)$  , 当且仅当对于任意集合 $S$ 存在唯一映射 $typ:f:S->X$ .

显然集合 $\bf 1$ 具有性质 $I$ , 但是一个有趣的事实是

>[!property] Universal property of $\bf 1$
>对于任意的集合 $X$ , 若 $I(X)$ , 则存在 $X$ 到 $\bf 1$ 的双射.

