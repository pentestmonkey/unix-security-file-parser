from upc.parser.parser import parser
import re

class shadow(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb_local = kb.register_section("shadow")
		self.kb_global = kb
		self.kb_local.register_string("filename")
		self.kb_local.add_info("filename", filename)
		
		lines = self.slurpfile(filename, {"remove_blanklines": 1, "trim": 1})
		
		crypt_std_des_used = 0
		crypt_ext_des_used = 0
		md5_hash_used = 0
		blowfish2_used = 0
		blowfish2a_used = 0
		sha256_used = 0
		sha512_used = 0
				
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
				self.report.get_by_id("UPC510").add_supporting_data('text_line', [self.kb_global, line])
				
			# Record which hash types are used
			elif re.search("^[\./0-9A-Za-z]{9}$", fields[1]):
				crypt_std_des_used = 1
				
			elif re.search("^_", fields[1]):
				crypt_ext_des_used = 1
				
			elif re.search("^\$1\$", fields[1]):
				md5_hash_used = 1
				
			elif re.search("^\$2\$", fields[1]):
				blowfish2_used = 1
				
			elif re.search("^\$2a\$", fields[1]):
				blowfish2a_used = 1
				
			elif re.search("^\$5\$", fields[1]):
				sha256_used = 1
				
			elif re.search("^\$6\$", fields[1]):
				sha512_used = 1
				
			elif fields[1] != "!" and fields[1] != "*":
				self.report.get_by_id("UPC511").add_supporting_data('text_line', [self.kb_global, line])
				
		# Mixture of hashes used
		if crypt_std_des_used + crypt_ext_des_used + md5_hash_used + blowfish2_used + blowfish2a_used + sha256_used + sha512_used > 1:
			self.report.get_by_id("UPC512").add_supporting_data('none', [self.kb_global])
				
