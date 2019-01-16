import numpy as np
import pandas as pd
import os
import Training-Verification as GND

Path=input('Insert the directory containing the list of speakers')

SpeakersList=os.listdir(Path)

print(SpeakersList)

if 'TestsData.csv' not in os.listdir():
    nRows=len(SpeakersList)
    TestInfo=['Number of False Rejection Tests','Number of False Acceptance Tests','False Acceptance Rate','False Rejection Rate']
    nCols=len(TestInfo)
    TestData=pd.DataFrame(np.zeros((nRows,nCols)),index=SpeakersList, columns=TestInfo)
    
    print('DataFrame Created')

else:
    
    TestData=pd.read_csv('TestsData.csv')


def TestAccept(SPEAKER):
    
    TestCounter=0
    Result=0
    if os.path.exists(Path+'/'+SPEAKER) and os.path.isdir(Path+'/'+SPEAKER):
        for Audio in os.listdir(Path+'/'+SPEAKER):
            if Audio.endswith('.wav'):
                TestCounter+=1
                Audio=Path+'/'+SPEAKER+'/'+Audio
                Result+=GND.Verification(SPEAKER,Audio,ReturnTheta='n')
        if TestCounter==0:
            print('There is no audio file in this directory')
        else:
            TestData.loc[SPEAKER]['Number of False Rejection Tests']=TestCounter
            TestData.loc[SPEAKER]['False Rejection Rate']= 1 - Result/TestCounter
    else:
        print('Directory does not exist')
    TestData.to_csv('TestsData.csv')
    
def RejectionTest(SPEAKER):

    TestCounter=0
    Result=0
    if not os.listdir(Path):
        print('There is no data for the Verification')
    else:
        ListSpeakers=os.listdir(Path)
        ListSpeakers.remove(SPEAKER)
        for Impostor in ListSpeakers:
            if os.path.isdir(Path+'/'+Impostor):
                for Audio in os.listdir(Path+'/'+Impostor):
                    if Audio.endswith('.wav'):
                        TestCounter+=1
                        Audio=Path+'/'+Impostor+'/'+Audio
                        Result+=GND.Verification(SPEAKER,Audio,ReturnTheta='n')
        TestData.loc[SPEAKER]['Number of False Acceptance Tests']=TestCounter
        TestData.loc[SPEAKER]['False Acceptance Rate']= Result/TestCounter
        TestData.to_csv('TestsData.csv')
    
