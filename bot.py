import discord
import responses


# Send a private message
async def send_private_message(message, user_message):
    try:
        response = responses.handle_response(user_message)  # [1:] Removes the '?'
        await message.author.send(response)
    except Exception as e:
        print(e)


# Respond to message in current channel
async def respond_in_channel(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'YOUR_KEY'
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == client.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_private_message(message, user_message)
        else:
            await respond_in_channel(message, user_message)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
