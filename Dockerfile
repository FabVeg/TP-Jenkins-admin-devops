# Utilisation de l'image Python officielle comme base
FROM python:3.11-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances
RUN pip install -r requirements.txt

# Copier le code source
COPY . .

# Exécuter les tests ou démarrer l'application
CMD ["python", "-m", "unittest", "discover"]