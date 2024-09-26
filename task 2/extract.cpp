#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

const std::vector<wchar_t> rus_letters = {L'а', L'е', L'о', L'р', L'с', L'у', L'х', L'А', L'В', L'Е', L'К', L'О', L'Р', L'С', L'Т', L'Х'};
const std::vector<wchar_t> eng_letters = {L'a', L'e', L'o', L'p', L'c', L'y', L'x', L'A', L'B', L'E', L'K', L'O', L'P', L'C', L'T', L'X'};

std::wstring bin_to_text(const std::wstring& bin_str) {
    std::wstring text;
    for (size_t i = 0; i < bin_str.length(); i += 8) {
        std::bitset<8> byte(bin_str.substr(i, 8));
        text += static_cast<wchar_t>(byte.to_ulong());
    }
    return text;
}

std::wstring extract_info_from_container(const std::wstring& container) {
    std::wstring secret_message_bin;

    for (wchar_t ch : container) {
        if (std::find(rus_letters.begin(), rus_letters.end(), ch) != rus_letters.end()) {
            secret_message_bin += L'0'; // Бит = 0
        } else if (std::find(eng_letters.begin(), eng_letters.end(), ch) != eng_letters.end()) {
            secret_message_bin += L'1'; // Бит = 1
        }
    }

    return secret_message_bin;
}

int main() {
    std::wstring container_with_hidden_info_file = L"code.txt";
    std::wstring output_secret_message_file = L"message.txt";

    std::wifstream container_f(container_with_hidden_info_file);
    std::wofstream output_f(output_secret_message_file);

    if (!container_f.is_open() || !output_f.is_open()) {
        std::wcerr << L"Ошибка при открытии файлов!" << std::endl;
        return 1;
    }

    std::wstring container_text((std::istreambuf_iterator<wchar_t>(container_f)), std::istreambuf_iterator<wchar_t>());
    
    // Извлечение бинарного сообщения
    std::wstring secret_message_bin = extract_info_from_container(container_text);
    
    // Преобразование бинарного сообщения в текст
    std::wstring secret_message = bin_to_text(secret_message_bin);

    output_f << secret_message;

    container_f.close();
    output_f.close();

    return 0;
}
