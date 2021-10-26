import os
import time
import asyncio
import datetime
import numpy as np
import transformers
from sample_config import Config
from pyrogram import Client, filters

class ChatBot():
    def __init__(self, name):
        print("----- Starting up", name, "-----")
        self.name = name

@Client.on_message(filters.private)
async def ai(bot, update):
  ai = ChatBot(name="dev")
  nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
  os.environ["TOKENIZERS_PARALLELISM"] = "true"
  bot.send_message("Hi Sir")
  
