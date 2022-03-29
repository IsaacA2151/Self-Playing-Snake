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
