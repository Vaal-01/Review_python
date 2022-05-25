from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import main
from transitions import get_enunciado,get_salida1

class onlyprintView:
    def __init__(self,window):
        #Format Window
        self.window = window
        self.window.geometry("1280x720+0+0")
        self.window.title("Parcial Final - Carvajal Valeria")
        self.window.resizable(False,False)
        #self.window.eval('tk::PlaceWindow . center')

        #BACKGROUND
        self.database_frame = ImageTk.PhotoImage\
            (file='img\imgframes\onlyprint_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #LABELS 

        #Enunciado
        self.enunciado = Label(self.window, text=str(get_enunciado()), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.enunciado.place(x=200, y=100)

        #Salida
        self.print = Label(self.window, text=str(get_salida1()), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.print.place(x=200, y=280)

        #BUTTON
        #Show
        self.submit = ImageTk.PhotoImage\
            (file='img\imgframes\sbtninfo.png')
        self.submit_button = Button(self.window,image=self.submit, relief = "flat", borderwidth=0, background="#ffffff",activebackground="#ffffff", cursor="hand2", command=self.calculate)
        self.submit_button.place(x=1080,y=290)

        #Exit
        self.exit_img = ImageTk.PhotoImage \
            (file='img\imgframes\sbtnexit.png')
        self.exit_button = Button(self.window, image=self.exit_img, relief="flat", activebackground="#FFF157", borderwidth=0, background="#FFF157", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=1200, y=25)

    def click_exit(self):
        win = Toplevel()
        main.main(win)
        self.window.withdraw()
        win.deiconify()

    def calculate(self):
        self.print['text']= get_salida1()
        
    
def win():
    window = Tk()
    onlyprintView(window)
    window.mainloop()