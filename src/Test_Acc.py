import os
import numpy as np
import Speaker_Verification.Training_Verification as GND
import argparse

def Get_Arguments():

    parser=argparse.ArgumentParser() 
    parser.add_argument('Speaker', help='Speaker Id to Verify or Train a new model')
    parser.add_argument('D', help='Audio Directory for the accuracy test')
    parser.add_argument('-ff','--fileformat',default='wav',help='Format of the Audio File(Default=wav)')
  
    return parser.parse_args()

def main():
    Models_Dir = 'AcusticModels'
    Arguments = Get_Arguments()
    Speaker_Id = Arguments.Speaker
    Directory = Arguments.D
    Audio_Format = Arguments.fileformat
    Files_For_Test = os.listdir(Directory)
    n_tests = 0
    success = 0

    for Voice_File in Files_For_Test:
        File_Path = os.path.join(Directory, Voice_File)
        if os.path.isfile(File_Path):
            if Voice_File.endswith(Audio_Format):
                n_tests += 1
                success += GND.Verification(Speaker_Id, File_Path)            
    print(success)
    print(n_tests)

if __name__ == '__main__':
    main()
