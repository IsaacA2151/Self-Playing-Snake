import time

class Decide:

	def __init__(self,snake,winWidth,winHeight,food,size,wallMode,walls):
		self.snake = snake
		self.winWidth = winWidth
		self.winHeight = winHeight
		self.food = food
		self.calcs = []
		self.size = size
		self.punishment = self.winWidth*self.winHeight
		self.upPos,self.rightPos,self.downPos,self.leftPos = True,True,True,True
		self.walls = walls

		if not wallMode:
			self.walls = []

	def checkSurroundings(self):
		up = [self.snake[0][0],self.snake[0][1]-self.size]
		right = [self.snake[0][0]+self.size,self.snake[0][1]]
		down = [self.snake[0][0],self.snake[0][1]+self.size]
		left = [self.snake[0][0]-self.size,self.snake[0][1]]

		if up in self.snake or (0-self.size) in up or up in self.walls:
			self.upPos = False
		if right in self.snake or 500 in right or right in self.walls:
			self.rightPos = False
		if down in self.snake or 500 in down or down in self.walls:
			self.downPos = False
		if left in self.snake or (0-self.size) in left or left in self.walls:
			self.leftPos = False

	def evalDir(self,up,down,left,right):
		# 0 up    1 right    2 down    3 left
		# self.snake[x][y]

		self.checkSurroundings()

		self.calcs = []

		if up:
			self.upCalc()
			self.rightCalc()
			# no down
			self.leftCalc()
			self.calcs.insert(2,self.punishment)
			
		if right:
			self.upCalc()
			self.rightCalc()
			self.downCalc()
			# no left
			self.calcs.insert(3,self.punishment)

		if down:
			# no up
			self.rightCalc()
			self.downCalc()
			self.leftCalc()
			self.calcs.insert(0,self.punishment)

		if left:
			self.upCalc()
			# no right
			self.downCalc()
			self.leftCalc()
			self.calcs.insert(1,self.punishment)

		#print('up right down left')
		#print(self.calcs)

		low = self.getLowest()

		#print(self.calcs)

		return low

	def upCalc(self):
		if self.upPos:
			self.calcs.append(self.manhatten_distance(self.snake[0][0],self.snake[0][1]-self.size,self.food[0],self.food[1]))
		else:
			self.calcs.append(self.punishment)

	def rightCalc(self):
		if self.rightPos:
			self.calcs.append(self.manhatten_distance(self.snake[0][0]+self.size,self.snake[0][1],self.food[0],self.food[1]))
		else:
			self.calcs.append(self.punishment)

	def downCalc(self):
		if self.downPos:
			self.calcs.append(self.manhatten_distance(self.snake[0][0],self.snake[0][1]+self.size,self.food[0],self.food[1]))
		else:
			self.calcs.append(self.punishment)

	def leftCalc(self):
		if self.leftPos:
			self.calcs.append(self.manhatten_distance(self.snake[0][0]-self.size,self.snake[0][1],self.food[0],self.food[1]))
		else:
			self.calcs.append(self.punishment)

	def getHighest(self):
		highest = 0
		for i in range(len(self.calcs)):
			if self.calcs[i] > self.calcs[highest]:
				highest = i

		return highest

	def getLowest(self):
		lowest = 0
		for i in range(len(self.calcs)):
			if self.calcs[i] < self.calcs[lowest]:
				lowest = i

		return lowest

	def manhatten_distance(self,x1,y1,x2,y2):
		score = abs(x1-x2) + abs(y1-y2)
		return score

