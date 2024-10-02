"""Controladores de páginas."""

# App
from app import app

# Flask
from flask import render_template


@app.route("/", methods=["GET"])
def index():
    """Página de inicio."""
    return render_template("pages/index.html")


@app.route("/nosotros/", methods=["GET"])
def nosotros():
    """Página de nosotros."""
    return render_template("pages/nosotros.html")


@app.route("/contacto/", methods=["GET"])
def contacto():
    """Página de contacto."""
    return render_template("pages/contacto.html")