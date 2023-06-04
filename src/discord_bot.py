"""
https://realpython.com/how-to-make-a-discord-bot-python/#creating-a-guild

"""
import os


import discord
from discord.ext import tasks
from dotenv import load_dotenv


from src.models import (
    JacquesChiracSpeechModel2,
    generate_chorus
)


load_dotenv(".env")


class DiscordBot:
    def __init__(self):
        self.client = discord.Client(intents=discord.Intents.all())
        self.model = JacquesChiracSpeechModel2(chorus=generate_chorus())

    def run(self):
        @self.client.event
        async def on_ready():
            for guild in self.client.guilds:
                if guild.name == os.getenv("DISCORD_GUILD"):
                    break
            print(f"{self.client.user} is connected to the following guild: {guild.name}.")
            members = [member.name for member in guild.members]
            print(f"Guild Members: {members}.")

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return

            if message.content.startswith("$hello"):
                await message.channel.send("Hello world!")

            if message.content.startswith("$generate_quote"):
               generated_sentence = self.model.generate_sentence()
               while not generated_sentence:
                   print(generated_sentence)
                   generated_sentence = self.model.generate_sentence()
               await message.channel.send(generated_sentence)

        self.client.run(os.getenv("DISCORD_TOKEN"))


if __name__ == "__main__":
    client = DiscordBot()
    client.run()
