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

>[!definition] Adjoint functors and an adjunction
>对于范畴 $\A,\B$ 以及函子
>$$
>F:\A\to\B,\qquad G:\B\to\A,
>$$
>称 $F$ **左伴随于** $G$, 或者称 $G$ **右伴随于** $F$, 记为
>$$F\dashv G,$$
>当且仅当存在一族关于 $A\in\A$ 与 $B\in\B$ 自然的一一对应
>$$
>(-)^{*_{A,B}}:\A(A,G(B))\longleftrightarrow\B(F(A),B).
>$$
>命题 $F\dashv G$ 只表示至少存在这样一族自然的一一对应. 在所有可能的对应中具体选择一族, 才称为 $F$ 与 $G$ 之间的 **an adjunction**, 在本文中也称为一个**伴随结构**.
>
>以下固定 $F$ 与 $G$ 之间的一个伴随结构. 对于 $\phi\in\A(A,G(B))$, 以
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

>[!remark] 性质与结构
>“$F$ is left adjoint to $G$”与“an adjunction between $F$ and $G$”并不是完全相同的说法:
>
>- **$F$ is left adjoint to $G$** 是一个性质, 它只断言某个伴随结构存在, 记为 $F\dashv G$;
>- **an adjunction between $F$ and $G$** 是一份具体的数据, 它包含一族已经选定的、关于两个对象自然的 Hom-set 一一对应.
>
>这类似于“$X\cong Y$”与“选定一个同构 $f:X\to Y$”之间的区别. 前者只说明存在同构, 后者则指定了一个具体的同构. 在上下文已经固定某个伴随结构时, 通常仍会简写为 $F\dashv G$, 但这时必须记得背后还包含那一族已经选定的对应.

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
>这两个构造互为逆映射, 并且容易验证这一对应关于 $A$ 与 $C$ 是自然的. 因此, currying 给出了这两个函子之间的一个伴随结构, 从而
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
>并且已经分别选定 $F$ 与 $G$ 之间、$F'$ 与 $G'$ 之间的一个伴随结构. 特别地, $F\dashv G$ 且 $F'\dashv G'$. 分别以 $(-)^{*^{FG}}$ 和 $(-)^{*^{F'G'}}$ 表示这两个伴随结构中的对应.
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
>所以这族双射关于 $V,W$ 是自然的, 从而给出一个伴随结构, 并且在性质层面有
>$$
>1_{\mathbf{Vect}_{\mathbb R}}\dashv1_{\mathbf{Vect}_{\mathbb R}}.
>$$
>不同的 $\lambda$ 给出不同的伴随结构, 但它们都使同一个命题 $1_{\mathbf{Vect}_{\mathbb R}}\dashv1_{\mathbf{Vect}_{\mathbb R}}$ 成立. 因此, $F\dashv G$ 这一性质并不包含对伴随结构的唯一选择, 具体的 Hom-set 对应也不能只由函子 $F,G$ 唯一确定.

## Adjunctions via units and counits

>[!note] 学习脉络
>上一节从一族自然的一一对应
>$$
>\B(F(A),B)\cong\A(A,G(B))
>$$
>给出了一个伴随结构. 本节将从另一个角度重新叙述同一个结构: 一个伴随结构也可以由两个自然变换
>$$
>\eta:1_\A\to GF,
>\qquad
>\epsilon:FG\to1_\B
>$$
>以及它们所满足的 triangle identities 来描述. 这不是另一个伴随结构, 而是用另一组等价的数据记录原来那一族 Hom-set 对应.

为了找到这两个自然变换, 我们先固定 $F$ 与 $G$ 之间的一个伴随结构, 并考虑如何从它的 Hom-set 对应中选出一些最基本的信息. 这族对应为每对对象 $A\in\A,B\in\B$ 给出了许多态射之间的对应; 在这些态射中, 最特殊的就是恒等态射.

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
当 $A$ 与 $B$ 变化时, 这两族态射分别组成 unit 与 counit. 因此, unit 和 counit 可以理解为伴随结构中的对应在两族恒等态射上留下的信息; 本节接下来要说明, 这些信息实际上足以恢复整个伴随结构.

准确来说, 对于任意的 $X\in\A$ 与 $Y\in\B$, 定义
$$
\eta_X:=\left(1_{F(X)}\right)^{*_{X,F(X)}}
:X\to G(F(X)),
$$
以及
$$
\epsilon_Y:=\left(1_{G(Y)}\right)^{*_{G(Y),Y}}
:F(G(Y))\to Y.
$$
它们分别组成自然变换
$$
\eta:1_\A\to G\circ F,
\qquad
\epsilon:F\circ G\to1_\B.
$$

>[!lemma] Triangle identities
>固定 $F$ 与 $G$ 之间的一个伴随结构. 由它得到的 unit $\eta$ 与 counit $\epsilon$ 满足如下两条等式. 对于任意的 $X\in\A$,
>$$
>\boxed{\epsilon_{F(X)}\circ F(\eta_X)=1_{F(X)}};
>$$
>对于任意的 $Y\in\B$,
>$$
>\boxed{G(\epsilon_Y)\circ\eta_{G(Y)}=1_{G(Y)}}.
>$$
>也就是说, 下面两幅图交换:
>
>```tikz size=medium
>\usepackage{tikz-cd}
>\begin{document}
>\begin{tikzcd}[row sep=large, column sep=large]
>F(X) \arrow[rr,"F(\eta_X)"] \arrow[dr,"1_{F(X)}"']
>& & F(G(F(X))) \arrow[dl,"\epsilon_{F(X)}"]\\
>& F(X) &
>\end{tikzcd}
>\end{document}
>```
>
>```tikz size=medium
>\usepackage{tikz-cd}
>\begin{document}
>\begin{tikzcd}[row sep=large, column sep=large]
>G(Y) \arrow[rr,"\eta_{G(Y)}"] \arrow[dr,"1_{G(Y)}"']
>& & G(F(G(Y))) \arrow[dl,"G(\epsilon_Y)"]\\
>& G(Y) &
>\end{tikzcd}
>\end{document}
>```

这两条等式的意思很简单. 在第一条等式中, $F(\eta_X)$ 先在 $F(X)$ 中加入一层 $G\circ F$, 然后 $\epsilon_{F(X)}$ 再将这一层消去; 最后得到的结果与恒等态射相同. 第二条等式则是在 $G(Y)$ 上进行同样的过程.

