from upc.parser.parser import parser
import re

class sudoers(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb_local = kb.register_section("sudoers")
		self.kb_global = kb
		self.kb_local.register_string("filename")
		self.kb_local.add_info("filename", filename)
		
		lines = self.slurpfile(filename, {"remove_comments": "^#", "remove_blanklines": 1, "trim": 1})
		
		for line in lines:
			if re.search("^\S+\s.*NOPASSWD:", line):
				self.report.get_by_id("UPC502").add_supporting_data('text_line', [self.kb_global, line])
				
			if re.search("^\S+\sALL=\(ALL\)\s+ALL", line):
				self.report.get_by_id("UPC505").add_supporting_data('text_line', [self.kb_global, line])
				
			if re.search("=.*\bchown\b", line):
				self.report.get_by_id("UPC506").add_supporting_data('text_line', [self.kb_global, line])

