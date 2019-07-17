raw = list(str(input()))

no_vowel = [char for char in raw if char != "a" and char != "i" and char != "u" and char != "e" and \
    char != "o" and char != "y" and char != "A" and char != "I" and char != "U" and char != "E" and \
        char != "O" and char != "Y"]
changed_consonant = ["." + char.lower() for char in no_vowel]
print("".join(changed_consonant))