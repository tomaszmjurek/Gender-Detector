from scipy.fft import fft
from numpy import linspace


def highest_spectrum(data, rate):
    nframe = len(data)
    frequency = linspace(0, rate, nframe)
    spectrum = fft(data)
    spectrum = abs(spectrum)
    amp, freq = [], []
    for i in range(len(frequency)):
        if 85 < frequency[i] < 255:  # Human voices
            freq.append(frequency[i])
            amp.append(spectrum[i])
    index = amp.index(max(amp))  # Index of max element
    hi_spect = freq[index]
    return hi_spect
