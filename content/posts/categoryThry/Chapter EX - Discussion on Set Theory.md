---
title: Chapter EX - Discussion on Set Theory
date: 2026-10-15
tags:
  - category-theory
math: true
draft: false
---

## 前言

学习范畴论时, 我经常会从一个具体构造出发, 追问它与集合论、数理逻辑以及我们进行数学推理的背景有什么关系. 这些问题有些直接服务于教材, 有些则逐渐离开了当前章节. 因此我把 Introduction 与前三章中相关的延伸讨论集中到这里, 原章保留理解教材所需的定义、结论与前提.

这里既记录背景约定, 也保留我自己的证明与探索过程. 其中“意识宇宙”是我描述数学思考背景的用语; 具体论证仍需要说明使用了哪些假设.

## 语言背景 {#language-background}

我把我们实际进行数学思考时所依赖的对象、直觉和推理背景称为**意识宇宙**. 在明确写下某个形式系统之前, 我们已经能够在这个背景中谈论自然数、集合, 并进行数学推理. 这是本文理解形式化的出发点. 这里的意识宇宙指数学思考的背景; 下文的 Grothendieck 宇宙则是用于控制集合大小的数学概念, 两者需要区分.

一个**形式系统**规定了使用哪些符号、怎样组成合法的表达式、接受哪些公理, 以及允许怎样从已有表达式推出新的表达式. 这些属于语法层面的规定. 语义则通过解释, 把这些符号与背景中的某个数学结构联系起来, 使公式能够表达关于该结构的命题. 我们希望选取的公理和推理规则能够捕获其中一部分真理. 例如, PA 将大量通常的自然数论证形式化; 但一个命题能够在 PA 的语言中表达, 还不保证它能够在 PA 中被证明.

对于一个选定的形式系统 $T$, 在系统中使用公理和规则证明公式, 是对象层次的工作; 从外部研究 $T$ 的语言、证明以及模型, 则是相对于 $T$ 的元层次工作. 一个例子是归纳: 我们可以在 PA 中应用归纳公理模式证明算术结论, 也可以在外部对公式的结构或复杂度进行归纳, 证明关于语法对象的结论. 两者的研究对象与推理所处的位置不同.

这里还需要保留层次的相对性. 关于 PA 的元推理可以进一步在某个形式理论中实现, 例如在 ZFC 中定义公式和证明, 再研究 PA. 此时 ZFC 承担关于 PA 的元理论的角色; 当我们转而研究 ZFC 本身时, 它又成为对象理论. 因此, 意识宇宙说明我们开展数学活动的背景, 而“对象”和“元”还需要相对于当前研究的系统来区分.

**这组笔记目前是在这个背景中进行非形式化、但受公理约束的范畴论研究.** 我们使用范畴公理、通常的数学推理, 以及讨论时明确接受的背景假设, 尚未将所有论证逐步写入一个指定的完整形式系统. 用对象与态射表达一个性质, 是将它翻译成范畴语言; 要把整段讨论形式化, 还需要固定相应的语言、公理与推理规则.

