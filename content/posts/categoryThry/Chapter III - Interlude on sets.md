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

## 本章的背景约定

本章在通常的数学背景中讨论集合与函数, $\mathbf{Set}$ 指当前背景中的集合范畴. 除非另有说明, 这组笔记默认接受普通的、由集合编号的选择公理. 本章的构造及大小比较都在这个背景中理解.

我们会用对象和态射重新表述集合的性质, 但尚未把整套讨论逐步写入某个指定的形式系统. 关于意识宇宙、对象与元层次, 以及不同范围的选择原则, 见 [Chapter EX]({{< relref "posts/categoryThry/Chapter EX - Discussion on Set Theory.md" >}}#language-background). 涉及大范畴的统一选择时, 还需说明相应的宇宙层级或类选择原则.

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

在 $\mathbf{Set}$ 中, $A^B$ 与以 $B$ 的元素为索引的积 $\prod_{b\in B}A$ 自然同构. 这还使用了集合 $B$ 可以看成由其元素编号的一元集之和, 不能仅凭两种构造各自的泛性质推广到所有范畴. 我的探索及其他范畴中的反例整理在 [Chapter EX]({{< relref "posts/categoryThry/Chapter EX - Discussion on Set Theory.md" >}}#products-and-exponentials).

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

#### 满态射与范畴化表述

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
普通集合论选择公理与这个表述等价. 关于这项等价、将同一句式用于其他范畴时的区别, 以及它与 Chapter I 的等价判据和大范畴选择的关系, 见 [Chapter EX: 选择公理与范畴等价]({{< relref "posts/categoryThry/Chapter EX - Discussion on Set Theory.md" >}}#choice-and-equivalence).

## Small and large categories

比较集合的大小时, 我们规定 $|A|\leq|B|$ 表示存在单射 $A\to B$, 而 $|A|=|B|$ 表示存在双射 $A\to B$. Cantor–Bernstein 定理说明, 两个集合能够互相单射, 就足以保证它们之间存在双射.

恒等映射与单射的复合说明这个比较自反且传递. 它在集合上是预序: 互相不大于只保证同构, 不保证两个集合相等. 记 $|A|<|B|$ 表示 $|A|\leq|B|$ 且 $|A|\ne|B|$; 由 Cantor–Bernstein 定理, 有 $|A|\leq|B|<|C|\Rightarrow|A|<|C|$.

### Cantor–Bernstein

>[!theorem] Theorem 3.2.1 (Cantor–Bernstein)
>设 $A,B$ 是集合. 如果 $|A|\leq|B|\leq|A|$, 那么 $A\cong B$.

证明可以在 $A,B$ 中分别构造交错递降的集合列, 将两侧的层垒及交集部分一一对应. 我的完整证明及其所依赖的假设移至 [Chapter EX: Cantor–Bernstein 的层垒证明]({{< relref "posts/categoryThry/Chapter EX - Discussion on Set Theory.md" >}}#cantor-bernstein).

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

$\mathcal B$ 的对象由 $\mathbb N$ 编号, 每个 hom-set 又是有限集, 所以 $\mathcal B$ 是小范畴. 每个有限集合都同构于某个 $[n]$, 因而包含函子 $\mathcal B\to\mathbf{FinSet}$ 满、忠实且本质满. 按照 Chapter I 的等价判据及 [Chapter EX 中的选择约定]({{< relref "posts/categoryThry/Chapter EX - Discussion on Set Theory.md" >}}#large-categories-and-choice), 有 $\mathcal B\simeq\mathbf{FinSet}$. 所以 $\mathbf{FinSet}$ 本质小, 尽管全体有限集合本身组成大类.

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

教材先前用 $\mathbf{CAT}$ 表示更一般的范畴与函子组成的范畴. 使用“所有范畴”这样的说法时, 其大小仍按 [Chapter EX 的类与宇宙层级约定]({{< relref "posts/categoryThry/Chapter EX - Discussion on Set Theory.md" >}}#large-categories-and-choice) 理解.

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

[层垒证明]({{< relref "posts/categoryThry/Chapter EX - Discussion on Set Theory.md" >}}#cantor-bernstein) 已整理到 Chapter EX; 这道题提供从保序映射的不动点出发的另一条路线. (b) 中的 $f,g$ 不要求单射, 在 (c) 中才应用到互相单射的情形.

对于 (a), 我的构造是
$$
T=\{X\subseteq A\mid\theta(X)\subseteq X\},\qquad S=\bigcap T.
$$
保序性保证 $S$ 与 $\theta(S)$ 都属于 $T$, 再由 $S$ 的最小性得到 $\theta(S)=S$. 从自然数次迭代、超限延长到这个交集构造的探索与完整证明, 见 [Chapter EX: 保序映射的不动点]({{< relref "posts/categoryThry/Chapter EX - Discussion on Set Theory.md" >}}#monotone-fixed-points).

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
