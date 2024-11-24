from tkinter import *


class IMain:
    
    #Main method of interface
    def __init__(self):
        #window configurator
        self.window = Tk()
        self.window.title("Menu System")
        self.window.geometry('800x470')
        self.window.resizable(False, False)
        
        #menu frame
        self.frameMenu = Frame(height=800, width=200, bg='#18171c')
        self.frameMenu.place(x=0, y=0)
        
        #menu buttons
        self.botonHome = Button(self.frameMenu, height=3, width=30, text ='HOME', bg='#708090', command=self.initMenuHome)
        self.botonHome.place(x=-10, y=50)  
        self.botonTask1 = Button(self.frameMenu, height=3, width=30, text ='TASK 1', bg='#708090', command=self.initMenuTask1)
        self.botonTask1.place(x=-10, y=105) 
        self.botonTask2 = Button(self.frameMenu, height=3, width=30, text ='TASK 2', bg='#708090')
        self.botonTask2.place(x=-10, y=160) 
        self.botonTask3 = Button(self.frameMenu, height=3, width=30, text ='TASK 3', bg='#708090')
        self.botonTask3.place(x=-10, y=215)
        self.botonTask4 = Button(self.frameMenu, height=3, width=30, text ='TASK 4', bg='#708090')
        self.botonTask4.place(x=-10, y=270)    
        
        #Home frame definition
        self.frameHome = Frame(height=720, width=600, bg = '#317874')
        self.frameHome.place(x=200,y=0)
        self.homeText1 = Label(self.frameHome, height=2,width=50,text='SISTEMAS INTELIGENTES', bg='#317874', fg='#FFFFFF', font=100)
        self.homeText1.place(x=0 ,y=180)
        self.homeText2 = Label(self.frameHome, height=2,width=50,text='Aplicación', bg='#317874', fg='#FFFFFF', font=100)
        self.homeText2.place(x=0 ,y=220)
        self.homeText3 = Label(self.frameHome, height=2,width=50,text='La Gomera - UTM - 2M', bg='#317874', fg='#FFFFFF', font=100)
        self.homeText3.place(x=0 ,y=400)
        
        #Task 1 frame definition
        self.frameTask1 = Frame(height=720, width=600, bg = '#81C2AE')
        self.frameTask1.place(x=200,y=0)
        #Buttons
        self.botonComprobarTask1 = Button(self.frameTask1,text="Calcular Valor",fg="black", width=20)
        self.botonComprobarTask1.place(x=230 ,y=150)        
        self.botonRedimension = Button(self.frameTask1, text="Redimensionar", fg="black", width=20)
        self.botonRedimension.place(x=230 ,y=370)
        #labels
        self.lblX = Label(self.frameTask1, text="Coordenada X:", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblX.place(x=50 ,y=65)
        self.lblY = Label(self.frameTask1, text="Coordenada Y:", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblY.place(x=50 ,y=105)
        self.lblMapa = Label(self.frameTask1, text="Factor:", font=("Comic Sans",15), fg="white", background="#81C2AE")
        self.lblMapa.place(x=210 ,y=290)
        #Text
        txtX=Entry(self.frameTask1, justify=LEFT, width=30)
        txtX.place(x=210 ,y=70)
        txtY=Entry(self.frameTask1, justify=LEFT, width=30)
        txtY.place(x=210 ,y=110)
        txtFactor=Entry(self.frameTask1, justify=LEFT, width=30)
        txtFactor.place(x=210 ,y=330)
        
        #start with main menu
        self.initMenuHome() 
            
        self.window.mainloop()
        
    #method init home interface
    def initMenuHome(self):
        self.frameTask1.place_forget()
        self.frameHome.place(x=200,y=0)
             
    #method init Task1 interface        
    def initMenuTask1(self):
        self.frameHome.place_forget()
        self.frameTask1.place(x=200,y=0)

   
       