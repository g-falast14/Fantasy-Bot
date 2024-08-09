from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "Well, you\'re awfully silent...r"
    elif "hello" in lowered:
        return "Hello there!"
    elif 'how are you' in lowered:
        return 'good, thanks!'
    elif 'bye' in lowered:
        return 'see you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['test', 'test1', 'test2'])
