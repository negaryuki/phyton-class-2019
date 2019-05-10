text = ["hello darkness my old friend"]


def get_vowel(text):
    words = text.split()
    vowel = []
    for w in words:
        if w[0] in 'aeiou':
            vowel.append(w)
            print(w)
        return vowel

