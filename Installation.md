# Dependencies #

You'll need to install the python lxml package.

On debian/ubuntu:
```
# apt-get install python-lxml
```

On gentoo:
```
# emerge dev-python/lxml
```

# Installation #

The python script needs to be in the same directory as the "xsl" directory.  Don't separate the two.

It's best to untar/checkout it to a directory and add that directory to your path.

Or just use the full path when calling:
```
/path/to/unix_security_file_parser.py -p audit/passwd
```

Also check out the UserGuide.