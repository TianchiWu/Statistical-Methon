import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import tensorflow as tf

# 此处的Url中必须使用斜杠而不是Windows自带的反斜杠
parent_dir = "C:/Users/JackWu/Desktop/测试"
res_dir = "D:/dataset/Spec"


def get_wav_files(parent_dir):
    wav_files = []
    for (root, dirs, filenames) in os.walk(parent_dir):
        for filename in filenames:
            filename_path = os.path.join(root, filename)
            wav_files.append(filename_path)
    return wav_files

def run_main():
    wav_files = get_wav_files(parent_dir)
    print(wav_files)
    for wav_file in wav_files:
        image_name = wav_file.split('/')[-1].split('.')[0].split('\\')[1]
        y, sr = librosa.load(wav_file, sr=None)
        melspec = librosa.feature.melspectrogram(
            y, sr, n_fft=1024, hop_length=512, n_mels=128)
        logmelspec = librosa.power_to_db(melspec)
        plt.figure()
        librosa.display.specshow(logmelspec, sr=sr, x_axis='time', y_axis='mel')
        plt.savefig(res_dir + '/' + str(image_name) + ' .png')
        plt.close()

if __name__ == '__main__':
    run_main()