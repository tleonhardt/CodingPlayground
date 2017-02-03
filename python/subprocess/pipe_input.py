#!/usr/bin/env python

import subprocess


def main():
    piped_in = b'this is a test\n'
    args = ["wc"]

    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate(input=piped_in)
    print("out = {},  err = {}".format(out, err))


if __name__ == '__main__':
    main()
