import argparse
import sounddevice as sd
from scipy.io import wavfile
import Speaker_Verification.Training_Verification as GND
import Speaker_Verification.FeatureExtraction as FtE
import Speaker_Verification.format_to_wav as fileConvert
def get_arguments():

    parser=argparse.ArgumentParser()
    #parser.add_argument('option',help='(train/verify) Choose between training a new model or performing the verification of an audio')
    #parser.add_argument('-UBM','--UniversalModel',help='Choice of which Universal model to be used(Required for Verification)')
    parser.add_argument('Speaker',help='Speaker Id to verify or train a new model')
    parser.add_argument('-aud','--Audio',default='audioDef',help='Audio File for Verification or Directory for Training if file option was selected on -audm argument')
    parser.add_argument('-ff','--fileformat',default='wav',help='Format of the Audio File(Default=wav)')
    parser.add_argument('-lf','--listfiles',action='store_true',help='if there is a list of files being processed')
    parser.add_argument('Audm',help='Method for delivering the audio to perform the verification(file/microphone)')
    return parser.parse_args()


def Main():
    arguments=get_arguments()
    SpeakerId=arguments.Speaker
    AudioF=arguments.Audio
    #UnivModel=arguments.UniversalModel
    formatAudio=arguments.fileformat
    islist=arguments.listfiles
    if formatAudio!='wav':
        fileConvert.ConvertWAV(AudioF,formatAudio,OneFile=islist)
    if arguments.Audm=='file':
        GND.Verification(SpeakerId,AudioF)
    elif arguments.Audm=='microphone':
        recording=sd.rec(int(44100*5),samplerate=44100,channels=2)
        print('RECORDING')
        sd.wait()
        print('Recording Finished')
        wavfile.write('Verify.wav',44100,recording)
        GND.Verification(SpeakerId,'Verify.wav')
    else:
        print('Invalid Method')

if __name__=='__main__':
    
    Main()
    