**除非另有说明, 这组贯穿全书的范畴论学习笔记默认当前意识宇宙承认普通集合论选择公理 $\mathrm{AC}$:** 任意由集合编号的非空集合族都存在选择函数. 本文的 $\mathbf{Set}$ 指当前背景中的集合与函数; 因而这项约定等价于 $\mathrm{AC}_{\mathbf{Set}}$, 即 $\mathbf{Set}$ 中每个满态射都存在右逆. 这一等价在下文的 [选择公理](#choice-and-equivalence) 部分说明.

按上面的用语, 这是描述当前意识宇宙中集合与函数所具有的一项性质的外部语句, 也是我们接受的一项额外假设. 单凭一般的范畴公理, 并不能推出这项存在性结论. 当我们把同样的语句列入一个形式理论的公理时, 它又成为那个对象理论中的公理. 其他范畴的 $\mathrm{AC}_{\mathcal C}$ 则需要分别判断; 同一个背景可以满足 $\mathrm{AC}_{\mathbf{Set}}$, 同时不满足 $\mathrm{AC}_{\mathbf{Grp}}$.

我们也可以讨论接受不同假设的数学背景, 比如研究 $\mathrm{ZF}+\neg\mathrm{AC}$ 的模型. 将这些背景理解为不同的意识宇宙, 是我采用的哲学解释; 在具体推理中, 仍然需要说明当前接受哪些假设. 选择公理在这里表达的是选择函数的存在性, 并不要求人实际执行、描述或计算任意多次选择.

本组笔记先用朴素的对象与态射语言来研究范畴, 不把对象的具体集合论编码放入范畴公理. 这并不意味着推理完全不依赖背景基础; 集合、类以及统一选择的使用范围仍需说明. 涉及大范畴时, 普通集合论选择公理不直接保证真类编号的选择, 相应的宇宙层级或类选择原则见下文.

## 选择公理与范畴等价 {#choice-and-equivalence}

### 从教材中的选择公理出发

教材在第 71 页先定义 section, 再给出选择公理的原话:

> Every surjection has a section.

>[!definition] Section / right inverse
>在范畴 $\mathcal C$ 中, 对态射 $f:X\to Y$, 如果存在态射 $s:Y\to X$ 满足
>$$
>f\circ s=\operatorname{id}_Y,
>$$
>就称 $s$ 为 $f$ 的一个 **section**, 或者**右逆**.

在 $\mathbf{Set}$ 中, 有右逆的函数一定满射: 对每个 $y\in Y$, 元素 $s(y)$ 就是它的一个原像. 教材把反方向的断言称为选择公理. 为了与后面的推广区分, 我们将它记为 $\mathrm{AC}_{\mathbf{Set}}$.

>[!definition] $\mathrm{AC}_{\mathbf{Set}}$: 集合中的选择公理
>对任意集合 $X,Y$ 及满射 $f:X\to Y$, 都存在函数 $s:Y\to X$ 使得
>$$
>f\circ s=\operatorname{id}_Y.
>$$

为什么这里出现了“选择”? 对每个 $y\in Y$, 满射条件保证纤维
$$
f^{-1}(\{y\})=\{x\in X\mid f(x)=y\}
$$
非空. 指定右逆 $s$, 就是在每个纤维中选择一个元素 $s(y)$, 并将所有选择记录为一条函数. 这里断言的是函数的存在性, 不要求给出可计算或可描述的选择方法.

在 $\mathbf{Set}$ 中, 满态射恰好就是满射; 这个对应不需要选择公理. 满态射的定义是: 对 $f:X\to Y$, 任意 $u,v:Y\to Z$ 满足 $u\circ f=v\circ f$ 时都有 $u=v$. 定义与对应的证明保留在 [Chapter III 的 Choice 部分]({{< relref "posts/categoryThry/Chapter III - Interlude on sets.md" >}}#choice). 因而教材的断言也可以写成
$$
\mathbf{Set}\text{ 中每个满态射都存在右逆}.
$$

### 与普通集合论选择公理的关系

>[!definition] 集合论层面的选择公理 $\mathrm{AC}$
>给定集合 $I$ 及一族非空集合 $(X_i)_{i\in I}$, 存在函数
>$$
>c:I\to\bigcup_{i\in I}X_i
>$$
>使得 $c(i)\in X_i$ 对每个 $i\in I$ 都成立. 这样的 $c$ 称为这族集合的**选择函数**.

这里的 $I$ 必须是集合; 普通选择公理不直接涉及真类编号的选择. 在通常的 ZF 背景下, 有
$$
\boxed{\mathrm{AC}\Longleftrightarrow\mathrm{AC}_{\mathbf{Set}}.}
$$

>[!proof]
>先设 $\mathrm{AC}$ 成立. 对任意满射 $f:X\to Y$, 集合族 $(f^{-1}(\{y\}))_{y\in Y}$ 的每项都非空. 选择公理给出函数 $s:Y\to X$, 满足 $s(y)\in f^{-1}(\{y\})$, 因而 $f(s(y))=y$. 所以 $s$ 是右逆, 得到 $\mathrm{AC}_{\mathbf{Set}}$.
>
>反过来, 设 $\mathrm{AC}_{\mathbf{Set}}$ 成立. 对一族非空集合 $(X_i)_{i\in I}$, 构造不交并
>$$
>E=\{(i,x)\mid i\in I,\ x\in X_i\},
>$$
>以及投影 $p:E\to I$, $p(i,x)=i$. 每个 $X_i$ 非空, 所以 $p$ 满射. 根据 $\mathrm{AC}_{\mathbf{Set}}$, 存在右逆 $s:I\to E$. 等式 $p(s(i))=i$ 保证 $s(i)$ 具有形式 $(i,x_i)$, 其中 $x_i\in X_i$. 因而 $c(i)=x_i$ 就是所需的选择函数.

所以, 我们在意识宇宙中接受普通集合论选择公理, 就等价于断言当前集合与函数构成的范畴满足 $\mathrm{AC}_{\mathbf{Set}}$. 这两个表述使用的是同一背景中的集合与函数.

### 其他范畴中的选择性质 {#choice-in-other-categories}

右逆的定义也只涉及态射、复合与恒等态射. 所以我们可以保留这个句式, 将 $\mathbf{Set}$ 换成其他范畴.

>[!definition] 范畴 $\mathcal C$ 的选择性质 $\mathrm{AC}_{\mathcal C}$
>对固定的范畴 $\mathcal C$, 记 $\mathrm{AC}_{\mathcal C}$ 为以下性质: 每个满态射 $f:X\to Y$ 都存在 $\mathcal C$ 中的态射 $s:Y\to X$, 满足
>$$
>f\circ s=\operatorname{id}_Y.
>$$
>有右逆的满态射也称为**分裂满态射** (split epimorphism), 因而这个性质可以简称为“每个满态射都分裂”.

在任意范畴中, 有右逆一定能推出满态射.

>[!proof]
>若 $u\circ f=v\circ f$ 且 $f\circ s=\operatorname{id}_Y$, 就在等式两边右复合 $s$, 得到
>$$
>u=u\circ f\circ s=v\circ f\circ s=v.
>$$
>所以 $f$ 满足右消去律, 是满态射.

但从满态射推出右逆需要额外条件, 一般的范畴公理并不保证它成立.

按照本文关于意识宇宙的用语, **这些选择命题是对我们意识宇宙中所研究结构的不同限定**. 例如, $\mathrm{AC}_{\mathbf{Set}}$ 要求其中的集合与函数具有上述性质; $\mathrm{AC}_{\mathbf{Grp}}$ 则要求其中的群与群同态具有相应性质. 每次都需要说明所谈的是哪个范畴, 以及允许哪些态射.

当研究抽象范畴 $\mathcal C$ 时, 可以将 $\mathrm{AC}_{\mathcal C}$ 作为额外公理, 限定所研究的范畴. 当 $\mathcal C$ 已经是一个具体确定的范畴时, 它就是一条需要判断真假的外部命题. 不同范畴的这些命题也不自动形成一条强弱有序的公理链.

例如, 在同一个接受普通选择公理的背景中, 可以同时有 $\mathrm{AC}_{\mathbf{Set}}$ 成立, 而 $\mathrm{AC}_{\mathbf{Grp}}$ 不成立.

>[!example] 群中的满态射
>取商同态
>$$
>q:\mathbb Z\to\mathbb Z/2\mathbb Z,\qquad q(n)=\overline n.
>$$

$q$ 是满射群同态, 因而是 $\mathbf{Grp}$ 中的满态射. 但它没有群同态右逆.

>[!proof]
>若存在群同态右逆 $s:\mathbb Z/2\mathbb Z\to\mathbb Z$, 则
>$$
>2s(\overline1)=s(\overline1+\overline1)=s(\overline0)=0.
>$$
>因为 $\mathbb Z$ 中没有非零元素满足 $2n=0$, 所以 $s(\overline1)=0$. 于是 $q(s(\overline1))=\overline0\ne\overline1$, 与 $q\circ s=\operatorname{id}_{\mathbb Z/2\mathbb Z}$ 矛盾.

作为集合之间的函数, $q$ 确实可以取右逆 $s(\overline0)=0$, $s(\overline1)=1$. 但这条函数不是群同态, 因而不是 $\mathbf{Grp}$ 中的态射. 可见, 普通选择公理保证的原像选择, 未必保持其他范畴要求的结构.

因此, 我们不能进一步断言“所有范畴都满足 $\mathrm{AC}_{\mathcal C}$”. 上面的群范畴已经给出反例. 只要保留这些对象、态射及通常的推理规则, 增加选择原则也不能让这个已经被否定的具体性质成立.

### 等价判据中的选择 {#equivalence-choice}

[Chapter I 的等价判据]({{< relref "posts/categoryThry/Chapter I - Categories, functors and natural transformations.md" >}}#natural-transformations) 从 full、faithful 与 essentially surjective 构造拟逆时, 我们多次说“选择一个对象”或者“选择一个同构”. 如果范畴的对象不能组成集合, 那么这些选择是否仍然安全? 这个问题确实存在. 不过真正需要注意的并不是“选择的次数太多”, 而是我们是否需要同时作出一整族选择, 以及这族选择是由集合还是由真类来编号的.

#### 选择发生在哪里

回到 full、faithful 且 essentially surjective 的函子 $F:\mathscr{A}\to\mathscr{B}$. 对于每个 $B\in\mathscr{B}$ , 本质满性告诉我们: 存在某个 $A\in\mathscr{A}$ 以及同构
$$\epsilon_B:F(A)\xrightarrow{\sim}B.$$
但是这句话只分别保证了每个 $B$ 都有这样的 $A$. 为了定义拟逆函子 $G$, 我们还要对所有 $B$ 同时指定一个这样的对象, 并令
$$G(B)=A.$$
因此证明真正需要的是一族选择
$$B\longmapsto\bigl(G(B),\epsilon_B:F(G(B))\xrightarrow{\sim}B\bigr).$$

一旦这族数据已经选好, 态射上的定义就不再需要选择. 对于任意的 $f:B\to B'$, 因为 $F$ 是 full 且 faithful, 所以恰好存在一个态射 $G(f):G(B)\to G(B')$ 满足
$$F(G(f))=\epsilon_{B'}^{-1}\circ f\circ\epsilon_B.$$
这里 full 保证它存在, faithful 保证它唯一. 恒等态射与复合的验证也都由唯一性直接得到. 因此, 整个构造中真正需要选择的是对象以及相应的同构, 而不是态射.

Chapter I 的正文中“先选取每个同构类的代表元”的说法很适合帮助理解: $G$ 要把彼此同构的对象送到预先选好的代表元. 不过对于大范畴, “所有同构类组成的商”本身可能有大小问题. 所以在正式处理大范畴时, 直接对每个 $B$ 选择 $G(B)$ 和 $\epsilon_B$ 会更稳妥.

#### 选择公理确实参与了这个定理

如果 $\mathscr{A}$ 和 $\mathscr{B}$ 都是小范畴, 那么上述候选对象与同构可以组成一族非空集合, 普通的选择公理便允许我们同时选出 $G(B)$ 和 $\epsilon_B$. 这里的选择并不只是某种证明技巧: 对所有小范畴都断言
$$\text{full}+\text{faithful}+\text{essentially surjective}\Longrightarrow\text{equivalence}$$
实际上已经足以推出选择公理.

>[!proof] 小范畴的等价判据推出选择公理
>为了看出这一点, 设 $(X_i)_{i\in I}$ 是一族非空集合. 构造范畴 $\mathscr{A}$, 其对象是所有的 $(i,x)$, 其中 $x\in X_i$; 两个对象之间恰好有一个态射, 当且仅当它们的第一个分量相同. 再令 $\mathscr{B}$ 为以 $I$ 为对象的离散范畴, 并定义
>$$F:\mathscr{A}\to\mathscr{B},\qquad F(i,x)=i.$$
>$F$ 是 full、faithful 且 essentially surjective. 如果它一定存在拟逆 $G$, 那么 $G(i)$ 必须具有形式 $(i,x_i)$, 从而 $i\mapsto x_i$ 就是这一族集合的选择函数. 所以, 如果不使用任何形式的选择公理, 这个定理的反方向一般不能成立.

因此, 这里的问题并不是选择公理处于一种无法讨论的模糊状态. 它与 ZF 的关系可以被精确地研究; 对当前证明来说, 关键只是明确我们采用了哪一种选择原则, 以及它是否足以完成这里的选择.

需要区分的是, 从“$F$ 是 equivalence”推出它 full、faithful 且 essentially surjective 的方向并不需要重新作出这些选择, 因为拟逆 $G$ 和两个自然同构已经作为条件的一部分给出了. 需要选择的是反方向, 即从三个性质构造 $G$ 的过程.

因而在通常的 ZF 背景下, 有
$$
\mathrm{AC}
\Longleftrightarrow\mathrm{AC}_{\mathbf{Set}}
\Longleftrightarrow
\begin{gathered}
\text{小范畴之间的每个 full、faithful 且}\\
\text{essentially surjective 的函子都是等价}.
\end{gathered}
$$
这里只针对某个特定函子给出一套选择数据, 并不等于接受了对所有集合族都成立的完整选择公理.

### 选择范围更小: 有限或可数编号

所谓“更低层面的选择”, 可以指只允许对某些范围的集合族作选择. 例如, 有限多个非空集合可以同时选择, 这在 ZF 中已经能够证明; 如果只接受可数选择, 就只保证由可数集合编号的非空集合族有选择函数.

这些限制对应于满射的目标集合大小: 有限的目标集合只需要有限次选择, 可数的目标集合只需要可数选择. 因此, $\mathbf{FinSet}$ 中每个满态射都有右逆可以在 ZF 中证明, 却不能由此推出整个 $\mathbf{Set}$ 的 $\mathrm{AC}_{\mathbf{Set}}$. 可数选择也不保证任意大小的满射都有右逆.

同样, 在 Chapter I 的构造中, 如果候选集合确实都是集合, 且 $\operatorname{Ob}(\mathscr{B})$ 有限或可数, 相应范围的选择就足够. 只接受这些较弱原则, 还不能得到对所有小范畴都成立的等价结论. 这里“有限次选择”指索引集有限, 不应与“从任意多的非空有限集合中同时选择”混淆.

### 当范畴是大范畴时 {#large-categories-and-choice}

如果 $\operatorname{Ob}(\mathscr{B})$ 是真类, 那么我们需要的就是一族由真类编号的选择. ZFC 中的选择公理只谈集合族, 因而不能直接保证这种选择存在. 仅仅要求范畴 locally small 也不能解决这个问题: locally small 只保证任意两个对象之间的态射组成集合, 并不保证所有对象组成集合.

这正是为什么 $\mathbf{Set}$、$\mathbf{Vect}_k$、$\mathbf{Grp}$、$\mathbf{Ring}$ 和 $\mathbf{CRing}$ 等范畴通常被视为大范畴. 它们虽然 locally small, 但对象并不能在通常的集合论层级中组成集合; 它们一般也不能通过取一个小骨架而变成小范畴. 因此, 把所有范畴都规定成小范畴虽然能避开当前问题, 却会排除许多最常用的例子.

常见的处理方式有以下几种:

1. **只在小范畴之间使用这个定理.** 此时普通的选择公理已经足够. 这是最简单的做法, 但使用范围有限.

2. **使用 Grothendieck universe.** 先固定一个宇宙 $\mathcal U$, 把其中的集合叫作小集合; 再在一个更大的宇宙 $\mathcal V$ 中讨论它们. 这样 $\mathbf{Set}_{\mathcal U}$ 相对于 $\mathcal U$ 是大范畴, 但它的全部对象相对于 $\mathcal V$ 又构成集合, 因而可以在更高一层使用选择公理. 这种方法不会消灭大小问题, 而是把所需的选择放到更高的集合论层级中. 还要注意, “存在足够多的 Grothendieck universe”通常作为额外的集合论约定使用, 不能直接由 ZFC 证明.

3. **使用带有全局选择原则的类理论.** 例如在 NBG 或 GBC 一类理论中把集合和真类都作为讨论对象, 再加入足够的 Global Choice 原则, 便可以为这里出现的类族统一指定代表元. 这使我们能够直接处理大范畴, 但必须明确说明所采用的基础体系.

还有一种不依赖选择公理的说法: 把 essentially surjective 加强为 **split essentially surjective**. 这不只要求每个 $B$ 存在某个原像, 而是把选好的 $G(B)$ 与同构 $\epsilon_B:F(G(B))\cong B$ 直接作为条件的一部分. 此时可以由这些数据构造 $G$, 不必再调用选择公理. 换句话说, 我们没有消除选择的数据, 而是把它从证明中的隐含步骤改成了定理的显式条件.

#### 不同宇宙中的选择如何联系

“更高或更低”也可以指所讨论集合的大小层级. 这与上面限制索引集有限或可数是两个不同的问题.

例如, 固定两个 Grothendieck 宇宙 $\mathcal U\in\mathcal V$, 并用 $\mathbf{Set}_{\mathcal U}$、$\mathbf{Set}_{\mathcal V}$ 分别表示相应范围内的集合与函数. 在较大宇宙 $\mathcal V$ 中接受普通选择公理, 就能为 $\mathcal U$ 中的满射选取右逆. 而且这个右逆仍属于 $\mathcal U$: 若 $f:X\to Y$ 的 $X,Y$ 都在 $\mathcal U$ 中, 则右逆的图是 $Y\times X$ 的子集, 由 Grothendieck 宇宙的闭包性质, 它也在 $\mathcal U$ 中.

因此, 对这样的宇宙层级, 较大范围内的选择能够保证较小范围内的 $\mathrm{AC}_{\mathbf{Set}_{\mathcal U}}$. 但只接受 $\mathcal U$ 范围内的选择, 并不自动保证 $\mathcal V$ 范围内的选择, 也不能直接完成 $\mathcal U$ 外的大族选择. 这里使用了 Grothendieck 宇宙的闭包性质, 不能不加限定地推广到任意两个集合论模型.

这提供了处理大范畴的一种方式: $\mathbf{Set}_{\mathcal U}$ 的全部对象相对于 $\mathcal U$ 不组成小集合, 但在 $\mathcal V$ 中组成集合, 因而可以使用较大范围内的选择公理. 存在这样的 Grothendieck 宇宙层级本身是额外的基础假设, 不能由普通选择公理单独得到.

如果直接在类理论中处理真类编号的选择, 则还需要相应的类选择原则. 例如, **Global Choice** 可以表述为: 存在一个类函数, 为每个非空集合指定其中的一个元素. 在合适的类理论背景中, 它推出普通集合选择, 也能支持 Chapter I 中对大范畴的对象及同构作统一选择. 但普通 $\mathrm{AC}$ 或 $\mathrm{AC}_{\mathbf{Set}}$ 本身不直接提供这套类层面的选择.

因此, 讨论不同选择原则时, 我们需要分别说明**选择的集合族范围、所使用的集合宇宙层级, 以及命题针对的范畴**. 单凭“对象层次”或“元层次”的名称, 不能判断它们的强弱. 即使接受全局选择, 也不会使所有范畴的满态射都有右逆; 上面的 $\mathbf{Grp}$ 反例仍然存在.

### 本组笔记采用的约定

在这组笔记中, “full、faithful 且 essentially surjective 的函子是等价”应理解为已经采用了足够的选择原则. 对小范畴, 普通选择公理即可; 对大范畴, 可以使用 Grothendieck universe 的层级约定, 或在类理论中采用相应的全局选择原则. 如果希望完全不依赖选择公理, 就应当把 essentially surjective 改成 split essentially surjective, 并明确给出所选择的对象与同构.

关于这些集合论约定, 可以进一步参考 [Mike Shulman, *Set theory for category theory*, §7–8](https://arxiv.org/abs/0810.1279) 以及 [Zhen Lin Low, *Universes for category theory*](https://arxiv.org/abs/1304.5227). [Stacks Project 的等价判据](https://stacks.math.columbia.edu/tag/02C3) 明确把范畴限制为小范畴; 满态射的定义见 [Tag 003A](https://stacks.math.columbia.edu/tag/003A).

## 超限归纳,良序与Hartogs {#transfinite-well-orders-hartogs}

先前在构造不动点时, 我用到了超限递归与 Hartogs 数. 现在我希望把这些工具本身弄清楚, 尤其是它们在元层面与对象层面之间如何表述. 本节先说明超限递归和超限归纳, 再沿着我自己的思路证明良序集存在唯一序型, 最后构造 Hartogs 数.

以下讨论可以在 ZF 中完成, 不需要 AC. 我们使用 von Neumann 序数: 序数是由 $\in$ 严格良序的传递集合, 对序数写 $\xi<\eta$ 就是 $\xi\in\eta$. 集合 $X$ 上的非严格良序 $\leq$ 可以转换成严格良序 $R$, 其中 $xRy$ 表示 $x\leq y$ 且 $x\ne y$. 后面的 $\operatorname{WO}(X,R)$ 统一表示这个严格版本.

### 1. 超限归纳

#### 1.1 超限递归原理 {#transfinite-recursion}

超限递归允许我们按照一个规则, 从此前已经得到的全部历史确定下一项. 如果所得序列记作 $g$, 那么在阶段 $\beta$ 输入规则的对象是 $g\restriction\beta$, 而非仅仅上一项 $g(\beta-1)$. 极限阶段同样有一个由全部先前阶段组成的历史.

这里需要分别说明: 定义域是否限制在某个序数之内, 以及规则是作为集合函数给出, 还是由固定公式描述.

##### 有上界, 规则是集合函数

固定序数 $\alpha$ 和集合 $X$. 令
$$
\operatorname{Hist}_{\alpha}(X)
=\{h\mid\exists\beta<\alpha,\ h:\beta\to X\}.
$$
这是所有长度小于 $\alpha$、取值于 $X$ 的历史初段组成的集合. 每个这样的函数图都包含于 $\alpha\times X$, 所以可以从 $\mathcal P(\alpha\times X)$ 中用分离取得它.

>[!theorem] 有界的集合函数递归
>若 $f:\operatorname{Hist}_{\alpha}(X)\to X$, 则存在唯一函数 $g:\alpha\to X$ 满足
>$$
>\forall\beta<\alpha,\qquad
>g(\beta)=f(g\restriction\beta).
>$$

这里 $f$ 本身是集合, 可以成为对象语言中被量化的变量. 因而上述结论可以写成一条全称定理:
$$
\begin{aligned}
\mathrm{ZF}\vdash\forall X\,\forall\alpha\,\forall f\,
\Bigl[&
\bigl(\operatorname{Ord}(\alpha)
\land f:\operatorname{Hist}_{\alpha}(X)\to X\bigr)\\
&\longrightarrow
\exists!g\bigl(
g:\alpha\to X
\land\forall\beta<\alpha\
g(\beta)=f(g\restriction\beta)
\bigr)
\Bigr].
\end{aligned}
$$
“函数”“序数”“限制”等记号都可以展开为集合论语言 $\{\in\}$ 中的一阶公式. 所谓这个版本可以被对象化, 是指递归序列存在且唯一的全称断言能够在 ZF 中表达并证明.

##### 有上界, 规则由类函数公式描述 {#bounded-class-recursion}

现在不预先指定值域集合. 在元层面固定一个公式 $\psi(h,y,p)$, 其中 $p$ 是集合参数, 用它表达“历史 $h$ 导出下一项 $y$”. 为了在 ZF 中得到对应的递归结论, 需要先给出规则函数性的 ZF 证明. 为了记号简洁, 这里要求对每个集合输入都有唯一输出:
$$
\mathrm{ZF}\vdash\forall h\,\exists!y\,\psi(h,y,p).
$$
裸公式 $\forall h\,\exists!y\,\psi(h,y,p)$ 表达规则具有函数性; 加上 $\mathrm{ZF}\vdash$ 则是在元层面说明这条公式能够由 ZF 的公理与推理规则证明. 这里 $p$ 是自由参数, 若证明没有关于 $p$ 的额外假设, 就可以进一步对 $p$ 作全称概括. 若函数性只在某个条件 $C(p)$ 下成立, 则应证明
$$
\mathrm{ZF}\vdash
\forall p\bigl(
C(p)\longrightarrow\forall h\,\exists!y\,\psi(h,y,p)
\bigr),
$$
并在相应条件下应用递归定理.

实际上只需在有关的序数域函数上保证这一条件; 对其他输入可以补上一个默认输出.

>[!definition] 函数谓词 $\operatorname{Fun}(g)$
>$\operatorname{Fun}(g)$ 表示集合 $g$ 是一个函数的图: 它的每个元素都是有序对, 并且同一第一分量至多对应一个第二分量. 具体可以写为
>$$
>\begin{aligned}
>\operatorname{Fun}(g)\quad:\equiv\quad&
>\bigl(\forall u\in g\,\exists x\,\exists y\
>u=\langle x,y\rangle\bigr)\\
>&\land\forall x\,\forall y\,\forall y'\,
>\Bigl[
>(\langle x,y\rangle\in g\land\langle x,y'\rangle\in g)
>\longrightarrow y=y'
>\Bigr].
>\end{aligned}
>$$

在 ZF 中, 函数以它的图表示; 有序对也可以用 $\langle x,y\rangle=\{\{x\},\{x,y\}\}$ 编码, 所以 $\operatorname{Fun}$ 是一阶公式的缩写, 并非额外的原始符号. 空集也满足这个谓词, 对应空函数. $\operatorname{Fun}(g)$ 本身不指定定义域, 因而下面还要另写 $\operatorname{dom}(g)=\alpha$.

选定 $\psi$ 之后, 我们在元层面按下面的句法模板构造公式 $R_\psi$:
$$
\begin{aligned}
R_\psi(\alpha,g,p)
\quad:\equiv\quad&
\operatorname{Ord}(\alpha)
\land \operatorname{Fun}(g)
\land\operatorname{dom}(g)=\alpha\\
&\land\forall\beta<\alpha\
\psi(g\restriction\beta,g(\beta),p).
\end{aligned}
$$
这里从 $\psi$ 到 $R_\psi$ 的构造是元层面关于公式的句法操作; 下标 $\psi$ 标记已经选定的公式, 不是对象语言中额外的量化变量. 构造得到的 $R_\psi(\alpha,g,p)$ 本身则是对象语言中的一阶公式, 可以在 ZF 中使用. 它表达“$g$ 是按照规则 $\psi$ 构造的长度为 $\alpha$ 的递归序列”. 对每个固定的 $\psi$, ZF 都能证明
$$
\begin{aligned}
\mathrm{ZF}\vdash\forall p\,
\Bigl[
\bigl(\forall h\,\exists!y\,\psi(h,y,p)\bigr)
\longrightarrow
\forall\alpha\bigl(
\operatorname{Ord}(\alpha)
\longrightarrow\exists!g\,R_\psi(\alpha,g,p)
\bigr)
\Bigr].
\end{aligned}
$$
所以, 没有预先给出值域集合并不妨碍有界递归在 ZF 中进行. 这里仍然有关于参数 $p$ 与上界 $\alpha$ 的全称定理; 但公式 $\psi$ 是在元层面选定的, 不属于这条公式中的量化变量.

这条条件定理将函数性公式保留为对象语言中的前提. 要推出不带这个前提的递归结论, 就结合开头给出的函数性证明. $\mathrm{ZF}\vdash$ 表达的是元层面的可证性, 不能直接塞进上述方括号内充当对象语言中的条件.

证明的 idea 是先验证不同长度的递归初段彼此相容, 再在后继阶段添加一个值, 在极限阶段把已有初段并起来. 下面使用 [超限归纳法](#transfinite-induction) 来完成这个证明.

>[!proof] 有界递归序列的存在与唯一性
>先固定满足函数性条件的参数 $p$. 若 $g,h$ 都满足相应的递归条件, 它们在公共定义域上必定相同. 否则取最小的不同位置 $\beta$. 此前 $g\restriction\beta=h\restriction\beta$, 而 $\psi$ 对同一输入只允许一个输出, 从而 $g(\beta)=h(\beta)$, 矛盾. 特别地, 较长的递归初段必定延伸较短的初段.
>
>对 $\alpha$ 作超限归纳. 当 $\alpha=0$ 时, 空函数满足要求. 若长度为 $\gamma$ 的递归序列 $g_\gamma$ 已经存在, 取满足 $\psi(g_\gamma,y,p)$ 的唯一 $y$, 并令
>$$
>g_{\gamma+1}=g_\gamma\cup\{\langle\gamma,y\rangle\}.
>$$
>它满足长度为 $\gamma+1$ 的递归条件.
>
>若 $\lambda$ 为非零极限序数, 并且每个 $\gamma<\lambda$ 都存在唯一的 $g_\gamma$, 则由公式 $R_\psi$ 及替换公理得到集合
>$$
>\{g_\gamma:\gamma<\lambda\}.
>$$
>令
>$$
>g_\lambda=\bigcup_{\gamma<\lambda}g_\gamma.
>$$
>初段之间的相容性保证它是定义域为 $\lambda$ 的函数. 对任意 $\beta<\lambda$, 有 $\beta+1<\lambda$, 因而可以在初段 $g_{\beta+1}$ 中验证阶段 $\beta$ 的递归条件. 所以 $g_\lambda$ 满足要求. 唯一性由第一段得到.

递归得到 $g:\alpha\to V$ 之后, 它的实际值域 $X_\alpha=\operatorname{ran}(g)$ 是集合. 进一步, 替换公理给出实际出现的初段集合与规则在其上的限制:
$$
\begin{aligned}
D_\alpha&=\{g\restriction\beta:\beta<\alpha\},\\
f_\alpha&=
\{\langle g\restriction\beta,g(\beta)\rangle:\beta<\alpha\}.
\end{aligned}
$$
于是 $f_\alpha:D_\alpha\to X_\alpha$ 是集合函数, 且 $g(\beta)=f_\alpha(g\restriction\beta)$. 这正是把类规则限制到实际递归路径上的方法.

不过, $X_\alpha$ 只收集实际出现的输出. 原规则作用于其他取值在 $X_\alpha$ 中的历史时, 仍可能导出 $X_\alpha$ 外的值. 因此, 这个事后取得的限制不自动等于一个定义在全部 $\operatorname{Hist}_{\alpha}(X_\alpha)$ 上、取值仍在 $X_\alpha$ 中的规则. 也不能反过来用尚未构造的 $g$ 及其值域证明 $g$ 的存在.

##### 无上界, 规则与结果都由公式描述

如果希望在所有序数上递归, 最终得到的图不会是集合, 因为它的定义域是全体序数. 但我们仍可以显式写出描述这个类函数的公式:
$$
\begin{aligned}
\varphi_\psi(\alpha,y,p)
\quad:\equiv\quad&
\operatorname{Ord}(\alpha)\\
&\land\exists g\bigl(
R_\psi(\alpha+1,g,p)\land g(\alpha)=y
\bigr).
\end{aligned}
$$
也就是说, 先用公式描述长度为 $\alpha+1$ 的递归初段, 再读取它在 $\alpha$ 处的值. 初段的相容性保证不同长度的构造给出同样的结果.

此时, 我们刚刚讨论的四个步骤可以明确写为:

1. **元层面: 给出规则公式.** 选定 $\psi(h,y,p)$, 说明它表达怎样的递归规则.
2. **对象层面: 证明规则的函数性.** 给出 $\mathrm{ZF}\vdash\forall h\,\exists!y\,\psi(h,y,p)$ 所表示的形式证明; 如果参数需要满足 $C(p)$, 就证明带有这一前提的版本. 被证明的函数性公式属于对象语言, 而 $\mathrm{ZF}\vdash$ 是我们在元语言中对可证性的表述. 这里的“验证”并不承诺一个自动判定任意公式是否具有函数性的程序.
3. **元层面: 按模板构造新公式.** 将 $\psi$ 代入 $R_\psi$ 与 $\varphi_\psi$ 的句法模板, 得到显式的一阶公式 $\varphi_\psi(\alpha,y,p)$. 构造公式本身不必等待第 2 步; 第 2 步提供后面应用定理的条件.
4. **元层面: 按证明范式生成对象层面的证明.** 这里的范式指上面的 [“有界递归序列的存在与唯一性”证明](#bounded-class-recursion), 以及随后由递归初段定义 $\varphi_\psi$ 的构造与论证, 包括下文 [“$\varphi_\psi$ 满足递归要求”](#unbounded-recursion-correctness) 中的证明. 将选定的 $\psi$ 及第 2 步给出的函数性证明代入这个通用范式, 由它生成新公式对每个序数具有唯一输出、且输出遵循原规则的 ZF 证明. 生成证明的操作发生在元层面, 生成的证明则属于对象层面的 ZF.

因此, 应用这个原理时, 我们需要自行提供的证明只有第 2 步中原规则的函数性证明. 第 4 步由既有的证明范式生成, 无需再为这个具体规则独立寻找递归结论的证明.

这个范式为每个固定的 $\psi$ 生成如下条件定理的证明; 再结合第 2 步的函数性证明, 就得到新公式的函数性:
$$
\begin{aligned}
\mathrm{ZF}\vdash\forall p\,
\Bigl[
\bigl(\forall h\,\exists!y\,\psi(h,y,p)\bigr)
\longrightarrow
\forall\alpha\bigl(
\operatorname{Ord}(\alpha)
\longrightarrow\exists!y\,\varphi_\psi(\alpha,y,p)
\bigr)
\Bigr].
\end{aligned}
$$

###### $\varphi_\psi$ 满足递归要求 {#unbounded-recursion-correctness}

递归要求也可以明确写成一条 ZF 定理. 先在元层面定义公式
$$
\begin{aligned}
P_\psi(\alpha,h,p)\quad:\equiv\quad&
\operatorname{Fun}(h)
\land\operatorname{dom}(h)=\alpha\\
&\land\forall\beta<\alpha\
\varphi_\psi(\beta,h(\beta),p).
\end{aligned}
$$
它表达“$h$ 是由 $\varphi_\psi$ 给出的长度为 $\alpha$ 的历史函数”. 对每个固定的 $\psi$, 上面同一个证明范式还给出
$$
\begin{aligned}
\mathrm{ZF}\vdash\forall p\,\Bigl[
&\bigl(\forall k\,\exists!y\,\psi(k,y,p)\bigr)
\longrightarrow\\
&\forall\alpha\Bigl(
\operatorname{Ord}(\alpha)\longrightarrow
\exists!h\,\Bigl[
P_\psi(\alpha,h,p)\\
&\hspace{4em}\land\forall y\bigl(
\varphi_\psi(\alpha,y,p)
\longleftrightarrow\psi(h,y,p)
\bigr)
\Bigr]\Bigr)
\Bigr].
\end{aligned}
$$
其中 $h$ 的存在性说明每个阶段之前的全部历史确实组成一个集合函数; 双条件则说明, $\varphi_\psi$ 在该阶段给出的值恰好是规则 $\psi$ 对这个历史给出的值. 结合第 2 步提供的规则函数性的 ZF 证明, 即可在相应参数条件下消去函数性前提, 得到 **ZF 对“构造出来的 $\varphi_\psi$ 满足递归要求”的证明**.

>[!proof] 从有界递归得到递归关系
>固定满足函数性前提的 $p$ 及序数 $\alpha$. 由有界递归定理, 存在唯一的 $g$ 满足 $R_\psi(\alpha+1,g,p)$. 令 $h=g\restriction\alpha$.
>
>对每个 $\beta<\alpha$, 限制 $g\restriction(\beta+1)$ 满足 $R_\psi(\beta+1,g\restriction(\beta+1),p)$. 因而由 $\varphi_\psi$ 的定义,
>$$
>\varphi_\psi(\beta,g(\beta),p).
>$$
>所以 $P_\psi(\alpha,h,p)$ 成立. 又由 $g$ 在阶段 $\alpha$ 的递归条件及 $\varphi_\psi$ 的定义, 分别得到
>$$
>\psi(h,g(\alpha),p),\qquad
>\varphi_\psi(\alpha,g(\alpha),p).
>$$
>$\psi(h,-,p)$ 的输出唯一性来自前提, $\varphi_\psi(\alpha,-,p)$ 的输出唯一性来自有界递归的唯一性. 二者都有输出 $g(\alpha)$, 因而对任意 $y$ 都有
>$$
>\varphi_\psi(\alpha,y,p)
>\longleftrightarrow\psi(h,y,p).
>$$
>最后, 若 $h'$ 也满足 $P_\psi(\alpha,h',p)$, 则由 $\varphi_\psi$ 在每个 $\beta<\alpha$ 处的输出唯一性, 有 $h'(\beta)=h(\beta)$. 两者的定义域都是 $\alpha$, 所以由函数外延性得到 $h'=h$.

这里 $p,\alpha,h,y$ 等量化变量全部表示集合. $\psi$、$\varphi_\psi$ 与 $P_\psi$ 则是在元层面固定的公式, 将这些缩写展开后, 上面的断言就是集合论语言中的一阶公式. 这一证明同样可以按既有范式在 ZF 中形式化, 不需要另行提供关于这个具体 $\psi$ 的递归正确性证明.

若用 $F_p(\alpha)$ 简记 $\varphi_\psi$ 描述的值, 刚刚证明的递归关系便可以简写为
$$
\psi(F_p\restriction\alpha,F_p(\alpha),p).
$$
这里 $F_p\restriction\alpha$ 就是上面的历史函数 $h$, 上式的一阶表述已经给出. 这个类函数也由递归关系唯一确定: 两个候选若在某阶段不同, 取最小的不同阶段, 就与原规则的函数性矛盾. 这里比较的候选也各自由固定公式描述, 唯一性按相应公式实例理解, 不引入对所有类函数的量词.

因此, “对每个规则公式 $\psi$, 都可以构造相应公式及证明”是元层面的**定理模式**; 对每个固定 $\psi$, 得到的函数性与递归性质都有对象层面的 ZF 证明. 一阶 ZF 中不能直接写 $\forall\psi$ 并把 $\psi$ 当作可应用的谓词变量. 对谓词或关系变量量化属于二阶语法; 对公式的语法编码量化则仍可以是一阶的, 但编码本身不会自动在谓词位置发挥作用.

#### 1.2 超限归纳法 {#transfinite-induction}

超限递归构造序列; 超限归纳则用来证明性质. 这里也可以区分两种表述: 在有上界时用集合表示性质, 或者在元层面固定一个描述性质的一阶公式.

##### 有上界, 性质由集合表示 {#bounded-set-induction}

固定一个序数 $\kappa$. 如果只讨论阶段 $\beta<\kappa$, 就可以用一个子集 $S\subseteq\kappa$ 记录性质在哪些阶段成立: $\beta\in S$ 表示阶段 $\beta$ 满足性质. 这里 $S$ 表示性质的外延, 不承担编码性质公式的工作.

由于 $\beta$ 是序数, $\beta\subseteq S$ 就表示所有比 $\beta$ 小的阶段都属于 $S$. 因而归纳条件可以写成
$$
\forall\beta\in\kappa\,
\bigl(\beta\subseteq S\longrightarrow\beta\in S\bigr).
$$

>[!theorem] 有界超限归纳的集合版本
>若 $\kappa$ 是序数, $S\subseteq\kappa$, 并且对每个 $\beta\in\kappa$ 都有
>$$
>\beta\subseteq S\longrightarrow\beta\in S,
>$$
>那么 $S=\kappa$.

因为 $\kappa$ 与 $S$ 都是集合变量, 这个版本可以在 ZF 中写成一条统一的全称定理:
$$
\begin{aligned}
\mathrm{ZF}\vdash\forall\kappa\,\forall S\,\Bigl[
&\bigl(\operatorname{Ord}(\kappa)\land S\subseteq\kappa\\
&\quad\land\forall\beta\in\kappa\,
(\beta\subseteq S\longrightarrow\beta\in S)\bigr)
\longrightarrow S=\kappa
\Bigr].
\end{aligned}
$$
这里 $\forall S$ 是对象语言中对集合的一阶量化. 我们能够统一讨论所有作为性质外延的子集, 无需把性质公式放到量词的位置.

>[!proof] 最小反例
>若 $S\ne\kappa$, 则 $\kappa\setminus S$ 是序数 $\kappa$ 的非空子集, 因而存在最小元 $\beta$. 对任意 $\gamma<\beta$, 都有 $\gamma\in\kappa$, 且由 $\beta$ 的最小性得到 $\gamma\in S$. 所以 $\beta\subseteq S$. 归纳条件于是给出 $\beta\in S$, 与 $\beta\in\kappa\setminus S$ 矛盾.

##### 性质由固定公式描述

现在在元层面固定一个一阶公式 $P(\alpha,p)$, 用它表达我们要证明的性质, 其中 $p$ 是集合参数. 这个版本可以讨论全体序数上的归纳.

>[!theorem] 超限归纳
>若对每个序数 $\alpha$ 都有
>$$
>\bigl(\forall\beta<\alpha\ P(\beta,p)\bigr)
>\longrightarrow P(\alpha,p),
>$$
>那么对所有序数 $\alpha$ 都有 $P(\alpha,p)$.

同样, “对每个公式 $P$”是在元层面说的. 对每个固定的 $P$, 则有 ZF 中的全称定理
$$
\begin{aligned}
\mathrm{ZF}\vdash\forall p\,
\Bigl[
&\forall\alpha\bigl(
\operatorname{Ord}(\alpha)\longrightarrow
((\forall\beta<\alpha\ P(\beta,p))\longrightarrow P(\alpha,p))
\bigr)\\
&\longrightarrow
\forall\alpha\bigl(
\operatorname{Ord}(\alpha)\longrightarrow P(\alpha,p)
\bigr)
\Bigr].
\end{aligned}
$$

>[!proof]
>假定归纳条件成立, 却存在序数 $\gamma$ 不满足 $P$. 用分离公理得到非空集合
>$$
>C=\{\xi\leq\gamma:\neg P(\xi,p)\}.
>$$
>由序数的良序性, $C$ 有最小元 $\mu$. 对每个 $\xi<\mu$, 都有 $P(\xi,p)$; 归纳条件于是给出 $P(\mu,p)$, 与 $\mu\in C$ 矛盾.

这两个版本通过分离公理联系起来. 对于任意在元层面固定的公式 $P$、集合参数 $p$ 与序数 $\kappa$, 分离公理给出集合
$$
S=\{\beta\in\kappa:P(\beta,p)\}.
$$
将它代入上面的集合版本, 就得到关于公式 $P$ 的有界超限归纳实例. 因而在有上界时, 我们既可以先固定公式再应用归纳, 也可以直接在那条统一的 ZF 定理中对集合 $S$ 作全称量化.

无上界时, 性质成立的阶段可能形成真类. 例如性质恒真时, 它的全部成立阶段就是 $\operatorname{Ord}$, 无法收集成一个集合 $S$. 所以全体序数上的公式版本仍然按固定公式给出定理模式; 其中可以量化集合参数 $p$, 而“对每个公式 $P$”仍属于元层面的表述.

实践中常将归纳步骤分成三种情形:

1. **零阶段:** 证明 $P(0,p)$.
2. **后继阶段:** 从 $P(\gamma,p)$ 推出 $P(\gamma+1,p)$.
3. **非零极限阶段:** 从所有 $\xi<\lambda$ 都满足 $P(\xi,p)$ 推出 $P(\lambda,p)$.

这是一套有限的证明安排. 形式证明本身仍由有穷多个公式组成, 不需要实际完成无穷或超限多个推理步骤. 这个句法上的有穷性来自形式证明的定义; 序数归纳的正确性来自良序性. 正则性公理并不承担把一个无限证明压缩为有限证明的工作. 此外, 递归存在性也不保证递归值可以被有效计算.

### 2. 不同序数之间不存在保序同构 {#ordinals-order-isomorphism}

>[!theorem]
>若序数 $\alpha\ne\beta$, 则 $(\alpha,\in)$ 与 $(\beta,\in)$ 不存在保序同构.

我的思路是从假定的同构导出一个下降点, 再反复应用映射, 得到可数长度的严格递降路径. 这里需要准确说明被排除的情形: 序数上的保序单射可以存在, 但严格保序的自映射不可能把某个点送到它自身以下.

>[!proof]
>由序数的可比较性, 不妨设 $\alpha<\beta$. 若两者存在保序同构, 取其逆向映射 $f:\beta\to\alpha$. 因为 $\alpha\subsetneq\beta$, 也可以把它看作严格保序的映射 $f:\beta\to\beta$.
>
>取 $x\in\beta\setminus\alpha$, 则
>$$
>f(x)<\alpha\leq x<\beta,
>$$
>所以 $f(x)<x$. 自然数递归给出
>$$
>x_0=x,\qquad x_{n+1}=f(x_n),
>$$
>也就是
>$$
>x\longmapsto f(x)\longmapsto f^{(2)}(x)
>\longmapsto\cdots\longmapsto f^{(n)}(x)\longmapsto\cdots.
>$$
>从 $x_1<x_0$ 出发, 严格保序性保证
>$$
>x_{n+1}<x_n
>\quad\Longrightarrow\quad
>x_{n+2}=f(x_{n+1})<f(x_n)=x_{n+1}.
>$$
>因此整条路径严格递降.
>
>令非空集合 $D=\{x_n:n\in\omega\}\subseteq\beta$. 由良序性, 它有最小元 $\mu$. 对序数而言 $\mu\subseteq x_n$ 对每个 $n$ 都成立, 且 $\mu\in D$, 所以
>$$
>x_\omega:=\bigcap_{n\in\omega}x_n=\mu.
>$$
>但若 $\mu=x_k$, 则
>$$
>f(\mu)=x_{k+1}\in D,\qquad x_{k+1}<x_k=\mu,
>$$
>与 $\mu$ 的最小性矛盾. 所以假定的保序同构不存在.

这里的 $x_\omega$ 只是这条递降链的交集记号; 矛盾来自它必须是已有集合 $D$ 的最小元. 整个迭代由 $f$ 唯一决定, 不需要 AC. 它可以在 ZF 中得到统一的全称形式:
$$
\begin{aligned}
\mathrm{ZF}\vdash\forall\alpha\,\forall\beta\,
\Bigl[
&\operatorname{Ord}(\alpha)\land\operatorname{Ord}(\beta)
\land(\alpha,\in)\cong_{\mathrm{ord}}(\beta,\in)\\
&\longrightarrow\alpha=\beta
\Bigr].
\end{aligned}
$$
其中“存在保序同构”也可以展开为关于集合函数的一阶公式.

### 3. 任意良序集都同构于唯一一个序数 {#well-order-order-type}

>[!theorem]
>若 $R$ 是集合 $X$ 上的严格良序, 则存在唯一的序数 $\delta$, 使得
>$$
>(X,R)\cong_{\mathrm{ord}}(\delta,\in).
>$$

唯一性已经由上一部分得到: 若两个序数都与 $(X,R)$ 同构, 复合相应同构便得到它们之间的保序同构. 下面保留我从超限递归出发的存在性证明.

取新标记 $\Omega\notin X$. 以下统一令 $\Omega=X$, ZF 的正则性公理保证 $X\notin X$. 在 $X'=X\cup\{\Omega\}$ 中保留原来的序, 并把 $\Omega$ 放在所有 $x\in X$ 之后, 得到良序 $R'$.

>[!example] 依次枚举良序集的递归规则
>对历史函数 $h$, 令
>$$
>\Psi_{X,R}(h)=
>\begin{cases}
>\min_{R'}(X'\setminus\operatorname{ran}(h)),
>&X'\setminus\operatorname{ran}(h)\ne\varnothing,\\
>\Omega,&X'\setminus\operatorname{ran}(h)=\varnothing.
>\end{cases}
>$$
>对非函数输入补上默认值 $\Omega$, 便得到由一阶公式描述的类规则.

每个非空剩余集合都有唯一最小元, 空集情形也指定了唯一输出. 因此规则具有函数性. 无界超限递归给出类函数 $H$, 其公式记作 $H^*(X,R,\xi,y)$, 表示 $H(\xi)=y$. 递归关系为
$$
H(\xi)=\Psi_{X,R}(H\restriction\xi).
$$
这里必须保留取尽元素后的默认值: $\Omega$ 可以在后面反复出现, 不能将整个 $H$ 直接当作单射反转. 我们需要先证明每个 $x\in X$ 出现且只出现一次.

>[!proof] 存在性
>**每个 $x\in X$ 至多出现一次.** 若 $H(\xi)=x\in X$, 则之后的每个历史值域都已包含 $x$, 所以最小未出现元素的规则不会再次选中它; 默认输出 $\Omega$ 也不等于 $x$.
>
>**每个 $x\in X$ 都会出现.** 先用分离取得实际出现的元素集合
>$$
>Y=\{x\in X:\exists\xi\,
>(\operatorname{Ord}(\xi)\land H^*(X,R,\xi,x))\}.
>$$
>对每个 $x\in Y$, 出现序数存在且唯一. 对这个反向对应应用替换公理, 得到集合
>$$
>S=\{\xi:\exists x\in Y\
>(\operatorname{Ord}(\xi)\land H^*(X,R,\xi,x))\}.
>$$
>若某个 $x\in X$ 从未出现, 那么每个阶段的剩余集合都仍含 $x$. 因为 $x$ 位于 $\Omega$ 之前, 该阶段选出的最小元必属于 $X$, 不会是 $\Omega$. 于是每个序数 $\xi$ 都属于 $S$, 与不存在包含所有序数的集合矛盾: 此时 $S$ 就是全体序数组成的集合, 它自身也将是序数, 导出 $S\in S$. 因此 $Y=X$.
>
>**反向替换得到一个序数.** 现在可以定义反向公式
>$$
>H'(X,R,x,\xi)
>\quad:\equiv\quad
>x\in X\land\operatorname{Ord}(\xi)
>\land H^*(X,R,\xi,x).
>$$
>它在整个 $X$ 上具有存在唯一性. 对 $X$ 应用替换, 得到
>$$
>\delta=\{\xi:\exists x\in X\ H'(X,R,x,\xi)\}.
>$$
>一旦某阶段输出 $\Omega$, 那时 $X$ 中的元素就已全部出现; 否则未出现的元素位于 $\Omega$ 之前, 应当先被选出. 此后只能继续输出 $\Omega$.
>
>因此, 若 $\xi\in\delta$ 且 $\zeta<\xi$, 则 $H(\zeta)$ 也属于 $X$, 所以 $\zeta\in\delta$. $\delta$ 是传递的序数集合, 从而本身是序数.
>
>**枚举保持次序.** 限制 $H\restriction\delta$ 是集合函数, 并且是 $\delta\to X$ 的双射. 若 $\xi<\zeta<\delta$, 则 $H(\zeta)$ 在阶段 $\xi$ 尚未出现, 而 $H(\xi)$ 是那时剩余集合的最小元. 两者不同, 所以
>$$
>H(\xi)\mathrel R H(\zeta).
>$$
>两边都是线性序, 因而这个双射也反映次序, 给出所需的保序同构. 当 $X=\varnothing$ 时, 同一构造给出 $\delta=0$.

这也补足了我最初“把公式的两个位置反过来, 对 $X$ 应用替换”的想法: 反向公式必须使用递归导出的 $H^*$, 并且需要先证明它对每个 $x\in X$ 都给出唯一序数. 上面先对实际出现的 $Y$ 应用替换, 正是为了完成这个存在性论证; 这里没有借用 Hartogs 定理.

进一步, 可以统一定义序型公式:
$$
\begin{aligned}
T(X,R,\delta)\quad:\equiv\quad&
\operatorname{Ord}(\delta)\\
&\land\exists u\Bigl[
u:\delta\to X\text{ 是双射}\\
&\hspace{3em}\land
\forall\xi,\zeta\in\delta\
(\xi\in\zeta\longleftrightarrow
\langle u(\xi),u(\zeta)\rangle\in R)
\Bigr].
\end{aligned}
$$
这是一阶公式的缩写. 构造与证明对集合参数 $X,R$ 一致进行, 因而可以得到全称定理
$$
\mathrm{ZF}\vdash
\forall X\,\forall R\,
\bigl(
\operatorname{WO}(X,R)
\longrightarrow\exists!\delta\,T(X,R,\delta)
\bigr).
$$
所以这里的全称性能够在对象层面得到. 这条定理接受一个已经给定的良序, 并不保证任意集合都能被赋予良序; 后一个命题涉及选择公理.

### 4. Hartogs 数的构造 {#hartogs-number}

我希望找出最小的、不能单射到给定集合 $X$ 的序数. 如果这样的序数存在, 它应当是
$$
h(X)=
\min\{\alpha\in\operatorname{Ord}:
\text{不存在单射 }\alpha\hookrightarrow X\}.
$$
为了证明它存在, 我考虑先收集所有能够单射到 $X$ 的序数:
$$
B_X=
\{\alpha\in\operatorname{Ord}:
\text{存在单射 }\alpha\hookrightarrow X\}.
$$
这时右侧先是一条定义类的公式. 关键在于证明它实际上是集合, 而不能直接把对全体序数的分离当作集合构造.

#### 从 $X$ 的子集上的良序出发

对象层面的构造可以分成下面三步:

1. **幂集、笛卡尔积与分离:** 先形成集合
   $$
   \mathcal P(X)\times\mathcal P(X\times X),
   $$
   再从中分离得到
   $$
   Q=\{(Y,R):Y\subseteq X,\ R\subseteq Y\times Y\}.
   $$
   这里取得所有候选子集和关系, 首先需要幂集公理, 不能仅以“应用替换”代替这一步.
2. **分离:** 筛出良序对组成的集合
   $$
   W=\{(Y,R)\in Q:\operatorname{WO}(Y,R)\}.
   $$
3. **替换:** 由上一部分的统一公式 $T$, 每个 $(Y,R)\in W$ 都对应唯一的序型. 因而替换公理给出集合
   $$
   B=\{\alpha:\exists(Y,R)\in W\ T(Y,R,\alpha)\}.
   $$

这里收集的是所有候选良序的唯一序型, 无需为各个子集选择良序, 也无需从多个同构中选定一个. 接下来证明 $B=B_X$, 并且 $B$ 本身就是所求的 Hartogs 数.

>[!proof]
>**$B$ 恰好收集可注入 $X$ 的序数.** 若 $\alpha\in B$, 则存在 $Y\subseteq X$ 及其上的良序, 使 $\alpha$ 与 $Y$ 保序同构. 同构与包含映射复合, 就给出单射 $\alpha\hookrightarrow X$.
>
>反过来, 若 $\alpha$ 是序数且 $f:\alpha\hookrightarrow X$, 令 $Y=f[\alpha]$, 并沿 $f$ 搬运 $\alpha$ 的序:
>$$
>R=\{\langle f(\xi),f(\zeta)\rangle:
>\xi,\zeta\in\alpha,\ \xi\in\zeta\}.
>$$
>这使 $R$ 成为 $Y$ 上的良序, 且 $T(Y,R,\alpha)$, 因而 $\alpha\in B$. 所以
>$$
>\alpha\in B
>\quad\Longleftrightarrow\quad
>\operatorname{Ord}(\alpha)
>\land\exists f:\alpha\hookrightarrow X.
>$$
>
>**$B$ 本身是序数.** $B$ 的每个元素都是序数. 若 $\alpha\in B$ 且 $\gamma<\alpha$, 将单射 $\alpha\hookrightarrow X$ 限制到 $\gamma$, 就得到 $\gamma\hookrightarrow X$, 从而 $\gamma\in B$. 因此 $B$ 是传递的序数集合, 本身是序数.
>
>**$B$ 不能单射到 $X$.** 若存在单射 $B\hookrightarrow X$, 由刚刚证明的刻画便得到 $B\in B$, 与序数的性质矛盾.
>
>另一方面, 每个 $\gamma<B$ 都是 $B$ 的元素, 所以都能单射到 $X$. 因此 $B$ 正是最小的不能单射到 $X$ 的序数, 即 $h(X)$.

这里的 $B$ 本身才是 Hartogs 数, 不应再直接取 $\bigcup B$. 例如 $X=\varnothing$ 时, 只有序数 $0$ 能单射到 $X$, 所以 $B=\{0\}=1=h(\varnothing)$, 而 $\bigcup B=0$. 如果希望保留“取并”的表达, 则正确形式是
$$
h(X)=\bigcup\{\alpha+1:\alpha\hookrightarrow X\}.
$$

整个构造可以在 ZF 中统一表达为
$$
\begin{aligned}
\mathrm{ZF}\vdash\forall X\,\exists!B\,
\Bigl[
&\operatorname{Ord}(B)\\
&\land\forall\alpha\bigl(
\operatorname{Ord}(\alpha)\longrightarrow
(\alpha\in B\longleftrightarrow
\exists f:\alpha\hookrightarrow X)
\bigr)
\Bigr].
\end{aligned}
$$
因此, Hartogs 定理不需要先把 $X$ 良序化, 也不需要 AC. 在[不动点的超限迭代](#monotone-fixed-points)中, 取 $\kappa=h(\mathcal P(A))$ 就能给出严格递降过程无法一直持续的序数长度上界.

相关定理可参考 [Moosa, *Set Theory and Model Theory*, §1.7、Theorem 1.37 与 Proposition 2.6](https://www.math.uwaterloo.ca/~rmoosa/modeltheory-notes-v5.pdf). 这里的良序枚举与递降链论证保留了我自己的证明路线.

## 从具体集合到泛性质 {#sets-and-universal-properties}

### 一些关于 $A^B$ 和 $\prod_{b\in B}A$ 的 Idea {#products-and-exponentials}

这段讨论来自 [Chapter III 的 Sets of functions]({{< relref "posts/categoryThry/Chapter III - Interlude on sets.md" >}}#sets-of-functions). 在那里, 指数对象与任意多项积的泛性质已经分别给出.

我尝试只从泛性质出发证明 $\prod_{b\in B}A\cong A^B$, 却发现两种泛性质给出的数据并不直接相同. 对任意 $X$, 到 $\prod_{b\in B}A$ 的一条态射等价于分别给出一族态射 $f_b:X\to A$; 到 $A^B$ 的一条态射则等价于给出一条态射 $f:X\times B\to A$. 要证明这两个对象同构, 还需要说明“一族 $f_b$”与“一条 $f$”对每个 $X$ 都自然地对应. 这一步不能只靠两种构造各自的泛性质得到.

这让我想到数理逻辑中语法与模型的关系: 如果一个结论仅从某套公理推出, 它就应在这套公理的所有模型中成立. 这里用到的是 soundness 的方向. 类似地, 如果上面的同构仅由抽象的范畴泛性质推出, 那么它就应在每个具备相应构造的范畴中成立. 我所遇到的困难可能意味着: 在 $\mathbf{Set}$ 中把上述两种数据对应起来, 用到了集合特有的性质.

关键是分清 $B$ 的两种角色. 在 $\prod_{b\in B}A$ 中, $B$ 的元素充当**外部的索引**; 在指数对象 $A^B$ 中, $B$ 是范畴里的**对象**. 一般范畴的对象未必能直接当作索引集合, 所以若要比较两者, 必须先指定一套外部索引. 在 $\mathbf{Set}$ 中, 集合 $B$ 恰好也能用自己的元素作索引, 并且满足
$$
B\cong\coprod_{b\in B}1,\qquad
X\times B\cong\coprod_{b\in B}X.
$$
后一式说明: 一条 $X\times B\to A$ 的态射, 等价于从每一份 $X$ 各给出一条 $f_b:X\to A$ 的态射. 于是指数对象与以 $B$ 的元素为索引的积满足相同的泛性质, 从而自然同构. 这也可以具体写成 $h:B\to A$ 与函数值族 $(h(b))_{b\in B}$ 之间的对应.

这个额外条件在别的范畴中可以失败. 例如在偏序集和单调映射构成的范畴 $\mathbf{Pos}$ 中, 令 $A=B=\{0<1\}$. 若用 $B$ 的两个底层元素作外部索引, 两份 $A$ 的积 $A\times A$ 有四个元素; 但指数对象 $A^B$ 是由单调映射 $B\to A$ 按逐点序排列而成的偏序集, 只有三个元素, 分别由像 $(0,0)$、$(0,1)$、$(1,1)$ 决定, 因而二者不同构. 这里任意一族 $f_b:X\to A$ 未必能合成单调映射 $X\times B\to A$: 还必须满足由 $B$ 的顺序带来的相容条件.

因此, 我的怀疑是对的, 但需要说得更准确: **仅凭外部索引积与指数对象各自的泛性质, 不能推出它们同构**; 在 $\mathbf{Set}$ 中的说明还使用了 $B$ 是单点集之和, 以及积对这种和的分配. 如果把 $\prod_{b:B}A$ 理解为某种“内部的依赖积”, 那已经是另一种构造, 不能与这里按 $B$ 的元素作外部索引的积混为一谈.

## 子集、谓词与量词 {#predicates-and-quantifiers}

这段讨论接续 [Chapter II 习题 2.2.13]({{< relref "posts/categoryThry/Chapter II - Adjoints.md" >}}#2213) 中逆像函子的两个伴随, 将集合上的构造解释为逻辑中的代入与量化.

把一个子集 $A\subseteq K$ 看成谓词时,
$$
A(x)
\quad:\equiv\quad
x\in A.
$$
子集包含
$$
A\subseteq A'
$$
则表示谓词之间的蕴含: $A(x)$ 成立时, $A'(x)$ 也成立. 因此, 幂集偏序 $\mathcal P(K)$ 可以看成论域 $K$ 上全部谓词组成的偏序. 这里把子集看作谓词的语义外延, 并不要求每个子集都能在某个固定的一阶语言中定义.

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
\quad:\equiv\quad
B(f(x)).
$$
因此, $f^*$ 可以理解为沿着 $f$ 进行代入. 元素沿 $f$ 从 $K$ 进入 $L$, 而谓词则沿相反方向从 $L$ 被拉回到 $K$.

[Chapter II 习题 2.2.13]({{< relref "posts/categoryThry/Chapter II - Adjoints.md" >}}#2213) 中构造的左伴随 $L_f$ 可以记为 $\exists_f$. 对于 $A\subseteq K$ 与 $y\in L$,
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
p^*(S)(x,y):\equiv S(x),
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

## Cantor–Bernstein 的层垒证明 {#cantor-bernstein}

这是我在学习 [Chapter III 的 Cantor–Bernstein 定理]({{< relref "posts/categoryThry/Chapter III - Interlude on sets.md" >}}#cantorbernstein) 时给出的证明. 先记录结论, 再说明具体构造与它所依赖的假设.

>[!theorem] Theorem 3.2.1 (Cantor–Bernstein)
>设 $A,B$ 是集合. 如果 $|A|\leq|B|\leq|A|$, 那么 $A\cong B$.

证明的思路是在 $A,B$ 中分别构造交错嵌套的两列集合, 得到两侧的层垒结构. 然后在不同的层上分别使用 $f$ 与 $g^{-1}$, 将两侧的各层以及交集部分对应起来.

>[!proof]
>设 $f:A\to B$、$g:B\to A$ 都是单射. 在 $A$ 中递归定义
>$$
>\begin{aligned}
>\mathcal M_0&=A,&\mathcal M_{i+1}&=gf[\mathcal M_i],\\
>\mathcal K_0&=g[B],&\mathcal K_{i+1}&=gf[\mathcal K_i]
>\end{aligned}
>\qquad(i\in\mathbb N),
>$$
>其中 $gf=g\circ f$. 由归纳法可得
>$$
>\mathcal M_0\supseteq\mathcal K_0\supseteq\mathcal M_1\supseteq\mathcal K_1\supseteq\cdots.
>$$
>同样, 在 $B$ 中定义
>$$
>\begin{aligned}
>\widehat{\mathcal M}_0&=B,&\widehat{\mathcal M}_{i+1}&=fg[\widehat{\mathcal M}_i],\\
>\widehat{\mathcal K}_0&=f[A],&\widehat{\mathcal K}_{i+1}&=fg[\widehat{\mathcal K}_i],
>\end{aligned}
>$$
>得到交错包含关系
>$$
>\widehat{\mathcal M}_0\supseteq\widehat{\mathcal K}_0\supseteq\widehat{\mathcal M}_1\supseteq\widehat{\mathcal K}_1\supseteq\cdots.
>$$
>记
>$$
>\mathcal M_\omega=\bigcap_{i\in\mathbb N}\mathcal M_i,
>\qquad
>\widehat{\mathcal M}_\omega=\bigcap_{i\in\mathbb N}\widehat{\mathcal M}_i.
>$$
>由交错包含关系, $A$ 被分成 $\mathcal M_\omega$ 以及两类差集 $\mathcal M_i\setminus\mathcal K_i$、$\mathcal K_i\setminus\mathcal M_{i+1}$, 这些部分两两不交且覆盖 $A$. $B$ 侧也有相应的分割.
>
>单射 $g$ 给出反函数 $g^{-1}:g[B]\to B$. 定义
>$$
>\varphi:A\to B,\qquad
>\varphi(x)=
>\begin{cases}
>f(x),&x\in\mathcal M_\omega\ \text{或}\ (\exists i\in\mathbb N)\,x\in\mathcal M_i\setminus\mathcal K_i,\\
>g^{-1}(x),&(\exists i\in\mathbb N)\,x\in\mathcal K_i\setminus\mathcal M_{i+1}.
>\end{cases}
>$$
>这里第二类差集都包含在 $\mathcal K_0=g[B]$ 中, 所以 $g^{-1}$ 有定义.
>
>根据构造, 对每个 $i\in\mathbb N$ 都有
>$$
>\begin{aligned}
>f[\mathcal M_i]&=\widehat{\mathcal K}_i,
>&f[\mathcal K_i]&=\widehat{\mathcal M}_{i+1},\\
>g^{-1}[\mathcal K_i]&=\widehat{\mathcal M}_i,
>&g^{-1}[\mathcal M_{i+1}]&=\widehat{\mathcal K}_i.
>\end{aligned}
>$$
>因为 $f$ 与 $g^{-1}$ 都是单射, 它们保持差集, 因而
>$$
>\begin{aligned}
>f[\mathcal M_i\setminus\mathcal K_i]
>&=f[\mathcal M_i]\setminus f[\mathcal K_i]
>=\widehat{\mathcal K}_i\setminus\widehat{\mathcal M}_{i+1},\\
>g^{-1}[\mathcal K_i\setminus\mathcal M_{i+1}]
>&=g^{-1}[\mathcal K_i]\setminus g^{-1}[\mathcal M_{i+1}]
>=\widehat{\mathcal M}_i\setminus\widehat{\mathcal K}_i.
>\end{aligned}
>$$
>最后, 利用 $f$ 的单射性以及 $B$ 侧的交错包含关系, 有
>$$
>\begin{aligned}
>f[\mathcal M_\omega]
>&=f\!\left[\bigcap_{i\in\mathbb N}\mathcal M_i\right]
>=\bigcap_{i\in\mathbb N}f[\mathcal M_i]\\
>&=\bigcap_{i\in\mathbb N}\widehat{\mathcal K}_i
>=\bigcap_{i\in\mathbb N}\widehat{\mathcal M}_i
>=\widehat{\mathcal M}_\omega.
>\end{aligned}
>$$
>这里像与交集交换, 是因为单射保证同一元素在各层中的前像必定是同一个元素.
>
>因此, $\varphi$ 在各部分上都是单射, 其像恰好是 $B$ 中两类差集与交集部分, 两两不交且覆盖 $B$. 所以 $\varphi:A\to B$ 是双射.

这份证明可在经典 ZF 中完成, 不需要选择公理: 两列集合由递归唯一确定, $g^{-1}$ 的值也由唯一前像确定. 其中对各层及交集部分的分类使用了经典逻辑. 关于 Cantor–Bernstein 定理与排中律的关系, 可参考 [Pradic 与 Brown, *Cantor-Bernstein implies Excluded Middle*](https://arxiv.org/abs/1904.09193).

## 保序映射的不动点 {#monotone-fixed-points}

[Chapter III 习题 3.2.12(a)]({{< relref "posts/categoryThry/Chapter III - Interlude on sets.md" >}}#3212) 要求证明: 对任意关于包含关系保序的映射 $\theta:\mathcal P(A)\to\mathcal P(A)$, 存在 $S\subseteq A$ 使 $\theta(S)=S$. 教材提示从满足 $R\subseteq\theta(R)$ 的集合的并出发; 我先尝试了另一条路线.

### 第一次尝试

我先不使用教材给出的构造, 而是从 $A$ 出发, 递归定义
$$
A_0=A,\qquad A_{n+1}=\theta(A_n)\qquad(n\in\mathbb N).
$$
因为 $\theta(A)\subseteq A$, 再由保序性与归纳法得到
$$
A_0\supseteq A_1\supseteq A_2\supseteq\cdots.
$$
于是尝试取 $S_\omega=\bigcap_{n\in\mathbb N}A_n$. 但保序性只保证
$$
\theta(S_\omega)
\subseteq\bigcap_{n\in\mathbb N}\theta(A_n)
=\bigcap_{n\in\mathbb N}A_{n+1}
=S_\omega,
$$
其中可能出现严格包含. 如果 $\theta$ 额外保持这种递降可数交, 就能得到等号; 仅有保序性还不够.

我最初猜测 $A$ 可数时这一步就会稳定, 但这个猜测也需要修正.

>[!example] 可数集合上的反例
>取 $A=\mathbb N\cup\{\infty\}$, 按 $0<1<2<\cdots<\infty$ 排序. 定义
>$$
>\theta(X)=\{x\in X\mid\exists y\in X,\ y<x\}.
>$$
>也就是说, 对非空 $X$ 删除其最小元素, 并令 $\theta(\varnothing)=\varnothing$.

这个映射保序: 若 $X\subseteq Y$, 则 $X$ 中比 $x$ 小的元素在 $Y$ 中仍然存在. 从 $A$ 开始迭代得到
$$
A_n=\{n,n+1,\ldots\}\cup\{\infty\},
\qquad S_\omega=\{\infty\},
$$
而 $\theta(S_\omega)=\varnothing\subsetneq S_\omega$. 所以可数性不能保证自然数次迭代后取交就得到不动点.

### 修正: 超限延长

既然取交以后仍可能继续下降, 我就把这个交集作为下一阶段的起点, 再重复同样的过程. 用超限递归可以统一写成
$$
\begin{aligned}
A_0&=A,\\
A_{\alpha+1}&=\theta(A_\alpha),\\
A_\lambda&=\bigcap_{\beta<\lambda}A_\beta
\qquad(\lambda\text{ 为非零极限序数}).
\end{aligned}
$$
保序性保证整个序列递降. 接下来的问题是, 它需要延长多少步才能停止变化?

我原先想取一个比 $\mathcal P(A)$ 更大的基数作为序数长度, 比如将 $|\mathcal P(\mathcal P(A))|$ 视为初始序数. 在承认 AC 的背景中这是可行的; 如果希望去掉这一步的良序化假设, 可以使用 **Hartogs 定理**: 对每个集合 $X$, 存在不能单射到 $X$ 的序数, 最小的一个记为 $h(X)$. 这个定理可在 ZF 中证明, 不需要 AC.

取 $\kappa=h(\mathcal P(A))$, 将上面的递归定义到 $\kappa$.

>[!proof]
>若对所有 $\alpha<\kappa$ 都有 $A_{\alpha+1}\subsetneq A_\alpha$, 那么对任意 $\alpha<\beta<\kappa$,
>$$
>A_\beta\subseteq A_{\alpha+1}\subsetneq A_\alpha.
>$$
>因此所有 $A_\alpha$ 都不同, $\alpha\mapsto A_\alpha$ 给出单射 $\kappa\to\mathcal P(A)$, 与 Hartogs 数的定义矛盾. 所以存在 $\alpha<\kappa$ 使 $\theta(A_\alpha)=A_\alpha$.
>
>若 $F$ 是任意不动点, 由超限归纳始终有 $F\subseteq A_\beta$: 初始时 $F\subseteq A$; 后继时由保序性得到 $F=\theta(F)\subseteq\theta(A_\beta)$; 极限时取交即可. 所以稳定后得到的是最大不动点.

这条路线可以在 ZF 中完成, 但需要先建立序数、Hartogs 定理与超限递归等工具. 这些工具的说明和证明见 [超限归纳,良序与Hartogs](#transfinite-well-orders-hartogs), 其中 [Hartogs 数的构造](#hartogs-number) 不使用 AC.

### 优化: 取所有合法起点的交

回看递降过程, 每个阶段的集合 $X$ 都满足 $\theta(X)\subseteq X$. 反过来, 任意满足这个条件的 $X$ 都可以作为递降迭代的起点. 我把从 $X$ 出发的路径称为“路径 $X$”; 将路径 $X$ 和路径 $Y$“插到一起”, 是指取 $X\cap Y$ 作为新起点, 再从这里重新迭代.

因此, 需要验证的是合法起点对交集封闭. 这个性质成立, 而且可以推广到任意多个合法起点. 这让我想到, 不妨把所有合法起点都取交, 于是定义
$$
T=\{X\subseteq A\mid\theta(X)\subseteq X\},
\qquad S=\bigcap T.
$$
这里 $A\in T$, 所以 $T$ 非空. 下面直接利用 $S$ 在 $T$ 中的最小性证明它是不动点.

>[!proof]
>先取任意非空一族合法起点 $(X_i)_{i\in I}$, 令 $Z=\bigcap_{i\in I}X_i$. 对每个 $i\in I$, 有 $Z\subseteq X_i$, 因而
>$$
>\theta(Z)\subseteq\theta(X_i)\subseteq X_i.
>$$
>对所有 $i\in I$ 取交, 得到 $\theta(Z)\subseteq Z$, 所以交集仍是合法起点. 在 $\mathcal P(A)$ 中将空族的交约定为 $A$, 这个结论也包含空族的情形.
>
>特别地, 对 $T$ 中所有起点取交, 得到 $\theta(S)\subseteq S$, 所以 $S\in T$.
>
>再由保序性得到
>$$
>\theta(\theta(S))\subseteq\theta(S),
>$$
>所以 $\theta(S)\in T$. 根据 $S=\bigcap T$, 又有 $S\subseteq\theta(S)$, 从而 $\theta(S)=S$.
>
>每个不动点都属于 $T$, 因而都包含 $S$. 所以这个构造给出的是最小不动点.

这个证明不使用 AC, 也不需要先发展超限迭代理论. 它直接使用保序性与交集的最大下界性质; 将交集换成最大下界, 同一论证也适用于一般完备格. 这就是 Knaster–Tarski 定理的最小不动点构造.

因此, “把所有路径插到一起”可以准确理解为: 将所有合法起点取交, 再从这个交集出发迭代. 交集本身仍是合法起点; 进一步由它在 $T$ 中的最小性得到 $\theta(S)=S$, 所以这条新路径从一开始就已经稳定. 这个论证不需要预先证明每条路径最终都会稳定.

### 两条路线的共同点

两条路线都利用了同一个保持条件:
$$
\theta(X)\subseteq X
\quad\Longrightarrow\quad
\theta(\theta(X))\subseteq\theta(X).
$$
超限迭代不断取得更小的集合, 再用集合大小限制严格递降的长度; 直接交集则先取得 $T$ 的最小元素, 使得 $\theta(S)$ 无法再严格小于 $S$. 两者都先得到一个方向的包含, 再由稳定性或极值性质取得反向包含.

不过, 从 $A$ 向下迭代得到最大不动点, 而上述交集给出最小不动点. 两种构造可以配成下面两组:

| 所求对象 | 迭代构造 | 直接构造 |
| --- | --- | --- |
| 最小不动点 | 从 $\varnothing$ 向上迭代, 极限处取并 | $\bigcap\{X\subseteq A\mid\theta(X)\subseteq X\}$ |
| 最大不动点 | 从 $A$ 向下迭代, 极限处取交 | $\bigcup\{X\subseteq A\mid X\subseteq\theta(X)\}$ |

教材提示的正是第二行的直接构造. 例如 $\theta=\mathrm{id}$ 时, 最小不动点是 $\varnothing$, 最大不动点是 $A$. 这两种对偶构造可参考 [Knaster–Tarski 不动点定理的证明](https://www.cs.utexas.edu/~misra/Notes.dir/KnasterTarski.pdf).

在按包含关系定义箭头的偏序范畴中, $\varnothing$ 是始对象, $A$ 是终对象; 上面构造的 $S$ 则是 $T$ 这个偏序范畴的始对象. 因而最后的证明也是通过一个最小性的泛性质导出不动点性质.

先前的集合论学习给了我超限迭代与控制迭代长度的工具. 随后, 我从具体过程里提取出各阶段始终满足的条件, 再用这个条件直接刻画所求对象. 这个过程也说明, 从逐步构造转向泛性质, 可以通过研究构造中保持的性质来完成.
