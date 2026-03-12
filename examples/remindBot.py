import asyncio
import os

from dotenv import load_dotenv

from chats_py import Client, Option

load_dotenv()

bot = Client(user=os.getenv("BOT_ACCOUNT_NAME"), password=os.getenv("BOT_ACCOUNT_PASSWORD"))

@bot.event
async def on_ready():
    print("Reminder Bot is online!")

@bot.slash_command(
    name="remind",
    description="Set a reminder after a number of seconds",
    options=[
        Option("seconds", "int", "Time to wait in seconds", required=True),
        Option("message", "str", "Reminder message", required=True)
    ]
)
async def remind(ctx):
    seconds = int(ctx.args["seconds"])
    message = ctx.args["message"]

    if seconds <= 0:
        await ctx.respond("Time must be greater than 0 seconds.")
        return

    await ctx.respond(f"Reminder set for {seconds} seconds.")

    await asyncio.sleep(seconds)

    await ctx.respond(f"⏰ Reminder: {message}")

bot.run("wss://chats.katnip.org")
