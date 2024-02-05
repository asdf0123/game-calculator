#include<bits/stdc++.h>
#define pii pair<int,int>
#define piiii pair<pii,pii >
using namespace std;

map<unsigned int,int>tc[3600];//
pair<int,unsigned int> hash(const map<pii,int>&m){
	int a[4][13]={{0}},i,j,n,ret=0;
	long long wt[4]={0};
	map<pii,int>::const_iterator it;
	pii t;
	unsigned int H=0;
	//puts("???0");
	for(it=m.begin();it!=m.end();it++){
		t=it->first;
		n=it->second;
		for(i=0;i<n;i++)
			a[t.second][++a[t.second][0]]=t.first;
	}
	for(i=0;i<4;i++){
		sort(a[i]+1,a[i]+a[i][0]+1,greater<int>());
		for(j=1;j<=a[i][0];j++)
			wt[i]=wt[i]*13+a[i][j];//priority:count>first height>second height>...
	}
	//puts("???1");
	int index[4]={0,1,2,3};//type hash: first->new type; second ->prev type
	for(i=0;i<4;i++)
		for(j=i+1;j<4;j++)
			if(wt[index[i]]<wt[index[j]])
				swap(index[i],index[j]);
	for(i=0;i<4;i++)
		ret=ret*7+a[index[i]][0];
	//index[0] is the greatest type
	for(i=0;i<4;i++)
		for(j=1;j<=a[index[i]][0];j++)
			H=H*7+a[index[i]][j];
	
	//puts("???2");
	return make_pair(ret,H);
}
int subsolve(const map<pii,int>&m){
	pair<int,unsigned int>t=hash(m);
	int typeidx=t.first;
	unsigned int heightidx=t.second;
	pii t1,t2,a,b;
	int p=0,temp;
	map<pii,int>::const_iterator st,ed,it;
	map<pii,int> tmp;
	//printf("%d %u\n",typeidx,heightidx);
	if(tc[typeidx].find(heightidx)!=tc[typeidx].end()){
		//for(it=m.begin();it!=m.end();it++)
		//	printf("[%d,%d]=%d ",it->first.first,it->first.second,it->second);
		//printf("%f\n",tc[typeidx][heightidx]);
		return tc[typeidx][heightidx];
	}
	//puts(">>>");
	for(st=m.begin();st!=m.end();st++){
		t1=st->first;
		if(st->second>=2){
			tmp.erase(tmp.begin(),tmp.end());
			for(it=m.begin();it!=m.end();it++){
				if(it!=st)
					tmp[it->first]+=it->second;
				else if(it->second>2)
					tmp[it->first]+=(it->second-2);
			}
			tmp[make_pair(t1.first+t1.first,t1.second)]+=1;
			temp=1-subsolve(tmp);
			if(p<temp)
				p=temp;
		}
		ed=st;
		for(ed++;ed!=m.end();ed++){
			t2=ed->first;
			if(t1.first!=t2.first&&t1.second!=t2.second)
				continue;
				
			tmp.erase(tmp.begin(),tmp.end());
			for(it=m.begin();it!=m.end();it++){
				if(it!=st&&it!=ed)
					tmp[it->first]+=it->second;
				else if(it->second-1)
					tmp[it->first]+=(it->second-1);
			}
			tmp[make_pair(t1.first+t2.first,t1.second)]+=1;//first top
			temp=1-subsolve(tmp);
			if(p<temp)
				p=temp;
			if(t1.second!=t2.second){//not same type
				if(tmp[make_pair(t1.first+t2.first,t1.second)]-1)
					tmp[make_pair(t1.first+t2.first,t1.second)]-=1;
				else
					tmp.erase(make_pair(t1.first+t2.first,t1.second));
				tmp[make_pair(t1.first+t2.first,t2.second)]+=1;//second first
				temp=1-subsolve(tmp);
				if(p<temp)
					p=temp;
			}
		}
	}/*
	for(it=m.begin();it!=m.end();it++){
		printf("[%d,%d]=%d ",it->first.first,it->first.second,it->second);
	}
	printf("%f\n",p);
	puts("<<<");*/
	return tc[typeidx][heightidx]=p;
}
int solve(const map<pii,int>&m,piiii &ret){
	pii t1,t2,a,b;
	int p=0,temp;
	piiii solu;
	map<pii,int>::const_iterator st,ed,it;
	map<pii,int> tmp;
	//puts(">>>");
	for(st=m.begin();st!=m.end();st++){
		t1=st->first;
		if(st->second>=2){
			tmp.erase(tmp.begin(),tmp.end());
			for(it=m.begin();it!=m.end();it++){
				if(it!=st)
					tmp[it->first]+=it->second;
				else if(it->second>2)
					tmp[it->first]+=(it->second-2);
			}
			tmp[make_pair(t1.first+t1.first,t1.second)]+=1;
			temp=1-subsolve(tmp);
			if(p<temp){
				ret=make_pair(t1,t1);
				p=temp;
			}
		}
		ed=st;
		for(ed++;ed!=m.end();ed++){
			t2=ed->first;
			if(t1.first!=t2.first&&t1.second!=t2.second)
				continue;
				
			tmp.erase(tmp.begin(),tmp.end());
			for(it=m.begin();it!=m.end();it++){
				if(it!=st&&it!=ed)
					tmp[it->first]+=it->second;
				else if(it->second-1)
					tmp[it->first]+=(it->second-1);
			}
			tmp[make_pair(t1.first+t2.first,t1.second)]+=1;//first top
			temp=1-subsolve(tmp);
			if(p<temp){
				ret=make_pair(t1,t2);
				p=temp;
			}
			if(t1.second!=t2.second){//not same type
				if(tmp[make_pair(t1.first+t2.first,t1.second)]-1)
					tmp[make_pair(t1.first+t2.first,t1.second)]-=1;
				else
					tmp.erase(make_pair(t1.first+t2.first,t1.second));
				tmp[make_pair(t1.first+t2.first,t2.second)]+=1;//second first
				temp=1-subsolve(tmp);
				if(p<temp){
					ret=make_pair(t2,t1);
					p=temp;
				}
			}
		}
	}/*
	for(it=m.begin();it!=m.end();it++){
		printf("[%d,%d]=%d ",it->first.first,it->first.second,it->second);
	}
	printf("%f\n",p);
	puts("<<<");*/
	return p;
}
int main(){
	char p[4][9]={"ri","yue","xing","hui"};
	int x,b,c,i,cnt,T;
	piiii solu;
	map<pii,int> m;
	for(scanf("%d",&T);T;T--){
		cnt=0;
		m.erase(m.begin(),m.end());
		do{
			scanf("%d",&x);
			if(!x)
				break;
			scanf("%d %d",&b,&c);//height type
			cnt+=x*b;
			m[make_pair(b,c)]=x;
		}while(true);
		if(cnt!=12){
			printf("mismatch, %d chess\n",cnt);
			continue;
		}
		printf("\t%f\n",solve(m,solu));
		printf("\t(h,t):(%d,%s)->(%d,%s)\n",solu.first.first,p[solu.first.second],solu.second.first,p[solu.second.second]);
	}
}
