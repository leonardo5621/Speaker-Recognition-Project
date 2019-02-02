import argparse
import Speaker_Verification.Training_Verification as GND
import Speaker_Verification.FeatureExtraction as FtE
import Speaker_Verification.format_to_wav as fileConvert
def get_arguments():

    parser=argparse.ArgumentParser()
    parser.add_argument('option',help='(train/verify) Choose between training a new model or performing the verification of an audio')
    #parser.add_argument('-UBM','--UniversalModel',help='Choice of which Universal model to be used(Required for Verification)')
    parser.add_argument('Speaker',help='Speaker Id to verify or train a new model')
    parser.add_argument('Audio',help='Audio File for Verification or Directory for Training')
    parser.add_argument('-TT','--TrainedThresholds',help='Use the trained threshold for the speaker model instead of the standard adopted, which is zero'
                        ,action='store_true')
    parser.add_argument('-ff','--fileformat',default='wav',help='Format of the Audio File(Default=wav)')
    parser.add_argument('-lf','--listfiles',action='store_true',help='if there is a list of files being processed')
    return parser.parse_args()


def Main():
    arguments=get_arguments()
    SpeakerId=arguments.Speaker
    AudioF=arguments.Audio
    #UnivModel=arguments.UniversalModel
    TT=arguments.TrainedThresholds
    formatAudio=arguments.fileformat
    islist=arguments.listfiles
    if formatAudio!='wav':
        fileConvert.ConvertWAV(AudioF,formatAudio,OneFile=islist)
    if arguments.option=='train':
        GND.TrainModel(AudioF,SpeakerId)
    elif arguments.option=='verify':
        GND.Verification(SpeakerId,AudioF,TrainedThresh=TT)
    else:
        print('Invalid Option')


if __name__=='__main__':
    
    Main()
    
