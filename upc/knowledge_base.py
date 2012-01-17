

class knowledge_base():
    def __init__(self):
        self.sections = {}
        self.data_type = {}
        self.name_dict = {}
        self.ulists = {}
        self.strings = {}
        
    def register_section(self, name):
        if not name in self.get_sections():
            self.sections[name] = knowledge_base()
        return self.sections[name]
            
    def get_sections(self):
        return self.sections.keys()
    
    def register_unique_list(self, name):
        if not name in self.get_names():
            self._add_ulist(name)
            
    def register_string(self, name):
        if not name in self.get_names():
            self._add_string(name)
    
    def _add_ulist(self, name):
        self._register_data_type("ulist", name)
        self.ulists[name] = []
    
    def _add_string(self, name):
        self._register_data_type("string", name)
        self.strings[name] = []
    
    def get_data_type(self, name):
        return self.data_type[name]
    
    def add_name(self, name):
        self.name_dict[name] = 1
        
    def _register_data_type(self, datatype, name):
        self.add_name(name)
        self.data_type[name] = datatype
    
    def get_names(self):
        return self.name_dict.keys()
        
    def get_ulists(self):
        return self.utists.keys()
    
    def get_strings(self):
        return self.strings.keys()
    
    def add_info(self, name, value):
        data_type = self.get_data_type(name)
        
        if data_type == "ulist":
                self.add_info_ulist(name, value)
                
        if data_type == "string":
                self.add_info_string(name, value)
                
    def add_info_ulist(self, name, value):
        self.ulists[name].append(value)
        self.ulists[name] = list(set(self.ulists[name]))
        
    def add_info_string(self, name, value):
        self.strings[name] = value

    def get_info(self, name):
        data_type = self.get_data_type(name)

        if data_type == "ulist":
            return self.get_ulist(name)
                
        if data_type == "string":
            return self.get_string(name)
        
    def get_ulist(self, name):
        return self.ulists[name]
    
    def get_string(self, name):
        return self.string[name]

        