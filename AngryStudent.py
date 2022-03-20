#Creditos:
#               -Walter A. G.
#               -(Agrega tu nombre)
#               -(Agrega tu nombre)
#               -(Agrega tu nombre)
#2013

from tkinter import*
import random

w=1000
h=800
#Establece eje XY en inferior izquierda:
H=800
W=1000

class Proyectil:
    def __init__(self,x,y,z):
        color_azar2=random.randint(100000,999999)
        self.z=color_azar2
        self.y=y
        self.x=x
        self.radioXo=x-z
        self.radioYo=H-y-z
        self.radioX1=x+z
        self.radioY1=H-y+z
        color_azar=random.randint(100000,999999)
        cv.create_oval(self.radioXo,self.radioYo,self.radioX1,self.radioY1,fill="#"+str(color_azar))
    def Cambiar_Color(self,B):
        cv.create_oval(self.radioXo,self.radioYo,self.radioX1,self.radioY1,fill=str(B))

ventana=Tk()

indicacion=Label(ventana,text="****AngryStudent**** \n De los jugadores de AngryBirds y CC1001-1... \n Llega a ustedes: AngryStudent. \n Basada en hechos reales, \
muestra la epica batalla entre un joven estudiante de inJenieria y su archinemesis Wanakotron. \n Ayuda al novel alumno a vencer a Wanakotron indicandole las \
componentes de velocidad y aceleracion de su molotov")
indicacion.pack()

cv=Canvas(ventana,width=w,height=h,bg="white")
cv.pack()


for k in range(10):
    cv.create_line(0,H-k,W,H-k,fill="green")
for k in range(10):
    cv.create_line(0+k,H,0+k,0,fill="green")

#Wanakotron:
#Longitud de wanacotron
aXi=random.randint(0,w)
aXf=aXi+200
cv.create_rectangle(aXi,h,aXf,h-100,fill="Dark Olive Green")
cv.create_rectangle(aXi,h-90,aXf-150,h-60,fill="deep sky blue")
cv.create_rectangle(aXi+15,h-100,aXi+35,h-110,fill="Dark Olive Green")

rueda1=Proyectil(aXi+20,0,16).Cambiar_Color("Black")
rueda2=Proyectil(aXf-20,0,16).Cambiar_Color("Black")
llanta1=Proyectil(aXi+20,0,8).Cambiar_Color("Grey")
llanta2=Proyectil(aXf-20,0,8).Cambiar_Color("Grey")

cv.create_text(aXf-80,h-80,text="Police",font="Arial 16 bold",fill="White")
cv.create_text(aXf-65,h-60,text="Wanakotron",font="Arial 8 bold",fill="White")

for j in range (1,5,1):
    cv.create_line(0+j,h+j,25+j,h-50+j,fill="blue")
for j in range (1,5,1):
    cv.create_line(26+j,h-49+j,31,h,fill="blue")
for j in range (1,5,1):
    cv.create_line(26+j,h-49+j,26+j,h-110,fill="blue")
for j in range (1,5,1):
    cv.create_line(10+j,h-75,60+j,h-115,fill="blue")
cabeza=Proyectil(30,110,10).Cambiar_Color("Blue")
piedra=Proyectil(11,75,6).Cambiar_Color("Red")

#Brazo del joven estudiante
Xo=11
Yo=75
bola=Proyectil(Xo,Yo,2)
    
def Lanzar():

    x=0
    while x<w:
        bola=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,int(Yo)+int(Vyo.get())*x+int(ay.get())*x*x,2)
        if int(int(int(Yo))+int(Vyo.get())*x+int(ay.get())*x*x)>=0 and int(int(int(Yo))+int(Vyo.get())*x+int(ay.get())*x*x)<=8:
            mensaje1.config(text="Toco el suelo en X="+str(int(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x)))
            bola2=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,25).Cambiar_Color("Yellow")
            bola3=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,20).Cambiar_Color("Red")
            bola4=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,15).Cambiar_Color("Yellow")
            bola5=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,10).Cambiar_Color("Red")
            bola6=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,5).Cambiar_Color("Yellow")
            if (int(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x))>(aXi-49) and (int(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x))<(aXf+49) :
                mensaje.config(text="Acertaste, carro alcanzado !!")
            else:
                mensaje.config(text="Intenta nuevamente...Fuera de rango")  
        x=x+0.1


