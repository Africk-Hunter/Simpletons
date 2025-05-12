import random
import time
import json

def advance_time(current_time):
    if current_time == 1440:
        current_time = 0
    else:
        current_time += 1
        
    time.sleep(.25)
    return current_time

class Character:

    def __init__(self, name, traits, action_timeout): # Constructor (initializer)
        self.name = name
        self.traits = traits
        self.action_timeout = action_timeout

    def decrement_action_timeout(self):
        self.action_timeout -= 1

def create_random_character():
    names = ['Hunter', 'Jimothy', 'Bob', 'Aniyah', 'Drew', 'Phoebe', 'Microwave']
    traits = ['clumsy', 'courageous', 'lazy', 'nonchalant', 'hyper' ]

    random.shuffle(traits)
    chosen_traits = traits[0: random.randint(1, 3)]

    character = Character(random.choice(names), chosen_traits, 3)
    print("Character Traits For " + character.name + ": " + str(character.traits))
    return character



def create_character(characters): ## Add handling for random or custom created characters maybe?
    characters.append(create_random_character())
    return

def stringify_minutes(minutes):
    if minutes < 10:
        minute_string = '0' + str(minutes)
        return minute_string
    else:
        minute_string = str(minutes)
        return minute_string

def create_current_time_for_printing(character, time, message):
    if time < 60:
        hour = 12
        minutes = int(time)
    else: 
        hour = int(time / 60)
        minutes = int((time - (60 * hour)))
    
    statement = "[" + str(hour) + ":" + stringify_minutes(minutes) + "] " + message
    print(statement)
    return


def is_valid_action(action, traits, time):

    if any(trait in action["excluded_traits"] for trait in traits):
        """ print('Has one of excluded traits: ', action["excluded_traits"]) """
        return False
    if not all(trait in traits for trait in action["required_traits"]) and action["required_traits"] != []:
        """ print('Does not have all required traits: ', action["required_traits"]) """
        return False
    return True

def pick_location(character, time):
    current_location = character.location

    location_list = ["Room", "Downtown", "Street", "Park", "Building", "Office", "Mall", "Restaurant", "City", "Neighborhood"]




def pick_action(character, time):
    character_traits = character.traits

    ## I should add a timeout value to every action, that timeout is what will be used as the characters new timeout. This makes it so certain actions take longer to do
    ## I think this would make it more 'realistic'. If someone were to brew coffee, a 30 minute timer before the next action would be reasonable. If they slept, a 30 minute timer would be too little
    with open('actions.json') as actions:
        json_actions = json.load(actions)
        random.shuffle(json_actions["actions"])
        
        """ print("\033[93mTrying For:\033[0m", character.name, "\033[93m(they are:\033[0m", character.traits, "\033[93m)\033[0m") """
        for action in json_actions["actions"]:
            if is_valid_action(action, character_traits, time):
                """ print("\033[92mMessage:\033[0m", action["message"].format(name=character.name)) """
                create_current_time_for_printing(character, time, action["message"].format(name=character.name))
                character.action_timeout = int(action["timeout"])
                break

def determine_character_actions(characters, time):
    for character in characters:
        if (character.action_timeout == 0) and (random.randint(1, 100) > 80):
            """ create_current_time_for_printing(character, time) """
            pick_action(character, time)
            """ character.reset_time_since_action() """
        else:
            if character.action_timeout != 0:
                """ print(character.name, "action timeout: ", character.action_timeout) """
                character.decrement_action_timeout()



def run_application():
    time = 0
    characters = []
    
    for i in range(2):
        create_character(characters)
    
    while time >= 0:
        
        determine_character_actions(characters, time)
        """ print(create_current_time_for_printing(characters[time], time), characters[time].print_characteristics()) """
        time = advance_time(time)


    # Initalize Characters
    # Option to Create Characters
    
    ## Time Engine
        ## Advance Time (Duh)
        ## Store current time in a variable in this function
        ## That variable is passed Down to the next function which will do something based on that time
        
    ## Schedule Handler:
        ## Characters are allotted X actions per hour
            ## Every tick (represetned as 60 tick in an hour) has a chance for an action to be done:
                ## If a character triggers an action, a pool is created for the character based on various conditions
                ## One option will be taken from the pool and displayed as an action.


if __name__ == '__main__':
    run_application()