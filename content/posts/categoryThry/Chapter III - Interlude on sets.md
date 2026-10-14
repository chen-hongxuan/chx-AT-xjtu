---
title: Chapter III - Interlude on sets
date: 2026-10-09
tags:
  - category-theory
math: true
draft: false
---

## 本章的问题

前两章已经多次使用集合与函数组成的范畴 $\mathbf{Set}$, 却没有说明集合和函数究竟如何被规定. 本章暂时放下新的范畴论构造, 先列出我们希望集合与函数满足的基本性质. 这里的重点不是把集合还原成某种更基本的对象, 而是说明我们能够对集合做哪些构造, 以及这些构造如何与函数相联系.

本章先讨论 $\mathbf{Set}$ 中的常见构造, 再区分小范畴与大范畴, 最后补充一些关于集合论基础的历史讨论.

## 本文的语言背景

我把我们实际进行数学思考时所依赖的对象、直觉和推理背景称为**意识宇宙**. 在明确写下某个形式系统之前, 我们已经能够在这个背景中谈论自然数、集合, 并进行数学推理. 这是本文理解形式化的出发点. 这里的意识宇宙指数学思考的背景; 下文的 Grothendieck 宇宙则是用于控制集合大小的数学概念, 两者需要区分.

一个**形式系统**规定了使用哪些符号、怎样组成合法的表达式、接受哪些公理, 以及允许怎样从已有表达式推出新的表达式. 这些属于语法层面的规定. 语义则通过解释, 把这些符号与背景中的某个数学结构联系起来, 使公式能够表达关于该结构的命题. 我们希望选取的公理和推理规则能够捕获其中一部分真理. 例如, PA 将大量通常的自然数论证形式化; 但一个命题能够在 PA 的语言中表达, 还不保证它能够在 PA 中被证明.

对于一个选定的形式系统 $T$, 在系统中使用公理和规则证明公式, 是对象层次的工作; 从外部研究 $T$ 的语言、证明以及模型, 则是相对于 $T$ 的元层次工作. 一个例子是归纳: 我们可以在 PA 中应用归纳公理模式证明算术结论, 也可以在外部对公式的结构或复杂度进行归纳, 证明关于语法对象的结论. 两者的研究对象与推理所处的位置不同.

这里还需要保留层次的相对性. 关于 PA 的元推理可以进一步在某个形式理论中实现, 例如在 ZFC 中定义公式和证明, 再研究 PA. 此时 ZFC 承担关于 PA 的元理论的角色; 当我们转而研究 ZFC 本身时, 它又成为对象理论. 因此, 意识宇宙说明我们开展数学活动的背景, 而“对象”和“元”还需要相对于当前研究的系统来区分.

**本文目前是在这个背景中进行非形式化、但受公理约束的范畴论研究.** 我们使用范畴公理、通常的数学推理, 以及讨论时明确接受的背景假设, 尚未将所有论证逐步写入一个指定的完整形式系统. 用对象与态射表达一个性质, 是将它翻译成范畴语言; 要把整段讨论形式化, 还需要固定相应的语言、公理与推理规则.

