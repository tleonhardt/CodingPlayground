#!/usr/bin/env python
# coding=utf-8
"""
Generates a random ed25519 SigningKey/VerifyingKey key pair for use with a digital signature system
"""
import sys

import colorama
from colorama import Fore
import ed25519


if __name__ == '__main__':
    colorama.init(autoreset=True)

    expected_args = 1
    received_args = len(sys.argv) - 1
    if received_args != expected_args:
        print(Fore.RED + 'require {} argument, but received {}'.format(expected_args, received_args))
        print(Fore.CYAN + 'USAGE:  {} <private_keyfile>'.format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]

    # The first step is to create a signing key and store it. The safest way to generate a key is with create_keypair()
    signing_key, verifying_key = ed25519.create_keypair()   # Generates a 32 byte SigningKey and 32 byte VerifyingKey

    # Save the private Signing key to a file along with the public Verifying Key
    with open(filename, 'wb') as key_file:
        # Saves 64 bytes (both keys) to a file
        key_file.write(signing_key.to_bytes())

    # Print out the public Verifying key
    vkey_hex = verifying_key.to_ascii(encoding="hex")
    print(Fore.GREEN + 'the  public key is {}'.format(vkey_hex))

    # Print out the private Signing key
    skey_hex = signing_key.to_ascii(encoding="hex")
    print(Fore.YELLOW + 'the private key is {}'.format(skey_hex))
