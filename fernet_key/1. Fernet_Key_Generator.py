from cryptography.fernet import Fernet

# Generate a new Fernet key
key = Fernet.generate_key()

# Print the key - THIS IS YOUR SECRET KEY!
print("--- GENERATED FERNET KEY ---")
print("COPY THIS KEY AND SAVE IT IN AN EXTREMELY SECURE, SEPARATE PLACE:")
print(key.decode()) # .decode() converts the bytes to a string for easy copying
print("----------------------------")