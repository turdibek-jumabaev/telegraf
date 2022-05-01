from typing import Optional, List
import requests
import json

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

    def sendDocument(self, chat_id: int, document: str,
                     caption: str = None, parse_mode: str = None,
                     disable_notification: bool = None, reply_to_message_id: int = None,
                     reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#senddocument
        """
        if parse_mode is None:
            parse_mode = self.parse_mode
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendDocument',
                                 data={'chat_id': chat_id,
                                       'document': document,
                                       'caption': caption,
                                       'parse_mode': parse_mode,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendSticker(self, chat_id: int, sticker: str,
                    disable_notification: bool = None, reply_to_message_id: int = None,
                    reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendsticker
        """
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendSticker',
                                 data={'chat_id': chat_id,
                                       'sticker': sticker,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendVideo(self, chat_id: int, video: str,
                  duration: int = None, width: int = None, height: int = None,
                  caption: str = None, parse_mode: str = None,
                  supports_streaming: bool = None, disable_notification: bool = None,
                  reply_to_message_id: int = None, reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendvideo
        """
        if parse_mode is None:
            parse_mode = self.parse_mode
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendVideo',
                                 data={'chat_id': chat_id,
                                       'video': video,
                                       'duration': duration,
                                       'width': width,
                                       'height': height,
                                       'caption': caption,
                                       'parse_mode': parse_mode,
                                       'supports_streaming': supports_streaming,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendVoice(self, chat_id: int, voice: str,
                  caption: str = None, parse_mode: str = None,
                  duration: int = None, disable_notification: bool = None,
                  reply_to_message_id: int = None, reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendvoice
        """
        if parse_mode is None:
            parse_mode = self.parse_mode
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendVoice',
                                 data={'chat_id': chat_id,
                                       'voice': voice,
                                       'caption': caption,
                                       'parse_mode': parse_mode,
                                       'duration': duration,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendVideoNote(self, chat_id: int, video_note: str,
                      duration: int = None, length: int = None,
                      disable_notification: bool = None, reply_to_message_id: int = None,
                      reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendvideonote
        """
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendVideoNote',
                                 data={'chat_id': chat_id,
                                       'video_note': video_note,
                                       'duration': duration,
                                       'length': length,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendLocation(self, chat_id: int, latitude: float, longitude: float,
                     disable_notification: bool = None, reply_to_message_id: int = None,
                     reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendlocation
        """
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendLocation',
                                 data={'chat_id': chat_id,
                                       'latitude': latitude,
                                       'longitude': longitude,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendVenue(self, chat_id: int, latitude: float, longitude: float, title: str,
                  address: str, foursquare_id: str = None,
                  disable_notification: bool = None, reply_to_message_id: int = None,
                  reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendvenue
        """
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendVenue',
                                 data={'chat_id': chat_id,
                                       'latitude': latitude,
                                       'longitude': longitude,
                                       'title': title,
                                       'address': address,
                                       'foursquare_id': foursquare_id,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendContact(self, chat_id: int, phone_number: str, first_name: str,
                    last_name: str = None, disable_notification: bool = None,
                    reply_to_message_id: int = None, reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendcontact
        """
        if disable_notification is None:
            disable_notification = False
        if reply_to_message_id is None:
            reply_to_message_id = None
        if reply_markup is None:
            reply_markup = {}
        response = requests.post(f'{self.url}/sendContact',
                                 data={'chat_id': chat_id,
                                       'phone_number': phone_number,
                                       'first_name': first_name,
                                       'last_name': last_name,
                                       'disable_notification': disable_notification,
                                       'reply_to_message_id': reply_to_message_id,
                                       'reply_markup': json.dumps(reply_markup)})
        return response.json()

    def sendChatAction(self, chat_id: int, action: str) -> dict:
        """
        API: https://core.telegram.org/bots/api#sendchataction
        """
        response = requests.post(f'{self.url}/sendChatAction',
                                 data={'chat_id': chat_id,
                                       'action': action})
        return response.json()

    def getUserProfilePhotos(self, user_id: int, offset: int = None, limit: int = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#getuserprofilephotos
        """
        response = requests.post(f'{self.url}/getUserProfilePhotos',
                                 data={'user_id': user_id,
                                       'offset': offset,
                                       'limit': limit})
        return response.json()

    def getFile(self, file_id: str) -> dict:
        """
        API: https://core.telegram.org/bots/api#getfile
        """
        response = requests.post(f'{self.url}/getFile',
                                 data={'file_id': file_id})
        return response.json()

    def kickChatMember(self, chat_id: int, user_id: int, until_date: int = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#kickchatmember
        """
        response = requests.post(f'{self.url}/kickChatMember',
                                 data={'chat_id': chat_id,
                                       'user_id': user_id,
                                       'until_date': until_date})
        return response.json()

    def unbanChatMember(self, chat_id: int, user_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#unbanchatmember
        """
        response = requests.post(f'{self.url}/unbanChatMember',
                                 data={'chat_id': chat_id,
                                       'user_id': user_id})
        return response.json()

    def restrictChatMember(self, chat_id: int, user_id: int,
                           until_date: int = None, can_send_messages: bool = None,
                           can_send_media_messages: bool = None,
                           can_send_other_messages: bool = None,
                           can_add_web_page_previews: bool = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#restrictchatmember
        """
        if until_date is None:
            until_date = None
        if can_send_messages is None:
            can_send_messages = None
        if can_send_media_messages is None:
            can_send_media_messages = None
        if can_send_other_messages is None:
            can_send_other_messages = None
        if can_add_web_page_previews is None:
            can_add_web_page_previews = None
        response = requests.post(f'{self.url}/restrictChatMember',
                                 data={'chat_id': chat_id,
                                       'user_id': user_id,
                                       'until_date': until_date,
                                       'can_send_messages': can_send_messages,
                                       'can_send_media_messages': can_send_media_messages,
                                       'can_send_other_messages': can_send_other_messages,
                                       'can_add_web_page_previews': can_add_web_page_previews})
        return response.json()

    def promoteChatMember(self, chat_id: int, user_id: int,
                          can_change_info: bool = None,
                          can_post_messages: bool = None,
                          can_edit_messages: bool = None,
                          can_delete_messages: bool = None,
                          can_invite_users: bool = None,
                          can_restrict_members: bool = None,
                          can_pin_messages: bool = None,
                          can_promote_members: bool = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#promotechatmember
        """
        if can_change_info is None:
            can_change_info = None
        if can_post_messages is None:
            can_post_messages = None
        if can_edit_messages is None:
            can_edit_messages = None
        if can_delete_messages is None:
            can_delete_messages = None
        if can_invite_users is None:
            can_invite_users = None
        if can_restrict_members is None:
            can_restrict_members = None
        if can_pin_messages is None:
            can_pin_messages = None
        if can_promote_members is None:
            can_promote_members = None
        response = requests.post(f'{self.url}/promoteChatMember',
                                 data={'chat_id': chat_id,
                                       'user_id': user_id,
                                       'can_change_info': can_change_info,
                                       'can_post_messages': can_post_messages,
                                       'can_edit_messages': can_edit_messages,
                                       'can_delete_messages': can_delete_messages,
                                       'can_invite_users': can_invite_users,
                                       'can_restrict_members': can_restrict_members,
                                       'can_pin_messages': can_pin_messages,
                                       'can_promote_members': can_promote_members})
        return response.json()

    def exportChatInviteLink(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#exportchatinvitelink
        """
        response = requests.post(f'{self.url}/exportChatInviteLink',
                                 data={'chat_id': chat_id})
        return response.json()

    def createChatInviteLink(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#createchatinvitelink
        """
        response = requests.post(f'{self.url}/createChatInviteLink',
                                 data={'chat_id': chat_id})
        return response.json()

    def editChatInviteLink(self, chat_id: int, invite_link: str) -> dict:
        """
        API: https://core.telegram.org/bots/api#editchatinvitelink
        """
        response = requests.post(f'{self.url}/editChatInviteLink',
                                 data={'chat_id': chat_id,
                                       'invite_link': invite_link})
        return response.json()

    def revokeChatInviteLink(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#revokechatinvitelink
        """
        response = requests.post(f'{self.url}/revokeChatInviteLink',
                                 data={'chat_id': chat_id})
        return response.json()

    def approveChatJoinRequest(self, chat_id: int, user_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#approvechatjoinrequest
        """
        response = requests.post(f'{self.url}/approveChatJoinRequest',
                                 data={'chat_id': chat_id,
                                       'user_id': user_id})
        return response.json()

    def declineChatJoinRequest(self, chat_id: int, user_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#declinechatjoinrequest
        """
        response = requests.post(f'{self.url}/declineChatJoinRequest',
                                 data={'chat_id': chat_id,
                                       'user_id': user_id})
        return response.json()

    def setChatAdministratorCustomTitle(self, chat_id: int, user_id: int, custom_title: str) -> dict:
        """
        API: https://core.telegram.org/bots/api#setchatadministratorcustomtitle
        """
        response = requests.post(f'{self.url}/setChatAdministratorCustomTitle',
                                 data={'chat_id': chat_id,
                                       'user_id': user_id,
                                       'custom_title': custom_title})
        return response.json()

    def setChatPermissions(self, chat_id: int, permissions: dict) -> dict:
        """
        API: https://core.telegram.org/bots/api#setchatpermissions
        """
        response = requests.post(f'{self.url}/setChatPermissions',
                                 data={'chat_id': chat_id,
                                       'permissions': permissions})
        return response.json()

    def setChatPhoto(self, chat_id: int, photo: str) -> dict:
        """
        API: https://core.telegram.org/bots/api#setchatphoto
        """
        response = requests.post(f'{self.url}/setChatPhoto',
                                 data={'chat_id': chat_id,
                                       'photo': photo})
        return response.json()

    def deleteChatPhoto(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#deletechatphoto
        """
        response = requests.post(f'{self.url}/deleteChatPhoto',
                                 data={'chat_id': chat_id})
        return response.json()

    def setChatTitle(self, chat_id: int, title: str) -> dict:
        """
        API: https://core.telegram.org/bots/api#setchattitle
        """
        response = requests.post(f'{self.url}/setChatTitle',
                                 data={'chat_id': chat_id,
                                       'title': title})
        return response.json()

    def setChatDescription(self, chat_id: int, description: str) -> dict:
        """
        API: https://core.telegram.org/bots/api#setchatdescription
        """
        response = requests.post(f'{self.url}/setChatDescription',
                                 data={'chat_id': chat_id,
                                       'description': description})
        return response.json()

    def pinChatMessage(self, chat_id: int, message_id: int, disable_notification: bool = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#pinchatmessage
        """
        if disable_notification is None:
            disable_notification = None
        response = requests.post(f'{self.url}/pinChatMessage',
                                 data={'chat_id': chat_id,
                                       'message_id': message_id,
                                       'disable_notification': disable_notification})
        return response.json()

    def unpinChatMessage(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#unpinchatmessage
        """
        response = requests.post(f'{self.url}/unpinChatMessage',
                                 data={'chat_id': chat_id})
        return response.json()

    def unpinAllChatMessages(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#unpinallchatmessages
        """
        response = requests.post(f'{self.url}/unpinAllChatMessages',
                                 data={'chat_id': chat_id})
        return response.json()

    def leaveChat(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#leavechat
        """
        response = requests.post(f'{self.url}/leaveChat',
                                 data={'chat_id': chat_id})
        return response.json()

    def getChat(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#getchat
        """
        response = requests.post(f'{self.url}/getChat',
                                 data={'chat_id': chat_id})
        return response.json()

    def getChatAdministrators(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#getchatadministrators
        """
        response = requests.post(f'{self.url}/getChatAdministrators',
                                 data={'chat_id': chat_id})
        return response.json()

    def getChatMembersCount(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#getchatmemberscount
        """
        response = requests.post(f'{self.url}/getChatMembersCount',
                                 data={'chat_id': chat_id})
        return response.json()

    def getChatMember(self, chat_id: int, user_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#getchatmember
        """
        response = requests.post(f'{self.url}/getChatMember',
                                 data={'chat_id': chat_id,
                                       'user_id': user_id})
        return response.json()

    def setChatStickerSet(self, chat_id: int, sticker_set_name: str) -> dict:
        """
        API: https://core.telegram.org/bots/api#setchatstickerset
        """
        response = requests.post(f'{self.url}/setChatStickerSet',
                                 data={'chat_id': chat_id,
                                       'sticker_set_name': sticker_set_name})
        return response.json()

    def deleteChatStickerSet(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#deletechatstickerset
        """
        response = requests.post(f'{self.url}/deleteChatStickerSet',
                                 data={'chat_id': chat_id})
        return response.json()

    def answerCallbackQuery(self, callback_query_id: str, text: str = None, show_alert: bool = None, url: str = None, cache_time: int = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#answercallbackquery
        """
        if text is None:
            text = None
        if show_alert is None:
            show_alert = None
        if url is None:
            url = None
        if cache_time is None:
            cache_time = None
        response = requests.post(f'{self.url}/answerCallbackQuery',
                                 data={'callback_query_id': callback_query_id,
                                       'text': text,
                                       'show_alert': show_alert,
                                       'url': url,
                                       'cache_time': cache_time})
        return response.json()

    def editMessageText(self, text: str, chat_id: int, message_id: int, inline_message_id: str = None, parse_mode: str = None, disable_web_page_preview: bool = None, reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#editmessagetext
        """
        if inline_message_id is None:
            inline_message_id = None
        if parse_mode is None:
            parse_mode = None
        if disable_web_page_preview is None:
            disable_web_page_preview = None
        if reply_markup is None:
            reply_markup = None
        response = requests.post(f'{self.url}/editMessageText',
                                 data={'text': text,
                                       'chat_id': chat_id,
                                       'message_id': message_id,
                                       'inline_message_id': inline_message_id,
                                       'parse_mode': parse_mode,
                                       'disable_web_page_preview': disable_web_page_preview,
                                       'reply_markup': reply_markup})
        return response.json()

    def editMessageCaption(self, caption: str, chat_id: int, message_id: int, inline_message_id: str = None, reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#editmessagecaption
        """
        if inline_message_id is None:
            inline_message_id = None
        if reply_markup is None:
            reply_markup = None
        response = requests.post(f'{self.url}/editMessageCaption',
                                 data={'caption': caption,
                                       'chat_id': chat_id,
                                       'message_id': message_id,
                                       'inline_message_id': inline_message_id,
                                       'reply_markup': reply_markup})
        return response.json()

    def editMessageReplyMarkup(self, chat_id: int, message_id: int, inline_message_id: str = None, reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#editmessagereplymarkup
        """
        if inline_message_id is None:
            inline_message_id = None
        if reply_markup is None:
            reply_markup = None
        response = requests.post(f'{self.url}/editMessageReplyMarkup',
                                 data={'chat_id': chat_id,
                                       'message_id': message_id,
                                       'inline_message_id': inline_message_id,
                                       'reply_markup': reply_markup})
        return response.json()

    def setMyCommands(self, commands: list) -> dict:
        """
        API: https://core.telegram.org/bots/api#setmycommands
        """
        response = requests.post(f'{self.url}/setMyCommands',
                                 data={'commands': commands})
        return response.json()

    def deleteMyCommands(self) -> dict:
        """
        API: https://core.telegram.org/bots/api#deletemycommands
        """
        response = requests.post(f'{self.url}/deleteMyCommands')
        return response.json()

    def setChatMenuButton(self, chat_id: int, text: str, url: str, hide: bool = None, **kwargs) -> dict:
        """
        API: https://core.telegram.org/bots/api#setchatmenubutton
        """
        if hide is None:
            hide = None
        response = requests.post(f'{self.url}/setChatMenuButton',
                                 data={'chat_id': chat_id,
                                       'text': text,
                                       'url': url,
                                       'hide': hide,
                                       **kwargs})
        return response.json()

    def getChatMenuButton(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#getchatmenubutton
        """
        response = requests.post(f'{self.url}/getChatMenuButton',
                                 data={'chat_id': chat_id})
        return response.json()

    def deleteChatMenuButton(self, chat_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#deletechatmenubutton
        """
        response = requests.post(f'{self.url}/deleteChatMenuButton',
                                 data={'chat_id': chat_id})
        return response.json()

    def getMyCommands(self) -> dict:
        """
        API: https://core.telegram.org/bots/api#getmycommands
        """
        response = requests.post(f'{self.url}/getMyCommands')
        return response.json()

    def answerInlineQuery(self, inline_query_id: str, results: list, cache_time: int = None, is_personal: bool = None, next_offset: str = None, switch_pm_text: str = None, switch_pm_parameter: str = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#answerinlinequery
        """
        if cache_time is None:
            cache_time = None
        if is_personal is None:
            is_personal = None
        if next_offset is None:
            next_offset = None
        if switch_pm_text is None:
            switch_pm_text = None
        if switch_pm_parameter is None:
            switch_pm_parameter = None
        response = requests.post(f'{self.url}/answerInlineQuery',
                                 data={'inline_query_id': inline_query_id,
                                       'results': results,
                                       'cache_time': cache_time,
                                       'is_personal': is_personal,
                                       'next_offset': next_offset,
                                       'switch_pm_text': switch_pm_text,
                                       'switch_pm_parameter': switch_pm_parameter})
        return response.json()

    def stopPoll(self, chat_id: int, message_id: int, reply_markup: dict = None) -> dict:
        """
        API: https://core.telegram.org/bots/api#stoppoll
        """
        if reply_markup is None:
            reply_markup = None
        response = requests.post(f'{self.url}/stopPoll',
                                 data={'chat_id': chat_id,
                                       'message_id': message_id,
                                       'reply_markup': reply_markup})
        return response.json()

    def deleteMessage(self, chat_id: int, message_id: int) -> dict:
        """
        API: https://core.telegram.org/bots/api#deletemessage
        """
        response = requests.post(f'{self.url}/deleteMessage',
                                 data={'chat_id': chat_id,
                                       'message_id': message_id})
        return response.json()
