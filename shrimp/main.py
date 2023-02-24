import discord
import tokenEncrypt


class MyClient(discord.Client):
    async def on_ready(self):
        await tree.sync(guild=discord.Object(id=789111709989863445))
        print(f'Logged on as {self.user}!')


intents = discord.Intents.default()

client = MyClient(intents=intents)

tree = discord.app_commands.CommandTree(client)


@tree.command(name="commandname", description="My first application Command", guild=discord.Object(id=12417128931))
async def first_command(interaction):
    await interaction.response.send_message("Hello!")


client.run(token=tokenEncrypt.get())


if __name__ == "__main__":
    ...
