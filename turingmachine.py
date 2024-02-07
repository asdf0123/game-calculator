from math import log2,factorial
from time import sleep
import traceback
from itertools import product,permutations
from copy import copy
def H(s):
	dic={}
	for ele in s:
		if ele in dic.keys():
			dic[ele]+=1
		else:
			dic[ele]=1
	bincount=dic.values()
	sb=sum(bincount)
	bincount=[ele/sb for ele in bincount]
	return sum(-p*log2(p) for p in bincount)
def mc(lst,m,r):
	return sum(ele%m==r for ele in lst)
def nc(lst,n):
	return sum(ele==n for ele in lst)
def f1(a,b,c,msk=0):
	if a==1:
		return "a =1"
	if a>1:
		return "a >1"
def f2(a,b,c,msk=0):
	if a<3:
		return "a <3"
	if a==3:
		return "a =3"
	if a>3:
		return "a >3"
	return None
def f3(a,b,c,msk=0):
	if b<3:
		return "b <3"
	if b==3:
		return "b =3"
	if b>3:
		return "b >3"
def f4(a,b,c,msk=0):
	if b<4:
		return "b <4"
	if b==4:
		return "b =4"
	if b>4:
		return "b >4"
def f5(a,b,c,msk=0):
	if a%2==0:
		return "a even"
	if a%2==1:
		return "a  odd"
	return None
def f6(a,b,c,msk=0):
	if b%2==0:
		return "b even"
	if b%2==1:
		return "b  odd"
	return None
def f7(a,b,c,msk=0):
	if c%2==0:
		return "c even"
	if c%2==1:
		return "c  odd"
	return None
def f8(a,b,c,msk=0):
	return "count1="+str(nc((a,b,c),1))
def f9(a,b,c,msk=0):
	return "count3="+str(nc((a,b,c),3))
def f10(a,b,c,msk=0):
	return "count4="+str(nc((a,b,c),4))
def f11(a,b,c,msk=0):
	if a<b:
		return "a <b"
	if a==b:
		return "a =b"
	if a>b:
		return "a >b"
	return None
def f12(a,b,c,msk=0):
	if a<c:
		return "a <c"
	if a==c:
		return "a =c"
	if a>c:
		return "a >c"
def f13(a,b,c,msk=0):
	if b<c:
		return "b <c"
	if b==c:
		return "b =c"
	if b>c:
		return "b >c"
	return None
def f14(a,b,c,msk=0):
	if a<b and a<c:
		return "a<min(bc)"
	if a>b and b<c:
		return "b<min(ac)"
	if a>c and b>c:
		return "c<min(ab)"
	return None
def f15(a,b,c,msk=0):
	if a>b and a>c:
		return "a>max(bc)"
	if a<b and b>c:
		return "b>max(ac)"
	if a<c and b<c:
		return "c>max(ab)"
	return None
def f16(a,b,c,msk=0):
	x,y=mc((a,b,c),2,0),mc((a,b,c),2,1)
	if x<y:
		return "more  odd"
	else:
		return "more even"
	return None
def f17(a,b,c,msk=0):
	return "counteven="+str(mc((a,b,c),2,0))
def f18(a,b,c,msk=0):
	if (a+b+c)&1:
		return "sumabc  odd"
	else:
		return "sumabc even"
	return None
def f19(a,b,c,msk=0):
	if a+b<6:
		return "sumab <6"
	if a+b==6:
		return "sumab =6"
	if a+b>6:
		return "sumab >6"
	return None
def f20(a,b,c,msk=0):
	if a!=b and a!=c and b!=c:
		return "1 same"
	if a==b and a==c:
		return "3 same"
	return "2 same"
def f21(a,b,c,msk=0):
	if a!=b and a!=c and b!=c:
		return "no exactly 2 same"
	if a==b and a==c:
		return "no exactly 2 same"
	return "   exactly 2 same"
def f22(a,b,c,msk=0):
	if a<b<c:
		return "inc+"
	elif a>b>c:
		return "dec-"
	else:
		return "badx"
def f23(a,b,c,msk=0):
	s=a+b+c
	if s<6:
		return "sum abc <6"
	if s==6:
		return "sum abc =6"
	if s>6:
		return "sum abc >6"

convolution=lambda X,Y:sum(x*y for x,y in zip(X,Y))
def cmpa1(a,b,c):#xref 1,31,39
	if a==1:
		return 0
	if a>1:
		return 1
	return None
def cmpb1(a,b,c):#xref 31,39
	if b==1:
		return 0
	if b>1:
		return 1
	return None
