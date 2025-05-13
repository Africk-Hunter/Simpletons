import random, json

class LocationManager:
    
    def __init__(self, transitions_file='./data/location_transitions.json'):
        with open(transitions_file) as f:
            self.transitions = json.load(f)["transitions"]
            
    def pick_random_location(self):
        location_list = ["Room", "Downtown", "Street", "Park", "Office", "Mall", "Restaurant", "City", "Neighborhood"]
        random.shuffle(location_list)
        return location_list[0]

    def change_location(self, character, time_manager):
        current_location = character.location

        location_list = ["Room", "Downtown", "Street", "Park", "Building", "Office", "Mall", "Restaurant", "City", "Neighborhood"]

        random.shuffle(location_list)

        for location in location_list:
            if location != current_location:
                current_location = location
                break
        
        for transition in self.transitions:
            if character.location == transition["leaving_location"] and current_location == transition["arriving_location"]:
                time_manager.create_current_time_for_printing(transition["message"].format(name=character.name))
                break

        character.location = current_location
        
    def go_to(self, character, location):
        character.location = location