__author__ = 'Administrator'


def longToInt(value):
    if value > 2147483647:
        return (value & (2 ** 31 - 1))
    else:
        return value


if __name__ == "__main__":
    a=long(1L)
    print a,type(a)