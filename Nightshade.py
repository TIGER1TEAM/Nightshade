import os

import discord

# Enable necessary intents
intents = discord.Intents.default()
intents.message_content = True  # Allow access to message content
intents.messages = True  # Listen to messages in guilds
intents.members = True
intents.members = True  # Required to access member roles

user_roles = []


# Initialize client with intents
client = discord.Client(intents=intents)

TARGET_CHANNEL_IDS = [1126199842734080032, 1300875592979316756]

@client.event
async def on_ready():
    channel = client.get_channel(1329585935373041745)  # Example channel ID
    if channel:
        await channel.send('Nightshade: Online')
        await channel.send('AP© 2025')
        await channel.send('Built by: TIGER TEAM')
        await channel.send('Powerd by: replit')
        await channel.send('Use bot panel for info and tests')
        await channel.send('SYSTEM: READY')
        await channel.send('Use !bot for intro')
        await channel.send('Use !cmd for commands')
        await channel.send('Use !ngt for registration')

print(f'Logged in as {client.user}')
print("DEBUG: RUNNING")
print("Actions listed below")

@client.event
async def on_message(message):
    if message.author == client.user:  # Prevent the bot from responding to itself
        return

    print(f"Message received: {message.content}")  # Log all received messages

    # Only proceed for messages from a guild text channel
    if isinstance(message.channel, discord.TextChannel):
        # Fetch the roles of the author
        user_roles = [role.name for role in message.author.roles]
    #    print(f"User {message.author.name} has roles: {user_roles}")
    

    if message.channel.id == 1329585935373041745:


        if message.content == '!rcv':  # Check for the exact command
            await message.channel.send('DEBUG: RUNNING')

        if message.content == '!where':  # Check for the exact command
            await message.channel.send('Welcome to the #bot-panel!')
            await message.channel.send('Here you can manage the bot and get more info.')
            await message.channel.send('To see all of the current commands, use !cmd.')


        if message.content == '!test':  # Check for the exact command
            await message.channel.send('TEXT')

        if message.content == '!cmd':  # Check for the exact command
            await message.channel.send('COMMAND LIST:')
            await message.channel.send('!rcv: Debug check')
            await message.channel.send('!where: Gives info on the panel')
            await message.channel.send('!test: Test command')
            await message.channel.send('!cmd: Shows command list')
            await message.channel.send('!bot: into')
            await message.channel.send('$tst: Global test cmd')
            await message.channel.send('!id: Shows role')
            await message.channel.send('!ngt: Shows registration and info')

        if message.content == '!ngt':  # Check for the exact command
            await message.channel.send('AP© 2025')
            await message.channel.send('Built by: TIGER-TEAM')
            await message.channel.send('Powerd by: replit')
            await message.channel.send('Language: python')
            await message.channel.send('Manager: tigerteam')
            await message.channel.send('Contact for info')
            await message.channel.send('Instagram: tigerteam900')
            await message.channel.send('Origin server: TIGER-TEAM CENTRAL')
            await message.channel.send('Ver: 1.17.2025')

        if message.content == '!bot':  # Check for the exact command
            await message.channel.send('Hi, im Nightshade!')
            await message.channel.send('I was made by TIGER TEAM and powerd by replit.')
            await message.channel.send('Use the command !where to explain the panel.')
            await message.channel.send('Use the command !cmd for the command list.')
            await message.channel.send('Use the command !help for more info.')
            await message.channel.send('Use !test to check serever respone.')
            await message.channel.send('Use !rcv to see if I am still running.')
            await message.channel.send('Enjoy!')

    elif message.channel.id in TARGET_CHANNEL_IDS:
            if message.content == '$tst':  # Check for the exact command
                await message.channel.send('RECEVE')

            if "!" in message.content.lower():
                user_roles = [role.name for role in message.author.roles]  
            if message.content == '!rcv':  # Check for the exact command
                await message.channel.send('DEBUG: RUNNING')

            if message.content == '!id':  # Check for the exact command
                user_roles = [role.name for role in message.author.roles]
                if "TIGER-TEAM" in user_roles:  
                    await message.channel.send('ID: TIGER-TEAM')

                user_roles = [role.name for role in message.author.roles]
                if "OP" in user_roles:  # Replace "Admin" with your desired role name
                    await message.channel.send('ID: OP')

            if message.content == '!bot':  # Check for the exact command
                await message.channel.send('Hi, im Nightshade!')
                await message.channel.send('Made by TIGER TEAM, powerd by replit.')
                await message.channel.send('Use the command !cmd for the command list.')
                await message.channel.send('Use the command !help for more info.')
                await message.channel.send('Use !test to check serever respone.')
                await message.channel.send('Use !rcv to see if I am still running.')
                await message.channel.send('Use the bot panel for more commands.')

    else:
        await message.channel.send("ERR")

client.run(os.getenv('DISCORD_BOT_TOKEN'))