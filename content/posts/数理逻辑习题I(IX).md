---
title: "数理逻辑习题I(IX)"
date: 2026-07-31T00:00:00+08:00
tags: []
math: true
draft: false
---

-----------------------------------------------------------------
$$
\newcommand{\lra}{\leftrightarrow}
\newcommand{\fa}{\forall}
\newcommand{\ex}{\exists}
\newcommand{\r}{\mathfrak{R}}
\newcommand{\bl}{\begin{aligned}}
\newcommand{\el}{\end{aligned}}
\newcommand{\t}{ {\bf t} }
\newcommand{\f}{ {\bf f} }
\newcommand{\eq}{\equiv}
\newcommand{\la}[1]{\langle #1\rangle}
\newcommand{\ov}[1]{\overline{#1}}
\newcommand{\m}{\mu}
\newcommand{\st}{{\mathrm{st}}}
\newcommand{\p}{\mathfrak{P}}
\newcommand{\l}{\lambda}
\newcommand{\xn}{{\vec x_n}}
\newcommand{\xm}{{\vec x_m}}
\newcommand{\dd}{\downarrow}
\newcommand{\aa}{\uparrow}
\newcommand{\x}{\vec x}
\newcommand{\if}{\mathbf{if}\quad}
\newcommand{\oth}{\mathbf{otherwise}}
\newcommand{\bb}[1]{\{#1\}}
\newcommand{\U}[1]{U^{(#1)}}
\newcommand{\no}{\o^{-1}}
\newcommand{\dom}{\mathrm{dom}\ }
\newcommand{\ran}{\mathrm{ran}\ }
\newcommand{\o}{\mathcal O}
\newcommand{\re}{{\bf r.e.}}
\newcommand{\I}{\mathcal I}
\newcommand{\fd}{\mathscr{Find}}
\newcommand{\lcm}{\mathrm{lcm}}
\newcommand{\n}{\mathfrak{N}}
\newcommand{\rob}{\mathbf{ROB}}
\newcommand{\w}[1]{\widetilde{#1}}
\newcommand{\uc}[1]{\ulcorner{#1}\urcorner}
\newcommand{\iff}{\quad\mathrm{iff}\quad}
\newcommand{\imp}{\quad\mathrm{implies}\quad}
\newcommand{\T}{\mathbf{T}}
\newcommand{\th}{\mathscr{T}}
\newcommand{\tr}{\mathbb{True}}
\newcommand{\A}{\mathcal{A}}
\newcommand{\B}{\mathcal{B}}
\newcommand{\Q}{\mathcal{Q}}
\newcommand{\P}{\mathcal{P}}
\newcommand{\R}{\mathcal{R}}
\newcommand{\F}{\mathcal{F}}
\newcommand{\G}{\mathcal{G}}
\newcommand{\H}{\mathcal{H}}
$$
----------------------------------------------------------

##### I.103

首先我们有放缩
$$
(x+y)^2\le (x+y)^2+x<(x+y+1)^2
$$
故对于任意 $x,y\in\N$ 我们有
$$
\left\lfloor\sqrt{J(x,y)}\right\rfloor=x+y
$$
记函数$q:=\l z.\lfloor\sqrt{z}\rfloor$ , 则 $J(x,y)-q(J(x,y))^2=x$ , 从而函数 $K:=\l z.z-q(z)^2,L:=\l z.q(z)-K(z)$ 即可. 

##### I.104

trivial.

##### I.105

令
$$
J:=\l xy.\max(x,y)^2+[x<y]\cdot x+[x\ge y]\cdot (y+\max(x,y))
$$

之后令
$$
K:=\l z.\min\{z-q(z)^2,q(z)\},L:=\l z.\min(2q(z)-(z-q(z)^2),z-q(z)^2)
$$
即可.

##### I.106

首先 $\l xy.\gcd$ 是原始递归函数, 我们可以通过 bounded-$\m$ 配合 $\l xy.x|y$ 得到它, 从而固定长度的最小公倍数函数也是原始递归的, 之后我们可以通过原始递归来得到函数 $p:c\mapsto\lcm\{1,2,...,c+1\}$ , 这是因为 $p(c+1)=\lcm\{p(c),c+1\}$ , 从而 $\l c.p\in\p\r$ .
	对于固定的输入长度 $n$ , 函数 $\vec a_n\mapsto\max\{1+J(0,n),1+J(1,a_1),...,1+J(n,a_n)\}$ 是原始递归的, 记 $\l c.p$ 与它的复合为 $\l\xn.\zeta$ , 之后我们可以构造函数
$$
q':=\l\xn.\lcm\{1+(1+J(1,x_1))\cdot\zeta(\xn),...,1+(1+J(n,x_n))\cdot \zeta(\xn)\}
$$
之后令 $q:=\l\xn.\lcm\{q'(\xn),1+(1+J(0,n))\cdot\zeta(\xn)\}$ 则 $\l\xn.q$ 是满足编码信息但是没有最小性的函数, 并且它是原始递归的, 好处是我们获得了一个上界, 因此我们可以用 bounded-$\m$ 来完成最小性的要求, 从而可以构造出函数
$$
\la{...}:=\l\xn.(\m z)_{\le q(\xn)}[\beta(z,0)=n\and\bigwedge_{i=1}^n\beta(z,i)=x_i]
$$
由于 $\l xy.\beta$ 是原始递归的, 所以编码函数也是原始递归的.

##### I.107

我们仅说明归纳步骤.
	假定 $t\eq f(t_1,...,t_n)$ , 则 $t^\n=f^\n(t_1^\n,...,t_n^\n)$ , 根据 I.H. 我们有 $\rob\vdash t_i=\w{t_i^\n}$ 从而由 Leibniz 替换规则可以得到 $\rob\vdash t=f(\w{t_1^\n},...,\w{t_n^\n})$ . 如果 $f$ 是 $S$ 函数, 则我们有 $t\eq S(t_1)$ , 则根据定义此时 $S(\w{t_1^\n})$ 就是 $\w{t^\n}$ ; 如果 $f$ 是 $+$ 函数, 则由 $\rob({+_2})$ 可得对于任意 $a,b\in\N$ 均有 $\rob\vdash\w a+\w b=\w{a+b}$ , 故此时也有 $\rob\vdash t=\w{t^\n}$ ; 乘法函数的情形同理. 

##### I.108

构造模型
$$
\n':=(\N\cup\{\infin\};0;S^*,\times^*,+^*;<^*)
$$
其中我们把自然数的 $S,\times,+,<$ 分别对加入的 $\omega$ 进行扩充: 对于任意 $x\in\N^+$ , $x+^*\infin=x\times^*\infin=\infin$ , 特殊的情况是 $S^*(\infin)=\infin,0+^*\infin=\infin,0\times^*\infin=0$ 并且我们要求 $\infin<^*\infin$ , 可以验证 $\n'\vDash\rob$ .

##### I.109

构造模型 $\n':=(\N\cup\{\omega+i:i\in\N\}\cup\{\infin\};0;S,\times,+;<)$ 其中 $+,\times,S,<$ 直接取序数的运算即可.

##### I.110

我们对 $y$ 施以归纳来证明, 公式 $\A:\eq x\times y=z$ 定义之.
	当 $y=0$ 时, 当 $z=0$ 时, 由 $\rob(\times_1)$ 可以得到 $\rob\vdash\w x\times \w y=0$ , 当 $z\not=0$ 时, 显然我们有 $\rob\vdash\neg 0=\w z$ 从而有 $\rob\vdash\neg\w x\times\w y=\w z$ .
	当 $y=q+1$ 时则 $\rob\vdash\w x\times\w y=\w x\times S\w q$ 从而有 $\rob\vdash\w x\times\w y=\w x\times\w q+\w x$ , 由 I.H. 以及加法的 $\rob$ 可表示性可以立即得出.

##### I.111

trivial.

##### I.112

trivial.

##### I.113

显然 $\uc\rob$ 是递归集, 所以 $\Theta_\rob$ 是 $\re$ 集, 考虑构造原始地归函数 $g:=\l x.\uc{\A(\w x)}$ , 则我们有
$$
n\in A\iff g(n)\in\Theta_\rob
$$
因此 $A\subseteq\N$ 是 $\re$ 集.

	如果我们去掉 positively , 那么对于 $x\in\N$ 我们可以借助 $\m$ 算符来枚举证明序列 $m$ 的编码直到它证明了 $\A(\w x)$ 或 $\neg\A(\w x)$ , 由二值性我们知道这样的 $m$ 一定存在, 所以我们构造出了一个递归函数来判别 $\A(\w x)$ 与 $\neg\A(\w x)$ 谁是内定理. 因此 $A$ 是递归的, 所以也必然是 $\re$ 的.
	
	逆命题是正确的, 若 $A$ 是 $\re$ 集, 则存在原始递归集 $\l xy.Q$ 使得 $A(x)\lra(\ex y)Q(x,y)$ , 而我们知道 $Q$ 是 $\rob$ 中强可定义的, 令 $\Q(x,y)$ 表示之, 则考虑公式 $(\ex y)\Q(x,y)$ , 若 $x\in A$ , 则存在 $z$ 使得 $Q(x,z)$ , 根据 $\Q$ 的定义有 $\rob\vdash \Q(\w x,\w z)$ , 从而 $\rob\vdash(\ex y)\Q(\w x,y)$ ; 令一方面, 若 $x\notin A$ , 我们通过模型论的方法来说明 $\rob\not\vdash(\ex y)\Q(\w x,y)$ , 此时我们只需要证明 $\rob\cup\{\neg(\ex y)\Q(\w x,y)\}$ 是一致的即可, 考虑标准在标准模型中, 由于 $x\notin A$ , 故 $\neg(\ex y)Q(x,y)$ , 而由于 $\Q$ 在 $\n$ 中定义 $Q$ , 故我们有 $\n\vDash\neg(\ex y)\Q(\w x,y)$ , 从而这个公式和 $\rob$ 是一致的.

##### I.114

显然不. 不然他们就不是 recursively inseparable 的.

##### I.115

利用 I.113 第二问的技术, 我们来枚举证明序列并回答它是 $\neg\A$ 还是 $\A$ 的证明序列, 由于拓展完全所以符合要求的证明序列一定存在, 因此这个枚举会停机, 因而是递归的.

##### I.116

由于 $K$ 是 $\re$ 的, 由 I.113 存在形如 $(\ex z)Q(x,z)$ 的公式 $K_*$ 在 $\rob$ 中正向强定义之, 其中 $Q$ 是 $\rob$ 中强定义某个原始递归关系的公式, 接下来我们考虑说明这个集合在 $\Gamma$ 中也是正向强可定义的.
###### Lem 1.  若关系 $\l x.R\in\r_*$ , 则它在 $\Gamma$ 中是强可定义的.

> 令 $\R$ 在 $\rob$ 中强定义之, 则对于任意 $n\in\N$ 
> $$
> \bl
> R(n)&\iff \rob\vdash\R(\w n)\\
> \neg R(n)&\iff\rob\vdash\neg\R(\w n)
> \el
> $$
> 而我们有 $\rob\subseteq\Gamma$ , 故 $\R$ 亦在 $\Gamma$ 中强定义 $R$ .

###### Lem 2.  所有 $\re$ 关系 $\l x.R$ 都是 $\Gamma$ 中正向强可定义的.

> 取关系 $\l xz.Q\in\r_*$ 使得 $R(x)\lra(\ex z)Q(x,z)$ , 并令公式 $\Q(v_0,v_1)$ 在 $\Gamma$ 中强表示 $Q$ , 于是可以构造公式 $\R(v_0):\eq(\ex v_1)\Q(v_0,v_1)$ , 对于 $x\in\N$ 
> 	若 $R(x)$ , 则存在 $z\in\N$ 使得 $Q(x,z)$ , 因此有 $\Gamma\vdash\Q(\w x,\w z)$ , 从而 $\Gamma\vdash(\ex v_1)\Q(\w x,v_1)$ 即 $\R(\w x)$ .
> 	若 $\Gamma\vdash(\ex v_1)\Q(\w x,v_1)$ , 由 $\Gamma$ 的 $\omega$-consistency 可得存在 $z\in\N$ 使得 $\Gamma\not \vdash\neg\Q(\w x,\w z)$ , 由 Lem 1 可知这等价于 $\neg\neg Q(x,z)$ 即 $Q(x,z)$ , 故 $(\ex z)Q(x,z)$ 即 $R(x)$ .

于是我们可以自然地在 $\Gamma$ 中延用公式 $K_*$ , 之后为导出矛盾我们假设 $\Gamma$ 是完备的, 于是考虑集合 $\ov K$ , 对于任意 $x\in\N$ 
$$
\bl
x\in\ov K&\iff x\notin K\\
&\iff \Gamma\not\vdash K_*(\w x)\\
&\iff \Gamma\vdash\neg K_*(\w x)\\
&\iff \uc{\neg K_*(\w x)}\in\Theta_\Gamma
\el
$$
显然函数 $\l n.\uc{\neg K_*(\w n)}$ 是原始递归的, 而由于 $\uc\Gamma\in\r_*$ , 故 $\Theta_\Gamma$ 是 $\re$ 的, 于是这就意味着 $\l x.x\in\ov K$ 是 $\re$ 的, 这与先前的结果矛盾了.
##### I.Extra

我们可以构造出无穷谓词, 它可以帮助我们在 $L_\mathfrak{A}$ 中区别自然数与非标准自然数.
$$
\inf(x):\eq (0<x\and (\fa y)(y<x\to S(y)<x))
$$

##### I.117

令公式 $\F(y,\xn)$ 在 $\Gamma$ 中作为函数形式化地定义全函数 $\l\xn.f$ , 则对于任意 $\vec a_n\in\N^n$ 我们显然有 $\Gamma\vdash\F(y,\w a_1,...,\w a_n)\lra y=\w{f(\vec a_n)}$ , 假设对于某个 $b\in\N$ 满足 $b\not=f(\vec a_n)$ 且 $\Gamma\vdash\F(y,\w a_1,...,\w a_n)\lra y=\w b$ , 则我们可以导出 $\Gamma\vdash\w{f(\vec a_n)}=\w b$ , 这与 $\rob\vdash\neg\w{f(\vec a_n)}=\w b$ 不一致, 因而有 $\Gamma\not\vdash\F(y,\w a_1,...,\w a_n)\lra y=\w b$ .

##### I.118

($\Rightarrow$) 令公式 $\F(y,\xn)$ 作为函数定义 $\l\xn.f$ , 则对于任意 $b,\vec a_n\in\N$ , 若 $b=f(\vec a_n)$ , 则 $\Gamma\vdash\F(\w b,\w a_1,...,\w a_n)$ ; 而若 $b\not=f(\vec a_n)$ , 则 $\Gamma\vdash\F(\w b,\w a_1,...,\w a_n)\lra\w b=\w{f(\vec a_n)}$ , 从而 $\Gamma\vdash\neg\F(\w b,\w a_1,...,\w a_n)$ . 因此公式 $\F$ 恰好能够定义 $f$ 的图. 并且对于 $b=f(\vec a_n)$ , $\Gamma\vdash\F(y,\w a_1,...,\w a_n)\lra y=\w b$ 天然蕴涵 $\Gamma\vdash\F(y,\w a_1,...,\w a_n)\to y=\w b$ .
	($\Leftarrow$) 令 $\F(y,\xn)$ 满足如下要求, 则对于任意的 $b,\vec a_n\in\N$ , 若 $b=f(\vec a_n)$ 则 $\Gamma\vdash\F(\w  b,\w a_1,...,\w a_n)$ , 从而根据逻辑公理有 $\vdash y=\w b\to(\F(\w b,\w a_1,...,\w a_n)\lra\F(y,\w a_1,...,\w a_n))$ , 从而有 $\Gamma\vdash y=\w b\to\F(y,\w a_1,...,\w a_n)$ , 而另一个方向则直接由 (ii) 提供, 从而 $\Gamma\vdash\F(y,\w a_1,...,\w a_n)\lra y=\w b$ .

##### I.119

令公式 $\F(y,\xn)$ 定义函数的图 $\l y\xn.[y=f(\xn)]$ , 则构造公式
$$
\G(y,\xn):\eq \F(y,\xn)\and(\fa z)_{<y}\neg\F(z,\xn)
$$
我们接下来说明 $\G$ 在 $\Gamma$ 中作为函数定义了 $f$ . 对于任意的 $b,\vec a_n\in\N$ , 若 $b=f(\vec a_n)$ , 由于 $\F$ 定义了 $f$ 的图, 故 $\Gamma\vdash\F(\w b,\w a_1,...,\w a_n)$ , 而另一方面, 对于任意 $z<b$ 我们有 $\Gamma\vdash\neg\F(\w z,\w a_1,...,\w a_n)$ , 从而由 I.9.44 可得 $\Gamma\vdash z<\w b\to \neg\F(z,\w a_1,...,\w a_n)$ , 再由概括定理可得 $\Gamma\vdash (\fa z)_{<\w b} \neg\F(z,\w a_1,...,\w a_n)$ , 故 $\Gamma\vdash\G(\w b,\w a_1,...,\w a_n)$ , 因此我们有 $\Gamma\vdash y=\w b\to\G(y,\w a_1,...,\w a_n)$ ; 之后我们再来证明 $\Gamma\vdash\neg y=\w b\to\neg\G(y,\w a_1,...,\w a_n)$ , 显然箭头的右边等价于 $\neg\F(y,\w a_1,...,\w a_n)\or(\ex z)_{<y}\F(z,\w a_1,...,\w a_n)$ , 由 $\rob(<_3)$ 可得 $\Gamma\vdash \neg y=\w b\to y<\w b\or \w b<y$ , 而我们显然有 $\Gamma\vdash\w b<y\to (\ex z)_{<y}\F(z,\w a_1,...,\w a_n)$ 故 $\Gamma\vdash\w b<y\to\neg\G(y,\w a_1,...,\w a_n)$ , 而同理上文中使用 I.9.44 的方法我们还可以得到 $\Gamma\vdash y<\w b\to \neg\F(y,\w a_1,...,\w a_n)$ 从而 $\Gamma\vdash y<\w b\to\neg \G(y,\w a_1,...,\w a_n)$ , 因此由 Prove by cases 可得 $\Gamma\vdash\neg y=\w b\to \neg\G(y,\w a_1,...,\w a_n)$ , 从而我们有 $\Gamma\vdash y=\w b\lra\G(y,\w a_1,...,\w a_n)$ , 故 $\G$ 在 $\Gamma$ 中作为函数定义了 $f$ .

##### I.120

由 I.119 , 存在公式 $\F(y,x)$ 在 $\Gamma$ 中作为函数定义 $f$ , 于是对于公式 $\A(x)$ , 我们构造公式
$$
\B(x):\eq(\ex z)\F(z,x)\and \A(z)
$$
则对于任意的 $n\in\N$ , 因为 $\Gamma\vdash\F(\w{f(n)},\w n)$ 所以根据重言规则有 $\Gamma\vdash \A(\w{f(n)})\to\F(\w{f(n)},\w n)\and\A(\w{f(n)})$ 以及 $\vdash \F(\w{f(n)},\w n)\and\A(\w{f(n)})\to(\ex z)\F(z,\w n)\and\A(z)$ , 从而 $\Gamma\vdash\A(\w{f(n)})\to\B(\w n)$ ; 另一方面, 由于 $\F$ 在 $\Gamma$ 中作为函数定义 $f$ 所以我们有 $\Gamma\vdash \F(z,\w n)\lra z=\w{f(n)}$ , 因此我们有 $\Gamma\vdash\B(\w n)\lra (\ex z)z=\w{f(n)}\and \A(z)$ , 接下来我们证明 $\Gamma\vdash\neg\A(\w{f(n)})\to\neg\B(\w n)$ , 由我们先前的结论, 箭头右边等价于 $(\fa z)z=\w{f(n)}\to\neg\A(z)$ , 根据逻辑公理我们有 $\vdash z=\w{f(n)}\to(\neg\A(\w{f(n)})\to\neg\A(z))$ , 而显然有 $\vDash_{\bf Taut}\P\to(\Q\to\R)\lra\Q\to(\P\to\R)$ , 所以我们有 $\vdash\neg\A(\w{f(n)})\to(z=\w{f(n)}\to\neg\A(z))$ 再应用 $\fa$-introduction 即可得到 $\vdash\neg\A(\w{f(n)})\to\neg\B(\w n)$ , 从而我们有 $\Gamma\vdash\B(\w n)\lra\A(\w{f(n)})$ .

##### I.121

(1) 首先考虑独立于递归论的证法, 钦定 $A$ 被公式 $\A(x)$ 正向强定义, 则对于任意的 $n\in\N$ 我们有
$$
\bl
n\in f^{-1}[A]&\iff f(n)\in A\\
&\iff \rob\vdash\A(\w{f(n)})
\el
$$
而 I.120 告诉我们存在公式 $\B(x)$ 使得对于任意的 $a\in\N$ 均有 $\rob\vdash\A[\w{f(n)}]\lra\B(\w n)$ , 因此我们有
$$
\bl
n\in f^{-1}[A]&\iff \rob\vdash\A(\w{f(n)})\\
&\iff \rob\vdash\B(\w n)

\el
$$
从而集合 $f^{-1}[A]$ 被公式 $\B$ 在 $\rob$ 中正向强定义.
	(2) 之后我们给出递归论证法, 由 I.113 及其逆命题, 在 $\rob$ 中正向强可定义集与 $\re$ 集描述的是同一个类. 因此 $A$ 是 $\re$ 的, 我们仅需要证明 $f^{-1}[A]$ 是 $\re$ 的, 由 I.119 可得函数 $f$ 的图是 $\rob$ 中可定义, 之后我们考虑一个引理
###### Lem 1.  若 $R\subseteq\N$ 是 $\rob$ 中可定义的, 那么它也是 $\rob$ 中强可定义的

> 根据假设, 存在公式 $\R(x)$ 使得对于任意的 $n\in\N$ 
> $$
> \bl
> R(n)&\imp \rob\vdash \R(\w n)\\
> \neg R(n)&\imp\rob\vdash\neg\R(\w n)
> \el
> $$
>
> 因此, 若 $\rob\vdash\R(\w n)$ , 则根据 $\rob$ 的一致性可得 $\rob\not\vdash\neg\R(\w n)$ , 从而必定有 $\neg\neg R(n)$ 即 $R(n)$ , 所以 $R(n)\ \ \mathrm{iff}\ \ \rob\vdash\R(\w n)$ , 借助类似的方法我们还可以证明 $\neg R(n)\ \ \mathrm{iff}\ \ \rob\vdash\neg\R(\w n)$ , 因此 $R$ 是 $\rob$ 中强可定义的.

因此 $f$ 的图是 $\rob$ 中强可定义的, 由 I.113 可得它是递归的, 因而 $f\in\r$ , 故 $f^{-1}\in\p$ , 所以 $f^{-1}[A]$ 是 $\re$ 集.
##### I.122

> 我服了, 对角化怎么这么困难...

根据提示, 函数 $D:=\l x.s(x,x)$ 是递归函数, 所以它的图是 $\rob$ 可定义的, 由 I.119 可得它是 $\Gamma$ 中作为函数可定义的, 于是对于 $L_{\frak A}$ 上的公式 $\A(v_0)$ , 由 I.120 存在公式 $\B(v_0)$ 使得对于任意 $a\in\N$ 我们有
$$
\Gamma\vdash\A(\w{D(a)})\lra\B(\w a)
$$
令 $q:=\uc{\B(v_0)}$ , 则根据 $D$ 的构造, $D(q)$ 所编码的语句 $\F$ 与 $\B(\w q)$ 等价, 于是取 $a$ 为 $q$ 可得
$$
\Gamma\vdash\A(\w{\uc\F})\lra\B(\w q)
$$
从而再由 $\Gamma\vdash\B(\w q)\lra\F$ 可得
$$
\Gamma\vdash\A(\w{\uc\F})\lra\F
$$
所构造的语句 $\F$ 即为公式 $\A(v_0)$ 的不动点.

##### I.123

若不然, 假定 $L_{\frak A}$ 上的公式 $\tr(v_0)$ 在 $\n$ 中定义了 $\T$ , 则考虑取公式 $\neg\tr(v_0)$ 的不动点 $\F$ , 则有
$$
\rob\vdash \F\lra\neg\tr(\w{\uc\F})
$$
而由 $\rob$ 的正确性可得 $\n\vDash\F\lra\neg\tr(\w{\uc\F})$ , 若 $\uc\F\in\T$ , 则 $\n\not\vDash\tr(\ov{\uc\F})$ 从而 $\uc\F\notin\T$ ; 然而另一方面若 $\uc\F\notin\T$ , 则 $\n\not\vDash\tr(\ov{\uc\F})$ , 然而同时根据 $\T$ 的完全性我们又有 $\uc{\neg\F}\in\T$ , 从而由不动点的性质可以得到 $\n\vDash\tr(\w{\uc\F})$ . 无论是那种情况都会产生矛盾, 所以 $\T$ 是不可定义的.

##### I.124

我们仅需证明 $\r'$ 关于原始递归封闭即可. 设 $\l\xn.f,\l\xn yz.g\in\r'$ , 考虑由 $f,g$ 原始递归得到的函数
$$
h:=\l\xn y.\left\{

\bl
&f(\xn)&\if&y=0\\
&g(\xn,y\ \dot-\  1,h(\xn,y\ \dot-\  1))&&\oth

\el
\right.
$$
借助编码函数, 只需要找到"模拟"计算的序列的编码即可, 具体来说就是找到最小的 $z$ 使得
$$
\bl
&\beta(z,0)=f(\xn)&\\
&\beta(z,i+1)=g(\xn,i,\beta(z,i))& \text{for all $0\le i<n$}
\el
$$
当然我们可以轻易证明 $\l ai.\beta\in\r'$ , 之后我们需要考虑模拟有界量词, 实际上我们可以考虑如下构造
$$
\bl
(\fa x)_{<y}f(x)=0\lra ((\m z)(\neg f(z)=0\or z=y))= y
\el
$$
其中 $\l xy.x=y$ 以及布尔操作 $\and,\or,\neg$ 均可以用 $\l xy.x+y,\l xy.xy,\l xy.x\ \dot-\ y$ 来实现. 而事实上由于 $f,g$ 都是全函数, 所以这样的计算模拟序列总是存在的, 所以我们可以得到 $h\in\r'$ , 因而 $\r\subseteq\r'$ , 从而可以得到 $\r=\r'$ .

##### I.125

由 I.9.41, I.9.42, I.9.46 可以得到除了 $\l xy.x\ \dot-\ y$ 的图的其他函数的图的可表示性, 而利用 $\l xy.x<y$ 我们也可以比较容易地得到 $\l xy.x\ \dot-\ y$ 的图的可表示性, 再由 I.119 可得所有归纳基础的函数都是 $\rob$ 作为函数可定义的.
	对于函数的复合, 令 $\l\xn.f,\l\xm.g_i(1\le i\le n)\in\r'$ , 假设这 $n+1$ 个函数的图分别被公式 $\F(y,\xn)$ 以及 $\G_i(y,\xm)(1\le i\le n)$ 作为函数定义, 则对于它们的复合 $h:=\l\xm.f(g_1(\xm),...,g_n(\xm))$ , 我们考虑公式
$$
\H(y,\xm):\eq(\ex\vec y_n)\F(y,\vec y_n)\and\bigwedge_{i=1}^n\G_i(y_i,\xm)
$$
对于任意的 $\vec a_m,b\in\N$ , 若 $b=h(\vec a_m)$ , 则我们取 $y_i:\eq \w{g_i(\vec a_m)}$ , 则由 I.H. 可得 $\rob\vdash \G_i(y_i,\w a_1,...,\w a_m)$ , 以及 $\rob\vdash\F(\w b,y_1,...,y_n)$ , 从而可以得到 $\rob\vdash\H(\w b,\w a_1,...,\w a_m)$ . 若 $b\not=h(\vec a_m)$ , 我们证明 $\neg\H$ , 它等价于 
$$
(\fa\vec y_n)\bigwedge_{i=1}^n\G_i(y_i,\w a_1,...,\w a_m)\to \neg\F(\w b,\vec y_n)
$$
由于 $\G_i$ 作为函数定义 $g_i$ , 故 $\rob\vdash\G_i(y_i,\w a_1,...,\w a_m)\lra y_i=\w{g_i(\vec a_m)}$ , 由 Leibniz 替换规则可得到上式的等价形式
$$
(\fa\vec y_n)\bigwedge_{i=1}^ny_i=\w{g_i(\vec a_m)}\to\neg\F(\w b,\vec y_n)
$$
仿照 I.120 的证明方法我们可以由 $\rob\vdash\neg\F(\w b,\w{g_1(\vec a_m)},...,\w{g_n(\vec a_m)})$ 轻易地得到上式的 $\rob$-可证性, 从而公式 $\H$ 表达了 $h$ 的图, 再由 I.119 可以的到 $h$ 在 $\rob$ 中作为函数的可定义性.
	对于 $\m$ 算符, 假设正则 $\l z\xn.g\in\r'$ 被公式 $\G(y,z,\xn)$ 作为函数表示, 对于 $f:=\l \xn.(\m z)g(z,\xn)$,  考虑公式
$$
\F(y,\xn):=\G(0,y,\xn)\and(\fa z)_{<y}\neg\G(0,z,\xn)
$$
对于 $b,\vec a_n\in\N$ , 若 $b=f(\vec a_n)$ , 则 $\rob\vdash\G(0,\w b,\w a_1,...,\w a_n)$ 和对于 $z<b$ 有 $\rob\vdash\neg\G(0,\w z,\w a_1,...,\w a_n)$ , 从而由 I.9.44 可得 $\rob\vdash y<\w b\to\G(0,y,\w a_1,...,\w a_n)$ , 从而 $\rob\vdash\F(\w b,\w a_1,...,\w a_n)$ . 而另一方面, 假设 $b\not=f(\vec a_n)$ , 则一定是 $g(b,\vec a_n)\not=0$ 或者 $b>f(\vec a_n)$ , 这两种情形都可以在 $\rob$ 中证明 $\neg\F(\w b,\w a_1,...,\w a_n)$ , 从而函数 $f$ 的图是可表示的, $f$ 作为函数可定义的.
##### I.126 

设理论 $\th$ 的编码 $\uc\th$ 是 $\re$ 集, 则存在函数 $q\in\p\r$ 使得 $q[\N]=\uc\th$ , 我们考虑构造如下函数
$$
(n,\uc\A)\mapsto \uc{\underbrace{\A\and\A\and...\and\A}_{\text{$n$ 个 $\A$}}}
$$
利用原始递归与编码函数我们可以得到它, 记之为 $\l nx.s$ 并且它是原始递归函数. 显然对于任意的 $\A$ 以及 $n\in\N$ , $s(n,\uc\A)$ 所编码的公式与 $\A$ 是等价的, 并且显然 $\l n.s(n,\uc\A)$ 是递增的, 并且总是有 $s(n,x)>n$ . 于是我们考虑改造一下我们的函数 $q$ 得到 $q'$ 使得
$$
\bl
&q'(0)=q(0),\\
&q'(i+1)=s(q'(i),q(i+1))
\el
$$
借助 Kleene's Recursion Theorem 我们可以轻易地构造出这样的 $q'$ , 并且它是严格增的递归函数, 之后我们考虑它的值域 $q'[\N]$ , 由 I.95 可知它是递归集, 并且由于 $q'(i)$ 所编码的公式总是与 $q(i)$ 等价, 所以它所编码的公式集可以公理化 $\th$ .

##### I.127

不失一般性, 我们可以钦定这个语言就是 $L_{\frak N}$ , 这里我们借助 $\rob$ 设计的巧妙之处了, 由于系统 $\rob$ 只有 $9$ 条公理, 并且它们都是语句, 所以对于任意的公式 $\A$ 而言, 由 Deduction Theorem 可得
$$
\rob\vdash\A\iff\vdash\rob_1\and \rob_2\and...\and \rob_9\to\A
$$
因此我们可以考虑原始递归函数
$$
q:\uc A\mapsto\uc{\rob_1\and \rob_2\and...\and \rob_9\to\A}
$$
若语言上的 pure theory $\frak T$ 是递归的, 那么对于所有 $n\in\N$ 我们有
$$
n\in\Theta_{\rob}\iff q(n)\in\uc{\frak T}
$$
 故 $\Theta_{\rob}$ 也是递归的, 这与 I.9.56(Church) 矛盾了.