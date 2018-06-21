# -*- coding: UTF-8 -*-
 
import sys
import argparse
import smtplib
from email.mime.text import MIMEText
from email.header    import Header
 
def createParser ():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers (dest='command')
 
    send_parser = subparsers.add_parser ('send')
    send_parser.add_argument ('--server', '-s', nargs='+', default=['сервер'])
    send_parser.add_argument ('--port', '-p', nargs='+', default=['порт'])
    send_parser.add_argument ('--login', '-l', nargs='+', default=['логин'])
    send_parser.add_argument ('--password', '-pw', nargs='+', default=['пароль'])
    send_parser.add_argument ('--body', '-b',nargs='*', default=['сообщение'])
    send_parser.add_argument ('--to', '-to', nargs='+', default=['кому'])
    send_parser.add_argument ('--subject',  '-sub', nargs='+' ,default=['тема'])
    return parser
 
def run_send (namespace):
    for server in namespace.server:
     for port in namespace.port:
      for login in namespace.login:
       for password in namespace.password:
        for subject in namespace.subject:
         for to in namespace.to:
          for body in namespace.body:
           smtp_host = '{}'.format(server)
           port = '{}'.format(port) 
           login = '{}'.format(login)
           password = '{}'.format(password)
           recipients_emails = '{}'.format(to)
           subject = '{}'.format(subject)
           body= '{}'.format(body)
           msg = MIMEText( body, 'plain', 'utf-8')
           msg['Subject'] = Header(subject, 'utf-8')
           msg['From'] = login
           msg['To'] = recipients_emails
           s = smtplib.SMTP_SSL(smtp_host,port, timeout=10)
##           s.set_debuglevel(1)
           try:
##              s.starttls()
              s.login(login, password)
              s.sendmail(msg['From'], recipients_emails, msg.as_string())
           finally:
              s.quit()
           
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    if namespace.command == "send":
        run_send (namespace)
    else:
        print ("Что-то пошло не так...")