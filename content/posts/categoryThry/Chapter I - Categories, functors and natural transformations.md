---
title: Chapter I - Categories, functors and natural transformations
date: 2026-08-25
math: true
draft:
tags:
  - category-theory
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
## Categories

>范畴论的语言不以集合论为基础, 所以以下的用词是朴素的, 用自然语言表达的. 同时, 我们也不应当去苛求一个建立在集合论基础下的范畴论.

>[!definition] 范畴/Category
>一个范畴 $\scr A$ 包含以下的元素,
>1. 一个元素的聚类(这里使用 collection 这个词汇, 刻意区别与集合论中的 set 或者是 class ), 称之为范畴 $\scr A$ 的对象, 记为 $\rm ob({\scr A})$ .
>2. 对于任意的 $A,A'\in {\rm ob({\scr A})}$ , 都有一组态射的聚类, 记之为 $\A(A,A')$ . 对于 $f\in \A(A,A')$ 我们时常用箭头 $A \map{f} A'$ 来表示之.
>3. 对于任意的 $A,B,C\in\A$ , 都有态射(morphism/map)的复合 $\circ$ 满足$$\begin{aligned}\A(B,C)\times\A(A,B)&\to\A(A,C)\\(g,f)&\mapsto g\circ f\end{aligned}$$并且这个复合满足结合律(我们可以用函数以及函数间的复合来类比地理解它).
>4. 对于每个 $A\in\A$ , 在 $\A(A,A)$ 中存在恒等态射 $1_A$ .

于是我们有非常多范畴的例子, 比如:

>[!example]
>1. $\bf Set$ is the category of set theory, whose object is the proper class consisting of all the sets. And the morphisms between sets are maps/functions.
>2. $\bf Grp$ is the category of groups, whose objects are groups and whose maps are group homomorphisms.
>3. $\bf Ring$ is the category of rings.
>4. ${\bf Vect}_k$ is the category of vector spaces over field $k$ , whose morphisms are linear maps.

之后我们可以仿照着这些我们熟悉的概念导出范畴论中的同构的概念:

>[!definition] Isomorphism
>A map $A\map f B$ in $\A$ is an isomorphism if there exists a map $B\map g A$ s.t. $g\circ f=1_A$ and $f\circ g=1_B$ . 简记为 $A\cong B$ .

当然, 我们会有一些对于范畴的有意思的描述, 比如:

>[!example]
>A group is essentially the same thing as a category that has only one object and whose collection of morphisms form a set in which all the maps are isomorphisms.

课本对于这一观点的一个解释是

>The first time one meets the idea that a group is a kind of category, it is
tempting to dismiss it as a coincidence or a trick. But it is not; there is real
content.
To see this, suppose that your education had been shuffled and that you
already knew about categories before being taught about groups. In your
first group theory class, the lecturer declares that a group is supposed to be
the system of all symmetries of an object. A symmetry of an object $X$, she
says, is a way of mapping $X$ to itself in a reversible or invertible manner.
At this point, you realize that she is talking about a very special type of category. In general, a category is a system consisting of all the mappings
(not usually just the invertible ones) between many objects (not usually
just one). So a group is just a category with the special properties that all
the maps are invertible and there is only one object.

当然最后我们介绍了两个附加的常见的概念:

>[!definition] Dual category
>对于范畴 $\A$ , 我们如下地定义它的对偶范畴 $\A\op$ ,
>1. $\ob(\A\op)=\ob(\A)$ .
>2. 对于任意的 $X\map f Y\in\A$ , 都有一个 $Y\map{f\op} X\in\A\op$ . 并且 $\A\op$ 的每个态射都是由某个 $\A$ 中的态射反转反向得到的.
>3. 我们还需要自然地导出 $\A\op$ 上的 $\circ\op$ . 具体地:$$\begin{aligned}((B\map{g\op}C),(A\map{f\op}B))\mapsto &(A\map{(f\circ g)\op}C)\\=&(A\map{g\op\circ\op f\op}C)\end{aligned}$$

>[!definition] Product category.
>对于范畴 $\A,\B$ , 定义它们的 Product 范畴 $\A\times\B$ 
>1. $\ob(\A\times\B)=\ob(\A)\times\ob(\B)$
>2. 对于 $A,A'\in\A$ 以及 $B,B'\in\B$ 有 $$(\A\times\B)((A,B),(A',B'))=\A(A,A')\times\B(B,B')$$
>3. 定义 $\A\times\B$ 中的复合 $\circ_{\A\times\B}$ 为$$((f,g),(f',g'))\mapsto(f\circ_\A f',g\circ_\B g')$$
## Functor

>One of the lessons of category theory is that whenever we meet a new type of mathematical object, we should always ask whether there is a sensible notion of ‘map’ between such objects. We can ask this about categories themselves. The answer is yes, and a map between categories is called a functor.
>函子是范畴间的"映射".

>[!definition] 函子/Functor
>对于范畴 $\A,\B$ , 一个函子 $F:\A\to\B$ 包含以下元素
>1. 一个对象层的映射:$$\begin{aligned}\ob(\A)&\to\ob(\B)\\A&\mapsto F(A)\end{aligned}$$
>2. 对于 $A,A'\in\A$ 有态射层的映射:$$\bl\A(A,A')&\to\B(F(A),F(A'))\\f&\mapsto F(f)\el$$这个态射层的映射应当保留恒等态射和复合结构, 即 $F(1_A)=1_{F(A)}$ 以及对于任意的 $A\map g B,B\map fC\in\A$ 有 $$F(f\circ_\A g)=F(f)\circ_\B F(g)$$ .

在代数学里常见的例子是遗忘函子和自由函子, 具体的例证需要用到基数算术的知识, 在此略过. 之后在用语上作如下的约定

>1. A **contravariant functor** from $\A$ to $\B$ is a functor $\A\op\to\B$ .
>2. An ordinary functor $\A\to\B$ is sometimes called a **covariant functor** from $\A$ to $\B$ .
>3. A **presheaf** is a functor $\A\op\to\bf Set$

之后来看一个例子

>[!example]
>固定域 $k$ , 考虑其上的向量空间构成的范畴 ${\bf Vect}_k$ , 对于向量空间 $V,W\in{\bf Vect}_k$ 从 $V$ 到 $W$ 的线性映射 ${\bf Hom}(V,W)$ 也是一个 $k$ 上的向量空间. 于是如果我们固定了 $W$ , 那么对于线性映射 $\overline g:V\to V'$ , 这很自然地导出了一个从 $\hom(V',W)$ 到 $\hom(V,W)$ 的线性映射 $$f\mapsto f\circ \overline g$$我们把这个映射记为 $(-\circ \overline g)$ , 唯一的不协调的地方是 $\overline g$ 的方向是反过来的, 所以一个协调的好办法就是把 $\vect_k$ 中的态射的方向都反向得到 $\vect_k\op$ 于是我们就自然地导出了一个函子$$\bl\hom(-,W):\vect_k\op&\to\vect_k\\V&\mapsto\hom(V,W)\\(V\map{f\op}V')&\mapsto(-\circ f)_{\hom(V,W)\to\hom(V',W)}\el$$

