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

# argparse is used to add arguments to the program

##################################################
# Import statements
##################################################
import argparse, time, os





##################################################
# Global variables
##################################################
outputFolder = 'outputSound'
inputFolder = 'inputMusic'

##################################################

parser = argparse.ArgumentParser(
    description='Creates a sound from a genetic algorithm using a reference')

parser.add_argument('file', help='the input file for sound reference (.mp3 or .wav)')
parser.add_argument('-t', help='time span that the sound spans in music file')

args = parser.parse_args()

# This is how you get the data from args
# print(args.file)
# print(args.t)

