from random import randint
import msvcrt as any_key

while True:
    dice_1_num = randint(1, 6)
    dice_2_num = randint(1, 6)
    print(dice_1_num + dice_2_num)
    check_any_key = any_key.getwch()
    
    if ord(check_any_key) == 27: # Exit the loop if pressed key is ESC
        break
