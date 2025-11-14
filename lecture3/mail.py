import smtplib
from email.message import EmailMessage

sender_email = "yana.a.dimitrova.2024@elsys-bg.org"
receiver_email = "ddimitrov@elsys-bg.org"
password = "dyax keap wpjz ljaz" 

smtp_server = "smtp.gmail.com"
port = 587  

msg = EmailMessage()
msg['Subject'] = "zadachata"
msg['From'] = "yana.a.dimitrova.2024@elsys-bg.org"
msg['To'] = "ddimitrov@elsys-bg.org"
msg.set_content("Zadachata.")

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")