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

>[!remark] Composition of adjunctions
>设有三个范畴 $\A,\A',\A''$ 以及函子
>$$
>F:\A\to\A',\qquad G:\A'\to\A,
>$$
>$$
>F':\A'\to\A'',\qquad G':\A''\to\A',
>$$
>并且 $F\dashv G$, $F'\dashv G'$. 分别以 $(-)^{*^{FG}}$ 和 $(-)^{*^{F'G'}}$ 表示这两个伴随的对应.
>
>对于任意的 $X\in\A$ 与 $Y\in\A''$, 我们定义 $F'F$ 与 $GG'$ 之间的新对应. 若
>$$\phi:X\to GG'(Y),$$
>则先使用 $F\dashv G$ 的对应, 再使用 $F'\dashv G'$ 的对应, 定义
>$$
>\phi^{*'_{X,Y}}
>:=\left(
>\phi^{*^{FG}_{X,G'(Y)}}
>\right)^{*^{F'G'}_{F(X),Y}}
>:F'F(X)\to Y.
>$$
>反过来, 若 $\psi:F'F(X)\to Y$, 则以相反的顺序定义
>$$
>\psi^{*'_{X,Y}}
>:=\left(
>\psi^{*^{F'G'}_{F(X),Y}}
>\right)^{*^{FG}_{X,G'(Y)}}
>:X\to GG'(Y).
>$$
>因为原来的两个对应都互为逆映射, 所以这里定义的两个方向也互为逆映射.
>
>下面简略验证自然性. 取态射
>$$
>u:X'\to X,\qquad v:Y\to Y',
>$$
>并令
>$$\theta:=\phi^{*^{FG}_{X,G'(Y)}}:F(X)\to G'(Y).$$
>先由 $F\dashv G$ 的自然性可得
>$$
>\left(GG'(v)\circ\phi\circ u\right)^{*^{FG}_{X',G'(Y')}}
>=G'(v)\circ\theta\circ F(u).
>$$
>再由 $F'\dashv G'$ 的自然性可得
>$$
>\bl
>\left(GG'(v)\circ\phi\circ u\right)^{*'_{X',Y'}}
>&=\left(G'(v)\circ\theta\circ F(u)\right)^{*^{F'G'}_{F(X'),Y'}}\\
>&=v\circ\theta^{*^{F'G'}_{F(X),Y}}\circ F'F(u)\\
>&=v\circ\phi^{*'_{X,Y}}\circ F'F(u).
>\el
>$$
>这正是新对应关于 $X$ 与 $Y$ 的自然性. 因此
>$$
>F'\circ F\dashv G\circ G'.
>$$

>[!remark] Non-uniqueness of an adjunction
>即使两个函子 $F$ 与 $G$ 已经固定, 它们之间的伴随对应也未必唯一. 例如取
>$$
>F=G=1_{\mathbf{Vect}_{\mathbb R}}.
>$$
>对于每个非零实数 $\lambda$, 定义
>$$
>\bl\Phi^\lambda_{V,W}:\mathbf{Vect}_{\mathbb R}(V,W)&\to
>\mathbf{Vect}_{\mathbb R}(V,W),\\
>\qquad f&\mapsto\lambda f.\el
>$$
>它是双射, 逆映射为 $g\mapsto\lambda^{-1}g$. 对于任意的线性映射 $u:V'\to V$ 与 $v:W\to W'$, 有
>$$
>\Phi^\lambda_{V',W'}(v\circ f\circ u)
>=\lambda(v\circ f\circ u)
>=v\circ(\lambda f)\circ u,
>$$
>所以这族双射关于 $V,W$ 是自然的, 从而给出一个伴随
>$$
>1_{\mathbf{Vect}_{\mathbb R}}\dashv1_{\mathbf{Vect}_{\mathbb R}}.
>$$
>不同的 $\lambda$ 给出不同的对应. 因此, 伴随的 Hom-set 对应是伴随结构的一部分, 而不能只由函子 $F,G$ 唯一确定.

## Adjunctions via units and counits

>[!note] 学习脉络
>上一节从一族自然的一一对应
>$$
>\B(F(A),B)\cong\A(A,G(B))
>$$
>定义了伴随. 本节将从另一个角度重新叙述同一个概念: 一个伴随也可以由两个自然变换
>$$
>\eta:1_\A\to GF,
>\qquad
>\epsilon:FG\to1_\B
>$$
>以及它们所满足的 triangle identities 来描述. 这不是另一种伴随, 而是用另一组等价的数据记录原来的 Hom-set 对应.

为了找到这两个自然变换, 我们先考虑如何从伴随对应中选出一些最基本的信息. 一个伴随为每对对象 $A\in\A,B\in\B$ 给出了许多态射之间的对应; 在这些态射中, 最特殊的就是恒等态射.

对于任意的 $A\in\A$, 取 $B=F(A)$ 并考察
$$1_{F(A)}:F(A)\to F(A).$$
它的伴随对应是一个态射
$$
\left(1_{F(A)}\right)^{*_{A,F(A)}}:A\to GF(A).
$$
对偶地, 对于任意的 $B\in\B$, 取 $A=G(B)$ 并考察
$$1_{G(B)}:G(B)\to G(B).$$
它的伴随对应是一个态射
$$
\left(1_{G(B)}\right)^{*_{G(B),B}}:FG(B)\to B.
$$
当 $A$ 与 $B$ 变化时, 这两族态射分别组成 unit 与 counit. 因此, unit 和 counit 可以理解为伴随对应在两族恒等态射上留下的信息; 本节接下来要说明, 这些信息实际上足以恢复整个伴随.

## Adjunctions via initial objects

## Exercise

### 2.1.15

>[!exercise]
>设有伴随函子
>$$
>F:\A\rightleftarrows\B:G,
>\qquad F\dashv G.
>$$
>证明左伴随 $F$ 保持始对象: 如果 $I$ 是 $\A$ 中的始对象, 那么 $F(I)$ 是 $\B$ 中的始对象.
>
>对偶地, 证明右伴随 $G$ 保持终对象.

>[!proof]
>先证明左伴随保持始对象. 设 $I$ 是 $\A$ 中的始对象, 那么对于任意的 $X\in\A$, Hom-set
>$$\A(I,X)$$
>都恰好包含一个态射.
>
>现在任取 $Y\in\B$. 由伴随 $F\dashv G$, 有一一对应
>$$
>\B(F(I),Y)\cong\A(I,G(Y)).
>$$
>因为 $G(Y)\in\A$ 且 $I$ 是始对象, 所以右边恰好包含一个态射, 从而左边也恰好包含一个态射. 因此对于每个 $Y\in\B$, 都存在唯一的态射
>$$F(I)\to Y.$$
>所以 $F(I)$ 是 $\B$ 中的始对象.
>
>对偶地, 设 $T$ 是 $\B$ 中的终对象. 对于任意的 $X\in\A$, 伴随对应给出
>$$
>\A(X,G(T))\cong\B(F(X),T).
>$$
>因为 $T$ 是终对象, 所以右边恰好包含一个态射, 从而左边也恰好包含一个态射. 因此对于每个 $X\in\A$, 都存在唯一的态射
>$$X\to G(T).$$
>所以 $G(T)$ 是 $\A$ 中的终对象.
