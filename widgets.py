import ttkbootstrap as ttk
import tkinter as tk
from downloader import *

class Notebook(ttk.Notebook):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
    
        # create frame widgets
        self.create_widgets()

    def create_widgets(self):
        # create the 2 frames
        self.mp3_frame = MP3Frame(self)
        self.mp4_frame = MP4Frame(self)

        # add 
        self.add(self.mp3_frame, text = 'MP3 Converter')
        self.add(self.mp4_frame, text = 'MP4 Converter')

class MP3Frame(ttk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window

        # site link var
        self.link = ttk.StringVar()
        self.button_text = ttk.StringVar(value = 'Download')

        # setup grid
        self.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = 'a')
    
        # create frame widgets
        self.create_widgets()

        # set functions
        self.set_functions()

    def create_widgets(self):
        self.entry = ttk.Entry(self, width = 45, textvariable=self.link)
        self.download_button = ttk.Button(self, textvariable = self.button_text)
        
        # place widgets
        self.entry.grid(row = 1, column = 1, columnspan = 6, sticky = 'nsew')
        self.download_button.grid(row = 2, column = 5, columnspan = 2, sticky = 'sew')

    def set_functions(self):
        self.download_button.bind('<Button-1>', self.dl_press)

    def dl_press(self, event):
        download_mp3(self.link.get())
 
class MP4Frame(ttk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window

        # site link var
        self.link = ttk.StringVar(value = 'Download')

        # setup grid
        self.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')
        self.columnconfigure((0,1,2,3,4,5,6,7), weight = 1, uniform = 'a')
    
        # create frame widgets
        self.create_widgets()

        # set functions
        self.set_functions()

    def create_widgets(self):
        self.entry = ttk.Entry(self, width = 45)
        self.download_button = ttk.Button(self, textvariable = self.link)
        
        # place widgets
        self.entry.grid(row = 1, column = 1, columnspan = 6, sticky = 'nsew')
        self.download_button.grid(row = 2, column = 5, columnspan = 2, sticky = 'sew')

    def set_functions(self):
        pass

class ProgressBar(ttk.Progressbar):
    def __init__(self, window):
        super().__init__(window, value = 5, maximum = 10)
        self.window = window
    
        # create frame widgets
        self.create_widgets()

    def create_widgets(self):
        pass
