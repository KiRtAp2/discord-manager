import logging
import sys
import re
import logger
import discord


client = discord.Client()
TOKEN = sys.argv[1]  # gets token from command line

# if TOKEN looks like a filename, read the file and overwtite TOKEN with the contents
# I'm not commiting any tokens to github again
if re.match(r'^/?([a-zA-Z0-9]+/)*[a-zA-Z0-9]+\.[a-zA-Z0-9]+', TOKEN):
    with open(TOKEN, 'r') as f:
        TOKEN = f.read()


if __name__ == '__main__':
    logger.init(level=logging.DEBUG)