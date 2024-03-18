from telethon import TelegramClient, events, sync
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient("session_name", api_id, api_hash)

GREETING_POST = """
🤝Благодарю за подписку!

В качестве подарка составил для тебя список самых полезных каналов для саморазвития.
   
🧠[OLYMPIA](https://t.me/+-FOEdpd-h-I1ZWYy) - все тонкости мужской психологии, раскрытие женских приемов манипуляции.

👁[Границы мужества](https://t.me/+WznZg97FDP80NjRi) - канал, вдохновляющий на преодоление жизненных вызовов и расширение границ собственных возможностей.
"""


async def main():
    # Getting information about yourself
    # CHAT_ID = -1002061276906
    CHAT_ID = 749179973

    await client.send_message(CHAT_ID, GREETING_POST, link_preview=False)


with client:
    client.loop.run_until_complete(main())

# client.start()
