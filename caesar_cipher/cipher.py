import nltk
from nltk.corpus import words
nltk.download('words')

def encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(encrypted, shift):
    return encrypt(encrypted, -shift)


def crack(ciphertext):
    # Implementing a simple frequency analysis
    # and trying all possible shifts to find the one with the most English words
    max_word_count = 0
    best_shift = 0

    for shift in range(26):
        decrypted_text = decrypt(ciphertext, shift)
        word_count = sum(word in words.words() for word in decrypted_text.split())
        if word_count > max_word_count:
            max_word_count = word_count
            best_shift = shift

    return decrypt(ciphertext, best_shift)
