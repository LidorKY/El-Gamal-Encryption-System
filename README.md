# El-Gamal-Encryption-System

This repository contains a Python implementation of the ElGamal encryption system, a public-key cryptosystem that uses asymmetric key encryption for secure communication.

## Description

The ElGamal encryption system is based on the difficulty of finding discrete logarithm in a cyclic group. It involves three main steps:

1. **Key Generation**: A large prime number and a generator of the cyclic group are chosen. A private key is randomly selected and a public key is computed.

2. **Encryption**: A random number is chosen and used along with the public key to encrypt the message.

3. **Decryption**: The shared secret and the ciphertext are used to compute the original message.

## Files

- `elgamal.py`: This is the main Python script that implements the ElGamal encryption system.

- `example1.txt`, `example2.txt`, `example3.txt`: These files contain the output of three different runs of the code.

## Usage

To run the code, simply execute the Python script `elgamal.py`. It will generate a public and private key, encrypt a set of messages, and then decrypt them to recover the original messages.

```bash
python elgamal.py


## Output

The script prints the public and private keys, the original messages, the encrypted messages (ciphertexts), and the decrypted messages. For example outputs, refer to the `example1.txt`, `example2.txt`, and `example3.txt` files.

## Note

This is a simplified example, and actual cryptographic applications would use much larger numbers to ensure security. The security of the ElGamal encryption system relies on the discrete logarithm problem being difficult to solve.


