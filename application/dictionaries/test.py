from numpy.f2py.auxfuncs import throw_error
try:
    a="s"
    print(int(a))
except Exception:
    print(str(Exception))