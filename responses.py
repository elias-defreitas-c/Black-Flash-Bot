from random import choice, randint


def get_response(user_input: str, username: str) -> str:
    lowered: str = user_input.lower()
    index = username.find('#')
    if index != -1:
        name_part = username[:index]
    else:
        name_part = username  
    if lowered == 'blackflash':
        chance = 100
        roll = randint(1, chance)
        if roll == chance:
            return 'OMG BLACK FLASH HIT'
        else:
            return f"{name_part} couldn't land a Black Flash"

    return 'Unknown command'