import ctypes

class PyObject(ctypes.Structure):

    _fields_ = [('ob_refcnt', ctypes.c_ssize_t), ('ob_type', ctypes.c_void_p)]

Object = ctypes.POINTER(PyObject)
PyCFunction = ctypes.CFUNCTYPE(ctypes.py_object, Object, Object)

class PyMethodDef(ctypes.Structure):

    _fields_ = [('ml_name', ctypes.c_char_p), ('ml_meth', PyCFunction),

            ('ml_flags', ctypes.c_int), ('ml_doc', ctypes.c_char_p)]

_MethodDef = ctypes.POINTER(PyMethodDef)

class PyBuiltinObject(ctypes.Structure):

    _fields_ = [('ob_refcnt', ctypes.c_ssize_t), ('ob_type', ctypes.c_void_p), ('m_ml', _MethodDef), ('m_self', Object),

                                ('m_module', Object)]

BuiltinObject = ctypes.POINTER(PyBuiltinObject)



class Alloc(object):

    __slots__ = map('x{}'.format, range((ctypes.sizeof(PyBuiltinObject)-ctypes.sizeof(PyPbject))/ctypes.sizeof(ctypes.c_void_p)))

def alloc_builtin():

    obj = Alloc()

    stru = ctypes.cast(id(obj), BuiltinObject)

    stru.contents.ob_type = ctypes.c_void_p(id(type(cmp)))

    return (obj, stru)