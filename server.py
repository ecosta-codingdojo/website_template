"""Server app."""

# Importar la aplicación
from app import app

# Controladores de las páginas
from app.controllers.pages import (
    index,
    nosotros,
    contacto,
)

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True, port=5000)
