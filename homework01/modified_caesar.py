def decrypt_growing_shift(ciphertext: str, start: int, delta: int) -> str:
    plaintext = ""
    current_shift = start
    first_up, last_up = ord("А"), ord("Я")
    first_low, last_low = ord("а"), ord("я")
    alphabet_size = 32
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                first, last = first_up, last_up
            else:
                first, last = first_low, last_low
            new_code = ord(char) - current_shift
            if new_code < first:
                diff = first - new_code
                cycles = (diff - 1) // alphabet_size + 1  # смотрим, на сколько полных алфавитов мы отдалились
                new_code += cycles * alphabet_size
            if new_code > last:
                diff = new_code - last
                cycles = (diff - 1) // alphabet_size + 1
                new_code -= cycles * alphabet_size
            current_shift += delta
            plaintext += chr(new_code)
        else:
            plaintext += char
    return plaintext
