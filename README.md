# Speaker Recognition
Repository for the project of an Access System Based on Speaker Recognition.

The Objective of this project is performing Speaker Recognition/Verification to control the access to restricted environments.
# The Main Techniques Explored in this project are:
- Mel-Frequency Cepstral Coefficients(MFCC) for the Feature Extraction from Audio Files
- Gaussian-Mixture Models with a Universal Background Model(GMM-UBM) for the Pattern Recognition
# Approach
The Speaker Recognition process will be performed using the two techniques mentioned.
The MFCC is used in order to convert the Audio data into useful features that we can apply to the Pattern-Recognition technique, which in the case is the Gaussian Mixture Model(GMM).
With the features obtained, two datasets have been created, one for training, and other for testing. The dataset meant for training contains Audio data from a group of Speakers, which will be used to train a Gaussian Mixture Model for each one of the Speakers.
An additional model has been created, the Universal Background Model(UBM). The objective of this model is to represent a generic speaker. The data for testing will be applied to both models, according to the Speaker Id. Each model will return an probability of the features being from a certain Speaker. The Verification will be performed by comparing the probabilities of the features returned by both models. For each Speaker an Threshold can be ajusted for optimizing the verification feature.

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
