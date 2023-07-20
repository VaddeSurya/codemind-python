vowels = "AEIOUaeiou"
word = input()
first_letter = word[0]

if first_letter in vowels:
    print("VOWEL")
else:
    print("CONSONANT")
