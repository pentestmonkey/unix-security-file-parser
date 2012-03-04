import upc.utils
from optparse import OptionParser
from optparse import OptionGroup
import sys

def parseOptions():
    upc.utils.print_banner()
    usage = "%s ( file-options | bulk-options ) -o report-file-stem\n\nA tool for identifying security problems in Unix configuration files.\nIt is assumed that you have copied the relevant files from the target system\nto the system you are running unix_security_file_parser from." % (sys.argv[0])

    parser  = OptionParser(usage = usage, version = upc.utils.get_version())
    fileopts = OptionGroup(parser, "file-options", "At least one of these to indicate what to examine")
    bulkopts = OptionGroup(parser, "bulk-options", "Automatically guess which files are which from their name")
    report  = OptionGroup(parser, "report-options", "Reporting options")

    fileopts.add_option("-p", "--passwd",      dest = "passwd_file",      default = False, help = "/etc/passwd file")
    fileopts.add_option("-g", "--group",       dest = "group_file",       default = False, help = "/etc/group file")
    fileopts.add_option("-s", "--shadow",      dest = "shadow_file",      default = False, help = "/etc/shadow file")
    fileopts.add_option("-S", "--sudoers",     dest = "sudoers_file",     default = False, help = "/etc/sudoers file")
    fileopts.add_option("-P", "--perms",       dest = "perms_file",       default = False, help = "Output of: find / -ls")
    fileopts.add_option("-H", "--sshd_config", dest = "sshd_config_file", default = False, help = "/etc/ssh/sshd_config")
    fileopts.add_option("-u", "--upc",         dest = "upc_file",         default = False, help = "Output of: unix-privesc-check standard|detailed")
    fileopts.add_option("-i", "--ifconfig",    dest = "ifconfig_file",    default = False, help = "Output of: ifconfig -a")

    bulkopts.add_option("-d", "--directory",   dest = "directory",   help = "Guess files to parse in given directory (don't use /!)")
    bulkopts.add_option("-t", "--tarball",     dest = "tarball",     help = "Unpack tar ball and guess files to parse")

    report.add_option("-o", "--report_file_stem",  dest = "report_file_stem",  default = False, help = "Filename stem for txt, html report files")

    parser.add_option_group(fileopts)
    parser.add_option_group(report)

    (options, args) = parser.parse_args()

    if not options.report_file_stem:
        print "[E] Specify report filename stem, e.g. '-o report-myhost'.  -h for help."
        sys.exit()

    fileopt_used = 0
    bulkopt_used = 0
    
    if options.group_file or options.ifconfig_file or options.passwd_file or options.shadow_file or options.sudoers_file or options.perms_file or options.sshd_config_file or options.upc_file:
        fileopt_used = 1
    
    if options.directory or options.tarball:
        bulkopt_used = 1
    
    if not (fileopt_used ^ bulkopt_used):
        print "[E] Specify something to look at.  At least one of: -p, -s, -S, -P, -H, -c *OR* one of: -d, -t.  -h for help."
        sys.exit()

    return options
