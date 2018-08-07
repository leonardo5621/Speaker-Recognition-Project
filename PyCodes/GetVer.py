import numpy as np
from MFCC import Mfcc
import os

def VerFT(PATH,NAME):

    PathVer=PATH+"/Verification/"

    os.chdir(PathVer)


    mfcc=Mfcc(NAME)

    os.chdir("..")
    os.chdir("..")

    
    return mfcc
