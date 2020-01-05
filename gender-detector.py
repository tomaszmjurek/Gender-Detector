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
k_t = 0
k_f = 0
m_t = 0
m_f = 0

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

    real_sex = wav_file[-5]

    if sex == 'M' and real_sex == 'M':
        m_t += 1
    elif sex == 'M' and real_sex == 'K':
        m_f += 1
    elif sex == 'K' and real_sex == 'K':
        k_t += 1
    elif sex == 'K' and real_sex == 'M':
        k_f += 1
    # if sex == 'M':
    #     test_m += 1
    # else:
    #     test_k += 1
    #
    # if wav_file[-5] == 'M':
    #     real_m += 1
    # else:
    #     real_k += 1

    files_num += 1

print('Processed: ' + str(files_num))
print('Errors: ' + str(errors))
print('m_t = ' + str(m_t) + ' m_f = ' + str(m_f))
print('k_t = ' + str(k_t) + ' k_f = ' + str(k_f))
# print('Recognized women: ' + str(test_k) + '/' + str(real_k))
# print('Recognized men: ' + str(test_m) + '/' + str(real_m))
