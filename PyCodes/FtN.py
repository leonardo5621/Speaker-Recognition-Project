import python_speech_features as psf
import numpy as np
import re
from os.path import join
from os import listdir,chdir
from scipy.io import wavfile
import python_speech_features as psf 

#Obter os dados de fala de um locutor
def readOne(SPEAKER,PATH):

    TRACKS=[]

    chdir(join('PATH','SPEAKER'))
    
    for f in listdir:

        TRACKS.append(wavfile.read(f))

    chdir('..')
    chdir('..')

    return TRACKS

#extrair as caracteristicas do sinal de voz

def Features(PATH):

    chdir(PATH)

    FT=np.zeros((1,13))

    for files in listdir():
        
        if files.endswith('.wav'):
        
            Audio=wavfile.read(files)
        
            Mfcc=psf.mfcc(Audio[1])

            FT=np.concatenate((FT,Mfcc))

    
    return FT

#extracao de uma lista de locutores

def getAll(SPEAKERS,PATH):

    AllFT=[]
    
    Audio=[RS(Spk,PATH) for Spk in SPEAKERS]

    AllFT=[getFT(Aud) for Aud in Audio]

    return AllFT
