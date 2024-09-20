def generate_vigenere_table(alphabet):
    """Генерирует таблицу Виженера на основе алфавита."""
    table = []
    n = len(alphabet)
    for i in range(n):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        table.append(shifted_alphabet)
    return table

def extend_key(text, key):
    """Расширяет ключ до длины текста."""
    extended_key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    return extended_key

def encrypt_vigenere(plaintext, key, alphabet):
    """Шифрует текст по схеме Виженера."""
    table = generate_vigenere_table(alphabet)
    extended_key = extend_key(plaintext, key)
    ciphertext = []

    for p_char, k_char in zip(plaintext, extended_key):
        if p_char in alphabet:
            p_index = alphabet.index(p_char)
            k_index = alphabet.index(k_char)
            cipher_char = table[k_index][p_index]
            ciphertext.append(cipher_char)
        else:
            ciphertext.append(p_char)  # Если символ не в алфавите

    return ''.join(ciphertext)

def decrypt_vigenere(ciphertext, key, alphabet):
    """Расшифровывает текст по схеме Виженера."""
    table = generate_vigenere_table(alphabet)
    extended_key = extend_key(ciphertext, key)
    plaintext = []

    for c_char, k_char in zip(ciphertext, extended_key):
        if c_char in alphabet:
            k_index = alphabet.index(k_char)
            c_index = table[k_index].index(c_char)
            plain_char = alphabet[c_index]
            plaintext.append(plain_char)
        else:
            plaintext.append(c_char)  # Если символ не в алфавите

    return ''.join(plaintext)

def save_to_file(filename, content):
    """Сохраняет результат в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Результат сохранен в файл: {filename}")

def read_from_file(filename):
    """Читает данные из файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None

if __name__ == "__main__":
    # Русский алфавит
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    # Выбор действия
    action = input("Выберите действие (1 - зашифровать, 2 - дешифровать): ").strip()

    if action == '1':
        # Ввод данных для шифрования
        plaintext = input("Введите текст для шифрования: ").lower()
        key = input("Введите ключ: ").lower()

        # Шифрование
        encrypted_text = encrypt_vigenere(plaintext, key, alphabet)
        print(f"Зашифрованный текст: {encrypted_text}")

        # Сохранение зашифрованного текста в файл
        save_to_file('encrypted_text.txt', encrypted_text)

    elif action == '2':
        # Чтение зашифрованного текста из файла
        encrypted_text = read_from_file('encrypted_text.txt')
        if encrypted_text:
            key = input("Введите ключ: ").lower()

            # Расшифровка
            decrypted_text = decrypt_vigenere(encrypted_text, key, alphabet)
            print(f"Расшифрованный текст: {decrypted_text}")

            # Сохранение расшифрованного текста в файл
            save_to_file('decrypted_text.txt', decrypted_text)
    else:
        print("Неверный выбор. Попробуйте снова.")
