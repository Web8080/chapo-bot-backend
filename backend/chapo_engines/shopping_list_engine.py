import json
from pathlib import Path

class ShoppingListEngine:
    def __init__(self, memory_file='/Users/user/chapo-bot-backend/backend/shopping_list.json'):
        self.memory_path = Path(memory_file)
        self.list = self.load_list()

    def load_list(self):
        if self.memory_path.exists():
            with open(self.memory_path, 'r') as f:
                return json.load(f)
        return []

    def save_list(self):
        with open(self.memory_path, 'w') as f:
            json.dump(self.list, f, indent=2)

    def add_items(self, items):
        if isinstance(items, str):
            items = [item.strip() for item in items.split(',')]
        for item in items:
            if item.lower() not in [x.lower() for x in self.list]:
                self.list.append(item)
        self.save_list()
        return f"Added {', '.join(items)} to your shopping list."

    def get_list(self):
        if self.memory_path.exists():
           with open(self.memory_path, 'r') as f:
               return json.load(f)
        return []



    def clear_list(self):
        self.list = []
        self.save_list()
        return "Your shopping list has been cleared."

    def remove_item(self, item):
        item_lower = item.lower()
        for i in self.list:
            if i.lower() == item_lower:
                self.list.remove(i)
                self.save_list()
                return f"Removed {item} from your shopping list."
        return f"{item} was not found on your list."

# Instantiate the engine globally (only once)
shopping_list_engine = ShoppingListEngine()

# Utility function to add items
def save_to_shopping_list(items):
    return shopping_list_engine.add_items(items)

# Utility function to load the list
def load_shopping_list():
    return shopping_list_engine.list

# Utility function to clear the list
def clear_shopping_list():
    return shopping_list_engine.clear_list()
