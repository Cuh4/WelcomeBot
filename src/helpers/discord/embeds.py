# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Discord Embeds
# // ---------------------------------------------------------------------

# // ---- Imports
import discord
import config

# // ---- Functions
def __setup(emoji: str, msg: str):
    if msg.find("\n") == -1: # no newlines, so this msg is just on one line
        msg = f"**{msg}**" # bolden msg as a result

    return f">>> {emoji} | {msg}"

def success(msg: str):
    embed = discord.Embed(
        description = __setup(":white_check_mark:", msg), 
        color = discord.Colour.from_rgb(0, 255, 0)
    )

    return embed

def failure(msg: str):
    embed = discord.Embed(
        description = __setup(":x:", msg), 
        color = discord.Colour.from_rgb(255, 0, 0)
    )

    return embed

def warning(msg: str):
    embed = discord.Embed(
        description = __setup(":warning:", msg), 
        color = discord.Colour.from_rgb(255, 125, 0)
    )

    return embed

def info(msg: str):
    embed = discord.Embed(
        description = __setup(":globe_with_meridians:", msg), 
        color = discord.Colour.from_rgb(0, 0, 255)
    )

    return embed

def load(msg: str):
    embed = discord.Embed(
        description = __setup(":timer:", msg), 
        color = discord.Colour.from_rgb(255, 255, 255)
    )

    return embed