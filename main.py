#!/usr/bin/env python3

# Winthrop Gillis 9/1/2014
# Music genetic algorithms
# Goal of the project: To be able to evolve a sound through 
# genetic algorithms given a sound to be used to calculate fitness
# 
# the fitness function will be the variance between the difference
# of the waveforms from the example and the evolved sound

# Program will be a command line interface

# a folder will be located in the program project folder
# that the user must put all input songs in before referencing
# in program
# this main file will handle all the abstracted stuff, and will be the 
# handler for general functionality, like the evolution steps


##################################################
# Import statements
##################################################

# argparse is used for command line interfacing
import argparse 
import time, os, sys





##################################################
# Global variables
##################################################
outputFolder = 'outputSound'
inputFolder = 'inputMusic'
if sys.platform == 'linux':
    outputFolder = '/media/odroid/UNTITLED/outputSound'

##################################################

parser = argparse.ArgumentParser(
    description='Creates a sound from a genetic algorithm using a reference')
# argument for the filename
parser.add_argument('file', help='the input file for sound reference (.mp3 or .wav)')
# argument for the time span in the file
parser.add_argument('-t', help='time span that the sound spans in music file')
# optional argument for the number of generations for evolution
parser.add_argument('-g', type=int, help='[OPTIONAL] amount of generations to evolve. Default is 1000.', default=1000)
# optional argument for the population size
parser.add_argument('-p', type=int, default=500, help='[OPTIONAL] the population size of sound producers. Default is 500')


args = parser.parse_args()

# How you access the vars in args
# print(args.g)
# print(args.file)
# print(args.t)
# print(args.p)

def main():
    '''This is the main function, where everything will be handled'''
    generations = args.g

    populationSize = args.p

    # array for holding the population
    population = []

    for generation in range(generations):
        print('Processing generation {0}'.format(generation))
        print('Populating...')
        # TODO: fill array with DNA containing creatures
        tempGeneration = []

# run the program!!
if __name__=='__main__':
    main()

