#!/usr/bin/env python

import six
import subprocess


def main():
    args = ["ls", "-l", "/dev/null"]
    if six.PY3:
        # The run function is present in Python 3.5 or newer
        completed_proc = subprocess.run(args, stdout=subprocess.PIPE)
        print(completed_proc.stdout)
    else:
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        print(p.stdout.read().strip())


if __name__ == '__main__':
    main()
