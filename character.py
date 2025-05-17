import random

class Character:

    def __init__(self, name, traits, action_timeout, location, done_actions, text_color): # Constructor (initializer)
        self.name = name
        self.traits = traits
        self.action_timeout = action_timeout
        self.location = location
        self.done_actions = done_actions
        self.sleep_time = random.randint(1260, 1440)
        self.move_timeout = 0
        self.current_location_time = 0
        self.text_color = text_color
        self.needs = {
            "hunger": {"value": 50, "decay_rate": 0.3, "priority_weight": 1.3, "max_value": 100},
            "sleep": {"value": 100, "decay_rate": 0.07, "priority_weight": 2, "max_value": 100},
            "social": {"value": 50, "decay_rate": 0.4, "priority_weight": 1, "max_value": 100},
            "thirst": {"value": 100, "decay_rate": 0.4, "priority_weight": 1.4, "max_value": 100},
            "hygiene": {"value": 80, "decay_rate": 0.2, "priority_weight": 0.9, "max_value": 100}
        }

    def decrement_action_timeout(self):
        self.action_timeout -= 1
        
    def decay_needs(self):
        for need, need_data in self.needs.items():
            if need_data["value"] - need_data["decay_rate"] > 0 and need_data["value"] <= 100:
                need_data["value"] -= need_data["decay_rate"]
            
    def update_based_on_action(self, timeout, change_type, change_amount):
        self.action_timeout = timeout
        
        for need, need_data in self.needs.items():
            if need == change_type:
                if need_data["value"] + change_amount > 100:
                    need_data["value"] = 100
                else:
                    need_data["value"] += change_amount
            
    def increment_current_location_time(self):
        self.current_location_time += 1