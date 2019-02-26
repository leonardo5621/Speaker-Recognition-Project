import glob
import os
from pydub import AudioSegment

def ConvertWAV(audioPath,inpFormat,OneFile=True):
    "If the objective is to convert several files at once, audioPath should be the path"
    "to a directory, otherwise it should give the path directly to the file"
    
    currentDir=os.getcwd()
    if OneFile:
        audioDir,audioFile=os.path.split(audioPath)
        os.chdir(audioDir)
        print(audioDir)
        baseName=os.path.splitext(os.path.basename(audioPath))[0]
        newFileName=baseName+'.wav'
        AudioSegment.from_file(audioFile).export(newFileName,format='wav')
        os.chdir(currentDir)
        print('Conversion Done')
    else:
        try:
            ##List of the audio files
            audioList=glob.glob(audioPath+'*.'+inpFormat)
            ##Changing to the directory containing the audio files
            os.chdir(os.path.dirname(audioPath))
            for audioFile in audioList:
                ##Name of the Audio File
                bs=os.path.basename(audioFile)
                FileName=os.path.split(audioFile)[1]
                baseFileName=os.path.splitext(FileName)[0]
                ##Name of the New file
                newFileName=baseFileName+'.wav'
                AudioSegment.from_file(bs,format=inpFormat).export(newFileName,format='wav')
            os.chdir(currentDir)
        except FileNotFoundError:
            os.chdir(currentDir)
            print('File not Found')
            
