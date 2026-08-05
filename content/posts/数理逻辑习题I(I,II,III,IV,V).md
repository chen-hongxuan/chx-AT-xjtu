---
title: "数理逻辑习题I(I,II,III,IV,V)"
date: 2026-07-31T00:00:00+08:00
tags:
  - mathematical-logic
math: true
draft: false
---

-------------------------------------
$$
\def\lra{\leftrightarrow}
\def\tx#1{\text{#1}}
\def\line#1#2{\  & #1 \quad & \rm{(#2)}\\}
\def\linet#1#2{\  & #1 \quad & \rm{#2}\\}
\def\fa{\forall}
\def\ex{\exists}
\def\A{\mathcal{A}}
\def\B{\mathcal{B}}
\def\C{\mathcal{C}}
\def\D{\mathcal{D}}
\def\E{\mathcal{E}}
\def\G{\mathcal{G}}
\def\H{\mathcal{H}}
\def\I{\mathcal{I}}
\def\J{\mathcal{J}}
\def\K{\mathcal{K}}
\def\Ax{{\bf Ax}}
\def\ax{\Lambda}
\def\bl{\begin{aligned}}
\def\el{\end{aligned}}
\def\T{\mathscr{T}}
\def\t{ {\bf t} }
\def\f{ {\bf f} }
\def\L#1{L(#1)}
\def\eq{\equiv}
\def\inp{\leftarrow}
\def\la#1{\langle #1\rangle}
\def\ov#1{\overline{#1}}
\def\wff{{\bf Wff}}
\def\so{{\scr O}}
\def\vd{\vdash_{L(N)}}
$$
***

## Chapter 1 - Section 1,2,3,4,5

#### I.11

实际上我们只需要证明一个方向即可，即 $\vdash (\fa x)(\fa y)\A\to(\fa y)(\fa x)\A$
$$
\begin{align}
(1)\line{\fa x\fa y\A\to \fa y\A}{Specialization}
(2)\line{\fa y\A\to \A}{Specialization} 
(3)\line{(\fa x\fa y\A\to \fa y\A)\to((\fa y\A\to \A)\to(\fa x\fa y\A\to\A))}{\Ax.1}
(4)\line{(\fa y\A\to \A)\to(\fa x\fa y\A\to\A)}{MP-(1)(3)}
(5)\line{\fa x\fa y\A\to\A}{MP-(2)(4)}
(6)\line{\fa x\fa y\A\to\fa x\A}{\fa-introduction}
(7)\line{\fa x\fa y\A\to\fa y\fa x\A}{\fa-introduction}
\end{align}
$$

#### I.12

$$
\begin{align}
(1)\line{\B\to\ex x\B}{\Ax.2}
(2)\line{(\A\to\B)\to((\B\to\ex x\B)\to(\A\to\ex x\B))}{\Ax.1}
(3)\line{\A\to\B}{given}
(4)\line{\A\to\ex x\B}{MP-(1)(2)(3)}
(5)\line{\ex x\A\to\ex x\B}{\ex-introduction}
\end{align}
$$

#### I.13

$$
\begin{align}
(1)\line{(\A\to\B)\to{(\neg\B\to\neg\A)}}{\Ax.1}
(2)\line{\A\to\B}{given}
(3)\line{\neg\B\to\neg\A}{MP-(1)(2)}
(4)\line{\ex x\neg\B\to\ex x\neg\A}{I.4.23}
(5)\line{(\ex x\neg\B\to\ex x\neg\A)\to(\fa x\A\to\fa x\B)}{\Ax.1}
(6)\line{\fa x\A\to\fa x\B}{MP-(4)(5)}
\end{align}
$$

#### I.14

(1)
$$
\bl
(1)\line{x<y}{given}
(2)\line{u<v}{I.4.12-(1)}
(3)\line{y<x}{I.4.12-(2)}
\el
$$
(2)

