import smtplib
from email.message import EmailMessage

sender_email = "srimanyuacharya@gmail.com"
receiver_email = "sumanpone8@gmail.com"
app_password = "jjzx mtnu sjay ubln"

# Create the email
msg = EmailMessage()
msg["From"] = "srimanyuacharya@gmail.com"
msg["To"] = "sumanpone8@gmail.com"
msg["Subject"] = "Test Email from Python"
msg.set_content("Hello! This email was sent using Python.")

# Send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.send_message(msg)

print("Email sent!")
