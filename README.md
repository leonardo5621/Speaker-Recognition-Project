# Speaker Recognition
Repository for the project of an Access System Based on Speaker Verification.

The Objective of this project is to build a Text-Independent Speaker Verification system to control the access to restricted environments.
# The Main Techniques Explored in this project are:
- Mel-Frequency Cepstral Coefficients(MFCC) for the Feature Extraction from Audio Files
- Gaussian-Mixture Models with a Universal Background Model(GMM-UBM) for the Pattern Recognition
# Approach
From an voice signal, the main goal is to determine whether the speaker is who he claims or not.
The MFCC is used in order to convert the audio data into useful acoustic features that represents the voice characteristics from a certain speaker.
Two datasets have been created for each speaker, one for training, and other for testing. The dataset meant for training contains Audio data from a group of Speakers, which will be used to train a Gaussian Mixture Model.
An additional model has been created, the Universal Background Model(UBM). The objective of this model is to represent a generic speaker. The Verification is performed applying the features obtained to the Universal Model, and to the model standing for the identity claimed by the speaker. Each model will return the probability of the features being generated from them . The Verification will take place by comparing these probabilities returned by both models. For each Speaker an Threshold can be ajusted for optimizing the its verification.

 # Results
Two separate audio datasets have been used to evaluate the approach.
The first dataset contains audio data from 15 different speaker from the VoxForge repository.
The second is the ELSDSR database, from the department of Informatics and Mathematical Modeling(IMM) at the Technical University of Denmark(DTU).
The metrics used in order to evaluate the efficiency of the models are: False Rejection Rate(FRR) and the  False Acceptance Rate(FAR). The results have been organized into spreadsheets at the /Results directory for each database.

 # Requirements
 
 The Python packages which have been used for this project:  
- Python Speech Features
- sklearn 
- scipy
- numpy
- matplotlib
- pyaudio
-pydub
-pandas 
