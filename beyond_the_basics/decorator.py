

# takes a callable, returns a callable
# they replace, enhance, or modify a function without replacing the original
@my_decorator
def my_function(x, y):
    return x + y


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap


@escape_unicode
def northern_city():
    return 'TromsÉ'