def cmpc1(a,b,c):#xref 31,39
	if c==1:
		return 0
	if c>1:
		return 1
	return None
def cmpa3(a,b,c):#xref 2,40
	if a<3:
		return 0
	if a==3:
		return 1
	if a>3:
		return 2
	return None
def cmpb3(a,b,c):#xref 3,40
	if b<3:
		return 0
	if b==3:
		return 1
	if b>3:
		return 2
	return None
def cmpc3(a,b,c):#xref 40
	if c<3:
		return 0
	if c==3:
		return 1
	if c>3:
		return 2
	return None
def cmpa4(a,b,c):#xref 41
	if a<4:
		return 0
	if a==4:
		return 1
	if a>4:
		return 2
	return None
def cmpb4(a,b,c):#xref 4,41
	if b<4:
		return 0
	if b==4:
		return 1
	if b>4:
		return 2
	return None
def cmpc4(a,b,c):#xref 41
	if c<4:
		return 0
	if c==4:
		return 1
	if c>4:
		return 2
	return None
def paritya(a,b,c):#xref 5
	return a&1
def parityb(a,b,c):#xref 6
	return b&1
def parityc(a,b,c):#xref 7
	return c&1
def count1(a,b,c):#xref 8
	return nc((a,b,c),1)
def count3(a,b,c):#xref 9
	return nc((a,b,c),3)
def count4(a,b,c):#xref 10
	return nc((a,b,c),4)
def cmpab(a,b,c):#xref 11,43,44,48
	if a<b:
		return 0
	if a==b:
		return 1
	if a>b:
		return 2
	return None
def cmpac(a,b,c):#xref 12,43,48
	if a<c:
		return 0
	if a==c:
		return 1
	if a>c:
		return 2
	return None
def cmpbc(a,b,c):#xref 13,44,48
	if b<c:
		return 0
	if b==c:
		return 1
	if b>c:
		return 2
	return None
def argmin(a,b,c):#xref 14,42
	if a<b and a<c:
		return 0
	if a>b and b<c:
		return 1
	if a>c and b>c:
		return 2
	return None
def argmax(a,b,c):#xref 15,42
	if a>b and a>c:
		return 0
	if a<b and b>c:
		return 1
	if a<c and b<c:
		return 2
	return None
def cmpevenodd(a,b,c):#xref 16
	x,y=mc((a,b,c),2,0),mc((a,b,c),2,1)
	if x<y:
		return 0
	if x>y:
		return 1
	return None
def counteven(a,b,c):#xref 17
	return mc((a,b,c),2,0)
def paritysumabc(a,b,c):#xref 18
	return (a+b+c)&1
def cmpsumab_6(a,b,c):#xref 19
	x=a+b
	if x<6:
		return 0
	if x==6:
		return 1
	if x>6:
		return 2
def samenum(a,b,c):#xref 20
	if a!=b and a!=c and b!=c:
		return 0
	if a==b and a==c:
		return 2
	return 1
def same2(a,b,c):#xref 21
	if a!=b and a!=c and b!=c:
		return 0
	if a==b and a==c:
		return 0
	return 1
def order(a,b,c):#xref 22
	if a<b<c:
		return 0
	if a>b>c:
		return 1
	return 2
def cmpsumabc_6(a,b,c):#xref 23
	x=a+b+c
	if x<6:
		return 0
	if x==6:
		return 1
	if x>6:
		return 2
def consecutiveinc(a,b,c):#xref 24
	if a+1==b and b+1==c:
		return 2
	if a+1==b or b+1==c:
		return 1
	return 0
def consecutivenum(a,b,c):#xref 25
	if abs(a-b)==1 and abs(c-b)==1:
		if a<b<c or a>b>c:
			return 2
		return 1#121 434
	if abs(a-b)==1 or abs(c-b)==1:
		return 1
	return 0
def alt3(a,b,c):#xref 26
	return int(a<3)
def blt3(a,b,c):#xref 26
	return int(b<3)
def clt3(a,b,c):#xref 26
	return int(c<3)
def alt4(a,b,c):#xref 27
	return int(a<4)
def blt4(a,b,c):#xref 27
	return int(b<4)
def clt4(a,b,c):#xref 27
	return int(c<4)
def aeq3(a,b,c):#xref 29
	return int(a==3)
def beq3(a,b,c):#xref 29
	return int(b==3)
def ceq3(a,b,c):#xref 29
	return int(c==3)
def aeq4(a,b,c):#xref 30
	return int(a==4)
