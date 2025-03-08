#EntitiyDebug

import sys
import time
import os

Entity = "Dx0000f"
if Entity == "Dx0000f":
    print(Entity)
def Args():
    function = "Dim"
    if function == "Dim":
        Dim = 10

        Dim += 5
        print(Dim)
    Variable = "Var"
    if Variable == "Var":
        Var = 0
        Var += 10
        print(Var)
def Var():
    Dim = "Var"
    Dim()
def Dim():
    Var = "Dim"
"""Simple math function to use dim as an varaible like int and var as a float variable"""

def DimVar():
    Dim = 50
    Var = 3.2
    sum = float(Dim) + float(Var)
    print(sum)
    EntityDebug()
"""Debug the entity bu running compiled C++ code"""

def EntityDebug():
    if os.path.exists("Player.exe"):
        X = 5
        Y = 2
        time.sleep(2)
        data = int(X) + int(Y)
        print(data)
        os.startfile("Player.exe")
        Var()
    else:
        print("0")
    

if __name__ == "__main__":
    Args()
    DimVar()

time.sleep(2)
sys.exit()

