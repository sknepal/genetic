
import datetime
import genetic
import random

geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
def test_Hello_World():
    target = "BlaBla"
    guess_password(target)
    
def guess_password(target):
    #geneset = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    startTime = datetime.datetime.now()
    
    def fnGetFitness(genes):
        return get_fitness(genes, target)

    def fnDisplay(candidate):
        display(candidate, startTime)
        
    optimalFitness = len(target)
    genetic.get_best(fnGetFitness, len(target), optimalFitness, geneset, fnDisplay)

def get_fitness(genes, target):
    return sum(1 for expected, actual in zip(target, genes)
              if expected == actual)

def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(''.join(candidate.Genes), candidate.Fitness, str(timeDiff)))
    
def test_Random(): 
    length = 150
    target = ''.join(random.choice(geneset) for _ in range(length)) 
    guess_password(target)

genetic.Benchmark.run(test_Hello_World)


