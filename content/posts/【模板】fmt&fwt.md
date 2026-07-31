FMT

```cpp
struct FMT{
	int fmt[1<<N];
	void insert(int *f){
		for(int i=0;i<n;++i)fmt[i]=f[i];
	}
	void FMT_or(int tag){
		for(int o=2,k=1;o<=n;o<<=1,k<<=1){
			for(int i=0;i<n;i+=o){
				for(int j=0;j<k;++j){
					(fmt[i+j+k]+=mo+fmt[i+j]*tag)%=mo;
				}
			}
		}
	}
	void FMT_and(int tag){
		for(int o=2,k=1;o<=n;o<<=1,k<<=1){
			for(int i=0;i<n;i+=o){
				for(int j=0;j<k;++j){
					(fmt[i+j]+=mo+fmt[i+j+k]*tag)%=mo;
				}
			}
		}
	}
}A,B;
```

FWT

```cpp
struct FWT{
	int fwt[1<<N];
	void insert(int *f){
		for(int i=0;i<n;++i)fwt[i]=f[i];
	}
	void FWT_(int tag){
		for(int o=2,k=1;o<=n;o<<=1,k<<=1){
			for(int i=0;i<n;i+=o){
				for(int j=0;j<k;++j){
					int x=fwt[i+j],y=fwt[i+j+k];
					fwt[i+j]=(x+y)%mo;
					fwt[i+j+k]=(x+mo-y)%mo;
					if(tag==-1){
						fwt[i+j]=fwt[i+j]*499122177LL%mo;
						fwt[i+j+k]=fwt[i+j+k]*499122177LL%mo;
					}
				}
			}
		}
	}
}A,B;
```