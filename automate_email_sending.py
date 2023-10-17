''' You work at a company that sends daily reports to clients via email.
The goal of this project is to automate the process of
sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email,
    including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of
    recipients and send the email and attachment.

    Use the schedule library to schedule the script
    to run daily at a specific time.

    You can also set up a log file to keep track of
    the emails that have been sent and any errors that
    may have occurred during the email sending process. '''


import smtplib
from email.message import EmailMessage
import os
from email.utils import formatdate
import schedule as sc

def automatedEmailSender():
    log = open('Log', 'a')

    # while True:
    #     continueFlag = None
    #     id_count = 0
    #     username = input('Enter username e-mail address: ')
    #     if '@' in username:
    #         aux = username.split('@')
    #         # print(aux)
    #         for i in aux:
    #             if i == '':
    #                 print('Must contain an e-mail address.')
    #                 log.write(formatdate(localtime=True) + '\n  Empty or invalid e-mail address\n')
    #                 continueFlag = True
    #         if continueFlag:
    #             continue
    #         id_count += 1
    #         if '.' in aux[1]:
    #             aux2 = aux[1].split('.')
    #             # print(aux2)
    #             for ii in aux2:
    #                 if ii == '':
    #                     print('Must contain an e-mail address.')
    #                     log.write(formatdate(localtime=True) + '\n  Empty or invalid e-mail address\n')
    #                     continueFlag = True
    #             if continueFlag:
    #                 continue
    #             id_count += 2
    #         else:
    #             print('Must contain an e-mail address.')
    #             log.write(formatdate(localtime=True) + '\n  Empty or invalid e-mail address\n')
    #     else:
    #         print('Must contain an e-mail address.')
    #         log.write(formatdate(localtime=True) + '\n  Empty or invalid e-mail address\n')
    #     continueFlag = False
    #     if id_count == 3:
    #         break
    #     else:
    #         print('Must contain an e-mail address.')
    #         log.write(formatdate(localtime=True) + '\n  Empty or invalid e-mail address\n')
    #         continue
    # while True:
    #     password = input('Enter password: ')
    #     if len(password) == 0:
    #         print('Password cannot be empty.')
    #         log.write(formatdate(localtime=True) + '\n  No password typed\n')
    #         continue
    #     elif len(password) > 0:
    #         break

    username = 'username'
    password = 'password'

    print('\nGenerating reports ...')
    file_paths = []
    # file_names = []
    dir_path = r'.\Report files'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for i in range(1, 3):
        file_name = "Report file " + str(i)
        # file_names.append(file_name)
        full_path = os.path.join(dir_path, file_name)
        file_paths.append(full_path)
        with open(full_path, 'w') as f:
            f.write('Hello, world! ' + str(i))

    recipientList = []
    if os.stat("./Recipients").st_size == 0:
        print('Recipients file is empty.')
        log.write(formatdate(localtime=True) + '\n  Recipients file is empty.\n')
        exit(0)

    with open('Recipients', 'r') as f:
        print('\nRecipients:')
        for line in f.readlines():
            recipientList.append(line)
            # print(line, end='')
    # print(recipientList)
    trimmedRecipientList = []
    for r in recipientList:
        if '\n' in r:
            trimmedRecipientList.append(r[:-1])
        else:
            trimmedRecipientList.append(r)
    print(trimmedRecipientList)
    print()

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    try:
        mailserver.login(username, password)
    except:
        print('Wrong login credentials.')
        log.write(formatdate(localtime=True) + '\n  Wrong login credentials.\n')

    for to_address in trimmedRecipientList:
        msg = EmailMessage()
        # msg["From"] = 'gheorghicaraduiulian@gmail.com'
        msg["From"] = username
        # print(msg["From"])
        # msg["To"] = 'radugheorghica@protonmail.com'
        msg["To"] = to_address
        # print(msg["To"])
        msg["Date"] = formatdate(localtime=True)
        # print(msg["Date"])
        message = 'Hello,\n\nAttached to this e-mail are the generated report files.\n\nBest regards,\nRadu'
        msg.set_content(message)
        msg["Subject"] = 'Daily report files'

        for f in os.listdir("./Report files"):
            msg.add_attachment(open('./Report files/'+str(f), 'r').read(), filename=str(f))
        try:
            mailserver.sendmail(username, to_address, msg.as_string())
            log.write(msg["Date"] + '\n   E-mail sent at address: ' + msg['To'] + '\n')
            print('Email sent successfully at time:',formatdate(localtime=True))
        except:
            print('Could not send e-mail.')
            log.write(formatdate(localtime=True) + '\n  Could not send e-mail.\n')

    log.close()
    mailserver.quit()

sc.every(1).days.do(automatedEmailSender)
while True:
    sc.run_pending()

