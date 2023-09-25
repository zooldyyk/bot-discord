import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

@bot.event
async def on_member_update(before, after):
    role_to_remove_id_1 = 
    role_to_remove_id_2 = 
    role_to_remove_id_3 = 

    if role_to_remove_id_2 in [role.id for role in after.roles]:
        role_to_remove = discord.utils.get(after.roles, id=role_to_remove_id_1)
        if role_to_remove:
            await after.remove_roles(role_to_remove)
            print(f'Removed role {role_to_remove.name} from {after.display_name}')

    if role_to_remove_id_3 in [role.id for role in after.roles]:
        role_to_remove = discord.utils.get(after.roles, id=role_to_remove_id_2)
        if role_to_remove:
            await after.remove_roles(role_to_remove)
            print(f'Removed role {role_to_remove.name} from {after.display_name}')



