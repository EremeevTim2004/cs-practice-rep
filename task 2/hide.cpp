#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

const std::vector<wchar_t> rus_letters = {L'а', L'е', L'о', L'р', L'с', L'у', L'х', L'А', L'В', L'Е', L'К', L'О', L'Р', L'С', L'Т', L'Х'};
const std::vector<wchar_t> eng_letters = {L'a', L'e', L'o', L'p', L'c', L'y', L'x', L'A', L'B', L'E', L'K', L'O', L'P', L'C', L'T', L'X'};

std::wstring text_to_bin(const std::wstring& text) {
    std::wstring binary_str;
    for (wchar_t ch : text) {
        binary_str += std::bitset<8>(static_cast<unsigned char>(ch)).to_string();
    }
    return binary_str;
}

std::wstring hide_info_in_container(const std::wstring& container, const std::wstring& secret_message_bin) {
    std::wstring container_with_hidden_info;
    size_t message_idx = 0;

    for (wchar_t ch : container) {
        if (message_idx < secret_message_bin.length() && std::find(rus_letters.begin(), rus_letters.end(), ch) != rus_letters.end()) {
            if (secret_message_bin[message_idx] == L'1') {
                // Заменяем русскую букву на английский аналог
                ch = eng_letters[std::distance(rus_letters.begin(), std::find(rus_letters.begin(), rus_letters.end(), ch))];
            }
            message_idx++;
        }
        container_with_hidden_info += ch;
    }

    return container_with_hidden_info;
}

int main() {
    std::wstring container_file = L"container.txt";
    std::wstring secret_message_file = L"secret.txt";
    std::wstring output_file = L"code.txt";

    std::wifstream container_f(container_file);
    std::wifstream secret_f(secret_message_file);
    std::wofstream output_f(output_file);

    if (!container_f.is_open() || !secret_f.is_open() || !output_f.is_open()) {
        std::wcerr << L"Ошибка при открытии файлов!" << std::endl;
        return 1;
    }

    std::wstring container_text((std::istreambuf_iterator<wchar_t>(container_f)), std::istreambuf_iterator<wchar_t>());
    std::wstring secret_message((std::istreambuf_iterator<wchar_t>(secret_f)), std::istreambuf_iterator<wchar_t>());

    std::wstring secret_message_bin = text_to_bin(secret_message);
    std::wstring container_with_hidden_info = hide_info_in_container(container_text, secret_message_bin);

    output_f << container_with_hidden_info;

    container_f.close();
    secret_f.close();
    output_f.close();

    return 0;
}
