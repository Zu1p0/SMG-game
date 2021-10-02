# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:43:54 2021

@author: anton

"""

from ursina import *
import ursina.main as main
import maze_generator 
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from time import time, sleep


app = Ursina()
window.fullscreen = False


class Data:
    player = None
    level = 10
    blocklist = []
    opti = True
    label = None
    
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


def create_square(i,y,j, opti = False, color=color.white):
    global data
    if data.opti == False:
        i = i*2
        j = j*2
        data.blocklist.append(Block(position = (i,y,j), coloring=color))
        data.blocklist.append(Block(position = (i+1,y,j), coloring=color))
        data.blocklist.append(Block(position = (i,y,j+1), coloring=color))
        data.blocklist.append(Block(position = (i+1,y,j+1), coloring=color))
    else :
        data.blocklist.append(Block(position = (i,y,j), coloring=color))

def start_game():
    global data
    window.color = color.dark_gray

    if data.player != None:
        data.player.ignore = True
        data.player.ignore_input = True

    gen = maze_generator.Maze(height = round(data.level), width = round(data.level))
    
    for block in data.blocklist : destroy(block)

    for i in range(0, gen.height):
        for j in range(0, gen.width):
            
            if (gen.maze[i][j] == 'u'):
                raise Exception("Generator problem")
                
            elif (gen.maze[i][j] == 'c'):
                create_square(i,0, j, opti = data.opti)
            
            elif gen.maze[i][j] == 's' :
                create_square(i,0, j, opti = data.opti, color = color.green)
                if data.opti == False : startpoint = (i*2,0,j*2)
                else : startpoint = (i,0,j)
                
            elif gen.maze[i][j] == 'e' :
                create_square(i,0, j, opti = data.opti, color = color.blue)
                if data.opti == False : endpoint = (i*2,0,j*2)
                else : endpoint = (i,0,j)
                
            else:
                for y in range(4):
                    create_square(i,y, j, opti = data.opti)

    if data.player != None :
        data.player.reboot(startpoint=startpoint, endpoint = endpoint)
    else:
        data.player = Player(startpoint=startpoint, endpoint = endpoint)
        data.player.mouse_sensitivity = (30,30)
    sky = Sky()
    data.player.ignore = False
    data.player.ignore_input = False


def start_screen():
    window.color = color.dark_gray
    title = Entity(parent = camera.ui,
            position = (0,0.14,0),
            model = "quad",
            texture = "logo.png")
    title.scale = 1.2
    title.scale_y = 0.7
    
    class KeyClick(Button):
        def __init__(self):
            super().__init__(parent = camera.ui, position = (0,-0.2,0), text = "", icon = "start.png")
            self.scale = 0.3
            self.scale_y = 0.14
            self.scale_x = 1
            self.color = color.rgb(255,255,255, a=0)
            self.highlight_color = self.color
            self.pressed_color = self.color
            self.it = 0
        def update(self):
            if held_keys["enter"] :
                start_game()
                destroy(self)
                destroy(title)
                data.label = LevelLabel()
            
            self.it += 2 * main.time.dt
            if self.visible == False: 
                if self.it > 1 : 
                    self.visible = True
                    self.it = 0
            else : 
                if self.it > 2 : 
                    self.visible = False
                    self.it = 0
            
            print(self.it)
        
    click = KeyClick()
    

class Player(FirstPersonController):
    def __init__(self, startpoint, endpoint):
        super().__init__(z = startpoint[2])
        self.startpoint = startpoint
        self.endpoint = endpoint
    def restart(self):
        self.x = self.startpoint[0]
        self.z = self.startpoint[2]
    def reboot(self, startpoint, endpoint):
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.x = self.startpoint[0]
        self.z = self.startpoint[2]

class LevelLabel(Text):
    def __init__(self, **kwargs):
        super().__init__(master = camera.ui, **kwargs)
        self.size = 0.03
        self.color = color.black
        self.x = .5
        self.y = .4

    def update(self):
        global data
        self.text = "level: "+str(data.level)
        
def update():
    global player, level
    if data.player != None:
        data.label.update()
        if held_keys["r"]: data.player.restart()
        if round(data.player.x) == data.player.endpoint[0]: #and round(data.player.z) == data.player.endpoint[2]:
            if data.level <30 : data.level += 2
            if data.level == 30 : data.opti = True
            start_game()
    if held_keys["q"]: quit()

msc = Audio("backgroundmusic.mp3", loop = True)
msc.play()

start_screen()
data = Data()

app.run()
