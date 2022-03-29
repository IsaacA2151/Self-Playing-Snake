import conditionals

class Around:

				#width, size
	def __init__(self, snake, w, s, direction):
		self.snake = snake
		self.y = snake[0][1]
		self.x = snake[0][0]
		self.o = snake
		self.w = w
		self.s = s
		self.d = direction													

	def setUp(self):
		# left also down, right also up

		if self.d == 'up':
			self.lx,self.ly = self.x-self.s,self.y
			self.rx,self.ry = self.x+self.s,self.y
		elif self.d == 'down':
			self.lx,self.ly = self.x-self.s,self.y
			self.rx,self.ry = self.x+self.s,self.y
		elif self.d == 'left':
			self.lx,self.ly = self.x,self.y+self.s
			self.rx,self.ry = self.x,self.y-self.s
		elif self.d == 'right':
			self.lx,self.ly = self.x,self.y+self.s
			self.rx,self.ry = self.x,self.y-self.s

	def calc(self):
		self.setUp()

		lSpaces,rSpaces = [],[]
		lCon = conditionals.Conditionals([],self.lx,self.ly,self.snake,self.w,self.s)
