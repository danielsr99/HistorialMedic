import tkinter as tk
from modelo.pacienteDao import Persona, guardarDatoPaciente

class Frame(tk.Frame):
    def __init__(self,root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.camposPaciente()
        self.deshabilitar()
        

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
        self.entryNombre.grid(column=1, row=0 ,padx= 10 ,pady=5, columnspan=2)

        self.svApePaterno = tk.StringVar()
        self.entryApePaterno = tk.Entry(self,textvariable=self.svApePaterno)
        self.entryApePaterno.config(width= 30, font=('ARIAL', 15))
        self.entryApePaterno.grid(column=1, row=1 ,padx= 10 ,pady=5, columnspan=2)

        self.svApeMaterno = tk.StringVar()
        self.entryApeMaterno = tk.Entry(self,textvariable=self.svApeMaterno)
        self.entryApeMaterno.config(width= 30, font=('ARIAL', 15))
        self.entryApeMaterno.grid(column=1, row=2 ,padx= 10 ,pady=5, columnspan=2)

        self.svDocumento = tk.StringVar()
        self.entryDocumento = tk.Entry(self,textvariable=self.svDocumento)
        self.entryDocumento.config(width= 30, font=('ARIAL', 15))
        self.entryDocumento.grid(column=1, row=3 ,padx= 10 ,pady=5, columnspan=2)

        self.svFecNacimiento = tk.StringVar()
        self.entryFecNacimiento = tk.Entry(self,textvariable=self.svFecNacimiento)
        self.entryFecNacimiento.config(width= 30, font=('ARIAL', 15))
        self.entryFecNacimiento.grid(column=1, row=4 ,padx= 10 ,pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self,textvariable=self.svEdad)
        self.entryEdad.config(width= 30, font=('ARIAL', 15))
        self.entryEdad.grid(column=1, row=5 ,padx= 10 ,pady=5, columnspan=2)

        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self,textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width= 30, font=('ARIAL', 15))
        self.entryAntecedentes.grid(column=1, row=6 ,padx= 10 ,pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self,textvariable=self.svCorreo)
        self.entryCorreo.config(width= 30, font=('ARIAL', 15))
        self.entryCorreo.grid(column=1, row=7 ,padx= 10 ,pady=5, columnspan=2)

        self.svPais = tk.StringVar()
        self.entryPais = tk.Entry(self,textvariable=self.svPais)
        self.entryPais.config(width= 30, font=('ARIAL', 15))
        self.entryPais.grid(column=1, row=8 ,padx= 10 ,pady=5, columnspan=2)

        #Buttons

        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL', 12, 'bold'),
                            fg='#DAD5D6', bg='#057D00', cursor='hand2',activebackground='#35BD6F')
        self.btnNuevo.grid(column=0 , row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL', 12, 'bold'),
                            fg='#DAD5D6', bg='#1658A2', cursor='hand2',activebackground='#5F5F5F')
        self.btnGuardar.grid(column=1 , row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL', 12, 'bold'),
                            fg='#DAD5D6', bg='#EA2B02', cursor='hand2',activebackground='#EC8C77')
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=5)

    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(),self.svApePaterno.get(),self.svApeMaterno.get(),self.svDocumento.get(),
            self.svFecNacimiento.get(),self.svEdad.get(),self.svAntecedentes.get(),self.svCorreo.get(),
            self.svPais.get()
        )
        guardarDatoPaciente(persona)
        self.deshabilitar()

    def habilitar(self):
            self.svNombre.set('')
            self.svApePaterno.set('')
            self.svApeMaterno.set('')
            self.svDocumento.set('')
            self.svFecNacimiento.set('')
            self.svEdad.set('')
            self.svAntecedentes.set('')
            self.svCorreo.set('')
            self.svPais.set('')

            self.entryNombre.config(state='norma')
            self.entryApePaterno.config(state='normal')
            self.entryApeMaterno.config(state='normal')
            self.entryDocumento.config(state='normal')
            self.entryFecNacimiento.config(state='normal')
            self.entryEdad.config(state='normal')
            self.entryAntecedentes.config(state='normal')
            self.entryCorreo.config(state='normal')
            self.entryPais.config(state='normal')

            self.btnGuardar.config(state='normal')
            self.btnCancelar.config(state='normal')
    def deshabilitar(self):
            self.svNombre.set('')
            self.svApePaterno.set('')
            self.svApeMaterno.set('')
            self.svDocumento.set('')
            self.svFecNacimiento.set('')
            self.svEdad.set('')
            self.svAntecedentes.set('')
            self.svCorreo.set('')
            self.svPais.set('')

            self.entryNombre.config(state='disabled')
            self.entryApePaterno.config(state='disabled')
            self.entryApeMaterno.config(state='disabled')
            self.entryDocumento.config(state='disabled')
            self.entryFecNacimiento.config(state='disabled')
            self.entryEdad.config(state='disabled')
            self.entryAntecedentes.config(state='disabled')
            self.entryCorreo.config(state='disabled')
            self.entryPais.config(state='disabled')

            self.btnGuardar.config(state='disabled')
            self.btnCancelar.config(state='disabled')