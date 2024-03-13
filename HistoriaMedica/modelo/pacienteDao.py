from .conexion import ConexionDB
from tkinter import messagebox

def guardarDatoPaciente(persona):
    conexion = ConexionDB()
    sql = f"""INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno , documento , fechaNacimiento, edad, antecedentes, correo, pais, activo) 
    VALUES ('{persona.nombre}','{persona.apellidoMaterno}', '{persona.apellidoPaterno}', {persona.documento},'{persona.FechaNacimiento}', {persona.edad}, '{persona.antecedentes}',
    '{persona.correo}','{persona.pais}', 1)"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente registrado Exitosamente'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Registrar paciente'
        mensaje = 'error al registrar paciente'
        messagebox.showerror(title,mensaje)


class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, documento,
                        FechaNacimiento, edad, antecedentes, correo, pais):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.documento = documento
        self.FechaNacimiento = FechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo
        self.pais = pais

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellidoPaterno}, {self.apellidoMaterno},{self.documento}, {self.FechaNacimiento},{self.antecedentes},{self.correo},{self.pais}]'
