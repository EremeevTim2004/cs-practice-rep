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