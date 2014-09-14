# this file contains the representation of the sound information
# including how the 'DNA' will be merged and produce new members

import numpy as np
import random

class SoundDna:
    
    # a small number representing the rate of mutation
    self.mutationRate = 1/100
    
    def __init__(self, time, samplingRate, genes=None):
        # TODO: figure out what parameters to add to init
        
        # populate the gene array with initial conditions if genes weren't 
        # provided already
        # name parameters and initialize them
        # genes will be a list containing a dictionary of all the parameters for each individual
        # gene, i.e. amplitude, start time, stop time, function used, frequency
        # each will be acessible by an index number

        # sampling rate of the song
        self.samplingRate = samplingRate
        # specifies the time that passes between each data point
        self.dt = 1/self.samplingRate
        
        # the amount of datapoints needed to give the correct sampling rate
        self.datapoints = time / self.dt
        
        self.time = time
        
        # contains the property for how many genes are present in the DNA
        self.geneCount = 0
        # amplitude of the sound at any given time
        self.maxAmplitude = 500000
    
        # bounds of the frequency ranges
        self.minFrequency = 10
        self.maxFrequency = 20000
        # functions that can be used to calculate a sound
        
        self.fitness = 0        
        
        self.functions = [np.sin, np.cos]
        if not genes:
            self.geneCount = 1
            # populate gene array with random gene
            self.genes = [self.generateRandomGene() for x in range(self.geneCount)]
        else:
            self.genes = genes
            self.geneCount = len(self.genes)

    def generateRandomGene(self):
        amplitude = random.randint(1, self.maxAmplitude)
        frequency = random.randint(self.minFrequency, self.maxFrequency)
        function = random.choice(self.functions)
        return {'amp': amplitude, 'freq': frequency, 'func': function}

    def Recombine(self, dna):
        #TODO: handle times where the incoming dna is not the same length
        return # return a recombined set of dna

    def Mutate(self):
        # TODO define a list of possible mutations that could happen
        
        # trying to stick to the functional programming paradigm
        # by always returning things from functions
        return #mutated dna
        
    def willMutate(self):
        '''Returns true or false'''
        return random.Random() < self.mutationRate

    def getDna(self):
        # TODO: figure the return format
        # return dna in a list format to be applied successively
        return
        
    def getFitness(self):
        ''' returns the fitness if calculated, otherwise defaults to 0'''
        return self.fitness

    def CalculateFitness(self, reference):
        '''Calculates the fitness of the current organism based on the
        waveform of the reference. The reference should be a numpy array. Fitness is
        calculated by first normalizing the input sound by the max amplitude
        and dividing the waveform by that number. Then the average distance 
        between the waveforms across all frequencies will be calculated.'''
        
        #TODO figure out how to calculate the fitness

        return True
        
    def produceSoundWaveform(self):
        ''' applies the periodic functions to the time period to produce
        a sound that will be used to calculate the fitness of the sound
        or output to a file. Returns a numpy array.'''
        
        timeDatapoints = np.arange(0, self.time, self.dt)
        tempOutput = None
        output = None
        for gene in self.genes:
            # calculate the current function using the time
            tempOutput = gene['amp'] *gene['func'](
                timeDatapoints * gene['freq'] * np.pi * 2)
                
            # if the output array exists, add the outputs, otherwise create
            # the array
            if output:
                output += tempOutput
            else:
                output = tempOutput
                
        return output
            
            
