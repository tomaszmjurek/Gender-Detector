import soundfile as sf
import sounddevice as sd

path = 'train/'

def play_audio(audio, f_s):
    sd.play(audio, f_s)
    # Wait for audio to stop
    status = sd.wait()



#def get_data():
wav_file = path + '001_K.wav'
input_data, f_s = sf.read(wav_file, dtype='float32')

play_audio(input_data, f_s)