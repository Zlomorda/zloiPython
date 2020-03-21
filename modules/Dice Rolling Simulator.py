from random import randint
import msvcrt as any_key

while True:
    dice_num = randint(2, 12)
    print(dice_num)
    check_any_key = any_key.getwch()
    # Exit the loop if pressed key is ESC
    if ord(check_any_key) == 27:
        break
