# ElGamal Encryption System in Python

This repository contains a Python implementation of the ElGamal encryption system, a public-key cryptosystem that uses asymmetric key encryption for secure communication.

## Description

The ElGamal encryption system is based on the difficulty of finding discrete logarithm in a cyclic group. It involves three main steps:

1. **Key Generation**: A large prime number and a generator of the cyclic group are chosen. A private key is randomly selected and a public key is computed.

2. **Encryption**: A random number is chosen and used along with the public key to encrypt the message.

3. **Decryption**: The shared secret and the ciphertext are used to compute the original message.

## Files

- `elgamal.py`: This is the main Python script that implements the ElGamal encryption system.

## Installation

Before running the code, you need to install the sympy library. You can do this by running the following command in your terminal:

```bash
pip install sympy
```

## Usage

To run the code, simply execute the following command in your terminal:

```bash
python elgamal.py
```

This will run the `elgamal.py` script. It will generate a public and private key, encrypt a message, and then decrypt it to recover the original message.

## Output

The script prints the public and private keys, the original message, the encrypted message (ciphertext), and the decrypted message.

## Note

This is a simplified example, and actual cryptographic applications would use much larger numbers to ensure security. The security of the ElGamal encryption system relies on the discrete logarithm problem being difficult to solve. The provided Python code uses 100-bit prime numbers, but real-world applications would use larger primes for increased security.
