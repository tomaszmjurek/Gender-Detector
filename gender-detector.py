import soundfile as sf
import sounddevice as sd
import AvgFrequency
from os import listdir

path = 'voices/'


def play_audio(audio, rate):
    sd.play(audio, rate)
    sd.wait()  # Wait for audio to stop


def detectGender(freq):
    if freq < 200:
        return 'M'
    else:
        return 'K'


files = [f for f in listdir(path)]


for file in files:
    wav_file = path + file
    try:
        data, rate = sf.read(wav_file)  # , dtype='float32')
    except:
        print("Error reading file!")
        continue

    # w, signal_in = wavfile.read(path + '001_K.wav') #not working

    if str(type(data[0])) == '<class \'numpy.ndarray\'>':
        data = [s[0] for s in data]  # mono ze stereo

    frequency = AvgFrequency.avgFrequency(data, rate)
    sex = detectGender(frequency)
    print(wav_file + ': sex: ' + sex + ', freq: ' + str(frequency))


# plt.pcolormesh(times, frequencies, spectrogram)
# plt.imshow(spectrogram)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()

# Spectogram sposob 2
# f, t, Sxx = signal.spectrogram(np.array(data), rate)
# plt.pcolormesh(t, f, Sxx)
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()
