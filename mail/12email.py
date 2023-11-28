import smtplib
import os


def send_email(messange):
    sender = 'kruher232@gmail.com'
    password = 'Ggwpawp23122003'

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender,password)
        server.send_email(sender,sender, messange)

        return "all ok"
    
    except Exception as _ex:
        return f"{_ex}\n cheak log or pass"
def main():
    messange = input(':')
    print(send_email(messange=messange))

if __name__ == '__main__':
    main(),print('start')
