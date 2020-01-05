from scipy.fft import fft
from numpy import linspace

# data to wczytany plik wav, rate to jego samplerate
def avgFrequency(data, rate):
    nframe = len(data)
    frequency = linspace(0, rate, nframe)
    spectrum = fft(data)  #to jest jakas funkcja od scipy
    spectrum = abs(spectrum) #czym jest spectrum?
    amp, freq = [], []  #amp to pewnie amplituda
    for i in range(len(frequency)):
        if 85 < frequency[i] < 255:  # Human voices
            freq.append(frequency[i])
            amp.append(spectrum[i])
    index = amp.index(max(amp))  # Index of max element w tablicy?
    avg_freq = freq[index]
    return avg_freq