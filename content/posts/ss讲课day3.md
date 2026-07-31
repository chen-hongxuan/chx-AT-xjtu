---
title: "ss讲课day3"
date: 2026-07-31T00:00:00+08:00
tags: []
math: true
draft: false
---

### A

#### 矩阵死了！

这个题是个科技题，但其实也有贪心的哈希做法，只是过于复杂了

联想一下什么东西像括号一样，没有交换律的？是矩阵！

考虑钦定四种左括号分别对应四种不同的可逆矩阵，然后两个串可合并的必要条件是乘积为单位阵

注意到这是必要条件而非充要条件，但是众所周知哈希也是必要条件

如果担心撞的话，可以考虑多两组

所以只需维护矩阵的前缀积和矩阵前缀积的逆即可，注意矩阵运算无交换律

然后再对矩阵维护哈希表就行了
```
#include <bits/stdc++.h>
#define int long long
#define lc p<<1
#define rc p<<1|1
#define pb push_back
#define pii pair<int,int>
#define st first
#define nd second
#define mpr make_pair
using namespace std;
inline int read(){
    int x=0,f=1;char ch=getchar();
    for(;!isdigit(ch);ch=getchar())f^=ch=='-';
    for(;isdigit(ch);ch=getchar())x=x*10+(ch^48);
    return f?x:-x;
}
pii operator + (pii x,pii y){return mpr(x.st+y.st,x.nd+y.nd);}
pii operator - (pii x,pii y){return mpr(x.st-y.st,x.nd-y.nd);}
pii operator * (pii x,pii y){return mpr(x.st*y.st,x.nd*y.nd);}
pii operator % (pii x,pii y){return mpr(x.st%y.st,x.nd%y.nd);}
bool operator != (pii x,pii y){return x.st!=y.st||x.nd!=y.nd;}
const int N=5e5+5,inf=1e9;
const pii bas=mpr(2909,3881),mo=mpr(1e9+7,1e9+9);
inline pii qpow(pii x,int t){
    pii ret=mpr(1,1);
    for(;t;t>>=1,x=x*x%mo)if(t&1)ret=ret*x%mo;
    return ret;
}
inline int fpow(int x,int t,int mo){
    int  ret=1;
    for(;t;t>>=1,x=x*x%mo)if(t&1)ret=ret*x%mo;
    return ret;
}
int n,m,a[N],l[N],r[N],match[N],rev[N],ans;
char str[N];
map<pii,int> tms;
vector<int> qry[N];
set<int> ban;
pii pw[N],ipw[N];
inline void red(pii &x){
    if(x.st>=mo.st)x.st-=mo.st;
    if(x.nd>=mo.nd)x.nd-=mo.nd;
}
void mul(pii &a,pii b){a=a*b%mo;}
void add(pii &a,pii b){red(a=a+b);}
struct SegmentTree1{
    pii ADD[N<<2],MUL[N<<2];
    void clear(int p,int l,int r){
        ADD[p]=mpr(0,0),MUL[p]=mpr(1,1);
        if(l==r)return;
        int mid=(l+r)>>1;
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
        if(L<=l&&r<=R){
            if(t)mul(ADD[p],d),mul(MUL[p],d);
            else add(ADD[p],d);
        }else{
            int mid=(l+r)>>1;
            pushdown(p);
            if(L<=mid)modify(lc,l,mid,L,R,d,t);
            if(mid<R)modify(rc,mid+1,r,L,R,d,t);
        }
    }
    pii query(int p,int l,int r,int x){
        if(l==r)return ADD[p];
        pushdown(p);
        int mid=(l+r)>>1;
        if(x<=mid)return query(lc,l,mid,x);
        else return query(rc,mid+1,r,x);
    }
}Tree;
struct SegmentTree2{
    pii hash[N<<2];
    int siz[N<<2];
    void clear(int p,int l,int r){
        hash[p]=mpr(0,0);
        siz[p]=0;
        if(l==r)return;
        int mid=(l+r)>>1;
        clear(lc,l,mid);
        clear(rc,mid+1,r);
    }
    void pushup(int p){
        siz[p]=siz[lc]+siz[rc];
        red(hash[p]=hash[lc]+pw[siz[lc]]*hash[rc]%mo);
    }
    void insert(int p,int l,int r,int x,int t,int v){
        if(l==r){
            if(t)hash[p]=mpr(v,v),siz[p]=1;
            else hash[p]=mpr(0,0),siz[p]=0;
        }else{
            int mid=(l+r)>>1;
            if(x<=mid)insert(lc,l,mid,x,t,v);
            if(mid<x)insert(rc,mid+1,r,x,t,v);
            pushup(p);
        }
    }
    pii query(){return hash[1];}
}arr;
int sgn(char x){
    return x=='('||x=='['||x=='{'||x=='<';
}
int mth(char x,char y){
    if(!sgn(x))return 0;
    if(x=='(')return y==')';
    else if(x=='[')return y==']';
    else if(x=='{')return y=='}';
    else return y=='>';
}
int mp(char x){
    if(x=='(')return 2;
    else if(x=='[')return 3;
    else if(x=='{')return 5;
    else return 7;
}
void debug(pii x){printf("<%lld,%lld>\n",x.st,x.nd);}
void work(int turns){
    // printf("This is the %lldth TURNS\n\n",turns);
    for(int i=1;i<=n;++i){
        match[i]=rev[i]=0;
        qry[i].clear();
    }
    for(int i=1;i<=m;++i)qry[l[i]].pb(r[i]);
    str[n+1]='*',match[n+1]=-(n+1);
    for(int i=n;i>=1;--i){
        if(sgn(str[i])){
            int pos=i+1;
            while(sgn(str[pos])&&match[pos]>0)
                pos=match[pos]+1;
            if(sgn(str[pos]))match[i]=match[pos];
            else match[i]=mth(str[i],str[pos])?pos:-pos;
            if(match[i]>0)rev[match[i]]=i;
        }
    }
    ban.clear();
    for(int i=1;i<=n;++i)
        if(!sgn(str[i])&&!rev[i])ban.insert(i);
    arr.clear(1,1,n),Tree.clear(1,1,n);
    for(int i=1;i<=n;++i){
        if(sgn(str[i]))
            arr.insert(1,1,n,i,1,mp(str[i]));
        else if(rev[i])
            arr.insert(1,1,n,rev[i],0,0);
        Tree.modify(1,1,n,i,i,arr.query(),0);
    }
    for(int i=1;i<=n;++i){
        int f=ban.empty()?n+1:(*ban.begin());
        for(int x:qry[i])if(x<f){
            if(turns==1){
                pii cnm=Tree.query(1,1,n,x);
                // printf("[%lld,%lld]=",i,x);debug(cnm);
                // for(int j=i;j<=x;++j)putchar(str[j]);puts("");
                ++tms[cnm];
            }
            if(turns==2){
                pii tmp=Tree.query(1,1,n,x);
                // printf("[%lld,%lld]=",i,x);debug(tmp);
                // for(int j=i;j<=x;++j)putchar(str[j]);puts("");
                if(tmp!=mpr(0,0)&&tms[tmp]>0){
                    --tms[tmp];
                    ++ans;
                }
            }
        }
        while(ban.size()&&(*ban.begin())<=i)
            ban.erase(ban.begin());
        if(sgn(str[i])){
            pii d=mo-mpr(mp(str[i]),mp(str[i]));
            if(match[i]>0){
                ban.insert(match[i]);
                Tree.modify(1,1,n,i,match[i]-1,d,0);
                Tree.modify(1,1,n,i,match[i]-1,ipw[1],1);
            }else{
                Tree.modify(1,1,n,i,n,d,0);
                Tree.modify(1,1,n,i,n,ipw[1],1);
            }
        }
    }
    if(turns==2)ans+=tms[mpr(0,0)]/2;
}
int flip(char x){
    if(x=='(')return ')';
    else if(x==')')return '(';
    else if(x=='[')return ']';
    else if(x==']')return '[';
    else if(x=='{')return '}';
    else if(x=='}')return '{';
    else if(x=='<')return '>';
    else return '<';
}
void solve(){
    n=read(),m=read();
    scanf("%s",str+1);
    for(int i=1;i<=m;++i){
        l[i]=read(),r[i]=read();
    }
    ans=0;
    tms.clear();
    work(1);
    for(int i=1;i<=n;++i)str[i]=flip(str[i]);
    for(int i=1;i<=n;++i)if(i<=n-i+1)
        swap(str[i],str[n-i+1]);
    for(int i=1;i<=m;++i){
        l[i]=n+1-l[i],r[i]=n+1-r[i];
        swap(l[i],r[i]);
    }
    work(2);
    printf("%lld\n",ans);
}
signed main(){
    pw[0]=ipw[0]=mpr(1,1);
    for(int i=1;i<N;++i){
        pw[i]=pw[i-1]*bas%mo;
        if(i==1){
            ipw[i].st=fpow(pw[i].st,mo.st-2,mo.st);
            ipw[i].nd=fpow(pw[i].nd,mo.nd-2,mo.nd);
        }
    }
    int u=read();
    for(int G=1;G<=u;++G){
        // if(G==17){
        //     int n=read(),m=read();
        //     scanf("%s",str+1);
        //     for(int i=1;i<=m;++i){
        //         l[i]=read(),r[i]=read();
        //     }
        //     printf("### %lld %lld\n",n,m);
        //     printf("### %s\n",str+1);
        //     for(int i=1;i<=m;++i){
        //         printf("### %lld %lld\n",l[i],r[i]);
        //     }
        //     return 0;;
        // }
        solve();
    }
}
```
### B

