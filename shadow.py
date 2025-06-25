def is_shadow(sentence1, sentence2):
    words = sentence1.split()
    words1 = sentence2.split()

    if len(words) != len(words1):
        return False
    for word, word1 in zip(words, words1):
        if len(word) != len(word1):
            return False
        for ch1, ch2 in zip(word, word1):
            if ch1 == ch2:
                return False
    return True
s1 = input()
s2 = input()
is_shadow(s1, s2)