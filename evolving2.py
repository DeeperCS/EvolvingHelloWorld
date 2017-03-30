import random

source = "jiKnp4bqpmAbp"
target = "Hello, World!"

def fitness(source, target):
    fitval = 0
    for i in range(0, len(source)):
        fitval += (ord(target[i]) - ord(source[i])) ** 2
    return fitval

# Mutate and Crossover
def mutate(parent1, parent2):
    child_dna = parent1['dna'][:]
    
    # Mix both DNAs
    start = random.randint(0, len(parent2['dna'])-1)
    stop = random.randint(0, len(parent2['dna'])-1)
    if start > stop:
        stop, start = start, stop
    child_dna[start:stop] = parent2['dna'][start:stop]
    
    # Mutate one position
    charpos = random.randint(0, len(child_dna)-1)
    child_dna[charpos] = chr(ord(child_dna[charpos]) + random.randint(-1, 1) )
    child_fitness = fitness(child_dna, target)
    return ({'dna':child_dna, 'fitness':child_fitness})

def random_parent(genepool):
    # uniform product distribution
    wRndNr = random.random() * random.random() * (GENSIZE - 1)
    wRndNr = int(wRndNr)
    return (genepool[wRndNr])

# Generate initial population
GENSIZE = 20
genepool = []
for i in range(0, GENSIZE):
   dna = [random.choice(source) for j in range(0, len(target))]
   fitval = fitness(dna, target)
   candidate = {'dna': dna, 'fitness': fitval }
   genepool.append(candidate)

# Begin to evolve
i = 1
while True:
    # Elitism
    genepool.sort(key=lambda candidate:candidate['fitness'])
    if genepool[0]['fitness'] == 0:
        break
    parent1 = random_parent(genepool)
    parent2 = random_parent(genepool)
    
    child = mutate(parent1, parent2)
    print("i:{}, fitval:{}, {}".format(i, child['fitness'], ''.join(child['dna'])))
    i += 1
    if child['fitness'] < genepool[-1]['fitness']:
        genepool[-1] = child