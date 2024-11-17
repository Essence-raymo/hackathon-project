import re
from discord import Embed
from random import choice, randint
from main import *

# we will add users to a database to create a "profile" for them based on their input
def register_user() -> str:
    return True

# intial message that bot will send once it joins a server
def manual() -> str:
    embed = Embed (
        title= "Welcome to MatchMaking Bot! 🎉",
        description= ("Thank you for joining! Here's how to get started:\n\n"
                     "For your profile you will be entering: \n"
                     " __**Languages**__: [list the programming languages you know, separated by commas]; \n"

                     " __**Skill Level**__: [Your skill level: Beginner, Intermediate, or Advanced];\n"

                     " __**Areas of Interest**__: [List your interests, separated by commas];\n"

                     " __**Time Zone**__: [Your time zone, e.g., EST, PST, GMT+2];\n \n \n" 
                     "__**Answer in this format exactly, put all in one line.**__ \n" 
                     "Languages: Python, JavaScript, C++; Skill Level: Intermediate; Areas of Interest: Web Development, AI, Game Development; Time Zone: EST;"),

    
        color= 0x2F3136
        ) 

    return (embed)


# creating bot responses
def get_response(user_input: str) -> str:
    #checks the number of catagorizes sent
    lowered: str = user_input.lower()
    #if message is valid, return a  nice message 
    if vaild_entry(lowered):
        return "Thank you for your response it is being processed now"
    elif lowered == '':
        return "Well, you are awfully silent..."
    elif 'hello' in lowered:
        return "Hello There!"
    else:
        return "Something's not right with your entry check it and try again"

# validates the user message
def vaild_entry(str):
    # lowers message
    entry = str.lower()
    # regular expression to check formatting
    regexp = "languages: .+; skill level: .+; areas of interest: .+; time zone: .+" #regular exspression
    match = re.match(regexp, entry)
    if match:
        return True
    else: 
        return False
        
