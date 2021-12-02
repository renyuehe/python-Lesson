''''''

'''
1. inspect.getclasstree(classes[, unique])

2. inspect.getargspec(func)

3. inspect.getargvalues(frame)

4. inspect.formatargspec(args[, varargs, varkw, defaults, formatarg, formatvarargs, formatvarkw, formatvalue, join])

5. inspect.formatargvalues(args[, varargs, varkw, locals, formatarg, formatvarargs, formatvarkw, formatvalue, join])

6. inspect.getmro(cls)： 元组形式返回cls类的基类（包括cls类），以method resolution顺序;通常cls类为元素的第一个元素

7. inspect.getcallargs(func[, *args][, **kwds])：将args和kwds参数到绑定到为func的参数名；对bound方法，也绑定第一个参数（通常为self）到相应的实例；返回字典，对应参数名及其值；

>>> from inspect import getcallargs
>>> def f(a, b=1, *pos, **named):
...     pass
>>> getcallargs(f, 1, 2, 3)
{'a': 1, 'named': {}, 'b': 2, 'pos': (3,)}
>>> getcallargs(f, a=2, x=4)
{'a': 2, 'named': {'x': 4}, 'b': 1, 'pos': ()}
>>> getcallargs(f)
Traceback (most recent call last):
...
TypeError: f() takes at least 1 argument (0 given)

'''