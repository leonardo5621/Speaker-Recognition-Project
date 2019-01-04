import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import python_speech_features as psf
import pickle
from scipy.io import wavfile
import os
import FeatureExtraction as FtE

print('TrainModel Creates a new model based on GMM')
print('TrainModel Parameters:  \n -TrainDirectory: Directory which contains the audio data for training')
print('ModelName: The Name of Model according to the Speaker \n N_Components: number of Gaussian Components of the Model(80 has been set as default)')
print('Type: Type of the Covariance Matrix in the Model( tied has been set as default)')

def TrainModel(TrainDirectory,ModelName,N_Components=80,Type='tied'):

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
	ipt=input('Do you want to train a new Universal Background Model? (y/n)')
	if ipt=='y':
		TrainModel('Audio_Data/UniverslModel','UBMFile')
		UBM=open('UBMFile','rb')
		U = pickle.load(UBM)
		UBM.close()


def Verification(SPEAKER,Audio):

	if (isinstance(Audio,str) & isinstance(SPEAKER,str)):

    
		if (SPEAKER in os.listdir()):

			SPFile=open('train/'+SPEAKER+'/'+SPEAKER,'rb')
        
			ModelRequested=pickle.load(SPFile)
        
			SPFile.close()
        
			TestTrack=wavfile.read(Audio)

			MFCC=psf.mfcc(TestTrack[1],TestTrack[0])

			P1=ModelRequested.score(MFCC)

			P2=U.score(MFCC)

			Theta=P1-P2

			if (Theta>0):

				print('Acesso Permitido')

				return 'Acesso Permitido'

			else:
				print('Acesso Negado')
				
				return 'Acesso Negado'

		else:

			print('Modelo Nao Encontrado')
            
	else:

        	print('Parametro Incorreto')
     
