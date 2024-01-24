from openai import OpenAI
import discord

intents = discord.Intents.default()
intents.message_content = True

token = 'discord_token'
openai_client = OpenAI(api_key="openai_key")


discord_client = discord.Client(intents=intents)

@discord_client.event
async def on_ready():
    print(f"We have logged in as {discord_client.user}")

@discord_client.event
async def on_message(message):
    if message.author == discord_client.user or message.channel.name != 'bot':
        return

    response = openai_client.chat.completions.create(
        messages=[{"role": "system",
                   "content": "You are an assistant."},
                  {"role": "user", "content": message.content}]
        ,model="gpt-3.5-turbo" )

    output = response.choices[0].message.content
    await message.channel.send(output)


discord_client.run(token)