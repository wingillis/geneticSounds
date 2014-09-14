# this file deals with creating the waveform data to initially manipulate
# and handles all the timing information associated with finding out
# time lengths in imported files.
# This file also handles saving the sound waveforms to a file

# load modules

import mp3towav, os
import scipy.io.wavfile

#import numpy as np
class WaveformHandler():

    def loadFile(self, timing, fileName):
        ''' loads a file and returns a tuple of the sampling rate
        and the waveform numpy array.
        Timing is a tuple containing start and stop times.
        supports wav and mp3'''
        
        # there is no need to convert it to a wav because it already is
        if fileName.endswith('.wav'):
            output = scipy.io.wavfile.read(os.path.join('inputMusic', fileName))
        else:
            newPath = mp3towav.processMp3File(os.path.join('inputMusic', fileName), fileName, 'inputMusic')
            output = scipy.io.wavfile.read(newPath)
            
        #TODO load only the time specified by start and stop options
        # using the quality of the waveform in the audio

        return output

    def saveFile(self, outputName, rate, waveform):
        ''' Rate is in samples/sec. saves file to outputSound folder'''
        # this saves the file to the output destination
        # and returns true if it worked correctly
        
        scipy.io.wavfile.write(os.path.join('outputSound', outputName), rate, waveform.astype('i2'))        
        
        return True

    
