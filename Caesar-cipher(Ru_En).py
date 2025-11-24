with open('key.txt', 'w') as file:
    key: str = str(input("Введите ключ шифрования: "))
    file.write(f"Key cipher = {key}")

with open("key.txt", "r") as file:
    for line in file:
        if "=" in line:
            key_from_file = int(line.split("=")[1].strip()) # Считываем ключ символ находящийся после "="
            break
    attempt = 1  # Учитываем верную попытку

    while True: # Реализация проверки кода шифрования
        try:
            key_your = int(input("Попробуйте угадать ключ шифрования: "))
            if key_your == key_from_file:
                print(f"Да, ключом шифрования был - {key_your}")
                break
            else:
                attempt += 1
                print("Не верно, попробуйте ещё раз.")
        except ValueError:
            print("Ошибка! Введите целое число.")
            attempt += 1

    print(f"Всего попыток на угадывание было совершенно: {attempt}")

def alphabet_RuA(text, encryption_key):
    alphabet_RU: list[str] = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    result = ""

    for letter in text: # Основа кода шифрования "Цезарь"
        if letter.lower() in alphabet_RU:
            current_index = alphabet_RU.index(letter.lower())
            new_index = (current_index + encryption_key) % len(alphabet_RU)

            if letter.isupper():
                result += alphabet_RU[new_index].upper()
            else:
                result += alphabet_RU[new_index]
        else:
            result += letter

    print(f"Исходное: {text}")
    print(f"Зашифрованное: {result}")

def alphabet_EnA(text, encryption_key):
    alphabet_EN: list[str] = list('abcdefghijklmnopqrstuvwxyz')
    result = ""

    for letter in text: # Основа кода шифрования "Цезарь"
        if letter.lower() in alphabet_EN:
            current_index = alphabet_EN.index(letter.lower())
            new_index = (current_index + encryption_key) % len(alphabet_EN)

            if letter.isupper():
                result += alphabet_EN[new_index].upper()
            else:
                result += alphabet_EN[new_index]
        else:
            result += letter

    print(f"Исходное: {text}")
    print(f"Зашифрованное: {result}")

def central_block_code(encryption_key): # Реализация определения языка в тексте
    alphabet_RU = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    alphabet_EN = list('abcdefghijklmnopqrstuvwxyz')
    ans = input("Введите текст: ")
    first_letter = ans[0].lower() if ans else ''

    '''
    Считываем первый символ(букву), реализуется, если используется два/или более различных языков(по алфавиту!)
    '''

    if first_letter in alphabet_RU:
        alphabet_RuA(ans, encryption_key) # Запускает функция шифрования, если язык русский
        print("Языком вашего текста является русский.")
    elif first_letter in alphabet_EN:
        alphabet_EnA(ans, encryption_key) # Зыпускает функция шифрования, если язык английский
        print("Языком вашего текста является английский.")
    else:
        print("Не удалось определить язык текста")

central_block_code(key_your)
