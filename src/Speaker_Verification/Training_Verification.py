import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import python_speech_features as psf
import pickle
from scipy.io import wavfile
import os
from .FeatureExtraction import *
from .remove_Silence import *
import pandas as pd
import soundfile as sf

    
def TrainModel(TrainDirectory,ModelName,Aformat='wav',N_Components=80,Type='tied'):
    
    """ Parameters of the Function
    
    -TrainDirectory: Directory where is located all the Data for the Training of the new model
    -ModelName: Name of the new model, usually it takes the ID of the Speaker
    -N_Components: Number of Components in the Gaussian Mixture Model
    -Type: type of the covariance matrix in the model 
    """
    ModelsDir='AcusticModels'      
    Model=GMM(N_Components,Type)
    CurrentDir=os.getcwd()        
    FTS=Features(TrainDirectory,Aformat)
    print('Features Extracted')
    Model.fit(FTS)
    print('Model Trained')
    os.chdir(TrainDirectory)
    os.chdir(CurrentDir)
    File=open(ModelsDir+'/'+ModelName,'wb')
    pickle.dump(Model,File)
    File.close()
    print('Model File Created')
    Dist=AjustTheta(ModelName,TrainDirectory)
    DistInfo=['Mean','std dev']
    Idx=[ModelName]
    print(Dist)
    NewDist=pd.DataFrame({'Name':ModelName,'Mean':Dist[0],'std dev':Dist[1]},index=[0])
    DistData=pd.read_csv('DistFrame.csv')
    DistData=pd.concat([DistData,NewDist],sort=True)
    DistData.to_csv('DistFrame.csv',index=False)


def Verification(SPEAKER,Audio,ModelsDir='AcusticModels/',UBM='UBMFileN3'):
    
    """ Parameters of the Function
    
    -SPEAKER: Speaker ID Claimed for the Verification
    -Audio: Audio File inserted to perform the Verification
    -ReturnTheta: Decides whether or not the function gives back the value of Theta, which is the difference between the scores of the Audio in the Speaker Model and in the Universal Model
    -UBM: Which Universal model to be used for the Verification
    """

    if (isinstance(Audio,str) & isinstance(SPEAKER,str)):
        if (SPEAKER in os.listdir(ModelsDir)):
            SPFile=open(ModelsDir+SPEAKER,'rb')
            ModelRequested=pickle.load(SPFile)
            SPFile.close()
            TestTrack=sf.read(Audio)
            #TrackSL=SilenceRemoval(TestTrack[1],TestTrack[0])
            TrackSL=TestTrack[0]
            if (TestTrack[1]>20000):
                MFCC=psf.mfcc(TrackSL,TestTrack[1],winlen=0.01,winstep=0.004)
            else:
                MFCC=psf.mfcc(TrackSL,TestTrack[1])

            P1=ModelRequested.score(MFCC)

            DistData=pd.read_csv('DistFrame.csv')
            DistData.sort_values('Name',inplace=True)
            DistData.drop_duplicates(subset='Name',inplace=True,keep='last')
            Mean=float(DistData.loc[DistData['Name']==SPEAKER].Mean)
            Sigma=float(DistData.loc[DistData['Name']==SPEAKER]['std dev'])

            FinalScore=P1-(Mean-1.5*Sigma)

            if FinalScore>0:
                print('Verification Confirmed')
                print(FinalScore)
            else:
                print('Access Denied')
                print(FinalScore)
        else:
            print('Model not found')
    else:
        print('Incorrect Parameter')
        
def GetScore(SPEAKER,Audio,ModelsDir='AcusticModels/'):
    SPFile=open(ModelsDir+SPEAKER,'rb')
    ModelRequested=pickle.load(SPFile)
    SPFile.close()
    TestTrack=sf.read(Audio)
    TrackSL=TestTrack[0]
    if (TestTrack[1]>20000):
        MFCC=psf.mfcc(TrackSL,TestTrack[1],winlen=0.01,winstep=0.004)
        P1=ModelRequested.score(MFCC)
        return P1
    else:
        MFCC=psf.mfcc(TrackSL,TestTrack[1])
        P1=ModelRequested.score(MFCC)
        return P1

def AjustTheta(SPEAKER,PathToAudio):
    
    """ Parameters of the Function
    
    -SPEAKER: ID of the Speaker in which the optmization of the Threshold in goin to be performed
    -SpeakersPath: Directory with the Audio Files for the process
    
    """
    ThetaList=[]
    if os.path.isdir(PathToAudio):
        for Trial in os.listdir(PathToAudio):
            
            try:
                ThetaList.append(GetScore(SPEAKER,PathToAudio+'/'+Trial))
            except RuntimeError:
                pass
            
        Results=np.array(ThetaList)       
        DistParams=np.array([Results.mean(),Results.std()])        
        return DistParams

    
    
