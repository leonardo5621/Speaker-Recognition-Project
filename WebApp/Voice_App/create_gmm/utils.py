import python_speech_features as psf
import numpy as np
import soundfile as sf
import librosa
import os
import glob
from sklearn import preprocessing
from scipy.io import wavfile
from pydub import AudioSegment

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




def ConvertWAV(audioPath,inpFormat,OneFile=True):
    "If the objective is to convert several files at once, audioPath should be the path"
    "to a directory, otherwise it should give the path directly to the file"

    currentDir=os.getcwd()
    if OneFile:
        audioDir,audioFile=os.path.split(audioPath)
        os.chdir(audioDir)
        print(audioDir)
        baseName=os.path.splitext(os.path.basename(audioPath))[0]
        newFileName=baseName+'.wav'
        AudioSegment.from_file(audioFile).export(newFileName,format='wav')
        os.chdir(currentDir)
        print('Conversion Done')
    else:
        try:
            ##List of the audio files
            audioList=glob.glob(audioPath+'*.'+inpFormat)
            ##Changing to the directory containing the audio files
            os.chdir(os.path.dirname(audioPath))
            for audioFile in audioList:
                ##Name of the Audio File
                bs=os.path.basename(audioFile)
                FileName=os.path.split(audioFile)[1]
                baseFileName=os.path.splitext(FileName)[0]
                ##Name of the New file
                newFileName=baseFileName+'.wav'
                AudioSegment.from_file(bs,format=inpFormat).export(newFileName,format='wav')
            os.chdir(currentDir)
        except FileNotFoundError:
            os.chdir(currentDir)
            print('File not Found')

def SilenceRemoval(AudioSignal,sr,threshold_only=False):
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
    #Option of only returning the voice thresold
    if threshold_only:
        return threshold
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
        return AudioReconst,

