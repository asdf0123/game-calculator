from copy import copy
from bisect import bisect_right
piecenames=["sun","luna","star","comet"]
dp={}
class Status:
	def chksum(self):
		assert(sum(sum(h*n for (h,n) in group) for group in self.groups)==12)
		return None
	def __init__(self,groups):
		assert(len(groups)==4)
		self.groups=groups
		self.chksum()
		return None
	def pivot(self):
		a,b,c,d=map(tuple,map(sorted,self.groups))
		#print(a,b,c,d)
		a,b,c,d=sorted(zip((a,b,c,d),range(4)),key=lambda x:(len(x),x))
		self.groups=(a[0],b[0],c[0],d[0])
		return (a[1],b[1],c[1],d[1])
	def unlink(self,h,t):
		#print(self.groups)
		groupt=self.groups[t]
		idx=bisect_right(groupt,(h,0))
		hit=groupt[idx]
		assert hit[0]==h
		assert hit[1]>0
		newn=hit[1]-1
		if newn>=1:
			newstatust=groupt[:idx]+((h,hit[1]-1),)+groupt[idx+1:]
		else:
			newstatust=groupt[:idx]+groupt[idx+1:]
		self.groups=self.groups[:t]+(newstatust,)+self.groups[t+1:]
		return 
	def link(self,h,t):
		groupt=self.groups[t]
		idx=bisect_right(groupt,(h,0))
		if idx==len(groupt) or groupt[idx][0]>h:#empty
			newstatust=groupt[:idx]+((h,1),)+groupt[idx:]
		else:
			hit=groupt[idx]
			assert hit[0]==h
			assert hit[1]>0
			newstatust=groupt[:idx]+((h,hit[1]+1),)+groupt[idx+1:]
		self.groups=self.groups[:t]+(newstatust,)+self.groups[t+1:]
	def trymov(self,h1,h2,t1,t2):
		status=Status(self.groups)
		status.unlink(h1,t1)
		status.unlink(h2,t2)
		status.link(h1+h2,t1)
		status.chksum()
		status.pivot()
		if status.groups not in dp.keys():
			status.choice()
		return status.groups
	
	def realmov(self,h1,h2,t1,t2):
		#status=Status(self.groups)
		self.unlink(h1,t1)
		self.unlink(h2,t2)
		self.link(h1+h2,t1)
		self.chksum()
		self.pivot()
		assert self.groups in dp.keys()
		#if status.groups not in dp.keys():
		#	status.choice()
		return None
	def choice(self):
		buf=[]
		for t,group in enumerate(self.groups):
			for h,n in group:
				buf.append((h,t,n))#there're n height h, type t pieces
		ans=[(0,(1000,0,1000,0))]
		for i in range(len(buf)):
			h1,t1=buf[i][:2]
			for j in range(len(buf)):
				h2,t2=buf[j][:2]
				if h1!=h2 and t1!=t2:
					continue
				if h1==h2 and t1==t2 and buf[j][2]==1:#same but not enough piece
					continue
				if t1==t2 and h1>h2:#symmetric
					continue
				#printf("{} {}".format(t1,t2))
				solution=(h1,h2,t1,t2)
				solutiongroups=self.trymov(*solution)
				assert solutiongroups in dp
				ans.append((dp[solutiongroups]+1,solution))
		evenmove=list(filter(lambda x:x[0]&1==0,ans))#loss
		oddmove=list(filter(lambda x:x[0]&1==1,ans))#win
		oddmove.sort(key=lambda x:x)
		evenmove.sort(key=lambda x:(-x[0],x[1:]))
		#print("======")
		#print(oddmove,evenmove)
		#print("======")
		ans=oddmove+evenmove
		if len(oddmove)==0:
			dp[self.groups]=max(ele for ele,_ in evenmove)
		else:
			dp[self.groups]=min(ele for ele,_ in oddmove)
		return ans
class Chequer(Status):
	def __init__(self,nums):
		super().__init__(tuple(((1,num),) if num else () for num in nums))#(h,n):n of height h
		self.namemap=list(range(4))
		return None
	def pivot(self):
		idxs=super().pivot()
		self.namemap=tuple(self.namemap[idx] for idx in idxs)
		return idxs
	def show(self):
		#print(self.groups,self.namemap)
		for samepiece,nameidx in zip(self.groups,self.namemap):
			for pieceheight,piecenum in samepiece:
				for j in range(piecenum):
					print("{:^5} {:>2}:  {}".format(piecenames[nameidx],pieceheight,"-"*pieceheight))
		print("{} piece in total".format(sum(piecenum for samepiece in self.groups for pieceheight,piecenum in samepiece)))
			
	def showchoice(self,ans):
		for i,(val,(h1,h2,t1,t2)) in enumerate(ans):
			#print(i,(val,(h1,h2,t1,t2)))
			if h1>12 or h2>12:
				print("{:>2}. I choose death.".format(i))
				continue
			print("{:>2}. move type {:^5} of height {} onto type {:^5} of height {}:".format(i,piecenames[self.namemap[t1]],h1,piecenames[self.namemap[t2]],h2),end="")
			print("win " if val&1 else "loss",end=" in {} move\n".format(val))
		return None
	def choice(self):
		ans=super().choice()
		self.showchoice(ans)
		op=int(input("your option: "))
		assert(0<=op<len(ans))
		self.realmov(*ans[op][1])
		return len(ans)>0
if __name__=="__main__":
	nums=list(map(int,input("the number of {}, {}, {} and {}: ".format(*piecenames)).split(",")))
	chequer=Chequer(nums)
	
	#exit(0)
	chequer.pivot()
	flag=True
	while flag:
		#chequer.pivot()
		chequer.show()
		flag=chequer.choice()
