---
title: 2024年ICPC区域赛昆明站B题题解
date: 2026-07-31T00:00:00+08:00
tags:
  - tutorial
math: true
draft: false
---

## 前言
成功摄金！世界上没有什么更加美妙的事了
这题在赛时没有做出来，但是感觉实际上是很好处理的，索性就赛后做一下，发现确实不太难
写题解的另外一个原因是代码估计很难写，所以先贷款
另外，很喜欢这种一层一层把思路剥开的题目，

## 思路
#### 考虑一个子段 $A$ 能够有机会成为匹配的条件是什么

`(a)` 假定 $X$ 是一个合法括号串，那么 $aXb(a,b不是同一类型的括号)$ 这种结构不能出现
`(b)` 把 $A$ 中的所有合法的子段尽数消除后，$A$ 中剩余的部分是方向完全相同的括号
附：容易使用贪心的方式来证明 `(b)` 的消除方式与消除顺序不影响最终的消除结果，并且只会有一个消除结果
同时满足上述条件的子段称作可匹配的

因此不难有推论：某一个可匹配的子段如果本身不是合法的括号匹配，那么这个子段只能出现在左边和右边中的一个

#### 再考虑两个子段 $A,B$ 能够匹配的条件

`(a)` 首先 $A,B$ 本身都是可匹配的，并且一左一右
`(b)` 设 $A$ 的消除结果为 $A'$ ，$B$ 的消除结果为 $B'$ ，那么 $A',B'$ 恰好是镜像对称的

