#!/usr/bin/env python
# coding=utf-8
"""
Uses ed25519 to sign a message
"""
import sys

import colorama
from colorama import Fore
import ed25519


if __name__ == '__main__':
    colorama.init(autoreset=True)

    expected_args = 2
    received_args = len(sys.argv) - 1
    if received_args != expected_args:
        print(Fore.RED + 'require {} arguments, but received {}'.format(expected_args, received_args))
        print(Fore.CYAN + 'USAGE:  {} <private_keyfile> <file_to_sign>'.format(sys.argv[0]))
        sys.exit(1)

    key_filename = sys.argv[1]
    input_filename = sys.argv[2]
    output_filename = input_filename + '.sig'

    # The first step is to create a signing key and store it. The safest way to generate a key is with create_keypair()
    signing_key, verifying_key = ed25519.create_keypair()   # Generates a 32 byte SigningKey and 32 byte VerifyingKey

    # Open the private key to a file and read data for both the private Signing key and public Verifying key
    with open(key_filename, 'rb') as key_file:
        keydata = key_file.read()

    # Reconstruct the SigningKey instance from the serialized form
    signing_key = ed25519.SigningKey(keydata)

    # Print out the private Signing key
    skey_hex = signing_key.to_ascii(encoding="hex")
    print(Fore.LIGHTBLUE_EX + 'the private key is {}'.format(skey_hex))

    # Open the input file and read its data in as a message that we wish to sign
    with open(input_filename, 'rb') as msg_file:
        msg = msg_file.read()

    # Once you have the SigningKey instance, use its .sign() method to sign a message.
    # The signature is 64 bytes, but can be generated in printable form with the encoding= argument (e.g. "base64")
    sig = signing_key.sign(msg)

    # Save the signature to an output file
    with open(output_filename, 'wb') as sig_file:
        sig_file.write(sig)

    print(Fore.GREEN + 'Saved signature to {!r} for message file {!r}'.format(output_filename, input_filename))
