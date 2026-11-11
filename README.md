# Validación de credenciales con Tkinter

Este proyecto consiste en un programa de inicio de sesión desarrollado en Python utilizando Tkinter.

## Requisitos
- Python 3.12
- python-dotenv

## Instalación
1. Crear un entorno virtual.
2. Instalar las dependencias con:

   `python -m pip install -r requirements.txt`

3. Crear un archivo `.env` con las siguientes variables:

   `APP_USER=tu_usuario`

   `APP_PASSWORD=tu_contraseña`

## Ejecución

Ejecutar el programa con:

`python main.py`

## Funcionamiento

El programa permite ingresar un usuario y una contraseña. Si los datos son correctos, muestra el mensaje «Acceso correcto» en verde. Si son incorrectos, muestra un mensaje de error en rojo.
