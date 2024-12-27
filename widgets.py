import ttkbootstrap as ttk
import tkinter as tk

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
    
        # create frame widgets
        self.create_widgets()

    def create_widgets(self):
        pass

class MP4Frame(ttk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
    
        # create frame widgets
        self.create_widgets()

    def create_widgets(self):
        pass

class MP4Frame(ttk.Scale):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
    
        # create frame widgets
        self.create_widgets()

    def create_widgets(self):
        pass