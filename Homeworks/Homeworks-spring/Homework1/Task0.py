def sum(a, b):
    try:
        result = a + b
        if type(a) is int and type(b) is int:
            if (a >= 0) and (b >= 0):
                return result
            else:
                raise ValueError
        else:
            raise TypeError
    except TypeError:
        raise TypeError

