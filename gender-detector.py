import soundfile as sf
import sounddevice as sd

path = 'train/'

#def get_data():
wav_file = path + '001_K.wav'
input_data, f_s = sf.read(wav_file, dtype='float32')

sd.play(input_data, f_s)
status = sd.wait()