import json, random, os
from context_manager import ContextManger
from location_manager import LocationManager

class ActionManager:
    def __init__(self, time_manager, actions_dir='./data/actions'):
        
        self.actions = {}
        self.CM = ContextManger()
        self.LM = LocationManager()
        self.TM = time_manager
        
        for filename in os.listdir(actions_dir):
            filepath = os.path.join(actions_dir, filename)
            category = os.path.splitext(filename)[0]
            
            with open(filepath, 'r') as f:
                data = json.load(f)
                self.actions[category] = data.get("actions", [])

    def get_actions(self, category):
        return self.actions.get(category, [])
    
    def is_valid_action(self, character, action):
        traits = character.traits
        location = character.location
        done_actions = character.done_actions

        if action["id"] in done_actions:
            return False
        if location != action['location']:
            return False
        if any(trait in action["excluded_traits"] for trait in traits):
            return False
        if not all(trait in traits for trait in action["required_traits"]) and action["required_traits"] != []:
            return False

        return True
                
    def pick_action_from_provided_list(self, character, action_list):
        random.shuffle(action_list)
        
        for action in action_list:
                if self.is_valid_action(character, action):
                    return action
                
        return None
    
    def determine_which_need_takes_priority(self, character):
        
        char_needs = character.needs
        priority_need = {"need": '', "priority_value": -1}
        
        for need, need_data in char_needs.items():
            
            score = (need_data["max_value"] - need_data["value"]) * need_data["priority_weight"]

            if score > priority_need["priority_value"]:
                priority_need["need"] = need
                priority_need["priority_value"] = score
          
        return priority_need["need"]
    
    def find_location_for_need(self, action_list, character):
        new_location = self.LM.find_location_with_need_type(action_list)
        self.LM.go_to_location(character, new_location, self.TM)
        character.move_timeout = 60

    
    def handle_action_picking(self, character, priority_need):
        
        if character.current_location_time > 120:
            self.LM.change_location_at_random(character, self.TM)
            character.current_location_time = 0
            return None
        
        action_list = self.get_actions(priority_need)
        picked_action = self.pick_action_from_provided_list(character, action_list)
        
        while picked_action is None:
            if character.move_timeout != 0:
                action_list = self.get_actions('idle')
                picked_action = self.pick_action_from_provided_list(character, action_list)
            else:
                self.find_location_for_need(action_list, character)
                picked_action = self.pick_action_from_provided_list(character, action_list)
        
        filled_action = self.CM.fill_action_context(character, picked_action)
        character.update_based_on_action(picked_action["timeout"], priority_need, picked_action["restore_value"])
        
        return filled_action
        