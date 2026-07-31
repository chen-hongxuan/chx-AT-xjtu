---
title: "【模板】FHQtreap"
date: 2026-07-31T00:00:00+08:00
tags: []
math: true
draft: false
---

```cpp
mt19937 rnd(time(0));
struct FHQtreap{
	int lc[N],rc[N],val[N],key[N],siz[N],pool,root;
	int create(int x){
		int p=++pool;
		val[p]=x;
		siz[p]=1;
		key[p]=rnd();
		lc[p]=rc[p]=0;
		return p;
	}
	void update(int p){
		if(!p)return;
		siz[p]=siz[lc[p]]+siz[rc[p]]+1;
	}
	void split(int p,int d,int &x,int &y){
		if(!p){
			x=y=0;
			return;
		}
		if(val[p]<=d){
			x=p;
			split(rc[p],d,rc[p],y);
		}
		else{
			y=p;
			split(lc[p],d,x,lc[p]);
		}
		update(p);
	}
	int merge(int x,int y){//val[x]<val[y]
		if(x==0||y==0)return x^y;
		if(key[x]>key[y]){
			rc[x]=merge(rc[x],y);
			update(x);
			return x;
		}
		else{
			lc[y]=merge(x,lc[y]);
			update(y);
			return y;
		}
	}
	void insert(int d){
		int x,y;
		split(root,d-1,x,y);
		root=merge(merge(x,create(d)),y);
	}
	void remove(int d){
		int x,y,z;
		split(root,d,x,z);
		split(x,d-1,x,y);
		if(y){
			y=merge(lc[y],rc[y]);
		}
		root=merge(merge(x,y),z);
	}
	int rank(int d){
		int x,y,ret;
		split(root,d-1,x,y);
		ret=siz[x]+1;
		root=merge(x,y);
		return ret;
	}
	int kth(int k){
		int p=root;
		while(siz[lc[p]]+1!=k){
			if(siz[lc[p]]>=k)p=lc[p];
			else{
				k-=siz[lc[p]]+1;
				p=rc[p];
			}
		}
		return val[p];
	}
	int pre(int d){
		int x,y,p;
		split(root,d-1,x,y);
		p=x;
		while(rc[p])p=rc[p];
		root=merge(x,y);
		return val[p];
	}
	int nxt(int d){
		int x,y,p;
		split(root,d,x,y);
		p=y;
		while(lc[p])p=lc[p];
		root=merge(x,y);
		return val[p];
	}
}T;

```