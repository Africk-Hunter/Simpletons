import random
import time
import json

def advance_time(current_time):
    
    if current_time == 1440:
        current_time = 0
    else:
        current_time += 1
        
    time.sleep(1)
    return current_time

class Character:

    def __init__(self, name, traits, time_since_last_action): # Constructor (initializer)
        self.name = name
        self.traits = traits
        self.time_since_last_action = time_since_last_action
        
    def print_characteristics(self):
        return [self.name, self.traits]
    
    def get_time_since_action(self):
        return self.time_since_last_action

    def reset_time_since_action(self):
        
        self.time_since_last_action = 0
    def increment_time_since_action(self):
        self.time_since_last_action += 1
    

def create_random_character():
    names = ['Hunter', 'Jimothy', 'Bob', 'Aniyah', 'Drew', 'Phoebe', 'Microwave']
    traits = ['clumsy', 'courageous', 'lazy', 'nonchalant', 'hyper' ]

    random.shuffle(traits)
    chosen_traits = traits[0: random.randint(1, 3)]

    character = Character(random.choice(names), random.choice(chosen_traits), 0)
    print("Character Traits For " + character.name + ": " + character.traits)
    return character



def create_character(characters): ## Add handling for random or custom created characters maybe?
    characters.append(create_random_character())
    return



def create_current_time_for_printing(character, time):
    if time < 60:
        hour = 12
        minutes = int(time)
    else: 
        hour = int(time / 60)
        minutes = int((time - (time * hour)))
    
    statement = "[" + str(hour) + ":" + str(minutes) + "]"
    return statement


def is_valid_action(action, traits):
    print(action)
    if any(trait in action["excluded_traits"] for trait in traits):
        print('Has one of excluded traits: ', action["excluded_traits"])
        return False
    if not any(trait in action["required_traits"] for trait in traits):
        print('Does not have all required traits: ', action["required_traits"])
        return False
    return True

def pick_action(character):

    character_traits = character.traits
    print(character_traits)

    with open('actions.json') as actions:
        json_actions = json.load(actions)
        random.shuffle(json_actions)
        i = 0
        for action in json_actions:
            print(i, action)
            """ if is_valid_action(action, character_traits):
                print(action) """

    return


def determine_character_actions(characters, time):
    for character in characters:
        if (character.get_time_since_action() > 5) and (random.randint(1, 100) > 80):
            print(create_current_time_for_printing(character, time), character.name)
            pick_action(character)
            character.reset_time_since_action()
        else:
            character.increment_time_since_action()



def run_application():
    time = 0
    characters = []
    
    for i in range(5):
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