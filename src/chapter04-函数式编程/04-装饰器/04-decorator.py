#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#再思考一下能否写出一个@log的decorator，使它既支持：
#@log
#def f():
#    pass

#又支持：
#@log('execute')
#def f():
#    pass

def log(arg):
    if not isinstance(arg,str):
       func=arg
       @functools.wraps(func)
       def wrapper(*args, **kw):
            print('begin call %s()\n' % (func.__name__))
            x=func(*args, **kw)
            print('end call %s()\n' % (func.__name__))
            return x
       return wrapper
    else:
       text=arg
       def decorator(func):
         @functools.wraps(func)
         def wrapper(*args, **kw):
            print('begin %s %s()\n' % (text, func.__name__))
            x=func(*args, **kw)
            print('end %s %s()\n' % (text, func.__name__))
            return x
         return wrapper
       return decorator

