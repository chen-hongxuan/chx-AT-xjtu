---
title: ss讲课day0
date: 2026-07-31T00:00:00+08:00
tags:
  - course
math: true
draft: false
---

## 简单数学基础

### 前言

数学是算法的核心

### 知识清单

* 莫比乌斯反演

* 高斯消元

* 拓展欧几里得

* 矩阵乘法

* 逻辑、命题与证明

### A - 简单莫反(I)

首先进行一个转化，记 $f(u,v,k)$ 为 $x:1 \sim u;y:1\sim v;\gcd(x,y)=k$ 的答案

那么对于询问 $a,b,c,d$ 有答案为 $f(b,d,k)-f(a,d,k)-f(b,c,k)+f(a,c,k)$

这么做是为了将询问从四个自由元变成两个自由元

如何求出 $f(A,B,k)$

实际上我们知道形如 $(kx,ky)$ 的数对的最大公因数一定是 $k$ 的倍数，且最大公因数为 $k$ 的倍数的数对一定可以写为 $(kx,ky)$ 的形式，因此我们证明了：
$$
\{(kx,ky):1\le kx\le A,1\le ky\le B\}= \{(x,y):k|\gcd(x,y),1\le x\le A,1\le y\le B\}
$$
设 $g(A,B,k)$ 为 $x:1 \sim A;y:1\sim B;k|\gcd(x,y)$ 的答案

那么有 
$$
g(A,B,k)=\lfloor\frac A k\rfloor\cdot \lfloor\frac B k\rfloor=\sum_{k|s}f(A,B,s)
$$
应用莫比乌斯反演有
$$
\begin{align}
f(A,B,k)&=\sum_{k|s}g(A,B,s)\cdot \mu(\frac s k)=\sum_{k|s}\lfloor\frac A s\rfloor\lfloor\frac B s\rfloor\cdot \mu(\frac s k)\\
&=\sum_{s=\lambda d}\lfloor\frac A {\lambda k}\rfloor\lfloor\frac B {\lambda k}\rfloor\cdot \mu(\lambda)=\sum_\lambda \lfloor\frac {\lfloor \frac A k\rfloor}\lambda\rfloor\lfloor\frac {\lfloor \frac B k\rfloor}\lambda\rfloor\cdot \mu(\lambda)
\end{align}
$$
应用整除分块即可



### B - 简单高斯消元

可以把所有的可行的询问处理出来（先别问交互器，先在本地处理一下），当作一个线性方程组

然后就是看这 $O(n^2)$ 个方程的秩是否为 $n-1$ ，这是因为方程组有唯一解的充要条件是
$$
r(A)=r([A|b])
$$
但是直接高斯消元的话时间复杂度是 $O(n^4)$ 的，这个时候注意到系数矩阵的元素均为 $0/1$ 因此可以使用 bitset 来优化，则时间复杂度为 $\Theta(\frac {n^4} \omega)$



### C - 简单莫反(II)

先考虑去掉绝对值，那就是把 $a_i$ 从小到大排序，那么答案就是
$$
\begin{align}
&2\sum_{i>j}(a_i-a_j)\cdot {b_ib_j\over\gcd^2(b_i,b_j)}\\
=&(\sum_{i\le n}a_ib_i\sum_{j<i}{b_j\over\gcd^2(b_i,b_j)})-(\sum_{i\le n}a_i\sum_{j<i}{a_jb_j\over \gcd^2(b_i,b_j)})\\
=&(\sum_{i\le n}a_ib_i\sum_{\substack{j<i\\\gcd(b_i,b_j)=t}}{b_j\over t^2})-(\sum_{i\le n}a_i)\sum_{\substack{j<i\\\gcd(b_i,b_j)=t}}{a_jb_j\over t^2}
\end{align}
$$
对于 $j<i$ 的限制我们可以考虑从小往大维护一个累和的东西来完成所有就是
$$
\begin{align}
&(\sum_{i\le n}a_ib_i\sum_{\substack{j<i\\\gcd(b_i,b_j)=t}}{b_j\over t^2})-(\sum_{i\le n}a_i\sum_{\substack{j<i\\\gcd(b_i,b_j)=t}}{a_jb_j\over t^2})\\
=&\sum_{i\le n}a_i(b_i\sum_{t|b_i}{\sum_{\gcd(b_i,b_j)=t}b_j\over t^2}-\sum_{t|b_i}{\sum_{\gcd(b_i,b_j)=t}a_jb_j\over t^2})
\end{align}
$$
（md，latex太难敲了，现场给你们讲吧）

