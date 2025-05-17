import random, json

class LocationManager:
    
    def __init__(self, transitions_file='./data/location_transitions.json'):
        with open(transitions_file) as f:
            self.transitions = json.load(f)["transitions"]
            
    def find_location_with_need_type(self, action_list):
        random.shuffle(action_list)
        return action_list[0]["location"]

    def pick_random_location_from_list(self):
        location_list = ["Room", "Downtown", "Street", "Park", "Office", "Mall", "Restaurant", "City", "Neighborhood"]
        random.shuffle(location_list)
        return location_list[0]

    def print_location_change_message(self, character, new_location, time_manager):
        for transition in self.transitions:
            if character.location == transition["leaving_location"] and new_location == transition["arriving_location"]:
                time_manager.create_current_time_for_printing(transition["message"].format(name=character.name), character)
                break

    def change_location_at_random(self, character, time_manager):        
        new_location = character.location
        
        while new_location == character.location:
            new_location = self.pick_random_location_from_list()
        self.print_location_change_message(character, new_location, time_manager)

        character.location = new_location
        
    def go_to_location(self, character, new_location, time_manager):

        self.print_location_change_message(character, new_location, time_manager)
        character.location = new_location