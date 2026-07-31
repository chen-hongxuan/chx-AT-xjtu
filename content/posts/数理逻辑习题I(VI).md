---
title: "数理逻辑习题I(VI)"
date: 2026-07-31T00:00:00+08:00
tags: []
math: true
draft: false
---

-------------------------------------
$$
\newcommand{\lra}{\leftrightarrow}
\newcommand{\tx}[1]{\text{#1}}
\newcommand{\line}[2]{\  & #1 \quad & \rm{(#2)}\\}
\newcommand{\linet}[2]{\  & #1 \quad & \rm{#2}\\}
\newcommand{\fa}{\forall}
\newcommand{\ex}{\exists}
\newcommand{\A}{\mathcal{A}}
\newcommand{\B}{\mathcal{B}}
\newcommand{\C}{\mathcal{C}}
\newcommand{\D}{\mathcal{D}}
\newcommand{\E}{\mathcal{E}}
\newcommand{\G}{\mathcal{G}}
\newcommand{\H}{\mathcal{H}}
\newcommand{\I}{\mathcal{I}}
\newcommand{\J}{\mathcal{J}}
\newcommand{\mK}{\mathfrak{K}}
\newcommand{\mN}{\mathfrak{N}}
\newcommand{\mM}{\mathfrak{M}}
\newcommand{\mA}{\mathfrak{A}}
\newcommand{\mB}{\mathfrak{B}}
\newcommand{\mC}{\mathfrak{C}}
\newcommand{\mD}{\mathfrak{D}}
\newcommand{\mL}{\mathfrak{L}}
\newcommand{\mR}{\mathfrak{R}}
\newcommand{\Ax}{{\bf Ax}}
\newcommand{\ax}{\Lambda}
\newcommand{\bl}{\begin{aligned}}
\newcommand{\el}{\end{aligned}}
\newcommand{\T}{\mathscr{T}}
\newcommand{\t}{ {\bf t} }
\newcommand{\f}{ {\bf f} }
\newcommand{\L}[1]{L(#1)}
\newcommand{\eq}{\equiv}
\newcommand{\inp}{\leftarrow}
\newcommand{\la}[1]{\langle #1\rangle}
\newcommand{\ov}[1]{\overline{#1}}
\newcommand{\wff}{{\bf Wff}}
\newcommand{\so}{{\scr O}}
\newcommand{\vd}{\vdash_{L(N)}}
\newcommand{\ifff}{\ {\rm iff}\ }
\newcommand{\thm}{\mathbf{Thm}}
\newcommand{\mod}{\mathrm{Mod}\ }
\newcommand{\momg}{{\mM_\omega}}
\newcommand{\m}{\mM}
\newcommand{\st}{{\mathrm{st}}}
$$
----------------------------------

#####  I.47

我们只需要做一些检验性的工作即可. 对于常数变元, 条件天然成立; 对于函数符号 $f$ 以及 $\vec i_n\in|\mM|$ , 由于对于任何 $\vec j_n\in|\mK|$ 均有 $f^\mK(\vec j_n)=\phi(f^\mM(\phi^{-1}(j^n)))$ 并且 $\phi$ 是双射, 故存在唯一 $\vec i_n'\in|\mK|$ 使得 $\phi^{-1}(\vec i_n')=\vec i_n$ , 将其代入 $\vec j_n$ 即可得到 $f^\mK(\phi(\vec i_n))=\phi(f^\mM(\vec i_n))$ ; 对于谓词符号 $P$ 也是同理.

##### I.48

令 $\chi:=\psi\circ\phi$ , 那么对于任意常数符号 $c$ 有 $c^\mK=\phi(c^\mM),c^\mL=\psi(c^\mK)$ 从而有 $c^\mL=\psi(\phi(c^\mM))=\chi(c^\mM)$ ; 对于任意函数符号 $f$ 以及 $\vec i\in|\mM|$ 有 $f^\mK(\phi(\vec i))=\phi(f^\mM(\vec i))$ 从而有 $f^\mL(\psi(\phi(\vec i)))=\psi(f^\mK(\phi(\vec i)))=\psi(\phi(f^\mM(\vec i)))$ , 即 $f^\mL(\chi(\vec i))=\chi(f^\mM(\vec i))$ ; 对于任意谓词符号 $P$ 以及 $\vec i\in|\mM|$ 均有 $\psi(\phi(\vec i))\in P^\mL$ 当且仅当 $\phi(\vec i)\in P^\mK$ 当且仅当 $\vec i\in P^\mM$ , 即 $\chi(\vec i)\in P^\mL$ 当且仅当 $\vec i\in P^\mM$ . 从而嵌入的复合 $\chi$ 仍然是结构的嵌入. 

##### I.49

这种情况的存在是很广泛的, 设语言 $L$ 及其上的无穷模型 $\mA$ , 令基数 $\mathfrak n:=2^{\max\{|\mA|,|L|\}}$ 则显然有 $\mathfrak n >|\mA|$ , 由 I.6.24 可知存在模型 $\mA'$ 使得 $|\mA'|=\frak n$ 并且 $\mA\prec\mA'$ , 然而事实上他们两个模型之间不存在双射, 因为它们的基数不同, 因此他们必然不同构.

##### I.50

假设 $L$ 上的公式 $\A(\vec x_n)$ 在 $\mM$ 上定义了集合 $S$ , 那么有对于任意 $i\in|\mM|^n$ 有
$$
i\in S \iff \A[\vec x_n\inp \ov i]^\mM=\t
$$
 而由于 $\phi$ 是 $\mM$ 到 $\mM$ 的同构, 所以由 I.6.8 $\A[\vec x_n\inp\ov i]^\mM=\t\iff \A[\vec x_n\inp\ov{\phi(i)}]^\mM=\t$ , 这即是 $\phi(i)\in S$ .

##### I.51

若 $\N$ 是可定义的, 那么我们考虑一个函数
$$
\bl
\phi:&\R\to\R\\
&x\mapsto x+0.5
\el
$$
显然它是结构 $(\R,<)$ 上的自同构, 而显然对于 $n\in\N$ 一定有 $\phi(n)\not\in\N$ , 这与 I.50 矛盾了. 

##### I.52

证明的策略是构造一个 $\N\to\N$ 的双射 $f$ , 它满足对于任意 $x,y\in\N$ 均有 $f(x\cdot y)=f(x)\cdot f(y)$ 并且存在 $a,b\in\N$ 使得 $f(a+b)\not=f(a)+f(b)$ , 前者激励我们在积性函数中寻找答案, 事实上由素数分解定理, 对于每个 $n\in\N$ 均可以将其分解成如下的形式, 并且该形式唯一
$$
n=\prod_{i=1}^n p_i^{a_i}
$$
其中 $p_i$ 是从小往大数的第 $i$ 个质数, 于时我们考虑如下构造我们的 $f$
$$
\bl
f:\prod_{i=1}^np_i^{a_i}\mapsto p_1^{a_2}\cdot p_2^{a_1}\cdot\prod_{i=3}^np_i^{a_i}
\el
$$
实际上就是交换数字 $n$ 的 $2,3$ 这两个质因数上的幂次而已, 而我们可以验证这样的函数 $f$ 是完全积性函数并且还是双射, 因此 $f$ 可以导出一个 $(\N,\cdot)$ 上的自同构, 然而事实上我们有 $f(2+4)=6$ 而 $f(2)+f(4)=3+6=9$ , 从而加法的图在 $(\N,\cdot)$ 内不可定义.

##### I.53

设 $L$ 上的理论 $\cal T$ 被开公式集 $\Gamma$ 公理化, 即 $\mathcal{T}=\thm_\Gamma$ , 则由完全性定理 $\mod{\cal T}=\mod\Gamma$ , 则我们只需要证明, 对于开公式集 $\Gamma$ 以及 $L$ 上的模型 $\mA,\mB$ , 如果 $\mA\vDash\Gamma$ 并且 $\mB\subseteq\mA$ , 那么 $\mB\vDash\Gamma$ . 我们考虑对公式施以归纳来证明如下的引理

###### Lem 1.  固定模型 $\mB\subseteq\mA$ , 则对于任何 $L$ 上的开公式 $\A(\vec x_n)$ 以及 $i\in|\mB|^n$ 均有 $\A[\ov i]^\mA=\t\iff\A[\ov i]^\mB=\t$ .

> 首先当 $\A$ 是原子公式的时候, 假定 $\A\eq P(t_1...t_k)$ , 对于任意的 $j\in|\mB|$ , 由于 $\mB\subseteq\mA$ 故 $j\in|\mA|$ , 于是 $\A[\ov j]^\mA=\t$ 等价于 $\la{t_1(\ov j)^\mA...t_k(\ov j)^\mA}\in P^\mA$ , 而再一次由于 $\mB\subseteq\mA$ , 故对于 $1\le i\le k$ 有 $t_i(\ov j)^\mA=t_i(\ov j)^\mB\in|\mB|$ , 从而 $\la{t_1(\ov j)^\mA...t_k(\ov j)^\mA}\in P^\mA$ 实际上就是 $\la{t_1(\ov j)^\mA...t_k(\ov j)^\mA}\in P^\mA|_{|\mB|}$ , 即  $\la{t_1(\ov j)^\mB...t_k(\ov j)^\mB}\in P^\mB$ , 也就是 $\A[\ov j]^\mB=\t$ ; 等词的情况同理.
>
> 	之后考虑归纳情形, 如果 $\A\eq\neg\B$ , 则对于 $i\in|\mB|^n$ , 根据定义 $\A[\ov i]^\mA=\t$ 等价于 $\B[\ov i]^\mA=\f$ , 由 I.H. 这等价于 $\B[\ov i]^\mB=\f$ , 等价于 $\A[\ov i]^\mA=\t$ ; 如果 $\A\eq\B\or\C$ , 则对于 $i\in|\mB|^n$ , $\A[\ov i]^\mA=\t$ 等价于 $\B[\ov i]^\mA=\t$ 或者 $\C[\ov i]^\mA=\t$ , 这等价于 $\B[\ov i]^\mB=\t$ 或者 $\C[\ov i]^\mB=\t$ , 即 $\A[\ov i]^\mB=\t$ .

	而对于 $\A\in\Gamma$ , 如果 $\mA\vDash\A$ , 则对于任意的 $i\in|\mB|^n$ , 由于 $\mB\subseteq\mA$ 故 $i\in|\mA|^n$ , 从而有 $\A[\ov i]^\mA=\t$ , 由于 $\A$ 是开公式, 故根据上面的结果有 $\A[\ov i]^\mB=\t$ 从而 $\mB\vDash\A$ .

##### I.54

令 
$$
\mM_\omega:=\bigcup_{i\in\N}\mM_i
$$
首先我们检验对于 $i\in\N$ 均有 $\mM_i\subseteq\mM_\omega$ , 这是平凡的, 因为对于 $L$ 上的谓词符号 $P$ 以及函数符号 $f$ 均有
$$
P^{\mM_\omega}=\bigcup_{i\in\N}P^{\mM_i};f^{\mM_\omega}=\bigcup_{i\in\N}f^{\mM_i}.
$$
从而 $P^{\mM_i}=P^{\mM_\omega}|_{|\mM_i|},f^{\mM_i}=f^{\mM_\omega}|_{|\mM_i|}$ , 而对于常数符号的解释也是在 $\mM_0$ 就确定并一直不变的, 所以我们有 $\mM_i\subseteq\mM_\omega$ .

	之后我们我们来验证 $\mM_i\prec\mM_\omega$ , 证明的策略是对 $L$ 上的公式 $\A$ 施以归纳 . 于是首先我们需要验证一个引理

###### Lem 1.  $\mA,\mB,\mC$ 是语言 $L$ 的模型并且 $\phi:\mA\to_{\prec}\mB,\psi:\mB\to_{\prec}\mC$ , 则 $\psi\circ\phi$ 是 $\mA\to\mC$ 的初等嵌入.

> 对于 $L$ 上的公式 $\A(\vec x_n)$ 以及 $i\in|\mA|^n$ , 由 $\phi:\mA\to_{\prec}\mB$ 可得 $\A[\ov i]^\mA=\t\iff \A[\ov{\phi(i)}]^\mB=\t$ , 同时由于 $\phi(i)\in|\mB|^n$ , 故再由 $\psi:\mB\to_\prec\mC$ 可得 $\A[\ov{\phi(i)}]^\mB=\t\iff \A[\ov{\psi(\phi(i))}]^\mC=\t$ , 从而有 $\A[\ov i]^\mA=\t\iff\A[\ov{\psi\circ\phi(i)}]^\mC=\t$ , 故 $\psi\circ\phi$ 是一个初等嵌入.

接下来我们对于 $L$ 上的公式 $\A(\vec x_n)$ 施以归纳来证明对于任意的 $i\in\N$ 以及 $j\in|\mM_i|^n$ 有 $\A[\ov j]^{\mM_i}=\t\iff\A[\ov j]^{\mM_\omega}=\t$ ,

	如果 $\A$ 是原子公式, 则由于 $\mM_i\subseteq\mM_\omega$ 以及 I.6.23 可得, 对于任意 $j\in|\mM_i|^n$ 有 $\A[\ov j]^{\mM_i}=\t\iff\A[\ov j]^{\mM_\omega}=\t$ .
	
	如果 $\A$ 是经由逻辑联词得到的, 假设 $\A\eq\neg\B$ , 则对于 $j\in|\mM_i|^n$ 有 $\A[\ov j]^{\mM_i}=\t\iff \B[\ov j]^{\mM_i}=\f$ , 根据 I.H. 后者等价于 $\B[\ov j]^{\mM_\omega}=\f$ 亦即 $\A[\ov j]^{\mM_\omega}=\t$ ; 对于 $\A\eq\B\or\C$ 的情况, 同理经由 I.H. 可以平凡的验证这一结果.
	
	如果 $\A\eq\ex y\B(y,\vec x_n)$ , 那么对于 $j\in|\mM_i|^n$ , $\A[\ov j]^{\mM_\omega}=\t$ 当且仅当存在 $k\in|\mM_\omega|$ 使得 $\B[\ov k,\ov j]^{\mM_\omega}=\t$ . 根据我们对 $\mM_\omega$ 的构造, 存在充分大的 $l\in\N$ 使得 $k\in|\mM_l|$ , 而根据 I.H. 有 $\B[\ov k,\ov j]^{\mM_\omega}=\t\iff\B[\ov k,\ov j]^{\mM_l}=\t$ , 这就是在说: $\A[\ov j]^{\mM_\omega}=\t$ 当且仅当"存在 $l\in\N$ 以及 $k\in|\mM_l|$ 使得 $\B[\ov k,\ov j]^{\mM_l}=\t$ ", 即 $\A[\ov j]^{\mM_l}=\t$. 而根据 Lem 1 可得 $\mM_i\prec\mM_l$ , 从而 $\A[\ov j]^{\mM_l}=\t\iff\A[\ov j]^{\mM_i}=\t$ .

##### I.55

假定 $L$ 上的理论 $\scr S$ 是被 $\Gamma$ 公理化, 并且 $\Gamma$ 是归纳的, 并假定一个的 $L$ 上的模型链 $\la{\mM_i:i\in\N}$ 满足
$$
\mM_0\subseteq\mM_1\subseteq...\subseteq\mM_n\subseteq...
$$
并且每个 $\mM_i$ 都是 $\Gamma$ 的模型, 那么只需要验证 
$$
\mM_\omega:=\bigcup_{k\in\N}\mM_k
$$
是 $\Gamma$ 的模型即可, 即对于任意 $\D\in\Gamma$ 均有 $\mM_\omega\vDash\D$ . 在此之前可以先验证对于 $i\in\N$ 均有 $\mM_i\subseteq\mM_\omega$ , 之后根据 $\mM_\omega$ 的构造, 任意 $j\in|\mM_\omega|^n$ , 存在充分大的 $k\in\N$ 使得 $j\in|\mM_k|^n$ , 在此前提下我们可以证明以下的一个结论, 

###### Lem 1.  设语言 $L$ 上的两个模型 $\mA,\mB$ 满足 $\mA\subseteq\mB$ , 则对于任意形如 $\B(\vec x_n)\eq\ex\vec y_m\A(\vec x_n,\vec y_m)$ 的公式(其中 $\A$ 为开公式)以及 $i\in|\mA|^n$ , 如果 $\B[\ov i]^\mA=\t$ , 那么 $\B[\ov i]^\mB=\t$ .

> 我们对存在量词前缀的长度 $m$ 施以归纳来证明.
>
> 	对于 $m=0$ 的情形, 即 $\B$ 本身就是开公式, 那么由 I.53 的 Lem 1 可知结论成立.
> 	
> 	对于归纳情形, 假定 $\B(\vec x_n)\eq\ex z\C(\vec x_n,z)$ , 若 $\B[\ov i]^\mA=\t$ 则存在 $j\in|\mA|$ 使得 $\C[\ov i,\ov j]^\mA=\t$ , 根据 I.H. $\C[\ov i,\ov j]^\mB=\t$ , 从而 $\B[\ov i]^\mB=\t$ .

	对于任意 $\A(\vec x_n)\in\Gamma$ , 对于任意的 $i\in|\mM_\omega|^n$ , 根据我们对于 $\momg$ 的构造, 存在充分大的 $k\in\N$ 使得 $i\in|\m_k|$ , 而根据前提每个 $\m_k$ 均为 $\Gamma$ 的模型故 $\m_k\vDash\A$ , 即 $\A[\ov i]^{\m_k}=\t$ , 又因为 $\m_k\subseteq\momg$ 且 $\Gamma$ 是归纳的, 故 $\A[\ov i]^\momg=\t$ , 从而 $\momg\vDash\A$ .

##### I.56

令语言 $L_\mN:=(0,S,+,\times,<)$ 及其上面的标准模型 $\mN:=(\N,0,S,+,\times,<)$ . 考虑向语言中加入一个新的常数符号 $c$ 从而得到新语言 $L':=(0,S,+,\times,<,c)$ , 之后来看 $L'$ 上的公式集
$$
\mathscr N:={\bf Th}(\mN)+\{S^i0<c:i\in\N\}
$$
之后利用紧致性定理来证明 $\scr N$ 是一致的. 首先容易验证, 对于任何 $c'\in\N$ , 拓展后的 $L'$ 上的结构 $\mN(c'):=(\N,0,S,+,\times,<,c')$ 仍然是 $L'$ 上的公式集 ${\bf Th}(\mN)$ 的模型, 而对于 $\scr N$ 的任意有穷子集 $\scr N'$ , 它一定是由 ${\bf Th}(\mN)$ 的有穷个片段 $\scr A$ 以及 $\{S^i0<c:i\in\N\}$ 的有穷个片段 $\scr B$ 组成的, 而正因为 $\scr B$ 有穷, 所以我们总是可以挑选一个充分大的 $n\in\N$ 使得 $\mN(n)\vDash\scr B$ , 故 $\mN(n)\vDash\scr A+B$ 即 $\scr N'$ , 即 $\scr N'$ 是可满足的, 从而 $\scr N$ 是可满足的, 故它存在一个模型 $\mA:=(N,0^\mA,S^\mA,+^\mA,\times^\mA,<^\mA,c^\mA)$ , 之后我们将其限制在 $L_\mN$ 上得到的模型 $\mC$ 即为所求, 因为在它的论域 $N$ 上存在一个比所有"自然数"都要更大的数. 

##### I.57

令公式集
$$
\Gamma':=\Gamma+\{\ex\vec x_n\bigwedge_{1\le i<j\le n}(\neg x_i=x_j):n\in\N\}
$$
同理 I.56 , 对于任意 $\Gamma'$ 的有穷子集 $\Gamma^*$ , 根据前提, 我们总能挑选 $\Gamma$ 的充分大的一个模型 $\mA$ 使得 $\mA\vDash\Gamma^*$ , 从而 $\Gamma^*$ 可满足, 因此 $\Gamma'$ 可满足, 从而存在 $\Gamma'$ 的模型 $\mC$ , 它是 $\Gamma'$ 的模型并且它的论域是无穷的.

 ##### I.58 

我就要用 upward Lowenheim-Skolem theorem.

##### I.59

(1) 首先我们有 ${\bf Th}(\mR)\vdash \fa x(x-x=0)$ , 因此在 $^*\mR$ 中, 对于任意 $x\in^*\R$ 均有 $x-x=0$ , 而显然 $0$ 是无穷小量, 从而 $x\approx x$ .

(2) 这可以由 $|x-y|=|y-x|$ 导出, 因为这在 $\mR$ 中成立, 故它也在 $^*\mR$ 中成立.

(3) 这可以由 $|x-z|\le|x-y|+|y-z|$ 导出.

##### I.60

因为 $0\le x\le y\to |x|\le|y|$ 在 $\mR$ 中成立, 故它也在 $^*\mR$ 中成立.

##### I.61

(2) 对于任意 $x,y\in{^*\R}$ , 均有 $x+y=\st(x)+r+\st(y)+r'=\st(x)+\st(y)+(r+r')$ , 因为 $r,r'$ 是无穷小量所以 $r+r'$ 也是, 而由于 $\st(x),\st(y)\in\R$ 故 $\st(x)+\st(y)\in\R$ 从而 $\st(x+y)=\st(x)+\st(y)$ .

(3) 我们只需要验证 $\st(-x)=-\st(x)$ 即可, 对于 $x\in{^*\R}$ 我们有 $x=\st(x)+r$ 故 $-x=-st(x)-r$ , 而 $|-r|=|r|$ 故 $-r$ 是无穷小量, 从而 $\st(-x)=-\st(x)$. 在这里 $\st(a-b)=\st(a+(-b))=\st(a)+\st(-b)=\st(a)-\st(b)$ .

(4) 对于 $x,y\in{^*\R}$ , 我们有 $x\cdot y=(\st(x)+r)\cdot(\st(y)+r')=\st(x)\cdot\st(y)+r\cdot\st(y)+r'\cdot\st(x)+r\cdot r'$ , 由 I.6.41 可得后面那一坨都是无穷小量.  

(6) 对 $n$ 施以归纳, $n=0,1$ 的情形是显然的. 而 $\st(a^{n+1})=\st(a^n\cdot a)$ , 根据 (4) 可得 $RHS=\st(a^n)\cdot\st(a)$ , 根据 I.H. 有 $\st(a^n)=\st(a)^n$ 故 $RHS=\st(a)^n\cdot\st(a)=\st(a)^{n+1}$ .

##### I.62

考虑一阶语句 $\fa x\ex y(N(y)\and y>x)$ , 由于 $^*\R$ 中存在无穷大超实数 , 因而我们也存在无穷大"自然数". 

##### I.63

首先显然 $h-1$ 是无穷数, 并且我们有 $\fa x[(x\not= 0\and N(x))\to(N(x-1))]$ , 因此 $h-1$ 是 $^*\R$ 中的"自然数". 

	然而这并不与传达原理冲突, 因为一个"自然数"的非空子集没有最小值的前提是它不包含标准自然数, 而这样的一个子集我们是没法在 $L$ 中描述它的, 我们的语言的能力在区别无穷和有穷上是很有限的.

##### I.64

首先我们看一个一阶语句 $\A$
$$
\fa n((N(n)\and n>0)\to\ex i(N(i)\and i\le x\and\fa j((N(j)\and0\le j\le n)\to f(a+\frac{b-a}{n}\cdot i)\ge f(a+\frac{b-a}{n}\cdot i))))
$$

它的意思是说, 对于任意正整数 $n$ , 我们在 $[a,b]$ 这个区间内采样 $n+1$ 个点, 它们是 $\{a+\frac{b-a}{n}\cdot k:0\le k\le n\}$ , 那么在这 $n+1$ 个点中, 存在一个点 $i$ 使得它上面的函数值大于等于其余的 $n$ 个点. 这句话在 $\mR$ 中当然是正确的, 于是由于 $\mR\prec{^*\mR}$ 故这句话在 $^*\mR$ 中也是正确的. 

	根据前面的讨论我们知道存在无穷大自然数, 取出这样的一个无穷大自然数 $K$ , 那么我们可以把语句 $\A$ 中的 $n$ 替换为 $K$ , 因此存在另一个超自然数(标准或无穷大) $I$ 使得, 对于任意不超过 $K$ 的超自然数 $i$ 均有
$$
^*f(a+(b-a)\cdot\frac IK)\ge{^*f}(a+(b-a)\cdot\frac iK)
$$
由于 $x\ge y\implies\st(x)\ge\st(y)$ , 所以我们有
$$
\st({^*f}(a+(b-a)\cdot\frac IK))\ge\st({^*f}(a+(b-a)\cdot\frac iK))
$$
而 $f$ 连续, 所以 $^*f$ 和 $\st$ 关于 $\circ$ 交换, 故有
$$
^*f(\st(a+(b-a)\cdot\frac IK))\ge{^*f}(a+(b-a)\cdot\st(\frac iK))
$$
令 $I':=\st(a+(b-a)\cdot\frac IK)$ , 于是 $I'\in\R$ 并且 $LHS={^*f}(I')$ , 我们尝试论证这个 $I'$ 就是我们想要的那个实数, 因此我们需要先证明以下的引理

###### Lem 1.  $K$ 是某个无穷大自然数, 则对于任意 $r\in[0,1]\cap\R$ , 存在超自然数 $i$ 使得 $r=\st(\frac iK)$ .

> 我们考虑另外一个语句 $\B$
> $$
> \fa x\fa a((a>0)\to\ex k(N(k)\and (x\le k\cdot a< x+a)))
> $$
> 这句话说的是, 在区间 $[x,x+a]$ 中一定存在形如 $k\cdot a$ 的数. 它在 $\mR$ 中成立, 所以在 $^*\mR$ 中也成立, 于是我们取 $a$ 为 $\frac 1K$ , 取 $x$ 为 $r$ , 那么存在超自然数 $i$ 使得 $r\le\frac iK\le r+\frac 1K$ , 由于 $K$ 为无穷大自然数, 所以 $\frac 1K$ 为无穷小量, 所以 $r\approx r+\frac 1K$ , 由夹逼定理可得 $\frac iK\approx r$ , 即 $\st(\frac iK)=\st(r)=r$ .

因此 $a+(b-a)\cdot\st(\frac iK)$ 能够遍历全体 $[a,b]$ 中的实数, 所以我们可以说, 对于任意的 $x\in[a,b]\cap\R$ , $f(I')\ge f(x)$ , 于是我们就成功地通过 $^*\mR$ 把这个取得最大值的实数 $I'$ 构造出来了.

##### I.65

根据我们在实分析里证明介值定理的惯例, 我们先证明零点存在性定理.

###### Lem 1.  对于连续函数 $f$ 以及实数 $a,b(a<b)$ , 如果 $f(a)<0<f(b)$ , 则存在实数 $\xi\in[a,b]$ 使得 $f(\xi)=0$ .

> 我们考虑如下的一个一阶语句 $\A$
> $$
> \fa n((N(n)\and n>0)\to\ex i(N(i)\and i<n\and f(a+(b-a)\cdot\frac in)\le 0\and f(a+(b-a)\cdot\frac{i+1}n\ge 0)))
> $$
> 它是在说, 如果我们将 $[a,b]$ 这个区间内采样 $n+1$ 个点 $\{a+\frac{b-a}{n}\cdot k:0\le k\le n\}$ , 那么一定存在两个相邻的点 $u,v$ 使得 $f(u)\le 0\le f(v)$ . 这在 $\mR$ 中显然是正确的, 因此它在 $^*\mR$ 中也是正确的, 所以我们取一个无穷大自然数 $K$ 并将其代入 $n$ , 则存在超自然数 $i$ 使得 $f(a+(b-a)\cdot\frac iK)\le 0\le f(a+(b-a)\cdot\frac{i+1}K)$ , 记 $I:=a+(b-a)\cdot\frac iK,I':=a+(b-a)\cdot\frac{i+1}K$ , 则不难注意到 $I'-I=\frac{b-a}K$ 是无穷小量, 故 $I'\approx I$ , 即 $\st(I')=\st(I)$ . 我们直接取 $\xi:=\st(I)$ , 由于 $f(I)\le 0\le f(I')$ 并且 $f$ 是连续函数, 所以有 $f(\xi)=f(\st(I))=\st(f(I))\le 0$ , 而另一方面 $f(\xi)=f(\st(I'))=\st(f(I'))\ge0$ , 从而有 $f(\xi)=0$ .

	于是对于闭区间 $[a,b]$ , 由 I.64 我们可以假定其最小值最大值分别在 $x_1,x_2$ 处取得, 则对于任意 $a\in(f(x_1),f(x_2))$ 取 $g(x)=f(x)-a$ , 则 $g$ 连续并且 $g(x_1)<0<g(x_2)$ , 从而根据 Lem 1 存在零点 $\xi$ 使得 $g(\xi)=0$ , 即为 $f(\xi)=a$ .

##### I.66

令一阶公式
$$
P(x):=N(x)\and x>1\and\fa u\fa v((N(u)\and N(v)\and u\cdot v=x\and u\le v)\to(u=1\and v=x))
$$
则在 $\mR$ 中公式 $P$ 定义了素数集 $\mathbb P$ , 而我们显然有如下的在 $\mR$ 中正确的语句 $\A$
$$
\fa x(N(x)\to \ex y(P(y)\and y>x))
$$
从而 $\A$ 在 $^*\mR$ 中也正确, 而由于 $^*\mR$ 中存在无穷大自然数, 故存在无穷大素数.