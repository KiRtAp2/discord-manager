from logging import DEBUG as LOGGING_DEBUG
import sys

import basic_commands
import logger
import discord
import settings
import string_splitter

logger.init(level=LOGGING_DEBUG)


client = discord.Client()
TOKEN = sys.argv[1]  # gets token from command line
# I'm not commiting it again


@client.event
async def on_message(msg):

    if msg.author == client.user:
        return

    if msg.content.startswith(settings.COMMAND_PREFIX):

        cmd, args, kwargs = string_splitter.StringSplitter.get_command(msg.content[1:])
        if cmd is None:
            logger.error("Could not handle command")
            await client.send_message(msg.channel, "Command invalid.")
            return

        if cmd == "help":
            message = basic_commands.BasicHandler.get_help_str()
            await client.send_message(msg.channel, message)


@client.event
async def on_message_edit(before, after):
    if before.author == after.author:
        fmt = "SCUM! {author} edited their message: '{before}' to '{after}'"
        await client.send_message(after.channel,
                                  fmt.format(author=after.author, before=before.content, after=after.content))


@client.event
async def on_ready():
    print("Logged in")
    logger.info("Up and running!")


client.run(TOKEN)