假设 $L$ 是包含了二元谓词符号 $<$ 的语言，并且假定$ \vdash_L x<y\to y<x$ ，那么对于任何 $L$ 上的模型 $M=(|M|,\T)$ 均有 $M\vDash_L  x<y\to y<x$，然而模型 $(\N;<_\N)$ 显然不满足它，与假设矛盾，从而 $ \not\vdash_L x<y\to y<x$ .

(3)

显然不，因为公式 $x<y$ 不是一个语句；事实上，这反而强调了演绎定理中的条件的必要性 .

#### I.15

考虑对 $L$ 上的公式 $\C$ 施以归纳

当 $\C$ 是原子公式的时候，假定 $\C\equiv P(t_1...t_k)$ 或者 $\C\equiv t_1=t_2$，那么对于任意的一个将 $\C$ 中的若干子公式 $\A$ 替换为 $\B$ 后得到的公式 $\C'$ 均有 $\C\equiv\C'$ ，从而 $\C\lra\C'$ 是逻辑公理 .

对于逻辑连词的情形，若 $\C\equiv\neg\D$ ，那么对于任意的 $\C'$ 存在 $\D'$ 使得 $\C'\equiv\neg\D'$ ，根据 I.H. 有 $\Gamma\vdash\D\lra\D'$ ，而 $(\D\lra\D')\to (\neg\D\lra\neg\D')$ 是逻辑公理，故应用 MP 即可得到 $\Gamma\vdash\neg\D\lra\neg\D'$ 即 $\C\lra\C'$；若 $\C\eq\D\or\E$ ，则对于任意的 $\C'$ 存在 $\D',\E'$ 使得 $\C'\eq\D'\or\E'$ ，并且根据 I.H. 有 $\Gamma\vdash\D\lra\D',\E\lra\E'$ ，而 $\D\lra\D',\E\lra\E'\vDash_{\bf Taut}(\D\or\E)\lra(\D'\or\E')$ ，故有 $\Gamma\vdash(\D\or\E)\lra(\D'\or\E')$ 即 $\C\lra\C'$ .

当 $\C\eq\ex x\D$ 时，对于任意 $\C'$ 存在 $\D'$ 使得 $\Gamma\vdash\D\lra\D'$ 且 $\C'\eq\ex x\D'$ ，则 $\C\lra\C'\eq\ex x\D\lra\ex x\D'$ ，由 I.4.23 可得 $\D\to\D'\vdash\ex x\D\to\ex x\D'$ 以及 $\D'\to\D\vdash\ex x\D'\to\ex x\D$ 从而有 $\Gamma\vdash\ex x\D\lra\ex x\D'$ 即 $\C\lra\C'$ .

#### I.16

$$
\bl
(1)\line{x=y\to ((z=x)[z\leftarrow x]\lra (z=x)[z\leftarrow y])}{\Ax.4}
\equiv\linet{x=y\to((x=x)\lra(y=x))}{}
(2)\line{x=x}{\Ax.3}
(3)\line{(\A\to(\B\lra\C))\to(\B\to(A\to\C))}{\Ax.1}
(4)\line{x=y\to y=x}{MP-(1)(2)(3)}
\el
$$

#### I.17

首先容易验证 $(x=y\and y=z)\to x=z$ 和 $x=y\to(y=z\to x=z)$ 是同一个东西，所以只需要证明 $ \vdash x=y\to(y=z\to x=z)$ 即可.
$$
\bl
(1)\line{y=x\to ((u=z)[u\leftarrow y]\lra(u=z)[u\leftarrow x])}{\Ax.4}
\eq\linet{y=x\to(y=z\lra x=z)}{}
(2)\line{x=y\to y=x}{I.16}
(3)\line{(\A\lra\B)\to(\A\to\B)}{\Ax.1}
(4)\linet{x=y\to(y=z\to x=z)}{(1)(2)(3)}
\el
$$

#### I.18

对 $L$ 上的公式 $\C$ 施以归纳

当 $\C$ 是原子公式的时候，假定 $\C\eq P(t_1'...t_k')$ 或者 $\C\eq t_1'=t_2'$ ，对于任意一个 $\C'$ ，由于公式的构成是一个树形结构，所以我们总是可以选择若干个在 $\C$ 中没出现过的变元 $z_1...z_m$ 并且把这些变元替换掉 $\C$ 中需要被替换的位置，从而构造出一个公式 $\C^*[z_1...z_m]$ 使得 $\C^*[z_1...z_m\leftarrow t_{i_1}...t_{i_m}]\eq\C$ 且 $\C^*[z_1...z_m\leftarrow s_{i_1}...s_{i_m}]\eq\C'$ ，于是根据公式 $\C^*$ 就可以定义两个长度为 $m+1$ 的公式序列 $\langle\A_i:0\le i\le m\rangle,\langle\B_i:0\le i\le m\rangle$
$$
\A_0:\eq\C^*\ ;\A_{k+1}:\eq\A_k[z_{k+1}\leftarrow t_{i_{k+1}}]\\
\B_0:\eq\C^*\ ;\B_{k+1}:\eq\B_k[z_{k+1}\leftarrow s_{i_{k+1}}]
$$
之后对于 $k\le m$ 施以归纳
> 对于 $k=0$ 显然有 $\A_0\eq\B_0$ 从而有 $\vdash\A_0\lra\B_0$ .
> 
> 对于 $k<m$ ，由 I.H. 得到 $\Gamma\vdash\A_k\lra\B_k$ ，再由 I.4.12 得到 $\Gamma\vdash(\A_k\lra\B_k)[z_{k+1}\leftarrow t_{i_{k+1}}]$ 即 $\A_{k+1}\lra\B_k[z_{k+1}\leftarrow t_{i_{k+1}}]$ ，而由 $\Ax.4$ 可得 $\vdash s_{i_{k+1}}=t_{i_{k+1}}\to(\B_k[z_{k+1}\leftarrow s_{i_{k+1}}]\lra\B_k[z_{k+1}\leftarrow t_{i_{k+1}}])$ 即 $s_{i_{k+1}}=t_{i_{k+1}}\to(\B_{k+1}\lra\B_k[z_{k+1}\leftarrow t_{i_{k+1}}])$ ，而又由于 $\Gamma\vdash s_{i_{k+1}}=t_{i_{k+1}}$ ，从而应用 MP 即可得到 $\Gamma\vdash \A_{k+1}\lra\B_k[z_{k+1}\leftarrow t_{i_{k+1}}],\B_{k+1}\lra\B_k[z_{k+1}\leftarrow t_{i_{k+1}}]$ 故 $\Gamma\vdash\A_{k+1}\lra\B_{k+1}$ .

从而得到 $\Gamma\vdash \A_m\lra\B_m$ 即 $\C\lra\C'$ .

逻辑连词和量词的情形与 I.15 是类似的，也是平凡的，故略去.

#### I.19

这一情况可以看作是 I.18 的一个实例，对于一个 $L$ 上的项 $t$ 及经过若干次替换的 $t'$ ，令公式 $\A:\eq t=t$ 与公式 $\A':\eq t=t'$ 那么由 I.18 可得 $\Gamma\vdash\A\lra\A'$ ，而 $\A$ 可以由 $\Ax.3$ 与 I.4.12 轻易导出，从而 $\Gamma\vdash\A'$ .

#### I.20

不完全必要，主要是演绎定理的问题，如果我们的证明过程中使用的 $\ex$-introduction 所引入的量词均不影响到 $\A$ 中的某个变元 $x$ ，或者说变元 $x$ 被冻结了，那么实际上演绎定理的归纳法仍然正确，所以仍然可以应用演绎定理，从而仍然可以得到反证法的正确性.
 ##### I.21

令 $L':=L\cup\{a\}$ ，则根据 I.4.20 ，条件(2)是在说 $\Gamma\vdash_{L'}\A[a]\to\B$ ，取不在 $\A,\B$ 中出现的变元 $z$ ，则根据 I.4.15 有 $\Gamma\vdash_L \A[z]\to\B$ ，再由 $\ex$-introduction 规则得到 $\Gamma\vdash_L\ex z\A[z]\to\B$ ，由于对 $z$ 的约定以及 I.4.13 可得 $\vdash\ex x\A[x]\lra\ex z\A[z]$ ，从而应用两次 MP 可以得到 $\Gamma\vdash_L\B$ .

