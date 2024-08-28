class Signature(object):
    """Secondary metabolite signature"""

    def __init__(self, name, _type, description, cutoff, path):
        self.name = name
        self.type = _type
        self.description = description
        self.cutoff = cutoff
        self.path = path
