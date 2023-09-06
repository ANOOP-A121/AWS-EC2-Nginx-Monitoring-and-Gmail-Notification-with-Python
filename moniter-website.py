import requests

import smtplib

import paramiko

import schedule

EMAIL_ADDRESS = "anoop###gmail.com"
EMAIL_PASSWORD = "#####"

def send_notification(email):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f"subject: SIT DOWN\n{email}"
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)

def monitor_application():
    try:
    
        response = requests.get('http://43.205.235.56:8080/')

        if response.status_code == 200:

            print('Application is running successfully!')
  
        else:
    
            print('Application is down! fix it') 
            msg = f'Application returned {response.status_code}' 
            send_notification(msg)
        
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname='43.205.235.56', username='ec2-user', key_filename='/home/anoop/.ssh/docker-server.pem')
            stdin, stdout, stderr = ssh.exec_command('docker start 760df0afd9e9')
            print(stdout.readlines())
            ssh.close()
            print('Application is restaerted')
    except Exception as ex:
        print(f'connection error happend: {ex}')
        msg = "subject: SIT DOWN\nAppliction Not Working FIX THE ISSUE!"
        send_notification(msg)

schedule.every(5).seconds.do(monitor_application)

while True:
    schedule.run_pending()