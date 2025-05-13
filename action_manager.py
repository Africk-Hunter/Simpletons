import json, random

class ActionManager:
    def __init__(self, actions_file='actions.json'):
        with open(actions_file) as f:
            self.actions = json.load(f)["actions"]
    
    def is_valid_action(self, character, action, time):
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
    
    def pick_action(self, character, time_manager):
        with open('actions.json') as actions:
            json_actions = json.load(actions)
            random.shuffle(json_actions["actions"])
            
            for action in json_actions["actions"]:
                if self.is_valid_action(character, action, time_manager.current_time):
                    time_manager.create_current_time_for_printing(action["message"].format(name=character.name))
                    character.action_timeout = int(action["timeout"])
                    character.done_actions.append(action["id"])
                    break