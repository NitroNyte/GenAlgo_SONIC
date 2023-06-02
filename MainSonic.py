from __future__ import annotations
import sys
import retro
import GenAlgo
import cv2
import numpy as np
import random
from timeit import default_timer
from genome import genome
import keyboard

#Set the max number of generations here that it can iterate through
generation: int = 0
max_generation: int = 50
#Create the environment
env = retro.make('SonicTheHedgehog-Genesis', 'GreenHillZone.Act1')
env.reset()
#Create the action environment
action = env.action_space.sample()
inx, iny, inc = env.observation_space.shape
inx = int(inx/8)
iny = int(iny/8)
#Reset, rezise and set color included with shape in observation
ob = env.reset()
ob = cv2.resize(ob, (inx, iny))
ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY)
ob = np.reshape(ob, (inx, iny))

#Generate first population
population: list[genome] = GenAlgo.generate_population()

#Start the main loop depending on generations
for generation in range(max_generation):
    num: int = 1
    print("Current generation:", generation)
    #For every indvidual
    for individual in population:
        #Reset observation environment (Noctice the obsercation environment has no use in this algorithm but is olbigatory)
        ob = env.reset()
        frame = 0
        counter = 0
        xpos = 0
        xpos_max = 0
        # start = default_timer()
        done = False
        last_hearts = 3
        dead = False
        #For every sequence (On this code just think of it as an list of actions that can be performed) perform an action
        for act in individual.seq:
            env.render()
            action: list[int] = GenAlgo.intToAction(act)
            #env.render()
            #Decide on what to do on this taken action
            ob, rew, done, info = env.step(action)
            #Initialise the information about Sonic's position(xpos), Sonic's lives and end of the screen (xpos_end) 
            lives_Sonic = info['lives']
            xpos = info['x']
            xpos_end = info['screen_x_end']
            #Main criterion!
            #If the genome gets 100000 points "It's the chosen one..." (Yes, Star Wars meme intendet)
            if xpos == xpos_end and xpos_end > 500 :
                individual.fitness += 100000
                print("He is the chose one:", individual.seq)
                sys.exit()
    
                #Checks if Sonic dies he gets negative rewards
            if lives_Sonic == 0:
                individual.fitness -= 10000
                break
                #Support code for the upper part
            if lives_Sonic < last_hearts:
                individual.fitness -= 1000
                last_hearts = lives_Sonic
                break
            #If Sonic reaches new Height's add points
            if xpos > xpos_max:
                individual.fitness += 10
                xpos_max = xpos
                counter = 0
            # else:
            #     #Otherwise if Sonic moves to the left he gets negative points
            #     individual.fitness -= 30
            #     counter += 1
            #If the counter get's over 1000 start a new genome
            if counter > 1000:
                individual.fitness -= 1000
                break            
       
        print(str(individual))
    
    # The lower part is the complex operation's that require the GenAlgo.py for the incorporated methods

    # Sort population
    GenAlgo.sort_population(population)
    # Select best performing genomes (Some sort of "elitism")
    population = GenAlgo.select_top_genomes(population)
    # Create children for next generation, also perform crossover
    children: list[genome] = GenAlgo.crossover(population[:GenAlgo.num_top_genomes])
    # Add the children and population
    population = children + population[GenAlgo.num_top_genomes:]
    # Mutate
    GenAlgo.mutate(population)
    
    # Select top population
    
    # #children: list[genome] = GenAlgo.crossover(population[:GenAlgo.num_top_genomes])
    # #population = children + population[GenAlgo.num_top_genomes:]
    # Next Generation