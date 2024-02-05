import numpy as np
diceresults=None
#      0 1 2 3  4  5  6 7 8 9 a
steps=(3,5,7,9,11,13,11,9,7,5,3)
dicecase=6**4
m1=dict()
def encode(src):
	return ((src[0]*6+src[1])*6+src[2])*6+src[3]
def decode(src):
	ret=[]
	for i in range(4):
		ret.append(src%6)
		src//=6
	return tuple(ret[::-1])
def add1(src):
	return (src[0]+src[1],src[2]+src[3])
def add2(src):
	return (src[0]+src[2],src[1]+src[3])
def add3(src):
	return (src[0]+src[3],src[1]+src[2])
def combine(src):
	# combine 4 dice points into 2 groups
	#print(src)
	return add1(src)+add2(src)+add3(src)
def calcgain(track,comb):
	return sum(1/steps[ele] for ele in comb if ele in track)
def maxgain1(track,state):
	return max(calcgain(track,f(state)) for f in [add1,add2,add3])
def solve():
	for i in range(11):
		for j in range(i+1,11):
			for k in range(j+1,11):
				Eplus=0
				freq=0
				for (state,fq) in diceresults:
					if len(set((i,j,k))&set(combine(decode(state)))):
						freq+=fq
						Eplus+=maxgain1((i,j,k),decode(state))*fq
				#print([i,j,k],Ebase,freq)
				m1[(i,j,k)]=(freq/dicecase,Eplus)
				#for l in range(0,10):
				#	print((freq/dicecase)**l*(Ebase+Eplus*l))
				#if i==5 and j==6 and k==7:
				#	exit(0)
def calc(src,h):#max at p**x*(a+bx)
	a=sum(y/steps[x-2] for (x,y) in zip(src,h))*dicecase
	p,b=m1[(src[0]-2,src[1]-2,src[2]-2)]
	buf=[p**x*(a+b*x) for x in range(18)]
	for i in range(10):
		print(i, buf[i])
	print("fail prob:",p)
	return buf.index(max(buf))
def prepare():
	global diceresults
	f=[0 for i in range(dicecase)]
	#roll 4 dice 
	for a in range(6):
		for b in range(6):
			for c in range(6):
				for d in range(6):
					lst=[a,b,c,d]
					lst.sort()
					f[encode(lst)]+=1
	diceresults=[(i,f[i]) for i in range(dicecase) if f[i]>0]
	for i in range(11):#to get the peak, the expect of the number of rolling dices for each num
		print(i+2,(steps[i])/(sum(y for (x,y) in diceresults if i in combine(decode(x)))/dicecase))

if __name__=='__main__':
	prepare()
	solve()

	
