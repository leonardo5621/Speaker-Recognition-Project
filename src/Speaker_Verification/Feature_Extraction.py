import python_speech_features as psf
import numpy as np
from os.path import join
from os import listdir,chdir,getcwd
from scipy.io import wavfile
import python_speech_features as psf
import soundfile as sf
import librosa
from sklearn import preprocessing

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
    FT=np.asarray(())
    #DEFAULT PARAMETERS
    datatype='float64'
    ch=1
    sr=44100
    for files in listdir():
        if files.endswith('.'+Aformat):
            Audio=sf.read(files)
            dataType=Audio[0].dtype
            ch=len(Audio[0].shape)
            sr=Audio[1]
            Mfcc=librosa.feature.mfcc(Audio[0],sr=Audio[1],n_mfcc=20).transpose()
            Mfcc_Normalized=preprocessing.scale(Mfcc)
            Delta=librosa.feature.delta(Mfcc_Normalized)
            Features=np.hstack((Mfcc_Normalized,Delta))
            FT=Features if FT.size==0 else np.vstack((FT,Features))            
    chdir(currentDir)
    return [FT,dataType,ch,sr]
