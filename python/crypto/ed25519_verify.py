#!/usr/bin/env python
# coding=utf-8
"""
Uses ed25519 to verify a signature for a specific message
"""
import sys

import colorama
from colorama import Fore
import ed25519


if __name__ == '__main__':
    colorama.init(autoreset=True)

    expected_args = 3
    received_args = len(sys.argv) - 1
    if received_args != expected_args:
        print(Fore.RED + 'require {} arguments, but received {}'.format(expected_args, received_args))
        print(Fore.CYAN + 'USAGE:  {} <private_keyfile> <file_to_verify> <signature_file>'.format(sys.argv[0]))
        sys.exit(1)

    key_filename = sys.argv[1]
    msg_filename = sys.argv[2]
    sig_filename = sys.argv[3]

    # Open the private key to a file and read data for both the private Signing key and public Verifying key
    with open(key_filename, 'rb') as key_file:
        keydata = key_file.read()

    # Reconstruct the SigningKey instance from the serialized form
    signing_key = ed25519.SigningKey(keydata)

    # Derive the VerifyingKey from the SigningKey
    verifying_key = signing_key.get_verifying_key()

    # Print out the public Verifying key
    vkey_hex = verifying_key.to_ascii(encoding="hex")
    print(Fore.LIGHTBLUE_EX + 'the public key is {}'.format(vkey_hex))

    # Open the input message file and read its data in as a message that we wish to verify a signature for
    with open(msg_filename, 'rb') as msg_file:
        msg = msg_file.read()

    # Open the signature file and read the signature
    with open(sig_filename, 'rb') as sig_file:
        sig = sig_file.read()

    # Use its .verify() method of the VerifyingKey on the signature and message
    try:
        verifying_key.verify(sig, msg)
        print(Fore.GREEN + "signature is good")
    except ed25519.BadSignatureError:
        print(Fore.RED + "signature is bad!")
