# El-Gamal-Encryption-System

This repository contains a C implementation of the ElGamal encryption system, a public-key cryptosystem that uses asymmetric key encryption for secure communication.

## Description

The ElGamal encryption system is based on the difficulty of finding discrete logarithm in a cyclic group. It involves three main steps:

1. **Key Generation**: A large prime number and a generator of the cyclic group are chosen. A private key is randomly selected and a public key is computed.

2. **Encryption**: A random number is chosen and used along with the public key to encrypt the message.

3. **Decryption**: The shared secret and the ciphertext are used to compute the original message.

## Files

- `elgamal.c`: This is the main C script that implements the ElGamal encryption system.

## Installation

Before running the code, you need to install the GMP library. You can do this on Ubuntu by running the following command in your terminal:

```bash
sudo apt-get install libgmp-dev
```

## Usage

To run the code, simply execute the following commands in your terminal:

```bash
make
./elgamal
```

This will compile the `elgamal.c` file into an executable named `elgamal` using the GCC compiler and then run it. It will generate a public and private key, encrypt a set of messages, and then decrypt them to recover the original messages.

## Output

The script prints the public and private keys, the original messages, the encrypted messages (ciphertexts), and the decrypted messages.

## Note

This is a simplified example, and actual cryptographic applications would use much larger numbers to ensure security. The security of the ElGamal encryption system relies on the discrete logarithm problem being difficult to solve.
