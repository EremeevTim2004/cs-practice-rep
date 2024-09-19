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