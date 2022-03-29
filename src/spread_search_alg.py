################ IN PROGRESS ################

import conditionals

size = 11

wall = '£'

grid = [['#' for i in range(size)] for i in range(size)]

'''
grid = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
	['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
	['#', '#', '#', '#', '#', '#', '!', '!', '!', '!', '#'],
	['#', '#', '#', '#', '#', '#', '!', '#', '#', '!', '#'],
	['#', '#', '!', '!', '!', '!', '!', '#', '#', '!', '#'],
	['#', '#', '!', '#', '#', 's', '#', '#', '#', '!', '#'],
	['#', '#', '!', '#', '#', '!', '#', '#', '#', '!', '#'],
	['#', '#', '!', '#', '#', '!', '#', '#', '#', '!', '#'],
	['#', '#', '!', '!', '!', '!', '!', '!', '!', '!', '#'],
	['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
	['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
'''

new = [[] for i in range(size)]
walls = [[2, 6], [2, 7], [2, 8], [2, 9], [3, 6], [3, 9], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 9], [5, 2], [5, 9], [6, 2], [6, 5], [6, 9], [7, 2], [7, 5], [7, 9], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9]]

y,x = 5,5

locs = [[y,x]]
grid[y][x] = 'S'

def mark():
	for i in range(len(grid)):
		for k in range(len(grid[i])):
			if grid[i][k] == 's':
				locs.append([i,k])
			elif grid[i][k] == wall:
				walls.append([i,k])
	print(locs,'\n',walls)

def printGrid():
	for i in grid:
		#print(' '.join(i))
		print(''.join(i))

#def spread(sideArr, ):

def run():
	global y,x

	r = [[y,x+1]]
	l = [[y,x-1]]
						
	lGoing, rGoing = True, True
	lLen, rLen = 0,0	
	
	while lGoing and rGoing:
		for i in range(len(r)):
			print('r')
			y,x = r[i][0],r[i][1]

			con = conditionals.Conditionals(grid,x,y,walls+l+locs+r)
			con.checkEnv()

			if con.N:
				r.append([y-1,x])
			if con.E:
				r.append([y,x+1])
			if con.S:
				r.append([y+1,x])
			if con.W:
				r.append([y,x-1])

			if rLen == len(r):
				rGoing = False
				break

			rLen = len(r)

		for i in range(len(l)):
			lGoing = False
			print('l',lLen,len(l))
			y,x = l[i][0],l[i][1]

			con = conditionals.Conditionals(grid,x,y,walls+r+locs+l)
			con.checkEnv()

			if con.N:
				l.append([y-1,x])
			if con.E:
				l.append([y,x+1])
			if con.S:
				l.append([y+1,x])
			if con.W:
				l.append([y,x-1])

			print(lLen,len(l))

			if lLen == len(l):
				lGoing = False
				break

			lLen = len(l)

	for i in r:
		grid[i[0]][i[1]] = 'r'
	for i in l:
		grid[i[0]][i[1]] = 'l'
	for i in walls:
		grid[i[0]][i[1]] = wall

run()
mark()
printGrid()
