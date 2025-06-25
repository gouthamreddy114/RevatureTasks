def text_to_morse(s):
    morse_code_dict = {
        'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',
        '.': '.-.-.-', ',': '--..--', ':': '---...',
        '?': '..--..', "'": '.----.', '!': '-.-.--',
        ' ': '/'
    }

    s = s.upper()
    morse_words = []

    for word in s.split(' '):
        morse_letters = []
        for char in word:
            if char in morse_code_dict:
                morse_letters.append(morse_code_dict[char])
        morse_words.append(' '.join(morse_letters))
    
    return '  '.join(morse_words)