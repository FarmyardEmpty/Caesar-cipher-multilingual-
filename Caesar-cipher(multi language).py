with open('key.txt', 'w') as file:
    key: str = str(input("Введите ключ шифрования: "))
    file.write(f"Key cipher = {key}")

with open("key.txt", "r") as file:
    for line in file:
        if "=" in line:
            key_from_file = int(line.split("=")[1].strip())  # Считываем ключ символ находящийся после "="
            break
    attempt = 1  # Учитываем верную попытку

    while True:  # Реализация проверки кода шифрования
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


def language_analis(text):
    language_profiles = {
        'russian': {
            'freq': {
                'о': 0.109, 'е': 0.084, 'а': 0.080, 'и': 0.073, 'н': 0.067,
                'т': 0.063, 'с': 0.055, 'р': 0.047, 'в': 0.045, 'л': 0.044,
                'к': 0.035, 'м': 0.030, 'д': 0.026, 'п': 0.024, 'у': 0.022
            },
            'bigrams': [
                'ст', 'но', 'ен', 'то', 'на', 'ов', 'ни', 'ра', 'во', 'ко',
                'ер', 'не', 'го', 'пр', 'ро', 'ка', 'ет', 'ль', 'ор', 'по'
            ],
            'trigrams': [
                'сто', 'ени', 'нов', 'тов', 'нова', 'ров', 'ова', 'ение', 'ван', 'ере',
                'про', 'тор', 'оль', 'ель', 'стр', 'его', 'при', 'как', 'ать', 'ться'
            ]
        },

        'english': {
            'freq': {
                'e': 0.127, 't': 0.091, 'a': 0.082, 'o': 0.075, 'i': 0.070,
                'n': 0.067, 's': 0.063, 'h': 0.061, 'r': 0.060, 'd': 0.043,
                'l': 0.040, 'c': 0.028, 'u': 0.028, 'm': 0.024, 'w': 0.024
            },
            'bigrams': [
                'th', 'he', 'in', 'er', 'an', 're', 'nd', 'at', 'on', 'nt',
                'ha', 'es', 'st', 'en', 'ed', 'to', 'it', 'ou', 'ea', 'hi'
            ],
            'trigrams': [
                'the', 'and', 'ing', 'her', 'hat', 'his', 'tha', 'ere', 'for', 'ent',
                'ion', 'tio', 'has', 'ted', 'ter', 'ate', 'oul', 'all', 'ith', 'ght'
            ]
        },

        'french': {
            'freq': {
                'e': 0.147, 'a': 0.076, 'i': 0.075, 's': 0.073, 'n': 0.071,
                'r': 0.066, 't': 0.063, 'o': 0.058, 'l': 0.055, 'u': 0.054,
                'd': 0.037, 'c': 0.031, 'p': 0.031, 'm': 0.030, 'é': 0.023
            },
            'bigrams': [
                'es', 'le', 'de', 'en', 'nt', 're', 'on', 'er', 'et', 'te',
                'el', 'an', 'qu', 'la', 'ur', 'me', 'se', 'it', 'is', 'ne'
            ],
            'trigrams': [
                'ent', 'que', 'ait', 'ant', 'est', 'ont', 'our', 'men', 'ell', 'tre',
                'ion', 'ans', 'ure', 'res', 'nce', 'com', 'ait', 'ous', 'ait', 'dan'
            ]
        },

        'german': {
            'freq': {
                'e': 0.174, 'n': 0.097, 'i': 0.076, 's': 0.070, 'r': 0.068,
                'a': 0.065, 't': 0.058, 'd': 0.051, 'h': 0.047, 'u': 0.039,
                'l': 0.034, 'c': 0.031, 'g': 0.030, 'm': 0.026, 'o': 0.025
            },
            'bigrams': [
                'en', 'er', 'ch', 'de', 'ei', 'nd', 'ie', 'ge', 'te', 'sc',
                'be', 'un', 're', 'in', 'he', 'es', 'au', 'an', 'ac', 'it'
            ],
            'trigrams': [
                'ein', 'ich', 'und', 'der', 'che', 'end', 'gen', 'sch', 'cht', 'den',
                'ung', 'nen', 'ren', 'sen', 'ver', 'lie', 'ter', 'hen', 'ere', 'ber'
            ]
        },

        'spanish': {
            'freq': {
                'e': 0.136, 'a': 0.125, 'o': 0.087, 's': 0.079, 'n': 0.067,
                'r': 0.061, 'i': 0.062, 'l': 0.050, 'd': 0.046, 't': 0.040,
                'c': 0.039, 'u': 0.035, 'm': 0.031, 'p': 0.025, 'b': 0.015
            },
            'bigrams': [
                'de', 'la', 'el', 'en', 'es', 'os', 'ar', 'ue', 'ra', 're',
                'er', 'as', 'ci', 'ad', 'al', 'ie', 'se', 'nt', 'on', 'st'
            ],
            'trigrams': [
                'que', 'ent', 'ion', 'est', 'ado', 'ara', 'era', 'idad', 'par', 'nte',
                'per', 'con', 'los', 'del', 'una', 'por', 'com', 'ien', 'cia', 'res'
            ]
        }
    }

    text = text.lower()
    clean_text = ''.join([c for c in text if c.isalpha()])

    if len(clean_text) < 3:
        return 'unknown'

    freq_scores = {}
    for lang, profile in language_profiles.items():
        score = 0
        text_length = len(clean_text)
        actual_freq = {}
        for char in clean_text:
            actual_freq[char] = actual_freq.get(char, 0) + 1
        for char in actual_freq:
            actual_freq[char] /= text_length

        for char, expected_freq in profile['freq'].items():
            actual = actual_freq.get(char, 0)
            score += abs(expected_freq - actual)
        freq_scores[lang] = score

    bigram_scores = {}
    for lang, profile in language_profiles.items():
        score = 0
        bigrams = [clean_text[i:i + 2] for i in range(len(clean_text) - 1)]

        for common_bigram in profile['bigrams']:
            if common_bigram in bigrams:
                score -= 1
        bigram_scores[lang] = score

    trigram_scores = {}
    for lang, profile in language_profiles.items():
        score = 0
        trigrams = [clean_text[i:i + 3] for i in range(len(clean_text) - 2)]

        for common_trigram in profile['trigrams']:
            if common_trigram in trigrams:
                score -= 2
        trigram_scores[lang] = score

    total_scores = {}
    for lang in language_profiles.keys():
        total_scores[lang] = (freq_scores[lang] +
                              bigram_scores[lang] +
                              trigram_scores[lang])

    detected_lang = min(total_scores.items(), key=lambda x: x[1])[0]

    return detected_lang

