---
title: 【模板】ntt
date: 2026-07-31T00:00:00+08:00
tags:
  - oist
math: true
draft: false
---

```cpp
int cir[N];
void fft(int *f,int len,int t){
	memset(cir,0,sizeof(int)*len);
	for(int i=0;i<len;++i){
		cir[i]=(cir[i>>1]>>1)|((i&1)?len>>1:0);
		if(i>cir[i]){
			swap(f[i],f[cir[i]]);
		}
	}
	for(int n=2;n<=len;n<<=1){
		int dn=n>>1,w=qpow(t?g:ig,(mo-1)/n);
		for(int i=0;i<len;i+=n){
			int q=1,f1,f2;
			for(int j=0;j<dn;++j,q=q*w%mo){
				f1=f[i+j],f2=f[i+j+dn];
				f[i+j]=(f1+f2*q%mo)%mo;
				f[i+j+dn]=(f1+mo-f2*q%mo)%mo;
			}
		}
	}
	if(!t){
		int fac=qpow(len,mo-2);
		for(int i=0;i<len;++i){
			f[i]=f[i]*fac%mo;
		}
	}
}
```