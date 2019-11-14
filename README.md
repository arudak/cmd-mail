# cmd-mail - simple script send email by console

Example  
> python cmd-mail.py send -s smtp.gmail.com -p 465 -l login -pw password -to recipient -sub "subject email" -b "text email"

* -s - server SMTP  
* -p - port  
* -l - you account email  
* -pw - you password  
* -to - recipient email  
* -b - text email  

## cmd-mail-f - simple script send email by console with file

Example  

> python cmd-mail.py send -s smtp.gmail.com -p 465 -l login -pw password -to recipient -sub "subject email" -b "text email" -f "path to file"

* -f - path to file