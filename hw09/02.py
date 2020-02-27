from inspect import isfunction


class Pep8Warrior:
    def __new__(cls, *args, **kwargs):
        name, parents, attrs = args
        new_name = name.title().replace('_', '')
        new_attrs = {}
        for attr, value in attrs.items():
            if attr.startswith('_'):
                new_attrs[attr] = value
            elif isfunction(value):
                new_attrs[attr.lower()] = value
            elif callable(value):
                new_attrs[attr.title().replace('_', '')] = value
            else:
                new_attrs[attr.upper()] = value
        return type(new_name, parents, new_attrs)


class MyClass(metaclass=Pep8Warrior):
    def __init__(self, _first, second):
        self._first = _first
        self.second = second

    def get_something(self):
        pass

    def one_more(cls):
        pass

    def nothing(gig):
        pass
