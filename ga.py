from random import choice, random, randint
import numpy as np


class GA:
    def __init__(self,  fitfn, alleles, pop_size=1024, size=8, cp = 0.8, mp = 0.03):
        self.size = size
        self.alleles = alleles
        self.fitfn = fitfn
        self.cp = cp
        self.mp = mp
        self.population = [self.gen_random_chromosome() for i in range(pop_size)]

    
    def crossover(self, c1, c2):
        pivot = randint(0, len(c1) - 1)
        gene1 = c1[:pivot] + c2[pivot:]
        gene2 = c2[:pivot] + c1[pivot:]

        return gene1, gene2

    def mutate(self, c):
        gene = c
        index = randint(0, len(gene) - 1)
        newgene = choice(self.alleles)
        while(gene[index] == newgene):
            newgene = choice(self.alleles)
        gene[index] = newgene

        return gene
    
    def selection(self):
        c1 = choice(self.population)
        c2 = choice(self.population)
        if (self.fitfn(c2) < self.fitfn(c1)): 
            c1 = c2
        return c1

    def evolve(self):
        pop_size = len(self.population)
        index = int(round(pop_size * 0.1))
        buffer = self.population[:index]

        while(index < pop_size):
            if random() <= self.cp:
                (p1, p2) = (self.selection(), self.selection())
                children = self.crossover(p1, p2)
                for c in children:
                    if random() <= self.mp:
                        buffer.append(self.mutate(c))
                    else:
                        buffer.append(c)
                index += 2
            else:
                c = self.population[index]
                if random() <= self.mp:
                    buffer.append(self.mutate(c))
                else:
                    buffer.append(c)
                index += 1
        self.population = buffer[:pop_size]
    
    def gen_random_chromosome(self):
        gene = [choice(self.alleles) for x in range(self.size)]
        return gene



