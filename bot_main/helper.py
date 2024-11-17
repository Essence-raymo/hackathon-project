import re, os, json
from random import choice, randint

# grabs the programming languages the user inputted
def get_language(str):
    lowered = str.lower()
    split = lowered.split(';')
    index = split[0]
    lang_str = index[10:]
    languages = lang_str.split(',')
    return(languages)

# grabs the skill level the user inputted
def get_exp_level(str):
    lowered = str.lower()
    split = lowered.split(';')
    index = split[1]
    exp_level = index[14:]
    return(exp_level)  

# grabs the areas of interest the user inputted
def get_areas_of_interest(str):
    lowered = str.lower()
    split = lowered.split(';')
    index = split[2]
    aoi_str = index[19:]
    aoi = aoi_str.split(',')
    return(aoi)

# grabs the time zone the user inputted
def get_time_zone(str):
    lowered = str.lower()
    split = lowered.split(';')
    index = split[3]
    time_zone = index[11:]
    return(time_zone)  

# creates a dictionary from the get functions above
# dictionary will be added to json database
def sort_entryToDicFormat(username,contents):
    keys = ['Username', 'Languages', 'skill level', 'areas of interest', 'time zone']
    values = [username, get_language(contents), get_exp_level(contents), get_areas_of_interest(contents), get_time_zone(contents)]
    mydictionary = dict(zip(keys, values))
    return mydictionary

# checks if user is already in database
def checkIfUsernameAlreadyExists(fileData, newEntry):
    for entry in fileData:
        if entry["username"] == newEntry["username"]:
            return True
    return False

# dumps the user dictionaries into the json file (this builds our database)
def load_json(dict):
    try:
        file_path = os.path.join(os.path.dirname(__file__), "database.json")
        with open(file_path, 'r') as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("JSON file does not contain a list at the root.")


        data.append(dict)

    except FileNotFoundError:

        data = [dict]


    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
        
# debuggingggg

# message  = "Languages: Python, JavaScript, C++; Skill Level: Intermediate; Areas of Interest: Web Development, AI, Game Development; Time Zone: EST"
# print(get_language(message))
# print(get_exp_level(message))
# print(get_areas_of_interest(message))
# print(get_time_zone(message))
# print(sort_entryToDicFormat('testing', message))
# load_json(sort_entryToDicFormat('testing', message))
# load_json(sort_entryToDicFormat('testing2', message))
# load_json(sort_entryToDicFormat('testing3', message))
