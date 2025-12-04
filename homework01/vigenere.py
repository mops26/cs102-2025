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
    key_length = len(keyword)
    keyword = keyword.upper()
    multiplier = len(plaintext) // key_length + 1
    new_key = keyword * multiplier
    first_up, last_up = ord("A"), ord("Z")
    last_low = ord("z")
    for char, key_char in zip(plaintext, new_key):
        if char.isalpha():
            shift = ord(key_char) - first_up
            if char.isupper():
                new_char_code = ord(char) + shift
                if new_char_code > last_up:
                    new_char_code -= 26
                ciphertext += chr(new_char_code)
            else:
                new_char_code = ord(char) + shift
                if new_char_code > last_low:
                    new_char_code -= 26
                ciphertext += chr(new_char_code)
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
    key_length = len(keyword)
    keyword = keyword.upper()
    multiplier = len(ciphertext) // key_length + 1
    new_key = keyword * multiplier
    first_up, last_up = ord("A"), ord("Z")
    first_low = ord("a")
    for char, key_char in zip(ciphertext, new_key):
        if char.isalpha():
            shift = ord(key_char) - first_up
            if char.isupper():
                new_char_code = ord(char) - shift
                if new_char_code < first_up:
                    new_char_code += 26
                plaintext += chr(new_char_code)
            else:
                new_char_code = ord(char) - shift
                if new_char_code < first_low:
                    new_char_code += 26
                plaintext += chr(new_char_code)
        else:
            plaintext += char

    return plaintext
