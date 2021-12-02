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