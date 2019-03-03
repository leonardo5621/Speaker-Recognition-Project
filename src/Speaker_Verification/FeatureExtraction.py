import python_speech_features as psf
import numpy as np
from os.path import join
from os import listdir,chdir,getcwd
from scipy.io import wavfile
import python_speech_features as psf
import soundfile as sf

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

def Features(PATH,Aformat):
    currentDir=getcwd()
    chdir(PATH)
    FT=np.zeros((1,13))
    for files in listdir():
        if files.endswith('.'+Aformat):
            Audio=sf.read(files)
            if Audio[1]>20000:
                Mfcc=psf.mfcc(Audio[0],samplerate=Audio[1],winlen=0.01,winstep=0.004)
            else:
                Mfcc=psf.mfcc(Audio[0],samplerate=Audio[1],winlen=0.01,winstep=0.004)

            FT=np.concatenate((FT,Mfcc))
    chdir(currentDir)
    return FT
