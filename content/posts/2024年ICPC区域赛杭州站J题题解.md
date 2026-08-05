---
title: 2024年ICPC区域赛杭州站J题题解
date: 2026-07-31T00:00:00+08:00
tags:
  - tutorial
math: true
draft: false
---

## 前言
赛时没有做出来，然后赛后被队友嘲讽说是简单题，还搞了一堆奇奇怪怪的容斥加减......

> 我认为都是假的，毕竟计数的难点并不在于设计怎样的状态，而在于怎么不算重，我在赛时已经想过很多容斥了，要么会算重，要么就是无法通过的。经过了两天的思考，直到自己真正把这题弄出来后，我方才发现这是一个很巧妙的题，从朴素的暴力到正解这一过程绝对不是平凡的，而是很复杂的

谨以此文记录这一不轻易想到的巧妙的思路

## 赛时的思路
注意到题目要求的是**可重集对**数，因此我需要知道左右两边的可重集合里有多少种元素后还需要用一个组合数来求解

最朴素的暴力，枚举左边的集合出现了哪些数字 $\mathbb S$ ，然后想办法处理一下左边点对于右边选数字会产生那些影响与限制，就是两种：

* `(a)`右边集合的某些数字必选，记这些数字的集合为 $\mathbb T$

* `(b)`有若干个形如 "$a[i],b[i]$ 中至少选一个的" 的限制

我们将题目中的 $a[i],b[i]$ 限制放在图上，那就相当于给点连边，而我们枚举左边集合出现的数字实际上是在枚举图上的点集，那么看看这两种限制是怎么产生的:

如果在原来的图中某条边连接的两个点其中一个出现在左边的集合中，而另外一个没有出现，那么另外一个就必须出现在右边的集合中，这是 `(a)限制`

如果在原来的图中某条边连接的两个点都出现在了左边的集合里，那么这条边就转化成了 `(b)限制`，

如果在原来的图中某条边连接的两个点都没有出现在左边的集合里，那么这样的左边的集合是不合法的

然后可以注意到，其实 `(b)限制` 拍在图上是 **原图对于点集 $\mathbb S$ 的导出子图**，而选择右边集合就是在这个导出子图进行染色，使得导出子图的每一条边所连接的两个点中至少有一个点被染色了

因此可以把右边点集 $\mathbb G$ 拆成两部分: $\mathbb{G=T \cup S'}$，其中 $\mathbb S'$ 表示 $\mathbb S$ 的导出子图中符合 `(b)限制` 的染了色的点集

不过在此之前还需要把原图里没有任何边的点提前抽出来，扔到集合 $\mathbb X$ ，这些点可以加也可以不加，其余的至少有一个边连的点扔到集合 $\mathbb Q$ 里头

然后考虑怎么计算这个过程：

我们记 $F(a,\mathbb B,\mathbb C)$ 表示大小为 $a$ 的可重集，其中 $\mathbb B$ 中元素必须全部出现，然后还有 $\mathbb C$ 中的元素可以出现也可以不出现

首先枚举 $\mathbb S$ 并检查 $\mathbb S$ 是否合法，接着很容易导出 $\mathbb T$ ，然后再枚举 $\mathbb {S' \subseteq S}$

然后检查 $\mathbb S'$ 是否符合 `(b)限制` ，如果均能通过上述检验，那么 $ans+=F(n1,\mathbb S,\mathbb X)\cdot F(n2,\mathbb {S' \cup T},\mathbb X)$

## 优化
> 这个优化不是平凡的

* 具体的，你关注到其实想要计算 $F(a,\mathbb B,\mathbb C)$ 你不需要 $\mathbb B,\mathbb C$ 而是需要 $|\mathbb B|,|\mathbb C|$

* 另外一点，就是 $\mathbb S'$ 符合 `(b)限制` 的一个等价命题是: 点集 $\mathbb{U=S - S'}$ 的导出子图是一个独立集

