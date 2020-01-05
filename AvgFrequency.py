from scipy.fft import fft
from numpy import linspace

def avgFrequency(data, rate):
    # t = 3
    # n = w * t  #t*w
    nframe = len(data)
    #if n > nframe:
    n = nframe
    frequency = linspace(0, rate, n)
    spectrum = fft(data)
    spectrum = abs(spectrum)
    amp, freq = [], []
    for i in range(len(frequency)):
        if 85 < frequency[i] < 255:  # Human voices
            freq.append(frequency[i])
            amp.append(spectrum[i])
    index = amp.index(max(amp))  # Index of max element?
    avg_freq = freq[index]
    return avg_freq