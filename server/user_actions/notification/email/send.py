from datetime import datetime
import smtplib


def sendEmail(message, user):
    
    sender_email_id = "samuel.l.jeremia@gmail.com"
    sender_email_id_password = "3AuD!EJ38Us!NnE$7&#7202$++"
    
    try:
        
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(sender_email_id, sender_email_id_password)
        message = message
        smtp.sendmail(sender_email_id, user, message)
        
        smtp.quit()
        
        print("Email sent successfully! at : ", datetime.utcnow)

    except Exception as ex:
        print("Something went wrong....", ex)
