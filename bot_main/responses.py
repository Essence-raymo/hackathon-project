import re
from random import choice, randint


# we will add users to a database to create a "profile" for them based on their input
def register_user() -> str:
    return True

# intial message that bot will send once it joins a server
def manual() -> str:
      
      return """**Please enter your skills in the format below to register your profile!**

        **Format:**
        Languages: [list the programming languages you know, separated by commas];
        Skill Level: [your skill level: Beginner, Intermediate, or Advanced];
        Areas of Interest: [list your interests, separated by commas];
        Time Zone: [your time zone, e.g., EST, PST, GMT+2]; 
        Availability: [general days/times you're available, e.g., Weekdays after 6 PM]; 



        **Example:**
        Languages: Python, JavaScript, C++; Skill Level: Intermediate; 
        Areas of Interest: Web Development, AI, Game Development; 
        Time Zone: EST; Availability: 
        Weekdays after 6 PM, Weekends flexible

        """


# creating bot responses
def get_response(user_input: str) -> str:
    #checks the number of catagorizes sent
    lowered: str = user_input.lower()
    if vaild_entry(lowered):
        return "Thank you for your response it is being processed now"
    elif lowered == '':
        return "Well, you are awfully silent..."
    elif 'hello' in lowered:
        return "Hello There!"
    else:
        return "Something's not right with your entry check it and try again"
    
def vaild_entry(str):
    entry = str
    regexp = "languages: .+; skill level: .+; areas of interest: .+; time zone: .+" #regular exspression
    match = re.match(regexp, entry)
    if match:
        return True
    else: 
        return False
        