就是仿照 A 题的处理思路来处理 $\gcd(b_i,b_j)=t$ 的限制

所以时间复杂度就是 $O(N\omega(N))$ 可以通过



### D - 神奇不等式

首先注意到不等式:
$$
|x-y|\le x\oplus y\le x+y
$$
然后分类讨论：

对于 $1\le y \le 2x$ 的 $y$ ，

暴力枚举检验

对于 $2x < y\le m$ 的 $y$ ，

$$
x\oplus y>y-x>\frac 1 2 y \Longrightarrow y不可能是 x\oplus y 的倍数
$$

所以有所有的 $y$ 一定是形如：
$$
x\oplus y = \lambda x\Longrightarrow y=\lambda x \oplus x 
$$
然后对于边界处的 $\lambda$ 进行检验即可，时间复杂度为 $O(\sum x+T\log m)$



### E - 不等式证明时间复杂度

首先不难注意到答案不超过 $2\log a$ ，所以考虑爆搜，如果层数爆了就剪枝

那么时间复杂度为 
$$
O(\sum2^{2\log a})=O(\sum a^2)\le O\big((\sum a)^2\big)
$$



### F

这需要注意到一个性质：

性质1：

> 一个集合能合并的充要条件是差分数组的 $\gcd$ 不含有 $2$ 以外的因数

证：

考虑无法操作的时候，所有元素的差分数组是奇数且相等

因为如果存在偶数，那么可以把偶数拆分；

如果存在不同的奇数可以在不同的奇数间操作

然后不难发现一个性质是无论怎么操作差分数组的 $\gcd$ 将 $2$ 的因子全部除去得到的值 $\gcd'$ 是不变的

必要性：假如 $\gcd'\not=1$ 则每个元素一定是 $\gcd'$ 的倍数，不连续

充分性：假如 $\gcd'=1$ 则每个元素最终必定为 $1$ ，否则一定存在不同的奇数

然后通过欧几里得算法可知，改变集合内元素的顺序不影响 $\gcd'$ ，所以只需要原序列的差分数组的 $\gcd'=1$ 即可

实现方法有很多种，包括线段树和st表，这里提供 cdq分治 的做法



### G - 狗屎的构造题

考虑把所有数分成四类：
$$
\begin{align}
&x<{n\over2}:x\rightarrow 1\\
&x={n\over2}:x\rightarrow 2\\
&x={n\over2}+1:x\rightarrow 3\\
&x>{n\over2}+1:x\rightarrow 4
\end{align}
$$
然后题面就转换为了求出 $2,3$ 分别在哪，这个可以考虑每次去掉两个元素：

(a)如果去掉的是 $1,4$ ，那么返回的答案是 $2,3$
(b)如果去掉的是 $2,3$ ，那么返回的答案是 $1,4$
(c)如果去掉的是 $1,2$ ，那么返回的答案是 $3,4$
(d)如果去掉的是 $1,3$ ，那么返回的答案是 $2,4$
(e)如果去掉的是 $2,4$ ，那么返回的答案是 $1,3$
(f)如果去掉的是 $3,4$ ，那么返回的答案是 $1,2$
(g)如果去掉的是 $1,1$ ，那么返回的答案是 $3,4$
(h)如果去掉的是 $4,4$ ，那么返回的答案是 $1,2$

然后相当于使用了 $n\over 2$ 次操作求出了每对相邻元素的类型

假如出现了 (b) ，直接结束

其余的情况考虑分类模拟即可

### H - 线性基入门题

不难发现所有的环都是可以选择走或者不走的，这就启发我们使用线性基来计算

