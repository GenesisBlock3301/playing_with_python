from cryptography.fernet import Fernet

# generate key for encryption data
key = Fernet.generate_key()

# value of key is assigned to a variable
# and converted plaintext to ciphertext
encrypted_data = Fernet(key).encrypt(b"Welcome to bangladesh")

decrypted_data = Fernet(key).decrypt(encrypted_data)
print()
