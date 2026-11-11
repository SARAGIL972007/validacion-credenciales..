import tkinter as tk
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Obtener las credenciales registradas
APP_USER = os.getenv("APP_USER")
APP_PASSWORD = os.getenv("APP_PASSWORD")


# FUNCIÓN 1: Capturar las credenciales
def obtener_credenciales():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    validar_credenciales(usuario, contraseña)


# FUNCIÓN 2: Validar las credenciales
def validar_credenciales(usuario, contraseña):
    if usuario == APP_USER and contraseña == APP_PASSWORD:
        mostrar_mensaje("Acceso correcto", "green")
    else:
        mostrar_mensaje("Usuario o contraseña incorrectos", "red")


# FUNCIÓN 3: Mostrar el mensaje
def mostrar_mensaje(texto, color):
    etiqueta_mensaje.config(text=texto, fg=color)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.geometry("350x300")
ventana.resizable(False, False)

# Título
titulo = tk.Label(ventana, text="INICIAR SESIÓN", font=("Arial", 16, "bold"))
titulo.pack(pady=15)

# Campo de usuario
tk.Label(ventana, text="Usuario:").pack()
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack(pady=5)

# Campo de contraseña
tk.Label(ventana, text="Contraseña:").pack()
entrada_contraseña = tk.Entry(ventana, show="*")
entrada_contraseña.pack(pady=5)

# Botón para iniciar sesión
boton = tk.Button(
    ventana,
    text="Iniciar sesión",
    command=obtener_credenciales
)
boton.pack(pady=15)

# Etiqueta para mostrar el resultado
etiqueta_mensaje = tk.Label(ventana, text="", font=("Arial", 11, "bold"))
etiqueta_mensaje.pack()

# Ejecutar la ventana
ventana.mainloop()