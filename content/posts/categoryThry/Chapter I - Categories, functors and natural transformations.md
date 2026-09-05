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
$$
## Categories

>范畴论的语言不以集合论为基础, 所以以下的用词是朴素的, 用自然语言表达的. 同时, 我们也不应当去苛求一个建立在集合论基础下的范畴论.

>[!definition] 范畴/Category
>一个范畴 $\scr A$ 包含以下的元素,
>1. 一个元素的聚类(这里使用 collection 这个词汇, 刻意区别与集合论中的 set 或者是 class ), 称之为范畴 $\scr A$ 的对象, 记为 $\rm ob({\scr A})$ .
>2. 对于任意的 $A,A'\in {\rm ob({\scr A})}$ , 都有一组态射的聚类, 记之为 $\A(A,A')$ . 对于 $f\in \A(A,A')$ 我们时常用箭头 $A \map{f} A'$ 来表示之.
>3. 对于任意的 $A,B,C\in\A$ , 都有态射(morphism/map)的复合 $\circ$ 满足$$\begin{aligned}\A(B,C)\times\A(A,B)&\to\A(A,C)\\(g,f)&\mapsto g\circ f\end{aligned}$$并且这个复合满足结合律(我们可以用函数以及函数间的复合来类比地理解它).
>4. 对于每个 $A\in\A$ , 在 $\A(A,A)$ 中存在恒等态射 $1_A$ .

于是我们由非常多范畴的例子, 比如:

>[!example]
>1. $\bf Set$ is the category of set theory, whose object is the proper class consisting of all the sets. And the morphisms between sets are maps/functions.
>2. $\bf Grp$ is the category of groups, whose objects are groups and whose maps are group homomorphisms.
>3. $\bf Ring$ is the category of rings.
>4. ${\bf Vect}_k$ is the category of vector spaces over field $k$ , whose morphisms are linear maps.

之后我们可以仿照着这些我们熟悉的概念导出范畴论中的同构的概念:

>[!definition] Isomorphism
>A map $A\map f B$ in $\A$ is an isomorphism if there exists a map $B\map g A$ s.t. $g\circ f=1_A$ and $f\circ g=1_B$ . 

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
```tikz
\usepackage{tikz-cd}
\begin{document}\begin{tikzcd}[row sep=large, column sep=large]
F(X) \arrow[r,"F(f)"]\arrow[d,"\alpha_X"] &F(Y)\arrow[d,"\alpha_Y"]\\
G(X) \arrow[r,"G(f)"]&G(Y)
\end{tikzcd}\end{document}
```
由于自然变换是一族态射, 并且是函子间的变换, 所以我们自然地会想到自然变换的连接, 以下是纵列方向的连接:

>[!definition] Vertical composition
>对于范畴 $\A,\B$ 以及它们间的函子 $F,G,H$ , 假定有自然变换 $\alpha:F\to G$ 以及 $\beta:G\to H$ , 于是可以自然导出如下的一族态射:$$(\beta\circ\alpha)_X=\beta_X\circ\alpha_X$$容易验证 $\beta\circ\alpha$ 是 $F\to H$ 的自然变换, 这定义了自然变换的纵向复合.

而类似于恒等映射的概念, 我们可以导出某个函子 $F$ 的恒等自然变换 $$\id_F:(\id_F)_X=1_{F(X)}$$ 于是我们可以在函子间建立等价关系.

>[!definition] Natural isomorphic
>对于函子 $F,G:\A\to\B$ , 称 $F,G$ 是自然同构的当且仅当存在自然变换 $\eta:F\to G$ 以及 $\epsilon:G\to F$ 
## Exercise

### 1.1.13
设态射 $A\map fB,B\map{g,g'} A$ 满足 $fg=fg'=1_B,gf=g'f=1_A$ 那么显然有$$\begin{aligned}g&=g\circ1_B\\&=g(fg')\\&=(gf)g'\\&=1_A\circ g'=g'\end{aligned}$$因此态射的逆必定是唯一的.

### 1.2.21
对于函子 $F:\A\to\B$ 设 $X,Y\in\A$ 满足存在 $f\in\A(X,Y)$ 使得 $f:X\cong Y$ . 则存在 $Y\map g X$ 使得 $gf=1_X,fg=1_Y$ . 由于函子保持恒等映射和态射复合, 所以有 $F(gf)=F(g)F(f)=F(1_X)=1_{F(X)}$ , 另一方向同理. 因而 $F(f):F(X)\cong F(Y)$ .

### 1.2.24