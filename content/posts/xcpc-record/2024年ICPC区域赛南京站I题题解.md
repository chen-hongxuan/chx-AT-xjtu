---
title: 2024年ICPC区域赛南京站I题题解
date: 2026-07-31T00:00:00+08:00
tags:
  - tutorial
math: true
draft: false
---

### 看！一道计数题！我们有救了！
设 $f[x=i]$ 表示值恰好为 $i$ 的方案数，那么答案就是求 
$$
ans=\sum_{i\ge 0} f[x=i]\cdot i
$$
考虑进行阿贝尔变换，得到：
$$
\begin{aligned}
ans&=\sum_{i\ge 0} (f[x\ge i]-f[x\ge i+1])\cdot i 
\\&=f[x\ge 0]\cdot 0 + \sum_{i\ge 1}f[x\ge i] 
\\&=\sum_{i\ge 1}f[x\ge i]
\end{aligned}
$$
然后考虑 $f[x\ge i]$ 有什么组合意义：
先把序列里头所有小于 $i$ 的数全部染成黑色，假设有 $cnt$ 个黑色，然后把这些黑色块填入到方阵中，使得不存在某一行某一列全为黑色的
统计有多少种填法，记为 $F$ ，则 $f[x\ge i]=F\cdot cnt!\cdot (nm-cnt)!$

于是这就须要求 $G[i]$ 表示用恰好 $i$ 个黑色块，无法使得某一行某一列全为黑色的填法
那么就是有 $n+m$ 个限制，形如
* `(a)` $A_i$ 表示第 $i$ 行存在至少一个白色，其中 $1\le i \le n$
* `(b)` $A_i$ 表示第 $i-n$ 列存在至少一个白色，其中 $n+1\le i \le n+m$

那么有 
$$
G[i] = |\cap_{i=1}^{n+m}A_i|
$$
这种限制很不好弄，但是每个限制的补集却十分的简洁：某一行或某一列全为黑色
那么考虑容斥，就是枚举强制违反那些限制，忽略其他限制，而不难发现这个东西可以使用一个组合数来计算，并且你只关心违反了几个行限制，几个列限制，具体是谁并不关心，因此这是一个二项式反演，然后推式子
$$
\begin{aligned}
\eta\in \mathbb N,G[\eta]&=\sum_{x=0}^n\sum_{y=0}^m (-1)^x\binom n x\cdot (-1)^y\binom m y \cdot \binom {(n-x)(m-y)} \eta\\
&=(-1)^{n+m}\sum_{x=0}^n\sum_{y=0}^m (-1)^x\binom n x\cdot (-1)^y\binom m y \cdot \binom {xy} \eta\\
&=\sum_{r=0}^{nm}\binom r \eta \sum_{\substack{xy=r\\ 0\le x\le n\\0\le y \le m}} (-1)^{n+m-x-y}\binom n x\binom m y
\end{aligned}
$$
显然后面那一坨仅与 $r$ 相关，且是可以提前预处理的，记为 $v'[r]$
则
$$
\begin{aligned}
G[\eta]&=\sum_{r=0}^{nm}\binom r \eta \cdot v'[r]\\
&=\frac 1{\eta!}\sum_{r=\eta}^{nm}(\frac 1 {(r-\eta)!})\cdot(r!\cdot v'[r])
\end{aligned}
$$
显然这是一个卷积的形式，因此使用多项式乘法即可
把 $G[i]$ 处理出来后计算总和只需要对 $a_i$ 排个序即可，时间复杂度是 $\mathcal O(nm \log nm)$ 的
代码(3kb的多项式能一遍过，我是神人)
```cpp
#include <bits/stdc++.h>
#define mpr make_pair
#define int long long
#define pb push_back
#define pii pair<int,int>
#define st first
#define nd second
using namespace std;
inline int read(){
    int x=0,f=1;char ch=getchar();
    for(;!isdigit(ch);ch=getchar())f^=ch=='-';
    for(;isdigit(ch);ch=getchar())x=x*10+(ch^48);
    return f?x:-x;
}
mt19937 rnd(time(0));
const int mo=998244353;
inline int qpow(int x,int t){
    int ret=1;
    for(;t;t>>=1,x=x*x%mo)if(t&1)ret=ret*x%mo;
    return ret;
}
inline void red(int &x){x>=mo?x-=mo:0;}
inline void chmin(int &x,int y){x=min(x,y);}
inline void chmax(int &x,int y){x=max(x,y);}
namespace poly{
    const int N=2e6+5,G=3,iG=332748118;
    int cir[N],w[N],r[N],sav[N];
    void fft(int *f,int len,int t){
        for(int i=0;i<len;++i){
            cir[i]=(cir[i>>1]>>1)|((i&1)?len>>1:0);
            if(i>cir[i])swap(f[i],f[cir[i]]);
        }
        for(int l=2;l<=len;l<<=1){
            int w=qpow(t?G:iG,(mo-1)/l);
            for(int i=0;i<len;i+=l){
                int fw=1,u,v;
                for(int j=i;j<i+l/2;++j,fw=fw*w%mo){
                    u=f[j],v=f[j+l/2];
                    red(f[j]=u+fw*v%mo);
                    red(f[j+l/2]=u+mo-fw*v%mo);
                }
            }
        }
        int r=qpow(len,mo-2);
        for(int i=0;(!t)&&i<len;++i)f[i]=f[i]*r%mo;
    }
    void polymul(int *f,int *g,int len){
        for(int i=0;i<len;++i)f[i]=f[i]*g[i]%mo;
    }
    void mul(int *f,int *g,int len){
        fft(f,len,1),fft(g,len,1);
        polymul(f,g,len);
        fft(f,len,0);
    }
}
const int N=4e6+5;
int n,m,fac[N],ifac[N],a[N],f[N],g[N],len,v[N];
inline int binom(int x,int y){
    if(y>x||y<0||x<0)return 0;
    return fac[x]*ifac[y]%mo*ifac[x-y]%mo;
}
int sgn(int x){return x&1?-1:1;}
void solve(){
    n=read(),m=read();
    for(int i=0;i<=n*m*3;++i)f[i]=g[i]=v[i]=0;
    for(int i=1;i<=n*m;++i)a[i]=read();
    for(int x=0;x<=n;++x)for(int y=0;y<=m;++y)
        red(v[x*y]+=sgn(x+y)*binom(n,x)%mo*binom(m,y)%mo);
    for(int i=0;i<=n*m;++i){
        v[i]=v[i]*sgn(n+m)%mo*fac[i]%mo;
        g[n*m-i]=ifac[i];
    }
    len=1;
    while(len<=n*m*2)len<<=1;
    poly::mul(g,v,len);
    for(int i=0;i<=n*m;++i)
        f[n*m-i]=g[n*m+i]*fac[n*m-i]%mo;
    sort(a+1,a+n*m+1);
    int ans=0;
    for(int i=1,j;i<=n*m;i=j){
        j=i+1;
        while(j<=n*m&&a[i]==a[j])++j;
        red(ans+=f[i-1]*(a[i]-a[i-1])%mo);
    }
    printf("%lld\n",ans);
    return;
}
signed main(){
    fac[0]=1;
    for(int i=1;i<N;++i)fac[i]=fac[i-1]*i%mo;
    ifac[N-1]=qpow(fac[N-1],mo-2);
    for(int i=N-1;i;--i)ifac[i-1]=ifac[i]*i%mo;
    for(int cas=read();cas--;)solve();
    return 0;
}

```