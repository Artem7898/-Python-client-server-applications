import os.path
# "Скрывает" ввод в консоли (может не работать в IDE, например, PyCharm)
import getpass

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication


if __name__ == "__main__":

    # 1. Данные сервера и письма
    # 'email_from'         : адрес отправителя
    # 'email_to'           : адрес получателя
    # 'email_from_password': пароль для email_from
    email_from = input("Адрес отправителя (Ваш): ")
    email_to = input("Адрес получателя: ")
    # Для ввода пароля используется функция getpass.getpass,
    # не отображающая ввод
    email_from_password = getpass.getpass("Пароль для {}: ".format(email_from))

    # Текст сообщения для отправки в HTML-формате.
    # Возможно использовать и простой текст.
    html = """\
    <html>
      <body>
        <h1>Привет!</h1>
        <p>Как дела?</p>
        <p>
          Вот ссылка на сайт Python:
          <a href="http://www.python.org">http://www.python.org</a>.
        </p>
        <p>
          А еще к письму прикреплены:.
          <ul>
            <li>рисунок;</li>
            <li>исходный код.</li>
          </ul>
        </p>
      </body>
    </html>
    """

    # 2. Создание контейнера с содержимым
    msg = MIMEMultipart()
    msg["Subject"] = "Ссылка на сайт Python"
    msg["From"] = email_from
    msg["To"] = email_to

    # 2.1. Текст
    # Добавление вложения в контейнер, используя метод attach контейнера.
    # Для MIMEText если вместо HTML используется текст,
    # вторым параметром будет "plain".
    msg.attach(MIMEText(html, "html"))

    # 2.2. Файл - Рисунок
    img_filename = input("Имя файла с рисунком: ")
    with open(img_filename, "rb") as image:
        attachment = MIMEImage(image.read())
    # Обозначаем, что это вложение и указываем имя
    attachment.add_header("Content-Disposition", "attachment",
                          filename=os.path.basename(img_filename))
    msg.attach(attachment)

    # 2.3. Файл - Код
    with open(__file__, "rb") as f:
        attachment = MIMEApplication(f.read())
    # Необходимо обозначить, что это вложение и его имя
    attachment.add_header("Content-Disposition", "attachment",
                          filename=os.path.basename(__file__))
    msg.attach(attachment)

    # 3. Подключение к серверу и отправка письма
    server = smtplib.SMTP("smtp.gmail.com", 587)
    try:
        # Установление защищенного соединения и авторизация
        server.starttls()
        server.login(email_from, email_from_password)
        # Отправка сообщения
        server.send_message(msg)
        print("Письмо успешно отправлено!")
    except smtplib.SMTPException as err:
        print("Ошибка при отправке письма:", err)
    finally:
        server.quit()

# -------------
# Пример вывода:
#
# Адрес отправителя (Ваш): YuriPetrov***@gmail.com
# Адрес получателя: alex***@gmail.com
# Пароль для YuriPetrov***@gmail.com:
# Имя файла с рисунком: chuvak.png
# Письмо успешно отправлено!
