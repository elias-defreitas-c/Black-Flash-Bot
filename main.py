from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True  
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    username: str = str(message.author)
    if not user_message:
        print('(Message was empty because intents were not enabled properly)')
        return

    is_valid = user_message[0] == '#'
    if is_valid:
        user_message = user_message[1:]

    try:
        if is_valid:
            response: str = get_response(user_message, username)
            if response:
                await message.channel.send(response)
            else:
                print('Response was empty, not sending a message.')
    except Exception as e:
        print(f'Error sending message: {e}')


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()
