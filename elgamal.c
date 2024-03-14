#include <stdio.h>
#include <stdlib.h>
#include <gmp.h>
#include <time.h>

// Function to generate keys
void generate_keys(mpz_t prime, mpz_t generator, mpz_t private_key, mpz_t public_key, gmp_randstate_t state) {
    mpz_urandomb(prime, state, 100); // Generate a random 100-bit number
    mpz_nextprime(prime, prime); // Find the next prime after prime

    mpz_set_ui(generator, 2); // Set generator to 2

    mpz_urandomb(private_key, state, 100); // Generate a random 100-bit number
    mpz_mod(private_key, private_key, prime); // Reduce private_key modulo prime

    mpz_powm(public_key, generator, private_key, prime); // Compute public_key = generator^private_key mod prime
}

// Function to encrypt a message
void encrypt(mpz_t ciphertext1, mpz_t ciphertext2, mpz_t message, mpz_t prime, mpz_t generator, mpz_t public_key, gmp_randstate_t state) {
    mpz_t ephemeral_key;
    mpz_init(ephemeral_key);

    mpz_urandomb(ephemeral_key, state, 100); // Generate a random 100-bit number
    mpz_mod(ephemeral_key, ephemeral_key, prime); // Reduce ephemeral_key modulo prime

    mpz_powm(ciphertext1, generator, ephemeral_key, prime); // Compute ciphertext1 = generator^ephemeral_key mod prime

    mpz_t shared_secret;
    mpz_init(shared_secret);
    mpz_powm(shared_secret, public_key, ephemeral_key, prime); // Compute shared_secret = public_key^ephemeral_key mod prime

    mpz_mul(ciphertext2, message, shared_secret);
    mpz_mod(ciphertext2, ciphertext2, prime); // Compute ciphertext2 = message * shared_secret mod prime

    mpz_clear(ephemeral_key);
    mpz_clear(shared_secret);
}

// Function to decrypt a message
void decrypt(mpz_t decrypted_message, mpz_t ciphertext1, mpz_t ciphertext2, mpz_t prime, mpz_t private_key) {
    mpz_t shared_secret;
    mpz_init(shared_secret);
    mpz_powm(shared_secret, ciphertext1, private_key, prime); // Compute shared_secret = ciphertext1^private_key mod prime

    mpz_invert(shared_secret, shared_secret, prime); // Compute shared_secret = shared_secret^-1 mod prime

    mpz_mul(decrypted_message, ciphertext2, shared_secret);
    mpz_mod(decrypted_message, decrypted_message, prime); // Compute decrypted_message = ciphertext2 * shared_secret mod prime

    mpz_clear(shared_secret);
}

int main() {
    gmp_randstate_t state;
    gmp_randinit_mt(state);
    gmp_randseed_ui(state, time(NULL)); // Seed the random number generator with the current time

    mpz_t prime, generator, private_key, public_key;
    mpz_inits(prime, generator, private_key, public_key, NULL);

    generate_keys(prime, generator, private_key, public_key, state);

    gmp_printf("Public key: prime = %Zd, generator = %Zd, public_key = %Zd\n", prime, generator, public_key);
    gmp_printf("Private key: private_key = %Zd\n", private_key);

    mpz_t message1, message2, message3;
    mpz_init_set_ui(message1, 123); // Set message1 to 123
    mpz_init_set_ui(message2, 456); // Set message2 to 456
    mpz_init_set_ui(message3, 789); // Set message3 to 789

    gmp_printf("Original messages: message1 = %Zd, message2 = %Zd, message3 = %Zd\n", message1, message2, message3);

    mpz_t ciphertext1_1, ciphertext2_1, ciphertext1_2, ciphertext2_2, ciphertext1_3, ciphertext2_3;
    mpz_inits(ciphertext1_1, ciphertext2_1, ciphertext1_2, ciphertext2_2, ciphertext1_3, ciphertext2_3, NULL);

    encrypt(ciphertext1_1, ciphertext2_1, message1, prime, generator, public_key, state);
    encrypt(ciphertext1_2, ciphertext2_2, message2, prime, generator, public_key, state);
    encrypt(ciphertext1_3, ciphertext2_3, message3, prime, generator, public_key, state);

    gmp_printf("Encrypted messages: ciphertext1_1 = %Zd, ciphertext2_1 = %Zd, ciphertext1_2 = %Zd, ciphertext2_2 = %Zd, ciphertext1_3 = %Zd, ciphertext2_3 = %Zd\n", ciphertext1_1, ciphertext2_1, ciphertext1_2, ciphertext2_2, ciphertext1_3, ciphertext2_3);

    mpz_t decrypted_message1, decrypted_message2, decrypted_message3;
    mpz_inits(decrypted_message1, decrypted_message2, decrypted_message3, NULL);

    decrypt(decrypted_message1, ciphertext1_1, ciphertext2_1, prime, private_key);
    decrypt(decrypted_message2, ciphertext1_2, ciphertext2_2, prime, private_key);
    decrypt(decrypted_message3, ciphertext1_3, ciphertext2_3, prime, private_key);

    gmp_printf("Decrypted messages: message1 = %Zd, message2 = %Zd, message3 = %Zd\n", decrypted_message1, decrypted_message2, decrypted_message3);

    mpz_clears(prime, generator, private_key, public_key, message1, message2, message3, ciphertext1_1, ciphertext2_1, ciphertext1_2, ciphertext2_2, ciphertext1_3, ciphertext2_3, decrypted_message1, decrypted_message2, decrypted_message3, NULL);
    gmp_randclear(state);

    return 0;
}
