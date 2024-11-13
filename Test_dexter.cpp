#include <iostream>
#include "Dexter.h"

int main() {
    // Create an instance of Dexter with default values
    Dexter dexter;

    std::string input = "Hello, World!";
    std::cout << "Original data: " << input << std::endl;

    // Encode the data
    std::string encoded = encode(input, dexter);
    std::cout << "Encoded data: " << encoded << std::endl;

    // Decode the data
    std::string decoded = decode(encoded, dexter);
    std::cout << "Decoded data: " << decoded << std::endl;

    return 0;
}