def alphabet_RuA(text, encryption_key):
    alphabet_RU = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    result = ""

    for letter in text:
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
    return result


def alphabet_EnA(text, encryption_key):
    alphabet_EN = list('abcdefghijklmnopqrstuvwxyz')
    result = ""

    for letter in text:
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
    return result


def alphabet_FrA(text, encryption_key):
    # Французский алфавит с диакритическими знаками
    alphabet_FR = list('abcdefghijklmnopqrstuvwxyzàâæçèéêëîïôœùûüÿ')
    result = ""

    for letter in text:
        if letter.lower() in alphabet_FR:
            current_index = alphabet_FR.index(letter.lower())
            new_index = (current_index + encryption_key) % len(alphabet_FR)

            if letter.isupper():
                result += alphabet_FR[new_index].upper()
            else:
                result += alphabet_FR[new_index]
        else:
            result += letter

    print(f"Исходное: {text}")
    print(f"Зашифрованное: {result}")
    return result


def alphabet_DeA(text, encryption_key):
    # Немецкий алфавит с умлаутами
    alphabet_DE = list('abcdefghijklmnopqrstuvwxyzäöüß')
    result = ""

    for letter in text:
        if letter.lower() in alphabet_DE:
            current_index = alphabet_DE.index(letter.lower())
            new_index = (current_index + encryption_key) % len(alphabet_DE)

            if letter.isupper():
                result += alphabet_DE[new_index].upper()
            else:
                result += alphabet_DE[new_index]
        else:
            result += letter

    print(f"Исходное: {text}")
    print(f"Зашифрованное: {result}")
    return result


def alphabet_EsA(text, encryption_key):
    # Испанский алфавит
    alphabet_ES = list('abcdefghijklmnopqrstuvwxyzñáéíóúü')
    result = ""

    for letter in text:
        if letter.lower() in alphabet_ES:
            current_index = alphabet_ES.index(letter.lower())
            new_index = (current_index + encryption_key) % len(alphabet_ES)

            if letter.isupper():
                result += alphabet_ES[new_index].upper()
            else:
                result += alphabet_ES[new_index]
        else:
            result += letter

    print(f"Исходное: {text}")
    print(f"Зашифрованное: {result}")
    return result


def central_block_code(encryption_key):
    ans = input("Введите текст: ")

    if not ans:
        print("Текст не введен!")
        return

    detected_language = language_analis(ans)

    print(f"Определенный язык: {detected_language}")

    if detected_language == 'russian':
        alphabet_RuA(ans, encryption_key)
        print("Языком вашего текста является русский.")
    elif detected_language == 'english':
        alphabet_EnA(ans, encryption_key)
        print("Языком вашего текста является английский.")
    elif detected_language == 'french':
        alphabet_FrA(ans, encryption_key)
        print("Языком вашего текста является французский.")
    elif detected_language == 'german':
        alphabet_DeA(ans, encryption_key)
        print("Языком вашего текста является немецкий.")
    elif detected_language == 'spanish':
        alphabet_EsA(ans, encryption_key)
        print("Языком вашего текста является испанский.")

central_block_code(key_your)