import io
import os
from random import choice, randint
from telethon.tl.types import DocumentAttributeFilename
from telethon.sync import TelegramClient, events
from .. import loader, utils

@loader.tds
class STTSMod(loader.Module):
  """Module for bot Silero TTS"""
  strings = { "name": "STTS"}
  async def client_ready(self, client, db):
    self.client = client
  async def sttscmd(self, message):
    """Используй .stts <текст(максимальная длина 500 символов)>"""
    text = utils.get_args_raw(message)
    chat_id = message.chat_id
    chat_uname = message.client.get_entity(chat_id).to_dict()['username']
    
    await message.client.send_message('silero_voice_bot', f'{text}')
    @message.client.on(events.NewMessage(chats='silero_voice_bot'))
    async def handler_new_message(event):
      await message.client.send_message(f'{chat_uname}', event.message)
    
    

