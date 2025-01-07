from pytubefix import YouTube
from pytubefix.cli import on_progress
from pydub import AudioSegment
import os

def download_mp3(link):
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only()
    ys.download()

    AudioSegment.converter = "C:\\ffmpeg\\ffmpeg.exe"

    file_name = yt.title + ".m4a"
    mp3 = AudioSegment.from_file(file_name)
    to_exp = yt.title + ".mp3"
    mp3.export(to_exp, format='mp3')
    os.remove(file_name)

def download_mp4(link):
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download()
