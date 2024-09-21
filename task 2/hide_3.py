# Словарь русских букв и их аналогов в английском языке
rus_to_eng = {
    'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x',
    'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X'
}

# Обратный словарь: английские буквы и их русские аналоги
eng_to_rus = {v: k for k, v in rus_to_eng.items()}


def hide_method3(container_file, secret_file, output_file):
    with open(container_file, 'r', encoding='utf-8') as container, open(secret_file, 'r', encoding='utf-8') as secret:
        container_text = container.read()
        secret_text = secret.read()

    # Преобразуем секретный текст в биты
    secret_bits = ''.join(format(ord(char), '08b') for char in secret_text)
    result = []
    bit_index = 0

    for char in container_text:
        if char in rus_to_eng and bit_index < len(secret_bits):
            if secret_bits[bit_index] == '1':
                result.append(rus_to_eng[char])  # Меняем русскую букву на английский аналог
            else:
                result.append(char)  # Оставляем русскую букву без изменений
            bit_index += 1
        else:
            result.append(char)

    # Записываем результат в выходной файл
    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(''.join(result))

    print(f"Скрытая информация записана в {output_file}")
