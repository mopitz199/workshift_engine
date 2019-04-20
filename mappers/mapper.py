class Mapper(object):
    """
    This class allow us to mapper any object.

        * obj: Is the object that we want to map
        * attr_mapping: Is a dict that has the map to access to an attr of the obj, from a different name

    For get an attr, it will try to get thet attr directly in the mapper and if it can't it will try to get it from the obj

    For set an attr, it will try to set the attr in the obj, otherwise it will set it in the mapper
    """

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