#### I.22

首先看 $ \vdash\A\to\fa x\A$ ，首先 $\vDash_{\bf Taut}\A\to\A$ ，再应用 $\fa$-introduction （ $x$ 不在 $\A$ 中自由出现）即可得到 $ \vdash\A\to\fa x\A$ ；对于 $ \vdash\ex x\A\to\A$ 也是同理，应用 $\ex$-introduction 即可.

#### I.23

首先来证明 $\vdash\fa x(\A\and\B)\lra(\fa x\A\and\fa x\B)$  
$(\to)$ 首先由 Specialization 可得 $\vdash\fa x(\A\and\B)\to(\A\and\B)$ ，进一步有 $\A\and\B\vDash_{\bf Taut}\A,\B$ ，之后经由 $\Ax.1$ 以及几次 MP 可以得到 $\vdash\fa x(\A\and\B)\to\A,\fa x(\A\and\B)\to\B$ ，再由 $\fa$-introduction 得到 $\vdash\fa x(\A\and\B)\to\fa x\A,\fa x(\A\and\B)\to\fa x\B$ ，而又有 $\C\to\D,\C\to\E\vDash_{\bf Taut}\C\to(\D\and\E)$ ，从而有 $\vdash\fa x(\A\and\B)\to(\fa x\A\and\fa x\B)$ .

