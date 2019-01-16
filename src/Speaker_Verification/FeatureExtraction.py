import python_speech_features as psf
import numpy as np
from os.path import join
from os import listdir,chdir
from scipy.io import wavfile
import python_speech_features as psf 

#Get the Tracks of a Single Speaker
def readOne(SpeakerID,PATH):
	CurrentDir=os.getcwd()
	TRACKS=[]
	chdir(join('PATH',SpeakerID))
	for f in listdir:
		TRACKS.append(wavfile.read(f))
	chdir(CurrentDir)
	return TRACKS

#Feature Extraction for All the Files in a Given Directory

def Features(PATH):
    chdir(PATH)
    FT=np.zeros((1,13))
    for files in listdir():
        if files.endswith('.wav'):
            Audio=wavfile.read(files)
            Mfcc=psf.mfcc(Audio[1])
            FT=np.concatenate((FT,Mfcc))

    return FT
