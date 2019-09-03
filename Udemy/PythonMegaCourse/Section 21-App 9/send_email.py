from email.mime.text import MIMEText

def send_email(email, height):
    from_email="nowacki69@gmail.com"
    from_password="Brittany@ngel91"
    to_email=email

    subject="Height data"
    message=f"Hey there, your height is <strong>{height}</strong>."

    msg = MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
