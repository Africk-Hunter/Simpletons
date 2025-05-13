class Character:

    def __init__(self, name, traits, action_timeout, location, done_actions): # Constructor (initializer)
        self.name = name
        self.traits = traits
        self.action_timeout = action_timeout
        self.location = location
        self.done_actions = done_actions

    def decrement_action_timeout(self):
        self.action_timeout -= 1