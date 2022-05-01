import aiohttp
import asyncio


class AIOTelegraf:

    def __init__(self, token: str, parse_mode: str = 'html'):
        self.token = token
        self.parse_mode = parse_mode
        self.url = f'https://api.telegram.org/bot{self.token}/'

    async def getMe(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}getMe') as resp:
                return await resp.json()

    async def getUpdates(self, offset: int = None, limit: int = None, timeout: int = None, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}getUpdates', params={
                'offset': offset,
                'limit': limit,
                'timeout': timeout,
                **kwargs
            }) as resp:
                return await resp.json()

    async def forwardMessage(self, chat_id: int, from_chat_id: int, message_id: int, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}forwardMessage', data={
                'chat_id': chat_id,
                'from_chat_id': from_chat_id,
                'message_id': message_id,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendMessage(self, chat_id: int, text: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendMessage', data={
                'chat_id': chat_id,
                'text': text,
                'parse_mode': self.parse_mode,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendPhoto(self, chat_id: int, photo: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendPhoto', data={
                'chat_id': chat_id,
                'photo': photo,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendAudio(self, chat_id: int, audio: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendAudio', data={
                'chat_id': chat_id,
                'audio': audio,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendDocument(self, chat_id: int, document: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendDocument', data={
                'chat_id': chat_id,
                'document': document,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendSticker(self, chat_id: int, sticker: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendSticker', data={
                'chat_id': chat_id,
                'sticker': sticker,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendVideo(self, chat_id: int, video: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendVideo', data={
                'chat_id': chat_id,
                'video': video,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendVoice(self, chat_id: int, voice: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendVoice', data={
                'chat_id': chat_id,
                'voice': voice,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendVideoNote(self, chat_id: int, video_note: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendVideoNote', data={
                'chat_id': chat_id,
                'video_note': video_note,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendLocation(self, chat_id: int, latitude: float, longitude: float, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendLocation', data={
                'chat_id': chat_id,
                'latitude': latitude,
                'longitude': longitude,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendVenue(self, chat_id: int, latitude: float, longitude: float, title: str, address: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendVenue', data={
                'chat_id': chat_id,
                'latitude': latitude,
                'longitude': longitude,
                'title': title,
                'address': address,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendContact(self, chat_id: int, phone_number: str, first_name: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendContact', data={
                'chat_id': chat_id,
                'phone_number': phone_number,
                'first_name': first_name,
                **kwargs
            }) as resp:
                return await resp.json()

    async def sendChatAction(self, chat_id: int, action: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}sendChatAction', data={
                'chat_id': chat_id,
                'action': action
            }) as resp:
                return await resp.json()

    async def getUserProfilePhotos(self, user_id: int, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}getUserProfilePhotos', params={
                'user_id': user_id,
                **kwargs
            }) as resp:
                return await resp.json()

    async def getFile(self, file_id: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}getFile', params={
                'file_id': file_id
            }) as resp:
                return await resp.json()

    async def kickChatMember(self, chat_id: int, user_id: int, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}kickChatMember', data={
                'chat_id': chat_id,
                'user_id': user_id,
                **kwargs
            }) as resp:
                return await resp.json()

    async def unbanChatMember(self, chat_id: int, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}unbanChatMember', data={
                'chat_id': chat_id,
                'user_id': user_id
            }) as resp:
                return await resp.json()

    async def restrictChatMember(self, chat_id: int, user_id: int, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}restrictChatMember', data={
                'chat_id': chat_id,
                'user_id': user_id,
                **kwargs
            }) as resp:
                return await resp.json()

    async def promoteChatMember(self, chat_id: int, user_id: int, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}promoteChatMember', data={
                'chat_id': chat_id,
                'user_id': user_id,
                **kwargs
            }) as resp:
                return await resp.json()

    async def exportChatInviteLink(self, chat_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}exportChatInviteLink', data={
                'chat_id': chat_id
            }) as resp:
                return await resp.json()

    async def setChatPhoto(self, chat_id: int, photo: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}setChatPhoto', data={
                'chat_id': chat_id,
                'photo': photo
            }) as resp:
                return await resp.json()

    async def deleteChatPhoto(self, chat_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}deleteChatPhoto', data={
                'chat_id': chat_id
            }) as resp:
                return await resp.json()

    async def setChatTitle(self, chat_id: int, title: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}setChatTitle', data={
                'chat_id': chat_id,
                'title': title
            }) as resp:
                return await resp.json()

    async def setChatDescription(self, chat_id: int, description: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}setChatDescription', data={
                'chat_id': chat_id,
                'description': description
            }) as resp:
                return await resp.json()

    async def pinChatMessage(self, chat_id: int, message_id: int, disable_notification: bool = False):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}pinChatMessage', data={
                'chat_id': chat_id,
                'message_id': message_id,
                'disable_notification': disable_notification
            }) as resp:
                return await resp.json()

    async def unpinChatMessage(self, chat_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}unpinChatMessage', data={
                'chat_id': chat_id
            }) as resp:
                return await resp.json()

    async def leaveChat(self, chat_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}leaveChat', data={
                'chat_id': chat_id
            }) as resp:
                return await resp.json()

    async def getChat(self, chat_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}getChat', params={
                'chat_id': chat_id
            }) as resp:
                return await resp.json()

    async def getChatAdministrators(self, chat_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}getChatAdministrators', params={
                'chat_id': chat_id
            }) as resp:
                return await resp.json()

    async def getChatMembersCount(self, chat_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}getChatMembersCount', params={
                'chat_id': chat_id
            }) as resp:
                return await resp.json()

    async def getChatMember(self, chat_id: int, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}getChatMember', params={
                'chat_id': chat_id,
                'user_id': user_id
            }) as resp:
                return await resp.json()

    async def answerCallbackQuery(self, callback_query_id: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}answerCallbackQuery', data={
                'callback_query_id': callback_query_id,
                **kwargs
            }) as resp:
                return await resp.json()

    async def editMessageText(self, chat_id: int, message_id: int, text: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}editMessageText', data={
                'chat_id': chat_id,
                'message_id': message_id,
                'text': text,
                **kwargs
            }) as resp:
                return await resp.json()

    async def editMessageCaption(self, chat_id: int, message_id: int, caption: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}editMessageCaption', data={
                'chat_id': chat_id,
                'message_id': message_id,
                'caption': caption,
                **kwargs
            }) as resp:
                return await resp.json()

    async def editMessageReplyMarkup(self, chat_id: int, message_id: int, reply_markup: str, **kwargs):
        async with aiohttp.ClientSession() as session:
            async with session.post(f'{self.url}editMessageReplyMarkup', data={
                'chat_id': chat_id,
                'message_id': message_id,
                'reply_markup': reply_markup,
                **kwargs
            }) as resp:
                return await resp.json()
