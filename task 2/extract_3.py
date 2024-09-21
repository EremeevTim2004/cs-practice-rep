# Словарь русских букв и их аналогов в английском языке
rus_to_eng = {
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x',
    'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X'
}

# Обратный словарь: английские буквы и их русские аналоги
eng_to_rus = {v: k for k, v in rus_to_eng.items()}

def extract_method3(container_file):
    with open(container_file, 'r', encoding='utf-8') as container:
        container_text = container.read()

    secret_bits = []

    for char in container_text:
        if char in eng_to_rus:
            secret_bits.append('1')  # Английская буква означает бит '1'
        elif char in rus_to_eng:
            secret_bits.append('0')  # Русская буква означает бит '0'

    # Преобразуем биты в символы
    secret_chars = [chr(int(''.join(secret_bits[i:i+8]), 2)) for i in range(0, len(secret_bits), 8)]
    secret_text = ''.join(secret_chars).strip('\x00')

    print(f"Извлеченная информация: {secret_text}")
    return secret_text