def Genkidama():

    x=0
    while x<w:
        bola=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,int(Yo)+int(Vyo.get())*x+int(ay.get())*x*x,2)
        if int(int(int(Yo))+int(Vyo.get())*x+int(ay.get())*x*x)>=0 and int(int(int(Yo))+int(Vyo.get())*x+int(ay.get())*x*x)<=8:
            mensaje1.config(text="Toco el suelo en X="+str(int(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x)))
            bola22=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,85).Cambiar_Color("Cyan")
            bola23=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,80).Cambiar_Color("SteelBlue")
            bola24=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,75).Cambiar_Color("Cyan")
            bola25=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,70).Cambiar_Color("SteelBlue")
            bola26=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,65).Cambiar_Color("Cyan")
            bola27=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,60).Cambiar_Color("SteelBlue")
            bola28=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,55).Cambiar_Color("Cyan")
            bola29=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,50).Cambiar_Color("SteelBlue")
            bola22=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,45).Cambiar_Color("Cyan")
            bola23=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,40).Cambiar_Color("SteelBlue")
            bola24=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,35).Cambiar_Color("Cyan")
            bola25=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,30).Cambiar_Color("SteelBlue")
            bola26=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,25).Cambiar_Color("Cyan")
            bola27=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,20).Cambiar_Color("SteelBlue")
            bola28=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,15).Cambiar_Color("Cyan")
            bola29=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,10).Cambiar_Color("SteelBlue")
            bola30=Proyectil(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x,0,5).Cambiar_Color("Yellow")
            if (int(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x))>(aXi-84) and (int(int(Xo)+int(Vxo.get())*x+int(ax.get())*x*x))<(aXf+84) :
                mensaje.config(text="YOU WIN!!, carro alcanzado !!")
            else:
                mensaje.config(text="Intenta nuevamente...Fuera de rango")  
        x=x+0.1


    
def JN():
    mensaje.config(text="Bienvenido...Esperando lanzamiento     ")
    mensaje1.config(text="Toco el suelo en X=")
    cv.create_rectangle(0,0,w+2,h+2,fill="White")

    Vxo.delete(0, END)
    Vyo.delete(0, END)
    ax.delete(0, END)
    ay.delete(0, END)
    

    for k in range(10):
        cv.create_line(0,H-k,W,H-k,fill="green")
    for k in range(10):
        cv.create_line(0+k,H,0+k,0,fill="green")
    #Wanakotron
    #Longitud de wanakotron
    aXi=random.randint(0,w)
    aXf=aXi+200
    cv.create_rectangle(aXi,h,aXf,h-100,fill="Dark Olive Green")
    cv.create_rectangle(aXi,h-90,aXf-150,h-60,fill="deep sky blue")
    cv.create_rectangle(aXi+15,h-100,aXi+35,h-110,fill="Dark Olive Green")

    rueda1=Proyectil(aXi+20,0,16).Cambiar_Color("Black")
    rueda2=Proyectil(aXf-20,0,16).Cambiar_Color("Black")
    llanta1=Proyectil(aXi+20,0,8).Cambiar_Color("Grey")
    llanta2=Proyectil(aXf-20,0,8).Cambiar_Color("Grey")

    cv.create_text(aXf-80,h-80,text="Police",font="Arial 16 bold",fill="White")
    cv.create_text(aXf-65,h-60,text="Wanakotron",font="Arial 8 bold",fill="White")

    for j in range (1,5,1):
        cv.create_line(0+j,h+j,25+j,h-50+j,fill="blue")
    for j in range (1,5,1):
        cv.create_line(26+j,h-49+j,31,h,fill="blue")
    for j in range (1,5,1):
        cv.create_line(26+j,h-49+j,26+j,h-110,fill="blue")
    for j in range (1,5,1):
        cv.create_line(10+j,h-75,60+j,h-115,fill="blue")
    cabeza=Proyectil(30,110,10).Cambiar_Color("Blue")
    piedra=Proyectil(11,75,6).Cambiar_Color("Red")
   

marco1=Frame(ventana)
marco1.pack()

pregunta2=Label(marco1,text="Velocidad inicial en X: ")
pregunta2.pack(side=LEFT)
Vxo=Entry(marco1)
Vxo.pack(side=LEFT)

pregunta3=Label(marco1,text="Aceleracion en X: ")
pregunta3.pack(side=LEFT)
ax=Entry(marco1)
ax.pack(side=LEFT)

marco2=Frame(ventana)
marco2.pack()

pregunta5=Label(marco2,text="Velocidad inicial en Y: ")
pregunta5.pack(side=LEFT)
Vyo=Entry(marco2)
Vyo.pack(side=LEFT)

pregunta6=Label(marco2,text="Aceleracion en Y: ")
pregunta6.pack(side=LEFT)
ay=Entry(marco2)
ay.pack()


marco3=Frame(ventana)
marco3.pack()

boton1=Button(marco3,text="Lanzar o Relanzar",command=Lanzar)
boton1.pack(side=LEFT)
botonBT=Button(marco3,text="Genkidama",command=Genkidama)
botonBT.pack(side=LEFT)
mensaje0=Label(marco3,text="                 ")
mensaje0.pack(side=LEFT)
boton2=Button(marco3,text="Jugar denuevo",command=JN)
boton2.pack()

marco4=Frame(ventana)
marco4.pack()

mensajeMensaje=Label(marco4,text="Mensajes y comentarios  ====>   ")
mensajeMensaje.pack(side=LEFT)
mensaje=Label(marco4,text="Bienvenido...Esperando lanzamiento     ")
mensaje.pack(side=LEFT)
mensaje1=Label(marco4,text="Toco al suelo en X=")
mensaje1.pack(side=LEFT)
                                               

ventana.mainloop()