**除非另有说明, 这组贯穿全书的范畴论学习笔记默认当前意识宇宙承认普通集合论选择公理 $\mathrm{AC}$:** 任意由集合编号的非空集合族都存在选择函数. 本文的 $\mathbf{Set}$ 指当前背景中的集合与函数; 因而这项约定等价于 $\mathrm{AC}_{\mathbf{Set}}$, 即 $\mathbf{Set}$ 中每个满态射都存在右逆. 这一等价在下文的 [Choice](#choice) 部分说明.

按上面的用语, 这是描述当前意识宇宙中集合与函数所具有的一项性质的外部语句, 也是我们接受的一项额外假设. 单凭一般的范畴公理, 并不能推出这项存在性结论. 当我们把同样的语句列入一个形式理论的公理时, 它又成为那个对象理论中的公理. 其他范畴的 $\mathrm{AC}_{\mathcal C}$ 则需要分别判断; 同一个背景可以满足 $\mathrm{AC}_{\mathbf{Set}}$, 同时不满足 $\mathrm{AC}_{\mathbf{Grp}}$.

涉及大范畴的统一选择时, 仍需按 Chapter I 的讨论说明相应的选择原则或宇宙层级. 普通集合论选择公理本身不直接保证真类编号的选择; 更大的 Grothendieck 宇宙或类理论中的全局选择原则, 需要根据论证的范围另行说明.

我们也可以讨论接受不同假设的数学背景, 比如研究 $\mathrm{ZF}+\neg\mathrm{AC}$ 的模型. 将这些背景理解为不同的意识宇宙, 是我采用的哲学解释; 在具体推理中, 仍然需要说明当前接受哪些假设. 选择公理在这里表达的是选择函数的存在性, 并不要求人实际执行、描述或计算任意多次选择.

## Constructions with sets

直观地说, 集合是一群不带额外结构的元素, 函数 $f:A\to B$ 为 $A$ 的每个元素指定 $B$ 中的一个元素. 函数可以复合, 复合满足结合律, 每个集合也有恒等函数, 所以集合与函数构成范畴 $\mathbf{Set}$. 但只说“它是一个范畴”还不足以刻画 $\mathbf{Set}$: 其他许多范畴同样满足范畴公理. 因此, 接下来需要看 $\mathbf{Set}$ 还具有哪些特殊的对象和构造.

>[!example] The empty set
>空集 $\varnothing$ 不含任何元素.

对于任意集合 $B$, 从 $\varnothing$ 到 $B$ 的函数无需指定任何元素的像, 因而恰好有一个:
$$
\left|\mathbf{Set}(\varnothing,B)\right|=1.
$$
这就是说, $\varnothing$ 是 $\mathbf{Set}$ 的始对象. 反过来, 如果 $A$ 非空, 就不存在从 $A$ 到 $\varnothing$ 的函数, 因为 $A$ 中的元素在 $\varnothing$ 中没有可选的像.

>[!example] The one-element set
>取单点集 $1=\{*\}$.

对任意集合 $A$, 从 $A$ 到 $1$ 的函数只能把所有元素送到 $*$, 因而恰好有一个:
$$
\left|\mathbf{Set}(A,1)\right|=1.
$$
因此, $1$ 是 $\mathbf{Set}$ 的终对象.

从 $1$ 到集合 $B$ 的函数则不同: 它只需决定 $*$ 的像, 所以每个元素 $b\in B$ 恰好对应一个函数 $\widehat b:1\to B$, 其中 $\widehat b(*)=b$. 于是有一一对应
$$
B\cong\mathbf{Set}(1,B).
$$
这说明在 $\mathbf{Set}$ 中, “元素”可以理解为从单点集出发的态射. 本节后面的构造会继续用范畴的语言描述我们熟悉的集合与函数.

### 积与和的泛性质

本节先给出积与不交并的具体构造. 下面提前借用第五章将正式定义的泛性质, 从它们与其他集合之间的态射来重新描述这两个对象.

>[!example] 积与不交并的具体构造
>笛卡尔积 $A\times B$ 由有序对 $(a,b)$ 构成, 其中 $a\in A$、$b\in B$. 它带有投影 $p_A(a,b)=a$ 与 $p_B(a,b)=b$.
>
>不交并 $A+B$ 可取为 $\bigl(\{0\}\times A\bigr)\cup\bigl(\{1\}\times B\bigr)$. 它带有包含映射 $i_A(a)=(0,a)$ 与 $i_B(b)=(1,b)$.

>[!example] 积的泛性质
>设集合 $P$ 带有两个映射 $p_A:P\to A$ 与 $p_B:P\to B$. 我们要求: 对任意集合 $X$ 以及任意一对函数 $f:X\to A$、$g:X\to B$, 都存在唯一的函数 $h:X\to P$ 使得
>$$
>p_A\circ h=f,\qquad p_B\circ h=g.
>$$

换句话说, 对每个 $X$, 给出一个函数 $h:X\to P$, 就同时给出了函数 $p_A\circ h:X\to A$ 和 $p_B\circ h:X\to B$. 反过来, 任意指定这两个函数, 都会唯一确定一个这样的 $h$. 这里的两个函数可以分别指定, 不需要满足额外的条件.

上面的笛卡尔积 $A\times B$ 满足这一性质: 对给定的 $f,g$, 取 $h(x)=(f(x),g(x))$ 即可. 特别地, 令 $X=1$, 就看出 $P$ 的一个元素对应于 $A$ 中的一个元素与 $B$ 中的一个元素, 也就是一个有序对.

>[!example] 和的泛性质
>设集合 $C$ 带有两个映射 $i_A:A\to C$ 与 $i_B:B\to C$. 我们要求: 对任意集合 $X$ 以及任意一对函数 $f:A\to X$、$g:B\to X$, 都存在唯一的函数 $k:C\to X$ 使得
>$$
>k\circ i_A=f,\qquad k\circ i_B=g.
>$$

换句话说, 对每个 $X$, 给出一个函数 $k:C\to X$, 就同时给出了函数 $k\circ i_A:A\to X$ 和 $k\circ i_B:B\to X$. 反过来, 任意指定这两个函数, 都会唯一确定一个这样的 $k$.

上面的不交并 $A+B$ 满足这一性质: 只要分别在来自 $A$ 与来自 $B$ 的两份元素上按 $f,g$ 定义, 就得到唯一的 $k$. 如果改用普通并集 $A\cup B$, 那么 $A$ 与 $B$ 的公共元素可能被 $f,g$ 送到不同的位置, 此时这样的 $k$ 无法定义.

这里的“互动”指的是上述特定方向的态射, 而且对应要对每个 $X$ 成立, 并与 $X$ 上的态射复合相容. 积将两条从同一个 $X$ 出发的态射合成一条 $X\to P$; 和将两条指向同一个 $X$ 的态射合成一条 $C\to X$. 满足相同泛性质的对象, 连同相应的投影或包含映射, 在唯一同构的意义下相同.

### 任意多个集合的积与和

令 $I$ 是一个索引集, $(A_i)_{i\in I}$ 是一族集合. 上面的两项泛性质可以直接推广到这族集合, 不要求 $I$ 只有两个元素.

>[!example] 一族集合的积的泛性质
>一个积由集合 $P$ 以及每个 $i\in I$ 对应的投影 $p_i:P\to A_i$ 构成. 它满足: 对任意集合 $X$, 如果分别给定每个 $i\in I$ 上的函数 $f_i:X\to A_i$, 就存在唯一的函数 $h:X\to P$ 使
>$$
>p_i\circ h=f_i\qquad(i\in I).
>$$

在 $\mathbf{Set}$ 中, 可以取 $P=\prod_{i\in I}A_i$: 它的一个元素是在每个 $A_i$ 中各选一个元素所得到的族 $(a_i)_{i\in I}$. 此时唯一的 $h$ 由 $h(x)=(f_i(x))_{i\in I}$ 给出.

>[!example] 一族集合的和的泛性质
>一个和由集合 $C$ 以及每个 $i\in I$ 对应的包含映射 $j_i:A_i\to C$ 构成. 它满足: 对任意集合 $X$, 如果分别给定每个 $i\in I$ 上的函数 $g_i:A_i\to X$, 就存在唯一的函数 $k:C\to X$ 使
>$$
>k\circ j_i=g_i\qquad(i\in I).
>$$

在 $\mathbf{Set}$ 中, 可以取不交并 $C=\coprod_{i\in I}A_i$, 把它的元素写成带有来源标记的 $(i,a)$, 其中 $a\in A_i$. 此时 $j_i(a)=(i,a)$, 而唯一的 $k$ 由 $k(i,a)=g_i(a)$ 给出.

如果 $I=\varnothing$, 就没有需要指定的投影或包含映射. 积的条件变成“对每个 $X$, 恰有一个函数 $X\to P$”, 因而空族的积是终对象 $1$; 和的条件变成“对每个 $X$, 恰有一个函数 $C\to X$”, 因而空族的和是始对象 $\varnothing$.

### Sets of functions

教材接着讨论函数集 $A^B$, 并指出它可以看作以 $B$ 为索引的许多份 $A$ 的积. 这种说法需要谈到 $B$ 的每个元素以及相应的“第 $b$ 项”.

>[!example] 函数集的具体构造
>取 $E=\mathbf{Set}(B,A)$, 即所有函数 $B\to A$ 组成的集合, 并定义求值映射 $e:E\times B\to A$, $e(h,b)=h(b)$.

如果希望只从对象 $A,B$ 和态射出发刻画这种对象, 可以使用下面的泛性质.

>[!example] 指数对象的泛性质
>寻找一个集合 $E$ 及一条态射 $e:E\times B\to A$, 使得对于任意集合 $X$ 和态射 $f:X\times B\to A$, 都存在唯一的态射 $\widetilde f:X\to E$ 满足
>$$
>e\circ(\widetilde f\times 1_B)=f.
>$$
>满足这一性质的 $E$ 记为 $A^B$.

这里的 $\widetilde f\times1_B:X\times B\to E\times B$ 由积的泛性质确定: 它到 $E$ 的投影是 $\widetilde f$ 与 $X\times B\to X$ 的投影之复合, 到 $B$ 的投影则是 $X\times B\to B$ 的投影. 因此, 泛性质本身只使用对象、积、态射、复合与唯一性, 无需指定“取第 $b$ 项”的操作.

上面构造的函数集满足这一性质. 对给定的 $f:X\times B\to A$, 定义 $\widetilde f(x)$ 为函数 $b\mapsto f(x,b)$, 就得到所需的态射 $X\to E$; 泛性质中的等式又保证它是唯一的. 这里才使用元素来验证函数集确实满足泛性质.

所以, 对任意 $X$, 给出态射 $X\times B\to A$ 与给出态射 $X\to A^B$ 是自然地一一对应的. 这就是第 II 章中 currying 对应在 $\mathbf{Set}$ 里的具体含义.

#### 一些关于 $A^B$ 和 $\prod_{b\in B}A$ 的 Idea

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

### Digression on arithmetic

若有限集合 $A,B$ 分别有 $m,n$ 个元素, 那么 $A+B$、$A\times B$、$A^B$ 分别有 $m+n$、$mn$、$m^n$ 个元素. 这解释了这些运算记号, 以及用 $0$ 表示空集、$1$ 表示单点集的习惯.

算术规则在集合中对应于同构, 例如
$$
\begin{aligned}
A\times(B+C)&\cong(A\times B)+(A\times C),\\
A^{B+C}&\cong A^B\times A^C,\\
(A^B)^C&\cong A^{B\times C}.
\end{aligned}
$$
它们分别对应于积对和的分配、将 $B+C\to A$ 的函数拆成两个函数, 以及 currying. 这些同构对无限集合也成立.

### The two-element set

>[!example] 二元集与特征函数的具体构造
>取 $2=1+1=\{\mathrm{true},\mathrm{false}\}$. 对子集 $S\subseteq A$, 定义它的**特征函数**
>$$
>\chi_S:A\to2,\qquad
>\chi_S(a)=
>\begin{cases}
>\mathrm{true},&a\in S,\\
>\mathrm{false},&a\notin S.
>\end{cases}
>$$

反过来, 任意函数 $f:A\to2$ 都确定子集 $f^{-1}(\{\mathrm{true}\})\subseteq A$. 这两个过程互为逆, 因而
$$
\mathcal P(A)\cong2^A.
$$
也就是说, 给出 $A$ 的一个子集, 等价于给出一条态射 $A\to2$. 从逻辑的角度来看, 特征函数就是判断“$a\in S$”真假的二值谓词.

#### 幂集的泛性质

教材在这里直接给出的是子集与特征函数的一一对应. 结合指数对象的泛性质, 我们还可以进一步描述 $\mathcal P(A)$ 如何与任意集合 $X$ 互动.

>[!example] 幂集对象的泛性质
>固定集合 $A$. 寻找集合 $P$ 以及一个关系 $M\subseteq P\times A$, 使得对于任意集合 $X$ 及子集 $R\subseteq X\times A$, 都存在唯一的映射 $h:X\to P$ 满足
>$$
>(x,a)\in R\quad\Longleftrightarrow\quad(h(x),a)\in M
>\qquad(x\in X,\ a\in A).
>$$

在 $\mathbf{Set}$ 中, 取 $P=\mathcal P(A)$ 以及 $M=\{(S,a)\mid a\in S\}$. 对于给定的 $R$, 所需映射由 $h_R(x)=\{a\in A\mid(x,a)\in R\}$ 给出. 反方向则把映射 $h:X\to\mathcal P(A)$ 变成关系 $R_h=\{(x,a)\mid a\in h(x)\}$. 这些构造说明, 一条 $X\to\mathcal P(A)$ 的态射恰好记录了一个由 $X$ 参数化的子集族, 或者等价地记录了 $X$ 与 $A$ 之间的关系.

上述对应对 $X$ 是自然的, 也可以通过下面的一串对应看出来:
$$
\mathbf{Set}(X,\mathcal P(A))
\cong\mathbf{Set}(X,2^A)
\cong\mathbf{Set}(X\times A,2)
\cong\mathcal P(X\times A).
$$

### Equalizers

教材接着考虑一种由等式定义子集的方式: 给定两个函数, 取出它们相等的那一部分. 这一节先给出集合中的具体构造; 我们再补充它的泛性质, 将这种构造翻译成范畴的语言.

>[!example] 等化子的具体构造
>给定两个函数 $f,g:A\to B$, 定义集合
>$$
>E=\{a\in A\mid f(a)=g(a)\},
>$$
>以及包含映射 $i:E\to A$, $i(a)=a$. 这个集合连同包含映射称为 $f,g$ 的**等化子** (equalizer).

例如, 取 $f,g:\mathbb R\to\mathbb R$, 分别由 $f(x)=x^2$ 和 $g(x)=x$ 给出. 两个函数相等的地方恰好是 $0,1$, 因而上述构造给出 $E=\{0,1\}$.

如果要用范畴的语言描述这个构造, 就需要说明 $E$ 连同 $i$ 如何与其他态射互动.

>[!example] 等化子的泛性质
>给定范畴中的两条态射 $f,g:A\to B$. 一个等化子由对象 $E$ 及态射 $i:E\to A$ 构成, 满足
>$$
>f\circ i=g\circ i,
>$$
>并且对任意对象 $X$ 及态射 $h:X\to A$, 只要 $f\circ h=g\circ h$, 就存在唯一的态射 $\overline h:X\to E$ 使得
>$$
>i\circ\overline h=h.
>$$

也就是说, **任何使 $f,g$ 相等的态射, 都唯一地经过 $E$**. 第一条等式说明 $i$ 本身使 $f,g$ 相等; 后面的唯一分解说明所有具有这一性质的态射都能通过 $i$ 表达出来. 因此, 泛性质刻画的是 $E$ 与 $i$ 共同组成的结构.

在 $\mathbf{Set}$ 中, 上面的具体构造满足这一泛性质. 若 $f\circ h=g\circ h$, 则对每个 $x\in X$ 都有 $f(h(x))=g(h(x))$, 所以 $h(x)\in E$. 于是将同一条规则 $x\mapsto h(x)$ 的目标集合改为 $E$, 就得到所需的 $\overline h$. 包含映射 $i$ 又保证, 任何满足 $i\circ\overline h=h$ 的函数都只能如此取值, 因而分解是唯一的.

### Quotients

商集把等价的元素看作同一个元素. 教材在第 70 页给出它的具体构造, 并直接说明了它的泛性质.

>[!example] 商集的具体构造
>给定集合 $A$ 及其上的等价关系 $\sim$, 定义 $a\in A$ 的等价类
>$$
>[a]=\{a'\in A\mid a'\sim a\}.
>$$
>取所有等价类组成的集合
>$$
>A/{\sim}=\{[a]\mid a\in A\},
>$$
>并定义商映射 $p:A\to A/{\sim}$, $p(a)=[a]$.

商映射 $p$ 是满射, 并且 $p(a)=p(a')$ 当且仅当 $a\sim a'$. 例如, 在 $\mathbb Z$ 上规定 $m\sim n$ 当且仅当它们奇偶性相同, 得到的商集就只有两个元素: 偶数这一类与奇数这一类.

>[!example] 商集的泛性质
>给定集合 $A$ 及其上的等价关系 $\sim$. 寻找集合 $Q$ 及函数 $p:A\to Q$, 满足
>$$
>a\sim a'\quad\Longrightarrow\quad p(a)=p(a'),
>$$
>并且对任意集合 $B$ 及函数 $f:A\to B$, 只要
>$$
>a\sim a'\quad\Longrightarrow\quad f(a)=f(a'),
>$$
>就存在唯一的函数 $\overline f:Q\to B$ 使得
>$$
>\overline f\circ p=f.
>$$

