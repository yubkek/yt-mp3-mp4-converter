from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

def download_mp3(link):
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams.get_audio_only()
    ys.download()

def download_mp4(link):
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()
    ys.download()