$(\leftarrow)$ 首先由 $\vdash(\fa x\A\and\fa x\B)\to\fa x\A,\fa x\A\to\A$ 可以得到 $\vdash(\fa x\A\and\fa x\B)\to\A$ 类似的还有 $\vdash(\fa x\A\and\fa x\B)\to\B$ ，从而有 $\vdash(\fa x\A\and\fa x\B)\to(\A\and\B)$ ，之后由 $\fa$-introduction 可得 $\vdash(\fa x\A\and\fa x\B)\to\fa x(\A\and\B)$ .

接下来我们来证明 $\vdash\ex x(\A\or\B)\lra(\ex x\A\or\ex x\B)$ ，事实上可以把存在量词的情形看作全称量词的情形的一个实例，首先注意到 $\vdash\ex x(\A\or\B)\lra \neg\fa x(\neg\A\and\neg\B),(\ex x\A\or\ex x\B)\lra \neg(\fa x\neg\A\and\fa x \neg\B)$ ，于是令 $\A':\eq\neg\A,\B':\eq\neg\B$ ，之后通过 I.4.25 即可得到存在量词的情形的证明.

#### I.24

$(\fa$-monotonicity$)$ 首先由 $\Ax.2$ 可得 $\vdash\A\to\ex x\A$ ，之后由 $\fa$-monotonicity 可得 $\vdash\fa y\A\to\fa y\ex x\A$ ，之后再由 $\ex$-introduction 得到 $\vdash \ex x\fa y\A\to\fa y\ex x\A$ .

$($auxiliary constant$)$首先我们扩充语言，向 $L$ 中添加一个常数 $c$ 得到语言 $L'$ ，之后我们先证明 $\vdash_{L'}\fa y\A[x\inp c]\to \fa y\ex x\A$ ，这可以通过 $\Ax.2$ 以及应用一次 $\fa$-monotonicity 得到，取适当变元 $z$ 可得到 $\vdash_L\fa y\A[x\inp z]\to\fa y\ex x\A$ ，这里假设了 $x\not\eq y$ ，于是由 I.4.12 将 $z$ 替换为 $x$ 即可得到 $\vdash_L\fa y\A\to\fa y\ex x\A$ ，之后再进行一次 $\ex$-introduction 即可得到我们想要的结论了.  

