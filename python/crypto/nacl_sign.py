#!/usr/bin/env python
# coding=utf-8
"""
Uses PyNaCl to sign a message using ed25519 digital signature algorithm
"""
import sys

import colorama
from colorama import Fore
from nacl.encoding import HexEncoder
from nacl.signing import SigningKey


if __name__ == '__main__':
    colorama.init(autoreset=True)

    expected_args = 3
    received_args = len(sys.argv) - 1
    if received_args != expected_args:
        print(Fore.RED + 'require {} arguments, but received {}'.format(expected_args, received_args))
        print(Fore.CYAN + 'USAGE:  {} <private_keyfile> <file_to_sign> <signature_file>'.format(sys.argv[0]))
        sys.exit(1)

    key_filename = sys.argv[1]
    input_filename = sys.argv[2]
    output_filename = sys.argv[3]

    # Open the private key to a file and read data for both the private Signing key and public Verifying key
    with open(key_filename, 'rb') as key_file:
        keydata_hex = key_file.read()

    # Specify an NaCL encoder
    nacl_encoder = HexEncoder

    # Reconstruct the SigningKey instance from the serialized form
    signing_key = SigningKey(keydata_hex, encoder=nacl_encoder)

    # Print out the private Signing key
    print(Fore.LIGHTBLUE_EX + 'the private key is {}'.format(keydata_hex))

    # Open the input file and read its data in as a message that we wish to sign
    with open(input_filename, 'rb') as msg_file:
        msg = msg_file.read()

    # Sign a message with the signing key - this also containes the original message at the end
    sig = signing_key.sign(msg)

    # Save the signature to an output file
    with open(output_filename, 'wb') as sig_file:
        sig_file.write(sig)

    print(Fore.GREEN + 'Saved signature to {!r} for message file {!r}'.format(output_filename, input_filename))
