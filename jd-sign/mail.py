# from email.header import Header
# from email.mime.multipart import MIMEMultipart
from pathlib import Path
# import argparse
# import smtplib

# parser = argparse.ArgumentParser()
# parser.add_argument('-f', '--file')
# parser.add_argument('-s', '--sender')
# parser.add_argument('-r', '--receiver')
# parser.add_argument('--host')
# parser.add_argument('-u', '--username')
# parser.add_argument('-p', '--password')

# args = parser.parse_args()

file = Path('./result.txt')
# file = Path(args.file)
# sender = args.sender
# receiver = args.receiver
# host = args.host
# port = 465
# username = args.username
# password = args.password

need_send = False
with file.open() as f:
    lines = f.readlines()
    for line in lines:
        if 'Cookie失效' in line:
            need_send = True

if need_send:
    exit(-1)
#     smtp = smtplib.SMTP_SSL(host=host)
#     smtp.connect(host, port)
#     smtp.login(username, password)

#     try:
#         msg = MIMEMultipart()
#         msg['From'] = sender
#         msg['To'] = receiver
#         msg['Subject'] = Header('JD-Sign Cookie needs refresh', 'utf-8')

#         smtp.sendmail(sender, receiver, msg.as_bytes())
#     except Exception as e:
#         print(e)
