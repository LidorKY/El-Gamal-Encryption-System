import random
from sympy import isprime

def generate_keys(bit_length):
    # Generate a prime number q of bit_length - 1
    prime_q = 1
    while not isprime(prime_q):
        prime_q = random.getrandbits(bit_length - 1)

    # Generate a safe prime p = 2q + 1
    safe_prime_p = 2 * prime_q + 1
    while not isprime(safe_prime_p):
        prime_q = random.getrandbits(bit_length - 1)
        safe_prime_p = 2 * prime_q + 1
    print(f"Found safe prime: {safe_prime_p}")

    # Generate a generator g of the group
    generator_g = 2
    while pow(generator_g, prime_q, safe_prime_p) == 1 or pow(generator_g, 2, safe_prime_p) == 1:
        generator_g = random.randint(2, safe_prime_p - 2)
    print(f"Found generator: {generator_g}")

    # Generate private and public keys
    private_key_a = random.randint(1, prime_q)  # private key
    public_key_h = pow(generator_g, private_key_a, safe_prime_p)  # public key

    return (safe_prime_p, generator_g, public_key_h), private_key_a

def encrypt(public_key, message):
    safe_prime_p, generator_g, public_key_h = public_key
    # Generate a random number r
    random_num_r = random.randint(0, safe_prime_p - 2)
    # Compute s = g^r mod p
    ciphertext_s = pow(generator_g, random_num_r, safe_prime_p)
    # Compute t = m*h^r mod p
    ciphertext_t = (message * pow(public_key_h, random_num_r, safe_prime_p)) % safe_prime_p
    # Return the ciphertext (s,t)
    return ciphertext_s, ciphertext_t

def decrypt(private_key, ciphertext, public_key):
    ciphertext_s, ciphertext_t = ciphertext
    # Compute sa = s^a mod p
    decrypted_sa = pow(ciphertext_s, private_key, public_key[0])
    # Compute m = t/sa mod p
    decrypted_message = (ciphertext_t * pow(decrypted_sa, -1, public_key[0])) % public_key[0]
    # Return the decrypted message
    return decrypted_message

# Example usage:
public_keys, private_keys = generate_keys(100)
print(f"Public keys: {public_keys}")
print(f"Private key: {private_keys}")

ciphertext = encrypt(public_keys, 10)
print(f"Ciphertext: {ciphertext}")

plaintext = decrypt(private_keys, ciphertext, public_keys)
print(f"Decrypted message: {plaintext}")
