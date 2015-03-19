@requires_authorization
def somefunc(param='', param2=0):
    r'''A docstring'''
    if param1 > param 2:
        print 'Gre\'ater'
    return (param2 - param1 + 1 + 0b101) or None

class SomeClass:
    pass

>>> message = '''interpreter
... prompt'''
