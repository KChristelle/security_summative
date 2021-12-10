# program imports
import os
import hashlib

# create a random 32-byte length salt
salting = os.urandom(32)
# password example to encode
password = 'r@che1'.encode()

# generate hash of password using sha256
disgest = hashlib.pbkdf2_hmac('sha256', password, salting, 10000)

# convert hash to hex string
hex_string_hash = disgest.hex()
print(hex_string_hash)
