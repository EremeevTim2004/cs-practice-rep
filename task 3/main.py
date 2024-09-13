# Генерирует таблицу Виженера на основе алфавита.
def generate_vigenere_table(alphabet):
    table = []
    n = len(alphabet)
    for i in range(n):
        shifted_alphabet = alphabet[i:] + alphabet[:i]
        table.append(shifted_alphabet)
    return table

# Расширяет ключ до длины текста.
def extend_key(text, key):
    extended_key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
    return extended_key

# Шифрует текст по схеме Виженера.
def encrypt_vigenere(plaintext, key, alphabet):
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

# Расшифровывает текст по схеме Виженера.
def decrypt_vigenere(ciphertext, key, alphabet):
    table = generate_vigenere_table(alphabet)
    extended_key = extend_key(ciphertext, key)
    plaintext = []
    for c_char, k_char in zip(ciphertext, extended_key):
        if c_char in alphabet:
            k_index = alphabet.index(k_char)
            c_index = table[k_index].index(c_char)
            plain_char = alphabet[c_index]
            plaintext.append(plain_char)
        # Если символ не в алфавите
        else:
            plaintext.append(c_char)
    return ''.join(plaintext)

if __name__ == "__main__":
    # Русский алфавит
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    # Ввод данных
    plaintext = input("Введите текст для шифрования: ").lower()
    key = input("Введите ключ: ").lower()
    # Шифрование
    encrypted_text = encrypt_vigenere(plaintext, key, alphabet)
    print(f"Зашифрованный текст: {encrypted_text}")
    # Расшифровка
    decrypted_text = decrypt_vigenere(encrypted_text, key, alphabet)
    print(f"Расшифрованный текст: {decrypted_text}")
