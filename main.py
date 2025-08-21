# main.py
import smtplib, ssl
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

def send_email(destinataire, sujet, contenu):
    # Créer l'objet email
    msg = EmailMessage()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = destinataire
    msg['Subject'] = sujet
    msg.set_content(contenu)

    # Créer le contexte SSL
    context = ssl.create_default_context()

    try:
        # Connexion au serveur SMTP et envoi de l'email
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"✅ Email envoyé à {destinataire} avec succès !")
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi de l'email : {e}")

if __name__ == "__main__":
    destinataire = input("Entrez l'email du destinataire : ")
    sujet = input("Entrez le sujet : ")
    contenu = input("Entrez le message : ")
    send_email(destinataire, sujet, contenu)
