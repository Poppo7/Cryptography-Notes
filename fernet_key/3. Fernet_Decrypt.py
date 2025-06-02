from cryptography.fernet import Fernet
import os

# --- IMPORTANT: Load your SINGLE, SAVED FERNET KEY here ---
# Paste the ENTIRE key string (including the b'' and quotes) from your secure storage.
# Example: my_fernet_key_string = b'YOUR_ACTUAL_GENERATED_FERNET_KEY_HERE='
my_fernet_key_string = b'ukA1dXNQcDnhrl-s0fK086vEnxcBfnagGCdVyEVqRdw=' # <<< PASTE YOUR SAVED FERNET KEY HERE!
# Make sure this key matches the one used for encryption!

try:
    # Create a Fernet instance using your key
    cipher_suite = Fernet(my_fernet_key_string)
except ValueError:
    print("Error: Invalid Fernet key. Please ensure you pasted the exact key used for encryption.")
    exit()

# --- Input Directory (where encrypted files are) and Output Directory (for decrypted files) ---
# This script will ask you for the path to the folder containing the encrypted files.
# It will create a new subfolder named 'decrypted_files' inside that directory
# to save the decrypted files.
input_dir = input("Enter the FULL path to the directory containing the encrypted files (e.g., C:\\Users\\YourName\\Documents\\Subfolder\\encrypted_files): ")

if not os.path.isdir(input_dir):
    print(f"Error: Encrypted files directory not found at {input_dir}. Please check the path and try again.")
    exit()

# Renamed output subfolder to be generic and consistent
output_dir = os.path.join(input_dir, "decrypted_files") # Changed from 'decrypted_memory_files'
os.makedirs(output_dir, exist_ok=True) # Create output directory if it doesn't exist

# Define the extension used for encrypted files - THIS IS CRUCIAL
ENCRYPTED_EXTENSION = ".fernet_enc" # <<< THIS MUST MATCH THE EXTENSION FROM YOUR ENCRYPTION SCRIPT!

print(f"\nProcessing encrypted files in: {input_dir}")
print(f"Decrypted files will be saved in: {output_dir}\n")

processed_count = 0
for filename in os.listdir(input_dir):
    # Only process files ending with the specific encrypted extension
    # This was `.fernet` in your original script, but should be `.fernet_enc`
    if filename.endswith(ENCRYPTED_EXTENSION):
        input_filepath = os.path.join(input_dir, filename)

        # Remove the '.fernet_enc' extension to get the original filename with its original extension
        # THIS IS THE KEY TO RESTORING THE ORIGINAL FILE TYPE
        original_filename = filename.replace(ENCRYPTED_EXTENSION, "")
        output_filepath = os.path.join(output_dir, original_filename)

        try:
            # Read the encrypted data from the file
            with open(input_filepath, 'rb') as f_in:
                encrypted_data = f_in.read()

            # Decrypt the data
            decrypted_data = cipher_suite.decrypt(encrypted_data)

            # Write the decrypted data to the new file
            with open(output_filepath, 'wb') as f_out: # 'wb' for writing bytes - correct for any file type
                f_out.write(decrypted_data)

            print(f"  - Decrypted '{filename}' -> '{original_filename}' (Saved in {output_dir})")
            processed_count += 1
        except Exception as e:
            print(f"  - Error decrypting '{filename}': {e}")
            print(f"    Possible reasons: Incorrect Fernet key, file corruption, or tampering.")
            print(f"    Skipping this file.")

if processed_count == 0:
    print(f"\nNo files ending with '{ENCRYPTED_EXTENSION}' found or processed in the specified directory.")
else:
    print(f"\n--- Decryption process completed for {processed_count} file(s). ---")
    print(f"All decrypted files are in the subfolder: '{output_dir}'")
    print("These are the decrypted files, restored to their original format!")