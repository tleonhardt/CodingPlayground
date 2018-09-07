Todd's conda constructor example
================================

In this example, I want to demonstrate how to build custom Python environment
installers for Linux, Mac and Windows, which are similar to Anaconda installers, but
significantly smaller in size and with precise versions of all packages.

We only want to construct installers which include:

- Python 3.6
- `cmd2`, so people can create awesome CLIs (includes cmd2 dependencies)
- `ipython`, to assist with debugging

We also want to include Anaconda's license file `EULA.txt`, which is located in this directory.

Finally, to create a cmd2conda installer, you simply run (in this directory):

    $ constructor .
    ...
    $ ls -lh cmd2*
    -rwxr-xr-x 1 todd todd  53M Sep  6 22:18 cmd2conda-1.0-Linux-x86_64.sh
    
This was done on Linux.

A 53 MB installer is not bad for all the packages it installs.  Python by itself
is around 26 MB and ipython is also quite large.

Note that `constructor` will by default create an installer for the platform
which it is executed on.  However, it is also possible to build installers
for other platforms.