def beq4(a,b,c):#xref 30
	return int(b==4)
def ceq4(a,b,c):#xref 30
	return int(c==4)
def agt3(a,b,c):#xref 32
	return int(a>3)
def bgt3(a,b,c):#xref 32
	return int(b>3)
def cgt3(a,b,c):#xref 32
	return int(c>3)
def aminimum(a,b,c):#xref 34
	return int(a<=b and a<=c)
def bminimum(a,b,c):#xref 34
	return int(a>=b and b<=c)
def cminimum(a,b,c):#xref 34
	return int(a>=c and b>=c)
def amaximum(a,b,c):#xref 35
	return int(a>=b and a>=c)
def bmaximum(a,b,c):#xref 35
	return int(a<=b and b>=c)
def cmaximum(a,b,c):#xref 35
	return int(a<=c and b<=c)
def sumabcdiv3(a,b,c):#xref 36
	return int((a+b+c)%3==0)
def sumabcdiv4(a,b,c):#xref 36
	return int((a+b+c)%4==0)
def sumabcdiv5(a,b,c):#xref 36
	return int((a+b+c)%5==0)
def sumabeq4(a,b,c):#xref 37
	return int(a+b==4)
def sumaceq4(a,b,c):#xref 37
	return int(a+c==4)
def sumbceq4(a,b,c):#xref 37
	return int(b+c==4)
def sumabeq6(a,b,c):#xref 38
	return int(a+b==6)
def sumaceq6(a,b,c):#xref 38
	return int(a+c==6)
def sumbceq6(a,b,c):#xref 38
	return int(b+c==6)
def count1_012(a,b,c):#xref 45,47
	x=nc((a,b,c),1)
	if x==3:
		return None
	return x
def count3_012(a,b,c):#xref 45,46
	x=nc((a,b,c),3)
	if x==3:
		return None
	return x
def count4_012(a,b,c):#xref 46,47
	x=nc((a,b,c),4)
	if x==3:
		return None
	return x

class G:#baseclass
	def __init__(self,flist,funcrange):
		self._flist=flist
		self._flen=len(flist)
		self._funcrange=funcrange
	def dump(self):
		return self._flist,self._funcrange
	def dumpf(self):
		assert 0<=self._mask<self._flen,"wtf"
		return self._flist[self._mask],self._funcrange[self._mask]
	def _getkey(self,key):
		a=key//100%10
		b=key//10%10
		c=key//1%10
		return a,b,c
	def setmask(self,mask):
		self._mask=mask
	def maskrange(self):
		return self._flen
	def setkey(self,key):
		a,b,c=self._getkey(key)
		tmp=[0]*self._funcrange[self._mask]
		idx=self._flist[self._mask](a,b,c)
		if idx is not None:
			tmp[idx]=1
		else:
			raise ValueError("wtf")
		self._key=tuple(tmp)
	#def testfkey(self,guess):
	#	a,b,c=self._getkey(guess)
	#	return self._flist[self._mask](a,b,c)
	def chkkey(self,guess):
		a,b,c=self._getkey(guess)
		tmp=[0]*self._funcrange[self._mask]
		idx=self._flist[self._mask](a,b,c)
		if idx is not None:
			tmp[idx]=1
		return convolution(tmp,self._key)
	def __add__(self,other):
		f1,r1=self.dump()
		f2,r2=other.dump()
		return G(f1+f2,r1+r2)
