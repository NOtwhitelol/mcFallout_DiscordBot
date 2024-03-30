#main.py
import aiohttp
import os
from discord.ext import commands
from discord import Intents

import json
with open('config.json','r') as f:
    data = json.load(f)

class client(commands.Bot):
    def __init__(self,**options):
        super().__init__(
            command_prefix="-",
            intents = Intents.all(),
            application_id = 1223516391332646945,
            **options
        )
    
    async def setup_hook(self):
        self.session = aiohttp.ClientSession()
        #載入資料夾commands裡面的py檔案
        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'commands.{filename[:-3]}') #載入插件


    async def on_ready(self): #當bot準備好時執行(不保證是第一個執行)
        print('bot已上線')

if __name__ == "__main__":
   bot = client()
   bot.run(data['TOKEN'])
   