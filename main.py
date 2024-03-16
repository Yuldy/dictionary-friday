from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Load Token:
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Bot Setup
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return
    
    # Users can message privately
    # Question marks is message private
    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        # If channel is private, send it to author, or send it back to current channel
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    # We can change the exception later
    except Exception as e:
        print("An error has occured as ", e)


# Handling startup of bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

# Handling Incoming Messages
@client.event
async def on_message(message: Message) -> None:
    # Bot is the one who wrote the message
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel} {username}: "{user_message}"]')
    await send_message(message, user_message)

# Main entry point

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()