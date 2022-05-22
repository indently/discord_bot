import discord
import responses


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
            try:
                # Send a private message
                response = responses.handle_response(user_message[1:])  # [1:] Removes the '?'
                await message.author.send(response)
            except Exception as e:
                print("User has not allowed access to private messages.")
        else:
            # Send a message to the channel
            response = responses.handle_response(user_message)
            await message.channel.send(response)

    # Remember to run your bot with your personal TOKEN
    client.run(TOKEN)
