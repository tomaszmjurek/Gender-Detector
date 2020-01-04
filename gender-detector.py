import soundfile as sf
import sounddevice as sd
# from scipy.fft import fftshift
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
# import pandas as pd
import PitchSpectralHps

path = 'train/0'

def play_audio(audio, f_s):
    sd.play(audio, f_s)
    # Wait for audio to stop
    status = sd.wait()

#def get_data():
files = ['01_K', '02_M', '03_K', '04_M', '05M', '06_K', '07_M']

for i in range(4):
    wav_file = path + files[i] + '.wav'
    data, rate = sf.read(wav_file, dtype='float32')

    #play_audio(input_data, f_s)

    # w, signal_in = wavfile.read(path + '001_K.wav') #not working

    if str(type(data[0])) == '<class \'numpy.ndarray\'>':
        # print('yea')
        data = [s[0] for s in data]  # mono ze stereo
    #     print(len(data[0])) # liczba kolumn

    # Spectogram sposob 1
    nperseg = 1024
    noverlap = nperseg/8
    nfft = nperseg

    frequencies, times, spectrogram = signal.spectrogram(np.array(data), rate, nperseg=nperseg, noverlap=noverlap, nfft=nfft) #  np.array(data) jesli nie dziala
    x = PitchSpectralHps.PitchSpectralHps(spectrogram, rate)

    result = np.where(x == np.amax(x)) # index of max element in array  # zwraca kilka indeksow jesli takie same wartosci
    freq = result[0] * rate / nfft
    print(str(files[i] + ' ' + str(freq)))

# plt.pcolormesh(times, frequencies, spectrogram)
# plt.imshow(spectrogram)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()

# Wlasny dzwiek do testowania
# fs = 10e3
# N = 1e5
# amp = 2 * np.sqrt(2)
# noise_power = 0.01 * fs / 2
# time = np.arange(N) / float(fs)
# mod = 500*np.cos(2*np.pi*0.25*time)
# carrier = amp * np.sin(2*np.pi*3e3*time + mod)
# noise = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
# noise *= np.exp(-time/5)
# x = carrier + noise

# Spectogram sposob 2
# f, t, Sxx = signal.spectrogram(np.array(data), rate)
# plt.pcolormesh(t, f, Sxx)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()