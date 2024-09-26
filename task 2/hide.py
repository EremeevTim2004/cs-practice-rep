# coding: cp1251

# Массивы для русских и латинских букв-замен
rus_letters = ['а', 'е', 'о', 'р', 'с', 'у', 'х', 'А', 'В', 'Е', 'К', 'О', 'Р', 'С', 'Т', 'Х']
eng_letters = ['a', 'e', 'o', 'p', 'c', 'y', 'x', 'A', 'B', 'E', 'K', 'O', 'P', 'C', 'T', 'X']

# Чтение файлов
container_file = 'container.txt'
secret_message_file = 'secret.txt'
output_file = 'code.txt'

def text_to_bin(text):
    """Преобразование текста в бинарное представление с учетом кодировки CP1251."""
    binary_str = ''.join(format(ord(char), '08b') for char in text)
    return binary_str

def hide_info_in_container(container, secret_message_bin):
    """Скрытие информации в контейнере."""
    container_with_hidden_info = []
    message_idx = 0
    
    for char in container:
        if char in rus_letters and message_idx < len(secret_message_bin):
            if secret_message_bin[message_idx] == '1':
                # Заменяем русскую букву на английский аналог
                char = eng_letters[rus_letters.index(char)]
            message_idx += 1
        container_with_hidden_info.append(char)
    
    return ''.join(container_with_hidden_info)

# Чтение файлов и обработка
with open(container_file, 'r', encoding='cp1251') as container_f:
    container_text = container_f.read()

with open(secret_message_file, 'r', encoding='cp1251') as secret_f:
    secret_message = secret_f.read()

# Преобразование секретного сообщения в двоичный формат
secret_message_bin = text_to_bin(secret_message)

# Скрытие информации
container_with_hidden_info = hide_info_in_container(container_text, secret_message_bin)

# Запись результата в файл
with open(output_file, 'w', encoding='cp1251') as output_f:
    output_f.write(container_with_hidden_info)
