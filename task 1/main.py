import os
import struct

# Имя файла для хранения хэш-сумм
HASH_FILE = "hashes.txt"

# Подсчет хэш-суммы файла по принципу XOR 16-битных блоков.
def calculate_hash(file_path):
    hash_value = 0
    try:
        with open(file_path, 'rb') as f:
            while True:
                # Читаем 16 бит (2 байта)
                chunk = f.read(2)  
                if not chunk:
                    break
                # Если последний блок меньше 16 бит, дополняем нулями
                if len(chunk) == 1:
                    chunk += b'\x00'
                # Преобразуем в число и выполняем XOR
                (value,) = struct.unpack('H', chunk)
                hash_value ^= value
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
    return hash_value

# Рекурсивный обход каталога и сохранение хэш-сумм файлов.
def save_hashes(directory):
    with open(os.path.join(directory, HASH_FILE), 'w') as hash_file:
        for root, _, files in os.walk(directory):
            for file in files:
                # Пропускаем файл с хэш-суммами
                if file == HASH_FILE:
                    continue
                file_path = os.path.join(root, file)
                file_hash = calculate_hash(file_path)
                # Записываем хэш-сумму в файл
                relative_path = os.path.relpath(file_path, directory)
                hash_file.write(f"{relative_path}:{file_hash}\n")
                print(f"Файл: {relative_path}, Хэш: {file_hash}")

# Проверка целостности файлов по сохраненным хэш-суммам.
def verify_hashes(directory):
    hash_path = os.path.join(directory, HASH_FILE)
    if not os.path.exists(hash_path):
        print(f"Файл с хэшами {HASH_FILE} не найден в каталоге {directory}.")
        return
    with open(hash_path, 'r') as hash_file:
        stored_hashes = {}
        for line in hash_file:
            relative_path, file_hash = line.strip().split(':')
            stored_hashes[relative_path] = int(file_hash)
    for root, _, files in os.walk(directory):
        for file in files:
            # Пропускаем файл с хэш-суммами
            if file == HASH_FILE:
                continue  
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            current_hash = calculate_hash(file_path)
            if relative_path in stored_hashes:
                if stored_hashes[relative_path] != current_hash:
                    print(f"Файл изменен: {relative_path}")
                del stored_hashes[relative_path]
            else:
                print(f"Новый файл: {relative_path}")
    for missing_file in stored_hashes:
        print(f"Файл отсутствует: {missing_file}")

if __name__ == "__main__":
    catalog = input("Введите путь к каталогу: ")
    action = input("Выберите действие (save/verify): ")
    if action == "save":
        save_hashes(catalog)
        print("Хэш-суммы сохранены.")
    elif action == "verify":
        verify_hashes(catalog)
        print("Проверка целостности завершена.")
    else:
        print("Неправильная команда.")