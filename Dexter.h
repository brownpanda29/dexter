#ifndef DEXTER_H
#define DEXTER_H

#include <string>
#include <sstream>
#include <iomanip>
#include <cstdlib>
#include <ctime>
#include <stdexcept>

class Dexter {
private:
    int min_shift;
    int max_shift;

public:
    // Constructor to initialize the shift range and random seed
    Dexter(int min_shift = 10, int max_shift = 50, int seed = -1)
        : min_shift(min_shift), max_shift(max_shift) {
        if (seed != -1) {
            std::srand(seed);  // Initialize random seed if provided
        } else {
            std::srand(static_cast<unsigned int>(std::time(nullptr)));  // Otherwise, use current time for seed
        }
    }

    // Encode method to encode a string with random shifts and return the result in hexadecimal format
    std::string encode(const std::string& data) {
        std::stringstream encoded_data;
        for (char c : data) {
            // Generate a random shift in the given range
            int shift = rand() % (max_shift - min_shift + 1) + min_shift;

            // Shift the character within the ASCII range (0-255)
            char shifted_char = static_cast<char>((static_cast<unsigned char>(c) + shift) % 256);

            // Convert the shift and shifted character to hexadecimal
            encoded_data << std::setw(2) << std::setfill('0') << std::hex << shift;
            encoded_data << std::setw(2) << std::setfill('0') << std::hex << static_cast<int>(shifted_char);
        }
        return encoded_data.str();
    }

    // Decode method to reverse the encoding and restore the original string
    std::string decode(const std::string& encoded_data) {
        if (encoded_data.length() % 4 != 0) {
            throw std::invalid_argument("Encoded data length is incorrect. It must be a multiple of 4.");
        }

        std::stringstream decoded_data;
        for (size_t i = 0; i < encoded_data.length(); i += 4) {
            // Extract the 2-digit shift value and the 2-digit shifted character
            std::string shift_hex = encoded_data.substr(i, 2);
            std::string shifted_char_hex = encoded_data.substr(i + 2, 2);

            // Convert the hexadecimal values back to integers
            int shift = std::stoi(shift_hex, nullptr, 16);
            int shifted_char_int = std::stoi(shifted_char_hex, nullptr, 16);

            // Reverse the shift to find the original character
            char original_char = static_cast<char>((shifted_char_int - shift + 256) % 256);
            decoded_data << original_char;
        }

        return decoded_data.str();
    }
};

// Wrapper functions for easy use
inline std::string encode(const std::string& data, Dexter& dexter) {
    return dexter.encode(data);
}

inline std::string decode(const std::string& encoded_data, Dexter& dexter) {
    return dexter.decode(encoded_data);
}

#endif // DEXTER_H
