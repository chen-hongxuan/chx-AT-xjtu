---
title: "数理逻辑习题I(VIII)"
date: 2026-07-31T00:00:00+08:00
tags: []
math: true
draft: false
---

-----------------------------------------------------------------------------------
$$
\gdef\lra{\leftrightarrow}
\gdef\fa{\forall}
\gdef\ex{\exists}
\gdef\r{\mathfrak{R}}
\gdef\bl{\begin{aligned}}
\gdef\el{\end{aligned}}
\gdef\t{ {\bf t} }
\gdef\f{ {\bf f} }
\gdef\eq{\equiv}
\gdef\la#1{\langle #1\rangle}
\gdef\ov#1{\overline{#1}}
\gdef\m{\mu}
\gdef\st{{\mathrm{st}}}
\gdef\p{\mathfrak{P}}
\gdef\l{\lambda}
\gdef\xn{{\vec x_n}}
\gdef\dd{\downarrow}
\gdef\aa{\uparrow}
\gdef\x{\vec x}
\gdef\if{\mathbf{if}\quad}
\gdef\oth{\mathbf{otherwise}}
\gdef\bb#1{\{#1\}}
\gdef\U#1{U^{(#1)}}
\gdef\no{\o^{-1}}
\gdef\dom{\mathrm{dom}\ }
\gdef\ran{\mathrm{ran}\ }
\gdef\o{\mathcal O}
\gdef\re{{\bf r.e.}}
\gdef\I{\mathcal I}
\gdef\fd{\mathscr{Find}}
$$
***

##### I.68

trivial.

##### I.69

令关系 $R:=\{(y,\vec x_n):y=f(\vec x_n)\}$ 的特征函数为 $\chi$ 则, $\chi\in\r$ . 于是我们考虑函数 $f':=\l\vec x_n.(\m y)\chi(y,\vec x_n)$ , 则根据定义 $f'\in\p$ , 而我们容易验证, 对于任意的 $\xn$ 均有 $f'(\xn)\dd$ 并且 $f'(\xn)=f(\xn)$ , 从而 $f'\in\r$ 并且 $f=f'$ , 从而 $f\in\r$ .

$f$ 是全函数这一点是必要的, 不然 $f'$ 就不是全函数了.

##### I.70

对于函数 $\l y\xn.f$ 我们分别构造以下函数
$$
\bl
S_f(0,\xn)&=0,\\
S_f(y+1,\xn)&=f(y,\xn)+S_f(y,\vec x_n).
\el
$$
以及
$$
\bl
P_f(0,\xn)&=1,\\
P_f(y+1,\xn)&=f(y,\xn)\times P_f(y,\xn).
\el
$$
显然 $\l y\xn.S_f,\l y\xn.P_f$ 分别是 $\sum_{z<y}f(z,\xn),\prod_{z<y}f(z,\xn)$ , 而 $\r,\p\r$ 均对原始递归封闭并且 $\l xy.x+y,\l xy.x\times y\in\p\r$ , 所以如果 $f\in\r$ (或者 $\p\r$ ), 那么就有 $S_f,P_f\in\r$ (或者 $\p\r$ ). 

##### I.71

记关系 $\l y\x.[y=f(\x)]$ 为 $R$ , 由于 $R\in\p_*$ , 根据 I.8.41 存在 $\l zy\x.Q\in \r_*$ 使得 $R=(\ex z)Q$ , 由于 $Q$ 是递归的, 所以关系
$$
Q':=\l z\x.Q((z)_0,(z)_1,\x)
$$
也是递归的, 于是我们构造函数
$$
f':=\l\x.((\m z)Q'(z,\x))_1
$$
接下来我们说明 $f'$ 是递归函数并且 $f'=f$ . 首先显然有 $f'\in\p$ , 对于输入 $\x$ , 总是存在 $y$ 使得 $(y,\x)\in R$ , 从而根据 $Q$ 的构造可得存在 $z'$ 使得 $(z',y,\x)\in Q$ , 于是取 $z:=\la{z',y}$ 可得 $(z,\x)\in Q'$ , 从而 $f'(x)\dd$ , 因此 $f'\in\r$ ; 同时对于每个输入 $\x$ , 这样的 $y_0$ 是唯一的, 所以对于所有满足 $(z,\x)\in Q'$ 的 $z$ 均有 $((z)_0,(z)_1,\x)\in Q$ 从而有 $((z)_1,\x)\in R$ , 因此一定有 $(z)_1=y_0$ , 所以对于所有 $\x$ 均有 $f'(\x)=f(\x)$ , 因此 $f'=f$ .

##### I.72

$$
f=\l\x.sw(\chi_{R_1}(\x),g_1(\x),sw(\chi_{R_2}(\x),g_2(\x),sw(...,...,sw(...))))
$$

##### I.73

这是一个经典的初等数论的结论, 为证明它我们先证明以下的一个引理.

