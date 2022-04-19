# E:\python_projects\pygame\snake_ai_not_ml\new work in progress

import pygame
import random
import time
import snake_decisions
import senses
import conditionals

pygame.init()

#### MODES ####

speedIncreaseMode = False
wallMode = False

winWidth = 500
winHeight = 500
boardSize = 20
win = pygame.display.set_mode((winWidth,winHeight))
timeDelay = 20
wallCap = 20

sx = winWidth/2 
sy = winHeight/2
size = int(winWidth/boardSize)
start = sx,sy
ds = size*2

newX = sx
newY = sy

snake = [[newX,newY],[newX-(size),newY],[newX-(size)*2,newY]]
#snake = [[325.0, 150.0], [350.0, 150.0], [350.0, 125.0], [350.0, 100.0], [350.0, 75.0], [350.0, 50.0], [325.0, 50.0], [300.0, 50.0], [300.0, 75.0], [300.0, 100.0], [300.0, 125.0], [300.0, 150.0], [300.0, 175.0], [300.0, 200.0], [300.0, 225.0], [275.0, 225.0], [250.0, 225.0], [225.0, 225.0], [225.0, 250.0], [225.0, 275.0], [200.0, 275.0], [175.0, 275.0], [175.0, 300.0], [150.0, 300.0], [150.0, 275.0], [125.0, 275.0], [100.0, 275.0]]

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,255,255)
FULL_BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,50,0)  

up,right,down,left = False,False,True,False
game = True
run = False

touchingFood = False

wallCounter = 0
walls = []

def touching():
	global snake,game,winWidth,winHeight,food,touchingFood,timeDelay,walls

	for i in range(1,len(snake)):
		try:
			if snake[0] == snake[i]:
				respawn()
				#game = False
				#time.sleep(5)
		except:
			pass

	if snake[0] == food:
		#print(len(snake))
		touchingFood = True

		if speedIncreaseMode:
			timeDelay -= 2

		spawnFood()

	if snake[0][0] > winWidth-size or snake[0][0] < 0 or snake[0][1] > winHeight-size or snake[0][1] < 0:
		respawn()
		#game = False
		#time.sleep(5)

	if snake[0] in walls:
		respawn()

def spawnFood():
	global snake,boardSize,food,walls

	food = [random.randint(0,9)*50,random.randint(0,9)*50]

	if food in snake or food in walls:
		while food in snake or food in walls:
			food = [random.randint(0,9)*50,random.randint(0,9)*50]

def spawnWall():
	global snake,boardSize,food,walls

	newWall = [random.randint(0,9)*50,random.randint(0,9)*50]

	if newWall in walls or newWall in food or newWall in snake:
		while newWall in walls or newWall in food or newWall in snake:
			newWall = [random.randint(0,9)*50,random.randint(0,9)*50]

	walls.append(newWall)

def respawn():
	global sx,sy,start,size,newX,newY,snake,up,down,left,right,timeDelay,walls,speedIncreaseMode

	walls = []

	if speedIncreaseMode:
		timeDelay = 100

	sx = winWidth/2
	sy = winHeight/2
	start = sx,sy

	newX = sx
	newY = sy

	snake = [[sx,sy],[sx-size,sy],[sx-(size*2),sy]]

	up,down,left,right = False,False,False,False

def drawVision(u,d,l,r):
	toDraw = []

	if u:
		for i in range(int(snake[0][1])-size,0-size,-size):
			s = [int(snake[0][0]),i]
			if s == food or s in snake:
				break
			else:
				toDraw.append(s)
	if d:
		for i in range(int(snake[0][1])+size,winHeight,size):
			s = [int(snake[0][0]),i]
			if s == food or s in snake:
				break
			else:
				toDraw.append(s)
	if l:
		for i in range(int(snake[0][0])-size,0-size,-size):
			s = [i,snake[0][1]]
			if s == food or s in snake:
				break
			else:
				toDraw.append(s)
	if r:
		for i in range(int(snake[0][0])+size,winWidth,size):
			s = [i,snake[0][1]]
			if s == food or s in snake:
				break
			else:
				toDraw.append(s)

	for i in toDraw:
		pygame.draw.rect(win,(BLUE),(i[0],i[1],size,size))

spawnFood()

while game:

	d = snake_decisions.Decide(snake,winWidth,winHeight,food,size,wallMode,walls)
	move = d.evalDir(up,down,left,right)

	con = conditionals.Conditionals([0],snake[0][0],snake[0][1],snake,winWidth)
	con.checkEnv()

	horizontal = con.E and con.W
	vertical = con.N and con.S

	if up and [snake[0][0],snake[0][1]-ds] in snake:
		#s = senses.Around(snake, winWidth, size, 'up')
		#s.calc()
		if horizontal:
			print(con.E, con.W)
			#time.sleep(5)
	if right and [snake[0][0]+ds,snake[0][1]] in snake:
		#s = senses.Around(snake, winWidth, size, 'right')
		#s.calc()
		if vertical:
			print(con.N, con.S)
			#time.sleep(5)
	if down and [snake[0][0],snake[0][1]+ds] in snake:
		#s = senses.Around(snake, winWidth, size, 'down')
		#s.calc()
		if horizontal:
			print(con.E, con.W)
			#time.sleep(5)
	if left and [snake[0][0]-ds,snake[0][1]] in snake:
		#s = senses.Around(snake, winWidth, size, 'left')
		#s.calc()
		if vertical:
			print(con.N, con.S)
			#time.sleep(5)


	#print(d.upPos,d.rightPos,d.downPos,d.leftPos,snake[0])

	if move == 0:
		up,right,down,left = True,False,False,False
		#print('up')
	elif move == 1:
		up,right,down,left = False,True,False,False
		#print('right')
	elif move == 2:
		up,right,down,left = False,False,True,False
		#print('down')
	elif move == 3:
		up,right,down,left = False,False,False,True
		#print('left')
	
	if wallMode:
		wallCounter += 1

	for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        game = False

                if event.type == pygame.KEYDOWN:
                	run = True
                	if event.key == pygame.K_UP:
                		up,right,down,left = True,False,False,False
                	if event.key == pygame.K_RIGHT:
                		up,right,down,left = False,True,False,False
                	if event.key == pygame.K_DOWN:
                		up,right,down,left = False,False,True,False
                	if event.key == pygame.K_LEFT:
                		up,right,down,left = False,False,False,True

	win.fill(BLACK) 

	if run:
		if not touchingFood:
			del snake[len(snake)-1]
		else:
			touchingFood = False

		if up:
			newY -= size
		if right:
			newX += size
		if down:
			newY += size
		if left:
			newX -= size

		snake.insert(0,[newX,newY])	

	pygame.draw.rect(win,(FULL_BLUE),(snake[0][0],snake[0][1],size,size))

	for i in range(1,len(snake)):
		pygame.draw.rect(win,(WHITE),(snake[i][0],snake[i][1],size,size))

	pygame.draw.rect(win,(RED),(food[0],food[1],size,size))

	#drawVision(up,down,left,right)

	if len(walls) > 0:
		for i in range(len(walls)):
			pygame.draw.rect(win,(GREEN),(walls[i][0],walls[i][1],size,size))

	touching()

	if wallCounter == wallCap:
		spawnWall()
		wallCounter = 0

	pygame.time.delay(timeDelay)                 

	pygame.display.flip()                       

pygame.quit()                     
