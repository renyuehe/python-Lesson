
'''
class object:
    def __delattr__(self, *args, **kwargs): !!
    def __dir__(self, *args, **kwargs):
    def __eq__(self, *args, **kwargs):
    def __format__(self, *args, **kwargs): !!
    def __getattribute__(self, *args, **kwargs): !!
    def __ge__(self, *args, **kwargs): !!
    def __gt__(self, *args, **kwargs):

    def __hash__(self, *args, **kwargs):

    def __init_subclass__(self, *args, **kwargs): !!

    def __init__(self):  # known special case of object.__init__

    def __le__(self, *args, **kwargs):  !!

    def __lt__(self, *args, **kwargs):

    @staticmethod  # known case of __new__
    def __new__(cls, *more):  # known special case of object.__new__ !!

    def __ne__(self, *args, **kwargs): !!

    def __reduce_ex__(self, *args, **kwargs):!!

    def __reduce__(self, *args, **kwargs): !!

    def __repr__(self, *args, **kwargs): !!

    def __setattr__(self, *args, **kwargs): !!

    def __sizeof__(self, *args, **kwargs): !!

    def __str__(self, *args, **kwargs):

    @classmethod  # known case
    def __subclasshook__(cls, subclass):  # known special case of object.__subclasshook__ !!!!!!!!!
'''


print(help(object))
