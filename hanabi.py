
import traceback
mode1,mode2,mode3=1,2,3
print('''
	multicolor mode
	{}. no multicolor
	{}. multicolor is sixth color
	{}. multicolor is every color
'''.format(mode1,mode2,mode3))
multiflag=int(input("multicolor option: "))
handsize=int(input("how many card do you have: "))
assert(4<=handsize<=6)
colorstr="rygbw"
pointstr="12345"

color=set(colorstr)
point=set(pointstr)
if multiflag==mode2:
	color.add("m")
	colorstr+="m"
class Card:
	def __init__(self):
		self.colorcandidates=set(color)
		self.pointcandidates=set(point)
		if multiflag==mode3:
			self.canbemulti=True
			
	def filtcolor(self,c,hit):
		if hit:
			if multiflag==mode3 and len(self.colorcandidates)==1:
				ccopy=self.colorcandidates.pop()
				if ccopy!=c:
					self.colorcandidates=set(["m"])
				else:
					self.colorcandidates=set([c])
			else:
				self.colorcandidates=set([c])
		else:
			self.colorcandidates.discard(c)
			if multiflag==mode3:
				self.canbemulti=False
		return None
	
	def filtpoint(self,p,hit):
		if hit:
			self.pointcandidates=set([p])
		else:
			self.pointcandidates.discard(p)
		return None
	
	def __str__(self):
		colorcandidates="".join(ch if ch in self.colorcandidates else " " for ch in colorstr)
		pointcandidates="".join(ch if ch in self.pointcandidates else " " for ch in pointstr)
		if multiflag==mode3:
			colorcandidates+="m" if self.canbemulti else " "
		return "|{}|--|{}|".format(colorcandidates,pointcandidates)
class Hand():
	def __init__(self):
		self.cards=[Card() for _ in range(handsize)]
	
	def filtcolor(self,c,hitset):
		for i,card in enumerate(self.cards):
			card.filtcolor(c,i in hitset)
		return None
		
	def filtpoint(self,p,hitset):
		for i,card in enumerate(self.cards):
			card.filtpoint(p,i in hitset)
		return None
	
	def showhand(self):
		print("v left")
		for i,card in enumerate(self.cards):
			print("| idx {}: {}".format(i,str(card)))
		print("v right")
		return None
	
	def reset(self,idx):
		assert(0<=idx<handsize)
		self.cards=[Card()]+self.cards[:idx]+self.cards[idx+1:]

def parseargs():
	banner='''
		1. color clue
		2. point clue
		3. play/discard one and draw one
	'''
	print(banner)
	while True:
		try:
			op=int(input("your option: "))
			if op==-1:
				return -1,None
			if op==1:
				c=input("color[{}]:".format(colorstr)).strip()
				assert (len(c)==1 and c in colorstr)
				hitpos=list(map(int,input("positions split with comma: ").strip().split(",")))
				for pos in hitpos:
					assert(0<=pos<handsize)
				print("checking color '{}' at position {}".format(c,hitpos))
				args=(c,set(hitpos))
			elif op==2:
				c=input("point[{}]:".format(pointstr)).strip()
				assert (len(c)==1 and c in pointstr)
				hitpos=list(map(int,input("positions split with comma: ").strip().split(",")))
				for pos in hitpos:
					assert(0<=pos<handsize)
				print("checking point '{}' at position {}".format(c,hitpos))
				args=(c,set(hitpos))
			elif op==3:
				idx=int(input("card position: "))
				assert(0<=idx<handsize)
				print("play/discard the card at position {} from left".format(idx))
				args=(idx,)
			confirm=input("are you sure?[Y/n] (n for input again): ").strip()
			if len(confirm)==0 or confirm[0] in "Yy":
				return op,args
		except Exception as e:
			print(e.args)
			traceback.print_exc()
			return None,None
if __name__=="__main__":
	hand=Hand()
	hand.showhand()
	while True:
		op,args=parseargs()
		if op==1:
			hand.filtcolor(*args)
		elif op==2:
			hand.filtpoint(*args)
		elif op==3:
			hand.reset(*args)
		elif op==-1:
			break
		else:
			print("wtf")
			
		hand.showhand()
		
