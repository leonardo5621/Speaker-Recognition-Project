import re
from os import listdir
from scipy.io import wavfile
import numpy as np



def read_1_Spk(SPEAKER,PATH):

    FILES=[re.search(SPEAKER+'[\w]+.wav',file) for file in listdir(PATH)]
    read_Those=[]
    TRACKS=[]
    AUDIO=[]
    for f in FILES:

        if f!=None:

            read_Those.append(f.group())



    TRACKS=[wavfile.read(PATH+'/'+SPK) for SPK in read_Those]

    return TRACKS