实际上就是要求把一个区间里的数从小到大排序后满足：

$$
\begin{align}
&a_i+a_{m-i+1}=a_1+a_m\\
\iff& a_i = (a_1+a_m)-a_{m-i+1}
\end{align}
$$
也就是说，如果我们同时维护序列 $\{b_n\}:b_i=-a_i$

那么对于同一个区间将 $\{a\},\{b\}$ 均排序后应有：
$$
a_i-b_i=(a_1+a_m)
$$
关键在于怎么动态的维护一个序列，同时支持询问某个区间排序后的结果呢

考虑对于 $\{a\},\{b\}$ 分别维护生成函数：
$$
F_{[l,r]}(x)=\sum_{i\in[l,r]}x^{a_i},G_{[l,r]}(x)=\sum_{i\in[l,r]}x^{b_i}
$$
那么对于区间 $[l,r]$ 只要满足：
$$
F_{[l,r]}(x)\equiv G_{[l,r]}(x)\cdot x^{a_1+a_m}
$$
那么这个区间就是好的

事实上，直接维护多项式是不现实的，但是多项式恒等的一个必要条件是两个多项式上的若干的特征值相等，所以我们随意令 $x$ 为一个值，然后维护多项式的和即可，原理类似于哈希（担心撞哈希的可以考虑维护多哈希）

