import random

class ContextManger():
    
    def __init__(self):
        self.foods = [
            "grilled cheese", "leftover pasta", "granola bar", "cold pizza",
            "apple slices", "turkey sandwich", "instant ramen", "bag of chips",
            "yogurt cup", "microwave burrito", "PB&J sandwich", "protein bar",
            "cereal", "bowl of rice", "banana", "cup of soup", "trail mix",
            "cheese and crackers", "frozen dinner", "chicken nuggets",
            "fruit smoothie", "salad", "beef jerky", "toast with jam",
            "muffin", "omelette", "peanut butter spoon", "cup noodles"
        ]
        self.trait_messages = {
            "clumsy": [
                "and almost dropped it on the way to the couch.",
                "but spilled some on the floor.",
                "and stumbled while carrying it.",
            ],
            "courageous": [
                "as if it were some daring culinary experiment.",
                "with a fearless grin.",
                "ready to face any kitchen disaster.",
            ],
            "lazy": [
                "without even sitting up all the way.",
                "barely lifting a finger to eat.",
                "half-asleep while chewing.",
            ],
            "nonchalant": [
                "with zero regard for presentation or utensils.",
                "like it was just another boring meal.",
                "completely unfazed by the mess.",
            ],
            "hyper": [
                "then bounced their leg nonstop while chewing.",
                "talking fast between bites.",
                "barely able to keep still.",
            ]
        }
        
    def fill_action_context(self, character, action):
        context = {
            'name': character.name,
            'food': random.choice(self.foods),
            'trait_message': '',
        }
        
        return action["message"].format(**context)