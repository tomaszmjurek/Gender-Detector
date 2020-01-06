import soundfile as sf
import sounddevice as sd
import Highest_spectrum
from os import listdir
import sys


def play_audio(audio, rate):
    sd.play(audio, rate)
    sd.wait()  # Wait for audio to stop


def detect_gender(freq):
    if freq < 200:
        return 'M'
    else:
        return 'K'


def process_all():
    k_t = 0
    k_f = 0
    m_t = 0
    m_f = 0
    files_num = 0

    path = 'voices/'
    files = [f for f in listdir(path)]  # All files in dir

    for file in files:
        wav_file = path + file
        sex, frequency = process(wav_file)
        real_sex = wav_file[-5]

        # Matrix of mistakes
        if sex == 'M' and real_sex == 'M':
            m_t += 1
        elif sex == 'M' and real_sex == 'K':
            m_f += 1
        elif sex == 'K' and real_sex == 'K':
            k_t += 1
        elif sex == 'K' and real_sex == 'M':
            k_f += 1

        files_num += 1
    print('Processed: ' + str(files_num))

    print('m_t = ' + str(m_t) + ' m_f = ' + str(m_f))
    print('k_t = ' + str(k_t) + ' k_f = ' + str(k_f))


def process(wav_file):
    try:
        data, rate = sf.read(wav_file)
    except:
        print("Error reading file!")
        return

    if str(type(data[0])) == '<class \'numpy.ndarray\'>':
        data = [s[0] for s in data]  # Changing mono to stereo

    frequency = Highest_spectrum.highest_spectrum(data, rate)
    sex = detect_gender(frequency)
    # print(wav_file + ': sex: ' + sex + ', x_freq: ' + str(frequency))
    print(str(sex))
    return sex, frequency


def main():
    # process_all()
    process(sys.argv[1])


if __name__ == "__main__":
    main()

