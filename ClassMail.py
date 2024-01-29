import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ClassOrdersAddonSyncro import OrdersAddonSyncro as oa

class Mail:

    def sendBk(messageObject,messageBody,messageOption):

        mailHost = ""
        mailPort = ""
        mailUser = ""
        mailPass = ""
        mailFrom = ""
        mailTo = ""

        mail = smtplib.SMTP(mailHost,mailPort)
        mail.starttls()
        mail.login(mailUser,mailPass)
        mail.sendmail(mailFrom,mailTo,messageBody,messageOption)
        mail.quit()

    def send(messageObject,messageBody):
        
        port = oa.get_configuration().get('mail','mail_port')
        smtp_server = oa.get_configuration().get('mail','mail_host')
        login = oa.get_configuration().get('mail','mail_user')
        password = oa.get_configuration().get('mail','mail_pass')
        sender_email = oa.get_configuration().get('mail','mail_from')
        receiver_email = oa.get_configuration().get('mail','mail_to')

        message = MIMEMultipart("alternative")
        message["Subject"] = messageObject
        message["From"] = sender_email
        message["To"] = receiver_email
        text = messageBody
        
        # Conversione in oggetti MIMEText e aggiunta al messaggio MIMEMultipart
        part1 = MIMEText(text, "plain")
        #part2 = MIMEText(html, "html")
        message.attach(part1)
        #message.attach(part2)

        # Invio email al server SMTP specificato
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.login(login, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    
    