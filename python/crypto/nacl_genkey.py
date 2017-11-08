#!/usr/bin/env python
# coding=utf-8
"""
Generates a random ed25519 SigningKey/VerifyingKey key pair for use with a digital signature system using PyNaCl
"""
import sys

import colorama
from colorama import Fore
from nacl.encoding import HexEncoder
from nacl.signing import SigningKey


if __name__ == '__main__':
    colorama.init(autoreset=True)

    expected_args = 2
    received_args = len(sys.argv) - 1
    if received_args != expected_args:
        print(Fore.RED + 'require {} argument, but received {}'.format(expected_args, received_args))
        print(Fore.CYAN + 'USAGE:  {} <private_keyfile> <public_keyfile>'.format(sys.argv[0]))
        sys.exit(1)

    private_filename = sys.argv[1]
    public_filename = sys.argv[2]

    # Generate a new random private SigningKey for producing digital signatures using the Ed25519 algorithm
    signing_key = SigningKey.generate()

    # Extract the public VerifyingKey counterpart for verifying digital signatures created with the SigningKey
    verify_key = signing_key.verify_key

    # Specify an NaCL encoder
    nacl_encoder = HexEncoder

    # Serialize the signing key to save it to a file
    signing_hex = signing_key.encode(encoder=nacl_encoder)

    # Serialize the verify key to send it to a third party
    verify_hex = verify_key.encode(encoder=nacl_encoder)

    # Save the private Signing key to a file
    with open(private_filename, 'wb') as private_file:
        # Saves 64 bytes (both keys) to a file
        private_file.write(signing_hex)

    # Save the public Verifying key to a file
    with open(public_filename, 'wb') as public_file:
        # Saves 64 bytes (both keys) to a file
        public_file.write(verify_hex)

    # Print out the public Verifying key
    print(Fore.GREEN + 'the  public key is {}'.format(verify_hex))

    # Print out the private Signing key
    print(Fore.YELLOW + 'the private key is {}'.format(signing_hex))
