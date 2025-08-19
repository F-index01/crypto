import hashlib

def calculer_hash_avec_nonce(message, nonce):
    message_bytes = message.encode('utf-8')
    nonce_bytes = nonce.to_bytes(4, byteorder='big')  # 32 bits = 4 octets
    data = message_bytes + nonce_bytes
    return hashlib.sha256(data).digest()

def hash_commence_par_n_zero_bits(hash_bytes, n_bits):
    hash_int = int.from_bytes(hash_bytes, byteorder='big')
    return (hash_int >> (256 - n_bits)) == 0  # Vérifie les N bits de gauche

def chercher_nonces(message, n_bits, essais):
    nonces_trouves = []
    nonce = 0

    while len(nonces_trouves) < essais and nonce < 2**32:
        hash_result = calculer_hash_avec_nonce(message, nonce)
        if hash_commence_par_n_zero_bits(hash_result, n_bits):
            nonces_trouves.append(nonce)
            nonce += 1  # Continue après ce nonce
        else:
            nonce += 1

    return nonces_trouves

def main():
    message = input("Entre le message : ")
    essais = 10
    valeurs_n = [4, 8, 12]

    for n in valeurs_n:
        print(f"\n Recherche de {essais} nonces pour N = {n} bits à 0...")
        nonces = chercher_nonces(message, n, essais)
        print(f" Nonces trouvés pour N = {n} : {nonces}")

if __name__ == "__main__":
    main()
