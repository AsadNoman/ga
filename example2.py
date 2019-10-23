#this example has all alphabets as alleles

from ga import GA
import time

#function to measure a DNA's fitness
#this function is passed to GA instance
allelestr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
target = 'ASAD'
def fitnessfunc(gene): #looks for max number of 1's
    #gene is list of 1s and 0s like [0, 1, 1, 0]
    fitness = 0
    for i in range(len(target)):
        fitness += abs(allelestr.index(target[i]) - allelestr.index(gene[i]))
    return fitness

maxgenerations = 50000
alleles = list(allelestr)
ga = GA(fitfn = fitnessfunc, alleles = alleles, pop_size=6, size=4, mp=0.05, cp=0.5)

for i in range(maxgenerations):
    strchr = [''.join([str(j) for j in i]) for i in ga.population] #array for population
    strfit = [fitnessfunc(i) for i in ga.population] #array for each DNA's corresponding fitness
    print(f'{strchr} | gen={i+1}', end='\r') #write on the same line
    #time.sleep(0.01)# wait 0.01sec before moving on
    
    if 0 in strfit: #if fittest found
        print(f'{strchr} | gen={i}\n fittest chromosome found.')
        break
    elif i == maxgenerations - 1: #if generation size has been exhausted
        print(f'gen{i+1} criteria exhuasted \n no fittest solution found.')
        break
    else: #move on if criteria is not met
        ga.evolve()