然后实际上有 $\mathbb{Q - U = T\cup S'} \Longrightarrow \mathbb{|T\cup S|=|Q|-|U|}$

因此就有 $ans+=F(n1,|\mathbb S|,|\mathbb X|)\cdot F(n2,|\mathbb Q|-|\mathbb U|,|\mathbb X|)$，这里只要求：

* $\mathbb U$ 是独立集（这只与 $\mathbb U$ 有关，与 $\mathbb S$ 无关，我们成功分离了 `(b)限制` 里的捆绑的关系）

* $\mathbb {S' \subseteq S} \Longleftrightarrow \mathbb {U \subseteq S}$

所以可以先把所有独立集 $\mathbb U$ 求出来，并给数组 $f[\mathbb U]$ 赋值为 $F(n2,|\mathbb Q|-|\mathbb U|,|\mathbb X|)$ ，对 $f[]$ 做一遍高维前缀和，然后枚举所有合法的 $\mathbb S$ 使得 $ans+=F(n1,|\mathbb S|,|\mathbb X|)\cdot f[\mathbb S]$

代码:
```cpp
#include <bits/stdc++.h>
#define int long long
#define pb push_back
using namespace std;
inline int read(){
    int x=0,f=1;char ch=getchar();
    for(;!isdigit(ch);ch=getchar())f^=ch=='-';
    for(;isdigit(ch);ch=getchar())x=x*10+(ch^48);
    return f?x:-x;
}
const int N=2e6+5,mo=1e9+7;
inline void red(int &x){x>=mo?x-=mo:0;}
inline int qpow(int x,int t){
    int ret=1;
    for(;t;t>>=1,x=x*x%mo)if(t&1)ret=ret*x%mo;
    return ret;
}
int fac[N],ifac[N];
inline int C(int x,int y){
    if(y>x||y<0||x<0)return 0;
    int ret=1;
    for(int i=x;i>x-y;--i)ret=ret*i%mo;
    return ret*ifac[y]%mo;
}
int F(int u,int a,int b){return C(u+b-1,a+b-1);}
int n1,n2,m,k,lnk[23],f[N],vis[23],ans;
vector<int> avi[2];
void solve(){
    n1=read(),n2=read(),m=read(),k=read(),ans=0;
    for(int i=0;i<m;++i)lnk[i]=vis[i]=0;
    for(int i=0;i<(1<<m);++i)f[i]=0;
    for(int i=0;i<k;++i){
        int x=read()-1,y=read()-1;
        vis[x]=vis[y]=1;
        lnk[x]|=1<<y;
        lnk[y]|=1<<x;
    }
    int tt=0,Z=0,sz=0;//tt is the size of X , Z is Q
    for(int i=0;i<m;++i){
        tt+=!vis[i];
        Z|=vis[i]<<i;
        sz+=vis[i];
    }
    avi[0].clear();
    avi[0].pb(0);
    for(int i=0;i<m;++i)if(vis[i]){
        avi[1].clear();
        for(int x:avi[0]){
            avi[1].pb(x);
            if(!((x|(1<<i))&lnk[i]))avi[1].pb(x|(1<<i));
        }
        avi[0]=avi[1];
    }
    for(int x:avi[0])
        f[x]=F(n2,sz-__builtin_popcountll(x),tt);
    for(int j=0;j<m;++j)for(int i=0;i<(1<<m);++i)
        if(i&(1<<j))red(f[i]+=f[i^(1<<j)]);
    for(int i=0;i<(1<<m);++i)if((i&Z)==i){
        int tag=1;
        for(int j=0;j<m;++j)if(vis[j]){
            if(!(i&(1<<j))){
                if((lnk[j]&i)!=lnk[j])tag=0;
            }
        }
        if(tag)red(ans+=F(n1,__builtin_popcountll(i),tt)*f[i]%mo);
    }
    printf("%lld\n",ans);
}
signed main(){
    fac[0]=1;
    for(int i=1;i<N;++i)fac[i]=fac[i-1]*i%mo;
    ifac[N-1]=qpow(fac[N-1],mo-2);
    for(int i=N-1;i;--i)ifac[i-1]=ifac[i]*i%mo;
    for(int cas=read();cas--;)solve();
}
```