'''
https://cdn.1j1ju.com/medias/a6/12/e4-turing-machine-rulebook.pdf
'''
G1=G([cmpa1],[2])
G2=G([cmpa3],[3])
G3=G([cmpb3],[3])
G4=G([cmpb4],[3])
G5=G([paritya],[2])
G6=G([parityb],[2])
G7=G([parityc],[2])
G8=G([count1],[4])
G9=G([count3],[4])
G10=G([count4],[4])
G11=G([cmpab],[3])
G12=G([cmpac],[3])
G13=G([cmpbc],[3])
G14=G([argmin],[3])
G15=G([argmax],[3])
G16=G([cmpevenodd],[2])
G17=G([counteven],[4])
G18=G([paritysumabc],[2])
G19=G([cmpsumab_6],[3])
G20=G([samenum],[3])
G21=G([same2],[2])
G22=G([order],[3])
G23=G([cmpsumabc_6],[3])
G24=G([consecutiveinc],[3])
G25=G([consecutivenum],[3])
'''
本验证器验证了...是否有一个升序或降序且连续的序列
没有数字连续且按升序或降序排列
2个数字连续且按升序或降序排列
3个数字连续且按升序或降序排列
25

The Verifier verifies that there are either increasing or decreasing
values in a 2-digit consecutive sequence (e.g.: 312 or 254), a 3-digit
consecutive sequence (e.g.: 345 or 321), or none at all. (e.g.: 135 or
531 - in this example the 1-3 sequence is increasing, but 1 and 3 are not
consecutive numbers)

The Verifier does not know if the sequence is increasing or decreasing

323 和 325 返回值相同
f(323)*f(325)=1
'''
G26=G([alt3,blt3,clt3],[2]*3)
G27=G([alt4,blt4,clt4],[2]*3)
G28=G([cmpa1,cmpb1,cmpc1],[2]*3)#[aeq1,beq1,ceq1]
G29=G([aeq3,beq3,ceq3],[2]*3)
G30=G([aeq4,beq4,ceq4],[2]*3)
G31=copy(G28)#[agt1,bgt1,cgt1]
G32=G([agt3,bgt3,cgt3],[2]*3)
G33=G([paritya,parityb,parityc],[2]*3)
G34=G([aminimum,bminimum,cminimum],[2]*3)
G35=G([amaximum,bmaximum,cmaximum],[2]*3)
G36=G([sumabcdiv3,sumabcdiv4,sumabcdiv5],[2]*3)
G37=G([sumabeq4,sumaceq4,sumbceq4],[2]*3)
G38=G([sumabeq6,sumaceq6,sumbceq6],[2]*3)
G39=copy(G31)#[cmpa1,cmpb1,cmpc1]
G40=G([cmpa3,cmpb3,cmpc3],[3]*3)
G41=G([cmpa4,cmpb4,cmpc4],[3]*3)
G42=G([argmin,argmax],[3]*2)
G43=G([cmpab,cmpac],[3]*2)
G44=G([cmpab,cmpbc],[3]*2)
G45=G([count1_012,count3_012],[3]*2)
G46=G([count3_012,count4_012],[3]*2)
G47=G([count1_012,count4_012],[3]*2)
G48=G([cmpab,cmpac,cmpbc],[3]*3)



def calcmonoset(op):
	dicall={}
	#verifiers=[3,13,15,17]
	for a in range(1,6):
		for b in range(1,6):
			for c in range(1,6):
				#y=tuple(eval("f{}(a,b,c)".format(i)) for i in op)
				y=[]
				for f in op:
					y.append(f(a,b,c))
				y=tuple(y)
				#y=eval("({})".format(",".join(["f{}(a,b,c)"]*len(op))).format(*op))#revcursive
				if all([True if ele is not None else False for ele in y]):
					if y in dicall.keys():
						dicall[y].add(str(a)+str(b)+str(c))
					else:
						t=set()
						t.add(str(a)+str(b)+str(c))
						dicall[y]=t
	ret={}
	for k in dicall.keys():
		if len(dicall[k])==1:
			#print(k,dicall[k])
			ret[dicall[k].pop()]=k
	return ret
def determined(verifiers,silent=True):
	a=calcmonoset(verifiers)#necessary
	for i in range(len(verifiers)):
		b=calcmonoset(verifiers[:i]+verifiers[i+1:])#not sufficient
		if not silent:
			print("delete {} candidates by rule {}: {}".format(len(a.keys()&b.keys()),i,b.keys()))
		reserved=a.keys()-b.keys()
		a={key:a[key] for key in reserved}
	tosort=list((int(key),a[key]) for key in a.keys())
	tosort.sort(key=lambda x:x[1])

	#for ele in tosort:
	#	print(ele)
	candidate=[int(ele[0]) for ele in tosort]
	'''#verifiers=[3,13,15,17]'''
	return tosort
def solve(verifiers):
	vnum=len(verifiers)
	maskranges=[verifier.maskrange() for verifier in verifiers]
	candidates=[]
	for masks in product(*[range(ele) for ele in maskranges]):
		#print(masks)
		for i in range(vnum):
			verifiers[i].setmask(masks[i])
		fs=[verifier.dumpf()[0] for verifier in verifiers]
		onething=determined(fs)
		for ele in onething:
			candidates.append((ele[0],tuple(zip(masks,ele[1]))))
	candidates.sort(key=lambda x:x[1])
	return candidates
