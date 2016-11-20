import datetime
import genetic

def test(length = 100):
    geneset = [0, 1]
    startTime = datetime.datetime.now()
    
    def fnDisplay(candidate):
        display(candidate, startTime)
        
    def fnGetFitness(genes):
        return get_fitness(genes)
        
    optimalFitness = length
    best = genetic.get_best(fnGetFitness, length, optimalFitness, geneset, fnDisplay)
    
def get_fitness(genes):
    return genes.count(1)
    
def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}...{1}\t{2:3.2f}\t{3}".format(''.join(map(str, candidate.Genes[:15])),
                    ''.join(map(str, candidate.Genes[:-15])),
                    candidate.Fitness,
                    str(timeDiff)))
                    
genetic.Benchmark.run(test)
genetic.Benchmark.run(lambda: test(1000))