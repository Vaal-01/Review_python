from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import main
from transitions import get_enunciado,get_entrada1,get_entrada2,get_entrada3,get_entrada4,get_entrada5,process5,get_salida1

class fiveEntryView:
    def __init__(self,window):
        #Format Window
        self.window = window
        self.window.geometry("1280x720+0+0")
        self.window.title("Parcial Final - Carvajal Valeria")
        self.window.resizable(False,False)
        #self.window.eval('tk::PlaceWindow . center')

        #BACKGROUND
        self.database_frame = ImageTk.PhotoImage\
            (file='img\imgframes\sfiveentry_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #LABELS 

        #Enunciado
        self.enunciado = Label(self.window, text=str(get_enunciado()), bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.enunciado.place(x=180, y=78)

        #Salida
        self.print = Label(self.window, text=str(get_salida1()), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.print.place(x=810, y=362)

        #Entrada 1
        self.entry = Label(self.window, text=str(get_entrada1()), bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.entry.place(x=150, y=296)

        #Entrada 2
        self.entry2 = Label(self.window, text=str(get_entrada2()), bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.entry2.place(x=355, y=296)

        #Entrada 3
        self.entry3 = Label(self.window, text=str(get_entrada3()), bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.entry3.place(x=150, y=402)

        #Entrada 4
        self.entry4 = Label(self.window, text=str(get_entrada4()), bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.entry4.place(x=355, y=402)

        #Entrada 5
        self.entry5 = Label(self.window, text=str(get_entrada5()), bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.entry5.place(x=285, y=512)

        #INPUTS
        #1Entry
        self.one_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.one_entry.place(x=170,y=330,width=120)

        #2Entry
        self.two_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.two_entry.place(x=375,y=330,width=120)

        #3Entry
        self.three_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.three_entry.place(x=170,y=440,width=120)

        #4Entry
        self.four_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.four_entry.place(x=375,y=440,width=120)

        #5Entry
        self.five_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.five_entry.place(x=285,y=545,width=120)

        #BUTTON
        #Calculate
        self.submit = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnonecalculate2.png')
        self.submit_button = Button(self.window,image=self.submit, relief = "flat", borderwidth=0, background="#feda5f",activebackground="#feda5f", cursor="hand2", command=self.calculate)
        self.submit_button.place(x=500,y=615)

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
        valor1 = self.one_entry.get()
        valor2 = self.two_entry.get()
        valor3 = self.three_entry.get()
        valor4 = self.four_entry.get()
        valor5 = self.five_entry.get()
        #Null validation 
        if valor1 == "" or  valor2 == "" or valor3 == "" or valor4 == "" or valor5 == "":
            messagebox.showerror("Incompleto", "Por favor, Ingresa los datos solicitados")
        else:
            process5(valor1,valor2,valor3,valor4,valor5)
            self.print['text']= get_salida1()
        
    
def win():
    window = Tk()
    fiveEntryView(window)
    window.mainloop()