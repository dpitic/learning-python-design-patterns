class Singleton(object):
    '''Implementation of a Singleton class.'''
    def __new__(cls):
        '''Return a new instance or the singleton instance if it exists.'''
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