类似于集合论里映射的单射满射, 我们也可以定义函子的**忠实性/faithfulness**和**全性/fullness**.

>[!definition] Faithful
>函子 $F:\A\to\B$ 是忠实的, 当且仅当对于任意的 $A,A'\in\A$ , $F$ 态射层的映射 $\A(A,A')\to\B(F(A),F(A'))$ 是单射.

>[!definition] Full
>类似于忠实性, 不过将态射层映射的要求由单射改为满射.

最后我们定义范畴的子范畴

>[!definition] Subcategory.
>范畴 $\B$ 是范畴 $\A$ 的一个子范畴, 当且仅当:
>1. $\ob(\B)$ is the subclass of $\ob(\A)$ .
>2. For each $X,X'\in\B$ , $\B(X,X')$ is the subclass of $\A(X,X')$.
>3. 范畴 $\B$ 的态射应当在复合意义下封闭, 并且保留恒等态射.
## Natural transformations

> 自然变换是函子间的变换.

>[!definition] Natural transformation
>对于范畴 $\A,\B$ 以及函子 $F,G:\A\to\B$ , 一个自然变换 $\alpha:F\to G$ 是一族 $\B$ 中的态射 $(\alpha_X)_{X\in\A}$ 满足:
>1. 对于任意的 $X\in\A$ , 均有 $\alpha_X\in\B(F(X),G(X))$ .
>2. 对于任意的 $X\map f Y\in\A$ , 均有 $\alpha_{Y}\circ F(f)=G(f)\circ\alpha_X$ .

当然, 一般来讲我们会用交换图来表述这个过程:
```tikz size=medium
\usepackage{tikz-cd}
\begin{document}\begin{tikzcd}[row sep=large, column sep=large]
F(X) \arrow[r,"F(f)"]\arrow[d,"\alpha_X"] &F(Y)\arrow[d,"\alpha_Y"]\\
G(X) \arrow[r,"G(f)"]&G(Y)
\end{tikzcd}\end{document}
```
之后我们来看一个例子. 对于固定的正整数 $n$ 以及任意交换环 $R$ , 我们可以导出数域是 $R$ 的 $n\times n$ 的矩阵构成的一个集合 $M_n(R)$ , 并且可以在其上定义矩阵的乘法 $*_R$ , 于是结构$$(M_n(R),*_R)$$构成了一个幺半群, 并且任意的环同态 $R\to S$ 都导出了 $M_n(R)\to M_n(S)$ 上的同态, 故实际上 $M_n$ 是一个 $\bf CRing\to Mon$ 的函子, 而另外一方面考虑 $\bf CRing\to Mon$ 的遗忘函子 $U$ , 它忘记了 $R$ 上的加法结构, 只保留乘法结构, 对于 $X\in M_n(R)$ , 我们可以求出其行列式, 显然 $\det_R(X)\in U(R)$ 并且对于任意的 $X,Y\in M_n(R)$ 均有 $\det_R(XY)=\det_R(X)\det_R(Y)$ , 于是 $\det_R$ 是一个 $M_n(R)\to U(R)$ 的同态, 于是这就形成了一组 $\bf Mon$ 中的态射$$(\mathrm{det}_R:M_n(R)\to U(R))_{R\in\bf CRing}$$于是我们就会很自然地去询问$$\rm det_{(-)}$$ 构成一个 $M_n\to U$ 的自然变换吗? 事实上是构成的, 以下来进行验证.

>[!proof]
>对于任意的 $S,T\in\bf CRing$ 以及环同态 $\theta:S\to T$ , 我们需要检查交换图
>```tikz size=medium
>\usepackage{tikz-cd}
>\begin{document}\begin{tikzcd}
>M_n(S)\arrow[r,"M_n\theta"]\arrow[d,"\det_R"] & M_n(T)\arrow[d,"\det_T"]\\
>U(S)\arrow[r,"U\theta"]&U(T)
>\end{tikzcd}\end{document}
>```
>对于任意的 $X\in M_n(S)$ 假定 $X=(a_{i,j})_{n\times n}$ 则有 $$\mathrm{det}_S(X)=\sum_{\sigma}{\rm sgn}(\sigma)\prod_{0\le i<n}a_{i,\sigma_i}$$之后有 $$\bl U\theta({\rm det}_S(X))&=\theta(\sum_\sigma{\rm sgn}(\sigma)\prod a_{i,\sigma_i})\\&=\sum_\sigma{\rm sgn}(\sigma)\theta(\prod a_{i,\sigma_i})\el$$由于交换环同态保持加法乘法结构所以有$$\theta(\prod a_{i,\sigma_i})=\prod\theta(a_{i,\sigma_i})$$从而有$$U\theta({\det}_S(X))={\det}_T(M_n\theta(X))$$因而
>```tikz size=medium
>\usepackage{tikz-cd}
>\begin{document}
>\begin{tikzcd}
>\mathbf{CRing}
>\arrow[bend left=60, r, "M_n", ""' name=U]
>\arrow[bend right=60, r, "" name=D, "U"']
>&
>\arrow[Rightarrow, to path=(U) -- (D) \tikztonodes,
>  "\mathrm{det}"]
>\mathbf{Mon}
>\end{tikzcd}
>\end{document}
>```
>是自然变换.

由于自然变换是一族态射, 并且是函子间的变换, 所以我们自然地会想到自然变换的连接, 以下是纵列方向的连接:

>[!definition] Vertical composition
>对于范畴 $\A,\B$ 以及它们间的函子 $F,G,H$ , 假定有自然变换 $\alpha:F\to G$ 以及 $\beta:G\to H$ , 于是可以自然导出如下的一族态射:$$(\beta\circ\alpha)_X=\beta_X\circ\alpha_X$$容易验证 $\beta\circ\alpha$ 是 $F\to H$ 的自然变换, 这定义了自然变换的纵向复合.

而类似于恒等映射的概念, 我们可以导出某个函子 $F$ 的恒等自然变换 $$\id_F:(\id_F)_X=1_{F(X)}$$ 于是我们可以在函子间建立等价关系.

>[!definition] Natural isomorphic
>对于函子 $F,G:\A\to\B$ , 称 $F,G$ 是自然同构的当且仅当存在自然变换 $\eta:F\to G$ 以及 $\epsilon:G\to F$ 使得 $\eta\circ\epsilon=\id_G, \epsilon\circ\eta=\id_F$ , 这种情况下简记为 $F\cong G$ .

于是这就导出了函子空间的概念, 对于任意范畴 $\A,\B$ , 令范畴 $[\A,\B]$ 的对象为全体 $\A\to\B$ 的函子, 而对于函子 $F,G:\A\to\B$ , 他们之间的态射就是全体 $F\to G$ 的自然变换.

之后我们有一个对于自然变换是否是同构的等价的描述:

>[!lemma]
>对于函子 $F,G:\A\to\B$ , 自然变换 $\alpha:F\to G$ 是自然同构当且仅当对于任意 $A\in\A$ 都满足 $\B$ 中的态射 $\alpha_A:F(A)\to G(A)$ 是一个 isomorphism.

之后我们再导出范畴等价的概念

>[!definition] **Equivalence** between categories
>An **equivalence** between categories $\A$ and $\B$ consists of a pair of functors $F:\A\to\B$ and $G:\B\to\A$ together with natural isomorphisms$$\eta:1_\A\to G\circ F, \epsilon:F\circ G\to 1_\B.$$If there exists an equivalence between $\A$ and $\B$ , we say that $\A$ and $\B$ are **equivalent**, and write $\A\simeq\B$ . We also say that the functors $F$ and $G$ are **equivalences**.

之后我们再给出一个对**范畴等价性**的等价描述. 首先补充如下的定义:

>[!definition] Essentially surjective
>函子 $F:\A\to\B$ 是**本质满的/essentially surjective** , 当且仅当对于任意的 $B\in\B$ , 均存在 $A\in\A$ 使得 $F(A)\cong B$ .

>[!theorem] Characterization of equivalences
>函子 $F:\A\to\B$ 是一个等价函子, 当且仅当它是**全的/full**、**忠实的/faithful**以及在对象上**本质满的/essentially surjective on objects**.

>[!proof]
>先证明充分性. 假定函子 $F:\A\to\B$ 是 full, faithful 以及 essentially surjective 的, 我们需要构造函子 $G:\B\to\A$ 以及相应的两个自然同构.
>
>在构造 $G$ 之前, 我们先说明一个事实: 如果 $F(A)\cong F(A')$ , 那么 $A\cong A'$ . 事实上, 设 $\theta:F(A)\to F(A')$ 是同构. 因为 $F$ 是 full 的, 所以存在 $f:A\to A'$ 以及 $g:A'\to A$ 使得
>$$F(f)=\theta,\qquad F(g)=\theta^{-1}.$$
>于是 $F(g\circ f)=1_{F(A)}$ 且 $F(f\circ g)=1_{F(A')}$ . 又因为 $F$ 是 faithful 的, 所以
>$$g\circ f=1_A,\qquad f\circ g=1_{A'},$$
>从而 $A\cong A'$ . 再结合 essentially surjective 可知, $\A$ 与 $\B$ 的对象同构类是一一对应的.
>
>现在来构造 $G$ . 对于 $\B$ 中的每个对象同构类 $C$ , 选取一个对象 $A_C\in\A$ 使得 $F(A_C)\in C$ , 并将 $F(A_C)$ 简记为 $B_C$ . 对于每个 $X\in C$ , 再选取一个同构
>$$\phi_X:B_C\to X.$$
>这里的选取使用了选择公理. 我们规定
>$$G(X)=A_C.$$
>这就定义了 $G$ 在对象上的作用.
>
>接下来定义 $G$ 在态射上的作用. 对于任意的态射 $f:X\to Y$ , 设 $X\in C,Y\in D$ . 利用刚才选取的 $\phi_X,\phi_Y$ , 可以得到态射
>$$\phi_Y^{-1}\circ f\circ\phi_X:B_C\to B_D,$$
>也就是一个从 $F(A_C)$ 到 $F(A_D)$ 的态射. 因为 $F$ 是 full 的, 所以存在 $h:A_C\to A_D$ 使得
>$$F(h)=\phi_Y^{-1}\circ f\circ\phi_X.$$
>又因为 $F$ 是 faithful 的, 所以这样的 $h$ 是唯一的. 我们便定义 $G(f)=h$ , 即
>$$F(G(f))=\phi_Y^{-1}\circ f\circ\phi_X.$$
>
>还需要简单验证以上定义确实给出了一个函子. 对恒等态射有
>$$F(G(1_X))=\phi_X^{-1}\circ1_X\circ\phi_X=1_{F(G(X))},$$
>所以由 faithfulness 可知 $G(1_X)=1_{G(X)}$ . 对于可复合的态射 $X\map fY\map gZ$ , 将 $G(f),G(g)$ 的定义代入即可得到
>$$F(G(g)\circ G(f))=\phi_Z^{-1}\circ g\circ f\circ\phi_X=F(G(g\circ f)).$$
>再次由 faithfulness 可知 $G(g\circ f)=G(g)\circ G(f)$ . 因此 $G:\B\to\A$ 是一个函子.
>
>之后我们来构造 $\epsilon:FG\to1_\B$ . 对于任意的 $X\in\B$ , 定义
>$$\epsilon_X=\phi_X:F(G(X))\to X.$$
>而 $G(f)$ 的定义正好给出了
>$$\epsilon_Y\circ F(G(f))=f\circ\epsilon_X,$$
>所以自然性方块交换. 又因为每个 $\phi_X$ 都是同构, 所以 $\epsilon$ 是自然同构.
>
>最后构造 $\eta:1_\A\to GF$ . 对于任意的 $A\in\A$ , 已经有同构
>$$\phi_{F(A)}^{-1}:F(A)\to F(GF(A)).$$
>因为 $F$ 是 full 的, 所以存在 $\eta_A:A\to GF(A)$ 使得
>$$F(\eta_A)=\phi_{F(A)}^{-1}.$$
>同理, 存在 $\xi_A:GF(A)\to A$ 使得 $F(\xi_A)=\phi_{F(A)}$ . 于是
>$$F(\xi_A\circ\eta_A)=1_{F(A)},\qquad F(\eta_A\circ\xi_A)=1_{F(GF(A))}.$$
>因为 $F$ 是 faithful 的, 所以 $\xi_A$ 与 $\eta_A$ 互为逆, 从而 $\eta_A$ 是同构.
>
>对于态射 $f:A\to A'$ , 我们还需要验证
>$$GF(f)\circ\eta_A=\eta_{A'}\circ f.$$
>将两边作用 $F$ , 再分别使用 $G$ 与 $\eta$ 的定义, 可以得到
>$$\bl F(GF(f)\circ\eta_A)
>&=\phi_{F(A')}^{-1}\circ F(f),\\
>F(\eta_{A'}\circ f)
>&=\phi_{F(A')}^{-1}\circ F(f).\el$$
>因为 $F$ 是 faithful 的, 所以上面的自然性等式成立. 因此 $\eta$ 也是自然同构, 我们便构造出了范畴等价所需要的全部数据.
>
>再证明必要性. 假定 $F$ 是等价函子, 那么存在函子 $G:\B\to\A$ 以及自然同构
>$$\eta:1_\A\to GF,\qquad\epsilon:FG\to1_\B.$$
>对于 $f,f':A\to A'$ , 若 $F(f)=F(f')$ , 则 $GF(f)=GF(f')$ . 由 $\eta$ 的自然性,
>$$f=\eta_{A'}^{-1}\circ GF(f)\circ\eta_A
>=\eta_{A'}^{-1}\circ GF(f')\circ\eta_A=f',$$
>所以 $F$ 是 faithful 的. 使用 $\epsilon$ 进行同样的论证还可以得到 $G$ 是 faithful 的.
>
>对于任意的 $f:F(A)\to F(A')$ , 定义
>$$f^*=\eta_{A'}^{-1}\circ G(f)\circ\eta_A:A\to A'.$$
>由 $\eta$ 对 $f^*$ 的自然性,
>$$GF(f^*)\circ\eta_A=\eta_{A'}\circ f^*=G(f)\circ\eta_A,$$
>所以 $G(F(f^*))=G(f)$ . 因为 $G$ 是 faithful 的, 所以 $F(f^*)=f$ , 从而 $F$ 是 full 的.
>
>最后, 对于任意的 $B\in\B$ , $\epsilon$ 的分量
>$$\epsilon_B:F(G(B))\to B$$
>是同构. 取 $A=G(B)$ , 就有 $F(A)\cong B$ , 所以 $F$ 在对象上 essentially surjective.

*关于上述构造中所使用的选择, 以及它在大范畴中引出的基础问题, 见文末的 [关于选择公理与大范畴](#关于选择公理与大范畴).*

## Vertical and horizontal compositions

自然变换有两种复合方式. Vertical composition 复合的是同一对范畴之间首尾相接的自然变换; horizontal composition 则把两对相邻范畴之间的自然变换连接起来. 我们先回顾较为直接的 vertical composition.

最后我们来补充一点有关于 Horizontal composition 的知识, 现在考虑三个位于同一条链上的范畴, 以及函子和自然变换
$$
F,G:\A\to\B,\qquad F',G':\B\to\mathscr C,
$$
$$
\alpha:F\to G,\qquad\alpha':F'\to G'.
$$
我们想要由它们构造一个从 $F'F$ 到 $G'G$ 的自然变换. 对于任意的 $X\in\A$, 从 $F'F(X)$ 到 $G'G(X)$ 有两种自然的走法:
$$
F'F(X)\xrightarrow{F'(\alpha_X)}F'G(X)
\xrightarrow{\alpha'_{G(X)}}G'G(X),
$$
以及
$$
F'F(X)\xrightarrow{\alpha'_{F(X)}}G'F(X)
\xrightarrow{G'(\alpha_X)}G'G(X).
$$
乍看之下, 这两条路径似乎会给出两种不同的定义. 但是将 $\alpha'$ 的自然性用于 $\B$ 中的态射
$$\alpha_X:F(X)\to G(X),$$
就可以得到
$$
\alpha'_{G(X)}\circ F'(\alpha_X)
=G'(\alpha_X)\circ\alpha'_{F(X)}.
$$
所以这两种写法对于每个 $X$ 都严格相等, 而不只是彼此同构. 因此我们可以无歧义地定义
$$
(\alpha'*\alpha)_X
:=\alpha'_{G(X)}\circ F'(\alpha_X)
=G'(\alpha_X)\circ\alpha'_{F(X)}.
$$
由这些分量组成的自然变换
$$
\alpha'*\alpha:F'F\to G'G
$$
称为 $\alpha'$ 与 $\alpha$ 的 **horizontal composition**.

最后简略验证它的自然性. 对于任意的 $f:X\to Y$, 依次使用 $\alpha'$ 与 $\alpha$ 的自然性可得
$$
\bl
G'G(f)\circ(\alpha'*\alpha)_X
&=\alpha'_{G(Y)}\circ F'G(f)\circ F'(\alpha_X)\\
&=\alpha'_{G(Y)}\circ F'(\alpha_Y)\circ F'F(f)\\
&=(\alpha'*\alpha)_Y\circ F'F(f).
\el
$$
从而 $\alpha'*\alpha$ 的确是一个自然变换, horizontal composition 也就定义完成了.

## Exercise

### 1.1.13
设态射 $A\map fB,B\map{g,g'} A$ 满足 $fg=fg'=1_B,gf=g'f=1_A$ 那么显然有$$\begin{aligned}g&=g\circ1_B\\&=g(fg')\\&=(gf)g'\\&=1_A\circ g'=g'\end{aligned}$$因此态射的逆必定是唯一的.

### 1.2.21
对于函子 $F:\A\to\B$ 设 $X,Y\in\A$ 满足存在 $f\in\A(X,Y)$ 使得 $f:X\cong Y$ . 则存在 $Y\map g X$ 使得 $gf=1_X,fg=1_Y$ . 由于函子保持恒等映射和态射复合, 所以有 $F(gf)=F(g)F(f)=F(1_X)=1_{F(X)}$ , 另一方向同理. 因而 $F(f):F(X)\cong F(Y)$ .

### 1.2.24

题目询问是否存在函子 $Z:\mathbf{Grp}\to\mathbf{Grp}$, 使得对于任意群 $G$, $Z(G)$ 都是 $G$ 的中心
$$
Z(G)=\{z\in G\mid zg=gz\text{ 对任意 }g\in G\}.
$$

>[!note] 解法来源
>以下解法及所使用的反例由 OpenAI 给出.

>[!proof]
>这样的函子不存在. 为了说明这一点, 考虑二阶循环群 $C_2$ 与三阶对称群 $S_3$. $S_3$ 是集合 $\{1,2,3\}$ 上所有置换组成的群, 共有六个元素
>$$
>S_3=\{e,(12),(13),(23),(123),(132)\}.
>$$
>$C_2$ 是阿贝尔群, 所以 $Z(C_2)=C_2$. 另一方面, $S_3$ 中的每个非恒等置换都不能与所有置换交换, 所以
>$$Z(S_3)=\{e\}.$$
>
>定义同态 $i:C_2\to S_3$, 将 $C_2$ 的非恒等元素映射到换位 $(12)$; 再考虑符号同态
>$$\operatorname{sgn}:S_3\to C_2.$$
>换位 $(12)$ 的符号是非恒等元素, 因而
>$$\operatorname{sgn}\circ i=1_{C_2}.$$
>如果题目中的函子 $Z$ 存在, 那么 functoriality 给出
>$$
>Z(\operatorname{sgn})\circ Z(i)
>=Z(\operatorname{sgn}\circ i)
>=1_{Z(C_2)}.
>$$
>但是 $Z(i)$ 与 $Z(\operatorname{sgn})$ 分别是
>$$
>C_2=Z(C_2)\xrightarrow{Z(i)}Z(S_3)=\{e\}
>\xrightarrow{Z(\operatorname{sgn})}Z(C_2)=C_2.
>$$
>它们的复合经过平凡群 $\{e\}$, 因而只能是 $C_2$ 上的平凡同态, 不可能等于 $1_{C_2}$. 这与上式矛盾, 所以这样的函子 $Z$ 不存在.

这个反例的关键不只是“一般的群同态未必把中心映入中心”. 题目并没有要求 $Z(f)$ 必须是 $f$ 在中心上的限制, 所以这一点本身还不足以排除其他定义. 上面的做法利用了函子必须保持复合与恒等态射, 因而排除了所有可能的态射层定义.

### 1.3.31

令 $\B$ 为有限集合与集合间双射组成的范畴. 对于有限集合 $X$, 以 $\operatorname{Sym}(X)$ 表示 $X$ 上所有置换组成的集合, 以 $\operatorname{Ord}(X)$ 表示 $X$ 上所有全序组成的集合.

**(a)** 对于 $\B$ 中的双射 $f:X\to Y$, 定义
$$
\operatorname{Sym}(f):\operatorname{Sym}(X)\to\operatorname{Sym}(Y),
\qquad p\longmapsto f\circ p\circ f^{-1}.
$$
也就是说, 我们用 $f$ 将 $X$ 上的置换搬到 $Y$ 上.

另一方面, 设 $p\in\operatorname{Ord}(X)$, 并将这个全序记为 $\leq_p$. 在 $Y$ 上定义全序 $\leq_{\operatorname{Ord}(f)(p)}$:
$$
y\leq_{\operatorname{Ord}(f)(p)}y'
\quad\Longleftrightarrow\quad
f^{-1}(y)\leq_p f^{-1}(y').
$$
这就定义了函数
$$
\operatorname{Ord}(f):\operatorname{Ord}(X)\to\operatorname{Ord}(Y).
$$
这两个定义都没有使用任意的选择. 对于恒等映射, 它们显然给出恒等映射; 对于双射 $X\xrightarrow{f}Y\xrightarrow{g}Z$, 由
$$
(g\circ f)^{-1}=f^{-1}\circ g^{-1}
$$
可以直接得到
$$
\operatorname{Sym}(g\circ f)=\operatorname{Sym}(g)\circ\operatorname{Sym}(f),
$$
$$
\operatorname{Ord}(g\circ f)=\operatorname{Ord}(g)\circ\operatorname{Ord}(f).
$$
所以这两个构造分别给出了函子
$$
\operatorname{Sym},\operatorname{Ord}:\B\to\mathbf{Set}.
$$

**(b)** 假定存在自然变换
$$
\eta:\operatorname{Sym}\to\operatorname{Ord}.
$$
那么对于任意双射 $f:X\to Y$ 以及任意 $p\in\operatorname{Sym}(X)$, 自然性要求
$$
\eta_Y\bigl(\operatorname{Sym}(f)(p)\bigr)
=\operatorname{Ord}(f)\bigl(\eta_X(p)\bigr).
$$
取 $p=1_X$. 因为
$$
\operatorname{Sym}(f)(1_X)=f\circ1_X\circ f^{-1}=1_Y,
$$
所以等式左边始终是固定的全序 $\eta_Y(1_Y)$. 但是右边是将全序 $\eta_X(1_X)$ 通过 $f$ 搬到 $Y$ 上, 它会随着 $f$ 的不同而改变.

具体地, 取 $X=Y=\{0,1\}$, 并令 $\tau:X\to X$ 交换 $0$ 与 $1$. 若 $\eta_X(1_X)$ 中 $0<1$, 那么经过 $\operatorname{Ord}(\tau)$ 后得到的全序中 $1<0$; 反方向同理. 因此
$$
\operatorname{Ord}(\tau)\bigl(\eta_X(1_X)\bigr)\neq \eta_X(1_X).
$$
然而 $\operatorname{Sym}(\tau)(1_X)=1_X$, 所以自然性又要求上式两边相等, 产生矛盾. 因此不存在自然变换 $\operatorname{Sym}\to\operatorname{Ord}$.

**(c)** 如果 $X$ 有 $n$ 个元素, 那么
$$
|\operatorname{Sym}(X)|=n!,
$$
因为 $X$ 上的置换就是对这 $n$ 个元素进行排列. 同时
$$
|\operatorname{Ord}(X)|=n!,
$$
因为每个全序都唯一对应于一种排列
$$x_1<x_2<\cdots<x_n.$$
所以对于每个有限集合 $X$, 都存在集合间的同构
$$
\operatorname{Sym}(X)\cong\operatorname{Ord}(X).
$$
但是由 (b) 可知, 这些同构不能组成自然同构. 也就是说, 对每个 $X$ 分别存在同构, 并不代表这些同构能够自然地统一选取.


## 关于选择公理与大范畴

在上面的证明中, 我们多次说“选择一个对象”或者“选择一个同构”. 如果范畴的对象不能组成集合, 那么这些选择是否仍然安全? 这个问题确实存在. 不过真正需要注意的并不是“选择的次数太多”, 而是我们是否需要同时作出一整族选择, 以及这族选择是由集合还是由真类来编号的.

### 选择发生在哪里

回到 full、faithful 且 essentially surjective 的函子 $F:\A\to\B$. 对于每个 $B\in\B$ , 本质满性告诉我们: 存在某个 $A\in\A$ 以及同构
$$\epsilon_B:F(A)\xrightarrow{\sim}B.$$
但是这句话只分别保证了每个 $B$ 都有这样的 $A$. 为了定义拟逆函子 $G$, 我们还要对所有 $B$ 同时指定一个这样的对象, 并令
$$G(B)=A.$$
因此证明真正需要的是一族选择
$$B\longmapsto\bigl(G(B),\epsilon_B:F(G(B))\xrightarrow{\sim}B\bigr).$$

一旦这族数据已经选好, 态射上的定义就不再需要选择. 对于任意的 $f:B\to B'$, 因为 $F$ 是 full 且 faithful, 所以恰好存在一个态射 $G(f):G(B)\to G(B')$ 满足
$$F(G(f))=\epsilon_{B'}^{-1}\circ f\circ\epsilon_B.$$
这里 full 保证它存在, faithful 保证它唯一. 恒等态射与复合的验证也都由唯一性直接得到. 因此, 整个构造中真正需要选择的是对象以及相应的同构, 而不是态射.

正文中“先选取每个同构类的代表元”的说法很适合帮助理解: $G$ 要把彼此同构的对象送到预先选好的代表元. 不过对于大范畴, “所有同构类组成的商”本身可能有大小问题. 所以在正式处理大范畴时, 直接对每个 $B$ 选择 $G(B)$ 和 $\epsilon_B$ 会更稳妥.

### 选择公理确实参与了这个定理

如果 $\A$ 和 $\B$ 都是小范畴, 那么上述候选对象与同构可以组成一族非空集合, 普通的选择公理便允许我们同时选出 $G(B)$ 和 $\epsilon_B$. 这里的选择并不只是某种证明技巧: 对所有小范畴都断言
$$\text{full}+\text{faithful}+\text{essentially surjective}\Longrightarrow\text{equivalence}$$
实际上已经足以推出选择公理.

为了看出这一点, 设 $(X_i)_{i\in I}$ 是一族非空集合. 构造范畴 $\A$, 其对象是所有的 $(i,x)$, 其中 $x\in X_i$; 两个对象之间恰好有一个态射, 当且仅当它们的第一个分量相同. 再令 $\B$ 为以 $I$ 为对象的离散范畴, 并定义
$$F:\A\to\B,\qquad F(i,x)=i.$$
$F$ 是 full、faithful 且 essentially surjective. 如果它一定存在拟逆 $G$, 那么 $G(i)$ 必须具有形式 $(i,x_i)$, 从而 $i\mapsto x_i$ 就是这一族集合的选择函数. 所以, 如果不使用任何形式的选择公理, 这个定理的反方向一般不能成立.

因此, 这里的问题并不是选择公理处于一种无法讨论的模糊状态. 它与 ZF 的关系可以被精确地研究; 对当前证明来说, 关键只是明确我们采用了哪一种选择原则, 以及它是否足以完成这里的选择.

需要区分的是, 从“$F$ 是 equivalence”推出它 full、faithful 且 essentially surjective 的方向并不需要重新作出这些选择, 因为拟逆 $G$ 和两个自然同构已经作为条件的一部分给出了. 需要选择的是反方向, 即从三个性质构造 $G$ 的过程.

### 当范畴是大范畴时

如果 $\operatorname{Ob}(\B)$ 是真类, 那么我们需要的就是一族由真类编号的选择. ZFC 中的选择公理只谈集合族, 因而不能直接保证这种选择存在. 仅仅要求范畴 locally small 也不能解决这个问题: locally small 只保证任意两个对象之间的态射组成集合, 并不保证所有对象组成集合.

这正是为什么 $\mathbf{Set}$、$\mathbf{Vect}_k$、$\mathbf{Grp}$、$\mathbf{Ring}$ 和 $\mathbf{CRing}$ 等范畴通常被视为大范畴. 它们虽然 locally small, 但对象并不能在通常的集合论层级中组成集合; 它们一般也不能通过取一个小骨架而变成小范畴. 因此, 把所有范畴都规定成小范畴虽然能避开当前问题, 却会排除许多最常用的例子.

常见的处理方式有以下几种:

1. **只在小范畴之间使用这个定理.** 此时普通的选择公理已经足够. 这是最简单的做法, 但使用范围有限.

2. **使用 Grothendieck universe.** 先固定一个宇宙 $\mathcal U$, 把其中的集合叫作小集合; 再在一个更大的宇宙 $\mathcal V$ 中讨论它们. 这样 $\mathbf{Set}_{\mathcal U}$ 相对于 $\mathcal U$ 是大范畴, 但它的全部对象相对于 $\mathcal V$ 又构成集合, 因而可以在更高一层使用选择公理. 这种方法不会消灭大小问题, 而是把所需的选择放到更高的集合论层级中. 还要注意, “存在足够多的 Grothendieck universe”通常作为额外的集合论约定使用, 不能直接由 ZFC 证明.

3. **使用带有全局选择原则的类理论.** 例如在 NBG 或 GBC 一类理论中把集合和真类都作为讨论对象, 再加入足够的 Global Choice 原则, 便可以为这里出现的类族统一指定代表元. 这使我们能够直接处理大范畴, 但必须明确说明所采用的基础体系.

还有一种不依赖选择公理的说法: 把 essentially surjective 加强为 **split essentially surjective**. 这不只要求每个 $B$ 存在某个原像, 而是把选好的 $G(B)$ 与同构 $\epsilon_B:F(G(B))\cong B$ 直接作为条件的一部分. 此时可以由这些数据构造 $G$, 不必再调用选择公理. 换句话说, 我们没有消除选择的数据, 而是把它从证明中的隐含步骤改成了定理的显式条件.

>[!remark] 本文采用的理解
>在本文中, “full、faithful 且 essentially surjective 的函子是等价”应理解为已经采用了足够的选择原则. 对小范畴, 普通选择公理即可; 对大范畴, 可以使用 Grothendieck universe 的层级约定, 或在类理论中采用相应的全局选择原则. 如果希望完全不依赖选择公理, 就应当把 essentially surjective 改成 split essentially surjective, 并明确给出所选择的对象与同构.

关于这些集合论约定, 可以进一步参考 [Mike Shulman, *Set theory for category theory*](https://arxiv.org/abs/0810.1279) 以及 [Zhen Lin Low, *Universes for category theory*](https://arxiv.org/abs/1304.5227). [Stacks Project 对这一结论的表述](https://stacks.math.columbia.edu/tag/02C3) 则明确把范畴限制为小范畴.
