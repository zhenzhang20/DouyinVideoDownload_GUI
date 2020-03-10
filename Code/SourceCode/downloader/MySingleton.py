class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
            cls._inst_has_init = False
        return cls._inst

    def __init__(self):
        if not self._inst_has_init:
            self.init()
            self._inst_has_init = True

    def init(slef):
        pass

