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

files_num = 0
errors = 0
freq_min = []
freq_max = []
for file in files:
    wav_file = path + file
    try:
        data, rate = sf.read(wav_file)
    except:
        errors += 1
        print("Error reading file!")
        continue

    if str(type(data[0])) == '<class \'numpy.ndarray\'>':
        data = [s[0] for s in data]  # Changing mono to stereo

    frequency = AvgFrequency.avgFrequency(data, rate)
    sex = detectGender(frequency)
    print(wav_file + ': sex: ' + sex + ', freq: ' + str(frequency))

    # if
    if frequency > freq_max: freq_max = frequency
    if frequency < freq_min: freq_min = frequency
    files_num += 1

print('Processed: ' + str(files_num))
print('Errors: ' + str(errors))
print('M: max=' + freq_max[0] + 'min=' + freq_min)
print('M: max=' + freq_max[0] + 'min=' + freq_min)
