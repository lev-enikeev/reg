import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart()

def send_email(message, to):
    me = 'logindsad@yandex.ru'
    msg['From'] = me
    msg['To'] = to
    msg['Subject'] = 'Тест скрипта SMTP'
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.yandex.ru', 587)
    mailserver.set_debuglevel(True)
    # # Определяем, поддерживает ли сервер TLS
    mailserver.ehlo()
    # # Защищаем соединение с помощью шифрования tls
    mailserver.starttls()
    # # Повторно идентифицируем себя как зашифрованное соединение перед аутентификацией.
    mailserver.ehlo()
    mailserver.login(me, 'kqeohtdzqihapyeb')
    mailserver.sendmail(me, to, msg.as_string())
    mailserver.quit()