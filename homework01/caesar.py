def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    first_up, last_up = ord("A"), ord("Z")
    first_low, last_low = ord("a"), ord("z")
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                first, last = first_up, last_up
            else:
                first, last = first_low, last_low

            new_code = ord(char) + shift

            if new_code > last:
                new_code -= 26
            elif new_code < first:
                new_code += 26

            ciphertext += chr(new_code)
        else:
            ciphertext += char

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    first_up, last_up = ord("A"), ord("Z")
    first_low, last_low = ord("a"), ord("z")
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                first, last = first_up, last_up
            else:
                first, last = first_low, last_low
            new_code = ord(char) - shift
            if new_code > last:
                new_code -= 26
            if new_code < first:
                new_code += 26
            plaintext += chr(new_code)
        else:
            plaintext += char
    return plaintext
