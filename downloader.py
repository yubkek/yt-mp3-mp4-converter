import pytube as pt
import os

def download_mp3(link):
    v_id = pt.extract.video_id(link)
    print(v_id)