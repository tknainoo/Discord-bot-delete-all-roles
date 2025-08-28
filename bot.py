import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Required to manage roles
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Step 1: Ask for confirmation
@bot.command()
@commands.has_permissions(administrator=True)
async def delroles(ctx):
    await ctx.send(
        "⚠️ Are you sure you want to delete **ALL roles** in this server?\n"
        "Type `!confirmdel` within 30 seconds to continue."
    )

    def check(m):
        return m.author == ctx.author and m.content.lower() == "!confirmdel"

    try:
        msg = await bot.wait_for("message", timeout=30.0, check=check)
        if msg:
            await delete_all_roles(ctx)
    except:
        await ctx.send("❌ Confirmation timed out. No roles were deleted.")

# Step 2: Actual deletion function
async def delete_all_roles(ctx):
    guild = ctx.guild
    deleted = 0

    for role in guild.roles:
        try:
            if role.name != "@everyone" and role < guild.me.top_role:
                await role.delete()
                deleted += 1
        except Exception as e:
            print(f"Could not delete {role.name}: {e}")

    await ctx.send(f"✅ Deleted {deleted} roles successfully.")

bot.run("YOUR_BOT_TOKEN")
