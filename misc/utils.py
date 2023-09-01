import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import logging


logger = logging.getLogger(__name__)


class SQLiter:

    def __init__(self, database) -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add_user(self, user):
        with self.connection:
            self.cursor.execute(
                f"INSERT OR IGNORE INTO users (tg_id, tg_username, tg_fullname, tg_is_bot, tg_locale) "
                f"VALUES ('{user.user_id}','{user.uname}','{user.fullname}','{user.is_bot}','{user.locale}')"
            )
        self.connection.commit()

    def add_action(self, user, action):
        with self.connection:
            user_id = self.cursor.execute(
                f"select id from users where tg_id = '{user.user_id}'"
            ).fetchone()
            self.cursor.execute(
                f"INSERT OR IGNORE INTO actions (user_id, action) "
                f"VALUES ('{user_id[0]}','{action}')"
            )
        self.connection.commit()

    def close(self):
        self.connection.close()


class Statisticer:

    def __init__(self) -> None:
        pass

    def send_log(self):
        pass


class Mailer:

    def __init__(self) -> None:
        self.server = os.getenv('MAIL_SERVER', 'smtp.server.com')
        self.port = os.getenv('MAIL_PORT', '465')
        self.sender = os.getenv('MAIL_SENDER', 'sender@mail.com')
        self.password = os.getenv('MAIL_SENDER_PWD', 'pa$$w0rd')
        self.receiver = os.getenv('MAIL_RECEIVER', 'receiver@mail.com')
        self.subject = os.getenv('MAIL_SUBJECT', 'Origami bot notice')

    def send_notify(self, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP_SSL(self.server, self.port)
            server.login(self.sender, self.password)
            server.send_message(msg)
            server.quit()

            logger.info("Email sent successfully")
        except Exception as e:
            logger.error(f"An error occurred while sending the email: {str(e)}")


if __name__ == '__main__':
    pass
