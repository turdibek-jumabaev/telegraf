import requests
import json
import re

# Telegram API


class Telegraf:

    def __init__(self, token: str, parse_mode: str = 'html'):
        self.token = token
        self.parse_mode = parse_mode
        self.url = f'https://api.telegram.org/bot{self.token}'

    def get_updates(self, offset: int = None, timeout: int = None, limit: int = None):
        """
        Get updates from Telegram
        :param offset:
        :param timeout:
        :param limit:
        :return:
        """
        params = {}
        if offset:
            params['offset'] = offset
        if timeout:
            params['timeout'] = timeout
        if limit:
            params['limit'] = limit
        return requests.get(f'{self.url}/getUpdates', params=params).json()

    def get_me(self):
        """
        Get bot info
        :return:
        """
        return requests.get(f'{self.url}/getMe').json()

    def send_message(self, chat_id: int, text: str, parse_mode: str = None, disable_web_page_preview: bool = None,
                     disable_notification: bool = None, reply_to_message_id: int = None, reply_markup: dict = None):
        """
        Send message to chat
        :param chat_id:
        :param text:
        :param parse_mode:
        :param disable_web_page_preview:
        :param disable_notification:
        :param reply_to_message_id:
        :param reply_markup:
        :return:
        """
        params = {'chat_id': chat_id, 'text': text}
        if parse_mode:
            params['parse_mode'] = parse_mode
        if disable_web_page_preview:
            params['disable_web_page_preview'] = disable_web_page_preview
        if disable_notification:
            params['disable_notification'] = disable_notification
        if reply_to_message_id:
            params['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            params['reply_markup'] = json.dumps(reply_markup)
        # return json
        return requests.post(f'{self.url}/sendMessage', data=params).json()


# test
bot = Telegraf('5120220134:AAHPNbEYTaIW2I8X607M43M-LfvCZ-OiI8Y')
print(bot.get_me())
