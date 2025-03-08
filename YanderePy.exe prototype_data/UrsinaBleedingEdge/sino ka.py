import os
import sys
import time

Crush = input("sino crush mo ")
Gender = input("Anu gender mo ")
GenderCrush = input("Ano gender ng crush mo > ")

if GenderCrush == "male":
    if Gender == "male":
        print("Bakla ka")
        time.sleep(4)
        os.remove(__file__)
if GenderCrush == "female":
    if Gender == "male":
        print("Tang ina mo")
        time.sleep(2)
        sys.exit()

if GenderCrush == "male":
    if Gender == "female":
        print("101010101")
        time.sleep(4)
        sys.exit()
if GenderCrush == "female":
    if Gender == "female":
        print("Bakla ka")
        os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")
