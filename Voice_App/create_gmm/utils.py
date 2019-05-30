import numpy as np
import soundfile as sf
import librosa
import os
import glob
from sklearn import preprocessing
from scipy.io import wavfile


#Get the Tracks of a Single Speaker
def readOne(SpeakerID, PATH):
	CurrentDir = os.getcwd()
	TRACKS = []
	os.chdir(os.join('PATH', SpeakerID))
	for f in os.listdir:
		TRACKS.append(wavfile.read(f))
	os.chdir(CurrentDir)
	return TRACKS

#Feature Extraction for All the Files in a Given Directory

def Features(PATH, Audioformat, sampling_rate):

    currentDir = os.getcwd()
    os.chdir(PATH)
    FT = np.asarray(())
 
    for files in os.listdir():
        if files.endswith('.'+Audioformat):
            Audio = sf.read(files)
            Mfcc = librosa.feature.mfcc(Audio[0], sr=sampling_rate, n_mfcc=20).transpose()
            Mfcc_Normalized = preprocessing.scale(Mfcc)
            Delta = librosa.feature.delta(Mfcc_Normalized)
            Features = np.hstack((Mfcc_Normalized,Delta))
            FT = Features if FT.size==0 else np.vstack((FT,Features))            
    os.chdir(currentDir)
    return FT