>[!proof]
>先证明第一条等式. 由 unit 的定义, $\eta_X$ 是 $1_{F(X)}$ 的伴随对应, 因此
>$$
>\left(\eta_X\right)^{*_{X,F(X)}}=1_{F(X)}.
>$$
>另一方面, 由 counit 的定义,
>$$
>\left(1_{G(F(X))}\right)^{*_{G(F(X)),F(X)}}
>=\epsilon_{F(X)}.
>$$
>现在对 $1_{G(F(X))}\circ\eta_X$ 使用伴随对应的自然性, 可得
>$$
>\left(1_{G(F(X))}\circ\eta_X\right)^{*_{X,F(X)}}
>=\epsilon_{F(X)}\circ F(\eta_X).
>$$
>因为 $1_{G(F(X))}\circ\eta_X=\eta_X$, 所以左边就是 $1_{F(X)}$. 从而
>$$
>\epsilon_{F(X)}\circ F(\eta_X)=1_{F(X)}.
>$$
>
>对于第二条等式, 同样使用伴随对应的自然性可得
>$$
>\left(G(\epsilon_Y)\circ\eta_{G(Y)}\right)^{*_{G(Y),Y}}
>=\epsilon_Y\circ
>\left(\eta_{G(Y)}\right)^{*_{G(Y),F(G(Y))}}
>=\epsilon_Y.
>$$
>而由 counit 的定义,
>$$
>\left(1_{G(Y)}\right)^{*_{G(Y),Y}}=\epsilon_Y.
>$$
>因为伴随对应是一一对应, 所以
>$$
>G(\epsilon_Y)\circ\eta_{G(Y)}=1_{G(Y)}.
>$$

这两条等式称为 **triangle identities**. 它们不是额外指定的性质, 而是由伴随对应的自然性以及 unit、counit 的定义直接得到的.

>[!lemma] Recovering the adjunction from the unit and counit
>固定 $F$ 与 $G$ 之间的一个伴随结构, 并设其 unit 与 counit 分别为 $\eta$ 和 $\epsilon$. 那么这个伴随结构中的全部 Hom-set 对应都可以由 $\eta$ 和 $\epsilon$ 恢复出来.
>
>具体来说, 对于任意的 $X\in\A$、$Y\in\B$ 以及态射
>$$
>g:F(X)\to Y,
>$$
>它在 $\A$ 中的伴随对应为
>$$
>\boxed{
>g^{*_{X,Y}}=G(g)\circ\eta_X
>}.
>$$
>也就是说, 它是复合态射
>$$
>X\xrightarrow{\eta_X}G(F(X))
>\xrightarrow{G(g)}G(Y).
>$$
>
>反过来, 对于态射
>$$
>f:X\to G(Y),
>$$
>它在 $\B$ 中的伴随对应为
>$$
>\boxed{
>f^{*_{X,Y}}=\epsilon_Y\circ F(f)
>}.
>$$
>也就是说, 它是复合态射
>$$
>F(X)\xrightarrow{F(f)}F(G(Y))
>\xrightarrow{\epsilon_Y}Y.
>$$

>[!proof]
>对于 $g:F(X)\to Y$, 有
>$$
>g=g\circ1_{F(X)}.
>$$
>由 unit 的定义, $1_{F(X)}$ 的伴随对应是 $\eta_X$. 因此由伴随对应的自然性,
>$$
>\bl
>g^{*_{X,Y}}
>&=\left(g\circ1_{F(X)}\right)^{*_{X,Y}}\\
>&=G(g)\circ
>\left(1_{F(X)}\right)^{*_{X,F(X)}}\\
>&=G(g)\circ\eta_X.
>\el
>$$
>
>对于 $f:X\to G(Y)$, 有
>$$
>f=1_{G(Y)}\circ f.
>$$
>由 counit 的定义, $1_{G(Y)}$ 的伴随对应是 $\epsilon_Y$. 因此同样由自然性,
>$$
>\bl
>f^{*_{X,Y}}
>&=\left(1_{G(Y)}\circ f\right)^{*_{X,Y}}\\
>&=\left(1_{G(Y)}\right)^{*_{G(Y),Y}}\circ F(f)\\
>&=\epsilon_Y\circ F(f).
>\el
>$$

这个引理说明, unit 和 counit 虽然只记录了两族恒等态射的伴随对应, 但是由自然性可以从它们求出任意态射的伴随对应. 因此, 当 $F$、$G$、$\eta$ 与 $\epsilon$ 都已经确定时, 原来的伴随对应也就被完全确定了.

不过, 这里不只是使用了“$F\dashv G$”这一存在性命题, 而是先固定了 $F$ 与 $G$ 之间的一个伴随结构. 接下来的 Theorem 2.2.5 将进一步说明: 反过来, 只要给定满足三角等式的 $\eta$ 与 $\epsilon$, 上面的两个公式就能够构造出唯一的伴随结构.

>[!theorem] Adjunctions via units and counits
>给定范畴 $\A,\B$ 以及函子
>$$
>F:\A\to\B,
>\qquad
>G:\B\to\A.
>$$
>以下两类数据之间存在一一对应:
>
>1. $F$ 在左、$G$ 在右的一个伴随结构, 也就是对于每个 $X\in\A$ 与 $Y\in\B$, 指定一个关于 $X,Y$ 自然的一一对应
>   $$
>   \A(X,G(Y))\cong\B(F(X),Y);
>   $$
>2. 一对自然变换
>   $$
>   \eta:1_\A\to G\circ F,
>   \qquad
>   \epsilon:F\circ G\to1_\B,
>   $$
>   并且它们满足三角等式. 将三角等式完全写到对象上, 就是对于任意的 $X\in\A$ 与 $Y\in\B$ 都有
>   $$
>   \epsilon_{F(X)}\circ F(\eta_X)=1_{F(X)},
>   $$
>   以及
>   $$
>   G(\epsilon_Y)\circ\eta_{G(Y)}=1_{G(Y)}.
>   $$

这里的第一项不是只要求命题“$F$ 左伴随于 $G$”成立, 而是包含具体选定的 Hom-set 之间的自然一一对应. 这个定理说明, 将一个伴随结构送到它的 unit 与 counit 时没有丢失信息; 反过来, 满足三角等式的 unit 与 counit 也恰好能够确定一个伴随结构.

