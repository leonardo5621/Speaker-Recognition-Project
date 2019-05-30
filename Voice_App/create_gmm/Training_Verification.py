import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import pickle
from scipy.io import wavfile
import os
import pandas as pd
from .utils import *
    
def Train_Model(TrainDirectory, ModelName, SamplingRate,  AudioFormat='wav', N_Components=80, Type='diag'):
    
    """ Parameters of the Function
    
    -TrainDirectory: Directory where is located all the Data for the Training of the new model
    -ModelName: Name of the new model, usually it takes the ID of the Speaker
    -N_Components: Number of Components in the Gaussian Mixture Model
    -Type: type of the covariance matrix in the model 
    """
   
    Model = GMM(N_Components,Type)
    CurrentDir = os.getcwd()        
    FTS = Features(TrainDirectory, AudioFormat, SamplingRate)

    print('Features Extracted')
    Model.fit(FTS)
    print('Model Trained')
    os.chdir(TrainDirectory)
    os.chdir(CurrentDir)
    File = open(TrainDirectory + ModelName + '.model','wb')
    pickle.dump(Model,File)
    File.close()
    print('Model File Created')
   # return Model.bic(FTS[0])
    #Dist=Ajust_Theta(ModelName,TrainDirectory)
    #DistInfo=['Mean','std dev']
    #Idx=[ModelName]
    #print(Dist)
    #DistData=pd.read_csv('DistFrame.csv')
    ##Check if the ModelName already exists in the DataFrame
    #L=len(DistData.loc[DistData['Name']==ModelName].index)
    #NewDist=pd.DataFrame({'Name':ModelName,'Mean':Dist[0],'std dev':Dist[1]},index=[L])
    #if L!=0:
    #    i=input('The Model has already been registred, would you like to overwrite it?(y/n)')
    #    if i=='y':
    #        DistData=pd.concat([DistData,NewDist])
    #        DistData.drop_duplicates('Name',keep='last',inplace=True)
    #        DistData.to_csv('DistFrame.csv',index=False)
    #else:
    #    DistData=pd.concat([DistData,NewDist],sort=True)
    #    DistData.to_csv('DistFrame.csv',index=False)
    #AudioProps=pd.read_csv('AudioProperties.csv')
    #L2=len(DistData.loc[DistData['Name']==ModelName].index)
    #NewSpeaker=pd.DataFrame({'Name':ModelName,'SamplingRate':srate,'dtype':dataType,'channels':ch,'AudioFormat':Aformat},index=[L2])
    #AudioProps=pd.concat([AudioProps,NewSpeaker])
    #AudioProps.to_csv('AudioProperties.csv',index=False)

def Verification(SPEAKER,Audio,ModelsDir='AcusticModels/'):
    
    """ Parameters of the Function
    
    -SPEAKER: Speaker ID Claimed for the Verification
    -Audio: Audio File inserted to perform the Verification
    -ReturnTheta: Decides whether or not the function gives back the value of Theta, which is the difference between the scores of the Audio in the Speaker Model and in the Universal Model
    -UBM: Which Universal model to be used for the Verification
    """
    full_path = '/home/leonardo/Speaker-Recognition-Project/WebApp/Voice_App/profiles_access'

    if (isinstance(Audio,str) & isinstance(SPEAKER,str)):
        if (SPEAKER in os.listdir(ModelsDir)):
            SPFile=open(ModelsDir+SPEAKER,'rb')
            ModelRequested=pickle.load(SPFile)
            SPFile.close()
            TestTrack,srate=sf.read(Audio)
            MFCC=librosa.feature.mfcc(TestTrack,sr=srate,n_mfcc=20).transpose()
            MFCC_N=preprocessing.scale(MFCC)
            delta=librosa.feature.delta(MFCC_N)
            Features=np.hstack((MFCC_N,delta))
            for FT in Features:
                P1=ModelRequested.score(FT)
                print(P1)

            #DistData=pd.read_csv('DistFrame.csv')
            #DistData.sort_values('Name',inplace=True)
            #DistData.drop_duplicates(subset='Name',inplace=True,keep='last')
            #Mean=float(DistData.loc[DistData['Name']==SPEAKER].Mean)
            #Sigma=float(DistData.loc[DistData['Name']==SPEAKER]['std dev'])

            FinalScore=P1

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
        
def Get_Score(SPEAKER,Audio,ModelsDir='AcusticModels/'):
    SPFile=open(ModelsDir+SPEAKER,'rb')
    ModelRequested=pickle.load(SPFile)
    SPFile.close()
    TestTrack=sf.read(Audio)
    MFCC=librosa.feature.mfcc(TestTrack[0],TestTrack[1],n_mfcc=20).transpose()
    MFCC_N=preprocessing.scale(MFCC)
    delta=librosa.feature.delta(MFCC_N)
    Features=np.hstack((MFCC_N,delta))
    P1=ModelRequested.score(Features)
    return P1

def Ajust_Theta(SPEAKER,PathToAudio):
    
    """ Parameters of the Function
    
    -SPEAKER: ID of the Speaker in which the optmization of the Threshold in goin to be performed
    -SpeakersPath: Directory with the Audio Files for the process
    
    """
    ThetaList=[]
    if os.path.isdir(PathToAudio):
        for Trial in os.listdir(PathToAudio):
            
            try:
                ThetaList.append(Get_Score(SPEAKER,PathToAudio+'/'+Trial))
            except RuntimeError:
                pass
            
        Results=np.array(ThetaList)
        DistParams=np.array([Results.mean(),Results.std()])        
        return DIstParams

    
    
