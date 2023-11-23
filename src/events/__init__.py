# // ---------------------------------------------------------------------
# // ------- [Welcome Bot] Events Init
# // ---------------------------------------------------------------------

# // ---- Imports
import discord
from helpers.general import events
from helpers import general as helpers

# // ---- Variables
clientEvents = [ # thx chatgpt
    "on_ready", # used in main.py
    "on_connect",
    "on_disconnect",
    "on_resumed",
    "on_error",
    "on_socket_raw_receive",
    "on_socket_raw_send",
    "on_typing",
    "on_message",
    "on_message_delete",
    "on_bulk_message_delete",
    "on_raw_message_delete",
    "on_raw_bulk_message_delete",
    "on_message_edit",
    "on_raw_message_edit",
    "on_reaction_add",
    "on_raw_reaction_add",
    "on_reaction_remove",
    "on_raw_reaction_remove",
    "on_reaction_clear",
    "on_raw_reaction_clear",
    "on_private_channel_delete",
    "on_private_channel_create",
    "on_private_channel_update",
    "on_private_channel_pins_update",
    "on_guild_channel_delete",
    "on_guild_channel_create",
    "on_guild_channel_update",
    "on_guild_channel_pins_update",
    "on_guild_integrations_update",
    "on_webhooks_update",
    "on_member_join",
    "on_member_remove",
    "on_member_update",
    "on_user_update",
    "on_guild_join",
    "on_guild_remove",
    "on_guild_update",
    "on_guild_role_create",
    "on_guild_role_delete",
    "on_guild_role_update",
    "on_guild_emojis_update",
    "on_raw_socket_open",
    "on_raw_socket_close",
    "on_raw_socket_discover",
    "on_voice_state_update",
    "on_member_ban",
    "on_member_unban",
    "on_invite_create",
    "on_invite_delete",
    "on_group_join",
    "on_group_remove",
    "on_relationship_add",
    "on_relationship_remove",
    "on_application_command_error",
    "on_guild_available",
    "on_guild_unavailable",
    "on_interaction_create",
    "on_integrations_update",
    "on_stage_instance_create",
    "on_stage_instance_delete",
    "on_stage_instance_update",
    "on_thread_join",
    "on_thread_remove",
    "on_thread_update",
    "on_thread_list_sync",
    "on_thread_member_update",
    "on_thread_members_update",
    "on_voice_server_update",
    "on_presence_update",
    "on_message_create",
    "on_invite_create",
    "on_invite_delete",
    "on_socket_response",
    "on_socket_raw_receive",
    "on_socket_raw_send",
    "on_socket_disconnect",
    "on_socket_connect",
    "on_message_delete_bulk",
    "on_reaction_clear_emoji",
    "on_application_command_create",
    "on_application_command_update",
    "on_application_command_delete",
    "on_group_join",
    "on_group_remove",
    "on_guild_available",
    "on_guild_unavailable",
    "on_stage_instance_create",
    "on_stage_instance_delete",
    "on_stage_instance_update",
    "on_thread_create",
    "on_thread_update",
    "on_thread_delete",
    "on_thread_list_sync",
    "on_thread_member_update",
    "on_thread_members_update",
    "on_thread_delete",
    "on_thread_list_sync",
    "on_thread_member_update",
    "on_thread_members_update",
    "on_voice_server_update",
    "on_voice_state_update",
    "on_button_click",
    "on_dropdown_menu",
]

# // ---- Main
async def setup(client: discord.Client):
    # register events
    for event in clientEvents:
        # save event
        savedEvent = events.event(event).save()

        # listen for the actual discord event
        async def callback(*args, **kwargs):
            # notify
            helpers.prettyprint.info(f"{event} was called.\nArgs: {str(args)}\nKeyword Args: {str(kwargs)}")
            
            # fire event
            await savedEvent.asyncFire(*args, **kwargs)
        
        callback.__name__ = event
        client.event(callback)
    
    # event listeners
    from . import on_member_join
    from . import on_message
    from . import on_ready