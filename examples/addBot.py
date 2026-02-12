import asyncio
import sys
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Allow running this file directly: "python examples/addBot.py"
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from client import Client
from slash.option import Option

bot = Client(user=os.getenv("BOT_ACCOUNT_NAME"), password=os.getenv("BOT_ACCOUNT_PASSWORD"))

@bot.event
async def on_ready():
    print("Bot is online!")

@bot.slash_command(
    name="add",
    description="Add two numbers",
    options=[
        Option("a", "int", "First number", required=True),
        Option("b", "int", "Second number", required=True)
    ]
)
async def add(ctx):
    result = int(ctx.args["a"]) + int(ctx.args["b"])
    print("Calculated result:", result)
    await ctx.respond(f"Result: {result}")

bot.run("wss://chats.katnip.org")
