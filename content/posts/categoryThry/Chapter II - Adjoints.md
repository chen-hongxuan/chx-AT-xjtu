---
title: Chapter II - Adjoints
tags:
  - category-theory
math: true
draft:
date: 2026-08-25
---
$$
\def\A{\mathscr{A}}
\def\B{\mathscr{B}}
\def\map#1{\xrightarrow{\,#1\,}}
\def\op{^{\rm op}}
\def\ob{\mathrm{ob}}
\def\bl{\begin{aligned}}
\def\el{\end{aligned}}
\def\vect{{\bf Vect}}
\def\hom{{\bf Hom}}
\def\id{{\rm id}}
\def\bl{\begin{aligned}}
\def\el{\end{aligned}}
$$

## Definition and examples

>[!definition] Adjoint functors
>对于范畴 $\A,\B$ 以及函子
>$$
>F:\A\to\B,\qquad G:\B\to\A,
>$$
>称 $F$ **左伴随于** $G$, 或者称 $G$ **右伴随于** $F$, 记为
>$$F\dashv G,$$
>当且仅当对于任意的 $A\in\A$ 以及 $B\in\B$, 都有一个指定的一一对应
>$$
>(-)^{*_{A,B}}:\A(A,G(B))\longleftrightarrow\B(F(A),B).
>$$
>对于 $\phi\in\A(A,G(B))$, 以
>$$\phi^{*_{A,B}}\in\B(F(A),B)$$
>表示它在右边的对应; 对于 $\psi\in\B(F(A),B)$, 也以
>$$\psi^{*_{A,B}}\in\A(A,G(B))$$
>表示它在左边的对应. 这里同一个符号 $(-)^{*_{A,B}}$ 同时表示这一对应的两个方向, 具体方向由输入态射所在的 Hom-set 决定. 因为两个方向互为逆映射, 所以
>$$
>\left(\phi^{*_{A,B}}\right)^{*_{A,B}}=\phi,
>\qquad
>\left(\psi^{*_{A,B}}\right)^{*_{A,B}}=\psi.
>$$
>此外, 这一族对应还必须关于 $A$ 和 $B$ 是自然的. 具体来说, 对于任意的对象 $A',A\in\A$ 与 $B,B'\in\B$, 以及态射
>$$
>f:A'\to A,\qquad g:B\to B',\qquad\phi:A\to G(B),
>$$
>复合态射
>$$
>A'\xrightarrow{f}A\xrightarrow{\phi}G(B)\xrightarrow{G(g)}G(B')
>$$
>在对应下必须等于
>$$
>F(A')\xrightarrow{F(f)}F(A)
>\xrightarrow{\phi^{*_{A,B}}}B\xrightarrow{g}B'.
>$$
>也就是说,
>$$
>\boxed{
>\left(G(g)\circ\phi\circ f\right)^{*_{A',B'}}
>=g\circ\phi^{*_{A,B}}\circ F(f)
>}.
>$$

最后的等式说明, 无论我们先在 $\A$ 中复合再取对应, 还是先取对应再在 $\B$ 中复合, 最后得到的态射都是同一个. 这正是 Hom-set 之间的对应关于 $A$ 与 $B$ 的自然性.

>[!example] Product-exponential adjunction in $\mathbf{Set}$
>固定一个集合 $B$. 对集合取与 $B$ 的笛卡尔积以及取从 $B$ 出发的函数集, 分别给出函子
>$$
>-\times B:\mathbf{Set}\to\mathbf{Set},
>\qquad
>(-)^B:\mathbf{Set}\to\mathbf{Set}.
>$$
>对于任意集合 $A,C$, 存在自然的一一对应
>$$
>\mathbf{Set}(A\times B,C)\cong\mathbf{Set}(A,C^B).
>$$
>具体来说, 对于 $g:A\times B\to C$, 定义 $\bar g:A\to C^B$ 为
>$$\bar g(a)(b)=g(a,b).$$
>反过来, 对于 $f:A\to C^B$, 定义 $\bar f:A\times B\to C$ 为
>$$\bar f(a,b)=f(a)(b).$$
>这两个构造互为逆映射, 并且容易验证这一对应关于 $A$ 与 $C$ 是自然的. 因此
>$$
>-\times B\dashv(-)^B.
>$$
>这个对应通常称为 **currying**, 它只是把 $g(a,b)$ 改写成 $\bar g(a)(b)$.

>[!definition] Initial and terminal objects
>设 $\A$ 是一个范畴. 如果对象 $I\in\A$ 满足: 对于任意的 $A\in\A$, 都恰好存在一个态射
>$$I\to A,$$
>那么称 $I$ 是 $\A$ 的**始对象/initial object**.
>
>如果对象 $T\in\A$ 满足: 对于任意的 $A\in\A$, 都恰好存在一个态射
>$$A\to T,$$
>那么称 $T$ 是 $\A$ 的**终对象/terminal object**.

>[!lemma]
>一个范畴的始对象与终对象在唯一同构的意义下是唯一的.

>[!proof]
>设 $I,I'$ 都是始对象. 由始对象的定义, 分别存在唯一的态射
>$$f:I\to I',\qquad g:I'\to I.$$
>于是 $g\circ f$ 与 $1_I$ 都是从 $I$ 到 $I$ 的态射. 因为这样的态射只有一个, 所以 $g\circ f=1_I$. 同理可得 $f\circ g=1_{I'}$, 从而 $f$ 是同构. 又因为从 $I$ 到 $I'$ 的态射只有一个, 所以这个同构也是唯一的.
>
>对于终对象使用方向相反的同样论证即可.

## Adjunctions via units and counits

## Adjunctions via initial objects
