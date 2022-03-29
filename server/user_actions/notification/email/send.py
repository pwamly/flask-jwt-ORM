from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import os
import uuid
from server.models import EmailLog


def sendEmail(receiver, subject, message, type, db):

    sender = os.environ.get('SENDER_EMAIL_ID')
    sender_email_id_password = os.environ.get('SENDER_EMAIL_PASSWORD')

    msg = MIMEText(message)

    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        smtpObj = smtplib.SMTP(os.environ.get(
            'SMTP_SERVER'), os.environ.get('SMTP_PORT'))
        smtpObj.starttls()
        smtpObj.login(sender, sender_email_id_password)
        smtpObj.send_message(msg)

        print("Successfully sent email to, ", receiver)

        emailLog = EmailLog(emailid=uuid.uuid4(),
                            destination=receiver,
                            subject=subject,
                            message=message,
                            type=type)

        # ...................add()
        db.session.add(emailLog)
        db.session.commit()

    except smtplib.SMTPException as ex:
        print(ex.with_traceback)
