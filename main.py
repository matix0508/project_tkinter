from tkinter import Tk, Frame, Label, Button


class MyApp(Tk):

    def __init__(self, *args, **kwagrs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'My title')

        
