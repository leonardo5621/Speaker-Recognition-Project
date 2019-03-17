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

def threshold_pass(signal,sr,parameter_signal,threshold=0.05,FrameLen=0.025):
    L=len(signal)
    coef_thresh=0.3
    Voice_limit=np.amax(parameter_signal)*threshold
    FS,NF,FL=Framing(signal,sr,FrameSpan=FrameLen)
    indexes=list()
        #Finding the Silent Frames
    for i in range(0,NF):
        if np.amax(FS[i])>Voice_limit:
            indexes.append(i)
    coefficient=len(indexes)/NF
    if coefficient>=coef_thresh:
        return True
    else:
        return False
    

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