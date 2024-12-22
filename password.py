import string
import random

# сохраняем все символы в списках
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# спрашиваем пользователя о количестве символов
user_input = input("Сколько символов вы хотите в своём пароле? ")

# проверьте, является ли введенное значение числом? больше ли оно 6
while True:

    try:

        characters_number = int(user_input)

        if characters_number < 6:

            print("Ваше число должно быть не меньше 6.")

            user_input = input("Пожалуйста, введите свой номер ещё раз: ")

        else:

            break

    except:

        print("Пожалуйста, вводите только цифры.")

        user_input = input("Сколько символов вы хотите в своём пароле?  ")

# перемешаем все списки
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# вычислить 30% и 20% от количества символов
part1 = round(characters_number * (30 / 100))
part2 = round(characters_number * (20 / 100))

# генерация пароля (60% букв и 40% цифр и знаков препинания)
result = []

for x in range(part1):
    result.append(s1[x])
    result.append(s2[x])

for x in range(part2):
    result.append(s3[x])
    result.append(s4[x])

# перемешать результат
random.shuffle(result)

# объединить результат
password = "".join(result)
print("Сгенерированный пароль: ", password)