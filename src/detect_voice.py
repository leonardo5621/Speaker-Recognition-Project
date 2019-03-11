import numpy as np
import scipy 
import soundfile as sf

def Framing(Signal,srate,FrameSpan=0.01):
    FrameLen=int(srate*FrameSpan)
    SLen=len(Signal)
    NFrames=int(np.ceil(SLen/FrameLen))
    padLen=int(np.abs(NFrames*FrameLen-SLen))
    SignalToReshape=np.append(Signal,np.zeros(padLen))
    FramedSignal=np.reshape(SignalToReshape,(NFrames,FrameLen))
    
    return FramedSignal,NFrames,FrameLen

def is_speech(signal,srate):
    Threshold=0.12
    Energies=[]
    maxfrq=5000
    L=len(signal)
    Frames,N,length=Framing(signal,srate)
    sig_in_frequency=scipy.fft(Frames)
    abs_in_frequency=np.abs(sig_in_frequency)
    for j in range(N):
        Power=np.power(abs_in_frequency[j,:],2)/length
        truncate=int(maxfrq*length/srate)
        Power_in_Speech=Power[:truncate]
        Energy=np.sum(Power_in_Speech)/(2*np.pi)
        Energies.append(Energy)
    
    Mean=np.mean(Energies)
    
    if Mean < Threshold:
        
        return False
    
    else:
        
        return True