---
title: 【模板】广义fwt
date: 2026-07-31T00:00:00+08:00
tags:
  - oist
math: true
draft: false
---

```cpp
struct matrix{
	int a[2][2],n,m;
	matrix(){}
	matrix(int x,int y){
		n=x,m=y;
		memset(a,0,sizeof(a));
	}
	matrix operator  (matrix &x){
		matrix y=matrix(n,x.m);
		for(int k=0;km;++k){
			for(int i=0;in;++i)for(int j=0;jx.m;++j)
				red(y.a[i][j]+=a[i][k]x.a[k][j]%mo);
		}
		return y;
	}
}tr,Itr;
void fwt(int f,int len,matrix &t){
	matrix w;
	for(int n=2;n=len;n=1){
		int dn=n1;
		w=matrix(1,2);
		for(int i=0;ilen;i+=n){
			for(int j=0;jdn;++j){
				w.a[0][0]=f[i+j];
				w.a[0][1]=f[i+j+dn];
				w=wt;
				f[i+j]=w.a[0][0];
				f[i+j+dn]=w.a[0][1];
			}
		}
	}
}
```