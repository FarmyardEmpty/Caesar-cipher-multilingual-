alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
ans:str = str(input())
result = ""

for letter in ans:
    if letter.lower() in alphabet:

        current_index = alphabet.index(letter.lower())

        new_index = (current_index + 3) % len(alphabet)

        if letter.isupper():
            result += alphabet[new_index].upper()
        else:
            result += alphabet[new_index]
    else:

        result += letter

print(f"Исходное: {ans}")
print(f"Зашифрованное: {result}")