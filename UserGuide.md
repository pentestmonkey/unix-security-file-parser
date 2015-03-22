# Usage #

```
$ unix_security_file_parser.py -h
unix_security_file_parser v0.1svn0 (http://pentestmonkey.net/unix_security_file_parser)

Usage: /home/x/workspace/unix-security-file-parser/unix_security_file_parser.py ( file-options | bulk-options ) -o report-file-stem

A tool for identifying security problems in Unix configuration files.
It is assumed that you have copied the relevant files from the target system
to the system you are running unix_security_file_parser from.

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit

  file-options:
    At least one of these to indicate what to examine

    -p PASSWD_FILE, --passwd=PASSWD_FILE
                        /etc/passwd file
    -s SHADOW_FILE, --shadow=SHADOW_FILE
                        /etc/shadow file
    -S SUDOERS_FILE, --sudoers=SUDOERS_FILE
                        /etc/sudoers file
    -P PERMS_FILE, --perms=PERMS_FILE
                        Output of: find / -ls
    -H SSHD_CONFIG_FILE, --sshd_config=SSHD_CONFIG_FILE
                        /etc/ssh/sshd_config
    -u UPC_FILE, --upc=UPC_FILE
                        Output of: unix-privesc-check standard|detailed

  report-options:
    Reporting options

    -o REPORT_FILE_STEM, --report_file_stem=REPORT_FILE_STEM
                        Filename stem for txt, html report files
```

# Use Case #1: Automatically Parse Files In A Directory Tree #

unix\_security\_file\_parser can walk through a directory structure looking for files that it knows how to audit:
```
$ unix_security_file_parser.py -d path/to/audit/data -o myreport
```

This will create the files "myreport.txt" and "myreport.html".

Only the filename is used to determine which files get parsed.  The -d option is intended to be used on a small directory tree containing data you collected from another host.  Don't pass "-d /".

# Use Case #2: Parse Specific Files #

You can specify the individual files you want to parse like this:

```
$ unix_security_file_parser.py -P ./find-ls.txt -p audit/passwd -s audit/shadow -S audit/sudoers -H /some/path/sshd_config -o myreport
```

You don't one file of each type.  You just need at least one file to parse.

# FAQ #

Can I parse data from multiple hosts?

Not yet.  Run the script multiple times and generate multiple reports.