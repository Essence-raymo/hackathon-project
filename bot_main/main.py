# we need these imports to use certain features in our program
from typing import Final  # allows us to define constants that shouldn't change
import os  # lets us access environment variables
from discord import Intents, Client, Message  # discord library for building the bot
from dotenv import load_dotenv  # helps load environment variables from a .env file
from responses import get_response  # custom function to get a response for a user message
from responses import manual
from helper import *

#  loads token from a .env file so we can use them in our program
load_dotenv()

# getting the discord token from the .env file to authenticate our bot
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
# creating intents to specify what permissions or data the bot should listen to
intents: Intents = Intents.default()  # use default intents for the bot
intents.message_content = True  # allow the bot to read message content
# creating the bot client with the specified intents
client: Client = Client(intents=intents)



# STEP 2: MESSAGE FUNCTIONALITY
# this function will send a response to a user based on their message
async def send_message(message: Message, user_message: str) -> None:
    # if the user message is empty, stop and print a message in the console
    if not user_message:
        print("Message was empty")
        return 
    
    # check if the user wants to send a private message (indicated by a '?' at the start)
    is_private = user_message[0] == "?"
    
    # remove the '?' if the message is private
    if is_private:
        user_message = user_message[1:]
        
    # try to get a response and send it back to the user
    try:
        response: str = get_response(user_message)  # get the bot's reply
        # if the message is private, send it directly to the user; otherwise, send it in the channel
        await message.author.send(response) if is_private else await message.channel.send(response)
        
    # if something goes wrong, print the error in the console
    except Exception as e:
        print(e)
        
        
# STEP 3: HANDLING THE STARTUP FOR OUR BOT
# this event runs when the bot is ready and connected
@client.event
async def on_ready() -> None:
    # print a message to let us know the bot is running
    print(f'{client.user} is now running')
    

# STEP 4: HANDLING INCOMING MESSAGES
# this event runs every time the bot sees a new message
@client.event
async def on_message(message: Message) -> None:
    # ignore messages sent by the bot itself
    if message.author == client.user:
        return
    
    # get information about the message and who sent it
    username: str = str(message.author)  # the user who sent the message
    user_message: str = message.content  # the content of the message
    channel: str = str(message.channel)  # the channel where the message was sent
    
    # print the message details in the console for debugging
    print(f'[{channel}] {username}: "{user_message}"')
    # process the message and send a response
    await send_message(message, user_message)

# this function will send a message each time the bot joins a server
# the message will contain instructions on HOW to use the bot
@client.event
async def on_guild_join(guild):
    response: str = manual()  # response = initial message
    # iterate through servers
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(response)  # send intial message to the channel
        break

@client.event
async def on_member_join(member):
    response: str = manual()
    try:
        print(f'{member} has joined a server.')
        await member.send(embed=response)

    except Exception as e:
        print(f"Error: {e}")

# STEP 5: MAIN ENTRY POINT
# this function starts the bot
def main() -> None:
    # run the bot using the token we loaded earlier
    client.run(token=TOKEN)
    

# check if this file is the main program being run
if __name__ == '__main__':
    # if it is, call the main function to start the bot
    main()

