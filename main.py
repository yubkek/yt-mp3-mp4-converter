from ttkbootstrap import Window
import ttkbootstrap as ttk
from tkinter import font
from widgets import *

class Main(Window):
    def __init__(self):
        # setup window
        super().__init__(themename='cyborg')
        self.title('Youtube to MP3/MP4')
        self.geometry('400x300')
        self.resizable(height=False, width=False)

        # setup grid
        self.rowconfigure((0,1,2,3,4,5), weight=1, uniform='a')
        self.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

        # create widgets
        self.create_widgets()

        # run
        self.mainloop()
    
    def create_widgets(self):
        # title
        self.title = ttk.Label(self, 
                               text='Youtube to MP3/MP4 Converter', 
                               anchor='c',
                               font=('Calibri', 15)
                               )
        
        # notebook
        self.notebook = Notebook(self)

        # progress bar
        self.progress_bar = ProgressBar(self)
    
        # place 
        self.title.grid(row = 0, column = 1, columnspan=3, sticky='nsew')
        self.notebook.grid(row = 1, column = 1, columnspan=3, rowspan=3, sticky='nsew')
        self.progress_bar.grid(row = 4, column = 1, columnspan=3, rowspan=2, sticky='ew')

def main():
    app = Main()
    app

if __name__ == "__main__":
    main()