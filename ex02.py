from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA key pair
def generate_keys():
    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()
    return public_key, private_key

# Hash a message using SHA-256
def compute_hash(message):
    if isinstance(message, str):
        message = message.encode()
    return SHA256.new(message)

# Sign a hash
def sign_hash(hash_obj, private_key):
    return pkcs1_15.new(private_key).sign(hash_obj)

# Main blockchain-like chaining process
def main():
    public_key, private_key = generate_keys()
    pub_pem = public_key.export_key().decode()

    # Step 1
    msg1 = "Bonjour le monde !" + pub_pem
    h1_1 = compute_hash(msg1)
    sig1 = sign_hash(h1_1, private_key)
    h1_2 = compute_hash(sig1)

    print("--- Étape 1 ---")
    print("Haché1.1 :", h1_1.hexdigest())
    print("Signature1 :", sig1.hex())
    print("Haché1.2 :", h1_2.hexdigest())

    # Step 2
    msg2 = h1_2.hexdigest() + pub_pem
    h2_1 = compute_hash(msg2)
    sig2 = sign_hash(h2_1, private_key)
    h2_2 = compute_hash(sig2)

    print("\n--- Étape 2 ---")
    print("Haché2.1 :", h2_1.hexdigest())
    print("Signature2 :", sig2.hex())
    print("Haché2.2 :", h2_2.hexdigest())

    # Step 3
    msg3 = h2_2.hexdigest() + pub_pem
    h3_1 = compute_hash(msg3)
    sig3 = sign_hash(h3_1, private_key)
    h3_3 = compute_hash(sig3)

    print("\n--- Étape 3 ---")
    print("Haché3.1 :", h3_1.hexdigest())
    print("Signature3 :", sig3.hex())
    print("Haché3.3 (Final) :", h3_3.hexdigest())

if __name__ == "__main__":
    main()
