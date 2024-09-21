# Модуль для скрытия информации в тексте-контейнере

# Словарь русских букв и их аналогов в английском языке
rus_to_eng = {
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x',
    'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X'
}

# Обратный словарь: английские буквы и их русские аналоги
eng_to_rus = {v: k for k, v in rus_to_eng.items()}

def text_to_binary(text):
    """Преобразование текста в бинарный формат."""
    binary_text = ''.join(format(ord(c), '08b') for c in text)
    return binary_text

def hide_message(container_text, secret_message):
    """Скрытие бинарного сообщения в тексте-контейнере."""
    binary_message = text_to_binary(secret_message)
    hidden_text = []
    binary_index = 0

    for char in container_text:
        if char in rus_to_eng and binary_index < len(binary_message):
            if binary_message[binary_index] == '1':
                hidden_text.append(rus_to_eng[char])  # Заменяем на латинскую букву
            else:
                hidden_text.append(char)  # Оставляем без изменений
            binary_index += 1
        else:
            hidden_text.append(char)  # Если не русская буква или сообщение закончилось, просто добавляем символ

    return ''.join(hidden_text)

def save_hidden_message(container_file, message_file, output_file):
    """Чтение файлов и сохранение контейнера с скрытым сообщением."""
    with open(container_file, 'r', encoding='utf-8') as f_container:
        container_text = f_container.read()

    with open(message_file, 'r', encoding='utf-8') as f_message:
        secret_message = f_message.read()

    hidden_text = hide_message(container_text, secret_message)

    with open(output_file, 'w', encoding='utf-8') as f_output:
        f_output.write(hidden_text)

    print(f"Скрытая информация записана в файл {output_file}")

# Пример использования
container_file = input("Введите путь к файлу-контейнеру: ")
message_file = input("Введите путь к файлу с секретным сообщением: ")
output_file = input("Введите путь к выходному файлу: ")

save_hidden_message(container_file, message_file, output_file)
