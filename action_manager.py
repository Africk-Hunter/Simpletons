import json, random, os
from context_manager import ContextManger

class ActionManager:
    def __init__(self, actions_dir='./data/actions'):
        
        self.actions = {}
        self.CM = ContextManger()
        
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

        if any(trait in action["excluded_traits"] for trait in traits):
            return False
        if location != action['location']:
            return False
        if not all(trait in traits for trait in action["required_traits"]) and action["required_traits"] != []:
            return False
        if action["id"] in done_actions:
            return False
        return True
                
    def pick_action_from_provided_list(self, character, action_list):
        random.shuffle(action_list)
        
        for action in action_list:
                if self.is_valid_action(character, action):
                    return action
    
    def determine_which_need_takes_priority(self, character):
        
        char_needs = character.needs
        priority_need = {"need": '', "priority_value": -1}
        
        for need, need_data in char_needs.items():
            score = (need_data["max_value"] - need_data["value"]) * need_data["priority_weight"]
        
            if score > priority_need["priority_value"]:
                priority_need["need"] = need
                priority_need["priority_value"] = score
          
        return priority_need["need"]
    
    def handle_action_picking(self, character, priority_need):
        
        action_list = self.get_actions(priority_need)
        picked_action = self.pick_action_from_provided_list(character, action_list)
        filled_action = self.CM.fill_action_context(character, picked_action)
        character.update_based_on_action(picked_action["timeout"], priority_need, picked_action["restore_value"])
        
        return filled_action
        