import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import requests
import json
from aiogram import types


class SQLiter:

    def __init__(self, database) -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add_user(self, user):
        with self.connection:
            self.cursor.execute(
                f"INSERT OR IGNORE INTO users "
                "(tg_id, tg_username, tg_fullname, tg_is_bot, tg_locale) "
                f"VALUES ('{user.user_id}','{user.uname}',"
                f"'{user.fullname}','{user.is_bot}','{user.locale}')"
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
        self.api_key = os.getenv('METRIC_API_KEY')
        self.url = os.getenv('METRIC_URL')

    def send_log(self, user_id: int, event: str, properties: dict) -> None:
        """
        Send metrics to amplitude.com for agregate information.
        """
        payload = {"api_key": self.api_key, "events": [
            {
                "user_id": user_id,
                "event_type": event,
                "user_properties": properties,
                "country": None,
            }
        ]}
        requests.post(self.url, data=json.dumps(payload))


class Mailer:

    def __init__(self) -> None:
        self.server = os.getenv('MAIL_SERVER', 'smtp.server.com')
        self.port = os.getenv('MAIL_PORT', '465')
        self.sender = os.getenv('MAIL_SENDER', 'sender@mail.com')
        self.password = os.getenv('MAIL_SENDER_PWD', 'pa$$w0rd')
        self.receiver = os.getenv('MAIL_RECEIVER', 'receiver@mail.com')
        self.subject = os.getenv('MAIL_SUBJECT', 'Origami bot notice')

    def send_notify(self, message) -> dict:
        msg = MIMEMultipart()
        msg['From'] = self.sender
        msg['To'] = self.receiver
        msg['Subject'] = self.subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            server = smtplib.SMTP_SSL(self.server, self.port)
            server.login(self.sender, self.password)
            server.send_message(msg)

            return {
                'status': True,
                'msg': 'Email sent successfully',
            }
        except Exception as e:
            return {
                'status': False,
                'msg': f'An error occurred while sending the email: {str(e)}'
            }
        finally:
            server.quit()


def get_user_info(message: types.Message):
    return {
        "user_id": message.from_user.id,
        "uname": message.from_user.username,
        "fullname": message.from_user.full_name,
        "is_bot": message.from_user.is_bot,
        "locale": message.from_user.language_code,
    }


if __name__ == '__main__':
    pass
