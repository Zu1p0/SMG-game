# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:49:07 2021

@author: anton
"""

import random
import time


# Find number of surrounding cells
def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1

	return s_cells


## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
start = "s"
end = "e"
height = 15
width = 15
maze = []


for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1

maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

maze[starting_height-1][starting_width] = 'w'
maze[starting_height][starting_width - 1] = 'w'
maze[starting_height][starting_width + 1] = 'w'
maze[starting_height + 1][starting_width] = 'w'

while (walls):
	rand_wall = walls[int(random.random()*len(walls))-1]

	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'u'):
			maze[i][j] = 'w'

for i in range(0, width):
	if (maze[1][i] == 'c'):
		maze[0][i] = 's'
		break

for i in range(width-1, 0, -1):
	if (maze[height-2][i] == 'c'):
		maze[height-1][i] = 'e'
		break
    
# print(maze)
