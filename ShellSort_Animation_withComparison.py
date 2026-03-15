#ShellSort_Animation (Tkinter).py

# Importar componentes de tkinter
from tkinter import Tk, Canvas, Button, Entry, Frame, Label, RIDGE, BOTTOM, E
import time
from tkinter import messagebox

BG1 = "gray26"

class ShellSort(object):

    def __init__(self):
        # Inicializar ventana principal
        self.root = Tk()
        self.root.title("Algoritmo de ordenamiento ShellSort")
        self.root.protocol("WN_DELETE_WINDOW", self.closing)
        self.Portada()
        self.root.mainloop()
        
    def Close_frame(self):
        # Cerrar portada y abrir programa principal
        self.pag.destroy()
        self.Programa()

    
    def closing(self):
        # Mostrar mensaje al cerrar ventana
        messagebox.showinfo(message="Hasta pronto", title="Cierre")
        self.root.destroy()


    def Portada(self):
        # Crear pantalla de portada con información de la universidad
        letra = 'Georgia Pro'
        c_letra = BG1
        clor = 'white'

        self.pag = Frame(self.root, bg=c_letra)
        self.pag.pack(expand=1, fill='both')
        Label(self.pag,text = "\n\n",bg=c_letra).pack()

        lbl_1 = Label(self.pag, text = "UNIVERSIDAD TECNOLÓGICA DE PANAMÁ\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_1.pack()
        lbl_2 = Label(self.pag, text = "FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_2.pack()
        lbl_3 = Label(self.pag, text = "DEPARTAMENTO DE COMPUTACION Y SIMULACION DE SISTEMAS\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_3.pack()
        lbl_4 = Label(self.pag, text = "CARRERA: LICENCIATURA EN INGENIERÍA DE SOFTWARE\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_4.pack()
        lbl_6 = Label(self.pag, text = "ANÁLISIS Y DISEÑO DE ALGORITMOS\n\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_6.pack()
        lbl_8 = Label(self.pag, text = "PROYECTO FINAL: Metodo de Ordenamiento ShellSort\n\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_8.pack()
        lbl_9 = Label(self.pag, text = "AUTOR:\nQuijano Antonio   8-908-1148\n\n",bg=c_letra,fg = clor,font=(letra,12,'bold'))
        lbl_9.pack()
        lbl_01 = Label(self.pag, text = "PROFESOR: Samuel Jimenez\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_01.pack()
        lbl_02 = Label(self.pag, text = "GRUPO: 1SF-121\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_02.pack()
        lbl_02 = Label(self.pag, text = "II SEMESTRE\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_02.pack()
        lbl_03 = Label(self.pag, text = "2019\n",bg=c_letra,font=(letra,12,'bold'),fg = clor)
        lbl_03.pack()

        # Botón para pasar a la siguiente pantalla
        boton = Button(self.pag, text="Cerrar Ventana", command = self.Close_frame, font=('Georgia Pro',10),bg='black',relief=RIDGE,fg='white').pack(anchor=E,side=BOTTOM)
          


    def Programa(self):
        # Crear ventana principal con canvas y botones
        self.canvas = Canvas(self.root, width=1000, height=600, bg=BG1)
        self.canvas.pack()
        
        # Crear campo de texto para ingresar números
        self.put_num = Entry(self.root)
        self.put_num.focus()
        
        # Crear botones
        self.bton_put_num = Button(self.root, text="Agregar Numero")
        self.bton_fix_list = Button(self.root,text="Ordenar Lista")
        self.bton_new_lista = Button(self.root, text="Nueva Lista")

        # Posicionar botones y campo de texto en el canvas
        self.canvas.create_window(100,50, window=self.put_num)
        self.canvas.create_window(250,50, window=self.bton_put_num)
        self.canvas.create_window(560,50, window=self.bton_fix_list)
        self.canvas.create_window(660,50, window=self.bton_new_lista)

        # Crear textos informativos en el canvas
        self.text_action = self.canvas.create_text(450,50,text = 'Acciones de lista: ',fill = 'white',font=('Gergia Pro',11,'bold'))
        self.inter = self.canvas.create_text(825,50,text = 'Intercambios: ',fill = 'white',font=('Gergia Pro',11,'bold'))

        # Inicializar contador de intercambios
        self.inter_acu = int(0)
        self.acu_text = self.canvas.create_text(900,50,text = str(self.inter_acu),fill = 'yellow',font=('Gergia Pro',11,'bold'))

        # Listas para almacenar datos
        self.list_num = []      # Números ingresados
        self.list_text = []    # Textos en el canvas
        self.list_circle = []  # Círculos en el canvas
        self.amount_circle = int(1)  # Contador para posición

        # Configurar comandos de los botones
        self.bton_put_num.config(command=self.add_num, font=('Georgia Pro',10),bg='black',fg='white',relief=RIDGE)
        self.bton_fix_list.config(command=self.sort_list, font=('Georgia Pro',10),bg='black',fg='white',relief=RIDGE)
        self.bton_new_lista.config(command=self.new_list, font=('Georgia Pro',10),bg='black',fg='white',relief=RIDGE)

        self.canvas.pack(fill="both",expand=True)



    def add_num(self):
        # Obtener número del Entry y agregarlo a la lista
        try:
            num = int(self.put_num.get())
            self.list_num.append(num)
            self.put_num.delete(0, 'end')
            self.create_circle(num)
        
        except ValueError:
            # Mostrar error si no es número entero
            messagebox.showerror(message="Ingrese un numero entero", title="Error")
            self.put_num.delete(0, 'end')

    
    def create_circle(self, num: int):
        # Crear círculo visual para representar el número
        self.circulo = self.canvas.create_oval((self.amount_circle*100), 200,((self.amount_circle*100)+38), 238, outline='white', fill='black')
        self.texto = self.canvas.create_text(((self.amount_circle*100)+19),219,text = num,fill = 'white',font=('Gergia Pro',11,'bold'))
        self.list_circle.append(self.circulo)
        self.list_text.append(self.texto)
        self.amount_circle += 1

        # Limitar a 11 números
        if self.amount_circle > 11:
            messagebox.showinfo(message="Limite de numeros alcanzado", title="Limite")
            self.bton_put_num.config(state='disabled')



    def new_list(self):
        # Limpiar todo y comenzar nueva lista
        self.sort = False
        x = int(0)
        long_list = int(len(self.list_circle))
        while x < long_list:
            self.canvas.delete(self.list_circle[x])
            self.canvas.delete(self.list_text[x])
            x += 1

        self.list_num[:] = []
        self.list_text[:] = []
        self.list_circle[:] = []
        self.amount_circle = int(1)
        self.inter_acu = int(0)
        self.canvas.itemconfig(self.acu_text, text = str(self.inter_acu))
        self.canvas.delete(self.comp)
        self.bton_put_num.config(state='normal')
        self.bton_fix_list.config(state='normal')



    def sort_list(self):
        # Iniciar ordenamiento
        self.sort = True
        self.bton_put_num.config(state='disabled')
        self.bton_fix_list.config(state='disabled')
        self.algoritmo_ShellSort(len(self.list_num), len(self.list_num), self.list_num, self.list_circle, self.list_text)


    
    def comparacion(self, oval_head, oval_tail, text_head, text_tail, gap_head, gap_tail, head, tail):
          # Animación de comparación entre dos elementos
          # Cambiar color a cyan para indicar que se están comparando
          self.canvas.itemconfig(oval_head,fill = 'cyan4')
          self.canvas.itemconfig(oval_tail,fill = 'cyan4')
          
          # Mostrar símbolo > entre los elementos
          self.comp = self.canvas.create_text(((gap_head*100)+((gap_tail*100)/2))+20,319,text = '>',fill = 'white',font=("New Time Roman",15,'bold'))
          
          # Ejecutar animación de movimiento
          self.down(oval_head, oval_tail, text_head, text_tail, self.comp, head, tail)
          
          # Restaurar colores
          self.canvas.itemconfig(oval_head,fill = 'black')
          self.canvas.itemconfig(oval_tail,fill = 'black')
          self.canvas.delete(self.comp)
    

    def down(self, o_head, o_tail, t_head, t_tail, text_comp, head, tail):
          # Animación vertical durante la comparación
          # Determinar color: verde si head > tail, rojo si head < tail
          a = int(0)
          track = 0
          color = ()
          if head > tail:
               color = 'green2'  # Verde: primer número mayor
          else:
               color = 'red2'    # Rojo: primer número menor
               
          # Animación de ida y vuelta
          while a < 2:
               if self.sort == False:
                    return
               x = 0
               y = 1
               if track == 0:
                    # Bajar elementos
                    for i in range(0,100):
                         time.sleep(0.007)
                         self.canvas.move(o_tail, x, y)
                         self.canvas.move(o_head, x, y)
                         self.canvas.move(t_head, x, y)
                         self.canvas.move(t_tail, x, y)
                         self.canvas.update()
                    track = 1
                    print("check")
                    # Cambiar color del símbolo
                    self.canvas.itemconfig(text_comp,fill = color)
                    
                    
               else:
                    # Subir elementos
                    for i in range(0,100):
                         time.sleep(0.007)
                         self.canvas.move(o_tail, x, -y)
                         self.canvas.move(o_head, x, -y)
                         self.canvas.move(t_head, x, -y)
                         self.canvas.move(t_tail, x, -y)
                         if i < 70:
                              self.canvas.move(text_comp, x, -y)
                         self.canvas.update() 
                    track = 1
                    print(track)
               a+=1


    def animation(self, oval_head, oval_tail, text_ovalHead, text_ovalTail, gap):
          # Animación de intercambio de posiciones
          # Cambiar color a dorado
          self.canvas.itemconfig(oval_head,fill = 'gold4')
          self.canvas.itemconfig(oval_tail,fill = 'gold4')

          # Ejecutar movimiento
          self.movement(oval_head, oval_tail, text_ovalHead, text_ovalTail ,gap)

          # Restaurar color negro
          self.canvas.itemconfig(oval_head,fill = 'black')
          self.canvas.itemconfig(oval_tail,fill = 'black')



    def movement(self, o_head, o_tail, text_ovalHead, text_ovalTail, gap):
          # Animación de movimiento para intercambio
          # Primera parte: movimiento vertical
          # Segunda parte: intercambio horizontal
          a = int(0)
          track = 0
          while a < 2:
               if self.sort == False:
                    return
               x = 0
               y = 1
               if track == 0:
                    # Separar verticalmente
                    for i in range(0,100):
                         time.sleep(0.007)
                         self.canvas.move(o_tail, x, -y)
                         self.canvas.move(text_ovalTail, x, -y)
                         self.canvas.move(o_head, x, y)
                         self.canvas.move(text_ovalHead, x, y)
                         self.canvas.update()
                    track = 1
                    print("check")
                    
               else:
                    # Intercambiar horizontalmente
                    for i in range(0,100):
                         time.sleep(0.007)
                         self.canvas.move(o_tail, -gap, y)
                         self.canvas.move(text_ovalTail, -gap, y)
                         self.canvas.move(o_head, gap, -y)
                         self.canvas.move(text_ovalHead, gap, -y)
                         self.canvas.update()
                    track = 1
                    print(track)
               a+=1


    def algoritmo_ShellSort(self, list_long: int, gap_list: int, list_num, list_circle, list_text):
        # Algoritmo ShellSort con animaciones
        
        # Verificar si se debe continuar ordenando
        if self.sort == False:
            return
        
        # Calcular gap inicial
        gap = gap_list//2
        x = int(0)
        temp_circle: tuple[()]
        temp_text: tuple[()]

        # Si gap > 0, continuar con el algoritmo
        if gap > 0:
            while((x+gap) < list_long):
                # Animación de comparación
                self.comparacion(list_circle[x], list_circle[x+gap], list_text[x], list_text[x+gap], (x+1), gap, list_num[x], list_num[x+gap])

                if self.sort == False:
                         return
                
                # Si necesita intercambio
                if list_num[x] > list_num[x+gap]:

                    temp_num = list_num[x]
                    list_num[x] = list_num[x+gap]
                    list_num[x+gap] = temp_num

                    # Animación de intercambio
                    self.animation(list_circle[x], list_circle[x+gap], list_text[x], list_text[x+gap], gap)

                    temp_circle = list_circle[x]
                    list_circle[x] = list_circle[x+gap]
                    list_circle[x+gap] = temp_circle

                    temp_text = list_text[x]
                    list_text[x] = list_text[x+gap]
                    list_text[x+gap] = temp_text

                    # Actualizar contador
                    self.inter_acu += 1
                    self.canvas.itemconfig(self.acu_text, text = str(self.inter_acu))
            
                x += 1
            
            # Llamar recursivamente con gap más pequeño
            self.algoritmo_ShellSort(list_long, gap, list_num, list_circle, list_text)
        
        # Cuando gap = 0, hacer bubble sort final
        else:
            y = int(0)
            while y < (list_long//2):
                x = 0
                while ((x+1) < list_long):
                    self.comparacion(list_circle[x], list_circle[x+1], list_text[x], list_text[x+1], (x+1), 1, list_num[x], list_num[x+1])

                    if self.sort == False:
                         return
                    if list_num[x] > list_num[x+1]:

                        temp_num = list_num[x]
                        list_num[x] = list_num[x+1]
                        list_num[x+1] = temp_num
                        self.animation(list_circle[x], list_circle[x+1], list_text[x], list_text[x+1], 1)

                        temp_circle = list_circle[x]
                        list_circle[x] = list_circle[x+1]
                        list_circle[x+1] = temp_circle

                        temp_text = list_text[x]
                        list_text[x] = list_text[x+1]
                        list_text[x+1] = temp_text
                        self.inter_acu += 1
                        self.canvas.itemconfig(self.acu_text, text = str(self.inter_acu))
                    
                    
                    
                    x += 1
                
                y += 1
        
            return print(f"Lista ordenada: {list_num}")




ShellSort()
