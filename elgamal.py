import random
from sympy import isprime


def find_generator(prime_number):
    '''Find a generator of the cyclic group Z_p*.

    Args:
        prime_number (int): The prime number defining the group.

    Returns:
        int: A generator of the group.
    '''
    # Loop over potential generators
    for potential_generator in range(2, prime_number):

        # Check if the potential generator is a generator of the group
        if all(pow(potential_generator, (prime_number - 1) // q, prime_number) != 1 for q in
               [2, (prime_number - 1) // 2]):
            return potential_generator
    return None


def generate_keys(byte_size):
    '''Generate the public and private keys for ElGamal encryption.

    Args:
        byte_size (int): The size of the prime number in bytes.

    Returns:
        tuple: The prime number, generator, public key, and private key.
    '''
    # Generate a prime number of the given byte size
    prime_number = random.getrandbits(byte_size * 8)

    while not isprime(prime_number):
        prime_number = random.getrandbits(byte_size * 8)

    # Find a generator of the cyclic group
    generator = find_generator(prime_number)

    # Generate a private key
    private_key = random.randint(1, prime_number - 2)

    # Compute the public key
    public_key = pow(generator, private_key, prime_number)

    return prime_number, generator, public_key, private_key


def encrypt(prime_number, generator, public_key, message):
    '''Encrypt a message using ElGamal encryption.

    Args:
        prime_number (int): The prime number from the public key.
        generator (int): The generator from the public key.
        public_key (int): The public key.
        message (int): The message to encrypt.

    Returns:
        tuple: The two parts of the ciphertext.
    '''
    # Generate a random number
    random_number = random.randint(1, prime_number - 2)

    # Compute the first part of the ciphertext
    ciphertext1 = pow(generator, random_number, prime_number)

    # Compute the shared secret
    shared_secret = pow(public_key, random_number, prime_number)

    # Compute the second part of the ciphertext
    ciphertext2 = (message * shared_secret) % prime_number

    return ciphertext1, ciphertext2


def decrypt(prime_number, private_key, ciphertext1, ciphertext2):
    '''Decrypt a ciphertext using ElGamal decryption.

    Args:
        prime_number (int): The prime number from the public key.
        private_key (int): The private key.
        ciphertext1 (int): The first part of the ciphertext.
        ciphertext2 (int): The second part of the ciphertext.

    Returns:
        int: The decrypted message.
    '''
    # Compute the shared secret
    shared_secret = pow(ciphertext1, private_key, prime_number)

    # Compute the original message
    message = (ciphertext2 * pow(shared_secret, prime_number - 2, prime_number)) % prime_number
    return message


def main():
    byte_size = 100 # parameter betihut or paranoidic parameter
    prime_number, generator, public_key, private_key = generate_keys(byte_size)
    print(f"Prime number = {prime_number}")
    print(f"Generator = {generator}")
    print(f"Public key = {public_key}")
    print(f"Private key: {private_key}")

    messages = [123, 456, 789]
    for message in messages:
        print(f"\nOriginal message: {message}")
        ciphertext1, ciphertext2 = encrypt(prime_number, generator, public_key, message)
        print(f"Encrypted message: (Ciphertext1 = {ciphertext1}, Ciphertext2 = {ciphertext2})")
        decrypted_message = decrypt(prime_number, private_key, ciphertext1, ciphertext2)
        print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