###### Lem 1. 对于任意 $n\in\N$ 均有 $p_{n+1}\le p_0p_1...p_n+1$ .

> 一个显然的观察是, 对于 $r\in\N$ , $r$ 是素数当且仅当对于任意小于 $r$ 的素数 $p$ 均有 $r\mod p\not=0$ . 于是记 $c:=p_0p_1...p_n+1$ , 那么一定有 $c>p_n$ , 如果 $p_{n+1}>c$ , 则 $c$ 不是素数并且小于 $c$ 的素数集就是 $\{p_i:0\le i\le n\}$ , 然而对于任意的 $i\le n$ 均有 $c\mod p_i=1$ , 这与 $c$ 的非素性矛盾了.

 从而我们可以对 $n$ 施以强归纳来证明 $p_n\le2^{2^n}$ .

> * 对于 $n=0$ , $2=p_n \le 2^{2^0}=2$ .
> * 对于 $n+1$ 的情形, 由 Lem 1 可得
>
> $$
> p_{n+1}\le p_0p_1...p_n+1\le 2^{2^0}\times 2^{2^1}\times...\times 2^{2^n}+1=2^{2^0+2^1+...+2^n}+1=2^{2^{n+1}-1}+1\le 2^{2^{n+1}}
> $$

##### I.74

$$
\pi=\l x.\sum_{z<x+1}\ov{sg}(Pr(z))
$$

而根据 I.70 , $\p\r$ 对有界和封闭, 而 $Pr,\ov{sg}\in\p\r$ 从而 $\pi\in\p\r$ .

##### I.75

trivial.

##### I.76

