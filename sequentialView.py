from tkinter import *
from PIL import Image,ImageTk
import main

class sequentialView:
    def __init__(self,window):
        #Format Window
        self.window = window
        self.window.geometry("1280x720+0+0")
        self.window.title("Parcial Final - Carvajal Valeria")
        self.window.resizable(False,False)
        #self.window.eval('tk::PlaceWindow . center')

        #BACKGROUND
        self.database_frame = ImageTk.PhotoImage\
            (file='img\imgframes\seq_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #BUTTON        
        #1. 
        self.submit1 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnone.png')
        self.submit_button1 = Button(self.window,image=self.submit1, relief = "flat", borderwidth=0, background="#fee75b",activebackground="#fee75b", cursor="hand2", command=self.fundata)
        self.submit_button1.place(x=750,y=188)

        #2. 
        self.submit2 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtntwo.png')
        self.submit_button2 = Button(self.window,image=self.submit2, relief = "flat", borderwidth=0, background="#ffee59",activebackground="#ffee59", cursor="hand2", command=self.fundata)
        self.submit_button2.place(x=895,y=188)
        
        #3. 
        self.submit3 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnthree.png')
        self.submit_button3 = Button(self.window,image=self.submit3, relief = "flat", borderwidth=0, background="#fff357",activebackground="#fff357", cursor="hand2", command=self.fundata)
        self.submit_button3.place(x=1048,y=188)
        
        #4. 
        self.submit4 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnfour.png')
        self.submit_button4 = Button(self.window,image=self.submit4, relief = "flat", borderwidth=0, background="#fee75b",activebackground="#fee75b", cursor="hand2", command=self.fundata)
        self.submit_button4.place(x=750,y=298)

        #5. 
        self.submit5 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnfive.png')
        self.submit_button5 = Button(self.window,image=self.submit5, relief = "flat", borderwidth=0, background="#fded59",activebackground="#fded59", cursor="hand2", command=self.fundata)
        self.submit_button5.place(x=895,y=298)

        #6. 
        self.submit6 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnsix.png')
        self.submit_button6 = Button(self.window,image=self.submit6, relief = "flat", borderwidth=0, background="#fff256",activebackground="#fff256", cursor="hand2", command=self.fundata)
        self.submit_button6.place(x=1048,y=298)

        #7. 
        self.submit7 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnseven.png')
        self.submit_button7 = Button(self.window,image=self.submit7, relief = "flat", borderwidth=0, background="#ffe55c",activebackground="#ffe55c", cursor="hand2", command=self.fundata)
        self.submit_button7.place(x=750,y=413)

        #8. 
        self.submit8 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtneight.png')
        self.submit_button8 = Button(self.window,image=self.submit8, relief = "flat", borderwidth=0, background="#fdeb59",activebackground="#fdeb59", cursor="hand2", command=self.fundata)
        self.submit_button8.place(x=895,y=413)

        #9. 
        self.submit9 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnnine.png')
        self.submit_button9 = Button(self.window,image=self.submit9, relief = "flat", borderwidth=0, background="#fff256",activebackground="#fff256", cursor="hand2", command=self.fundata)
        self.submit_button9.place(x=1048,y=413)

        #10. 
        self.submit10 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtnten.png')
        self.submit_button10 = Button(self.window,image=self.submit10, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.fundata)
        self.submit_button10.place(x=820,y=529)

        #11. 
        self.submit11 = ImageTk.PhotoImage\
            (file='img\imgframes\sbtneleven.png')
        self.submit_button11 = Button(self.window,image=self.submit11, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.fundata)
        self.submit_button11.place(x=980,y=530)

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

    def fundata(self):
       pass
    
def win():
    window = Tk()
    sequentialView(window)
    window.mainloop()