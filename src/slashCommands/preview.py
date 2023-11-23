# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Preview Slash Command
# // ---------------------------------------------------------------------

# // ---- Imports
import discord

from events import events
import ui
from helpers import general as helpers
from helpers import discord as discordHelpers

# // ---- Main
# // get vars
# discord-related
client: discord.Client = helpers.globals.get("client")
tree: discord.app_commands.CommandTree = helpers.globals.get("commandTree")

# // main command
# slash command
@tree.command(
    name = "preview",
    description = "Preview the welcome message for your server."
)
async def command(interaction: discord.Interaction):
    # // checks
    # setup
    checks = helpers.misc.failChecks()
    
    # permissions check
    if not discordHelpers.utils.hasPermissions(client, interaction.user, ["manage_guild"]):
        checks.fail("You need `manage_guild` permissions to run this command.")
        
    # failure message if failed
    failed, failureMessage = checks.result()
    
    if failed:
        return await interaction.response.send_message(
            embed = discordHelpers.embeds.failure(failureMessage),
            ephemeral = True
        )
        
    # // main
    await events.getSavedEvent("on_member_join").asyncFire(
        member = interaction.user
    )
    
    await interaction.response.send_message(
        embed = discordHelpers.embeds.success("Done! A preview of your server's welcome message has been sent in your server."),
        ephemeral = True
    )