
# Proyecto Final - Algoritmo

from tkinter import Tk, Canvas, Button, Entry, Frame, Label, RIDGE, BOTTOM, E
import time
from tkinter import messagebox
from functools import partial

class ShellSort(object):
     def __init__(self):
        self.root = Tk()
        self.root.title("Algoritmo de Ordenamiento ShellSort")
        self.root.protocol("WM_DELETE_WINDOW",self.closing)
        self.Presentacion()
        self.root.mainloop()


     def Close_frame(self):
          self.pag.destroy()
          self.Programa()

     def closing(self):
        messagebox.showinfo(message="Espero que haya sido de ayuda\n\nNos vemos pronto", title="Cierre")
        self.root.destroy()

     def Programa(self):
          self.canvas = Canvas(self.root, width=1000, height = 600,bg = 'dark slate gray')
          self.canvas.pack()
          self.num = Entry(self.root)
          self.num.focus()
          self.agregar = Button(text='Agregar valor al Arreglo')
          self.do = Button(text = 'Ordenar Arreglo')
          self.comenzar = Button(text = 'Nuevo Arreglo')
          self.canvas.create_window(100,50,window = self.num)
          self.canvas.create_window(250,50,window = self.agregar)
          self.canvas.create_window(405,50,window = self.do)
          self.canvas.create_window(535,50,window = self.comenzar)
          self.inter = self.canvas.create_text(710,50,text = 'Intercambios: ',fill = 'white',font=('Gergia Pro',11,'bold'))
          self.acumulador = int(0)
          self.acu_text = self.canvas.create_text(770,50,text = str(self.acumulador),fill = 'yellow',font=('Gergia Pro',11,'bold'))
          self.arr = []
          self.cir = []
          self.text = []
          self.e = [1]
        
        
          self.agregar.config(command = self.crear_circu,font=('Georgia Pro',10),bg='black',fg='white',relief=RIDGE)
          self.do.config(command = self.ordenar,font=('Georgia Pro',10),bg='black',fg='white',relief=RIDGE)
          self.comenzar.config(command = self.New_arr,font=('Georgia Pro',10),bg='black',fg='white',relief=RIDGE)
          self.canvas.pack(fill = 'both',expand = True)
          
          


     def Presentacion(self):
          letra = 'Georgia Pro'
          c_letra = 'dark slate gray'
          clor = 'white'
          self.pag = Frame(self.root,bg='dark slate gray')
          self.pag.pack(expand=1,fill='both')
          Label(self.pag,text = "\n\n",bg=c_letra).pack()
          lbl_1 = Label(self.pag, text = "UNIVERSIDAD TECNOLÓGICA DE PANAMÁ\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_1.pack()
          lbl_2 = Label(self.pag, text = "FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_2.pack()
          lbl_3 = Label(self.pag, text = "DEPARTAMENTO DE COMPUTACION Y SIMULACION DE SISTEMAS\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_3.pack()
          lbl_4 = Label(self.pag, text = "CARRERA LICENCIATURA EN INGENIERÍA DE SOFTWARE\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_4.pack()
          lbl_6 = Label(self.pag, text = "ANÁLISIS Y DISEÑO DE ALGORITMOS\n\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_6.pack()
          lbl_8 = Label(self.pag, text = "PROYECTO FINAL: Metodo de Ordenamiento ShellSort\n\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_8.pack()
          lbl_9 = Label(self.pag, text = "AUTOR: \nAntonio Quijano   8-908-1148\n\n",bg=c_letra,fg = clor,font=(letra,12,'bold'))
          lbl_9.pack()
          lbl_01 = Label(self.pag, text = "PROFESOR: Samuel Jimenez\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_01.pack()
          lbl_02 = Label(self.pag, text = "GRUPO: 1SF-121\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_02.pack()
          lbl_02 = Label(self.pag, text = "II SEMESTRE\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_02.pack()
          lbl_03 = Label(self.pag, text = "2019\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
          lbl_03.pack()
          boton = Button(self.pag,text="Delete Windown",command = self.Close_frame,font=('Georgia Pro',10),bg='black',relief=RIDGE,fg='white').pack(anchor=E,side=BOTTOM)
          

     def New_arr(self):
          x = int(0)
          long = int(len(self.arr))
          self.e[0] = 1
          while x < long:
               self.canvas.delete(self.cir[x])
               self.canvas.delete(self.text[x])
               x+=1
               
          self.arr[:] = []
          self.cir[:] = []
          self.text[:] = []
          self.acumulador = int(0)
          self.canvas.itemconfig(self.acu_text,text = str(self.acumulador))
          self.agregar['state'] = 'normal'

     def crear_circu(self):
             if self.num.get():
                  b = int(self.num.get())
                  self.circulo = self.canvas.create_oval((self.e[0]*100), 200,((self.e[0]*100)+38), 238, outline='white', fill='black')
                  self.texto = self.canvas.create_text(((self.e[0]*100)+19),219,text = self.num.get(),fill = 'white',font=('Gergia Pro',11,'bold'))
                  self.cir.append(self.circulo)
                  self.text.append(self.texto)
                  self.arr.append(b)
                  self.e[0] = self.e[0]+1
                  if self.e[0] > 13:
                       self.agregar['state'] = 'disabled'
          
                       
          
     

     def comparacion(self,oval1,oval2,text1,text2,a,b,c,d):
          
          self.canvas.itemconfig(oval1,fill = 'cyan4')
          self.canvas.itemconfig(oval2,fill = 'cyan4')
          self.comp = self.canvas.create_text(((a*100)+((b*100)/2))+20,319,text = '>',fill = 'white',font=("New Time Roman",15,'bold'))
          self.down(oval1,oval2,text1,text2,self.comp,c,d)
          self.canvas.itemconfig(oval1,fill = 'black')
          self.canvas.itemconfig(oval2,fill = 'black')
          self.canvas.delete(self.comp)


     def ordenar(self):
          self.Algoritmo_ShellSort(self.arr,len(self.arr),len(self.arr),self.cir,self.text)

     

     def animation(self,oval1,oval2,text_oval1,text_oval2,ca):
          self.canvas.itemconfig(oval1,fill = 'gold4')
          self.canvas.itemconfig(oval2,fill = 'gold4')

          self.movement(oval1,oval2,text_oval1,text_oval2,ca)

          self.canvas.itemconfig(oval1,fill = 'black')
          self.canvas.itemconfig(oval2,fill = 'black')
          

     def down(self,oval1,oval2,text1,text2,text_comp,c,d):
          a = int(0)
          track = 0
          color = ()
          if c > d:
               color = 'green2'
          else:
               color = 'red2'
               
          while a < 2:
               x = 0
               y = 1
               if track == 0:
                    for i in range(0,100):
                         time.sleep(0.007)
                         self.canvas.move(oval2, x, y)
                         self.canvas.move(oval1, x, y)
                         self.canvas.move(text1, x, y)
                         self.canvas.move(text2, x, y)
                         self.canvas.update()
                    track = 1
                    print("check")
                    self.canvas.itemconfig(text_comp,fill = color)
                    
                    
               else:
                    for i in range(0,100):
                         time.sleep(0.007)
                         self.canvas.move(oval2, x, -y)
                         self.canvas.move(oval1, x, -y)
                         self.canvas.move(text1, x, -y)
                         self.canvas.move(text2, x, -y)
                         if i < 70:
                              self.canvas.move(text_comp, x, -y)
                         self.canvas.update() 
                    track = 1
                    print(track)
               a+=1
     
     

     def movement(self,oval1,oval2,text_oval1,text_oval2,ca):
          a = int(0)
          track = 0
          while a < 2:
               x = 0
               y = 1
               if track == 0:
                    for i in range(0,100):
                         time.sleep(0.007)
                         self.canvas.move(oval2, x, -y)
                         self.canvas.move(text_oval2, x, -y)
                         self.canvas.move(oval1, x, y)
                         self.canvas.move(text_oval1, x, y)
                         self.canvas.update()
                    track = 1
                    print("check")
                    
               else:
                    for i in range(0,100):
                         time.sleep(0.007)
                         self.canvas.move(oval2, -ca, y)
                         self.canvas.move(text_oval2, -ca, y)
                         self.canvas.move(oval1, ca, -y)
                         self.canvas.move(text_oval1, ca, -y)
                         self.canvas.update()
                    track = 1
                    print(track)
               a+=1



     def Algoritmo_ShellSort(self,vector,tamaño,largo,vector_c,vector_t):
          dist = int(tamaño // 2)
          a = int(0)
          x = int(0)
          t = int()
          cir = ()
          text = ()
          
          if(dist > 0):
               while((x+dist) < largo):
                    self.comparacion(vector_c[x],vector_c[x+dist],vector_t[x],vector_t[x+dist],(x+1),dist,vector[x],vector[x+dist])
                    
                    if (vector[x] > vector[x+dist]):
                         t = vector[x]
                         vector[x] = vector[x+dist]
                         vector[x+dist] = t
                         
                         anime = partial(self.animation,vector_c[x],vector_c[x+dist],vector_t[x],vector_t[x+dist],dist)
                         self.root.after(0, anime)
                         cir = vector_c[x]
                         vector_c[x] = vector_c[x+dist]
                         vector_c[x+dist] = cir
                         text = vector_t[x]
                         vector_t[x] = vector_t[x+dist]
                         vector_t[x+dist] = text
                         self.acumulador+=1
                         self.canvas.itemconfig(self.acu_text,text = str(self.acumulador))
                         

                    x+=1

               self.Algoritmo_ShellSort(vector,dist,largo,vector_c,vector_t)
        
          else:
               p = int(0)
               while p < largo:
                    x = 0
                    while((x+1) < largo):

                         if (vector[x] > vector[x+1]):
                              t = vector[x]
                              vector[x] = vector[x+1]
                              vector[x+1] = t

                              anime = partial(self.animation,vector_c[x],vector_c[x+dist],vector_t[x],vector_t[x+dist],dist)
                              self.root.after(0, anime)
                              cir = vector_c[x]
                              vector_c[x] = vector_c[x+1]
                              vector_c[x+1] = cir
                              text = vector_t[x]
                              vector_t[x] = vector_t[x+1]
                              vector_t[x+1] = text
                              self.acumulador+=1
                              self.canvas.itemconfig(self.acu_text,text = str(self.acumulador))

                         x+=1
                    p+=1
                          
               

ShellSort()
       
