all: elgamal

elgamal: elgamal.c
	gcc -o elgamal elgamal.c -lgmp

clean:
	rm -f elgamal