def dfs(candidatesnames,ratings,cols,depth=3):
	h=H(candidatesnames)
	if depth==0 or h<0.01:
		return h,set(candidatesnames),depth
	minh,mins,maxbonus=h,set(candidatesnames),depth
	for col in cols:
		candidatesnames0=tuple(candidatesnames[i] for i in range(len(candidatesnames)) if ratings[i][col]==False)
		candidatesnames1=tuple(candidatesnames[i] for i in range(len(candidatesnames)) if ratings[i][col]==True)
		ratings0=tuple(filter(lambda x: x[col]==False,ratings))
		ratings1=tuple(filter(lambda x: x[col]==True,ratings))
		w0,w1=len(candidatesnames0),len(candidatesnames1)
		w0,w1=w0/(w0+w1),w1/(w0+w1)
		h0,s0,bonus0=dfs(candidatesnames0,ratings0,cols-set([col]),depth-1)
		h1,s1,bonus1=dfs(candidatesnames1,ratings1,cols-set([col]),depth-1)
		h=w0*h0+w1*h1
		bonus=w0*bonus0+w1*bonus1
		if minh>h or (minh==h and maxbonus<bonus):
			minh,mins,maxbonus=h,(chr(col+ord("A")),s0,s1),bonus
	return minh,mins,maxbonus
