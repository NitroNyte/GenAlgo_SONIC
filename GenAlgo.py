from __future__ import annotations
import retro
import random
from genome import genome



# Define the population size
population_size = 100
 # Calculate the number of top genomes (20% of the population)
num_top_genomes = int(population_size * 0.2) 

# Define the number of generations
crossover_rate = 0.5
mutation_rate = 0.01
#target_fitness = 100000
fitness_list = []
#Using the power of probability we use this as a way to get a "higher" jump
longJump = ['B', 'B', 'B', 'B', 'B']
#Really helpfull for the fuctions that Sonic is going to use
actionDict = {
    'B':0,
    'A':1,
    'UP':4,
    'DOWN':5,
    'LEFT':6,
    'RIGHT':7,
}


def intToAction(s: str) -> list[int]:
    l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    l[actionDict[s]] = 1
    return l
#Since the actions are defined as right and jump, create a probability we Sonic doesn't just jump everytime
def probForAction() -> str:
    r = random.random()
    s: str = ""
    if r < .035:
        s = 'B'
    else:
        s = 'RIGHT'
    return s
#Generate the random genome
def generate_random_genome() -> genome:
    gen = genome()
    # Define the length of the genome
    genome_length = 2000
    l: list[str] = []

    # Generate a random binary genome
    for _ in range(genome_length):
        p = probForAction()
        if p == 'B':
            [l.append(j) for j in longJump]
            # for j in longJump:
            #     gen.seq.append(j)
        else:
            l.append(p)
        if len(l) >= genome_length:
            break
    gen.seq = l
    return gen
#Generates a random genome based on genome.py which is a dataclass
def generate_population() -> list[genome]:
    population: list[genome] = []
    for _ in range(population_size):
        # Generate a random genome for each individual
        gen = generate_random_genome()
        # #print(gen.seq[:15])
        # #individual = genome()
        # #Create an individual with the genome
        # #[individual.seq.append(i) for i in gen.seq]
        # #Add the individual to the population
        population.append(gen)
    return population

# Parents - population[:num_top_genes]
# Put the return at the beginning of the new population list
# Perform the crossover operation
def crossover(parents) -> list[genome]:
    offsprings: list[genome] = []

    num_parents: int = len(parents)
    num_pairs: int = num_parents // 2  # Number of parent pairs

    for i in range(num_pairs):
        parent1: genome = parents[i * 2]
        parent2: genome = parents[i * 2 + 1]

        crossover_point: int = random.randint(1, len(parent1.seq) - 1)  # Select a random crossover point

        child1 = genome()
        #child2 = genome()

        child1.seq = parent1.seq[:crossover_point] + parent2.seq[crossover_point:]  # Perform crossover for child 1
        #child2.seq = parent2.seq[:crossover_point] + parent1.seq[crossover_point:]  # Perform crossover for child 2

        offsprings.append(child1)
        #offsprings.append(child2)

    return offsprings


    # Mutation operator
def mutate(genome: genome):
    # Perform mutation for each gene
    if random.random() < mutation_rate:
        idx = random.randint(0, len(genome))
        genome.seq[idx] = random.choice(list(actionDict.keys()))
        genome.fitness = 0

def select_top_genomes(population: list[genome]) -> list[genome]:
    top_genomes: list[genome] = population[:num_top_genomes]  # Select the top genomes

    new_population = top_genomes
    for _ in range(num_top_genomes, len(population)):
        genome = generate_random_genome()
        new_population.append(genome)

    return new_population

def sort_population(population: list[genome]):
    population.sort(key=lambda x: x.fitness, reverse=True)
    