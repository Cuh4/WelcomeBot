# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Discord Utils
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

# // ---- Functions
# // Permissions/Roles
def hasPermissions(client: discord.Client, member: discord.Member, permissions: list[str]):
    count = 0

    for permission in permissions:
        if getattr(member.guild_permissions, permission, False):
            count += 1
            
    return count == len(permissions) or member.guild_permissions.administrator or isCreator(client, member)
        
def isCreator(client: discord.Client, user: discord.User):
    return client.application.owner == user

def isAdministrator(member: discord.Member):
    return member.guild_permissions.administrator

def hasRole(member: discord.Member, role_id: int):
    if member.get_role(role_id):
        return True
    
    return False

# // String
def formatTimestamp(timestamp: int|float, mode: str = "F"):
    return f"<t:{int(timestamp)}:{mode}>"

def truncateIfTooLong(inp: str, max: int, endPartIfLong: str = ""):
    if len(inp) > max:
        return inp[0:max - len(endPartIfLong)] + endPartIfLong

    return inp

def stripMarkdown(msg: str):
    msg = msg.replace("`", "\\`") # escape code/highlight
    msg = msg.replace("*", "\\*") # escape italics/bold
    msg = msg.replace("~", "\\~") # escape strikethrough
    msg = msg.replace("_", "\\_") # escape underline
    msg = msg.replace("#", "\\#") # escape title
    msg = msg.replace("[", "\\[").replace("]", "\\]").replace("(", "\\(").replace(")", "\\)") # escape hyperlinks
    return msg

def stripHighlightMarkdown(msg: str):
    return msg.replace("`", "'")
 
def formattedName(user: discord.User):
    return user.name if user.discriminator == "0" else f"{user.name}#{user.discriminator}" # supports discord's new username system

def mentionUser(user: discord.User):
    return user.mention # was previously f"<@{user.id}>". i did not know the mention property existed

def mentionChannel(channel: discord.TextChannel|discord.VoiceChannel|discord.ForumChannel):
    return channel.mention # was previously f"<#{channel.id}>". i did not know the mention property existed

def linkUser(user: discord.User):
    return f"https://discord.com/users/{user.id}"

# // Other
def isMentioned(mentionedUsers: list[discord.User], who: discord.User):
    for i in mentionedUsers:
        if i == who:
            return True