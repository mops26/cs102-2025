def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword = keyword.upper()
    key_length = len(keyword)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            key_char = keyword[key_index]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                new_char_code = ord(char) + shift
                if new_char_code > ord('Z'):
                    new_char_code -= 26
                ciphertext += chr(new_char_code)
            else:
                new_char_code = ord(char) + shift
                if new_char_code > ord('z'):
                    new_char_code -= 26
                ciphertext += chr(new_char_code)
            key_index += 1
            if key_index == key_length:
                key_index = 0
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""

    keyword = keyword.upper()
    key_length = len(keyword)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = keyword[key_index]
            shift = ord(key_char) - ord('A')
            if char.isupper():
                new_char_code = ord(char) - shift
                if new_char_code < ord('A'):
                    new_char_code += 26
                plaintext += chr(new_char_code)
            else:
                new_char_code = ord(char) - shift
                if new_char_code < ord('a'):
                    new_char_code += 26
                plaintext += chr(new_char_code)
            key_index += 1
            if key_index == key_length:
                key_index = 0
        else:
            plaintext += char

    return plaintext