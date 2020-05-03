###Imports###
from tkinter import Tk, Frame
from tkinter.ttk import Label, Button

###FONTS###
LARGE_FONT = ('Verdana', 12)

###LONGER TEXTS###
EXAMPLE_TEXT = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit.
Ut sodales velit sed tempus accumsan.
Sed sodales nisl a fringilla tempus.
Quisque lacinia sit amet turpis."""


###PROGRAM###
class MyApp(Tk):
    """
    main root of a program
    """

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        Tk.wm_title(self, 'My title')

        container = Frame(self) # funny thing which does sth
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} # dictionary with all frames

        for F in (HomePage, PageOne):  # pętla do wrzucania klatek do self.frames
            frame = F(container, self)
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    def show_frame(self, cont): # function to change frames
        frame = self.frames[cont]
        frame.tkraise()


###FRAMES###
class HomePage(Frame):
    """
    First Page
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='HomePage', font=LARGE_FONT)
        label.pack(pady=10, padx=10) # margins

        button1 = Button(self, text="Visit Page1", # button to go to another page
                        command=lambda: controller.show_frame(PageOne))
        button1.pack()

        welcome_text = Label(self, text=EXAMPLE_TEXT) # some text
        welcome_text.pack()



class PageOne(Frame):
    """
    Another Page
    """

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = Button(self, text="Home Page",
                        command=lambda: controller.show_frame(HomePage))
        button1.pack()

###SETTING UP###
app = MyApp()
app.geometry('600x400') # changes size of the window to width:500px , height:400px
app.mainloop()
