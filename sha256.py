import hashlib

def hash_sha256(input_data):
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the input data (must be in bytes)
    sha256.update(input_data.encode('utf-8'))

    # Return the hexadecimal digest of the hash
    return sha256.hexdigest()

# Ask the user for input
user_input = input("Enter the text you want to hash with SHA-256: ")

# Generate and print the SHA-256 hash
hash_value = hash_sha256(user_input)
print(f"SHA-256 hash of '{user_input}': {hash_value}")
