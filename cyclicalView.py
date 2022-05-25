from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import main,oneEntryView,oneEntryBigView,onlyprintView
from transitions import asignar,process

class cyclicalView:
    def __init__(self,window):
        #Format Window
        self.window = window
        self.window.geometry("1280x720+0+0")
        self.window.title("Parcial Final - Carvajal Valeria")
        self.window.resizable(False,False)
        #self.window.eval('tk::PlaceWindow . center')

        #BACKGROUND
        self.database_frame = ImageTk.PhotoImage\
            (file='img\imgframes\cic_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #BUTTON        
        #1. 
        self.submit1 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnonec.png')
        self.submit_button1 = Button(self.window,image=self.submit1, relief = "flat", borderwidth=0, background="#fee958",activebackground="#fee958", cursor="hand2", command=self.fun1)
        self.submit_button1.place(x=835,y=185)

        #2. 
        self.submit2 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtntwoc.png')
        self.submit_button2 = Button(self.window,image=self.submit2, relief = "flat", borderwidth=0, background="#fff258",activebackground="#fff258", cursor="hand2", command=self.fun2)
        self.submit_button2.place(x=985,y=185)
        
        #3. 
        self.submit3 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnthreec.png')
        self.submit_button3 = Button(self.window,image=self.submit3, relief = "flat", borderwidth=0, background="#fee958",activebackground="#fee958", cursor="hand2", command=self.fun3)
        self.submit_button3.place(x=835,y=300)
        
        #4. 
        self.submit4 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnfourc.png')
        self.submit_button4 = Button(self.window,image=self.submit4, relief = "flat", borderwidth=0, background="#fef057",activebackground="#fef057", cursor="hand2", command=self.fun4)
        self.submit_button4.place(x=985,y=300)

        #5. 
        self.submit5 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnfivec.png')
        self.submit_button5 = Button(self.window,image=self.submit5, relief = "flat", borderwidth=0, background="#fee759",activebackground="#fee759", cursor="hand2", command=self.fun5)
        self.submit_button5.place(x=835,y=405)

        #6. 
        self.submit6 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnsixc.png')
        self.submit_button6 = Button(self.window,image=self.submit6, relief = "flat", borderwidth=0, background="#feef57",activebackground="#feef57", cursor="hand2", command=self.fun6)
        self.submit_button6.place(x=985,y=405)

        #7. 
        self.submit7 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnsevenc.png')
        self.submit_button7 = Button(self.window,image=self.submit7, relief = "flat", borderwidth=0, background="#ffe55a",activebackground="#ffe55a", cursor="hand2", command=self.fun7)
        self.submit_button7.place(x=835,y=510)

        #8. 
        self.submit8 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtneightc.png')
        self.submit_button8 = Button(self.window,image=self.submit8, relief = "flat", borderwidth=0, background="#feed59",activebackground="#feed59", cursor="hand2", command=self.fun8)
        self.submit_button8.place(x=985,y=510)

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

    def fun1(self):
       asignar(23)
       functionsseq(self)
       process()

    def fun2(self):
       asignar(24)
       functionsseq(self)
       process()
    
    def fun3(self):
       messagebox.showinfo("Un momento", "Por favor, Espere mientras pasan 9 segundos")
       asignar(25)
       functionsseq(self)
       process()
    
    def fun4(self):
       asignar(26)
       functionsseq(self)
       process()

    def fun5(self):
       asignar(27)
       functionsseq(self)
       process()
    
    def fun6(self):
       asignar(28)
       process()

    def fun7(self):
       asignar(29)
       functionsseq1(self)
    
    def fun8(self):
       asignar(30)
       functionsseqmul(self)
    
def functionsseq(self):
    #Cambio de vista
    win = Toplevel()
    onlyprintView.onlyprintView(win)
    self.window.withdraw()
    win.deiconify()

def functionsseq1(self):
    #Cambio de vista
    win = Toplevel()
    oneEntryView.oneEntryView(win)
    self.window.withdraw()
    win.deiconify()

def functionsseqmul(self):
    #Cambio de vista
    win = Toplevel()
    oneEntryBigView.oneEntryBigView(win)
    self.window.withdraw()
    win.deiconify() 
    
def win():
    window = Tk()
    cyclicalView(window)
    window.mainloop()