import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import shutil
import logging
import os

def monitoring():
    logging.basicConfig(filename='automation.log', level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def task_function():
        logging.info("Task Started")
        try:
            result = 10/2
            logging.info(f"Task Result: {result}")
        except Exception as e:
            logging.error(f"Task Failed: {e}")
        finally:
            logging.info("Task Finished")

    task_function()

    def send_alert_email(subject, body):
        sender_email = "youremail@example.com"
        receiver_email = "admin@example.com"
        password = "your_email_password"
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp@example.com", 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()
            print("Alert email sent successfully")
        except Exception as e:
            print(f"Alert Email Failed: {e}")

    def task_with_alert():
        try:
            result = 10/0
        except Exception as e:
            send_alert_email("task failure alert", f"The task failed with error: {str(e)}")

    task_with_alert()


    def monitoring_for_automated_backups():
        logging.basicConfig(filename='backup.log', level=logging.INFO,
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        def backup_files(source_dir, backup_dir):
            logging.info("Backup Process started")
            try:
                if not os.path.exists(backup_dir):
                    os.makedirs(backup_dir)
                    shutil.tree(source_dir, backup_dir)
                    logging.info(f"Backup successful from  ¨{source_dir} to {backup_dir}")
            except Exception as e:
                logging.error(f"Backup Failed: {e}")
                raise
            finally:
                logging.info(f"Backup Process completed")

        backup_files('/path/to/source', 'path/to/backup')
        monitoring_for_automated_backups()

    def check_backup_log():
        try:
            with open('backup.log', 'r') as log_file:
                logs = log_file.readlines()
                if "Backup failed" in logs[-1]:
                    send_alert_email("Backup Failed", "Automated backup process has failed. Check logs.")
                else:
                    print(f"Backup Log File Successful")
        except Exception as e:
            print(f"Error reading log: {e}")
