import re
from upc.fsobj import fsobj

class parser:
    def __init__(self):
        pass
    
    def order_files(self):
        pass
    
    def auto_parse(self):
        pass
    
    # opts can contain:
    #   remove_comments: "^#"
    # 
    # returns multiline string
    def slurpfile(self, filename, opts):
        print "[D] opening: %s" % filename
        f = open(filename, 'r')
        lines = f.readlines()
        
        if "remove_comments" in opts.keys():
            newlines = []
            for line in lines:
                if not re.search(opts["remove_comments"], line):
                    newlines.append(line)
                lines = newlines
                
        if "remove_blanklines" in opts.keys() and opts["remove_blanklines"]:
            newlines = []
            for line in lines:
                if not re.search("^\s*$", line):
                    newlines.append(line)
            lines = newlines

        if "trim" in opts.keys() and opts["trim"]:
            newlines = []
            for line in lines:
                newlines.append(line.strip())
            lines = newlines

        if "key_values" in opts.keys() and opts["key_values"]:
            newlines = []
            for line in lines:
                m = re.search("^\s*(\S+)\s+(.*?)\s*$", line) 
                if m:
                    newlines.append([m.group(1), m.group(2)])
            lines = newlines
                         
        return lines
    
    def query_perms(self, filename, opts):
        print "[D] opening: %s" % filename
        f = open(filename, 'r')
        
        # TODO move this somewhere
        regexp = {}
        regexp['world_writeable'] = '\s.[r-][w-][xsS][r-][w-][xsS][r-]w[xtT]\s'
        regexp['world_readable']  = '\s.[r-][w-][xsS][r-][w-][xsS]r[w-][xtT]\s'
        regexp['file']            = '\s-[r-][w-][xsS][r-][w-][xsS][r-][w-][xtT]\s'
        regexp['directory']       = '\sd[r-][w-][xsS][r-][w-][xsS][r-][w-][xtT]\s'
        regexp['sticky']          = '\s.[r-][w-][xsS][r-][w-][xsS][r-][w-][tT]\s'
        regexp['suid']            = '\s.[r-][w-][sS][r-][w-][xsS][r-][w-][xtT]\s'
        regexp['sgid']            = '\s.[r-][w-][xsS][r-][w-][sS][r-][w-][xtT]\s'
        
        eregexp = {}
        eregexp['min_size'] = '\d+\s+\d+\s+..........\s+\d+\s+\S+\s+\S+\s+(\d+)\s+?\S+\s+\S+\s+\S+\s+/'

        allowed_opts = ["matches", "ignore", "min_size"]        
        # This odd-looking construction is apparently quite fast
        # http://effbot.org/zone/readline-performance.htm
        while 1:
            lines = f.readlines(100000)
            if not lines:
                break
            for line in lines:
                # We need this regexp to avoid creating objects unnecessarily
                matched = 1
                
                # TODO check that one "matches" was passed at least
                # TODO check that matches are valid
                for opt in opts.keys():
                    if matched and opt in allowed_opts:
                        if matched and opt == "matches":
                            for s in opts['matches']:
                                m = re.search(regexp[s], line)
                                if not m:
                                    matched = 0
                                    break
                        
                        if matched and opt == "ignore":
                            for s in opts['ignore']:
                                m = re.search(regexp[s], line)
                                if m:
                                    matched = 0
                                    break

                        if matched and opt == "min_size":
                            #print "[D] min"
                            m = re.search(eregexp[opt], line)
                            if m:
                                size = m.group(1)
                                if int(size) < int(opts["min_size"]):
                                    matched = 0
                                    break

                if matched:
                    fso = fsobj();
                    r = fso.parse_from_find_line(line) 
                    if r:
                        yield fso
    
    def add_issue(self, title):
        print "[D] Added issue %s" % title
        pass
    