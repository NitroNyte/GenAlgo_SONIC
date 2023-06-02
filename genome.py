# import numpy as np
from dataclasses import dataclass

@dataclass
class genome:
    seq = []
    fitness: int = 0
    
    # def fillActionArr(act):
    #     actionDict = {
    #     'B':0,
    #     'A':1,
    #     'UP':4,
    #     'DOWN':5,
    #     'LEFT':6,
    #     'RIGHT':7,
    #     }
    #     a = [0,0,0,0,0,0,0,0,0,0,0,0]
    #     a[actionDict[act]] = 1
    #     return a