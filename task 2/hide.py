def hide_method1(container_file, secret_file, output_file):
    with open(container_file, 'r', encoding='utf-8') as container, open(secret_file, 'r', encoding='utf-8') as secret:
        container_lines = container.readlines()
        secret_text = secret.read()

    # Преобразуем секретный текст в биты
    secret_bits = ''.join(format(ord(char), '08b') for char in secret_text)

    result = []
    for i, line in enumerate(container_lines):
        if i < len(secret_bits):
            if secret_bits[i] == '1':
                result.append(line.rstrip() + ' \n')
            else:
                result.append(line)
        else:
            result.append(line)

    with open(output_file, 'w', encoding='utf-8') as output:
        output.writelines(result)

    print(f"Скрытая информация записана в {output_file}")

def hide_method2(container_file, secret_file, output_file):
    with open(container_file, 'r', encoding='utf-8') as container, open(secret_file, 'r', encoding='utf-8') as secret:
        container_text = container.read()
        secret_text = secret.read()

    secret_bits = ''.join(format(ord(char), '08b') for char in secret_text)
    container_chars = list(container_text)
    space_count = 0

    for i in range(len(container_chars)):
        if container_chars[i] == ' ':
            if space_count < len(secret_bits):
                if secret_bits[space_count] == '1':
                    container_chars[i] = '  '  # Удваиваем пробел
                space_count += 1

    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(''.join(container_chars))

    print(f"Скрытая информация записана в {output_file}")
rus_to_eng = {'а': 'a', 'е': 'e', 'о': 'o', 'р': 'p', 'с': 'c', 'у': 'y', 'х': 'x',
              'А': 'A', 'В': 'B', 'Е': 'E', 'К': 'K', 'О': 'O', 'Р': 'P', 'С': 'C', 'Т': 'T', 'Х': 'X'}
eng_to_rus = {v: k for k, v in rus_to_eng.items()}

def hide_method3(container_file, secret_file, output_file):
    with open(container_file, 'r', encoding='utf-8') as container, open(secret_file, 'r', encoding='utf-8') as secret:
        container_text = container.read()
        secret_text = secret.read()

    secret_bits = ''.join(format(ord(char), '08b') for char in secret_text)
    result = []
    bit_index = 0

    for char in container_text:
        if char in rus_to_eng and bit_index < len(secret_bits):
            if secret_bits[bit_index] == '1':
                result.append(rus_to_eng[char])  # Меняем русскую букву на аналог
            else:
                result.append(char)  # Оставляем русскую букву без изменений
            bit_index += 1
        else:
            result.append(char)

    with open(output_file, 'w', encoding='utf-8') as output:
        output.write(''.join(result))

    print(f"Скрытая информация записана в {output_file}")
