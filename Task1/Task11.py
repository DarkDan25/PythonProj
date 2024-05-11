class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def send(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'F'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == "E":
            self.state = "C"
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 9
        if self.state == 'H':
            self.state = 'B'
            return 11
        raise MealyError('send')

    def swap(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'D':
            self.state = 'F'
            return 5
        if self.state == "E":
            self.state = "F"
            return 6
        if self.state == "G":
            self.state = "H"
            return 10
        raise MealyError('swap')

    def code(self):
        if self.state == 'E':
            self.state = 'A'
            return 8
        raise MealyError('code')


def main():
    return StateMachine()


def raises(function, error):
    output = None
    try:
        output = function()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.send() == 0
    assert o.swap() == 1
    assert o.swap() == 2
    raises(lambda: o.code(), MealyError)
    assert o.send() == 4
    assert o.code() == 8
    assert o.send() == 0
    assert o.swap() == 1
    assert o.send() == 3
    raises(lambda: o.swap(), MealyError)
    assert o.send() == 9
    assert o.swap() == 10
    assert o.send() == 11
    assert o.swap() == 1
    assert o.swap() == 2
    assert o.send() == 4
    assert o.send() == 7
    raises(lambda: o.code(), MealyError)
    o = main()
    assert o.send() == 0
    raises(lambda: o.send(), MealyError)
    assert o.swap() == 1
    assert o.swap() == 2
    raises(lambda: o.code(), MealyError)
    assert o.send() == 4
    assert o.code() == 8
    assert o.send() == 0
    assert o.swap() == 1
    assert o.swap() == 2
    assert o.swap() == 5
    assert o.send() == 9
    assert o.swap() == 10
    assert o.send() == 11
    assert o.swap() == 1
    raises(lambda: o.code(), MealyError)
    assert o.send() == 3
    assert o.send() == 9
    assert o.swap() == 10
    assert o.send() == 11
    assert o.swap() == 1
    assert o.swap() == 2
    assert o.send() == 4
    assert o.swap() == 6
