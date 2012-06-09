from upc.parser.parser import parser

class sysctl(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		# It's not correct to treat sysctl_config as a list of key-value pairs.  
		# It's close enough for a basic audit, though.
		key_values = self.slurpfile(filename, {"remove_comments": "^#", "key_values": 1, "remove_blanklines": 1})
		
		
		for kv in key_values:
			k = kv[0]
			v = kv[1]
			print "Processing: %s = %s" % (k, v)
			if k == "kernel.sysrq" and v == "1":
				self.report.get_by_id("UPC559").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])

			if k == "kernel.modules_disabled" and v == "0":
				self.report.get_by_id("UPC560").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
		
			if k == "vm.mmap_min_addr" and v == "0":
				self.report.get_by_id("UPC561").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])

			if k == "kernel.kptr_restrict" and v == "0":
				self.report.get_by_id("UPC562").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
