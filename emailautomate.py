import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


# linux/apple crontab -e ; *****/pàth/to/script.py ; crontab -l  ; crontab -r
# windows: task scheduler
# Windows Steps:
# 1 Open Task Scheduler (programador de tareas) - crear tarea basica
# 2 set trigger to daily and time to 8:00AM
# 3 set the action to start a program and specify the pytho executable path and the path to the script

def send_email_report():
    # pip install smtplib email
    print('hello')
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    receiver_email = 'email@gmail.com'
    password = "xxxx"
    subject = f"Automate test Daily Report - {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}"
    body = "This is your automated daily report."

    #set up email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # connect to the server email and send
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent')
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()


