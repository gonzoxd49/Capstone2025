from werkzeug.security import generate_password_hash

# This generates the hash
secret_hash = generate_password_hash('Capstone2025Theater!', method='pbkdf2:sha256', salt_length=16)

print("--- COPY THE LINE BELOW ---")
print(secret_hash)
print("---------------------------")