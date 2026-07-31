---
title: "一种神奇的DP-树上覆盖DP"
date: 2026-07-31T00:00:00+08:00
tags: []
math: true
draft: false
---

### 遇到做过的题不会做，以后要好好改题 :(
$\color{blue}\textbf{[例题]}$  
`ZRtes AB day1 t3`  
`2022syzx夏季训练4`  
`poj#2152 fire`

`模型 #basic`：
>在树上选择若干个点，每个点能覆盖个离自己距离不大于某个值的所有点，问一系列最优化（计数不行）问题

设
`f[i][j]`表示目前已经做完了i的子树，且钦定i要么不被覆盖，要么被j覆盖的情况下
获得的最大最小值
best[i]表示某一个点的最优值
转移则考虑对于u枚举他被谁覆盖了，然后考虑如何去除多算的i的
费用，那么就有`f[u][i]+=min\max(best[v],f[v][i]-w[i])`，这
样就是相当于把给i的钱强制在树根u被计算，可能转移的时候发现
不连续，但是由于最优答案的性质，所以计算的答案被包含best里头
了因此不用分类讨论


```
//[zr AB day1 t3]
#include <bits/stdc++.h>
#define int long long
using namespace std;
inline int read(){
	int x=0,f=1;char ch=getchar();
	while(!isdigit(ch))f^=ch=='-',ch=getchar();
	while(isdigit(ch))x=x*10+(ch^48),ch=getchar();
	return f?x:-x;
}
const int N=1005,inf=1e18;
int dis[N][N],a[N],f[N][N],best[N],n,t,d,s;
vector<pair<int,int>> G[N];
void dfs1(int u,int fa,int rt){
	for(pair<int,int> v:G[u])if(v.first!=fa){
		dis[rt][v.first]=dis[rt][u]+v.second;
		dfs1(v.first,u,rt);
	}
}
void dfs2(int u,int fa){
	for(pair<int,int> v:G[u])if(v.first!=fa){
		dfs2(v.first,u);
	}
	for(int i=1;i<=n;++i){
		f[u][i]=(dis[u][i]<=d?a[u]:0)-s;
		for(pair<int,int> v:G[u])if(v.first!=fa){
			f[u][i]+=max(best[v.first],f[v.first][i]+s);
		}
	}
	for(int i=1;i<=n;++i){
		best[u]=max(best[u],f[u][i]);
	}
}		
signed main(){
	n=read(),t=read(),d=read(),s=read();
	for(int i=1;i<=n;++i)a[i]=read()*t;
	for(int i=1;i<n;++i){
		int x=read(),y=read(),z=read();
		G[x].push_back({y,z});
		G[y].push_back({x,z});
	}
	for(int i=1;i<=n;++i)dfs1(i,0,i);
	dfs2(1,0);
	printf("%lld\n",best[1]);
	return 0;
}
```

[fix]
关于best的作用：
其实发现定义的状态非常神奇：
每个点要么不被覆盖，要么强制被i覆盖，那么就会出现这种情况：
我钦定了u被很远的一个点控制，但是u的儿子v被很近的一个点控制
然后很远的这个点无法覆盖u，但是很近的这个点能够覆盖u，但是
由于我钦定了u被远点覆盖，因此在这种情况下没有贡献，并不合法
但是如果出现了这种情况，那么一定存在合法的状态比当前这个状态
的值更优，因此best里头就不会有这种非法的状态
