import io
import os
from random import choice, randint
from telethon.tl.types import DocumentAttributeFilename
from .. import loader, utils

@loader.tdsclass
STTSMod(loader.Module):
  """Module for bot Silero TTS"""
  strings = { "name": "STTS"}
  async def client_ready(self, client, db):
    self.client = client
  async def sttscmd(self, message):
    
    

