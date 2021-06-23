# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:43:54 2021

@author: anton

todo:
    stop program when fall down a lot (looking at maze from below)
    use health bar to set max time to find exit (-1 per second)
"""

from ursina import *
from time import time


app = Ursina()
window.fullscreen = True

playing = False


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
  

def start_game():
    import maze_generator as gen
    from ursina.prefabs.first_person_controller import FirstPersonController
    from ursina.prefabs.health_bar import HealthBar
    window.color = color.dark_gray 
    
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

def start_screen():
    window.color = color.dark_gray
    title = Entity(parent = camera.ui,
            position = (0,0.2,0),
            model = "quad",
            texture = "logo.png")
    title.scale = 1.2
    title.scale_y = 0.7
    
    class KeyClick(Button):
        def __init__(self):
            super().__init__(parent = camera.ui, position = (0,-0.2,0), text = "", icon = "keytostart.png")
            self.scale = 0.2
            self.scale_y = 0.1
            self.scale_x = 0.9
            self.color = color.rgb(255,255,255, a=0)
            self.highlight_color = self.color
            self.pressed_color = self.color
            self.it = 0
        def on_click(self): 
            start_game()
            destroy(self)
            destroy(title)
            playing = True
        def update(self):
            self.it += 1
            if self.it == 20:
                if self.visible == False: self.visible = True
                else : self.visible = False
                self.it = 0
        
    click = KeyClick()
    

def update():
    pass

msc = Audio("backgroundmusic.mp3", loop = True)
msc.play()

start_screen()

app.run()