顺便普及一下生日悖论

### C

首先考虑错排的结构：

如果 $n$ 是偶数，那么最近的错排是 $2i-1$ 和 $2i$ 进行交换，这是唯一的

如果 $n$ 是奇数，那么最近的错排是具有如下性质的排列：

>存在一个整数 $r$ 使得 $2r+1,2r+2,2r+3$ 三个数的位置是轮换的，剩下的元素是与相邻元素交换的

所以这样的排列有 $n-1$ 个

并且，每一个这样的排列（错排）都可以被如下的二元组表示：
$$
(r,0/1)
$$
然后为求出字典序的第 $k$ 个，考虑从前往后贪心的操作，

事实上，不难分析出每个位置 $i$ 上至多有 $5$ 种可能的值，分别对应 
$$
2r+3<i,\\
2r+3=i,\\
2r+2=i,\\
2r+1=i,\\
2r+1>i
$$
使用线段树维护即可

### D - 势能分析入门

考虑维护 $n+1$ 棵动态开点线段树，编号从 $0$ 到 $n$，$0$ 代表没有人用的位置，其余的分别代表每个人所占有的线段

然后不难发现题目的三种操作至多会增加 $O(n)$ 个连续段，

第一种操作就是线段树分裂，每次至多产生 $\log n$ 个节点，因此整个程序的总的节点数是 $O(n\log n)$

第二种操作是线段树合并，每次操作对时间复杂度的贡献是该次操作删除的节点的个数，显然总和不会超过总结点个数，所以这个部分的时间复杂度也是 $O(n\log n)$ 

现在还没有解决询问的问题

考虑对于所有连续段维护一个 set 或者什么别的，记录这个连续段的节点的编号，然后每次就二分找到那个弹幕所在的节点，显然这个节点是某个线段树的叶子，然后就一直往上跳跳到根节点即可判断这个根节点是在谁手上

上述的功能也可以用 fhqtreap 来完成，但是我不会 fhqtreap

