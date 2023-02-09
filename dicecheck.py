import re


def check_dice(dice: str):
    if re.match(r"^([0-9])*[D,d]([0-9])+([+-][0-9]+)*$", dice):
        return True
    return False


print(check_dice("8d7+10"))