import numpy as np
import python_speech_features as psf
import os
from scipy.io import wavfile

def Features(PATH):

    PathTraining=PATH+"/Training"

    os.chdir(PathTraining)

    FT=np.zeros((1,13))

    for file in os.listdir():
        Audio=wavfile.read(file)
        
        Mfcc=psf.mfcc(Audio[1])

        FT=np.concatenate((FT,Mfcc))

    os.chdir("..")
    os.chdir("..")

    
    return FT
