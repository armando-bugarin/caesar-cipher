import nltk
from nltk.corpus import words # Imports the "words" corpus from nltk, which contains a list of English words.
nltk.download('words') # Downloads the "words" corpus from nltk. This is necessary to access the list of English words later in the code.


def encrypt(plaintext, shift):
    encrypted_text = "" # initializes empty string to store encrypted text
    for char in plaintext: # iterates through each character in the plaintext
        if char.isalpha(): # checks if character is an alphabet letter
            if char.islower(): # checks if character is lowercase
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a')) # encrypts lowercase character by shift value
            elif char.isupper(): # checks if character is uppercase
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A')) # encrypts uppercase character by shift value
        else:
            encrypted_text += char # if not alphabet letter, just add it to the encrypted text

    return encrypted_text # returns encrypted text


def decrypt(encrypted, shift): 
    return encrypt(encrypted, -shift) # returns the decrypted text by subtracting the shift value from the encrypted text


def crack(ciphertext):
    max_word_count = 0
    best_shift = 0

    for shift in range(26): # iterates through all possible shift values (0-25)
        decrypted_text = decrypt(ciphertext, shift) # decrypts the ciphertext using the current shift value
        word_count = sum(word in words.words() for word in decrypted_text.split()) # counts number of valid english words in decrypted text
        if word_count > max_word_count: # if current shift produces more english words than previous shift
            max_word_count = word_count # update max_word_count with new count
            best_shift = shift # update best_shift with new shift value

    return decrypt(ciphertext, best_shift) # returns the decrypted text using the best shift value
