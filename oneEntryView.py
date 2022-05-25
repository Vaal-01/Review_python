from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import main
from transitions import get_enunciado,get_entrada,process1,get_salida1

class oneEntryView:
    def __init__(self,window):
        #Format Window
        self.window = window
        self.window.geometry("1280x720+0+0")
        self.window.title("Parcial Final - Carvajal Valeria")
        self.window.resizable(False,False)
        #self.window.eval('tk::PlaceWindow . center')

        #BACKGROUND
        self.database_frame = ImageTk.PhotoImage\
            (file='img\imgframes\oneentry_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #LABELS 

        #Enunciado
        self.enunciado = Label(self.window, text=str(get_enunciado()), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.enunciado.place(x=210, y=125)

        #Salida
        self.print = Label(self.window, text=str(get_salida1()), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.print.place(x=790, y=405)

        #Entrada
        self.entry = Label(self.window, text=str(get_entrada()), bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.entry.place(x=284, y=365)

        #INPUTS
        #1Entry
        self.one_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.one_entry.place(x=298,y=420,width=120)

        #BUTTON
        #Calculate
        self.submit = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnonecalculate.png')
        self.submit_button = Button(self.window,image=self.submit, relief = "flat", borderwidth=0, background="#fecd63",activebackground="#fecd63", cursor="hand2", command=self.calculate)
        self.submit_button.place(x=200,y=500)

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
        valor_entry = self.one_entry.get()
        #Null validation 
        if valor_entry == "":
            messagebox.showerror("Incompleto", "Por favor, Ingresa el dato solicitado")
        else:
            process1(valor_entry)
            self.print['text']= get_salida1()
        
    
def win():
    window = Tk()
    oneEntryView(window)
    window.mainloop()