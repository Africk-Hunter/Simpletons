import random
import sys
import time

def advance_time(current_time):
    
    if time == 1440:
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
    chosen_traits = [traits[0: random.randint(1, 3)]]

    person = Character(random.choice(names), random.choice(chosen_traits), 0)
    return person

def create_character(characters):
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

def determine_character_actions(characters, time):
    for character in characters:
        if (character.get_time_since_action() > 5) and (random.randint(1, 100) > 80):
            print(create_current_time_for_printing(character, time), character.name)
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