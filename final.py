compression_table = {
    ' ': '0000000',
    'e': '0000001',
    't': '0000010',
    'a': '0000011',
    'o': '0000100',
    'n': '0000101',
    's': '0000110',
    'r': '0000111',
    'i': '0001000',
    'l': '0001001',
    'c': '0001010',
    'd': '0001011',
    'h': '0001100',
    'u': '0001101',
    'p': '0001110',
    'm': '0001111',
    '.': '0010000',
    ',': '0010001',
    'g': '0010010',
    'b': '0010011',
    'y': '0010100',
    'w': '0010101',
    'f': '0010110',
    'k': '0010111',
    'x': '0011000',
    'j': '0011001',
    'q': '0011010',
    'z': '0011011',
    'A': '0011100', 'B': '0011101', 'C': '0011110', 'D': '0011111',
    'E': '0100000', 'F': '0100001', 'G': '0100010', 'H': '0100011',
    'I': '0100100', 'J': '0100101', 'K': '0100110', 'L': '0100111',
    'M': '0101000', 'N': '0101001', 'O': '0101010', 'P': '0101011',
    'Q': '0101100', 'R': '0101101', 'S': '0101110', 'T': '0101111',
    'U': '0110000', 'V': '0110001', 'W': '0110010', 'X': '0110011',
    'Y': '0110100', 'Z': '0110101',
    '0': '0110110', '1': '0110111', '2': '0111000', '3': '0111001',
    '4': '0111010', '5': '0111011', '6': '0111100', '7': '0111101',
    '8': '0111110', '9': '0111111',
    '-': '1000000', '!': '1000001', "'": '1000010', '"': '1000011',
    '\n': '1000100', '#': '1000101',
    'th': '10010000', 'he': '10010001', 'in': '10010010', 'er': '10010011',
    'an': '10010100', 're': '10010101', 'on': '10010110', 'at': '10010111',
    'en': '10011000', 'nd': '10011001', 'to': '10011010', 'ed': '10011011',
    'it': '10011100', 'or': '10011101', 'ha': '10011110', 'of': '10011111',
    'the': '101000000', 'and': '101000001', 'ing': '101000010',
    'ion': '101000011', 'ent': '101000100', 'her': '101000101',
    'for': '101000110', 'tha': '101000111', 'ere': '101001000',
    'ter': '101001001', 'est': '101001010', 'ers': '101001011'
}

def compress_text(text):
    compressed = ""
    i = 0
    while i < len(text):
        if text[i:i+3] in compression_table:
            compressed += compression_table[text[i:i+3]]
            i += 3
        elif text[i:i+2] in compression_table:
            compressed += compression_table[text[i:i+2]]
            i += 2
        elif text[i] in compression_table:
            compressed += compression_table[text[i]]
            i += 1
        else:
            compressed += compression_table['#']
            i += 1
    return compressed
def decompress_text(compressed):
    decompressed = ""
    buffer = ""
    for bit in compressed:
        buffer += bit
        for char, code in compression_table.items():
            if buffer == code:
                decompressed += char
                buffer = ""
                break
    if buffer:
        decompressed += "#"
    return decompressed

def run_from_file(filename): #new
    with open(filename, "r") as f:
        text = f.read()

    compressed = compress_text(text)
    decompressed = decompress_text(compressed)

    print("Compressed binary:", compressed)
    print("Decompressed text:", decompressed)

    matches = sum(1 for a, b in zip(text, decompressed) if a == b)
    accuracy = (matches / len(text)) * 100 if len(text) > 0 else 0
    print("Compression accuracy:", round(accuracy, 2), "%")

    original_bits = len(text) * 8
    compressed_bits = len(compressed)
    reduction = 100 * (1 - compressed_bits / original_bits) if original_bits > 0 else 0
    print("Bit reduction:", round(reduction, 2), "%")

filename = input("Enter the file name to open: ")
run_from_file(filename)