首先我们可以利用二重归纳法来证明对于任意输入 $n,x\in\N$ 均有 $A(n,x)\dd$ , 从而我们只需要证明 $A\in\p$ , 为此我们构造函数
$$
F:=\l znx.\left\{\bl
&x+2&\if &n=0\\
&2&\if &n>0\and x=0\\
&U^{(2)}(z,n\ \dot-\ 1,U^{(2)}(z,n,x\ \dot-\ 1))& &\oth
\el\right.
$$
显然 $F$ 是部分递归函数, 故由第二递归定理存在 $e\in\Phi$ 使得
$$
\l nx.F(e,n,x)=\bb e
$$
接下来我们验证 $\bb e=A$ . 

> * 当 $n=0$ 时, $\bb e(n,x)=F(e,0,x)=x+2$ . 
>
> * 当 $x=0$ 时, $\bb e(n+1,x)=F(2,n+1,0)=2$ . 
>
> * 至于其他情况, 对于全体的 $n,x\in\N$ 根据 $F$ 的定义我们有 $\bb e(n+1,x+1)=F(e,n+1,x+1)=\bb e(n,\bb e(n+1,x))$ . 

从而可以利用二重归纳法来证明对于任意 $n,x\in\N$ 有 $A(n,x)=\bb e(n,x)$ , 故 $A\in\p$ . 

##### I.77

构造部分递归函数
$$
F:=\l zyx.\left\{\bl
&y&\if &x=y+1\\
&U^{(2)}(z,y+1,x)& &\oth
\el\right.
$$
则由 I.8.55 可得, 存在 $e\in\Phi$ 使得 $\l yx.F(e,y,x)=\bb e$ , 于是我们验证 $\bb e=h$

> * 当 $x=y+1$ 时, $\bb e(y,x)=F(e,y,x)=y$ .
> * 其余情况, $\bb e(y,x)=F(e,y,x)=\bb e(y+1,x)$ .

从而对于所有输入 $x,y\in\N$ 均有 $\bb e(x,y)=h$ 故 $h\in\p$ .

事实上对于任意 $x\in\N$ 我们有
$$
h(0,x)=\left\{\bl
&\aa&\if&x=0\\
&x\ \dot-\ 1&&\oth
\el\right.
$$

##### I.78

构造
$$
F:=\l zyx.\left\{\bl
&y&\if&x=y+1\\
&\U2(z,y,x)+1&&\oth
\el\right.
$$

并取不动点 $e\in\Phi$ , 则容易证明 $\bb e=k$ .

##### I.79

我们遇到的一个问题是, 当条件判断函数不是全函数的时候, 我们该怎么处理, 这可能不是一个良定义的问题. 我们需要重新考虑一下如何表达条件. 事实上我们尝试构造函数
$$
F:=\l zy\x.sw(f(y,\x),y,U(z,y+1,\x))
$$
则取不动点 $e\in\Phi$ 可得 $\l y\x.F(e,y,\x)=\bb e$ , 从而对于任意输入 $y,\x\in\N$ 均有 $\bb e(y,\x)=sw(f(y,\x),y,\bb e(y+1,\x))$ .

而事实上 $\l\x.g(0,\x)$ 就是 $\l\x.(\m y)f(y,\x)$ .

##### I.80

我们首先需要证明一个引理
###### Lem 1.  存在 $e\in K,e'\notin K$ 使得 $\bb e=\bb {e'}$ .

> 显然关系 $\l xy.[x=y]$ 是原始递归的, 因此它也是半递归的, 因此存在一个函数 $\l xy.\rm eq\in\p$ 使得, 对于任意 $x,y\in\N$
> $$
> x=y\iff {\rm eq}(x,y)\dd
> $$
> 并且我们稍加修改可以使得当 $x=y$ 时有 ${\rm eq}(x,y)=0$ , 同时我们知道存在 $i_0\in\Phi$ 使得 $\bb{i_0}=\rm eq$ . 我们对 $\rm eq$ 应用 I.8.55 可以得到 $e\in\Phi$ 满足 $\bb e=\l x.{\rm eq}(e,x)$ , 即对于 $x\in\N$ 
> $$
> \bb e(x)=\left\{\bl
> &0&\if& x=e\\
> &\aa&&\oth
> \el\right.
> $$
> 因此 $e\in K$ , 同时我们知道 $\p$ 中的每个函数都有无穷多个指标所以存在 $e'\in\Phi$ 使得 $e'\not=e$ 并且 $\bb{e'}=\bb{e}$ , 于是根据我们对 $e$ 以及 $e'$ 的构造可得 $\bb{e'}(e')\aa$ 所以 $e'\notin K$ .

假定 $K$ 是完全指标集, 那么存在 $\frak D\subseteq P$ 使得 $x\in K\iff \bb x\in\frak D$ . 然而根据 Lem 1 我们可以取出 $e,e'\in\N$ 使得 $\bb e=\bb{e'}$ 并且 $e\in K,e'\notin K$ , 与假设矛盾. 

##### I.81

(1) 不是. 记集合 $\bb{x\in\N:\bb x(x)=0}$ 为 $K'$ , 则上述构造的 $e,e'$ 满足 $e\in K',e\notin K$ , 注意到 $K'\subseteq K$ 因此 $e'\notin K'$ , 则可以通过类似的论证证明 $K'$ 不是完全指标集.

(2) 不是. 事实上似乎存在归约的聪明证法, 但是我比较蠢, 所以也只能从对角线出发. 考虑证明 $\ov{K'}$ 不是半递归的, 假定是, 则根据 I.8.42 存在 $\l x.f\in\p$ 使得对于任意 $x\in\N$
$$
x\in\ov{K'}\iff f(x)=0
$$
假定 $i\in\Phi$ 使得 $f=\bb i$ 于是根据定义对于任意 $x\in\N$ ,
$$
\bb x(x)\not=0\iff x\in\ov{K'}\iff\bb i(x)=0
$$
取 $x$ 为 $i$ 即可轻易得出矛盾.

(3) 是. 取谓词 $(\ex z)(T^{(1)}(x,x,z)\and (z)_0=0)$ 即可.

##### I.82

不一定, 以下给出两种 $f\in\r$ 的选取, 分别使得 $\bb{x\in\N:\bb{f(x)}(x)\dd}$ 是/不是 完全指标集.
(1) 取 $f:=\lambda x.0$ , 则 $f(x)=0\notin\Phi$ 从而 $\bb{x\in\N:\bb{f(x)}(x)\dd}=\empty$ , 显然这是一个完全指标集.
(2) 取 $f:=\l x.x$ , 则 $\bb{x\in\N:\bb{f(x)}(x)\dd}=K$ 不是完全指标集.

##### I.83

> 构造真的好困难.

考虑构造如下的原始递归谓词
$$
H:=\l ixu.(\ex z)_{\le u} T^{(1)}(i,x,z)
$$
之后令 $\psi:=\l xy.(\m u)(H(a,y,u)\or(H(x,x,u)\and\neg H(a,y,u)))$ , 则显然 $\psi\in\p$ , 之后我们令函数
$$
\tau:=\l xy.\U 1(sw(H(a,y,\psi(x,y)),a,b),y)
$$
假设它的指标为 $i_0$ , 则根据 S-m-n 定理可得对于任意 $x\in\N$ 均有 $\l y.\tau(x,y)=\{\sigma(i_0,x)\}$ , 接下来我们证明 $\l x.\sigma(i_0,x)$ 是我们想要的那个归约函数 $f$.
对于 $x\in K$ , 则存在 $u$ 使得 $(x,x,u)\in T^{(1)}$ , 因而对于任意 $y\in\N$ 均有 $\psi(x,y)\dd$ . 如果 $\bb b(y)\aa$ 则根据构造 $\tau(x,y)\aa$ ; 而如果 $\bb b(y)\dd$ 并且 $\bb a(y)\aa$ (事实上一定存在这样的 $y$ , 若不然则由 $\bb a\subseteq\bb b$ 可以推出 $\bb a=\bb b$ , 这与 $\bb b\notin A$ 矛盾),  则显然对于任意的 $u$ 均有 $(a,y,u)\notin H$ , 所以这个时候 $\tau(x,y)=\U 1(b,y)=\bb b(y)$ ; 而如果 $\bb b(y)\aa$ 则此时有 $\tau(x,y)\aa$ . 综上所述, 此时 $\bb{\sigma(i_0,x)}=\l y.\tau(x,y)=\bb b$ .
对于 $x\notin K$ , 则对于任意 $u$ 均有 $(x,x,u)\notin H$ , 所以 $\psi(x,y)\dd$ 当且仅当 $\bb a(y)\dd$ . 注意这个时候我们实际上已经讨论过 $\bb a(y)\aa$ 的情形了, 所以只需要验证当 $\bb a(y)\dd$ 的时候 $\tau (x,y)=\bb a(y)$ 即可, 根据 $x\notin K$ 的假设, 当 $\bb a(y)\dd$ 时显然有 $(a,y,\psi(x,y))\in H$ 所以实际上 $\tau(x,y)=\U1(a,y)=\bb a(y)$ .  综上所述, 此时 $\bb{\sigma(i_0,x)}=\l y.\tau(x,y)=\bb a$.
而 $\l x.\sigma(i_0,x)$ 的单射性是显而易见的并且它还是原始递归的, 所以我们有对于任意 $x\in\N$
$$
\bl
x\in\ov K\implies \{\sigma(i_0,x)\}=\bb a\implies \sigma(i_0,x)\in A\\
x\notin\ov K\implies \{\sigma(i_0,x)\}=\bb b\implies \sigma(i_0,x)\notin A\\
\el
$$
故有
$$
x\in\ov K\iff\sigma(i_0,x)\in A
$$
而假定 $A$ 是半递归的, 取 $\l x.g\in\p$ 使得 $x\in A\iff g(x)\dd$ , 则函数 $\l x.g(\sigma(i_0,x))$ 满足
$$
x\in\ov K\iff \sigma(i_0,x)\in A\iff g(\sigma(i_0,x))\dd
$$
从而 $\l x.g(\sigma(i_0,x))$ 判定了 $\ov K$ , 这与" $\ov K$ 不是半递归的"矛盾, 因而 $A$ 必定不是半递归的.

##### I.84

> 我大抵是真的活到头了, 怎么到处都有构造啊.

上一个问题让我们构造出了一个从 $A$ 到 $\ov K$ 的归约函数, 而且这个函数在形式系统内, 所以这一问中让我们考察 $A$ 的产生性, 所以一个自然的想法是先考察 $\ov K$ 的产生性, 之后尝试将 $A$ 的产生性归约到 $\ov K$ 上面, 为此我们先看如下引理.

###### Lem 1.  $\ov K$ 是产生集.

> 取函数
> $$
> \psi_{\ov K}:=\l x.x
> $$
> 显然 $\psi_{\ov K}\in\p$ , 接下来我们证明它是集合 $\ov K$ 的产生函数. 对于任意 $e\in\N$ 满足 $W_e\subseteq\ov K$ , 假设 $e\in W_e$ , 则根据定义 $e\in K$ , 从而 $W_e\cap K\not=\empty$ , 这与 $W_e\subseteq \ov K$ 矛盾, 从而 $e\notin W_e$ , 因此 $e\notin K$ 即 $e\in\ov K$ , 于是这个 $e$ 恰好就是我们的目标元素.

之后我们开始构造归约, 首先关注之前构造出来的函数 $\l x.\sigma(i_0,x)$ , 记之为 $\o$ , 则我们有 $x\in\ov K\iff \o(x)\in A$ , 并且这个 $\o$ 是单射, 所以实际上 $\o$ 是 $\ov K$ 到 $A$ 的双射, 因而我们可以构造 $\o$ 的逆函数
$$
\no:=\l x.(\m y)[y=\o(x)]
$$
其中 $\no\in\p $ 并且 $\dom\no=A$ . 之后对于 $f\in\p$ 以及 $R\subseteq\N$ 我们规定符号
$$
f[R]:=\bb{f(x):x\in R\and f(x)\dd}
$$
则对于全体 $e\in\N$ 均有 $W_e\subseteq A$ 当且仅当 $\o[\no[W_e]]=W_e$ (一个显而易见的事实是对于全体 $e$ 根据规定均有 $\no[W_e]\subseteq\ov K$ ), 事实上半递归集和 $\re$ 集合是等价的, 因而我们可以说明对于 $e\in\N$ 总是存在 $e'$ 使得 $W_{e'}=\no[W_e]$ , 则根据 Lem 1. 可知 $e'$ 满足 $e'\in\ov K- W_{e'}$ , 从而如果 $W_e\subseteq A$ 则有 $\o[W_{e'}]=W_e$ , 从而 $\o(e')\notin W_e$ , 所以接下来我们只需要证明这种映射 $e\mapsto e'$ 是递归的即可.

###### Lem 2.  对于任意 $f\in\p$ , 存在原始递归函数 $\l x.g$ 使得对于任意 $e\in\N$ 均有 $f[W_e]=W_{g(e)}$ .

>  由于 $f\in\p$ 所以存在 $i_1\in\Phi$ 使得 $f=\bb {i_1}$ , 则对于任意 $x\in\N$ , 我们有
>  $$
>  \bl
>  x\in f[W_e]&\iff (\ex y)(y\in W_e\and f(y)=x)\\
>  &\iff(\ex y)((\ex z)T^{(1)}(e,y,z)\and(\ex z')T^{(1)}(i_1,y,\la{x,z'}))\\
>  &\iff(\ex l)(\ex y,z,z')_{\le l} (T^{(1)}(e,y,z)\and T^{(1)}(i_1,y,\la{x,z'}))
>  \el
>  $$
>  我们记 $N:=\l lxe.(\ex y,z,z')_{\le l}(T^{(1)}(e,y,z)\and T^{(1)}(i_1,y,\la{x,z'}))$ , 则 $N\in\p\r_*$ , 因此由 I.8.49 可得, 关系 $Q:=\l xe.x\in f[W_e]$ 是半递归的, 因此存在 $j_0\in\Phi$ 使得对于任意 $x,e\in\N$ 均有 $(x,e)\in Q\iff \bb{j_0}(x,e)\dd\iff \bb{\sigma(j_0,e)}(x)\dd$ , 因此对于固定的 $e\in\N$ , 对于任意 $x\in\N$ 我们有 $x\in f[W_e]\iff\bb{\sigma(j_0,e)}(x)\dd\iff x\in W_{\sigma(j_0,e)}$ , 因此有 $f[W_e]=W_{\sigma(j_0,e)}$ , 同时 $\sigma$ 函数是原始递归的, 所以 $\l x.\sigma(j_0,x)$ 就是我们想要的那个 $g$ .

由于 $\no\in\p$ 所以我们可以取这样的 $g$ 使得对于任意 $e$ 均有 $W_{g(e)}=\no[W_e]$ , 于是可以构造函数
$$
\psi_A:=\l x.\o(g(x))
$$
则对于满足 $W_e\subseteq A$ 的 $e$ 我们有 $\psi_A(e)\in A-W_e$ , 从而 $\psi_A$ 是 $A$ 集的产生函数, 从而 $A$ 是产生集.

##### I.85

$$
f:=\l x.((\mu q)T^{(1)}(x,(q)_0,(q)_1))_0
$$

实际上这就是在用 $q$ 来遍历全体的自然数对 $(y,z)$ 直到 $(x,y,z)\in T^{(1)}$ , 即 $\bb x(y)\dd$ .

##### I.86

$$
Sel^{(n)}:=\l a\vec y_n.((\m q) T^{(n+1)}(a,(q)_0,\vec y_n,(q)_1))_0
$$

##### I.87

($\Rightarrow$) $f$ 是部分递归函数故存在 $i_0\in\Phi$ 使得 $\bb{i_0}=f$ , 从而我们取原始递归谓词
$$
F:=\l\xn yz.T^{(n)}(i_0,\xn,\la{y,z})
$$
则显然对于任意 $y\in\N$ 我们有
$$
y=f(\xn)\iff(\ex z)F(\xn,y,z)
$$
因此根据 I.8.49 可得 $\l \xn y.y=f(\xn)$ 是半递归的.
($\Leftarrow$) 设函数 $\l y\xn.g\in\p$ 使得对于任意 $\xn,y\in\N$ 均有 $y=f(\xn)\iff g(y,\xn)\dd$ , 则取 $g$ 的指标 $i'$ , 则取函数
$$
f':=\l\xn.Sel^{(n)}(i',\xn)
$$
显然 $f'\in\p$ , 由 I.86 可得对于任意 $\xn\in\N$ , 如果 $f(\xn)\dd$ , 那么存在唯一 $y$ 使得 $y=f(\xn)$ , 从而 $f'(\xn)\dd$ 且 $f'(\xn)=f(\xn)$ ; 而另一方面如果 $f(\xn)\aa$ , 那么 $f'(\xn)\aa$ . 因此 $f'=f$ 从而 $f\in\p$ .

 ##### I.88

令谓词
$$
R:=\l c\xn.\bigvee_{i=1}^k(c=i)\and R_i(\xn)
$$
则由 I.8.48 可得 $R\in\p_*$ 于是令其指标为 $j_0$ , 则我们可以构造出一个选择函数
$$
\I:=\l\xn.Sel^{(n)}(j_0,\xn)
$$
之后对于每个 $r\le k$ , 由于 $f_r\in\p$ 故可以令其指标为 $i_r$ , 即对于每个 $r$ 均有 $\bb{i_r}=f_r$ , 之后我们可以进一步构造出如下的一个部分递归函数(因为它是有穷的, 所以总是可以构造的)
$$
\bl
i:\bb{1,2,...,k}&\to\{i_r:1\le r\le k\}\\
x&\mapsto i_x
\el
$$
之后我们就可以构造目标函数了
$$
f:=\l\xn.\U n(i(\I(\xn)),\xn)
$$
并且可以验证它满足我们的要求.

##### I.89

首先假定 $\re$ 集 $R\subseteq \N^n$ 的指标是 $a$ , 由于 $0\notin\Phi$ 故有 $\bb 0=\empty$ , 即对于任意输入 $\bb 0$ 均发散, 之后假设原始递归函数 $m\mapsto\la{(m)_0,...,(m)_{n-1}}$ 的指标为 $i_0$ , 则考虑原始递归函数
$$
\I:=\l m.sw(T^{(n)}(a,(m)_0,...,(m)_{n-1},(m)_n),i_0,0)
$$
则部分递归函数 $f:=\l m.\U 1(\I(m),m)$ 满足要求.

##### I.90

我们把上一问中的 $\I$ 改造一下, 一是把 $a$ 也作为变量, 二是取 $n$ 为 $1$ , 并假设原始递归函数 $m\mapsto\la{(m_0)}$ 的指标为 $i_0^1$ , 那么可以得到原始递归函数
$$
\I^1:=\l ma.sw(T^{(1)}(a,(m)_0,(m)_1),i_0^1,0)
$$
则根据构造, 函数 $f:=\l ma.\U1(\I^1(m,a),m)$ 满足对于任意 $a\in\N$ 如果 $\bb a$ 是一元函数(根据约定此时集合 $\bb{x\in\N:\bb a(x)\dd}$ 也可以写作 $W_a$ ), 那么 $\ran \l m.f(m,a)=\bb{\la x:\bb a(x)\dd}$ , 我们再将其解码从而得到一个部分递归函数 $f':=\l ma.(f(m,a))_0$ , 它满足对于任意的 $a\in\N$ 均有 $\ran \l m.f'(m,a)=W_a$ , 假设 $f'$ 的指标为 $q_0$ , 那么由 S-m-n 定理, 函数 $\l a.\sigma(q_0,a)$ 就是我们想要的那个 $h$ .

##### I.91

为达到这个要求我们需要再次改造我们的指标投送函数 $\I$ , 具体的, 我们需要把 I.8.51 中的 $(\oth)$ 的情形改造成一个和 $a$ 直接相关的项, 而不是凭空指定一个 $W_a$ 中的元素, 为此我们可以使用 I.85 . 设我们在 I.85 中构造的函数为 $\l x.\tau$ , 则可以假定函数 $\l xy.\la{\tau(y)}$ 的指标为 $j_0$ . 之后令函数 $(m,a)\mapsto\la{(m)_0}$ 的指标为 $i_1^1$ , 之后改造指标投送函数
$$
\I^2:=\l  ma.sw(T^{(1)}(a,(m)_0,(m)_1),i_1^1,j_0)
$$
则函数 $f:=\l ma.\U2(\I^2(m,a),m,a)$ 满足, 对于固定的 $a\in\N$ 以及任意输入 $x\in\N$ 
$$
f(x,a)=\left\{\bl
&\la{(x)_0}&\if&T^{(1)}(a,(x)_0,(x)_1)\\
&\la{\tau(a)}&&\oth
\el\right.
$$
而根据 $\tau$ 的构造如果 $W_a\not=\empty$ 则 $\tau(a)\dd$ 且 $\tau(a)\in W_a$ , 因此此时对于任意 $x$ 均有 $f(x,a)\dd$ , 故 $\l x.f(x,a)\in\r$ , 我们设 $f$ 的指标为 $q_1$ , 则函数 $\l a.\sigma(q_1,a)$ 就是我们想要的 $h$ .

##### I.92

由于我们实际上无法简单的去假设 $\bb x$ 是几元函数, 因此我们需要构造一个通用的 Kleene T-Predicate . 令谓词
$$
T:=\l exz.{\rm Computation}((z)_1)\and\la{e}*x*\la{(z)_0}\in (z)_1
$$
因此对于任意 $n,e,\xn,z\in\N$ 我们有
$$
T^{(n)}(e,\xn,z)\iff T(e,\la{\xn},z)
$$
之后我们可以形式化 $y\in\ran\bb x$ , 首先我们可以知道函数 $\bb x$ 的元数是 $(x)_1$ , 因此
$$
\bl
y\in\ran\bb x&\iff(\ex m\in \N^{(x)_1})\bb x(m)=y\\
&\iff (\ex m\in\N^{(x)_1})(\ex z)T^{(x)_1}(x,m,\la{y,z})\\
&\iff (\ex m')(\ex z)T(x,m',\la{y,z})


\el
$$
当然我们可以把两个存在量词压缩在一起, 从而 $y\in\ran\bb x$ 是一个部分递归谓词, 因此可以假定它的指标为 $i_0$ , 之后应用 S-m-n 定理, 得到对于任意的 $x,y\in\N$ , 我们有
$$
\bb{i_0}(x,y)=\bb{\sigma(i_0,x)}(y)
$$
即
$$
\bl
y\in\ran\bb x&\iff\bb{i_0}(x,y)\dd\\
&\iff\bb{\sigma(i_0,x)}(y)\dd\\
&\iff y\in\dom\bb{\sigma(i_0,x)}
\el
$$
因此这个 $\l x.\sigma(i_0,x)$ 就是我们想要的函数 $\sigma$ .

##### I.93

取 I.91 构造的 $\l x.h$ , I.92 构造的 $\l x.\sigma$ , 则取函数
$$
\tau:=\l x.h(\sigma(x))
$$
由 I.91 可得对于任意 $x\in\N$ , $\ran\bb x=W_{\sigma(x)}$ , 再由 I.91 可得 $W_{\sigma(x)}=\ran\bb{h(\sigma(x))}$ , 从而我们有
$$
\ran\bb x=\ran\bb{\tau(x)}
$$
更进一步, 若 $\ran\bb x$ 非空, 则 $W_{\sigma(x)}=\ran\bb x$ 非空, 从而根据 I.91 我们有 $\bb{h(\sigma(x))}\in\r$ , 满足要求.

##### I.94

($\Rightarrow$) 设 $R\subseteq\N$ 是非空递归集, 则它的特征函数 $\l x.\chi_R$ 是递归函数, 取 $R$ 中最小的元素 $a$ , 之后我们希望构造一个递归函数 $\l x.f'\in\r$ , 满足对于任意的 $x\in\N$ 
$$
f'(x)=\left\{\bl
&a&\if&x=0\\
&x&\if&x>0\and \chi_R(x)=0\\
&f'(x-1)&&\oth
\el\right.
$$
借助前面的习题中应用递归定理的技术我们可以构造生成 $f'$ 的函数
$$
F:=\l zx.\left\{
\bl
&a&\if&x=0\\
&x&\if&x>0\and\chi_R(x)=0\\
& U^{(1)}(z,x\ \dot-\  1)&&\oth
\el
\right.
$$
并取满足 $\l x.F(e,x)=\bb{e}$ 的指标 $e\in\Phi$ , 则可以验证 $\bb e=f'$ , 从而 $f'\in\p$ , 而显然 $f'$ 是全函数, 故 $f'\in\r$ , 并且根据构造 $R=\ran f'$ , 因此单调不降的递归函数 $f'$ 即为题目所求.
($\Leftarrow$) 设 $\l x.f'\in\r$ 是单调不降的, 并且 $R=\ran f'$ , 首先显然有 $f'(0)\in R$ , 故 $R$ 非空. 如果 $R$ 有穷, 那么显然 $R$ 是递归集, 所以我们仅关注 $R$ 是无穷集的情形, 令部分递归函数
$$
\fd:=\l y.(\m x)[f'(x)\ge y]
$$
由于 $R$ 是无穷集, 故对于任意 $y\in\N$ 存在 $r\in R$ 使得 $r\ge y$ , 因而对于任意 $y$ 都有 $\fd(y)\dd$ , 故 $\fd\in\r$ . 之后我们可以构造函数
$$
f:=\l x.[f'(\fd(x))=x]
$$
因为对于每个 $x$ 而言, $f'(\fd(x))$ 是 $R$ 中最小的不小于 $x$ 的元素, 如果 $x\in R$ , 那么结果就是 $x$ 本身, 所以 $f$ 就是 $R$ 的特征函数.

##### I.95

($\Rightarrow$) 令递归集 $R$ 为无穷集, 并取 $R$ 中的最小值 $a$ , 则我们可以构造如下函数
$$
F:=\l zx.\left\{
\bl
&a&\if&x=0\\
&(\m y)[\chi_R(y)\and y>\U1(z,x\ \dot-\ 1)]&&\oth
\el
\right.
$$

之后我们取递归定理的 $e\in\Phi$ 使得 $\l x.F(e,x)=\bb e$ , 则可以通过归纳法来证明对于任意的 $x\in\N$ 均有 $\bb e(x)\dd$ , 因此 $\bb e\in\r$ , 并且事实上 $\bb e$ 就是从小到大遍历 $R$ 中的元素, 它是严格增的并且满足 $\ran\bb e=R$ .
($\Leftarrow$) 同理 I.94 .

##### I.96

我们仅说明一元集的情形, $R$ 是半递归的, 因此它是 $\re$ 的, 故存在 $f\in\r$ 使得 $R=\ran f$ , 则我们构造函数
$$
F:=\l zx.\left\{
\bl
& f(0)&\if& x=0\\
&f((\m y)[f(y)>\U1(z,x\ \dot-\ 1)])&&\oth
\el
\right.
$$
取 $e\in\Phi$ 使得 $\bb e=\l x.F(e,x)$ , 则可以验证 $\bb e\in\r$ , 并且 $\bb e$ 是严格增的, 由 I.97 可得 $\ran\bb e\subseteq\dom f=R$ 是递归的.

##### I.97

我们需要改造 I.96 中的构造, 从而适配 $W_{(\cdot)}$ 的编号规则. 令函数
$$
F^*:=\l zex.\left\{
\bl
&\U1(e,0)&\if&x=0\\
&\U1(e,(\m y)[\U1(e,y)>\U2(z,e,x\ \dot-\ 1)])&&\oth
\el
\right.
$$
 显然 $F^*\in\p$ 故存在 $z_0\in\Phi$ 使得 $\bb{z_0}=\l ex.F^*(e,z_0,x)$ , 取 I.91 中构造的函数 $\l x.h$ , 并将其复合进 $\bb{z_0}$ 中, 得到函数
$$
{\cal B}:=\l ex.\bb{z_0}(h(e),x)
$$
对于 $a\in\N$ , 由 I.91 可得 $W_a=\ran\bb{h(a)}$ 并且如果 $W_a$ 是无穷集则 $\bb{h(a)}\in\r$ , 此时固定 $a$ , 记 $\bb{h(a)}$ 为 $f_a$ , 则我们有
$$
{\cal B}(a,x)=\left\{
\bl
&f_a(0)&\if&x=0\\
&f_a((\m y)[f_a(y)>{\cal B}(a,x\ \dot-\ 1)])&&\oth
\el
\right.
$$
并且对于所有 $x$ 均有 ${\cal B}(a,x)\dd$ , 因此 $\l x.{\cal B}(a,x)\in\r$ , 并且它是严格增的, 故它的值域是 $W_a$ 的递归子集, 令 $\cal B$ 的指标为 $r_0\in\Phi$ , 则应用 S-m-n 定理得到的原始递归函数 $\l a.\sigma(r_0,a)$ 即为题目所求的函数 $m$ .

##### I.98

根据以往的经验我们只需要说明关系 $\l uxy.u\in W_x\cap W_y$ 是半递归的即可.
$$
\bl
u\in W_x\cap W_y&\iff (\ex z)(\ex z')T(x,\la u,z)\and T(y,\la u,z')\\
&\iff(\ex z)T(x,\la u,(z)_0)\and T(y,\la u,(z)_1)
\el
$$
故存在 $i_0\in\Phi$ 使得对于任意 $u,x,y\in\N$ 有 $u\in W_x\cap W_y\iff \bb{i_0}(u,x,y)\dd$ , 之后应用 S-m-n 定理即可得到对于任意 $x,y\in\N$ 
$$
\l u.\bb{i_0}(u,x,y)=\bb{S^2_1(i_0,x,y)}
$$
从而原始递归函数 $\l xy.S^2_1(i_0,x,y)$ 就是题目所求的函数 $h$ .

##### I.99

同理于 I.98 .

##### I.100

$$
\bl
u\in W_x\times W_y&\iff (\ex z)(\ex z')z\in W_x\and z'\in W_y\and u=\la{z,z'}
\el
$$

则根据 I.8.48 可得关系 $\l uxy. u\in W_x\times W_y$ 是半递归的, 之后同理 I.98 .

##### I.101

由于 $K$ 是半递归的, 故关系 $\l xy. y\in K\and y\ge x$ 也是半递归的, 因此存在 $\l xy.f\in\p$ 使得对于任意 $x,y\in\N$
$$
y\in K\and y\ge x\iff f(x,y)=0
$$
若 $\p$ 对无规则取 $\min$ 封闭, 由于 $K$ 是无穷集, 则函数
$$
f_{\min y}:=\l x.\left\{
\bl
\min\bb{&y:y\in K\and y\ge x}&\if&\text{这样的 $y$ 存在}\\
&\aa&&\oth
\el
\right.
$$
是全函数, 因此 $f_{\min y}\in\r$ , 那么我们就可以用递归函数 $\l x.f_{\min y}(x)=x$ 来判定 $x$ 是否在 $K$ 中, 这与 $K$ 的不可判定性矛盾.

##### I.102

若存在, 假定其为 $\l x.f$ , 则显然函数 $\l x.f(x)+1$ 也是递归函数, 假定其指标为 $i_0$ , 则根据假设, 对于任意 $x\in K$ 
$$
\bb{i_0}(x)=f(x)+1=\bb x(x)+1
$$
则 $i_0\notin K$ , 则 $\bb{i_0}(i_0)\aa$ , 这与 $\bb{i_0}\in\r$ 矛盾.