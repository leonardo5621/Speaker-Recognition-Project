import numpy as np
from scipy.io import wavfile
import argparse

def SilenceRemoval(Audio):
    sr,Signal=wavfile.read("AudioExample.wav")
    ##Frame Length
    fl=0.025
    #samples per frame
    spf=int(np.ceil(fl*sr))
    L=len(Signal)
    #number of frames
    nf=int(np.ceil(len(Signal)/spf))
    #Setting a silence threshold
    threshold=np.amax(Signal)*.003
    #length to be padded
    toPad=int((nf*spf)-L)
    padZeros=np.zeros(toPad)
    if Signal.shape==(L,1):
        SignalPadded=np.append(Signal,padZeros)
        SignalFrames=np.reshape(SignalPadded,(nf,spf))
        indexes=list()
        for i in range(0,nf):
            if np.amax(SignalFrames[i])> threshold:
            
                indexes.append(i)
    
        AudioWout=SignalFrames[indexes,:]

        AudioReconst=np.ravel(AudioWout)
        AudioReconst=np.asarray(AudioReconst,dtype='int16')
        return AudioReconst
    elif Signal.shape==(L,2):
        SignalPadded=np.append(Signal[:,0],padZeros)
        SignalFrames=np.reshape(SignalPadded,(nf,spf))
        indexes=list()
        for i in range(0,nf):
            if np.amax(SignalFrames[i])> threshold:
            
                indexes.append(i)
    
        AudioOut1=SignalFrames[indexes,:]
        AudioOut1.shape[0]*AudioOut1.shape[1]
        AudioOut1=np.reshape(AudioOut1,(int(AudioOut1.size),1))
        AudioChan1=np.asarray(AudioOut1,dtype='int16')
        SignalPaddedChan2=np.append(Signal[:,1],padZeros)
        SignalFramesChan2=np.reshape(SignalPaddedChan2,(nf,spf))
        AudioOut2=SignalFramesChan2[indexes,:]
        AudioOut2=np.reshape(AudioOut2,(int(AudioOut2.size),1))
        AudioChan2=np.asarray(AudioOut2,dtype='int16')
        AudioReconst=np.concatenate((AudioChan1,AudioChan2),axis=1)
        return AudioReconst

def get_Arguments():

    parser=argparse.ArgumentParser(description='Remove the Silence Parts from an Audio File')
    parser.add_argument('AudioFile',help='Name of the File to be processed')
    parser.add_argument('-fform','--fileformat',help='Format of the File(default=wav)',action='store_const',default='wav')
    
    return parser.parse_args()

def Main():

    Args=get_Arguments()
    AudioProcessed=SilenceRemoval(Args.AudioFile)
    wavfile.write('NewFile.wav',44100,AudioProcessed)

if __name__=='__main__':
    Main()
    