def radix5tostr(x):
	return str(x//25+1)+str(x//5%5+1)+str(x%5+1)
decto5=lambda x:sum((int(a)-1)*(5**(b-1)) for a,b in zip(x,range(len(x),0,-1)))
def parseStrategy(s,depth=0):
	if type(s)==set:
		print(s)
	else:
		print(s[0])
		print("\t"*depth,False,end="\t")
		parseStrategy(s[1],depth+1)
		print("\t"*depth,True,end="\t")
		parseStrategy(s[2],depth+1)
	return None
def query(vnum,candidatesnames,ratings):
	h=H(candidatesnames)
	minh,mins=h,("111",set(candidatesnames))
	
	for depth in range(1,4):
		for num in range(5**3):
			h,s,bonus=dfs(candidatesnames,[ele[num] for ele in ratings],set(range(vnum)),depth)
			if minh>h:
				minh,mins=h,(radix5tostr(num),s)
		if minh<0.01:
			break
			
	print("False go left, true go right")
	print("H={}, suggest checking with information: {}".format(minh,mins))
	return minh,mins
def calcrating(verifiers,candidates):
	vnum=len(verifiers)
	buf=[]
	for candidate in candidates:
		for i in range(vnum):
			verifiers[i].setmask(candidate[1][i][0])
			verifiers[i].setkey(candidate[0])
		tmp=[]
		for a in range(1,6):
			for b in range(1,6):
				for c in range(1,6):
					k=int(str(a)+str(b)+str(c))
					val=tuple(verifier.chkkey(k) for verifier in verifiers)
					tmp.append(val)
		buf.append(tuple(tmp))
	return tuple(buf)
def show(answers):
	for answer in answers:
		print(answer)
	return None
def stdclassic(verifiers):
	fullverifiers=[eval("f{}".format(ele)) for ele in verifiers]
	ans=determined(fullverifiers,silent=False)
	show(ans)
	return None
simpleclassic=stdclassic
def prepare(fullverifiers):
	candidates=solve(fullverifiers)
	for candidate in candidates:
		print("candidate",candidate)
	candidatesnames=[candidate[0] for candidate in candidates]
	ratings=calcrating(fullverifiers,candidates)
	return candidatesnames,ratings
def getinput(vnum):
	guess=input("test num:\n")
	try:
		guess=decto5(guess)#int(guess[0])*25+int(guess[1])*5+int(guess[2])*1-1-5-25
		assert (type(guess)==int and 0<=guess<5**3),"wtf"
	except Exception as e:
		print(e.args)
		traceback.print_exc()
		return None

	s=input("verifier&value:\n").strip().split(",")
	s=[ele.split(":") for ele in s]
	filtexpr=[]
	for x,y in s:
		try:
			key=ord(x)-ord("A")
			assert (0<=key<vnum),"wtf"
			assert (y[0] in "YyTtNnFf"),"wtf"
			filtexpr.append((key,y[0] in "YyTt"))
		except Exception as e:
			print(e.args)
			traceback.print_exc()
			return None
	return guess,filtexpr

def subhardclassic(candidatesnames,ratings,vnum):
	while True:
		minh,mins=query(vnum,candidatesnames,ratings)
		print("enter {}".format(mins[0]))#just adivce
		parseStrategy(mins[1])#output
		if H(candidatesnames)<0.01:
			break
		#guess=mins[0]
		while True:
			result=getinput(vnum)
			if result:
				guess,filtexpr=result
				break
			else:
				print("wtf? try again")
				sleep(2)
		#print(s)
		fstr="lambda x:{}".format(" and ".join(["x[{}]=={}".format(*expr) for expr in filtexpr]))
		print(fstr)
		f=eval(fstr)
		#print(f)
		#print(ratings[0])
		#print(candidatesnames[0])
		#print(len(candidatesnames))
		#print(len(ratings))
		ratingscol=[rows[guess] for rows in ratings]
		candidatesnames=[candidatesnames[i] for i in range(len(ratingscol)) if f(ratingscol[i])]
		ratings=[ratings[i] for i in range(len(ratingscol)) if f(ratingscol[i])]
	return None
def hardclassic(verifiers):
	fullverifiers=[eval("G{}".format(ele)) for ele in verifiers]
	candidatesnames,ratings=prepare(fullverifiers)
	subhardclassic(candidatesnames,ratings,len(fullverifiers))
	return None
def hardextreme(verifiers1,verifiers2):
	fullverifiers=[eval("G{}+G{}".format(x,y)) for x,y in zip(verifiers1,verifiers2)]
	candidatesnames,ratings=prepare(fullverifiers)
	subhardclassic(candidatesnames,ratings,len(fullverifiers))
	return None
stdextreme=hardextreme
simpleextreme=stdextreme
def transpose_2d(data):
    # transposed = list(zip(*data))
    # [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
    # 注意 zip 本身返回的数据类型为 tuple 元组
    # 其中符号 * 号可以对元素进行解压或展开

    transposed = list(map(list, zip(*data)))
    return transposed
def hardnightmare(verifiers):
	fullverifiers=[eval("G{}".format(ele)) for ele in verifiers]
	vnum=len(fullverifiers)
	candidatesnames,ratings=prepare(fullverifiers)
	fullratings=[]
	fullcandidatesnames=[candidatename for candidatename in candidatesnames for _ in range(factorial(vnum))]
	for rating in ratings:
		buf=[list(permutations(ele)) for ele in rating]
		#print(len(buf),len(buf[0]))
		fullratings.extend(transpose_2d(buf))
		#print(len(fullratings),len(fullratings[0]))
	#print(*zip(fullcandidatesnames,range(len(fullcandidatesnames))))
	#print(len(fullratings))
	subhardclassic(fullcandidatesnames,fullratings,vnum)
	return None
stdnightmare=hardnightmare
simpenightmare=stdnightmare
def test():
	verifiers=[5,15,16,19,21]#[4,7,13,17,19,22]
	ans=stdclassic(verifiers)
	show(ans)

	print("="*80)
	verifiers=[5,15,16,19,21]#[7,19,24,25,33,36]
	hardclassic(verifiers)#interactive mode
	'''
	
	goodcase	verifiers=[3,13,15,17]
				(0, 0, 0)
				(0, 1, 1)
				(0, 1, 0)
				(1, 0, 0)
	multicase [19,20,24,31,33,45]#normal
	special I high [8,20,23,40,46,48]
	not balance [15,22,24,33,36,40]#key 551
	wtf [13,28,31,40] empty?
	
enter 114
B
 False	D
	 False	C
		 False	{512, 451, 452, 421, 241, 152, 541, 542}
		 True	{514, 521, 524, 154, 251, 254}
	 True	E
		 False	{425, 142, 145, 245, 215, 412, 125, 415}
		 True	{514, 214, 215, 154, 124, 125}
 True	C
	 False	D
		 False	{151, 511, 551}
		 True	{112, 515, 155}
	 True	F
		 False	{115, 511, 155, 515, 151}
		 True	{121, 211}
verifier&value:
B:T,C:F,D:F
[(1, True), (2, False), (3, False)]
False go left, true go right
H=0.0 check with ('152', ('D', ('F', {551}, {511}), ('F', {551}, {151})))
enter 152
D
 False	F
	 False	{551}
	 True	{511}
 True	F
	 False	{551}
	 True	{151}
verifier&value:
D:T,F:F        
[(3, True), (5, False)]
False go left, true go right
H=0.0 check with ('111', {551})
enter 111
{551}
	'''
if __name__=="__main__":
	#test()
	verifiers1=[13,28,31,40]#key 551 
	verifiers2=[13,4,16,5]
	#hardclassic(verifiers1)
	#simpleextreme(verifiers1,verifiers2)

	#hardclassic(verifiers1)
	#hardnightmare(verifiers1)
	hardclassic(verifiers1)
