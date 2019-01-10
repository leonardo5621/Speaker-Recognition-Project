import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import python_speech_features as psf
import pickle
from scipy.io import wavfile
import os
import FeatureExtraction as FtE
import pandas as pd

if 'Threshold.csv' in os.listdir():
    
    ThresholdList=pd.read_csv('Threshold.csv')
    
    print('DataFrame Loaded')
    
else:
    
    Inp=input('Do you want to create a new list for the Thresholds?(y/n)')
    
    if Inp=='y':
        
        Rows=len(os.listdir('Test'))
        
        ThresholdList=pd.DataFrame(np.zeros((Rows,1)),os.listdir('Test'),columns=['Threshold'])
        
        print('DataFrame Created')
        
        

def TrainModel(TrainDirectory,ModelName,N_Components=80,Type='tied'):
    
    """ Parameters of the Function
    
    :param TrainDirectory: Directory where is located all the Data for the Training of the new model
    :param ModelName: Name of the new model, usually it takes the ID of the Speaker
    :param N_Components: Number of Components in the Gaussian Mixture Model
    :param Type: type of the covariance matrix in the model
    
    """
            
	Model=GMM(N_Components,Type)
	dir=os.getcwd()        

	FTS=FtE.Features(TrainDirectory)

	Model.fit(FTS)
	
	os.chdir(TrainDirectory)
	File=open(ModelName,'wb')

	pickle.dump(Model,File)

	File.close() 

	os.chdir(dir)

if 'UBMFile' in os.listdir():

	UBM=open('UBMFile','rb')
	U = pickle.load(UBM)
	UBM.close()
else:
	ipt=input('Do you want to train a new Universal Background Model?(y/n) \n')
	if ipt=='y':
		TrainModel('Audio_Data/UBM','UBMFile')
		UBM=open('UBMFile','rb')
		U = pickle.load(UBM)
		UBM.close()

def Verification(SPEAKER,Audio,ReturnTheta='n'):
    
    """ Parameters of the Function
    
    :param SPEAKER: Speaker ID Claimed for the Verification
    :param Audio: Audio File inserted to perform the Verification
    :param ReturnTheta: Decides whether or not the function gives back the value of Theta, which is the difference between the scores of the Audio in the Speaker Model and in the Universal Model
    
    """

    if (isinstance(Audio,str) & isinstance(SPEAKER,str)):

        if (SPEAKER in os.listdir()):


            SPFile=open(SPEAKER,'rb')
            Threshold=ThresholdList.loc[SPEAKER]['Threshold']

            ModelRequested=pickle.load(SPFile)

            SPFile.close()

            TestTrack=wavfile.read(Audio)

            if (TestTrack[0]>20000):
                MFCC=psf.mfcc(TestTrack[1],TestTrack[0],winlen=0.01,winstep=0.0025)
                
                P1=ModelRequested.score(MFCC)

                P2=U.score(MFCC)

                Theta=P1-P2

                if (Theta>Threshold):
                
                    if ReturnTheta=='y':

                        return [1,Theta]
                    else:
                        
                        return 1
                else:
                
                    if ReturnTheta=='y':
                    
                        return [0,Theta]
                
                    else:
                        return 0

            else:
                
                MFCC=psf.mfcc(TestTrack[1],TestTrack[0],winlen=0.025,winstep=0.01)

                P1=ModelRequested.score(MFCC)

                P2=U.score(MFCC)

                Theta=P1-P2

                if (Theta>0):
                
                    if ReturnTheta=='y':

                        return [1,Theta]
                    else:
                    
                        return 1
                else:
                
                    if ReturnTheta=='y':
                    
                        return [0,Theta]
                
                    else:
                    
                        return 0

        else:

            print('Model not found')
            
    else:

        print('Incorrect Parameter')
        

def AjustTheta(SPEAKER,SpeakersPath='Test'):
    
    """ Parameters of the Function
    
    :param SPEAKER: ID of the Speaker in which the optmization of the Threshold in goin to be performed
    :param SpeakersPath: Directory with the Audio Files for the process
    
    """
    
    ###Ajust the Theta Parameter to Improve the False Rejection Rate
    ###Doing the tests for False Rejection and Acceptance
    ###And considering as the new Theta the pondered avarage of the thetas obtained in all the tests
    
    ###Theta Distribution for the False Rejection Tests
    
    ThetaList=[]
    
    ListofSpeakers=os.listdir(SpeakersPath)
    
    PathToAudio=SpeakersPath+'/'+SPEAKER
    
    if (SPEAKER in ListofSpeakers) and (os.path.isdir(PathToAudio)):
        
        for Trial in os.listdir(PathToAudio):
            
            if Trial.endswith('.wav'):
                
                
                ThetaList.append(Verification(SPEAKER,PathToAudio+'/'+Trial,ReturnTheta='y')[1])
                
        Results=np.array(ThetaList)       
                
        FRejectionDist=[Results.mean(),Results.std()]
        
    ###Theta Distribution for the False Acceptance Tests
    
    
        #ThetaList_Acc=[]
    
        #ListofSpeakers.remove(SPEAKER)
    
        #for Impostor in ListofSpeakers:
    
            #PathToAudio=SpeakersPath+'/'+Impostor
        
            #for Trial in os.listdir(PathToAudio):
            
                #if Trial.endswith('.wav'):
                
                    #ThetaList_Acc.append(Verification(SPEAKER,PathToAudio+'/'+Trial,ReturnTheta='y')[1])
                
        #Results_Acc=np.array(ThetaList_Acc)
    
        #FAcceptanceDistribution=[Results_Acc.mean(),Results_Acc.std()]
    
        print(FRejectionDist)
        #print(FAcceptanceDistribution)
        
        ThresholdList.loc[SPEAKER]['Threshold']=FRejectionDist[0]-FRejectionDist[1] 
        
        ThresholdList.to_csv('Threshold.csv')
                
                
    
    