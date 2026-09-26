---
title: 2026年ICPC网络赛第二场A题题解
date: 2026-09-26T00:00:00+08:00
tags:
  - tutorial
math: true
draft: false
---

## 前言

[题目链接](https://qoj.ac/problem/20236) / [VJudge 链接](https://vjudge.net/contest/850279#problem/A)

这题我自己想出了一个和官方题解不太一样的做法. 下面还是按照当时推思路的顺序, 从一个看起来很难实现的迭代过程开始讲.

## 先考虑一个朴素的过程

一个非空集合对异或封闭, 当且仅当它是 $\mathbb F_2^m$ 的一个线性子空间. 因此对于每个 $i$, 先维护一个线性基 $\mathbb B_i$, 初始化时令

$$
\operatorname{span}(\mathbb B_i)=\operatorname{span}(S_i).
$$

先令 $I=\{0\}$. 如果当前已经考虑到的空间是 $\operatorname{span}(\mathbb B_i)$, 那么其中不属于原集合 $S_i$ 的数都是需要补上的. 于是一个很自然的做法是, 每一轮求出

$$
I_{\mathrm{new}}:=\operatorname{span}\left(\bigcup_{i=1}^n\bigl(\operatorname{span}(\mathbb B_i)\setminus S_i\bigr)\right),
$$

然后对每个 $i$ 更新 $\mathbb B_i$, 使得新的线性基张成 $\operatorname{span}(\mathbb B_i\cup I_{\mathrm{new}})$, 再令 $I\leftarrow I_{\mathrm{new}}$. 重复这个过程, 直到 $I$ 不再变化. 一开始, 每个 $\mathbb B_i$ 只张成 $S_i$; 往后我们逐轮把必须补的元素纳入考虑, 再看这些新元素又会迫使哪些元素出现.

这里先说明为什么每一轮求到的数确实是必须的. 设 $T$ 是任意一个合法的操作集合, 那么 $S_i\cup T$ 都是线性空间.

>[!lemma] 每轮加入的空间都是必要的
>若当前的 $I$ 已经包含在每个 $S_i\cup T$ 中, 且 $\operatorname{span}(\mathbb B_i)=\operatorname{span}(S_i\cup I)$, 那么任意 $x\in\operatorname{span}(\mathbb B_i)\setminus S_i$ 都必须属于 $T$.

>[!proof]
>$S_i\cup T$ 包含 $S_i\cup I$, 又是线性空间, 所以包含 $\operatorname{span}(\mathbb B_i)$. 因此它包含 $x$. 但 $x\notin S_i$, 只能是一次操作把它加入了所有集合, 即 $x\in T$.

初始的 $I=\{0\}$ 就满足引理的前提, 因为每个最终集合都是非空线性空间, 必定包含 $0$. 注意这并不是说我们一开始就要操作 $0$; 这里只是拿它作为零维线性空间的起点. 往后的每轮更新, 都是在上一轮的 $I$ 上继续扩张.

直接求集合 $I$ 显然不现实. 不过我们只关心它的张成, 因此只需要维护 $I$ 的线性基 $\mathbb I$. 并且随着轮数增加, $\operatorname{span}(\mathbb I)$ 只会变大: 上一轮已经缺失的那些数仍然在更新后的 $\operatorname{span}(\mathbb B_i)$ 中, 而原集合 $S_i$ 没有改变. 所以每一轮可以复用上一轮的 $\mathbb I$.

还能再放宽一步: 如果这一轮能让 $\mathbb I$ 扩张, 我们先只扩张一维. 那些没来得及加入的方向不会凭空消失, 后面仍然会被发现. 这样至多发生 $m$ 次真正的扩张. 现在问题就变成了: **怎样判断是否还存在一个能扩张 $\mathbb I$ 的数?**

## Part A: 找到可以扩张的数

先看一个普通的线性基 $\mathbb L$. 把 $x$ 按照 $\mathbb L$ 的主元从高到低消元, 得到的余量记作 $q_{\mathbb L}(x)$. 如果余量是 $0$, 那么 $x$ 已经在线性基张成的空间中; 否则, 它的最高非零位一定还没有主元, 可以拿它来扩张 $\mathbb L$. 这就给出了一个映射

$$
q_{\mathbb L}:x\longmapsto\text{$x$ 对 $\mathbb L$ 消元后的余量}.
$$

回到原问题, 当前线性基是 $\mathbb I$. 对每个 $i$, 我们要判断

$$
q_{\mathbb I}\!\left[\operatorname{span}(\mathbb B_i)\setminus S_i\right]
$$

里面有没有非零元素. 直接维护这个差集还是很麻烦, 不妨先退一步, 看看如何维护整个 $q_{\mathbb I}[\operatorname{span}(\mathbb B_i)]$.

>[!theorem] 消元映射的线性性
>对于任意 $x,y$, 都有 $q_{\mathbb L}(x\oplus y)=q_{\mathbb L}(x)\oplus q_{\mathbb L}(y)$.

>[!proof]
>从高位到低位看每一次消元. 若当前主元位是 $j$, 这一轮的操作可以写成 $x\mapsto x\oplus x_j\mathbb L[j]$, 它是 $\mathbb F_2$ 上的线性映射. 整个消元过程是这些映射的复合, 因此也是线性的.

于是 $q_{\mathbb I}[\operatorname{span}(\mathbb B_i)]$ 仍然是一个线性空间, 而且

$$
q_{\mathbb I}[\operatorname{span}(\mathbb B_i)]
=\operatorname{span}\bigl(q_{\mathbb I}[\mathbb B_i]\bigr).
$$

对 $\mathbb B_i$ 中的向量逐个求余量, 再求一次线性基即可. 记得到的线性基为 $\mathbb C_i$. 现在只剩下一件事: 在 $\operatorname{span}(\mathbb C_i)$ 中找一个非零的 $u$, 使得它确实来自某个 $\operatorname{span}(\mathbb B_i)\setminus S_i$ 中的数.

对于每个 $x\in S_i$, 我们维护它的余量 $q_{\mathbb I}(x)$. 记 $\operatorname{occur}_i(u)$ 为这些余量中 $u$ 出现的次数. 由于 $q_{\mathbb I}$ 是线性映射, 同一个像的所有原像构成一个核的陪集, 因而每个像拥有一样多的原像. 以下 $|\mathbb B_i|$ 和 $|\mathbb C_i|$ 都指非零基向量的个数.

>[!lemma] 缺失原像的判别
>设 $u\in\operatorname{span}(\mathbb C_i)$ 且 $u\ne0$. 存在 $x\in\operatorname{span}(\mathbb B_i)\setminus S_i$ 满足 $q_{\mathbb I}(x)=u$, 当且仅当
>$$
>\operatorname{occur}_i(u)<2^{|\mathbb B_i|-|\mathbb C_i|}=2^{\dim I}.
>$$

>[!proof]
>这里的核应当是限制在 $\operatorname{span}(\mathbb B_i)$ 上的核. 由于每一轮都把 $I$ 加入了 $\mathbb B_i$, 这个核恰好是 $I$, 因而大小为 $2^{\dim I}$. 也可以由线性映射的核与像的维数关系得到 $|\mathbb B_i|-|\mathbb C_i|=\dim I$. 如果 $S_i$ 里落在这一类的元素少于原像总数, 那么剩余的原像就是要找的 $x$; 反过来也是一样的.

于是我们可以开桶统计 $\operatorname{occur}_i(u)$, 然后尝试 $\operatorname{span}(\mathbb C_i)$ 中的候选值. 这里其实不用枚举整个空间: 若非零元素超过 $|S_i|$ 个, 随便检查 $|S_i|+1$ 个**不同的非零**元素, 其中必有一个连一次都没有出现在 $S_i$ 的余量中; 若非零元素不足这么多, 就把它们全部检查完. 一定要排除 $u=0$, 因为它即使对应缺失原像, 也不能扩张 $\mathbb I$. 用格雷码枚举这些坐标, 从上一个候选值转移到下一个时只需异或一个基向量, 所以这一部分的时间是 $O(|S_i|)$.

如果所有 $i$ 都找不到这样的 $u$, 迭代就可以结束了. 下面再看找到 $u$ 后, 如何避免把刚才维护的信息从头计算一遍.

## Part B: 扩张以后维护什么

到这里, 我们关心的东西有四类:

1. 全局空间 $I$ 的线性基 $\mathbb I$;
2. 每个 $\operatorname{span}(S_i\cup I)$ 的线性基 $\mathbb B_i$;
3. 每个像空间的线性基 $\mathbb C_i$;
4. 对于每个 $x\in S_i$, 它当前的余量 $q_{\mathbb I}(x)$.

假定找到了能扩张 $I$ 的 $u$, 其最高非零位为 $h$. 对于前两项, 把 $u$ 插入对应的线性基即可. 真正需要考虑的是后两项: $\mathbb I$ 变了, 以前算出的像也跟着变了.

>[!theorem] 扩张后的余量
>令 $I'=\operatorname{span}(I\cup\{u\})$, $\mathbb I'$ 为它的线性基. 对任意 $x$, 有
>$$
>q_{\mathbb I'}(x)=
>\begin{cases}
>q_{\mathbb I}(x),&[q_{\mathbb I}(x)]_h=0,\\
>q_{\mathbb I}(x)\oplus u,&[q_{\mathbb I}(x)]_h=1.
>\end{cases}
>$$

>[!proof]
>令 $r=q_{\mathbb I}(x)$. 因为 $x\oplus r\in I$, 所以在扩张后的线性基下, $x$ 与 $r$ 的余量相同. 而 $r$ 和 $u$ 在旧基的所有主元位上都是 $0$, 新增的主元位只有 $h$. 因此对 $r$ 消元时只需要看第 $h$ 位是否为 $1$, 若是就异或 $u$, 否则保持原样.

先看第 4 项. 现在每个 $q_{\mathbb I}(x)$ 都已经保存在数组里了, 根据上面的式子检查第 $h$ 位, 必要时异或 $u$, 一遍扫描就能把它们更新为 $q_{\mathbb I'}(x)$.

再看第 3 项. 向 $\mathbb B_i$ 中加入 $u$ 不会给像空间增加新向量, 因为 $q_{\mathbb I'}(u)=0$. 所以只需把原来 $\mathbb C_i$ 的各个基向量按照定理更新:

- 主元位置 $b>h$ 时, 若第 $h$ 位为 $1$ 就异或 $u$; 最高位仍是 $b$, 直接保留.
- 主元位置 $b<h$ 时, 第 $h$ 位本来就是 $0$, 不用修改.
- 主元位置 $b=h$ 时, 将原向量异或 $u$ 后清掉这一位, 把余下的向量重新插入 $\mathbb C_i$.

这样对于每个 $i$ 只需 $O(m)$ 就能更新 $\mathbb C_i$. 实际写代码时还可以把第 2 项省掉: $\mathbb B_i$ 是用来解释像空间从哪里来的, 判断和转移只需要 $\mathbb C_i$、原集合元素的余量与全局基 $\mathbb I$.

## Part C: 复杂度与输出

每次只扩张一维, 所以至多有 $m$ 轮真正的扩张. 每一轮找 $u$ 时, 扫描所有原集合元素的余量, 用桶统计出现次数, 再用格雷码枚举候选, 时间为 $O(\sum_i|S_i|)$. 更新 $\mathbb I$ 是 $O(m)$; 概念上更新所有 $\mathbb B_i$ 是 $O(nm)$, 实现里更新所有 $\mathbb C_i$ 也是 $O(nm)$; 最后更新所有余量又是 $O(\sum_i|S_i|)$. 因而求出最终线性基的时间复杂度为

$$
O\left(m^2n+m\sum_i|S_i|\right).
$$

不过题目最终要我们输出的是具体做了哪些操作, 而不是一个线性基. 令 $H=\bigcap_i S_i$, 考虑输出 $I\setminus H$.

>[!theorem] 最终答案
>当再也找不到能扩张 $\mathbb I$ 的非零余量时, $I\setminus H$ 是最少的操作集合.

>[!proof]
>此时对于每个 $i$, $\operatorname{span}(\mathbb B_i)\setminus S_i$ 中的元素都在 $I$ 里, 因为它们的余量只能是 $0$. 因此 $\operatorname{span}(\mathbb B_i)=S_i\cup I$, 所有 $S_i\cup I$ 都已经对异或封闭. 对于 $I\cap H$ 中的数, 每个原集合本来就有; 对于 $I\setminus H$ 中的数, 输出的操作会把它加入所有集合. 所以输出以后得到的正是 $S_i\cup I$, 方案合法.
>
>另一方面, 前面每一轮的缺失元素都是任意合法答案必须加入的, 所以任意合法答案的每个最终集合都包含 $I$. 对于 $x\in I\setminus H$, 至少有一个原集合没有 $x$, 于是任何合法答案都必须操作 $x$. 因此这些操作一个也省不了.

最后枚举 $I$ 中所有元素, 用原集合中每个数出现于多少个 $S_i$ 的次数判断它是否属于 $H$. 若某个原集合缺少 $0$, 它也会在这里被输出. 这一步还需 $O(2^m)$ 时间. 算上真正输出答案的开销, 总时间复杂度是 $O(m^2n+m\sum_i|S_i|+2^m)$, 空间复杂度是 $O(nm+\sum_i|S_i|+2^m)$. 代码为了方便把格雷码预处理到了题目的上界 $2^{20}$.

## 代码

```cpp
#include <bits/stdc++.h>
#define VI vector<int>
using namespace std;

inline int read(){
    int x=0,f=1,ch=getchar();
    for(;ch<'0'||ch>'9';ch=getchar())f^=ch=='-';
    for(;ch>='0'&&ch<='9';ch=getchar())x=x*10+(ch^48);
    return f?x:-x;
}

namespace gray_code{
    void work(int n,VI &ret){
        ret.resize(1<<n);
        for(int i=0;i<(int)ret.size();++i)ret[i]=i^(i>>1);
    }
}

struct Linear_Basis{
    int m;
    VI B;

    int &operator[](size_t i){return B[i];}

    Linear_Basis(int n=0):m(n-1),B(VI(n,0)){}

    int proj(int x){
        for(int i=m;~i;--i){
            if(B[i]&&((x>>i)&1))x^=B[i];
        }
        return x;
    }

    void insert(int x){
        if(!(x=proj(x)))return;
        for(int i=m;~i;--i)if((x>>i)&1){
            B[i]=x;
            for(int j=m;j>i;--j){
                if((B[j]>>i)&1)B[j]^=x;
            }
            break;
        }
    }

    int dim(){
        int ret=0;
        for(int i=m;~i;--i)ret+=B[i]!=0;
        return ret;
    }

    void resort(VI &ret){
        ret={};
        for(int i=m;~i;--i){
            if(B[i])ret.push_back(B[i]);
        }
    }

    void restrict(int x,int h){
        for(int i=m;i>h;--i){
            if(B[i]&&((B[i]>>h)&1))B[i]^=x;
        }
        if(B[h]){
            int tmp=B[h]^x;
            B[h]=0;
            insert(tmp);
        }
    }
};

int n,m;
VI occur,gray,lg;
vector<VI> s;
vector<Linear_Basis> C;

void solve(){
    s.assign(n=read(),{}),m=read();

    Linear_Basis I(m);
    C.assign(n,Linear_Basis(m));
    occur.assign(1<<m,0);

    for(int i=0;i<n;++i){
        int c=read();
        s[i].resize(c);
        for(int &x:s[i]){
            x=read();
            ++occur[x];
            C[i].insert(x);
        }
    }

    VI cnt(1<<m,0);

    while(1){
        int FIND=0;
        int k=1<<I.dim();

        for(int i=0;i<n;++i){
            for(int x:s[i])++cnt[x];

            // 先检查已经出现过的非零投影值
            for(int x:s[i])if(x){
                if(cnt[x]<k){
                    FIND=x;
                    break;
                }
            }

            // 再枚举至多 |S_i|+1 个非零的像空间元素
            if(!FIND){
                int lim=min(1<<C[i].dim(),(int)s[i].size()+2);
                VI tmp;
                C[i].resort(tmp);

                for(int j=1,val=0;j<lim;++j){
                    int bit=lg[gray[j]^gray[j-1]];
                    val^=tmp[bit];
                    if(cnt[val]<k){
                        FIND=val;
                        break;
                    }
                }
            }

            for(int x:s[i])cnt[x]=0;
            if(FIND)break;
        }

        if(!FIND)break;

        I.insert(FIND);

        int highbit=0;
        for(int i=m-1;~i;--i){
            if((FIND>>i)&1){
                highbit=i;
                break;
            }
        }

        for(int i=0;i<n;++i){
            C[i].restrict(FIND,highbit);
            for(int &x:s[i]){
                if((x>>highbit)&1)x^=FIND;
            }
        }
    }

    VI tmp,ans={};
    I.resort(tmp);

    int ss=1<<(int)tmp.size();
    int val=0;

    for(int i=0;i<ss;++i){
        if(i){
            int bit=lg[gray[i]^gray[i-1]];
            val^=tmp[bit];
        }
        if(occur[val]!=n)ans.push_back(val);
    }

    printf("%d\n",(int)ans.size());
    for(int x:ans)printf("%d ",x);
    puts("");
}

signed main(){
    gray_code::work(20,gray);

    lg.assign(1<<20,-1);
    for(int i=1;i<(int)lg.size();++i){
        lg[i]=lg[i>>1]+1;
    }

    solve();
}
```
