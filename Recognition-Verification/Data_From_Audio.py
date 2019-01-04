import numpy as np
import pandas as pd
from scipy.io import wavfile
import os
## The Functions here may be used in order to get informations about the audio used
## AudioDuration computes total amount of audio data in seconds used to Train/Test the model
## AudioSize computes the total size of the data in megabytes(MB)
## All the data collected is stored in the file AudioData.csv


## Checks if the file AudioData.csv exists in the Directory

if 'AudioData.csv' not in os.listdir():
    
    AudioInfo=['Audio Duration-Train (Seconds)','Audio Size-Train (MB)','Audio Duration-Test (Seconds)','Audio Size-Test (MB)']
    indexes=['UniversalModel','Speaker1','Speaker2','Speaker3','Speaker4','Speaker5','Speaker6','Speaker7','Speaker8','Speaker9','Speaker10']
    AudioData=pd.DataFrame(np.zeros((11,4)),index=indexes,columns= AudioInfo)
else:
    
    AudioData=pd.read_csv('AudioData.csv')
    
    
def AudioDuration(Dir,SPK='UniversalModel',DataFor='Train'):
    CurrentDir=os.getcwd()

    ##Changing to the directory containing the audio data
    
    os.chdir(Dir)

    TotalDuration=0

    ## for loop for checking each file in the directory
    ## only the files with the extension .wav are opened
    
    for Audio in os.listdir():
        if Audio.endswith('.wav'):
            SampF,signal=wavfile.read(Audio)
            TotalDuration+=len(signal)/SampF

    Minutes=str(np.floor(TotalDuration/60))
    D=TotalDuration%60
    D='%.3f' %D
    ##Print the total length of the audio data
    print(Minutes+' Minutes of Audio and '+D+' Seconds for Training/Testing')

    os.chdir(CurrentDir)

    ##writing the data into the DataFrame
    AudioData.loc[SPK]['Audio Duration-'+DataFor+' (Seconds)']=TotalDuration
    AudioData.to_csv('AudioData.csv')

def AudioSize(PATH,DataFor='Train',SPK='SPEAKER1'):

    CurrentDir=os.getcwd()
    os.chdir(PATH)
    TotalSize=0
    for Audio in os.listdir():

        if Audio.endswith('.wav'):

            TotalSize+=os.path.getsize(Audio)

    print(str(TotalSize/(10**6))+'MB')
    os.chdir(CurrentDir)
    
    AudioData.loc[SPK]['Audio Size-'+DataFor+' (MB)']=TotalSize/(10**6)
        
    
    AudioData.to_csv('AudioData.csv')
