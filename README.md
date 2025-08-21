# 📧 Email Sender - Python

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

Un projet Python moderne pour envoyer des emails avec pièces jointes via un **formulaire web interactif**, sécurisé et responsive.

---

## **✨ Fonctionnalités**

- Formulaire web **responsive** pour envoyer des emails.
- Support des **pièces jointes**.
- **Loader animé** pendant l’envoi.
- Messages de succès et d’erreur visibles.
- Réinitialisation automatique du formulaire après succès.
- Utilisation sécurisée d’un **mot de passe d’application Gmail**.

---

## **🛠 Technologies utilisées**

- **Frontend :** HTML5, CSS3, JavaScript  
- **Backend :** Python, Flask  
- **Envoi d’emails :** SMTP via Gmail  
- **Configuration sécurisée :** `python-dotenv` et `.env`

---

## **⚡ Installation et configuration**

1. **Cloner le projet :**

```bash
git clone https://github.com/Nnos5/EmailSender.git
cd EmailSender

```

2. **Créer un environnement virtuel :**

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Installer les dépendances :**

```bash
pip install -r requirements.txt
```

4. **Créer un fichier `.env` à la racine du projet :**

```env
EMAIL_ADDRESS=votre_email@gmail.com
EMAIL_PASSWORD=mot_de_passe_app
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

> 🔒 **Mot de passe App Gmail :**  
> Gmail n’autorise plus l’accès SMTP avec le mot de passe normal. Tu dois créer un **mot de passe spécifique aux applications** :
> 1. Va sur [Compte Google → Sécurité → Mots de passe des applications](https://myaccount.google.com/apppasswords).  
> 2. Choisis **Mail** comme application et **Autre (Nom personnalisé)** pour l’appareil.  
> 3. Google te génère un mot de passe à 16 caractères.  
> 4. Mets ce mot de passe dans le champ `EMAIL_PASSWORD` de ton `.env`.

5. **Lancer le backend Flask :**

```bash
python3 app.py
```

6. **Ouvrir le frontend :**  
Ouvre `index.html` dans ton navigateur et commence à envoyer des emails.

---

## **📋 Usage**

1. Remplis le formulaire avec :  
   - Destinataire (`To`)  
   - Sujet (`Subject`)  
   - Message  
   - Pièce jointe (optionnelle)  

2. Clique sur **Envoyer**.  
3. Le **loader** s’affiche pendant l’envoi.  
4. Un **message de succès** ou d’erreur s’affiche.  
5. Le formulaire se réinitialise automatiquement après succès.  
6. Le message de succès disparaît après **10 secondes**.

---

## **🔒 Sécurité et bonnes pratiques**

- **Ne jamais pousser ton `.env` sur GitHub.**  
- Chaque utilisateur doit créer son propre mot de passe App Gmail.  
- Utilise un compte Gmail secondaire pour tester.

---

## **🤝 Contributions**

Contributions et améliorations sont les bienvenues :  
- Ajout de templates d’email HTML  
- Envoi à plusieurs destinataires  
- Intégration OAuth2 pour Gmail API

---

## **📄 Licence**

Ce projet est sous licence **MIT**.

---
