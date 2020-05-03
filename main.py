from tkinter import Tk, Frame, Label, Button


class MyApp(Tk):

    def __init__(self, *args, **kwagrs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'My title')

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, PageOne):  # pętla do wrzucania klatek do self.frames
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frame[cont]
        frame.tkraise()
