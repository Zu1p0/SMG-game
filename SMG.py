# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:43:54 2021

@author: anton

todo:
    entrance green exit red
    test that we do not appear in a block
    stop program when fall down a lot (looking at maze from below)
    use health bar to set max time to find exit (-1 per second)
"""

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
import maze_generator as gen

app = Ursina()
window.fullscreen = True

def update():
#   health.value -= 0.01
    pass

class Block(Button):
    
    def __init__(self, position=(0,0,0), coloring = color.color(0, 0, random.uniform(.9, 1.0))):
        
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            texture = "white_cube",
            color = coloring,
            origin_y = .5
                        )
    def input(self, key):
        pass
        
for i in range(0, gen.height):
    for j in range(0, gen.width):
        
        if (gen.maze[i][j] == 'u'):
            raise Exception("Generator problem")
            
        elif (gen.maze[i][j] == 'c'):
            Block(position = (i,0,j))
        
        elif gen.maze[i][j] == 's' :
            Block(position = (i,0,j))
            startpoint = (i,0,j)
            
        elif gen.maze[i][j] == 'e' :
            Block(position = (i,0,j))
        
        else:
            for y in range(4):
                Block(position = (i,y,j))

player = FirstPersonController(z = startpoint[2])
# health = HealthBar()
msc = Audio("backgroundmusic.wav", autoplay = True)
msc.play()

app.run()