先把图的 $dfs$ 生成树建出来，然后对于每个元素做一遍树上前缀异或，然后查看非树边能不能有机会为这一层的线性基贡献元素，然后一层层从大到小构造线性基，记得构建完每层的线性基要把那一层的值都给消掉，这个过程与高斯消元法是一致的

然后看看怎么处理答案：

把建完线性基的图再跑一遍 $dfs$ 生成树，令 $a_i$ 表示根节点到 $i$ 节点的前缀异或值，这个时候对于任意一个边 $(u,v,w)$ 一定有 $a_u\oplus a_v=w$

对于一个 $x,y$ ，$d(x,y)=(a_x\oplus a_y)\oplus t$ 其中 $t$ 是从线性基里贪心选取出来的

这个时候我们不能直观地看出 $t$ 要选哪些，但是如果我们将线性基的矩阵化为标准型，那么 $a_x\oplus a_y$ 有哪一位是 $0$ ，这一位的线性基就要被选取，之后我们就只需要关心一个区间里有多少个位是 $0$ 即可，这个可以用 $\log$ 个前缀和来维护

### I

建议先把 J 做出来再做这个题

不难发现结构：

```
POP 1 GOTO 2;PUSH 1 GOTO 1
POP 2 GOTO 3;PUSH 2 GOTO 1
POP 3 GOTO 4;PUSH 3 GOTO 1
...
POP [i] GOTO [i+1];PUSH [i] GOTO 1
...
POP [K] GOTO [K+1];PUSH [K] GOTO 1
HALT;PUSH 114514 GOTO 1919810
```

会被运行恰好 $\sum_{i=1}^K 2^i$ 次

然后不难发现将第 $x(K>x)$ 行的 `GOTO 1` 改为 `GOTO 2` 那么将使答案减少 $2^{K-i}$

所以需要求出最大的 $K$ 使得 $2^K\le n$

事实上，这个构造是该题目的最优解，赛时通过此题允许两倍的构造空间

### J - 递归分析

事实上想整出死循环还是很简单的

由于每次是在栈顶添加和访问元素，所以可以考虑对于每一个指令分别求出其存活周期(因为它会把以前的元素覆盖掉)

(1)事实上如果一个指令会去到死循环的指令，那么这个指令是死循环的

(2)一个指令的生命周期内不能再次出现自己

对于每个指令维护：

生命周期、生命周期结束后去到那个位置(或者程序终止)

由于确保了 (2) 性质，每一个指令遍历的元素不会超过 $O(n)$ 因此时间复杂度为 $O(n^2)$

### K - 简单证明题

先二分答案，把所有的点都变成黑白点

然后注意到一个性质：

性质1

> 最后的答案能成为黑点的充要条件是：
>
> 	(1)存在一个黑点的度数大于2
>
>  或者
>
> 	(2)存在至少两个黑点

可以使用归纳法证明

### L

转化一下题意： 就是要求 $ad+bc\over bd$ 约分完后分母仅剩 $2,5$ 因子

考虑进行一些变换：设 $g=\gcd(b,d),b=b'g,d=d'g$ 

则
$$
{ad+bc\over bd}={ad'+b'c\over b'd'g}
$$
可以分析：$b',d'$ 均只含有因数 $2,5$

然后我们对 $g$ 进行分析，令 $g=2^A5^B\cdot y$

所以 $y$ 是确定的，然后必然有 $d=d'\cdot g=d'\cdot 2^A5^B\cdot y$

则有 $d=2^C5^D\cdot y$ ，枚举这样的 $C,D$ 后可以求出 $d$

然后这个时候分子必须把分母里的 $y$ 给约分掉，所以分子必须是 $y$ 的倍数，所以可以列出不定方程，进行拓欧




### M

事实上，与其关心两者的比例不如关心其中一者的占比

然后这个题目就转换为:
$$
\begin{align}
c_i\in\{0,1\},{\sum_{i=0}^na^ib^{n-i}\over(a+b)^n}={x\over x+y}
\end{align}
$$
递归判断即可