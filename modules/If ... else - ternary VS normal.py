# Синтаксис
(False, True)[condition]

# Альтернативная версия
question = input("Do you like ternary operators? ")

answer = ("Nonsense", "Python rulezz!!")[question == "Yes"]

print(answer)

# Обычная версия
question = input("Do you like ternary operators? ")

if question.lower() == "yes":
    print("Python rulezz!!")
else:
    print("Nonsense")
