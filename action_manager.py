import json, random

class ActionManager:
    def __init__(self, actions_file='./data/actions.json', sleep_file='./data/sleep.json'):
        with open(actions_file) as f:
            self.actions = json.load(f)["actions"]
        with open(sleep_file) as f:
            self.sleep_messages = json.load(f)["sleep_messages"]
    
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
    
    def pick_sleep(self, character, location_manager):
        location_manager.go_to(character, 'Room')
        random.shuffle(self.sleep_messages)
        print(self.sleep_messages[0]["message"].format(name=character.name))
        character.action_timeout = (random.randint(420, 540) + (1440 - character.sleep_time))
        pass
        
    
    def pick_action(self, character, time_manager, location_manager):
            random.shuffle(self.actions)
            
            if time_manager.current_time > character.sleep_time:
                self.pick_sleep(character, location_manager)
            
            for action in self.actions:
                if self.is_valid_action(character, action, time_manager.current_time):
                    time_manager.create_current_time_for_printing(action["message"].format(name=character.name))
                    character.action_timeout = int(action["timeout"])
                    character.done_actions.append(action["id"])
                    break