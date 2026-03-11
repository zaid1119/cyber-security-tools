from cryptography.fernet import Fernet

# 1. Generate a Secret Key (In your report, explain this is AES-256)
key = Fernet.generate_key()
cipher = Fernet(key)

print("="*50)
print("   ONEIX - CRYPTO-VAULT (AES)")
print("="*50)

# 2. Get user input
message = input("Enter the secret message to encrypt: ")

# 3. Encrypt the data
encrypted_data = cipher.encrypt(message.encode())
print(f"\n[+] Encrypted (Ciphertext): {encrypted_data.decode()}")

# 4. Decrypt it back
decrypted_data = cipher.decrypt(encrypted_data)
print(f"[+] Decrypted (Original): {decrypted_data.decode()}")
print("="*50)