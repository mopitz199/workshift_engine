class Mapper(object):

    def __init__(self, obj, attr_mapping):
        self.attr_mapping = attr_mapping
        self.obj = obj

    def __getattr__(self, attr):
        attr_name = self.attr_mapping.get(attr, attr)
        return getattr(self.obj, attr_name)
    
    def __setattr__(self, attr, val):
        if attr in ['attr_mapping', 'obj']:
            return super(Mapper, self).__setattr__(attr, val)
        else:
            mapping = self.attr_mapping
            attr_name = mapping.get(attr, attr)
            if hasattr(self.obj, attr_name):
                return setattr(self.obj, attr_name, val)
            else:
                return super(Mapper, self).__setattr__(attr_name, val)

                