import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import python_speech_features as psf
import pickle
from scipy.io import wavfile
import os
import pandas as pd
import soundfile as sf
import librosa
from .utils import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def Train_Model(TrainDirectory,ModelName,Aformat='wav',N_Components=70,Type='diag'):
    
    """ Training of a Gaussian Mixture Model.

    Keyword Arguments:
    
    TrainDirectory: Directory where is located all the Data for the Training of the new model
    ModelName: Name of the new model, usually it takes the ID of the Speaker
    N_Components: Number of Components in the Gaussian Mixture Model
    Type: type of the covariance matrix in the model 
    
    """
    ModelsDir = os.path.join(BASE_DIR, 'AcusticModels')
    Model = GMM(N_Components, Type)        
    FTS = Features(TrainDirectory, Aformat)
    print('Features Extracted')
    Model.fit(FTS[0])
    print('Model Trained')
    try:
        with open(os.path.join(ModelsDir, '{}.model'.format(ModelName)),'wb') as File:
            pickle.dump(Model,File)
        print('Model File Created')
    except FileNotFoundError:
        print('Directory does not exist')

def Verification(ID, Audio, ModelsDir='AcusticModels', Background_Model='ubm'):
    
    """ Speaker Verification of a claimed ID.

    Keyword Arguments:
    
    ModelsDir: Directory of the Acoustic Models.  
   
   """

    ABS_DIR = os.path.join(BASE_DIR, ModelsDir)
    ID_Model = '{}.model'.format(ID)
    ID_Model_File = os.path.join(ABS_DIR, ID_Model) 
    number_mfccs = 13
    UBM_Model = '{}.model'.format(Background_Model)
    UBM_Model_File = os.path.join(ABS_DIR, UBM_Model)

    if (isinstance(Audio,str) & isinstance(ID,str)):

        if os.path.isfile(ID_Model_File):
            with open(ID_Model_File,'rb') as SPFile:
                ModelRequested = pickle.load(SPFile)

            with open(UBM_Model_File, 'rb') as UBM_File:
                UBM = pickle.load(UBM_File)

            TestTrack,srate = sf.read(Audio)
            MFCC = librosa.feature.mfcc(TestTrack,sr=srate,n_mfcc=number_mfccs).transpose()
            Features = preprocessing.scale(MFCC)
            P1 = ModelRequested.score(Features)
            P2 = UBM.score(Features)
            FinalScore = P1-P2

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

    
    
