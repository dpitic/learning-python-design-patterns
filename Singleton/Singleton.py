class Singleton(object):
    '''Implementation of a Singleton class.'''
    def __new__(cls):
        '''Return a new instance on the first call and the same singleton
        instance thereafter.'''
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
