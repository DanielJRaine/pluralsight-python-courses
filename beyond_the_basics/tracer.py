import functools


class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap

tracer = Trace()


# decorators are applied in reverse order that they are written
@tracer
def rotate_list(l):
    return l[1:] + [l[0]]
