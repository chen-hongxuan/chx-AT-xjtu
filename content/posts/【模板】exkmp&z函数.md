```cpp
int z[N],ex[N],n,m;
void get_z(){
	int l=1,r=1;z[1]=m;
	for(int i=2;i<=m;++i){
		if(i<=r)z[i]=min(z[i-l+1],r-i+1);
		while(i+z[i]<=m&&b[z[i]+1]==b[i+z[i]])++z[i];
		if(i+z[i]>r)l=i,r=i+z[i]-1;
	}
}

void get_ex(){
	while(a[1+ex[1]]==b[1+ex[1]]&&ex[1]+1<=n)++ex[1];
	int l=1,r=ex[1];
	for(int i=2;i<=n;++i){
		if(i+z[i-l+1]-1<r)ex[i]=z[i-l+1];
		else{
			ex[i]=max(0LL,r-i+1);
			while(b[ex[i]+1]==a[i+ex[i]]&&i+ex[i]<=n&&1+ex[i]<=m)++ex[i];
			l=i,r=i+ex[i]-1;
		}
	}
}
```