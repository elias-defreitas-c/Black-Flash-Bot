from random import randint
import glob
import random

def get_response(user_input: str, username: str) -> str:
    lowered: str = user_input.lower()
    index = username.find('#')
    if index != -1:
        name_part = username[:index]
    else:
        name_part = username  
    if lowered == 'blackflash':
        file_path_type = ["./blackflashGifs/*.gif"]
        images = glob.glob(random.choice(file_path_type))
        random_image = random.choice(images)
        chance = 10
        roll = randint(1, chance)
        if roll == chance:
            return f'Despite all odds. **{name_part}** hit a **Balckflash** {random_image}'
        else:
            return f"**{name_part}** couldn't land a Black Flash"

    return 'Unknown command'
