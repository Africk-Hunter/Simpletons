import random
from time_manager import TimeManager
from action_manager import ActionManager
from location_manager import LocationManager
from character import Character

class GameManager:
    def __init__(self):
        self.TM = TimeManager()
        self.AM = ActionManager()
        self.LM = LocationManager()
        self.characters = []
        self.colors = [ 32, 33, 34, 35, 36, 37]
        self.names = ['Hunter', 'Jimothy', 'Bob', 'Aniyah', 'Drew', 'Phoebe', 'Microwave']
    
    def select_from_and_update_array(self, array):
        return_value = random.choice(array)
        array.remove(return_value)
        return return_value

    def create_random_character(self):
        
        
        traits = ['clumsy']
        """ traits = [
            'clumsy', 'courageous', 'lazy', 'nonchalant', 'hyper',
            'easygoing', 'moody', 'paranoid', 'anxious', 'stoic',
            'irritable', 'methodical', 'impulsive', 'fidgety', 'obsessive',
            'distracted', 'friendly', 'aloof', 'observant', 'blunt',
            'shy', 'resourceful', 'neat', 'forgetful', 'stubborn', 'diligent'
        ] """

        random.shuffle(traits)
        chosen_traits = traits[0: random.randint(1, 3)]
        name = self.select_from_and_update_array(self.names)
        color = self.select_from_and_update_array(self.colors)

        character = Character(name, chosen_traits, 3, self.LM.pick_random_location_from_list(), [], color)
        print("Character Traits For " + character.name + ": " + str(character.traits), "They are located at:", character.location)
        self.characters.append(character)

    def determine_character_actions(self):
        for character in self.characters:
            if (character.action_timeout == 0) and (random.randint(1, 100) > 80):
                
                priority_need = self.AM.determine_which_need_takes_priority(character)
                filled_action = self.AM.handle_action_picking(character, priority_need, self.TM)
                self.TM.create_current_time_for_printing(filled_action, character)

            else:
                if character.action_timeout != 0:
                    character.decrement_action_timeout()
                    character.increment_current_location_time()

    def run(self):
        
        for _ in range(2):
            self.create_random_character()
            
        while True:
            self.determine_character_actions()
            self.TM.advance_time()

if __name__ == '__main__':
    gm = GameManager()
    gm.run()