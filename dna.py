# this file contains the representation of the sound information
# including how the 'DNA' will be merged and produce new members

import numpy as np
import scipy as sp
import random

class SoundDna:
class SoundDna:
    
    # name parameters and initialize them
    # genes will be a list containing a dictionary of all the parameters for each individual
    # gene, i.e. amplitude, start time, stop time, function used, frequency
    # each will be acessible by an index number
    self.genes = []

    # contains the property for how many genes are present in the DNA
    self.geneCount = 0
    # amplitude of the sound at any given time
    self.maxAmplitude = 500000

    # bounds of the frequency ranges
    self.minFrequency = 10
    self.maxFrequency = 20000
    # functions that can be used to calculate a sound
    self.functions = [np.sin, np.cos]
    def __init__(self, genes=None):
        # TODO: figure out what parameters to add to init
        
        # populate the gene array with initial conditions if genes weren't 
        # provided already
        if not genes:
            self.geneCount = 1
            # TODO: populate array
            self.genes = []
        else:
            self.genes = genes

    def generateRandomGene(self):
        amplitude = random.randint(1, self.maxAmplitude)
        frequency = random.randint(self.minFrequency, self.maxFrequency)
        function = random.choice(self.functions)
        return {'amp': amplitude, 'freq': frequency, 'func': fucntion}

    def Recombine(self, dna):
        #TODO: handle times where the incoming dna is not the same length
        return # return a recombined set of dna

    def Mutate(self):
        
        # trying to stick to the functional programming paradigm
        # by always returning things from functions
        return #mutated dna

    def getDna(self):

        # return dna in a list format to be applied successively
        return

    def CalculateFitness(self, reference):
        '''Calculates the fitness of the current organism based on the
        waveform of the reference (also a SoundDna object). Fitness is
        calculated by first normalizing the input sound and dividing the
        waveform by that number. Then the average distance between the waveforms
        across all frequencies will be calculated.'''

        return
