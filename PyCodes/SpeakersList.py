from os.path import join,isfile,isdir
from os import listdir
import re

def ELS(PATH):

    if PATH=='train':
    
        FILES=[F for F in listdir(PATH) if isfile(join(PATH,F))]

        SPEAKERS=[]
    
        for f in FILES:

            S=re.search('[\w]+_Sa.wav',f)

            if S!=None:

                SPEAKERS.append(f.split('_')[0])
                
    elif PATH=='test':

        SPEAKERS=[]

        FILES=[F for F in listdir(PATH)]

        for f in FILES:

            Nam=re.search('[\w]+_Sr1.wav',f)

            if Nam !=None:
                
                SPEAKERS.append(Nam)


    else:

        SPEAKERS=0

    return SPEAKERS

def KAGGLE(PATH):
    SPEAKERS=[]
    
    Directories=[join(PATH,D) for D in listdir(PATH) if isdir(join(PATH,D))]

    for Dir in Directories:

        for Files in Dir:
            
            S=re.search('[\w]+_nohash_+[\w]+.wav',Files)
            ## Terminar essa parte da busca pelos SPEAKERS

        
        

         
