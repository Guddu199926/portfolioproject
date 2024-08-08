import smtplib, ssl

def send_email(user_email, message):
    host = "smtp.gmail.com"
    port = 465

    username = "mannepalliravicharan2@gmail.com"
    password = "vqlj haoo ityw dcny"  # Ensure this is an App Password if 2FA is enabled

    context = ssl.create_default_context()

    try:
        # Establish a secure connection with the server and send the email
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(username, user_email, message)
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
