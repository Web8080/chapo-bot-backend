from core.wit_client import get_intent
from core.intent_handler import handle_intent

def main():
    print("Welcome to Chapo Bot CLI!")
    while True:
        user_input = input("You: ")
        wit_data = get_intent(user_input)
        response = handle_intent(wit_data, user_input)
        print("Chapo:", response)

if __name__ == "__main__":
    main()
