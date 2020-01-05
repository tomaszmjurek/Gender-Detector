import soundfile as sf
import sounddevice as sd
from numpy.fft import fft, fftfreq, ifft
from scipy.fftpack import fft
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
# import pandas as pd
import PitchSpectralHps
import GenderDetector

path = 'train/0'

from aubio import source, pitch

downsample = 1


def play_audio(audio, f_s):
    sd.play(audio, f_s)
    # Wait for audio to stop
    status = sd.wait()


# def get_data():
files = ['01_K', '02_M', '03_K', '04_M', '05M', '06_K', '07_M']

for i in range(7):
    wav_file = path + files[i] + '.wav'
    print(wav_file + ":")
    try:
        data, rate = sf.read(wav_file)  # , dtype='float32')
    except:
        continue
    # play_audio(input_data, f_s)

    # w, signal_in = wavfile.read(path + '001_K.wav') #not working

    if str(type(data[0])) == '<class \'numpy.ndarray\'>':
        data = [s[0] for s in data]  # mono ze stereo
    #     print(len(data[0])) # liczba kolumn

    # FFT
    # X = fft(data)

    # frequencies, times, spectrogram = signal.spectrogram(X, rate)
    # n = np.size(times)
    # X_m = abs(/X[0:n/2])
    # hz = PitchSpectralHps.PitchSpectralHps(X, rate)

    sex, freq = GenderDetector.recognizeGender(data, rate)
    print('sex: ' + sex)
    print('freq: ' + str(freq))

    '''
    win_s = 4096 // downsample  # fft size
    hop_s = 512 // downsample
    samplerate = rate // downsample

    s = source(wav_file, samplerate, hop_s)
    samplerate = s.samplerate

    tolerance = 0.8

    pitch_o = pitch("yin", win_s, hop_s, samplerate)
    pitch_o.set_unit("midi")
    pitch_o.set_tolerance(tolerance)

    pitches = []
    confidences = []

    total_frames = 0
    while True:
        samples, read = s()
        pitchy = pitch_o(samples)[0]
        pitches += [pitchy]
        confidence = pitch_o.get_confidence()
        confidences += [confidence]
        total_frames += read
        if read < hop_s: break

    # print("Average frequency = " + str(np.array(pitches).mean()) + " hz")
    # print("Min frequency = " + str(np.array(pitches).min()) + " hz\n")

    
    # Spectogram sposob 1
    nperseg = 2048 #1024
    noverlap = nperseg/8
    nfft = nperseg

    frequencies, times, spectrogram = signal.spectrogram(np.array(data), rate, nperseg=nperseg, noverlap=noverlap, nfft=nfft) #  np.array(data) jesli nie dziala
    x = PitchSpectralHps.PitchSpectralHps(spectrogram, rate)

    result = np.where(x == np.amax(x)) # index of max element in array  # zwraca kilka indeksow jesli takie same wartosci
    freq = (result[0] * rate) / nfft # np.size(x) #nfft
    print(str(files[i] + ' ' + str(freq)))
    '''
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
