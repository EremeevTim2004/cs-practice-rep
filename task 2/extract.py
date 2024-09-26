# Массивы для русских и латинских букв-замен
rus_letters = ['а', 'е', 'о', 'р', 'с', 'у', 'х', 'А', 'В', 'Е', 'К', 'О', 'Р', 'С', 'Т', 'Х']
eng_letters = ['a', 'e', 'o', 'p', 'c', 'y', 'x', 'A', 'B', 'E', 'K', 'O', 'P', 'C', 'T', 'X']

container_with_hidden_info_file = 'code.txt'
output_secret_message_file = 'message.txt'

def bin_to_text(bin_str):
    """Преобразование бинарного представления в текст с учётом кодировки CP1251."""
    byte_array = bytearray()
    for i in range(0, len(bin_str), 8):
        byte = bin_str[i:i+8]
        byte_array.append(int(byte, 2))
    
    return byte_array.decode('cp1251')

def extract_info_from_container(container):
    """Извлечение скрытой информации из контейнера."""
    secret_message_bin = []
    
    for char in container:
        if char in rus_letters:
            # Если буква осталась русской, значит бит = 0
            secret_message_bin.append('0')
        elif char in eng_letters:
            # Если буква заменена на английский аналог, значит бит = 1
            secret_message_bin.append('1')
    
    return ''.join(secret_message_bin)

# Чтение контейнера
with open(container_with_hidden_info_file, 'r', encoding='cp1251') as container_f:
    container_text = container_f.read()

# Извлечение бинарного сообщения
secret_message_bin = extract_info_from_container(container_text)

# Преобразование бинарного сообщения в текст
secret_message = bin_to_text(secret_message_bin)

# Запись извлеченного сообщения
with open(output_secret_message_file, 'w', encoding='cp1251') as output_f:
    output_f.write(secret_message)
