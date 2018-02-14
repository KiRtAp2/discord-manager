from logging import DEBUG as LOGGING_DEBUG
import sys
import re
import logger
import discord


logger.init(level=LOGGING_DEBUG)


client = discord.Client()
TOKEN = sys.argv[1]  # gets token from command line
# I'm not commiting it again


@client.event
async def on_message(msg):

    if msg.author==client.user:
        return


@client.event
async def on_ready():
    print("Logged in")
    logger.info("Up and running!")

client.run(TOKEN)
