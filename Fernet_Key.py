from cryptography.fernet import Fernet

# Step 1: Generate a fresh key
key = Fernet.generate_key()
cipher = Fernet(key)
print(f"Generated Key (store safely): {key}")

# Step 2: Encrypt a test message
original_message = b"Test encryption message"
encrypted_message = cipher.encrypt(original_message)
print(f"Encrypted Message: {encrypted_message}")

# Step 3: Decrypt to verify
try:
    decrypted_message = cipher.decrypt(encrypted_message)
    print(f"Decrypted Message: {decrypted_message.decode()}")
except Exception as e:
    print(f"Decryption Error: {e}")
