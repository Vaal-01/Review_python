from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import cyclicalView, sequentialView,conditionalsView


class main:
    def __init__(self,window):
        #Format Window
        self.window = window
        self.window.geometry("1280x720+0+0")
        self.window.title("Parcial Final - Carvajal Valeria")
        self.window.resizable(False,False)
        #self.window.eval('tk::PlaceWindow . center')

        #BACKGROUND
        self.database_frame = ImageTk.PhotoImage\
            (file='img\imgframes\main_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')


        #BUTTON        
        #Cyclical 
        self.submitask = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnciclicas.png')
        self.submit_buttonask = Button(self.window,image=self.submitask, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.funCyclical)
        self.submit_buttonask.place(x=750,y=505)

        #Conditionals
        self.submitfsk = ImageTk.PhotoImage\
            (file='img\imgframes\sbtncondicionales.png')
        self.submit_buttonfsk = Button(self.window,image=self.submitfsk, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.funConditionals)
        self.submit_buttonfsk.place(x=750,y=340)

        #Sequential
        self.submitbpsk = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnsecuenciales.png')
        self.submit_buttonbpsk = Button(self.window,image=self.submitbpsk, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.funSequential)
        self.submit_buttonbpsk.place(x=750,y=180)

        #Exit
        self.exit_img = ImageTk.PhotoImage \
            (file='img\imgframes\sbtnexit.png')
        self.exit_button = Button(self.window, image=self.exit_img, relief="flat", activebackground="#FFF157", borderwidth=0, background="#FFF157", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=1200, y=25)

    def click_exit(self):
        ask = messagebox.askyesnocancel("Confirmación", "¿Estás seguro que quieres salir?")
        if ask is True:
            self.window.quit()  
    
    def funSequential(self):
       #Cambio de vista
        win = Toplevel()
        sequentialView.sequentialView(win)
        self.window.withdraw()
        win.deiconify()
    
    def funConditionals(self):
       #Cambio de vista
        win = Toplevel()
        conditionalsView.conditionalsView(win)
        self.window.withdraw()
        win.deiconify()
    
    def funCyclical(self):
       #Cambio de vista
        win = Toplevel()
        cyclicalView.cyclicalView(win)
        self.window.withdraw()
        win.deiconify()

def win():
    window = Tk()
    main(window)
    window.mainloop()

if __name__ == '__main__':
    win()