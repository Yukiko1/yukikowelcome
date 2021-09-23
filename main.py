import discord, os

cid = os.getenv("CID")
intents = discord.Intents.all()
intents.members = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
  print("Hi")

@bot.event
async def on_member_join(member):
  guild = member.guild
  channel = bot.get_channel(int(cid))
  if channel is not None:
    embed = discord.Embed(title=f"ยินดีต้อนรับสู่เซิร์ฟเวอร์ **{guild.name}**\nขอให้อยู่ด้วยกันนานๆนะ", description=f"", color=discord.Color.from_rgb(153, 102, 255))
    embed.set_author(name = f"{member.name}#{member.discriminator}", icon_url = member.avatar_url)
    embed.set_image(url="https://i.pinimg.com/originals/06/80/81/068081ee5b913a47003a64f7233825fe.gif")
    try:
      await channel.send(embed=embed)
      print(f"<@!{member.id}> has joined the server")
    except:
      print("i can't do that")
  else:
      print("Failed to fetch channel")
      
@bot.event
async def on_member_remove(member):
  guild = member.guild
  channel = bot.get_channel(int(cid))
  if channel is not None:
    embed = discord.Embed(title=f"ได้ออกจากเซิร์ฟเวอร์ **{guild.name}** แล้ว\nหวังว่าจะได้มาพบกันอีกนะ", description=f"", color=discord.Color.from_rgb(153, 102, 255))
    embed.set_author(name = f"{member.name}#{member.discriminator}", icon_url = member.avatar_url)
    embed.set_image(url="https://i.imgur.com/ogeTrhI.gif")
    try:
      await channel.send(embed=embed)
      print(f"<@!{member.id}> has left the server")
    except:
      print("i can't do that")
  else:
      print("Failed to fetch channel")

token = os.environ.get("TOKEN")
bot.run(token)
