


# NKAMOTO - Application de Gestion des Motos Volées

Bienvenue dans l'application NKAMOTO, conçue pour aider les propriétaires de motos à protéger et à retrouver leurs motos volées. NKAMOTO vous permet d'enregistrer les informations de votre moto, de signaler les vols et de suivre leur emplacement en temps réel.

## Installation

Suivez ces étapes pour cloner et exécuter l'application NKAMOTO sur votre machine locale :

1. Clonez le dépôt NKAMOTO depuis GitHub en utilisant la commande suivante :

   ```shell
   git clone https://github.com/donaldte/nkamoto.git
   ```

2. Accédez au répertoire du projet :

   ```shell
   cd nkamoto
   ```

3. Créez un environnement virtuel (recommandé) pour isoler les dépendances du projet :

   ```shell
   python -m venv venv
   ```

4. Activez l'environnement virtuel :

   - Sur Windows :

     ```shell
     venv\Scripts\activate
     ```

   - Sur macOS et Linux :

     ```shell
     source venv/bin/activate
     ```

5. Installez les dépendances du projet depuis le fichier `requirements.txt` :

   ```shell
   pip install -r requirements.txt
   ```

6. Appliquez les migrations de la base de données :

   ```shell
   python manage.py migrate
   ```

7. Lancez le serveur de développement :

   ```shell
   python manage.py runserver
   ```

8. Accédez à l'application NKAMOTO dans votre navigateur en visitant `http://localhost:8000/`.

## Configuration Supplémentaire

- Assurez-vous d'avoir configuré correctement les paramètres de la base de données dans le fichier `settings.py` si vous utilisez une base de données différente de la base de données SQLite par défaut.

- Pour les environnements de production, veuillez consulter la documentation Django pour déployer votre application correctement.

## Auteur

HYBRAHIMA CISSE

## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE.md](LICENSE.md) pour plus de détails.
```
