from moviepy.editor import *


def video_to_radio(video_path,audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_path)


def over():
    filepath = r"C:\Users\JackWu\Desktop\抖音BGM-女装"  # 所有视频的路径
    os.chdir(filepath)
    filename = os.listdir(filepath)

    output_dir = r"C:\Users\JackWu\Desktop\output"

    for i in range(len(filename)):
        video_path = filepath + '\\' +filename[i]
        radio_path = output_dir + '\\' + filename[i][0:2] + '.mp3'
        video_to_radio(video_path,radio_path)

if __name__=='__main__':
    over()