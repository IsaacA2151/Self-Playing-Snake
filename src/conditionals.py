'''class Conditionals:

	def __init__(self, x, y, s, w, sz):
		# s = snake or any list of already filled points
		# w = max length of grid / area
		self.x = x
		self.y = y
		self.snake = s
		self.width = w
		self.size = sz
		self.N = True
		self.E = True
		self.W = True
		self.S = True

	def checkEnv(self):
		limit = self.size
		#print('O {}'.format(self.o))
		#print('[X {} Y {}] size {}'.format(self.x,self.y,self.size))
		#print('N {} E {} S {} W {}'.format([self.x-self.size,self.y],[self.x+self.size,self.y],[self.x,self.y-self.size],[self.x,self.y+self.size]))
		if self.y == 0 or [self.x,self.y-self.size] in self.snake:
			self.N = False
		if self.y == limit or [self.x,self.y+self.size] in self.snake:
			self.S = False
		if self.x == 0 or [self.x-self.size,self.y] in self.snake:
			self.W = False
		if self.x == limit or [self.x+self.size,self.y] in self.snake:
			self.E = False

		#print("N {} E {} S {} W {}".format(self.N,self.E,self.S,self.W))'''

class Conditionals:

	def __init__(self, grid, x, y, o=[], s=0):
		self.x = x
		self.y = y
		self.o = o
		if len(grid) < 2:
			self.limit = s
		else:
			self.limit = grid
		self.N = True
		self.E = True
		self.W = True
		self.S = True

	def checkEnv(self):
		if self.y == 0 or [self.y-1,self.x] in self.o:
			self.N = False
		if self.y == self.limit or [self.y+1,self.x] in self.o:
			self.S = False
		if self.x == 0 or [self.y,self.x-1] in self.o:
			self.W = False
		if self.x == self.limit or [self.y,self.x+1] in self.o:
			self.E = False

		print("{} {}\n {}  {}  {}  {}".format(self.x,self.y,int(self.N),int(self.E),int(self.S),int(self.W)))
