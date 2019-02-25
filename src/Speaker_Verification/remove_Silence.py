import numpy as np
from scipy.io import wavfile
import argparse

def SilenceRemoval(AudioSignal,sr):
    dataType=AudioSignal.dtype
    Signal=AudioSignal
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
    #Checking the Channels
    if Signal.shape==(L,1):
        SignalPadded=np.append(Signal,padZeros)
        #Signal Framing for Detecting the Silent parts
        SignalFrames=np.reshape(SignalPadded,(nf,spf))
        indexes=list()
        #Finding the Silent Frames
        for i in range(0,nf):
            if np.amax(SignalFrames[i])> threshold:
            
                indexes.append(i)
    
        AudioWout=SignalFrames[indexes,:]
        #Reconstruction of the Signal
        AudioReconst=np.ravel(AudioWout)
        AudioReconst=np.asarray(AudioReconst,dtype=dataType)
        return AudioReconst
    elif Signal.shape==(L,2):
        #Processing for an audio with two channels
        SignalPadded=np.append(Signal[:,0],padZeros)
        #Framing
        SignalFrames=np.reshape(SignalPadded,(nf,spf))
        indexes=list()
        #Finding the Silent Parts
        for i in range(0,nf):
            if np.amax(SignalFrames[i])> threshold:
            
                indexes.append(i)
        #Reconstruction of the two channels
        AudioOut1=SignalFrames[indexes,:]
        AudioOut1.shape[0]*AudioOut1.shape[1]
        AudioOut1=np.reshape(AudioOut1,(int(AudioOut1.size),1))
        AudioChan1=np.asarray(AudioOut1,dtype=dataType)
        SignalPaddedChan2=np.append(Signal[:,1],padZeros)
        SignalFramesChan2=np.reshape(SignalPaddedChan2,(nf,spf))
        AudioOut2=SignalFramesChan2[indexes,:]
        AudioOut2=np.reshape(AudioOut2,(int(AudioOut2.size),1))
        AudioChan2=np.asarray(AudioOut2,dtype=dataType)
        AudioReconst=np.concatenate((AudioChan1,AudioChan2),axis=1)
        return AudioReconst

def get_Arguments():

    parser=argparse.ArgumentParser(description='Remove the Silence Parts from an Audio File')
    parser.add_argument('AudioFile',help='Name of the File to be processed')
    parser.add_argument('-fform','--fileformat',help='Format of the File(default=wav)',default='wav')
    
    return parser.parse_args()

def Main():

    Args=get_Arguments()
    sr,AudioData=wavfile.read(Args.AudioFile)
    AudioProcessed=SilenceRemoval(AudioData,sr)
    wavfile.write('NewFile.wav',sr,AudioProcessed)

if __name__=='__main__':
    Main()
    
