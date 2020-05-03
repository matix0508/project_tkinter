from tkinter import Tk, Frame, Label, Button

LARGE_FONT = ('Verdana', 12)

WELCOME_TEXT = """long text
dijwid
ajsidjasi
aidhaid
asdkhahsk"""


class MyApp(Tk):

    def __init__(self, *args, **kwargs):
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
        frame = self.frames[cont]
        frame.tkraise()

class HomePage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='HomePage', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="Visit Page1",
                        command=lambda: controller.show_frame(PageOne))
        button1.pack()

        welcome_text = Label(self, text=WELCOME_TEXT)
        welcome_text.pack()

class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

app = MyApp()
app.mainloop()
