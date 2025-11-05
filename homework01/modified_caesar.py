def decrypt_growing_shift(ciphertext: str, start: int, delta: int) -> str:
    plaintext = ""
    current_shift = start
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                first, last = ord("А"), ord("Я")
            else:
                first, last = ord("а"), ord("я")
            new_code = ord(char) - current_shift
            if new_code > last:
                new_code -= 32
            if new_code < first:
                new_code += 32
            current_shift += delta
            plaintext += chr(new_code)
        else:
            plaintext += char
    return plaintext
