import soundfile as sf
import sounddevice as sd
import AvgFrequency
from os import listdir


def play_audio(audio, rate):
    sd.play(audio, rate)
    sd.wait()  # Wait for audio to stop


def detectGender(freq):
    if freq < 200:
        return 'M'
    else:
        return 'K'


path = 'voices/'
files = [f for f in listdir(path)]  # All files in dir

files_num = 0
errors = 0
real_k = 0
real_m = 0
test_k = 0
test_m = 0

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

    if sex == 'M':
        test_m += 1
    else:
        test_k += 1

    if wav_file[-5] == 'M':
        real_m += 1
    else:
        real_k += 1

    files_num += 1

print('Processed: ' + str(files_num))
print('Errors: ' + str(errors))
print('Recognized women: ' + str(test_k) + '/' + str(real_k))
print('Recognized men: ' + str(test_m) + '/' + str(real_m))
