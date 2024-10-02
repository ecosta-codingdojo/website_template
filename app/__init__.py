"""Archivo de configuración de nuestra aplicación."""

# Flask
from flask import Flask

# Python-dotenv
from dotenv import load_dotenv

# Es necesario para cargar las variables de entorno
load_dotenv()

# Instancia de Flask
app = Flask(__name__)