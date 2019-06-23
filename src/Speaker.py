import os
import Speaker_Verification.Training_Verification as GND
import Speaker_Verification.utils as utils
import soundfile as sf
import argparse
import pyaudio
import wave
from scipy.io import wavfile

def Get_Arguments():

    parser=argparse.ArgumentParser()
    parser.add_argument('Option',help='(train/verify) Choose between training a new model or performing the verification of an audio')
    parser.add_argument('Speaker',help='Speaker Id to Verify or Train a new model')
    parser.add_argument('-A','--Audio',default='audioDef',help='Audio File for Verification or Directory for Training if file option was selected on -audm argument')
    parser.add_argument('-ff','--fileformat',default='.wav',help='Format of the Audio File(Default=.wav)')
    parser.add_argument('Method',help='Method for delivering the audio to perform the verification(file/microphone)')
    return parser.parse_args()

def Record(Wave_Output):
    
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = Wave_Output
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def main():

    Arguments = Get_Arguments()
    Speaker_Id = Arguments.Speaker
    Audio_File = Arguments.Audio
    Opt = Arguments.Option
    Audio_Format = Arguments.fileformat
    Base_Dir = GND.BASE_DIR
    Recording_Dir = os.path.join(Base_Dir, 'Recordings')
    Speaker_Rec_Dir = os.path.join(Recording_Dir, Speaker_Id)
    
    if os.path.isdir(Speaker_Rec_Dir):
        pass
    else:
        os.mkdir(Speaker_Rec_Dir)

    if Opt == 'verify':
        if Arguments.Method == 'file':
            GND.Verification(Speaker_Id,Audio_File)
        elif Arguments.Method == 'microphone':
        
            Wave_Output_File = "{}_output.wav".format(Speaker_Id)
            Wave_Output = os.path.join(Speaker_Rec_Dir, Wave_Output_File)    
            Record(Wave_Output)

            if os.path.isfile(Wave_Output):

                VAD_Applied_Files = utils.Voice_Activity_Detection(Wave_Output)
                

if __name__ == '__main__':
    main()
