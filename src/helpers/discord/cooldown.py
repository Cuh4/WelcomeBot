# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Discord Embeds
# // ---------------------------------------------------------------------

# // ---- Imports
import discord
import threading
import time

# // ---- Variables
cooldowns = {}

# // ---- Functions
def __handler(fullKey: str, duration: float|int):
    time.sleep(duration)
    cooldowns.pop(fullKey)

def __key(user: discord.User, key: str):
    return str(user.id) + key

def __hasCooldown(fullKey: str):
    return cooldowns.get(fullKey, None) != None

def cooldown(user: discord.User, time: float|int, key: str) -> bool:
    fullKey = __key(user, key)

    if __hasCooldown(fullKey):
       return True
   
    cooldowns[fullKey] = True

    threading.Thread(
        target = __handler,
        args = [fullKey, time]
    ).start()

    return False 