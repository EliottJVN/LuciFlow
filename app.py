import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Import de la fonction main depuis transcriptor.py
from model import *

app = Flask(__name__)

# Configuration pour l'upload de fichiers
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg'}  # Types de fichiers autorisés

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Vérifie si le fichier a une extension autorisée
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route pour la page d'accueil
@app.route("/")
def index():
    return render_template("index.html")

# Route pour gérer le fichier uploadé
@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        # Appel de la fonction main du backend avec le fichier uploadé
        output_data = run_model(file_path)

        # Retourne le résultat dans le template
        return render_template("index.html", output_data=output_data)

    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)
