from telethon import TelegramClient, events, sync
from dotenv import load_dotenv, dotenv_values
import os
import logging
import asyncio
import itertools
import random
from telethon.tl.functions.channels import GetFullChannelRequest

from telethon.tl.types import channels

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient("session_name", api_id, api_hash)
client.start()

GREETING_POST = """
🤝Благодарю за подписку!

В качестве подарка составил для тебя список самых полезных каналов для саморазвития.
   
🧠[OLYMPIA](https://t.me/+-FOEdpd-h-I1ZWYy) - все тонкости мужской психологии, раскрытие женских приемов манипуляции.

👁[Границы мужества](https://t.me/+WznZg97FDP80NjRi) - канал, вдохновляющий на преодоление жизненных вызовов и расширение границ собственных возможностей.
"""

# CHANNEl_ID = -1002061276906  # mine
CHANNEl_ID = -1002146384930  # pimp's


async def getAllChannelUsers():
    async for user in client.iter_participants(CHANNEl_ID):
        print(user.username)
    # channel_info = await client(GetFullChannelRequest(CHANNEl_ID))
    # users = channel_info.users
    # for user in users:
    #     print(user.first_name)


with client:
    client.loop.run_until_complete(main())

# Start the client and run the fetch_participants function
# with client:
#     client.loop.run_until_complete(fetch_participants())
#     participants = client.loop.run_until_complete(fetch_participants())
#
#     # Log the participants
#     for user_id, user_info in participants.items():
#         print(f"User ID: {user_id}")
#         print(user_info)
#         print("---")
