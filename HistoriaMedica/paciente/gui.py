import tkinter as tk

class Frame(tk.Frame):
    def __init__(self,root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.camposPaciente()

    def camposPaciente(self):
        #LABELS
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblNombre.grid(column=0, row= 0, padx=10, pady=5)

        self.lblApePaterno = tk.Label(self, text='Apellido paterno: ')
        self.lblApePaterno.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblApePaterno.grid(column=0, row= 1, padx=10, pady=5)

        self.lblApeMaterno = tk.Label(self, text='Apellido materno: ')
        self.lblApeMaterno.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblApeMaterno.grid(column=0, row= 2, padx=10, pady=5)

        self.lblDocumento = tk.Label(self, text='Numero documento: ')
        self.lblDocumento.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblDocumento.grid(column=0, row= 3, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text='Fecha Nacimiento: ')
        self.lblFechNacimiento.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblFechNacimiento.grid(column=0, row= 4, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblEdad.grid(column=0, row= 5, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblAntecedentes.grid(column=0, row= 6, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo electronico: ')
        self.lblCorreo.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblCorreo.grid(column=0, row= 7, padx=10, pady=5)

        
        self.lblPais = tk.Label(self, text='Pais: ')
        self.lblPais.config(font=('ARIAL',15,'bold'), bg=('#CDD8FF'))
        self.lblPais.grid(column=0, row= 8, padx=10, pady=5)

        #ENTRYS (ENTRADA DE VALORES)
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self,textvariable=self.svNombre)
        self.entryNombre.config(width= 30, font=('ARIAL', 15))
        self.entryNombre.grid(column=1, row=0 ,padx= 10 ,pady=5)