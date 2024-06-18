from random import randint, choice
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
        random_gif = random.choice(images)
        chance = 20
        roll = randint(1, chance)
        if roll == chance:
            return choice([f'Despite all odds. **{name_part}** hit a **Balck Flash.** {random_gif}',
                           f"Surpassing every obstacle, **{name_part}s** **Balck Flash** landed flawlessly. {random_gif}",
                           f"And after all, **{name_part}s** **Balck Flash** connected with precision. {random_gif}",
                           f"Unexpected and unstoppable, **{name_part}s** **Balck Flash** made contact. {random_gif}",
                           f"Surpassing disbelief. **{name_part}** used **Balck Flash** and it struck perfectly. {random_gif}",
                           f"Surpassing all expectations, **{name_part}** hit a **Balck Flash** dead on. {random_gif}",
                           f"In a stunning display, **{name_part}** nailed a flawless **Balck Flash**. {random_gif}"
                           ])
        else:
            return f"**{name_part}** couldn't land a Black Flash"

    return 'Unknown command'
