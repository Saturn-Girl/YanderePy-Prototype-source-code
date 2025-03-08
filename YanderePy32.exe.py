#YanderePy source code python
from ursina import*
import os
import time
import logging
import sys
import json

app = Ursina() #Kill me

Sky()
ground = Entity(model='plane', scale=(10, 1, 10), texture='grass')
music = Audio('Finale undertale x Reeses puffs remix [6acm9LqdgzY].wav', loop=True, autoplay=True)
player = Entity(model='Yandere-Chan(Player - YanderePy.exe).obj')
camera.parent = player
camera.position = (0, 5, -20)
camera.rotation_x = 30
print("tip: press alt + f4 or use task maneger to close")
x = 5
y = 5
var = x + y

if var == 10:
    print(var)
else:
    print(f"x value (eg{x}) and y value {y} did not get the reult as 10")
    
def update():
        
    player.x += held_keys['d'] * time.dt * 5
    player.x -= held_keys['a'] * time.dt * 5
    player.z += held_keys['w'] * time.dt * 5
    player.z -= held_keys['s'] * time.dt * 5
if os.path.exists("YanderePy.exe prototype_data"):
    logging.info("info:Found the YanderePy.exe prototype_data folder.")
    print("info:Found the YanderePy.exe prototype_data folder.")
else:
    logging.error("info.error: There should be a YanderePy.exe prototype_data folder.")
    print("info.error: There should be a YanderePy.exe prototype_data folder.")
    time.sleep(5)
    sys.exit()
A = True
class Start:
    def file(self):
        #data
        if os.path.exists("YanderePy.exe prototype_data/UrsinaBleedingEdge"):
            print("LN")
        else:
            sys.exit()
        if os.path.exists("Save1.json"):
            with open('Save1.json', 'r') as file:
                data = json.load(file)
                print("Save file found")
        else:
            print("Info: Save data not found no data or object")
class Data:
    if os.path.exists("CharacterData.json"):
        with open('CharacterData.json', 'r') as file:
            data = json.load(file)
            print("Save file found")
    else:
        print("Info: Save data not found no data or object")
    if os.path.exists("CharacterData.json"):
        with open('CharacterData.json', 'r') as file:
            data = json.load(file)
            print("Save file found")
    else:
        print("Info: Save data not found no data or object")
    if os.path.exists("CharacterData.json"):
        with open('CharacterData.json', 'r') as file:
            data = json.load(file)
            print("Save file found")
    else:
        print("Info: Save data not found no data or object")
        
class System:

    def Run(self):
        KillCount = 0

        if KillCount == 3:
            TrueEnding = "Genocide"
            if TrueEnding == "Genocide":
                if os.path.exists(__file__):
                    os.remove(__file__)
                else:
                    os.startfile("Kill.bat")
        if KillCount == 1:
            TrueEndingA = "Normal"
            if TrueEndingA == "Normal":
                print("remember you cannot escape YanderePy.exe")
                A = True
                while A:
                    os.startfile("Error.vbs")
        if KillCount == 3:
            print("You killed everyone now the game will delete itself using batch file")
            TrueEnding = "Genocide"
            if TrueEnding == "Genocide":
                if os.path.exists(__file__):
                    os.remove(__file__)
                else:
                    os.startfile("Kill.bat")
        

class data:
    def Model(self):
        var = 10
        dat = int(5) + (var)
        """
        This find the model
        """
        if var == 15:
            print(var)

if __name__ == "__main__":
    data = data()
    data.Model()
model_entity = Entity(
    model='YanderePy.exe prototype_data/School.obj',
    scale=1,
    position=(0, 0, 0),
    rotation=(0, 0, 0)
)

light = DirectionalLight()
light.look_at(Vec3(1, -1, -1))

ground = Entity(
    model='plane',
    color=color.gray,
    scale=(10, 10),
    position=(0, -1, 0)
)

EditorCamera()
app.run()
