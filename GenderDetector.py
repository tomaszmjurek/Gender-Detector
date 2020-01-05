from scipy.fft import fft
from numpy import linspace

def recognizeGender(data, rate):
    t = 3
    w = rate
    n = w * t  #t*w
    signal = data
    nframe = len(signal)
    #if n > nframe:
    n = nframe
    frequency = linspace(0, w, n)
    spectrum = fft(signal)
    spectrum = abs(spectrum)
    amp, freq = [], []
    for i in range(len(frequency)):
        if 85 < frequency[i] < 255:
            freq.append(frequency[i])
            amp.append(spectrum[i])
    index = amp.index(max(amp))
    avg_freq = freq[index]
    if avg_freq < 200:
        return 'M', avg_freq
    else:
        return 'K', avg_freq