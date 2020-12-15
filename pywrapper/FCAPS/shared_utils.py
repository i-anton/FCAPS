from enum import Enum

class NoValue(Enum):
    """ Helper for enums """
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)

class ModuleSetting:
    def __init__(self, module_type: str, name: str):
        self.name = name
        self.module_type = module_type
        self.params = {}

    def to_dict(self):
        return {
            "Type": self.module_type,
            "Name": self.name,
            "Params": self.params
        }