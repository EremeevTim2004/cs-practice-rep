# Модуль для извлечения скрытой информации

# Словарь русских букв и их аналогов в английском языке
rus_to_eng = {
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x',
    'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X'
}

# Обратный словарь: английские буквы и их русские аналоги
eng_to_rus = {v: k for k, v in rus_to_eng.items()}

def binary_to_text(binary_message):
    """Преобразование бинарного сообщения в текст."""
    chars = [chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8)]
    return ''.join(chars)

def extract_message(container_text):
    """Извлечение скрытого сообщения из текста-контейнера."""
    binary_message = []

    for char in container_text:
        if char in rus_to_eng:
            binary_message.append('0')  # Русская буква
        elif char in eng_to_rus:
            binary_message.append('1')  # Латинская буква

    return binary_to_text(''.join(binary_message))

def extract_hidden_message(container_file, output_message_file):
    """Чтение файла-контейнера и извлечение скрытого сообщения."""
    with open(container_file, 'r', encoding='utf-8') as f_container:
        container_text = f_container.read()

    secret_message = extract_message(container_text)

    with open(output_message_file, 'w', encoding='utf-8') as f_output:
        f_output.write(secret_message)

    print(f"Скрытое сообщение извлечено и сохранено в {output_message_file}")

# Пример использования
container_file = input("Введите путь к файлу-контейнеру: ")
output_message_file = input("Введите путь к файлу для скрытого сообщения: ")

extract_hidden_message(container_file, output_message_file)
