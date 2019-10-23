#this example has 0 and 1 as alleles

from ga import GA
import time

#function to measure a DNA's fitness
#this function is passed to GA instance
def fitnessfunc(gene): #looks for max number of 1's
    #gene is list of 1s and 0s like [0, 1, 1, 0]
    fitness = 0           
    x = int(''.join([str(i) for i in gene]), 2) #converting binary (base 2) to decimal (base 10)
    fitness= 15 - x #for DNA size 4, max binary in 4 bits is 15
    return fitness

maxgenerations = 2000
ga = GA(fitfn = fitnessfunc, alleles = [0,1], pop_size=6, size=4, mp=0.01, cp=0.1)

for i in range(maxgenerations):
    strchr = [''.join([str(j) for j in i]) for i in ga.population] #array for population
    strfit = [fitnessfunc(i) for i in ga.population] #array for each DNA's corresponding fitness
    print(f'{strchr} | gen={i+1}', end='\r') #write on the same line
    time.sleep(0.1)# wait 0.1sec before moving on
    
    if 0 in strfit: #if fittest found
        print(f'{strchr} | gen={i}\n fittest chromosome found.')
        break
    elif i == maxgenerations - 1: #if generation size has been exhausted
        print(f'gen{i+1} criteria exhuasted \n no fittest solution found.')
        break
    else: #move on if criteria is not met
        ga.evolve()