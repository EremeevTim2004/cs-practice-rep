def extract_method1(container_file):
    with open(container_file, 'r', encoding='utf-8') as container:
        container_lines = container.readlines()

    secret_bits = []
    for line in container_lines:
        if line.endswith(' \n'):
            secret_bits.append('1')
        else:
            secret_bits.append('0')

    secret_chars = [chr(int(''.join(secret_bits[i:i+8]), 2)) for i in range(0, len(secret_bits), 8)]
    secret_text = ''.join(secret_chars).strip('\x00')

    print(f"Извлеченная информация: {secret_text}")
    return secret_text

def extract_method2(container_file):
    with open(container_file, 'r', encoding='utf-8') as container:
        container_text = container.read()

    secret_bits = []
    for i in range(len(container_text) - 1):
        if container_text[i] == ' ':
            if container_text[i + 1] == ' ':
                secret_bits.append('1')
            else:
                secret_bits.append('0')

    secret_chars = [chr(int(''.join(secret_bits[i:i+8]), 2)) for i in range(0, len(secret_bits), 8)]
    secret_text = ''.join(secret_chars).strip('\x00')

    print(f"Извлеченная информация: {secret_text}")
    return secret_text

def extract_method3(container_file):
    with open(container_file, 'r', encoding='utf-8') as container:
        container_text = container.read()

    secret_bits = []
    for char in container_text:
        if char in eng_to_rus:
            secret_bits.append('1')
        elif char in rus_to_eng:
            secret_bits.append('0')

    secret_chars = [chr(int(''.join(secret_bits[i:i+8]), 2)) for i in range(0, len(secret_bits), 8)]
    secret_text = ''.join(secret_chars).strip('\x00')

    print(f"Извлеченная информация: {secret_text}")
    return secret_text
