import python_speech_features as psf
import numpy as np
import re
from os import listdir
from scipy.io import wavfile

def readOne(SPEAKER,PATH):

    FILES=[re.search(SPEAKER+'[\w]+.wav',file) for file in listdir(PATH)]
    readThose=[]
    TRACKS=[]
    AUDIO=[]
    for f in FILES:

        if f!=None:

            readThose.append(f.group())



    TRACKS=[wavfile.read(PATH+'/'+SPK) for SPK in readThose]

     

    return TRACKS


def getFT(TRACKS):

    MFCC=[]

    MFCC=[psf.mfcc(TRACKS[i][1],TRACKS[i][0]) for i in range(len(TRACKS))]

    F=np.zeros((1,13))

    for L in range(len(MFCC)):
        
        F=np.concatenate((F,MFCC[L]))
    

    return F

def getAll(SPEAKERS,PATH):

    AllFT=[]
    
    Audio=[RS(Spk,PATH) for Spk in SPEAKERS]

    AllFT=[getFT(Aud) for Aud in Audio]

    return AllFT