>[!proof]
>我们要构造这两类数据之间的对应, 然后依次证明这个对应是良定义的、单射的和满射的.
>
>**由伴随结构得到 unit 与 counit.** 先固定 $F$ 与 $G$ 之间的一个伴随结构. 对于 $X\in\A$ 与 $Y\in\B$, 定义
>$$
>\eta_X:=\left(1_{F(X)}\right)^{*_{X,F(X)}},
>\qquad
>\epsilon_Y:=\left(1_{G(Y)}\right)^{*_{G(Y),Y}}.
>$$
>先说明这两族态射是自然变换. 这里只验证 $\eta$, $\epsilon$ 的自然性可以对偶地得到.
>
>对于任意的态射 $h:X\to X'$, 我们需要证明
>$$
>\eta_{X'}\circ h=G(F(h))\circ\eta_X.
>$$
>等式两边都是从 $X$ 到 $G(F(X'))$ 的态射, 因此可以分别取它们在 $\B(F(X),F(X'))$ 中的伴随对应. 对于左边, 由自然性可得
>$$
>\bl
>\left(\eta_{X'}\circ h\right)^{*_{X,F(X')}}
>&=\left(\eta_{X'}\right)^{*_{X',F(X')}}\circ F(h)\\
>&=1_{F(X')}\circ F(h)\\
>&=F(h).
>\el
>$$
>对于右边, 同样由自然性可得
>$$
>\bl
>\left(G(F(h))\circ\eta_X\right)^{*_{X,F(X')}}
>&=F(h)\circ\left(\eta_X\right)^{*_{X,F(X)}}\\
>&=F(h)\circ1_{F(X)}\\
>&=F(h).
>\el
>$$
>因为伴随对应是一一对应, 所以原来等式的两边相等. 因此 $\eta$ 是自然变换. $\epsilon$ 的自然性对偶地可得, 而 Lemma 2.2.2 又说明它们满足三角等式. 所以从一个伴随结构出发, 的确可以得到定理第二项中的一对自然变换; 这个对应是良定义的.
>
>**单射性.** 假定 $F$ 与 $G$ 之间有两个伴随结构 $(-)^{*^{(1)}}$ 与 $(-)^{*^{(2)}}$, 并且它们导出了相同的 $\eta$ 与 $\epsilon$. 由 Lemma 2.2.4, 对于任意的态射 $f:X\to G(Y)$, 都有
>$$
>f^{*^{(1)}_{X,Y}}=\epsilon_Y\circ F(f)=f^{*^{(2)}_{X,Y}},
>$$
>而对于任意的态射 $g:F(X)\to Y$, 都有
>$$
>g^{*^{(1)}_{X,Y}}=G(g)\circ\eta_X=g^{*^{(2)}_{X,Y}}.
>$$
>因此两个伴随结构中的对应在每个态射上的取值都相同, 所以它们是同一个伴随结构. 这就证明了单射性.
>
>**满射性.** 反过来, 假定给定自然变换
>$$
>\eta:1_\A\to G\circ F,
>\qquad
>\epsilon:F\circ G\to1_\B,
>$$
>并且它们满足三角等式. 对于任意的 $X\in\A$ 与 $Y\in\B$, 我们定义两个方向的对应如下:
>$$
>\bl
>f:X\to G(Y)
>&\quad\longmapsto\quad
>f^{*_{X,Y}}:=\epsilon_Y\circ F(f),\\
>g:F(X)\to Y
>&\quad\longmapsto\quad
>g^{*_{X,Y}}:=G(g)\circ\eta_X.
>\el
>$$
>先说明这两个方向互为逆映射. 对于 $f:X\to G(Y)$, 由构造可得
>$$
>\bl
>\left(f^{*_{X,Y}}\right)^{*_{X,Y}}
>&=G(\epsilon_Y)\circ G(F(f))\circ\eta_X\\
>&=G(\epsilon_Y)\circ\eta_{G(Y)}\circ f\\
>&=f.
>\el
>$$
>第二个等号使用了 $\eta$ 对于态射 $f$ 的自然性, 第三个等号使用了第二条三角等式
>$$
>G(\epsilon_Y)\circ\eta_{G(Y)}=1_{G(Y)}.
>$$
>对于 $g:F(X)\to Y$, 同样有
>$$
>\bl
>\left(g^{*_{X,Y}}\right)^{*_{X,Y}}
>&=\epsilon_Y\circ F(G(g))\circ F(\eta_X)\\
>&=g\circ\epsilon_{F(X)}\circ F(\eta_X)\\
>&=g.
>\el
>$$
>第二个等号使用了 $\epsilon$ 对于态射 $g$ 的自然性, 第三个等号使用了第一条三角等式
>$$
>\epsilon_{F(X)}\circ F(\eta_X)=1_{F(X)}.
>$$
>因此这两个方向互为逆映射.
>
>接下来验证这族对应的自然性. 任取态射
>$$
>u:X'\to X,
>\qquad
>v:Y\to Y',
>\qquad
>\phi:X\to G(Y).
>$$
>由对应的定义以及 $\epsilon$ 对于 $v$ 的自然性,
>$$
>\bl
>\left(G(v)\circ\phi\circ u\right)^{*_{X',Y'}}
>&=\epsilon_{Y'}\circ F(G(v))\circ F(\phi)\circ F(u)\\
>&=v\circ\epsilon_Y\circ F(\phi)\circ F(u)\\
>&=v\circ\phi^{*_{X,Y}}\circ F(u).
>\el
>$$
>这正是伴随对应关于 $X$ 与 $Y$ 的自然性, 所以上面的构造给出了 $F$ 与 $G$ 之间的一个伴随结构.
>
>最后还要验证这个伴随结构导出的 unit 与 counit 正是原来给定的 $\eta$ 与 $\epsilon$. 对于任意的 $X\in\A$,
>$$
>\left(1_{F(X)}\right)^{*_{X,F(X)}}
>=G\left(1_{F(X)}\right)\circ\eta_X
>=\eta_X;
>$$
>对于任意的 $Y\in\B$,
>$$
>\left(1_{G(Y)}\right)^{*_{G(Y),Y}}
>=\epsilon_Y\circ F\left(1_{G(Y)}\right)
>=\epsilon_Y.
>$$
>因此每一对满足三角等式的 $\eta$ 与 $\epsilon$ 都来自一个伴随结构, 从而得到了满射性. 结合前面的单射性, 定理得证.

#### 左伴随构造“最自由”或“最小”的对象

考虑一个伴随结构
$$
F:\A\rightleftarrows\B:G,
\qquad
F\dashv G.
$$
给定一个对象 $X\in\A$ 后, 左伴随首先构造出一个对象
$$
F(X)\in\B.
$$
但是, 只有 $F(X)$ 还不能说明这个构造有什么特殊之处. 伴随结构还给出 unit 的一个分量
$$
\eta_X:X\to G(F(X)).
$$
因为 $X$ 与 $F(X)$ 分别属于 $\A$ 与 $\B$, 所以一般不能直接比较它们. 函子 $G$ 将 $F(X)$ 带回 $\A$ 后, $\eta_X$ 才给出了原对象 $X$ 进入这个新对象的标准方式. 因此, 左伴随在 $X$ 上真正给出的普遍构造应当看成一对数据
$$
\left(F(X),\eta_X:X\to G(F(X))\right).
$$

为了说明它的普遍性, 任取一个对象 $Y\in\B$ 以及态射
$$
f:X\to G(Y),
$$
也就是说, 我们任意给出另一种将 $X$ 放入某个来自 $\B$ 的对象中的方式. 记 $f$ 的伴随对应为
$$
\overline f:=f^{*_{X,Y}}:F(X)\to Y.
$$
这里 $\overline f$ 是 $\B$ 中的态射, 所以它还不能直接与 $\eta_X$ 复合. 对它施加函子 $G$ 后, 可以得到 $\A$ 中的态射
$$
G(\overline f):G(F(X))\to G(Y).
$$
**这个 $G(\overline f)$ 描述了 $G(F(X))$ 进入 $G(Y)$ 的方式.** 这里的“进入”只表示存在这样一个态射, 并不表示它一定是集合意义下的单射. 它的起点恰好是 $\eta_X$ 的终点, 因为
$$
\eta_X:X\to G(F(X)).
$$
所以二者可以自然地复合为
$$
X\xrightarrow{\eta_X}G(F(X))
\xrightarrow{G(\overline f)}G(Y).
$$
伴随对应要求这个复合恰好还原原来的 $f$:
$$
\boxed{G(\overline f)\circ\eta_X=f}.
$$
也就是说, 任意一种将 $X$ 映入 $G(Y)$ 的方式, 都可以唯一地分成上面的两步:

```tikz size=medium
\usepackage{tikz-cd}
\begin{document}
\begin{tikzcd}[row sep=large, column sep=large]
X \arrow[r,"\eta_X"] \arrow[dr,"f"']
& G(F(X)) \arrow[d,"G(\overline f)"]\\
& G(Y)
\end{tikzcd}
\end{document}
```

因此, $\eta_X$ 可以看成所有态射 $X\to G(Y)$ 共有的第一步. 一旦给定 $f:X\to G(Y)$, 它就唯一确定了第二步 $\overline f:F(X)\to Y$, 而 $G(\overline f)$ 则把这第二步带回 $\A$, 使它能够接在 $\eta_X$ 后面. 这正是信息之间的转换
$$
\A(X,G(Y))\cong\B(F(X),Y).
$$

这里还有一个需要注意的地方: 我们需要的不是任意态射 $G(F(X))\to G(Y)$, 而是一个形如 $G(\overline f)$ 的态射, 其中 $\overline f$ 必须是 $\B$ 中的态射. 因此, 这个分解不仅给出一个集合层面的映射, 还保留了 $\B$ 中的结构. 真正重要的性质是: 对于每个 $f:X\to G(Y)$, 都存在唯一的 $\overline f:F(X)\to Y$ 使上述三角形交换.

这就是“最自由”或“最小”中的“最”所表达的内容. 它通常不是说 $F(X)$ 的元素数量最少, 也不是说它与 $X$ 的距离最近, 而是说: 对于任意其他候选对象 $Y$ 以及任意候选方式 $f:X\to G(Y)$, 都存在唯一的态射 $\overline f:F(X)\to Y$ 与之对应. 因此, 其他候选构造都可以由 $F(X)$ 以唯一的方式得到.

在不同范畴中, 这个普遍性质会表现成不同的“最”:

- 对于自由群函子, $F(X)$ 是由集合 $X$ 生成的最自由的群. 任意函数 $X\to G(Y)$ 都唯一延伸为群同态 $F(X)\to Y$, 所以这里的“最自由”表示没有加入不必要的关系;
- 对于闭包函子, $F(A)=\operatorname{Cl}(A)$ 是包含 $A$ 的最小闭集. 任意包含 $A$ 的闭集 $B$ 都满足 $\operatorname{Cl}(A)\subseteq B$, 所以这里的普遍性质真的表现为包含关系下的最小性.

因此,“给定一个对象以后, 左伴随构造出满足某种额外条件的最自由或最小的对象”这句话的准确含义是: 左伴随为 $X$ 构造 $F(X)$ 以及标准态射 $\eta_X:X\to G(F(X))$, 并且任意其他形如 $f:X\to G(Y)$ 的构造都能够沿着 $\eta_X$ 唯一分解. 在偏序范畴中, 这种唯一分解表现为最小性; 在代数范畴中, 它通常表现为自由性.

## Adjunctions via initial objects

> [!definition] Comma category
> 给定范畴 $\A,\B,\mathscr{C}$ 以及函子
> $$
> P:\A\to\mathscr{C},
> \qquad
> Q:\B\to\mathscr{C}.
> $$
> 因为 $P$ 与 $Q$ 的值都在 $\mathscr{C}$ 中, 所以可以考虑从 $P(X)$ 到 $Q(Y)$ 的态射. **逗号范畴** $(P\Rightarrow Q)$, 也常记作 $(P\downarrow Q)$, 定义如下.
>
> 它的对象是三元组
> $$
> (X,h,Y),
> $$
> 其中
> $$
> X\in\A,
> \qquad
> Y\in\B,
> \qquad
> h:P(X)\to Q(Y).
> $$
> 因此, 逗号范畴中的一个对象可以看成 $\mathscr{C}$ 中的一条指定态射
> $$
> P(X)\xrightarrow{h}Q(Y).
> $$
>
> 从 $(X,h,Y)$ 到 $(X',h',Y')$ 的态射是一对态射
> $$
> f:X\to X',
> \qquad
> g:Y\to Y',
> $$
> 并且要求下面的方块交换:
>
> ```tikz size=medium
> \usepackage{tikz-cd}
> \begin{document}
> \begin{tikzcd}[row sep=large, column sep=large]
> P(X) \arrow[r,"P(f)"] \arrow[d,"h"']
> & P(X') \arrow[d,"h'"]\\
> Q(Y) \arrow[r,"Q(g)"']
> & Q(Y')
> \end{tikzcd}
> \end{document}
> ```
>
> 也就是说,
> $$
> \boxed{Q(g)\circ h=h'\circ P(f)}.
> $$
> 对象 $(X,h,Y)$ 上的恒等态射是 $(1_X,1_Y)$; 两个态射的复合逐项定义:
> $$
> (f',g')\circ(f,g)
> =
> (f'\circ f,g'\circ g).
> $$
> 由 $P,Q$ 的函子性以及两个方块的交换性, 复合后得到的方块仍然交换, 因而这些数据的确构成一个范畴.

这里的符号 $P\Rightarrow Q$ 只是逗号范畴的记号, 并不表示 $P$ 与 $Q$ 之间存在自然变换. 实际上, $P$ 与 $Q$ 的定义域可以不同. 这个定义所做的事情, 是把所有形如
$$
P(X)\to Q(Y)
$$
的态射收集为对象, 再把它们之间的交换方块作为态射.

**Remark 2.3.2.** 逗号范畴自带两个投影函子
$$
\pi_{\A}:(P\Rightarrow Q)\to\A,
\qquad
\pi_{\B}:(P\Rightarrow Q)\to\B.
$$
它们在对象上分别取出三元组的两端:
$$
\pi_{\A}(X,h,Y)=X,
\qquad
\pi_{\B}(X,h,Y)=Y,
$$
在态射上则分别取出一对态射的两个分量:
$$
\pi_{\A}(f,g)=f,
\qquad
\pi_{\B}(f,g)=g.
$$
将它们分别与 $P,Q$ 复合, 得到两个从 $(P\Rightarrow Q)$ 到 $\mathscr{C}$ 的函子
$$
P\pi_{\A},
\qquad
Q\pi_{\B}.
$$
每个对象 $(X,h,Y)$ 中的态射 $h:P(X)\to Q(Y)$ 自然地给出一个分量
$$
\alpha_{(X,h,Y)}:=h.
$$
于是这些分量组成自然变换
$$
\alpha:P\pi_{\A}\Longrightarrow Q\pi_{\B}.
$$
对于态射 $(f,g):(X,h,Y)\to(X',h',Y')$, $\alpha$ 的自然性要求
$$
Q(g)\circ h=h'\circ P(f),
$$
而这恰好就是逗号范畴定义中的交换条件. 因此 $\alpha$ 不需要另外选择, 它是由逗号范畴中的对象和态射自然导出的.

**Example 2.3.3.** 固定范畴 $\A$ 中的对象 $A$. **切片范畴** $\A/A$ 的对象是所有指向 $A$ 的态射
$$
h:X\to A.
$$
从 $(X,h)$ 到 $(X',h')$ 的态射是满足
$$
h'\circ f=h
$$
的态射 $f:X\to X'$. 以
$$
A^*:\mathbf{1}\to\A
$$
表示选出对象 $A$ 的函子, 就有
$$
\A/A\cong(1_{\A}\Rightarrow A^*).
$$

对偶地, **余切片范畴** $A/\A$ 的对象是所有从 $A$ 出发的态射 $A\to X$, 并且
$$
A/\A\cong(A^*\Rightarrow1_{\A}).
$$
因此, 切片范畴收集所有进入固定对象 $A$ 的方式, 而余切片范畴收集所有从 $A$ 出发的方式; 它们都是逗号范畴的特殊情形.

**Example 2.3.4.** 给定函子
$$
G:\B\to\A
$$
以及对象 $A\in\A$. 以
$$
A^*:\mathbf{1}\to\A
$$
表示选出对象 $A$ 的函子. 逗号范畴 $(A^*\Rightarrow G)$ 的对象可以简记为
$$
(B,f),
\qquad
f:A\to G(B),
$$
其中 $B\in\B$. 从 $(B,f)$ 到 $(B',f')$ 的态射是满足
$$
G(q)\circ f=f'
$$
的态射 $q:B\to B'$. 因此, $(A^*\Rightarrow G)$ 收集了所有将 $A$ 映入某个形如 $G(B)$ 的对象的方式, 而它的态射描述这些方式之间如何通过 $\B$ 中的态射相互联系.

严格来说, 逗号范畴的对象是二元组 $(B,f)$, 而不只是态射 $f:A\to G(B)$. 因为可能存在不同的对象 $B,B'\in\B$ 满足 $G(B)=G(B')$, 如果只记录 $f$, 就会丢失它所对应的 $\B$ 中的对象.

本节开头的自由向量空间例子正是这种构造的一个特例. 此时 $A=S$, $G=U:\mathbf{Vect}_k\to\mathbf{Set}$, 并以
$$
S^*:\mathbf{1}\to\mathbf{Set}
$$
表示选出集合 $S$ 的函子. 因此相应的逗号范畴是 $(S^*\Rightarrow U)$, 而自由向量空间的泛性质可以重新表述为: $(F(S),\eta_S)$ 是这个逗号范畴的始对象.

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

### 2.2.10

>[!exercise]
>设 $A,B$ 是偏序集, 并且
>$$
>f:A\to B,
>\qquad
>g:B\to A
>$$
>都是保序映射. 直接证明以下两个条件等价:
>
>1. 对于任意的 $a\in A$ 与 $b\in B$,
>   $$
>   f(a)\leq b\iff a\leq g(b);
>   $$
>2. 对于任意的 $a\in A$ 与 $b\in B$,
>   $$
>   a\leq g(f(a)),
>   \qquad
>   f(g(b))\leq b.
>   $$

>[!proof]
>先证明 $(1)\Rightarrow(2)$. 任取 $a\in A$, 在条件 $(1)$ 中令 $b=f(a)$, 可得
>$$
>a\leq g(f(a))\iff f(a)\leq f(a).
>$$
>右边由自反性自然成立, 所以
>$$
>a\leq g(f(a)).
>$$
>再任取 $b\in B$, 在条件 $(1)$ 中令 $a=g(b)$, 可得
>$$
>f(g(b))\leq b\iff g(b)\leq g(b).
>$$
>右边同样由自反性成立, 所以
>$$
>f(g(b))\leq b.
>$$
>因此条件 $(2)$ 成立.
>
>下面证明 $(2)\Rightarrow(1)$. 任取 $a\in A$ 与 $b\in B$. 先假定
>$$
>f(a)\leq b.
>$$
>因为 $g$ 是保序映射, 所以
>$$
>g(f(a))\leq g(b).
>$$
>再由条件 $(2)$ 中的 $a\leq g(f(a))$, 可得
>$$
>a\leq g(f(a))\leq g(b),
>$$
>从而 $a\leq g(b)$.
>
>反过来, 假定
>$$
>a\leq g(b).
>$$
>因为 $f$ 是保序映射, 所以
>$$
>f(a)\leq f(g(b)).
>$$
>再由条件 $(2)$ 中的 $f(g(b))\leq b$, 可得
>$$
>f(a)\leq f(g(b))\leq b,
>$$
>从而 $f(a)\leq b$. 因此
>$$
>f(a)\leq b\iff a\leq g(b),
>$$
>所以条件 $(1)$ 成立.

### 2.2.11

>[!exercise]
>设有一个伴随结构
>$$
>F:\A\rightleftarrows\B:G,
>\qquad
>F\dashv G,
>$$
>其 unit 与 counit 分别为 $\eta$ 与 $\epsilon$. 令 $\operatorname{Fix}(GF)$ 为 $\A$ 的满子范畴, 其对象是所有使
>$$
>\eta_X:X\to G(F(X))
>$$
>成为同构的 $X\in\A$. 对偶地, 令 $\operatorname{Fix}(FG)$ 为 $\B$ 的满子范畴, 其对象是所有使
>$$
>\epsilon_Y:F(G(Y))\to Y
>$$
>成为同构的 $Y\in\B$.
>
>1. 证明原来的伴随结构可以限制为 $\operatorname{Fix}(GF)$ 与 $\operatorname{Fix}(FG)$ 之间的范畴等价;
>2. 选取一些伴随的例子, 求出这样得到的范畴等价.

>[!proof]
>先证明原来的函子可以直接限制到这两个满子范畴上. 任取
>$$
>X\in\operatorname{Fix}(GF).
>$$
>我们需要证明
>$$
>F(X)\in\operatorname{Fix}(FG),
>$$
>也就是证明
>$$
>\epsilon_{F(X)}:F(G(F(X)))\to F(X)
>$$
>是同构.
>
>由 $X\in\operatorname{Fix}(GF)$ 可知, $\eta_X:X\to G(F(X))$ 是同构. 记它的逆态射为
>$$
>\theta_X:G(F(X))\to X.
>$$
>于是
>$$
>\theta_X\circ\eta_X=1_X,
>\qquad
>\eta_X\circ\theta_X=1_{G(F(X))}.
>$$
>由 counit 的定义以及伴随对应的自然性,
>$$
>\bl
>\epsilon_{F(X)}
>&=\left(1_{G(F(X))}\right)^{*_{G(F(X)),F(X)}}\\
>&=\left(\eta_X\circ\theta_X\right)^{*_{G(F(X)),F(X)}}\\
>&=\left(\eta_X\right)^{*_{X,F(X)}}\circ F(\theta_X)\\
>&=1_{F(X)}\circ F(\theta_X)\\
>&=F(\theta_X).
>\el
>$$
>因为 $\theta_X$ 是同构, 而函子保持同构, 所以 $F(\theta_X)$ 是同构. 因此 $\epsilon_{F(X)}$ 是同构, 从而
>$$
>F(X)\in\operatorname{Fix}(FG).
>$$
>
>反过来, 任取 $Y\in\operatorname{Fix}(FG)$. 此时 $\epsilon_Y$ 是同构, 所以 $G(\epsilon_Y)$ 也是同构. 由第二条三角等式
>$$
>G(\epsilon_Y)\circ\eta_{G(Y)}=1_{G(Y)}
>$$
>可得
>$$
>\eta_{G(Y)}=G(\epsilon_Y)^{-1}.
>$$
>因此 $\eta_{G(Y)}$ 是同构, 从而
>$$
>G(Y)\in\operatorname{Fix}(GF).
>$$
>
>所以 $F$ 与 $G$ 在对象上的限制确实落在相应的满子范畴中. 因为这两个子范畴都是满子范畴, 它们保留了所选对象之间的全部态射, 所以 $F$ 与 $G$ 在态射上的作用也可以直接限制. 由此得到函子
>$$
>F':\operatorname{Fix}(GF)\to\operatorname{Fix}(FG),
>\qquad
>G':\operatorname{Fix}(FG)\to\operatorname{Fix}(GF).
>$$
>
>将原来的 unit 与 counit 限制到这些对象上, 得到自然变换
>$$
>\eta':1_{\operatorname{Fix}(GF)}\to G'\circ F',
>\qquad
>\epsilon':F'\circ G'\to1_{\operatorname{Fix}(FG)}.
>$$
>它们的自然性直接来自 $\eta$ 与 $\epsilon$ 的自然性. 又因为 $\operatorname{Fix}(GF)$ 中的对象正是使 $\eta_X$ 成为同构的对象, 而 $\operatorname{Fix}(FG)$ 中的对象正是使 $\epsilon_Y$ 成为同构的对象, 所以 $\eta'$ 与 $\epsilon'$ 都是自然同构.
>
>因此
>$$
>\left(F',G',\eta',\epsilon'\right)
>$$
>给出了 $\operatorname{Fix}(GF)$ 与 $\operatorname{Fix}(FG)$ 之间的范畴等价.
>
>第二问要求从具体伴随中寻找相应的例子, 此处从略.

### 2.2.12(a)

>[!exercise]
>设有一个伴随结构
>$$
>F:\A\rightleftarrows\B:G,
>\qquad
>F\dashv G,
>$$
>其 counit 为
>$$
>\epsilon:F\circ G\to1_\B.
>$$
>证明右伴随 $G$ 是全忠实函子, 当且仅当 $\epsilon$ 是自然同构.

>[!proof]
>先证明右伴随 $G$ 全忠实可以推出 $\epsilon$ 是自然同构. 任取 $X\in\B$. 为了证明
>$$
>\epsilon_X:F(G(X))\to X
>$$
>是同构, 我们为它构造逆态射.
>
>第二条三角等式中出现了态射
>$$
>\eta_{G(X)}:G(X)\to G(F(G(X))).
>$$
>因为 $G$ 是全的, 所以存在态射
>$$
>\delta_X:X\to F(G(X))
>$$
>使得
>$$
>G(\delta_X)=\eta_{G(X)}.
>$$
>又因为 $G$ 是忠实的, 所以这样的 $\delta_X$ 是唯一的.
>
>先证明
>$$
>\delta_X\circ\epsilon_X=1_{F(G(X))}.
>$$
>对左边取伴随对应, 由 counit 的定义可得
>$$
>\bl
>\left(\delta_X\circ\epsilon_X\right)^{*_{G(X),F(G(X))}}
>&=G(\delta_X)\circ
>\left(\epsilon_X\right)^{*_{G(X),X}}\\
>&=G(\delta_X)\circ1_{G(X)}\\
>&=\eta_{G(X)}.
>\el
>$$
>另一方面, 由 unit 的定义,
>$$
>\left(1_{F(G(X))}\right)^{*_{G(X),F(G(X))}}
>=\eta_{G(X)}.
>$$
>因为伴随对应是一一对应, 所以
>$$
>\delta_X\circ\epsilon_X=1_{F(G(X))}.
>$$
>
>再证明
>$$
>\epsilon_X\circ\delta_X=1_X.
>$$
>对这个复合施加函子 $G$, 并使用第二条三角等式, 可得
>$$
>\bl
>G(\epsilon_X\circ\delta_X)
>&=G(\epsilon_X)\circ G(\delta_X)\\
>&=G(\epsilon_X)\circ\eta_{G(X)}\\
>&=1_{G(X)}\\
>&=G(1_X).
>\el
>$$
>因为 $G$ 是忠实的, 所以
>$$
>\epsilon_X\circ\delta_X=1_X.
>$$
>因此 $\delta_X$ 是 $\epsilon_X$ 的逆. 对于每个 $X\in\B$, $\epsilon_X$ 都是同构, 所以 $\epsilon$ 是自然同构.
>
>反过来, 假定 $\epsilon$ 是自然同构. 对于任意的对象 $X,Y\in\B$ 以及态射 $f:X\to Y$, 由 counit 的定义与伴随对应的自然性可得
>$$
>\bl
>\left(f\circ\epsilon_X\right)^{*_{G(X),Y}}
>&=G(f)\circ\left(\epsilon_X\right)^{*_{G(X),X}}\\
>&=G(f)\circ1_{G(X)}\\
>&=G(f).
>\el
>$$
>
>先证明忠实性. 假定 $f,f':X\to Y$ 满足
>$$
>G(f)=G(f').
>$$
>由上面的等式可得
>$$
>\left(f\circ\epsilon_X\right)^{*_{G(X),Y}}
>=\left(f'\circ\epsilon_X\right)^{*_{G(X),Y}}.
>$$
>因为伴随对应是一一对应, 所以
>$$
>f\circ\epsilon_X=f'\circ\epsilon_X.
>$$
>再在右边复合 $\epsilon_X^{-1}$, 可得
>$$
>f=f'.
>$$
>因此 $G$ 是忠实的.
>
>最后证明全性. 任取态射
>$$
>g:G(X)\to G(Y).
>$$
>它的伴随对应为
>$$
>g^{*_{G(X),Y}}:F(G(X))\to Y.
>$$
>定义
>$$
>f:=g^{*_{G(X),Y}}\circ\epsilon_X^{-1}:X\to Y.
>$$
>于是
>$$
>f\circ\epsilon_X=g^{*_{G(X),Y}}.
>$$
>因此
>$$
>\bl
>G(f)
>&=\left(f\circ\epsilon_X\right)^{*_{G(X),Y}}\\
>&=\left(g^{*_{G(X),Y}}\right)^{*_{G(X),Y}}\\
>&=g.
>\el
>$$
>所以每个态射 $g:G(X)\to G(Y)$ 都是某个态射 $f:X\to Y$ 在 $G$ 下的像, 从而 $G$ 是全的. 因此 $G$ 是全忠实函子.
>
>第二问关于 reflection 以及具体例子的讨论从略.

### 2.2.13

>[!exercise]
>给定集合映射
>$$
>f:K\to L.
>$$
>逆像给出关于包含关系保序的映射
>$$
>f^*:\mathcal P(L)\to\mathcal P(K),
>\qquad
>f^*(B)=f^{-1}(B).
>$$
>
>1. 求 $f^*$ 的左伴随和右伴随;
>2. 对第一投影
>   $$
>   p:X\times Y\to X
>   $$
>   应用第一问的结果, 并说明两个伴随的 unit 与 counit 所表达的逻辑含义.

关于这些构造与逻辑量词的关系, 以及 unit、counit 的逻辑含义, 见文末的 [Bonus 伴随作为一种量词](#bonus-伴随作为一种量词).

>[!proof]
>**(a)** 定义映射
>$$
>L_f:\mathcal P(K)\to\mathcal P(L)
>$$
>为直接像
>$$
>L_f(A):=f(A)=\{f(x):x\in A\}.
>$$
>它是保序的. 对于任意的 $A\subseteq K$ 与 $B\subseteq L$, 有
>$$
>L_f(A)\subseteq B
>\iff
>A\subseteq f^{-1}(B)
>=f^*(B).
>$$
>因此
>$$
>L_f\dashv f^*.
>$$
>
>接下来定义映射
>$$
>R_f:\mathcal P(K)\to\mathcal P(L)
>$$
>为
>$$
>R_f(A)
>:=\left\{
>y\in L:
>f^{-1}(\{y\})\subseteq A
>\right\}.
>$$
>也就是说, $y\in R_f(A)$ 当且仅当 $y$ 在 $f$ 下的整个纤维都包含在 $A$ 中. 如果 $y$ 不在 $f$ 的像中, 那么这个纤维是空集, 因而 $y$ 也属于 $R_f(A)$.
>
>如果 $A\subseteq A'$, 那么任何包含在 $A$ 中的纤维也包含在 $A'$ 中, 所以
>$$
>R_f(A)\subseteq R_f(A').
>$$
>因此 $R_f$ 也是保序的. 对于任意的 $A\subseteq K$ 与 $B\subseteq L$, 有
>$$
>f^{-1}(B)\subseteq A
>\iff
>B\subseteq R_f(A).
>$$
>因此
>$$
>f^*\dashv R_f.
>$$
>综上,
>$$
>\boxed{L_f\dashv f^*\dashv R_f}.
>$$
>
>**(b)** 第一投影
>$$
>p:X\times Y\to X,
>\qquad
>p(x,y)=x
>$$
>只是第一问中的一个特殊函数, 因此可以直接令
>$$
>K=X\times Y,\qquad L=X,\qquad f=p.
>$$
>对于 $S\subseteq X$, 逆像为
>$$
>p^*(S)=S\times Y.
>$$
>对于 $R\subseteq X\times Y$, 左伴随为
>$$
>L_p(R)=p(R)
>=\left\{
>x\in X:
>R\cap(\{x\}\times Y)\neq\varnothing
>\right\},
>$$
>也就是由所有满足“纤维 $\{x\}\times Y$ 与 $R$ 相交”的 $x$ 组成的子集.
>
>右伴随为
>$$
>R_p(R)
>=\left\{
>x\in X:
>\{x\}\times Y\subseteq R
>\right\},
>$$
>也就是由所有满足“整个纤维 $\{x\}\times Y$ 都包含在 $R$ 中”的 $x$ 组成的子集. 因此
>$$
>\boxed{L_p\dashv p^*\dashv R_p}.
>$$
>
>这两个伴随的 unit 与 counit 在集合语言中分别是下面四个包含关系:
>$$
>\bl
>R&\subseteq p^*(L_p(R)),\\
>L_p(p^*(S))&\subseteq S,\\
>S&\subseteq R_p(p^*(S)),\\
>p^*(R_p(R))&\subseteq R.
>\el
>$$
>前两个属于 $L_p\dashv p^*$, 后两个属于 $p^*\dashv R_p$. 它们的逻辑解释统一放在文末的 Bonus 中.

## Bonus 伴随作为一种量词

把一个子集 $A\subseteq K$ 看成谓词时,
$$
A(x)
\quad\Longleftrightarrow\quad
x\in A.
$$
子集包含
$$
A\subseteq A'
$$
则表示谓词之间的蕴含: $A(x)$ 成立时, $A'(x)$ 也成立. 因此, 幂集偏序 $\mathcal P(K)$ 可以看成论域 $K$ 上全部谓词组成的偏序.

给定函数
$$
f:K\to L,
$$
逆像
$$
f^*:\mathcal P(L)\to\mathcal P(K)
$$
将 $L$ 上的谓词 $B(y)$ 变成 $K$ 上的谓词
$$
f^*(B)(x)
\quad\Longleftrightarrow\quad
B(f(x)).
$$
因此, $f^*$ 可以理解为沿着 $f$ 进行代入. 元素沿 $f$ 从 $K$ 进入 $L$, 而谓词则沿相反方向从 $L$ 被拉回到 $K$.

第一问构造的左伴随 $L_f$ 可以记为 $\exists_f$. 对于 $A\subseteq K$ 与 $y\in L$,
$$
y\in L_f(A)
\quad\Longleftrightarrow\quad
\exists x\in K,\quad f(x)=y\ \land\ x\in A.
$$
所以 $L_f$ 在 $y$ 的纤维上进行存在量化: 只要纤维中至少有一个元素属于 $A$, 就将 $y$ 放入结果中.

右伴随 $R_f$ 可以记为 $\forall_f$. 对于 $A\subseteq K$ 与 $y\in L$,
$$
y\in R_f(A)
\quad\Longleftrightarrow\quad
\forall x\in K,\quad f(x)=y\Longrightarrow x\in A.
$$
所以 $R_f$ 在 $y$ 的纤维上进行全称量化: 只有纤维中的每个元素都属于 $A$, 才将 $y$ 放入结果中. 如果纤维为空, 这个条件自动成立, 这与全称命题的空真性一致.

因此
$$
\boxed{\exists_f\dashv f^*\dashv\forall_f}.
$$
这不是形式上的类比, 而是说存在量化与全称量化可以精确地表示为代入函子的左伴随与右伴随.

对于投影
$$
p:X\times Y\to X,
$$
一个子集 $R\subseteq X\times Y$ 可以看成二元谓词 $R(x,y)$. 此时
$$
\begin{aligned}
x\in L_p(R)
&\Longleftrightarrow
\exists y\in Y,\ R(x,y),\\
x\in R_p(R)
&\Longleftrightarrow
\forall y\in Y,\ R(x,y).
\end{aligned}
$$
所以通常将 $L_p$ 与 $R_p$ 分别写成
$$
\exists_Y,\qquad\forall_Y,
$$
并且有
$$
\boxed{\exists_Y\dashv p^*\dashv\forall_Y}.
$$
这里 $p^*$ 将一元谓词 $S(x)$ 变成不依赖 $y$ 的二元谓词
$$
p^*(S)(x,y)\Longleftrightarrow S(x),
$$
而它的两个伴随则分别通过存在量化和全称量化消去变量 $y$.

最后来看 unit 与 counit 的逻辑含义. 对于 $\exists_Y\dashv p^*$, unit
$$
R\subseteq p^*(\exists_YR)
$$
表示
$$
R(x,y)\Longrightarrow\exists y'\in Y,\ R(x,y').
$$
它说明, 如果 $R(x,y)$ 对某个已经给定的 $y$ 成立, 那么当然可以断言存在一个使 $R(x,y')$ 成立的 $y'$.

同一个伴随的 counit
$$
\exists_Y(p^*(S))\subseteq S
$$
表示
$$
\left(\exists y\in Y,\ S(x)\right)\Longrightarrow S(x).
$$
因为 $S(x)$ 与 $y$ 无关, 所以只要左边成立, 就可以直接得到 $S(x)$.

对于 $p^*\dashv\forall_Y$, unit
$$
S\subseteq\forall_Y(p^*(S))
$$
表示
$$
S(x)\Longrightarrow\forall y\in Y,\ S(x).
$$
因为 $S(x)$ 与 $y$ 无关, 所以它一旦成立, 就对每个 $y$ 都成立.

最后, counit
$$
p^*(\forall_YR)\subseteq R
$$
表示
$$
\left(\forall y'\in Y,\ R(x,y')\right)
\Longrightarrow
R(x,y).
$$
它说明, 如果 $R(x,y')$ 对每个 $y'$ 都成立, 那么它当然对当前给定的 $y$ 成立.