### E

裸的线段树合并模板
```
#include <bits/stdc++.h>
#define int long long
#define pii pair<int,int>
#define mpr make_pair
#define pb push_back
using namespace std;
inline int read(){
    int x=0,f=1;char ch=getchar();
    for(;!isdigit(ch);ch=getchar())f^=ch=='-';
    for(;isdigit(ch);ch=getchar())x=x*10+(ch^48);
    return f?x:-x;
}
inline void chmax(int &x,int y){x=max(x,y);}
const int N=2e5+5,LOG=20,S=1e7+5;
struct SegmentTree{
    int lc[S],rc[S],f[S],g[S],pool;
    void pushdown(int p){
        if(!g[p])return;
        if(lc[p]){
            f[lc[p]]+=g[p];
            g[lc[p]]+=g[p];
        }
        if(rc[p]){
            f[rc[p]]+=g[p];
            g[rc[p]]+=g[p];
        }
        g[p]=0;
    }
    void pushup(int p){
        if(lc[p])chmax(f[p],f[lc[p]]);
        if(rc[p])chmax(f[p],f[rc[p]]);
    }
    void insert(int &p,int l,int r,int x){
        if(!p)p=++pool;
        if(l==r)return;
        int mid=(l+r)>>1;
        if(x<=mid)insert(lc[p],l,mid,x);
        else insert(rc[p],mid+1,r,x);
    }
    void modify(int p,int l,int r,int L,int R,int d){
        if(!p)return;
        if(L<=l&&r<=R){
            f[p]+=d;
            g[p]+=d;
            return;
        }
        pushdown(p);
        int mid=(l+r)>>1;
        if(L<=mid)modify(lc[p],l,mid,L,R,d);
        if(mid<R)modify(rc[p],mid+1,r,L,R,d);
        pushup(p);
    }
    int ask(int p){return f[p];}
    int query(int p,int l,int r,int L,int R){
        if(!p)return 0;
        if(L<=l&&r<=R)return f[p];
        pushdown(p);
        int mid=(l+r)>>1,ret=0;
        if(L<=mid)chmax(ret,query(lc[p],l,mid,L,R));
        if(mid<R)chmax(ret,query(rc[p],mid+1,r,L,R));
        return ret;
    }
    void merge(int &p,int q,int l,int r){
        if(!p||!q)p|=q;
        else{
            if(l==r){
                chmax(f[p],f[q]);
                return;
            }
            int mid=(l+r)>>1;
            pushdown(p);
            pushdown(q);
            merge(lc[p],lc[q],l,mid);
            merge(rc[p],rc[q],mid+1,r);
            pushup(p);
        }
    }
}Tree;
vector<pii> edge[N],oper[N];
vector<int> v[N],l[N];
int dist[N],nxt[N][LOG],n,m,root[N],k[N],s[N];
void dfs1(int u,int fa){
    nxt[u][0]=fa;
    for(int i=1;i<LOG;++i)
        nxt[u][i]=nxt[nxt[u][i-1]][i-1];
    for(auto [v,w]:edge[u])if(v!=fa){
        dist[v]=dist[u]+w;
        dfs1(v,u);
    }
}
int FIND(int x,int len){
    int y=x;
    for(int i=LOG-1;i>=0;--i){
        if(dist[x]-dist[nxt[y][i]]<len)
            y=nxt[y][i];
    }
    return y;
}
void dfs2(int u,int fa){
    int tot=0;
    for(auto [v,w]:edge[u])if(v!=fa){
        dfs2(v,u);
        tot+=Tree.ask(root[v]);
    }
    Tree.modify(root[u],1,m,1,m,tot);
    for(auto [v,w]:edge[u])if(v!=fa){
        int x=tot-Tree.ask(root[v]);
        Tree.modify(root[v],1,m,1,m,x);
        Tree.merge(root[u],root[v],1,m);
    }
    for(auto [id,val]:oper[u])
        Tree.modify(root[u],1,m,id,id,val);
}
signed main(){
    n=read(),m=read();
    for(int i=1;i<n;++i){
        int x=read(),y=read(),w=read();
        edge[x].pb(mpr(y,w));
        edge[y].pb(mpr(x,w));
    }
    dfs1(1,0);
    for(int i=1;i<=m;++i){
        k[i]=read(),s[i]=read(); 
        v[i].resize(k[i]+1,0);
        l[i].resize(k[i]+1,0);
        for(int j=1;j<=k[i];++j)v[i][j]=read();
        for(int j=1;j<=k[i];++j){
            l[i][j]=read()+l[i][j-1];
            oper[FIND(s[i],l[i][j])].pb(mpr(i,v[i][j]));
        }
        Tree.insert(root[s[i]],1,m,i);
    }
    dfs2(1,0);
    printf("%lld\n",Tree.ask(root[1]));
}
```
### F

