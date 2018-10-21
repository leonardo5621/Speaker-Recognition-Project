import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import python_speech_features as psf
import pickle
from scipy.io import wavfile
import os
import FtN

def TrainModel(TrainDirectory,ModelName,N_Components=80,Type='tied'):

	Model =GMM(N_Components,Type)
        
	FTS=FtN.Features(TrainDirectory)

	Model.fit(FTS)

	File=open(ModelName,'wb')

	pickle.dump(Model,File)

	File.close()

arquivo=open('UBMArq','rb')

#U=UBM(256,'tied')

U = pickle.load(arquivo)

#pickle.dump(U,arquivo)

arquivo.close()

def Verification(SPEAKER,Audio):

	if (isinstance(Audio,str) & isinstance(SPEAKER,str)):

		os.chdir('train/'+SPEAKER)
    
		if (SPEAKER in os.listdir()):

			SPFile=open(SPEAKER,'wb')
        
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
     
