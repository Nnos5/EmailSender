from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl, os
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT

app = Flask(__name__)

# 👉 Autoriser CORS pour toutes les routes
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_email():
    destinataire = request.form.get("to")
    sujet = request.form.get("subject")
    contenu = request.form.get("message")

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = destinataire
    msg["Subject"] = sujet
    msg.set_content(contenu)

    # 🔗 Gestion de pièce jointe si présente
    if "attachment" in request.files:
        file = request.files["attachment"]
        if file and file.filename != "":
            file_data = file.read()
            msg.add_attachment(file_data,
                               maintype="application",
                               subtype="octet-stream",
                               filename=file.filename)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        return jsonify({"status": "success", "message": f"Email envoyé à {destinataire}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
