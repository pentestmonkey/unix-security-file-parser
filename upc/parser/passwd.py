from upc.parser.parser import parser
import re

class passwd(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb_local = kb.register_section("passwd")
		self.kb_global = kb
		self.kb_local.register_string("filename")
		self.kb_local.add_info("filename", filename)
		
		lines = self.slurpfile(filename, {"remove_blanklines": 1, "trim": 1})
		
		for line in lines:
			fields = line.split(":")
			# tomcat6:x:134:140::/usr/share/tomcat6:/bin/false
			# field 0: user 
			# field 1: pass
			# field 2: uid
			# field 3: gid
			# field 4: ?
			# field 5: homedir
			# field 6: shell
			
			# Blank password
			if fields[1] == "":
				self.report.get_by_id("UPC507").add_supporting_data('text_line', [self.kb_global, line])
				
			# Password not shadowed
			if fields[1] != "x":
				self.report.get_by_id("UPC508").add_supporting_data('text_line', [self.kb_global, line])
				
			# User has shell
			if fields[6] != "/bin/false":
				self.report.get_by_id("UPC509").add_supporting_data('text_line', [self.kb_global, line])
				
