# **LuciFlow**

**LuciFlow** est une application Web basée sur Flask, conçue pour convertir des fichiers audio (mp3, wav, etc.) en texte à l'aide du modèle d'intelligence artificielle **openai/whisper-large-v3-turbo** disponible sur Hugging Face.

L'application et le modèle d'IA sont destinés à être exécutée en local, ce qui permet de rester maître de ces données. Cependant ceci nécessite, d'avoir une machine avec une puissance de calcul suffisante et ou du temps. ;)

---

## **Caractéristiques principales**

- Interface utilisateur simple et intuitive.
- Upload facile des fichiers audio.
- Support des formats audio courants (mp3, wav, etc.), grâce à ffmpeg.
- Permet la sauvegarde en un seul clic des fichiers de sortie extension txt et doc.
- Utilisation du modèle d'intelligence artificielle **openai/whisper-large-v3-turbo** pour une transcription précise.

---

## **Installation et utilisation**

### **Prérequis**

- Python 3.8 ou supérieur
- Pip (gestionnaire de paquets Python)
- Un environnement virtuel (recommandé)

### **Cloner le projet**

Pour utiliser LuciFlow, commencez par cloner le dépôt Git sur votre machine locale :

```bash
git clone git@github.com:EliottJVN/LuciFlow.git
cd LuciFlow
```

### **Étapes d'installation**

1. **Créer et activer un environnement virtuel :**

   ```bash
   python -m virtualenv env
   source env/bin/activate  # Pour Linux/MacOS
   env\Scripts\activate     # Pour Windows
   ```

2. **Installer les dépendances :**

   ```bash
   pip install -r requirements.txt
   ```

3. **Télécharger le modèle Whisper :**
   Le modèle **openai/whisper-large-v3-turbo** sera automatiquement téléchargé la première fois qu'il sera utilisé. Assurez-vous que votre machine est connectée à Internet.

4. **Lancer l'application :**

   ```bash
   python app.py
   ```

5. **Accéder à l'application :**
   Ouvrez un navigateur web et rendez-vous sur : [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## **Structure du projet**

Voici une vue d'ensemble de l'architecture du projet **LuciFlow** :

```text
LuciFlow
│
├── static/        # Contient les fichiers statiques (CSS, JS, images, etc.)
├── templates/     # Contient les fichiers HTML pour le rendu des pages.
├── uploads/       # Contient les fichiers audio téléchargés par l'utilisateur.
├── app.py         # Point d'entrée principal de l'application Flask.
├── model.py       # Gestion et chargement du modèle Whisper.
└── requirements.txt # Liste des dépendances nécessaires pour le projet.
```

---

## **Fonctionnalités de l'application**

1. **Page d'accueil :**
   - ✅ **Permet d'uploader un fichier audio** via le gestionaire de fichier.
   - ✅ **Bouton de conversion** pour démarrer la transcription.

2. **Traitement audio :**
   - ✅ Une fois le fichier uploadé, il est sauvegardé dans le dossier `uploads/`.
   - ✅ Le modèle **Whisper** effectue la transcription et renvoie le texte. Ce dernier est excuté en local téléchargé lors de la première utilisation.
   *Note: La rapidité de la transcription dépend de la puissance de votre machine.*

3. **Résultat :**
   - ✅ La transcription s'affiche sur la même page.
   - ✅ Possibilité de copier le texte généré.
   - ✅ Boutons de téléchargement pour sauvegarder le texte sous forme de fichier doc ou txt

---

## **Améliorations possibles**

➡️ **Support multi-langues** : Adapter le modèle pour détecter automatiquement la langue ou permettre une sélection manuelle.

➡️ **Interface améliorée** : Ajouter plus de style et de fonctionnalités (exemple : barre de progression pour le téléchargement/transcription).

➡️ **Hébergement distant** : Ajouter des options pour un déploiement sur des services cloud comme AWS, GCP ou Heroku.

➡️ **Historique des transcriptions** : Enregistrer les transcriptions pour un accès ultérieur.

➡️ **Sécurité** : Ajouter des validations pour les fichiers uploadés et limiter les tailles de fichiers.

---

## **Contributions**

Les contributions sont les bienvenues ! Si vous souhaitez contribuer :

1. Forkez le dépôt.
2. Créez une branche pour vos modifications : `git checkout -b feature_<name>`.
3. Soumettez une pull request.

![logo](./static/icon.jpeg)
