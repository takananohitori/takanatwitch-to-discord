import asyncio
import requests
from twitchio.ext import commands

# ===== 設定 =====
TWITCH_NICK = "one0ftakana"
TWITCH_TOKEN = "oauth:qcmhl8h9rxo3g5fvjm74fzlbsiud05"
TWITCH_CHANNEL = "one0ftakana"

CHAT_WEBHOOK = "https://discord.com/api/webhooks/1477048823703404637/kFKMp0gP7drYVc75uABp2fCmtb07gHTS58C4QMV1cj-Y0W_gryuJqeap0hNaCUkw7Zm6"
NOTIFY_WEBHOOK = "https://discord.com/api/webhooks/1477773369595138122/iT0lG6ohXM0e5PFD8sjzO1tI6zfpC071aEC1i8LYr9vJ8wj4x8X4LAxf_cUF6B2fTsn4"
# =================

def send_to_discord(webhook, content):
    requests.post(webhook, json={"content": content})

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TWITCH_TOKEN,
            prefix="!",
            initial_channels=[TWITCH_CHANNEL]
        )

    async def event_ready(self):
        print(f"ログイン成功: {self.nick}")

    async def event_message(self, message):
        if message.echo:
            return

        content = f"[{message.author.name}] {message.content}"
        send_to_discord(CHAT_WEBHOOK, content)

bot = Bot()
bot.run()
