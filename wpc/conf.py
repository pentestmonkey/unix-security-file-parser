# Not a class, just a bunch of constants

version = None

# Used to store a data structure representing the issues we've found
# We use this to generate the report
issues = {}

issue_template = {
    # 
    # These issues correspond ot issues from unix-privesc-check.  UPC000-UPC499 reserved for this.
    #                  
    'UPC001': {
       'title': "UPC001: Files and Directories writeable by other users",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC002': {
       'title': "UPC002: Group-writeable Files or Directories",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC003': {
       'title': "UPC003: World-writeable Files or Directories (but sticky bit set)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC004': {
       'title': "UPC004: World-writeable Files or Directories",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC005': {
       'title': "UPC005: Files readable by other users",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC006': {
       'title': "UPC006: Files readable by other groups",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC007': {
       'title': "UPC007: Files world-readable",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC008': {
       'title': "UPC008: /etc/passwd allows external authentcation",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC009': {
       'title': "UPC009: NIS is used for authentication on this system",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC010': {
       'title': "UPC010: LDAP is used for authentication on this system",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC011': {
       'title': "UPC011: NIS is used for authentication on this system",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC012': {
       'title': "UPC012: LDAP is used for authentication on this system",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC013': {
       'title': "UPC013: There seem to be some password hashes in /etc/passwd",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC014': {
       'title': "UPC014: The following accounts have no password:",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC015': {
       'title': "UPC015: User doesn't have a password",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC016': {
       'title': "UPC016: User doesn't have a password",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC017': {
       'title': "UPC017: Sudo is configured - Manually check nothing unsafe is allowed",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC018': {
       'title': "UPC018: Some users can use sudo without a password",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC019': {
       'title': "UPC019: Postgres trust configured in pg_hba.conf",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC020': {
       'title': "UPC020: Can connect to local postgres database as \\",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC021': {
       'title': "UPC021: Can connect to local postgres database as \\",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC022': {
       'title': "UPC022: This system is an NFS client.  Check for nosuid and nodev options.",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC023': {
       'title': "UPC023: SetUID shell script may be vulnerable to race attacks",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC024': {
       'title': "UPC024: Cleartext subversion passsword file",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC025': {
       'title': "UPC025: Encrypted private SSH key found",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC026': {
       'title': "UPC026: Unencrypted private SSH key found",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC027': {
       'title': "UPC027: Public SSH Key found",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC028': {
       'title': "UPC028: SSH agents running",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC029': {
       'title': "UPC029: SSH Agent has keys loaded",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC030': {
       'title': "UPC030: GPG agents running",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC031': {
       'title': "UPC031: No NX",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC032': {
       'title': "UPC032: No NX logging",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC033': {
       'title': "UPC033: Auditing not enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC034': {
       'title': "UPC034: No NX",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC035': {
       'title': "UPC035: NX set to logging only",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC036': {
       'title': "UPC036: No ASLR",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC037': {
       'title': "UPC037: Conservative ASLR",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC038': {
       'title': "UPC038: mmap allows map to 0",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC039': {
       'title': "UPC039: SELinux does not enforce",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC040': {
       'title': "UPC040: NX not enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC041': {
       'title': "UPC041: SSP not enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC042': {
       'title': "UPC042: SSP not enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                  
                  
    # 
    # Other issues start here
    #                  
    'UPC501': {
       'title': "Default SSH Port",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'writable_progs': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC502': {
       'title': "Some Users Do Not Require a Password To Use Sudo",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC503': {
       'title': "SSH Users Not Whitelisted",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC504': {
       'title': "SSH Match Rules Not Used",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'TODO': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC505': {
       'title': "Sudo Allow Some Users To Execute Any Command",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC506': {
       'title': "Sudo Allows The Use of Potentially Dangerous Commands",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'TODO': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC507': {
       'title': "User has blank password in /etc/passwd",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC508': {
       'title': "User has unshadowed password in /etc/passwd",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC509': {
       'title': "User has shell defined in /etc/passwd",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC510': {
       'title': "User has blank password in /etc/shadow",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC511': {
       'title': "Account uses unknown hashing algorithm in /etc/shadow",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC512': {
       'title': "Multiple hashing algorithms used in /etc/shadow",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                  
    'UPC513': {
       'title': "World Writeable Directory (not sticky bit)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC514': {
       'title': "World Writeable Directory (sticky bit set)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC515': {
       'title': "SUID Program",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC516': {
       'title': "SGID Program",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC517': {
       'title': "SGID Directory",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC518': {
       'title': "World Writeable File",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC519': {
       'title': "World Readable Big File",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                  
    'UPC5': {
       'title': "TODO",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'TODO': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC5': {
       'title': "TODO",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'TODO': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },



}
