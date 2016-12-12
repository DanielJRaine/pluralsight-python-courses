# def hypervolume(*lengths):
#     i = iter(lengths)
#     v = next(i)
#     for length in i:
#         v *= length
#     return v


# good form for a positive minimum bound for args number
def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


# (positional, args, *then_star_args, mandatory=keyword, args, **lastly_kwargs)
# default args have their own ordering rules:
# mandatory default args must be passed before optional args at the call site 
def func(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))


def tag(name, **attributes):
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result