神奇分块

首先需要发现一个性质：

性质1

> 对于序列 $\{b_n\}:b_i=\gcd(i,b_i)$ 的修改次数是不多的
>
> 具体的，是对每个数的质因子个数求和，为 $O(n \log\log n)$

考虑对于序列分块，每个节点维护它跳出当前块的第一个位置是多少以及收获的权值

每次修改 $b_i$ 时就对 $i$ 信息暴力重构即可，时间复杂度为 $O(B)$

取块长 $B=400$ 可以达到最佳效果

### G

考虑当一个球变成蓝色时会影响哪些侦测器：

所以维护蓝色球的连续段即可，使用线段树合并可以完成

### H

不难注意到后缀 $\gcd$ 至多 $\log$ 个取值，所以直接用个 set 维护一下就行了
```cpp
#include <bits/stdc++.h>
#define int long long
#define lc p<<1
#define rc p<<1|1
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
int gcd(int x,int y){return y?gcd(y,x%y):x;}
const int N=2e5+5;
set<pair<int,pii>> pos,tmp;
int a[N],b[N],gcda[N],gcdb[N],sufA[N],sufB[N],n;
void opf(pii &a,pii b){
    if(a.st==b.st)a.nd+=b.nd;
    else a=max(a,b);
}
void solve(){
    n=read();
    for(int i=1;i<=n;++i){
        a[i]=read();
        gcda[i]=gcd(gcda[i-1],a[i]);
    }
    for(int i=1;i<=n;++i){
        b[i]=read();
        gcdb[i]=gcd(gcdb[i-1],b[i]);
    }
    sufA[n+1]=sufB[n+1]=0;
    for(int i=n;i;--i){
        sufA[i]=gcd(sufA[i+1],a[i]);
        sufB[i]=gcd(sufB[i+1],b[i]);
    }
    pii ans={0,0};
    pos.clear();
    // pos.insert({0,{0,0}});
    for(int i=1;i<=n;++i){
        tmp.clear();
        for(auto [u,v]:pos){
            int x=v.st,y=v.nd;
            tmp.insert({u,{gcd(x,a[i]),gcd(y,b[i])}});
        }
        tmp.insert({i,{gcd(a[i],gcdb[i-1]),gcd(b[i],gcda[i-1])}});
        pos.clear();
        for(set<pair<int,pii>>::iterator it1=tmp.begin(),it2;it1!=tmp.end();it1=it2){
            it2=it1;
            it2++;
            while(it2!=tmp.end()&&(*it1).nd==(*it2).nd)it2++;
            it2--;
            pos.insert(*it1);
            it2++;
        }
        for(set<pair<int,pii>>::iterator it=pos.begin();it!=pos.end();){
            int x=(*it).nd.st,y=(*it).nd.nd,A,B;
            A=gcd(x,sufB[i+1])+gcd(y,sufA[i+1]);
            B=-(*it).st;
            ++it;
            if(it==pos.end())B+=i+1;
            else B+=(*it).st;
            opf(ans,{A,B});
        }
    }
    printf("%lld %lld\n",ans.st,ans.nd);
    return;
}
signed main(){
    // freopen("D.out","w",stdout);
    for(int cas=read();cas--;)
        solve();
    return 0;
}
```

### I

注意到整体加上一个数不影响相对大小，所以考虑通过相对大小的方式来讨论：

实际上一个序列是可整除的充要条件是笛卡尔树上的每个父亲都是儿子的因子

第二个要关注的是这样的 $x$ 是不多的，因为：
$$
\begin{align}
{a+x\over b+x}=k\iff1+{a-b\over b+x}=k
\end{align}
$$
事实上，在 $1\sim 1e9$ 之间最大的因子个数为 $1000$

所以暴力枚举后在笛卡尔树上检验，可以通过本题

### J

贪心+位运算即可