import io
import os
from random import choice, randint
from PIL import Image as IM
from telethon.tl.types import DocumentAttributeFilename
from wand.image import Image
from .. import loader, utils
@loader.tdsclass
DistortMod(loader.Module):"""Stickers or photo distort""" strings = { "name": "Distort", "bad_input": "<b>Reply to image or stick!</b>", "processing": "<b>Distorting...</b>", "bad_input_tgs": "<b>Reply to animated sticker</b>", } async def client_ready(self, client, db): self.client = client