> ps: srds 这种方法好像也使用了 monotonicity ，感觉本质上还是方法一，辅助常元的作用似乎不大. 

#### I.25

这个题我们用 I.4.26 . 首先由 $\Ax.1$ 有 $\vdash\fa x\A\or\neg\fa x\A$ ，之后只需要分别证明 $\vdash \fa x\A\to \ex x(\A\to\fa x \A),\neg\fa x\A\to\ex x(\A\to\fa x\A)$ .

$(\vdash\fa x\A\to\ex x(\A\to\fa x\A))$ 首先由 $\Ax.1$ 有 $\vdash\fa x\A\to(\A\to\fa x\A)$ ，之后由 $\Ax.2$ 有 $\vdash(\A\to\fa x\A)\to\ex x(\A\to\fa x\A)$ ，从而应用两次 MP 可以得到 $\vdash\fa x\A\to\ex x(\A\to\fa x\A)$ .

$(\vdash\neg\fa x\A\to\ex x(\A\to\fa x\A))$ 首先我们有 $\vdash \neg\fa x\A\lra\ex x\neg\A,\ex x(\A\to\fa x\A)\lra\ex x(\neg\A\or\fa x\A)$ ，由$\ex$-distributive law可得 $\vdash\ex x(\neg\A\or\fa x\A)\lra (\ex x\neg\A\or\ex x\fa x\A)$ ，再由 I.4.25 ，我们只需证明 $\vdash\ex x\neg\A\to(\ex x\neg\A\or\ex x\fa x\A)$ ，而事实上这是 $\Ax.1$ .

#### I.26

显然，这是因为这四个公式都是重言式，所以 $\ax_2\subseteq\ax_1$ .

#### I.27 ~ I.42 是关于 $\ax_2$ 的推理能力的，先略过

#### I.43

即验证，对于任意 $L$ 上的模型 $M:=(|M|,\T)$ ，如果 $M\vDash\A$ 那么 $M\vDash\fa x\A$ . 首先 $\fa x\A$ 本质上是 $\neg\ex x\neg\A$ ，并且我们钦定 $\A$ 中自由出现的变元的列表为 $(x_1...x_k)$ ，即 $\A\eq\A(x_1...x_k)$ ，根据假设 $M\vDash\A(x_1...x_k)$ 就是在 $L(M)$ 中，对于任意的 $\la{i_1...i_k}\in|M|^k$ 均有 $\A(\ov{i_1}...\ov{i_k})^\T=\t$ ，从而 $(\neg\A(\ov {i_1} ...\ov {i_k}))^\T=\f$ ，因此无论 $x$ 是否自由出现在 $\A$ 中都有 $(\ex x\neg\A(\ov {i_1}...\ov {i_k}))^\T=\f$ 从而 $(\fa x\A(\ov{i_1}...\ov{i_k}))^\T=\t$ 即 $M\vDash\fa xA$ .

#### I.44

即验证，如果 $\A$ 是语句，那么 $\Gamma+\A\vDash\B$ 蕴涵 $\Gamma\vDash\A\to\B$ . 假定前提成立，对于 $L$ 上的模型 $M:=(|M|,\T)$ 满足 $M\vDash \Gamma$ ，我们来验证 $M\vDash\A\to\B$ ，由于 $\A$ 是语句，所以可以分 $\A^\T=\t,\f$ 两种情况来讨论. 如果 $\A^\T=\t$ 则 $M\vDash\Gamma+\A$ 从而 $M\vDash\B$ 故容易验证 $M\vDash\A\to\B$ ；如果 $\A^\T=\f$ ，那么显然有 $M\vDash\A\to\B$ . 从而 $\Gamma\vDash\A\to\B$ .

#### I.45 , I.46

Trivial.

#### I.47

#### I.48