md，太jb长了，扔个代码剩下懒得写了
```cpp
#include bitsstdc++.h
#define int long long
#define lc p1
#define rc p11
#define pb push_back
#define pii pairint,int
#define st first
#define nd second
#define mpr make_pair
using namespace std;
inline int read(){
    int x=0,f=1;char ch=getchar();
    for(;!isdigit(ch);ch=getchar())f^=ch=='-';
    for(;isdigit(ch);ch=getchar())x=x10+(ch^48);
    return fx-x;
}
pii operator + (pii x,pii y){return mpr(x.st+y.st,x.nd+y.nd);}
pii operator - (pii x,pii y){return mpr(x.st-y.st,x.nd-y.nd);}
pii operator  (pii x,pii y){return mpr(x.sty.st,x.ndy.nd);}
pii operator % (pii x,pii y){return mpr(x.st%y.st,x.nd%y.nd);}
bool operator != (pii x,pii y){return x.st!=y.stx.nd!=y.nd;}
const int N=5e5+5,inf=1e9;
const pii bas=mpr(2909,3881),mo=mpr(1e9+7,1e9+9);
inline pii qpow(pii x,int t){
    pii ret=mpr(1,1);
    for(;t;t=1,x=xx%mo)if(t&1)ret=retx%mo;
    return ret;
}
inline int fpow(int x,int t,int mo){
    int  ret=1;
    for(;t;t=1,x=xx%mo)if(t&1)ret=retx%mo;
    return ret;
}
int n,m,a[N],l[N],r[N],match[N],rev[N],ans;
char str[N];
mappii,int tms;
vectorint qry[N];
setint ban;
pii pw[N],ipw[N];
inline void red(pii &x){
    if(x.st=mo.st)x.st-=mo.st;
    if(x.nd=mo.nd)x.nd-=mo.nd;
}
void mul(pii &a,pii b){a=ab%mo;}
void add(pii &a,pii b){red(a=a+b);}
struct SegmentTree1{
    pii ADD[N2],MUL[N2];
    void clear(int p,int l,int r){
        ADD[p]=mpr(0,0),MUL[p]=mpr(1,1);
        if(l==r)return;
        int mid=(l+r)1;
        clear(lc,l,mid);
        clear(rc,mid+1,r);
    }
    void pushdown(int p){
        mul(MUL[lc],MUL[p]),mul(ADD[lc],MUL[p]);
        mul(MUL[rc],MUL[p]),mul(ADD[rc],MUL[p]);
        add(ADD[lc],ADD[p]),add(ADD[rc],ADD[p]);
        MUL[p]=mpr(1,1),ADD[p]=mpr(0,0);
    }
    void modify(int p,int l,int r,int L,int R,pii d,int t){
        if(L=l&&r=R){
            if(t)mul(ADD[p],d),mul(MUL[p],d);
            else add(ADD[p],d);
        }else{
            int mid=(l+r)1;
            pushdown(p);
            if(L=mid)modify(lc,l,mid,L,R,d,t);
            if(midR)modify(rc,mid+1,r,L,R,d,t);
        }
    }
    pii query(int p,int l,int r,int x){
        if(l==r)return ADD[p];
        pushdown(p);
        int mid=(l+r)1;
        if(x=mid)return query(lc,l,mid,x);
        else return query(rc,mid+1,r,x);
    }
}Tree;
struct SegmentTree2{
    pii hash[N2];
    int siz[N2];
    void clear(int p,int l,int r){
        hash[p]=mpr(0,0);
        siz[p]=0;
        if(l==r)return;
        int mid=(l+r)1;
        clear(lc,l,mid);
        clear(rc,mid+1,r);
    }
    void pushup(int p){
        siz[p]=siz[lc]+siz[rc];
        red(hash[p]=hash[lc]+pw[siz[lc]]hash[rc]%mo);
    }
    void insert(int p,int l,int r,int x,int t,int v){
        if(l==r){
            if(t)hash[p]=mpr(v,v),siz[p]=1;
            else hash[p]=mpr(0,0),siz[p]=0;
        }else{
            int mid=(l+r)1;
            if(x=mid)insert(lc,l,mid,x,t,v);
            if(midx)insert(rc,mid+1,r,x,t,v);
            pushup(p);
        }
    }
    pii query(){return hash[1];}
}arr;
int sgn(char x){
    return x=='('x=='['x=='{'x=='';
}
int mth(char x,char y){
    if(!sgn(x))return 0;
    if(x=='(')return y==')';
    else if(x=='[')return y==']';
    else if(x=='{')return y=='}';
    else return y=='';
}
int mp(char x){
    if(x=='(')return 2;
    else if(x=='[')return 3;
    else if(x=='{')return 5;
    else return 7;
}
void debug(pii x){printf(%lld,%lldn,x.st,x.nd);}
void work(int turns){
     printf(This is the %lldth TURNSnn,turns);
    for(int i=1;i=n;++i){
        match[i]=rev[i]=0;
        qry[i].clear();
    }
    for(int i=1;i=m;++i)qry[l[i]].pb(r[i]);
    str[n+1]='',match[n+1]=-(n+1);
    for(int i=n;i=1;--i){
        if(sgn(str[i])){
            int pos=i+1;
            while(sgn(str[pos])&&match[pos]0)
                pos=match[pos]+1;
            if(sgn(str[pos]))match[i]=match[pos];
            else match[i]=mth(str[i],str[pos])pos-pos;
            if(match[i]0)rev[match[i]]=i;
        }
    }
    ban.clear();
    for(int i=1;i=n;++i)
        if(!sgn(str[i])&&!rev[i])ban.insert(i);
    arr.clear(1,1,n),Tree.clear(1,1,n);
    for(int i=1;i=n;++i){
        if(sgn(str[i]))
            arr.insert(1,1,n,i,1,mp(str[i]));
        else if(rev[i])
            arr.insert(1,1,n,rev[i],0,0);
        Tree.modify(1,1,n,i,i,arr.query(),0);
    }
    for(int i=1;i=n;++i){
        int f=ban.empty()n+1(ban.begin());
        for(int xqry[i])if(xf){
            if(turns==1){
                pii cnm=Tree.query(1,1,n,x);
                 printf([%lld,%lld]=,i,x);debug(cnm);
                 for(int j=i;j=x;++j)putchar(str[j]);puts();
                ++tms[cnm];
            }
            if(turns==2){
                pii tmp=Tree.query(1,1,n,x);
                 printf([%lld,%lld]=,i,x);debug(tmp);
                 for(int j=i;j=x;++j)putchar(str[j]);puts();
                if(tmp!=mpr(0,0)&&tms[tmp]0){
                    --tms[tmp];
                    ++ans;
                }
            }
        }
        while(ban.size()&&(ban.begin())=i)
            ban.erase(ban.begin());
        if(sgn(str[i])){
            pii d=mo-mpr(mp(str[i]),mp(str[i]));
            if(match[i]0){
                ban.insert(match[i]);
                Tree.modify(1,1,n,i,match[i]-1,d,0);
                Tree.modify(1,1,n,i,match[i]-1,ipw[1],1);
            }else{
                Tree.modify(1,1,n,i,n,d,0);
                Tree.modify(1,1,n,i,n,ipw[1],1);
            }
        }
    }
    if(turns==2)ans+=tms[mpr(0,0)]2;
}
int flip(char x){
    if(x=='(')return ')';
    else if(x==')')return '(';
    else if(x=='[')return ']';
    else if(x==']')return '[';
    else if(x=='{')return '}';
    else if(x=='}')return '{';
    else if(x=='')return '';
    else return '';
}
void solve(){
    n=read(),m=read();
    scanf(%s,str+1);
    for(int i=1;i=m;++i){
        l[i]=read(),r[i]=read();
    }
    ans=0;
    tms.clear();
    work(1);
    for(int i=1;i=n;++i)str[i]=flip(str[i]);
    for(int i=1;i=n;++i)if(i=n-i+1)
        swap(str[i],str[n-i+1]);
    for(int i=1;i=m;++i){
        l[i]=n+1-l[i],r[i]=n+1-r[i];
        swap(l[i],r[i]);
    }
    work(2);
    printf(%lldn,ans);
}
signed main(){
    pw[0]=ipw[0]=mpr(1,1);
    for(int i=1;iN;++i){
        pw[i]=pw[i-1]bas%mo;
        if(i==1){
            ipw[i].st=fpow(pw[i].st,mo.st-2,mo.st);
            ipw[i].nd=fpow(pw[i].nd,mo.nd-2,mo.nd);
        }
    }
    int u=read();
    for(int G=1;G=u;++G){
         if(G==17){
             int n=read(),m=read();
             scanf(%s,str+1);
             for(int i=1;i=m;++i){
                 l[i]=read(),r[i]=read();
             }
             printf(### %lld %lldn,n,m);
             printf(### %sn,str+1);
             for(int i=1;i=m;++i){
                 printf(### %lld %lldn,l[i],r[i]);
             }
             return 0;;
         }
        solve();
    }
}
```
#### 总结
所以问题的一切归约到了这个问题：一个子段消除后的结果是什么？

#### 考虑对于一个子段怎么求出消除结果
考虑暴力，并维护一个栈，栈内按照次序维护还未被匹配的做括号，然后不难发现一个性质：

`(a)` 无论起始位置在哪里，某一个左括号要么永远无法被移出栈，要么被移出栈的那个位置是固定的

所以考虑对于每个位置 $i$ 维护 $match[i]$ 表示子段 $text{str}[i...match[i]]$ 是一个最短的以 $i$ 为开头的合法括号串 