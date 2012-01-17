from upc.parser.parser import parser

class sshd_config(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb_local = kb.register_section("sshd_config")
		self.kb_global = kb
		self.kb_local.register_string("filename")
		self.kb_local.add_info("filename", filename)
		
		# It's not correct to treat sshd_config as a list of key-value pairs.  
		# It's close enough for a basic audit, though.
		key_values = self.slurpfile(filename, {"remove_comments": "^#", "key_values": 1, "remove_blanklines": 1})
		self.kb_local.register_unique_list("ssh_ports")
		self.kb_local.register_unique_list("ssh_ips")
		
		directives_used = {}
		
		for kv in key_values:
			k = kv[0]
			v = kv[1]
			
			# remember which directives have been used
			directives_used[k] = 1
			
			if k == "Port":
				for port in v.split(","):
					self.kb_local.add_info("ssh_ports", port)
				
		if not "Port" in directives_used.keys():
			self.report.get_by_id("UPC501").add_supporting_data('hostname', [self.kb_global])
		else:
			ports = self.kb_local.get_info("ssh_ports")
			if "22" in ports:
				self.report.get_by_id("UPC501").add_supporting_data('hostname', [self.kb_global])
				self.add_issue("UPC501")
		
		if not "AllowUsers" in directives_used.keys() and not "AllowGroups" in directives_used.keys():
			self.report.get_by_id("UPC503").add_supporting_data('hostname', [self.kb_global])
			
		if not "Match" in directives_used.keys():
			self.report.get_by_id("UPC504").add_supporting_data('hostname', [self.kb_global])
