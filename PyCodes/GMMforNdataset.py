import numpy as np
from sklearn.mixture import GaussianMixture as GMM
from GetFeatures import Features
import features
import python_speech_features as psf
from scipy.io import wavfile
from os.path import join

def UBM(N_Components,Type):

    ubm=GMM(N_Components,Type)

    FTS=Features('UBM')

    ubm.fit(FTS)
    
    return ubm


U=UBM(256,'tied')

def Verification(SPEAKER,Audio):

    if (isinstance(Audio,str) & isinstance(SPEAKER,str)):
    
        gmm=GMM(80,'tied')

        speakerAudio=features.readOne(SPEAKER,'train')

        speakerTrain=features.getFT(speakerAudio)

        gmm.fit(speakerTrain)

        TestTrack=wavfile.read('test'+'/'+SPEAKER+'/'+Audio)

        MFCC=psf.mfcc(TestTrack[1],TestTrack[0])

        P1=gmm.score(MFCC)
        P2=U.score(MFCC)

        Theta=P1-P2

        if Theta>0:
            print('Acesso Permitido')
            allow=1
        else:
            print('Acesso Negado')
            allow=0
    else:

        print('Parametro Incorreto')
        allow=10

    return allow
