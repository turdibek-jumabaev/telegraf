import requests
import json
import re

# Telegram API


class Telegraf:

    def __init__(self, token: str, parse_mode: str = 'html'):
        self.token = token
        self.parse_mode = parse_mode
        self.url = f'https://api.telegram.org/bot{self.token}'

    def getMe(self) -> dict:
        """
        API: https://core.telegram.org/bots/api#getme
        """
        response = requests.get(f'{self.url}/getMe')
        return response.json()

    def sendMessage(self, chat_id: int, text: str,
                    parse_mode: str = None, disable_web_page_preview: bool = None,
                    disable_notification: bool = None, reply_to_message_id: int = None,
                    reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendmessage
        """
        if parse_mode is None:
            parse_mode = self.parse_mode
        if disable_web_page_preview is None:
            disable_web_page_preview = False
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendMessage',
                                 data={'chat_id': chat_id,
                                       'text': text,
                                       'parse_mode': parse_mode,
                                       'disable_web_page_preview': disable_web_page_preview,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def forwardMessage(self, chat_id: int, from_chat_id: int, message_id: int,
                       disable_notification: bool = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#forwardmessage
        """
        if disable_notification is None:
            disable_notification = False
        response = requests.post(f'{self.url}/forwardMessage',
                                 data={'chat_id': chat_id,
                                       'from_chat_id': from_chat_id,
                                       'message_id': message_id,
                                       'disable_notification': disable_notification})
        return response.json()

    def sendPhoto(self, chat_id: int, photo: str,
                  caption: str = None, parse_mode: str = None,
                  disable_notification: bool = None, reply_to_message_id: int = None,
                  reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api
        """
        if parse_mode is None:
            parse_mode = self.parse_mode
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendPhoto',
                                 data={'chat_id': chat_id,
                                       'photo': photo,
                                       'caption': caption,
                                       'parse_mode': parse_mode,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendAudio(self, chat_id: int, audio: str,
                  caption: str = None, parse_mode: str = None,
                  duration: int = None, performer: str = None,
                  title: str = None, disable_notification: bool = None,
                  reply_to_message_id: int = None, reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendaudio
        """
        if parse_mode is None:
            parse_mode = self.parse_mode
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendAudio',
                                 data={'chat_id': chat_id,
                                       'audio': audio,
                                       'caption': caption,
                                       'parse_mode': parse_mode,
                                       'duration': duration,
                                       'performer': performer,
                                       'title': title,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()
