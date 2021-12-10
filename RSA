from cryptography.fernet import Fernet

# dummy password to encrypt
password = "rachel ayateke"

# generate key
key = Fernet.generate_key()

# Calling fernet class and pass it the generated key
fernet = Fernet(key)

# create variable for encrypted password with key
encrypted_password = fernet.encrypt(password.encode())

print("Password before encryption: ", password)
print("Password after encryption: ", encrypted_password)

# Decryption of the password
decrypted_password = fernet.decrypt(encrypted_password).decode()
print("Password after decryption: ", decrypted_password)