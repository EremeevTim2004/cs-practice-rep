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