也就是说, **知道商集如何映射到 $B$, 就等价于知道 $A$ 如何映射到 $B$, 同时要求这个映射不区分等价的元素**.

上面的具体构造满足这一泛性质: 对给定的 $f$, 定义 $\overline f([a])=f(a)$. 若 $[a]=[a']$, 就有 $a\sim a'$, 因而 $f(a)=f(a')$, 所以定义不依赖代表元的选择. 每个等价类都有代表元, 因此等式 $\overline f\circ p=f$ 又确定了 $\overline f$ 的所有取值, 保证了唯一性.

#### 完全范畴版本: 余等化子

上面的泛性质仍然谈到了元素和等价关系. 为了将它完全翻译成范畴的语言, 可以把关系本身编码成一个对象及两条态射.

>[!example] 等价关系的态射表示
>在 $\mathbf{Set}$ 中, 对 $A$ 上的等价关系 $\sim$, 取
>$$
>R=\{(a,a')\in A\times A\mid a\sim a'\},
>$$
>以及两个投影 $r_1,r_2:R\to A$, 定义为
>$$
>r_1(a,a')=a,\qquad r_2(a,a')=a'.
>$$

这样, “$f$ 不区分等价的元素”恰好等价于态射等式
$$
f\circ r_1=f\circ r_2.
$$
将这一改写代入商集的泛性质, 就得到下面的描述. 这里可以直接从一般范畴中的两条平行态射出发, 无需预先要求它们来自某个等价关系.

>[!example] 余等化子的泛性质
>给定范畴中的两条态射 $r_1,r_2:R\to A$. 一个**余等化子** (coequalizer) 由对象 $Q$ 及态射 $p:A\to Q$ 构成, 满足
>$$
>p\circ r_1=p\circ r_2,
>$$
>并且对任意对象 $B$ 及态射 $f:A\to B$, 只要 $f\circ r_1=f\circ r_2$, 就存在唯一的态射 $\overline f:Q\to B$ 使得
>$$
>\overline f\circ p=f.
>$$

这个泛性质只使用对象、态射、复合、相等与唯一性. 它说明: **任何使 $r_1,r_2$ 相等的态射, 都唯一地经过 $p$**. 对于上面由等价关系得到的两个投影, 商映射 $A\to A/{\sim}$ 正是它们在 $\mathbf{Set}$ 中的余等化子.

>[!example] $\mathbf{Set}$ 中余等化子的具体构造
>给定任意两条函数 $r_1,r_2:R\to A$, 令 $\approx$ 为 $A$ 上包含所有 $(r_1(x),r_2(x))$ ($x\in R$) 的最小等价关系. 取 $Q=A/{\approx}$, 并令 $p:A\to Q$ 为商映射.

这个构造给出 $r_1,r_2$ 的余等化子. 这里的等价关系用于实现这一泛性质; 抽象定义本身已经不需要元素或等价类.

余等化子是等化子的对偶: 把等化子定义中的全部箭头反向, 就得到余等化子的定义. 这一概念适用于一般范畴, 但给定的两条态射是否存在余等化子, 取决于所在的范畴. 教材在后面的 Definition 5.2.7 (第 128 页) 正式定义它, 并在 Example 5.2.9 (第 129 页) 说明 $\mathbf{Set}$ 中的具体构造; 此处作为“完全范畴版本”的拓展先行记录.

### Natural numbers

教材在第 71 页从熟悉的自然数集出发, 通过递归定义函数的能力描述它. 为了与前面的构造对应, 我们先补充一个通常集合论中的具体实现, 再记录它的泛性质. 这里约定 $0\in\mathbb N$.

>[!example] 自然数的具体构造
>在通常的 ZF 集合论中, 定义 $0=\varnothing$ 以及后继操作
>$$
>s(n)=n\cup\{n\}.
>$$
>这样得到 von Neumann 自然数
>$$
>0=\varnothing,\qquad 1=\{0\},\qquad 2=\{0,1\},\qquad 3=\{0,1,2\},\quad\ldots
>$$
>取 $\mathbb N=\omega$ 为满足 $0\in\omega$ 且在上述后继操作下封闭的最小集合, 并将后继操作限制为函数 $s:\mathbb N\to\mathbb N$. 记 $s(n)=n+1$.

这个集合的存在使用了无穷公理; 上述实现是我们的补充, 教材本段并不依赖这种具体编码. 接下来关心的是 $\mathbb N$、零与后继如何共同确定递归过程.

>[!example] 自然数的递归泛性质
>对任意集合 $X$、元素 $a\in X$ 以及函数 $r:X\to X$, 都存在唯一的函数 $h:\mathbb N\to X$ 满足
>$$
>h(0)=a,\qquad h\circ s=r\circ h.
>$$
>第二个条件也可以写成
>$$
>h(n+1)=r(h(n))\qquad(n\in\mathbb N).
>$$

也就是说, **给出一个起点和一个可反复执行的操作, 就唯一确定了一个由自然数索引的过程**. 这个过程依次取值为 $a,r(a),r(r(a)),\ldots$. 写作 $h(n)=r^n(a)$, 就得到所需的函数; 从起点逐步使用递归等式, 又可以看出它的取值是唯一确定的.

#### 完全范畴版本: 自然数对象

在 $\mathbf{Set}$ 中, 选定元素 $a\in X$ 等价于给出从单点集出发的函数 $a:1\to X$. 同样, 可以用 $z:1\to\mathbb N$ 表示选定零. 于是起点也能翻译成态射, 得到下面的描述.

>[!example] 自然数对象的泛性质
>设范畴 $\mathcal C$ 有终对象 $1$. 寻找对象 $N$ 及态射
>$$
>z:1\to N,\qquad s:N\to N,
>$$
>使得对于任意对象 $X$ 及态射 $a:1\to X$、$r:X\to X$, 都存在唯一的态射 $h:N\to X$ 满足
>$$
>h\circ z=a,\qquad h\circ s=r\circ h.
>$$
>满足这一性质的三元组 $(N,z,s)$ 称为**自然数对象** (natural numbers object); 此处采用的是无参数递归版本.

第一个等式要求 $h$ 保持起点, 第二个要求 $h$ 保持一步操作. 将带有起点和一步操作的三元组 $(X,a,r)$ 作为对象, 以保持这两项结构的态射作为态射, 就得到一个范畴; 上述泛性质恰好说明 $(N,z,s)$ 是其中的始对象. 因而它刻画的是整个三元组, 并将其确定到唯一的保持结构的同构.

#### 为什么 $z$ 从终对象出发?

零可以看作一个不需要输入的常量操作. 二元运算的输入对象是 $N\times N$, 一元运算的输入对象是 $N$, 而零元运算的输入对象是空积. 空积就是终对象, 所以零被表示为 $z:1\to N$.

这里的方向需要分清: 终对象的性质保证对任意 $X$ 恰有一条态射 $X\to1$, 并不要求 $1\to X$ 唯一. 在 $\mathbf{Set}$ 中, 后者恰好对应 $X$ 的各个元素. 对任意 $X$, 复合
$$
X\xrightarrow{!_X}1\xrightarrow{z}N
$$
给出一条常量态射, 在 $\mathbf{Set}$ 中就是常值为零的函数, 其中 $!_X$ 是到终对象的唯一态射.

在一般范畴中, 态射 $1\to X$ 称为 $X$ 的**全局元素**. 它推广了集合中的元素概念. 即使对象带有底层集合, 全局元素也未必对应全部底层元素. 例如, 在 $\mathbf{Grp}$ 中终对象是平凡群, 而从平凡群到群 $G$ 只有一条同态, 它只能选出单位元.

因此, 换到其他范畴时, 同样的态射条件可能发生退化. 按上面的无参数递归版本, 在 $\mathbf{Grp}$ 中取 $N=1$、$z=s=\mathrm{id}_1$ 就已经满足要求: 每个 $a:1\to G$ 都是唯一的单位元同态, 且任意自同态 $r:G\to G$ 都满足 $r\circ a=a$, 因而唯一的 $h=a$ 满足两个等式. 所以这套泛性质在一般范畴中的含义, 还取决于该范畴允许哪些起点与操作; 这里不讨论更强的带参数递归要求.

#### 在 $\mathbf{Set}$ 中, 后继为什么不会成环?

如果 $(N,z,s)$ 在 $\mathbf{Set}$ 中满足上述泛性质, 那么 $s$ 不可能有环, 即不存在 $x\in N$ 及正整数 $k$ 使 $s^k(x)=x$.

>[!proof]
>取上面具体构造的自然数集作为测试对象 $X=\mathbb N$, 起点为 $0$, 一步操作为 $r(m)=m+1$. 泛性质保证存在 $h:N\to\mathbb N$, 满足 $h\circ s=r\circ h$. 反复使用这一等式得到
>$$
>h(s^k(x))=h(x)+k.
>$$
>若 $s^k(x)=x$ 且 $k>0$, 就有 $h(x)=h(x)+k$, 矛盾. 因而 $s$ 不可能成环, 无论这个环是否能够从起点到达.

这里仅用了泛性质的存在性: 如果 $s$ 有环, 就无法向上面这个测试对象给出保持一步操作的函数. 关键在于泛性质要求对**任意** $X,a,r$ 都成立.

目标中的操作 $r$ 则允许有环. 例如取 $X=\{0,1\}$, 起点为 $0$, 并令 $r$ 交换 $0,1$, 就得到 $h(n)=n\bmod2$. 自然数能够记录周期过程, 而自身的后继操作不会成环.

### Choice

#### 教材中的选择公理 $\mathrm{AC}_{\mathbf{Set}}$

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

#### 满态射与其他范畴中的“选择公理”

“满射”的通常定义涉及集合中的元素. 如果希望将上述断言翻译成只使用态射的语言, 就需要引入满态射.

>[!definition] Epimorphism / 满态射
>在范畴 $\mathcal C$ 中, 态射 $f:X\to Y$ 称为**满态射** (epimorphism), 如果对任意对象 $Z$ 及任意两条态射 $u,v:Y\to Z$, 都有
>$$
>u\circ f=v\circ f\quad\Longrightarrow\quad u=v.
>$$
>也就是说, $f$ 满足右消去律.

在 $\mathbf{Set}$ 中, 满态射恰好就是满射. 这个对应本身不需要选择公理.

>[!proof]
>若 $f:X\to Y$ 满射且 $u\circ f=v\circ f$, 那么对任意 $y\in Y$, 存在 $x\in X$ 使 $f(x)=y$, 从而
>$$
>u(y)=u(f(x))=v(f(x))=v(y).
>$$
>所以 $u=v$, 即 $f$ 是满态射. 这里仅对任意给定的 $y$ 使用原像的存在性, 没有同时选定所有原像.
>
>反过来, 若 $f$ 不满射, 取 $y_0\in Y\setminus f(X)$. 定义 $u,v:Y\to\{0,1\}$, 其中 $u$ 恒为 $0$, 而 $v$ 在 $f(X)$ 上为 $0$, 在它的补集上为 $1$. 此时 $u\circ f=v\circ f$, 但 $u(y_0)\ne v(y_0)$, 所以 $f$ 不是满态射.

因此, $\mathrm{AC}_{\mathbf{Set}}$ 等价于下面的完全范畴化表述:
$$
\mathbf{Set}\text{ 中每个满态射都存在右逆}.
$$
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

#### 与 Chapter I 的选择公理相联系

前面在 [Chapter I 的“关于选择公理与大范畴”]({{< relref "posts/categoryThry/Chapter I - Categories, functors and natural transformations.md" >}}#关于选择公理与大范畴) 中, 为构造等价函子的拟逆, 使用了背景中的选择原则. 如果谈的是普通的集合论选择公理, 它可以写成下面的形式.

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

回到 Chapter I, 设 $F:\mathcal C\to\mathcal D$ 是 full、faithful 且 essentially surjective 的函子. 对每个 $d\in\mathcal D$, 要选定一个对象 $c_d$ 及同构
$$
\epsilon_d:F(c_d)\xrightarrow{\sim}d,
$$
然后令 $G(d)=c_d$. 当两个范畴都是小范畴时, 每个 $d$ 对应的候选对 $(c_d,\epsilon_d)$ 组成非空集合, 所有这些候选集合又由集合 $\operatorname{Ob}(\mathcal D)$ 编号, 因而普通 $\mathrm{AC}$ 足够. 一旦选好这些数据, $G$ 在态射上的定义由 full 与 faithful 唯一确定, 不需要再作选择.

Chapter I 还说明了反方向: 如果对所有小范畴都断言这样的函子有拟逆, 就能为任意非空集合族构造选择函数. 因而在通常的 ZF 背景下, 有
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

##### 选择范围更小: 有限或可数编号

所谓“更低层面的选择”, 可以指只允许对某些范围的集合族作选择. 例如, 有限多个非空集合可以同时选择, 这在 ZF 中已经能够证明; 如果只接受可数选择, 就只保证由可数集合编号的非空集合族有选择函数.

这些限制对应于满射的目标集合大小: 有限的目标集合只需要有限次选择, 可数的目标集合只需要可数选择. 因此, $\mathbf{FinSet}$ 中每个满态射都有右逆可以在 ZF 中证明, 却不能由此推出整个 $\mathbf{Set}$ 的 $\mathrm{AC}_{\mathbf{Set}}$. 可数选择也不保证任意大小的满射都有右逆.

同样, 在 Chapter I 的构造中, 如果候选集合确实都是集合, 且 $\operatorname{Ob}(\mathcal D)$ 有限或可数, 相应范围的选择就足够. 只接受这些较弱原则, 还不能得到对所有小范畴都成立的等价结论. 这里“有限次选择”指索引集有限, 不应与“从任意多的非空有限集合中同时选择”混淆.

##### 宇宙层级更高: 较大集合与真类

“更高或更低”也可以指所讨论集合的大小层级. 这与上面限制索引集有限或可数是两个不同的问题.

例如, 固定两个 Grothendieck 宇宙 $\mathcal U\in\mathcal V$, 并用 $\mathbf{Set}_{\mathcal U}$、$\mathbf{Set}_{\mathcal V}$ 分别表示相应范围内的集合与函数. 在较大宇宙 $\mathcal V$ 中接受普通选择公理, 就能为 $\mathcal U$ 中的满射选取右逆. 而且这个右逆仍属于 $\mathcal U$: 若 $f:X\to Y$ 的 $X,Y$ 都在 $\mathcal U$ 中, 则右逆的图是 $Y\times X$ 的子集, 由 Grothendieck 宇宙的闭包性质, 它也在 $\mathcal U$ 中.

因此, 对这样的宇宙层级, 较大范围内的选择能够保证较小范围内的 $\mathrm{AC}_{\mathbf{Set}_{\mathcal U}}$. 但只接受 $\mathcal U$ 范围内的选择, 并不自动保证 $\mathcal V$ 范围内的选择, 也不能直接完成 $\mathcal U$ 外的大族选择. 这里使用了 Grothendieck 宇宙的闭包性质, 不能不加限定地推广到任意两个集合论模型.

这正是 Chapter I 中处理大范畴的一种方式: $\mathbf{Set}_{\mathcal U}$ 的全部对象相对于 $\mathcal U$ 不组成小集合, 但在 $\mathcal V$ 中组成集合, 因而可以使用较大范围内的选择公理. 存在这样的 Grothendieck 宇宙层级本身是额外的基础假设, 不能由普通选择公理单独得到.

如果直接在类理论中处理真类编号的选择, 则还需要相应的类选择原则. 例如, **Global Choice** 可以表述为: 存在一个类函数, 为每个非空集合指定其中的一个元素. 在合适的类理论背景中, 它推出普通集合选择, 也能支持 Chapter I 中对大范畴的对象及同构作统一选择. 但普通 $\mathrm{AC}$ 或 $\mathrm{AC}_{\mathbf{Set}}$ 本身不直接提供这套类层面的选择.

因此, 讨论不同选择原则时, 我们需要分别说明**选择的集合族范围、所使用的集合宇宙层级, 以及命题针对的范畴**. 单凭“对象层次”或“元层次”的名称, 不能判断它们的强弱. 即使接受全局选择, 也不会使所有范畴的满态射都有右逆; 上面的 $\mathbf{Grp}$ 反例仍然存在.

关于小范畴的等价判据与满态射, 可分别参考 [Stacks Project 的等价判据](https://stacks.math.columbia.edu/tag/02C3) 与 [满态射的定义](https://stacks.math.columbia.edu/tag/003A); 宇宙层级及类选择的讨论可参考 [Mike Shulman, *Set theory for category theory*, §7–8](https://arxiv.org/abs/0810.1279).

## Small and large categories

比较集合的大小时, 我们规定 $|A|\leq|B|$ 表示存在单射 $A\to B$, 而 $|A|=|B|$ 表示存在双射 $A\to B$. Cantor–Bernstein 定理说明, 两个集合能够互相单射, 就足以保证它们之间存在双射.

恒等映射与单射的复合说明这个比较自反且传递. 它在集合上是预序: 互相不大于只保证同构, 不保证两个集合相等. 记 $|A|<|B|$ 表示 $|A|\leq|B|$ 且 $|A|\ne|B|$; 由 Cantor–Bernstein 定理, 有 $|A|\leq|B|<|C|\Rightarrow|A|<|C|$.

### Cantor–Bernstein

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

### Cantor's theorem

>[!theorem] Theorem 3.2.2 (Cantor)
>对任意集合 $A$, 都有 $|A|<|\mathcal P(A)|$.

>[!proof]
>映射 $a\mapsto\{a\}$ 是单射, 所以 $|A|\leq|\mathcal P(A)|$. 任取 $f:A\to\mathcal P(A)$, 令
>$$
>D=\{a\in A\mid a\notin f(a)\}.
>$$
>若 $f$ 满射, 则存在 $a_0\in A$ 使 $f(a_0)=D$, 从而
>$$
>a_0\in D\iff a_0\notin f(a_0)\iff a_0\notin D,
>$$
>矛盾. 所以不存在从 $A$ 到 $\mathcal P(A)$ 的满射, 更不存在双射.

因此, 对每个集合 $A$, 都存在集合 $B$ 使 $|A|<|B|$: 取 $B=\mathcal P(A)$ 即可. 这就是 Corollary 3.2.3, 也就是说, **不存在最大的集合大小**.

### 集合的同构类型

>[!theorem] Proposition 3.2.4
>设 $I$ 是集合, $(A_i)_{i\in I}$ 是一族集合. 则存在集合 $X$, 与每个 $A_i$ 都不同构.

>[!proof]
>令
>$$
>S=\coprod_{i\in I}A_i,\qquad X=\mathcal P(S).
>$$
>对任意 $j\in I$, 不交并的包含映射 $A_j\to S$ 是单射. 再由 Cantor 定理得到
>$$
>|A_j|\leq|S|<|\mathcal P(S)|=|X|,
>$$
>所以 $A_j\not\cong X$.

这里的 $I$ 可以是任意集合, 允许不可数多项. 因而, **任何由集合编号的清单, 都无法列尽全部集合的同构类型**. 这为接下来区分小范畴与大范畴提供了依据.

### 类、小范畴与局部小范畴

作者非正式地用 **class** (类) 表示一批数学对象. 能组成集合的类称为 **small**, 否则称为 **large**. 任意一个集合都是小的, 包括不可数集合; 全体集合构成的类则是大的. 这里暂未建立完整的类理论, 大小仍相对于当前的集合论背景而言.

>[!definition] Small / locally small
>范畴 $\mathcal C$ 称为**小范畴**, 如果它的全体态射组成一个集合; 否则称为**大范畴**.
>
>范畴 $\mathcal C$ 称为**局部小范畴**, 如果对任意两个固定对象 $A,B$, 态射类 $\mathcal C(A,B)$ 都是集合.

小范畴一定局部小, 其对象也组成集合, 因为每个对象对应自己的恒等态射. 严格来说, 只有在局部小的情况下, 才能将 $\mathcal C(A,B)$ 称为 hom-set; 许多作者直接把局部小性作为范畴定义的一部分.

反过来, **对象组成集合且局部小, 就能推出范畴小**.

>[!proof]
>若 $\operatorname{Ob}(\mathcal C)$ 是集合, 且每个 $\mathcal C(A,B)$ 都是集合, 那么将态射连同其定义域和值域记录下来, 全体态射可写成由集合编号的不交并
>$$
>\coprod_{(A,B)\in\operatorname{Ob}(\mathcal C)^2}\mathcal C(A,B),
>$$
>所以它们组成集合.

同样, 一个范畴有限, 当且仅当其对象有限, 且每两个对象之间的态射都只有有限多个.

Examples 3.2.5–3.2.6 中, $\mathbf{Set}$ 局部小, 因为固定 $A,B$ 后, 所有函数 $A\to B$ 组成函数集 $B^A$. $\mathbf{Vect}_k,\mathbf{Grp},\mathbf{Ab},\mathbf{Ring},\mathbf{Top}$ 也都局部小: 保持相应结构的映射, 构成底层函数集的子集. 但 $\mathbf{Set}$ 的对象无法组成集合, 所以它是一个局部小的大范畴.

### 本质小范畴

>[!definition] Essentially small
>如果范畴 $\mathcal C$ 等价于某个小范畴, 就称 $\mathcal C$ 是**本质小范畴**.

>[!example] 标准有限集合组成的范畴 (Example 3.2.7)
>对 $n\in\mathbb N$, 取标准有限集合 $[n]=\{0,\ldots,n-1\}$, 其中 $[0]=\varnothing$. 以这些集合为对象, 以它们之间的所有函数为态射, 得到 $\mathbf{FinSet}$ 的满子范畴 $\mathcal B$.

$\mathcal B$ 的对象由 $\mathbb N$ 编号, 每个 hom-set 又是有限集, 所以 $\mathcal B$ 是小范畴. 每个有限集合都同构于某个 $[n]$, 因而包含函子 $\mathcal B\to\mathbf{FinSet}$ 满、忠实且本质满. 按照 Chapter I 的等价判据及相应选择约定, 有 $\mathcal B\simeq\mathbf{FinSet}$. 所以 $\mathbf{FinSet}$ 本质小, 尽管全体有限集合本身组成大类.

如果 $\mathcal C$ 本质小, 取等价函子 $E:\mathcal B\to\mathcal C$, 其中 $\mathcal B$ 小. 那么 $(E(B))_{B\in\operatorname{Ob}(\mathcal B)}$ 就是一族由集合编号的对象, 涵盖 $\mathcal C$ 的全部同构类型. 这个表述避免把可能过大的同构类本身当作集合的元素.

>[!theorem] Proposition 3.2.8
>$\mathbf{Set}$ 不是本质小范畴.

>[!proof]
>若 $\mathbf{Set}$ 等价于小范畴 $\mathcal B$, 则等价函子的像给出一族由集合 $\operatorname{Ob}(\mathcal B)$ 编号的集合, 涵盖全部集合的同构类型. 这与 Proposition 3.2.4 矛盾.

### 其他非本质小范畴

Example 3.2.9 说明, 对任意域 $k$, $\mathbf{Vect}_k$ 也不是本质小范畴. 这里使用自由函子与遗忘函子的伴随 $F\dashv U$.

>[!proof]
>任取由集合 $I$ 编号的向量空间族 $(V_i)_{i\in I}$, 令
>$$
>S=\mathcal P\!\left(\coprod_{i\in I}U(V_i)\right).
>$$
>由 Cantor 定理, 对每个 $i$ 都有 $|U(V_i)|<|S|$. 自由向量空间 $F(S)$ 自带由 $S$ 编号的一组基, 所以 unit $\eta_S:S\to U(F(S))$ 是单射. 因而
>$$
>|U(V_i)|<|S|\leq|U(F(S))|.
>$$
>向量空间同构必然给出底层集合的双射, 所以 $F(S)$ 与每个 $V_i$ 都不同构. 因此任何由集合编号的向量空间族都不能涵盖全部同构类型, $\mathbf{Vect}_k$ 不是本质小范畴.

同样, $\mathbf{Grp},\mathbf{Ab},\mathbf{Ring},\mathbf{Top}$ 都不是本质小范畴. 统一的论证见习题 3.2.14: 若 $U:\mathcal C\to\mathbf{Set}$ 有左伴随, 且某个 $U(C_0)$ 至少含两个元素, 习题 2.3.11 就保证 unit $S\to U(F(S))$ 是单射, 从而可以重复上述大小比较.

### 小范畴组成的范畴

>[!definition] Definition 3.2.10
>以小范畴为对象、函子为态射的范畴记为 $\mathbf{Cat}$.

教材先前用 $\mathbf{CAT}$ 表示更一般的范畴与函子组成的范畴. 使用“所有范畴”这样的说法时, 仍按 Chapter I 的类与宇宙层级约定理解其大小.

>[!example] 幺半群对应的单对象小范畴 (Example 3.2.11)
>给定幺半群 $M$, 构造只有一个对象 $*$ 的范畴, 令 $\operatorname{Hom}(*,*)=M$, 以乘法为复合, 单位元为恒等态射. 反过来, 单对象小范畴的全体自态射在复合下构成一个幺半群.

这两种构造把幺半群同态与函子对应起来. 因此, 若 $\mathcal M$ 是 $\mathbf{Cat}$ 中由单对象小范畴组成的满子范畴, 则有
$$
\mathbf{Mon}\simeq\mathcal M.
$$
这里“小”保证 $\operatorname{Hom}(*,*)$ 确实是集合, 从而符合通常对幺半群的定义; 单对象条件本身不保证范畴小.

## Exercise

### 3.1.1

>[!exercise]
>对角函子 $\Delta:\mathbf{Set}\to\mathbf{Set}\times\mathbf{Set}$ 在对象上由 $\Delta(S)=(S,S)$ 给出. 构造 $\Delta$ 的左伴随和右伴随.

>[!proof]
>先找 $\Delta$ 的左伴随. 固定 $U=(U_1,U_2)\in\mathbf{Set}\times\mathbf{Set}$. 按照伴随的始对象刻画, 我们要找集合 $F(U)$ 和态射
>$$
>\eta_U:U\to\Delta F(U),
>$$
>使得任意 $f:U\to\Delta S$ 都唯一地写成 $\Delta(f')\circ\eta_U$, 其中 $f':F(U)\to S$.
>
>取 $F(U)=U_1+U_2$, 令 $\iota_i:U_i\to U_1+U_2$ 为不交并的两个包含映射, 并取 $\eta_U=(\iota_1,\iota_2)$. 任意 $f:U\to\Delta S$ 是一对函数 $f_1:U_1\to S$、$f_2:U_2\to S$. 上述分解条件就是
>$$
>f'\circ\iota_1=f_1,\qquad f'\circ\iota_2=f_2.
>$$
>和的泛性质恰好给出唯一的 $f'=[f_1,f_2]:U_1+U_2\to S$. 因此 $(F(U),\eta_U)$ 是 $(U^*\Rightarrow\Delta)$ 的始对象.
>
>对于态射 $g=(g_1,g_2):U\to V$, 由和的泛性质定义唯一的 $F(g):F(U)\to F(V)$, 使
>$$
>F(g)\circ\iota_i^U=\iota_i^V\circ g_i\qquad(i=1,2).
>$$
>唯一性保证 $F$ 保持恒等态射与复合, 而这两个等式也正是 $\eta$ 的自然性条件. 于是由 Theorem 2.3.6 得到 $F\dashv\Delta$.
>
>再找 $\Delta$ 的右伴随. 固定 $V=(A,B)\in\mathbf{Set}\times\mathbf{Set}$. 对偶地, 我们要找集合 $R(V)$ 和态射 $\varepsilon_V:\Delta R(V)\to V$, 使得任意 $f:\Delta S\to V$ 都唯一地写成 $\varepsilon_V\circ\Delta(f')$, 其中 $f':S\to R(V)$.
>
>取 $R(V)=A\times B$, 令 $\pi_A:A\times B\to A$、$\pi_B:A\times B\to B$ 为投影, 并取 $\varepsilon_V=(\pi_A,\pi_B)$. 任意 $f:\Delta S\to V$ 是一对函数 $f_A:S\to A$、$f_B:S\to B$. 分解条件就是
>$$
>\pi_A\circ f'=f_A,\qquad\pi_B\circ f'=f_B.
>$$
>积的泛性质恰好给出唯一的 $f'=\langle f_A,f_B\rangle:S\to A\times B$. 因此 $(R(V),\varepsilon_V)$ 是 $(\Delta\Rightarrow V^*)$ 的终对象.
>
>对于态射 $h=(h_A:A\to A',h_B:B\to B')$, 定义
>$$
>R(h)=\langle h_A\circ\pi_A,\,h_B\circ\pi_B\rangle:A\times B\to A'\times B'.
>$$
>积的唯一性保证 $R$ 是函子, $\varepsilon$ 是自然变换, 从而 $\Delta\dashv R$. 综上,
>$$
>(+)\dashv\Delta\dashv(\times).
>$$

### 3.2.12

>[!exercise]
>(a) 设 $\theta:\mathcal P(A)\to\mathcal P(A)$ 关于包含关系保序. 考虑
>$$
>S=\bigcup_{\substack{R\subseteq A\\R\subseteq\theta(R)}}R,
>$$
>证明 $\theta$ 至少有一个不动点, 即存在 $S\subseteq A$ 满足 $\theta(S)=S$.
>
>(b) 给定函数 $f:A\to B$、$g:B\to A$, 利用 (a) 证明存在 $S\subseteq A$, 使得
>$$
>g[B\setminus f[S]]=A\setminus S.
>$$
>
>(c) 推出 Cantor–Bernstein 定理.

正文已经给出层垒证明; 这道题提供从保序映射的不动点出发的另一条路线. (b) 中的 $f,g$ 不要求单射, 在 (c) 中才应用到互相单射的情形.

#### (a) 从递降迭代到交集构造

##### 第一次尝试

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

##### 修正: 超限延长

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

这条路线可以在 ZF 中完成, 但需要先建立序数、Hartogs 定理与超限递归等工具. 关于 Hartogs 定理可参考 [集合论讲义的 Theorem 7.28](https://people.maths.ox.ac.uk/~bays/teaching/b1set/B1.2.pdf).

##### 优化: 取所有单向稳定集合的交

回看递降过程, 每个阶段的集合 $X$ 都满足 $\theta(X)\subseteq X$. 这让我想到, 可以从所有满足这个条件的集合出发, 将它们一起取交. 于是定义
$$
T=\{X\subseteq A\mid\theta(X)\subseteq X\},
\qquad S=\bigcap T.
$$
这里 $A\in T$, 所以 $T$ 非空. 下面直接利用 $S$ 在 $T$ 中的最小性证明它是不动点.

>[!proof]
>对任意 $X\in T$, 有 $S\subseteq X$, 因而
>$$
>\theta(S)\subseteq\theta(X)\subseteq X.
>$$
>对所有 $X\in T$ 取交, 得到 $\theta(S)\subseteq S$, 所以 $S\in T$.
>
>再由保序性得到
>$$
>\theta(\theta(S))\subseteq\theta(S),
>$$
>所以 $\theta(S)\in T$. 根据 $S=\bigcap T$, 又有 $S\subseteq\theta(S)$, 从而 $\theta(S)=S$.
>
>每个不动点都属于 $T$, 因而都包含 $S$. 所以这个构造给出的是最小不动点.

这个证明不使用 AC, 也不需要先发展超限迭代理论. 它直接使用保序性与交集的最大下界性质; 将交集换成最大下界, 同一论证也适用于一般完备格. 这就是 Knaster–Tarski 定理的最小不动点构造.

我原先“把所有路径交起来”的想法, 在这里被改写为对所有满足 $\theta(X)\subseteq X$ 的集合取交. 不需要再断言两条迭代路径逐点相交后仍是迭代路径: 保序性仅保证 $\theta(X\cap Y)\subseteq\theta(X)\cap\theta(Y)$, 不保证等号.

##### 两条路线的共同点

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

### 3.2.13

>[!exercise]
>(a) 对函数 $f:A\to\mathcal P(A)$, 考虑 $\{a\in A\mid a\notin f(a)\}$, 证明 $f$ 不是满射.
>
>(b) 推出 Cantor 定理: $|A|<|\mathcal P(A)|$.

证明见正文 Cantor's theorem 部分.

### 3.2.14

>[!exercise]
>(a) 设 $U:\mathcal C\to\mathbf{Set}$ 有左伴随, 且存在 $C_0\in\mathcal C$ 使 $U(C_0)$ 至少有两个元素. 证明: 对任意集合 $I$ 及对象族 $(C_i)_{i\in I}$, 都存在 $\mathcal C$ 中的对象, 与每个 $C_i$ 都不同构. 提示: 使用习题 2.3.11.
>
>(b) 推出这样的 $\mathcal C$ 不是本质小范畴.
>
>(c) 推出 $\mathbf{Set},\mathbf{Vect}_k,\mathbf{Grp},\mathbf{Ab},\mathbf{Ring},\mathbf{Top}$ 都不是本质小范畴.

### 3.2.15

>[!exercise]
>判断下列范畴是否小、是否局部小:
>
>(a) 幺半群范畴 $\mathbf{Mon}$;
>
>(b) 将整数群 $\mathbb Z$ 视为单对象范畴;
>
>(c) 将整数有序集 $\mathbb Z$ 视为范畴;
>
>(d) 小范畴组成的范畴 $\mathbf{Cat}$;
>
>(e) 全体基数在乘法下构成的单对象范畴.

最后一项的唯一对象以全体基数为自态射, 复合为基数乘法, 恒等态射为基数 $1$. 此处允许自态射构成大类.

### 3.2.16

>[!exercise]
>设 $O:\mathbf{Cat}\to\mathbf{Set}$ 将小范畴映到其对象集. 构造函子 $C,D,I$, 给出伴随链
>$$
>C\dashv D\dashv O\dashv I.
>$$
